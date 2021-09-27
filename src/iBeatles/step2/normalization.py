from qtpy.QtWidgets import QFileDialog, QApplication, QListWidgetItem
import os
import shutil
import numpy as np
import logging

from NeuNorm.normalization import Normalization as NeuNormNormalization
from NeuNorm.roi import ROI

from ..step2.roi_handler import Step2RoiHandler
from ..step2.plot import Step2Plot
from ..utilities.file_handler import FileHandler
from ..step1.time_spectra_handler import TimeSpectraHandler
from ..utilities.status_message_config import StatusMessageStatus, show_status_message


class Normalization(object):
    coeff_array = 1  # ob / sample of ROI selected

    def __init__(self, parent=None):
        self.parent = parent

    def run_and_export(self):

        logging.info("Running and exporting normalization:")

        # ask for output folder location
        sample_folder = self.parent.data_metadata['sample']['folder']
        sample_name = os.path.basename(os.path.dirname(sample_folder))
        default_dir = os.path.dirname(os.path.dirname(sample_folder))
        output_folder = str(
            QFileDialog.getExistingDirectory(caption="Select Where the Normalized folder will be created...",
                                             directory=default_dir,
                                             options=QFileDialog.ShowDirsOnly))

        if not output_folder:
            logging.info(" No output folder selected, normalization stopped!")
            return

        logging.info(f" output folder selected: {output_folder}")
        full_output_folder = os.path.join(output_folder, sample_name + "_normalized")
        FileHandler.make_or_reset_folder(full_output_folder)
        logging.info(f" full output folder will be: {full_output_folder}")

        self.running_normalization(output_folder=full_output_folder)

        # # perform normalization on all images selected
        # self.normalize_full_set(output_folder=output_folder, base_folder_name=sample_name)

    def normalize_full_set(self, output_folder='', base_folder_name=''):

        output_folder = os.path.join(output_folder, base_folder_name + '_normalized')
        self.parent.time_spectra_normalized_folder = output_folder
        if os.path.exists(output_folder):
            # if folder does exist already, we first remove it
            shutil.rmtree(output_folder)
        os.mkdir(output_folder)
        self.parent.ui.normalized_folder.setText(base_folder_name + '_normalized')
        self.parent.data_metadata['normalized']['folder'] = output_folder

        # get range we want to normalize
        range_to_normalize = self.parent.range_files_to_normalized_step2['file_index']

        # get short list of data file names
        # list_samples_names = self.parent.data_files['sample']
        list_samples_names = [os.path.basename(_file) for _file in self.parent.list_files['sample']]

        data = self.parent.data_metadata['sample']['data']
        array_coeff = self.coeff_array
        ob = self.parent.data_metadata['ob']['data']

        if range_to_normalize != []:
            from_index = range_to_normalize[0]
            to_index = range_to_normalize[1]+1

            list_samples_names = list_samples_names[from_index: to_index]
            data = data[from_index: to_index]
            array_coeff = array_coeff[from_index: to_index]
            ob = ob[from_index: to_index]

        # progress bar
        self.parent.eventProgress.setMinimum(0)
        self.parent.eventProgress.setMaximum(len(list_samples_names) - 1)
        self.parent.eventProgress.setValue(0)
        self.parent.eventProgress.setVisible(True)
        QApplication.processEvents()

        # list of file name (short)
        normalized_array = []
        normalized_file_name = []
        normalized_sum_counts = []
        for _index_file, _short_file in enumerate(list_samples_names):
            _long_file_name = os.path.join(output_folder, _short_file)
            _data = data[_index_file]
            _ob = ob[_index_file]
            _coeff = array_coeff[_index_file]

            normalized_data = self.perform_single_normalization_and_export(data=_data,
                                                                           ob=_ob,
                                                                           coeff=_coeff,
                                                                           output_file_name=_long_file_name)
            normalized_data[np.isnan(normalized_data)] = 0
            normalized_array.append(normalized_data)
            _sum = np.nansum(normalized_data)
            normalized_sum_counts.append(_sum)
            normalized_file_name.append(_short_file)

            self.parent.eventProgress.setValue(_index_file + 1)
            QApplication.processEvents()

        self.parent.data_metadata['normalized']['data'] = normalized_array
        # self.parent.data_files['normalized'] = normalized_file_name
        self.parent.list_files['normalized'] = normalized_file_name

        # tof array
        tof_array = self.parent.data_metadata['time_spectra']['data']

        if range_to_normalize != []:
            from_index = range_to_normalize[0]
            to_index = range_to_normalize[1] + 1
            tof_array = tof_array[from_index: to_index]

        short_tof_file_name = '{}_Spectra.txt'.format(base_folder_name)
        tof_file_name = os.path.join(output_folder, short_tof_file_name)
        tof_array = list(zip(tof_array, normalized_sum_counts))
        FileHandler.make_ascii_file(data=tof_array, output_file_name=tof_file_name, sep='\t')
        self.parent.ui.time_spectra_folder_2.setText(os.path.basename(output_folder))
        self.parent.ui.time_spectra_2.setText(short_tof_file_name)

        o_time_handler = TimeSpectraHandler(parent=self.parent)
        o_time_handler.load()
        o_time_handler.calculate_lambda_scale()
        tof_array = o_time_handler.tof_array
        lambda_array = o_time_handler.lambda_array
        self.parent.data_metadata['time_spectra']['normalized_data'] = tof_array
        self.parent.data_metadata['time_spectra']['normalized_lambda'] = lambda_array

        # populate normalized tab
        list_ui = self.parent.ui.list_normalized
        list_ui.clear()
        for _row, _file in enumerate(normalized_file_name):
            _item = QListWidgetItem(_file)
            list_ui.insertItem(_row, _item)

        self.parent.eventProgress.setVisible(False)

    def perform_single_normalization_and_export(self, data=[], ob=[], coeff=[], output_file_name=''):

        ob = ob.astype(float)
        data = data.astype(float)
        coeff = coeff.astype(float)

        # sample / ob
        ob[ob == 0] = np.NAN
        _step1 = np.divide(data, ob)
        _step1[_step1 == np.NaN] = 0
        _step1[_step1 == np.inf] = 0

        # _term1 * coeff
        _data = _step1 * coeff

        FileHandler.make_fits(data=_data, filename=output_file_name)

        return _data

    def running_normalization(self, output_folder=None):
        logging.info(" running normalization!")
        _data = self.parent.data_metadata['sample']['data']
        _ob = self.parent.data_metadata['ob']['data']

        # no data, nothing to do
        if not _data:
            print("I shouldn't be able to see this!")
            return

        # check if roi selected or not
        o_roi_handler = Step2RoiHandler(parent=self.parent)
        try:  # to avoid valueError when row not fully filled
            list_roi_to_use = o_roi_handler.get_list_of_background_roi_to_use()
        except ValueError:
            logging.info(" Error raised when retrieving the background ROI!")
            return

        logging.info(f" Background list of ROI: {list_roi_to_use}")

        # if just sample data
        if not _ob:
            self.normalization_only_sample_data(_data, list_roi_to_use, output_folder)
        else:
            self.normalization_sample_and_ob_data(_data, _ob, list_roi_to_use)

    def normalization_only_sample_data(self, data, list_roi, output_folder):

        logging.info(" running normalization with only sample data ...")

        show_status_message(parent=self.parent,
                            message="Loading data ...",
                            status=StatusMessageStatus.working)
        o_norm = NeuNormNormalization()
        o_norm.load(data=data)
        show_status_message(parent=self.parent,
                            message="Loading data ... Done!",
                            status=StatusMessageStatus.working,
                            duration_s=5)

        list_roi_object = []
        for _roi in list_roi:
            o_roi = ROI(x0=int(_roi[0]),
                        y0=int(_roi[1]),
                        width=int(_roi[2]),
                        height=int(_roi[3]))
            list_roi_object.append(o_roi)

        show_status_message(parent=self.parent,
                            message="Running normalization ...",
                            status=StatusMessageStatus.working)
        o_norm.normalization(roi=list_roi_object,
                             use_only_sample=True)
        show_status_message(parent=self.parent,
                            message="Running normalization ... Done!",
                            status=StatusMessageStatus.working,
                            duration_s=5)

        show_status_message(parent=self.parent,
                            message="Exporting normalized files ...",
                            status=StatusMessageStatus.working)
        o_norm.export(folder=output_folder)
        show_status_message(parent=self.parent,
                            message="Exporting normalized files ... Done!",
                            status=StatusMessageStatus.working,
                            duration_s=5)

        logging.info(" running normalization with only sample data ... Done!")

    def normalization_sample_and_ob_data(self, data, ob, list_roi):
        pass
        # if list_roi == []:
        #     self.normalization_sample_and_ob_data_without_roi(data, ob, live_plot)
        # else:
        #     self.normalization_sample_and_ob_data_with_roi(data, ob, list_roi, live_plot)

    def normalization_sample_and_ob_data_without_roi(self, data, ob, live_plot):
        o_plot = Step2Plot(parent=self.parent)
        o_plot.clear_counts_vs_file()

    def normalization_sample_and_ob_data_with_roi(self, data, ob, list_roi, live_plot):
        o_plot = Step2Plot(parent=self.parent, normalized=data)
        self.calculate_coeff(sample=data, ob=ob, list_roi=list_roi)
        # sample_integrated = o_plot.calculate_mean_counts(data)
        # ob_integrated = o_plot.calculate_mean_counts(ob)
        # ratio_array = sample_integrated / ob_integrated
        # array_by_coeff = o_plot.multiply_array_by_coeff(data=ratio_array, coeff=self.coeff_array)
        if live_plot:
            # o_plot.display_counts_vs_file(data = array_by_coeff)
            o_plot.display_counts_vs_file(data=self.coeff_array)

    def calculate_coeff(self, sample=[], ob=[], list_roi=[]):
        if ob == []:
            # we consider that no OB is like having a perfect OB -> intensity of 1
            o_plot = Step2Plot(parent=self.parent)
            one_over_coeff = o_plot.calculate_mean_counts(sample, list_roi=list_roi)
            # replace 0 by NaN
            one_over_coeff[one_over_coeff == 0] = np.NaN
            self.coeff_array = 1 / one_over_coeff
        else:
            o_plot = Step2Plot(parent=self.parent)
            ob_mean = o_plot.calculate_mean_counts(ob, list_roi=list_roi)
            sample_mean = o_plot.calculate_mean_counts(sample, list_roi=list_roi)
            # replace 0 by NaN
            sample_mean[sample_mean == 0] = np.NaN
            coeff = ob_mean / sample_mean
            self.coeff_array = coeff
