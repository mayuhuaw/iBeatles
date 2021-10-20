import os

from .. import DataType
from ..step1.data_handler import DataHandler
from ..step1.gui_handler import Step1GuiHandler
from ..step2.plot import Step2Plot
from ..utilities.gui_handler import GuiHandler
from ..utilities.pyqrgraph import Pyqtgrah as PyqtgraphUtilities


class LoadLoadDataTab:

    def __init__(self, parent=None):
        self.parent = parent
        self.session_dict = parent.session_dict

    def sample(self):

        session_dict = self.session_dict
        data_type = DataType.sample

        list_sample_files = self.session_dict[data_type]['list files']
        if list_sample_files:
            input_folder = session_dict[data_type]['current folder']
            self.parent.image_view_settings[data_type]['state'] = \
                session_dict[data_type]['image view state']
            o_data_handler = DataHandler(parent=self.parent,
                                         data_type=data_type)
            list_sample_files_fullname = [os.path.join(input_folder, _file) for _file in list_sample_files]
            o_data_handler.load_files(list_of_files=list_sample_files_fullname)
            time_spectra_file = session_dict[data_type]['time spectra filename']
            o_data_handler.load_time_spectra(time_spectra_file=time_spectra_file)
            list_files_selected = session_dict[data_type]['list files selected']
            self.parent.list_roi[data_type] = session_dict[data_type]['list rois']
            o_gui = Step1GuiHandler(parent=self.parent, data_type=data_type)
            o_gui.initialize_rois_and_labels()
            for _row_selected in list_files_selected:
                _item = self.parent.ui.list_sample.item(_row_selected)
                _item.setSelected(True)
            o_gui.check_time_spectra_widgets()
            o_gui.check_step1_widgets()
            self.parent.check_files_error()
            self.parent.retrieve_general_infos(data_type=data_type)
            self.parent.retrieve_general_data_infos(data_type=data_type)

            o_step2_plot = Step2Plot(parent=self.parent)
            o_step2_plot.prepare_data()
            o_step2_plot.init_roi_table()

            o_pyqt = PyqtgraphUtilities(parent=self.parent,
                                        image_view=self.parent.ui.image_view,
                                        data_type=data_type)
            o_pyqt.set_state(session_dict[data_type]['image view state'])
            histogram_level = session_dict[data_type]['image view histogram']
            o_pyqt.set_histogram_level(histogram_level=histogram_level)

    def ob(self):

        session_dict = self.session_dict
        data_type = DataType.ob

        self.parent.image_view_settings[data_type]['state'] = session_dict[data_type]['image view state']
        self.parent.image_view_settings[data_type]['histogram'] = session_dict[data_type]['image view histogram']
        list_ob_files = session_dict[data_type]['list files']
        if list_ob_files:
            input_folder = session_dict[data_type]['current folder']
            o_data_handler = DataHandler(parent=self.parent,
                                         data_type=data_type)
            list_ob_files_fullname = [os.path.join(input_folder, _file) for _file in list_ob_files]
            o_data_handler.load_files(list_of_files=list_ob_files_fullname)
        list_files_selected = session_dict[data_type]['list files selected']
        self.parent.list_roi[data_type] = session_dict[data_type]['list rois']
        o_gui = Step1GuiHandler(parent=self.parent, data_type=data_type)
        o_gui.initialize_rois_and_labels()
        for _row_selected in list_files_selected:
            _item = self.parent.ui.list_open_beam.item(_row_selected)
            _item.setSelected(True)

        o_pyqt = PyqtgraphUtilities(parent=self.parent,
                                    image_view=self.parent.ui.ob_image_view,
                                    data_type=data_type)
        o_pyqt.set_state(session_dict[data_type]['image view state'])
        o_pyqt.reload_histogram_level()
        histogram_level = session_dict[data_type]['image view histogram']
        o_pyqt.set_histogram_level(histogram_level=histogram_level)

    def instrument(self):

        session_dict = self.session_dict

        o_gui = GuiHandler(parent=self.parent)
        list_ui = {'distance': self.parent.ui.distance_source_detector,
                   'beam': self.parent.ui.beam_rate,
                   'detector': self.parent.ui.detector_offset}

        for _key in list_ui.keys():
            list_ui[_key].blockSignals(True)

        o_gui.set_index_selected(index=session_dict["instrument"]["beam index"], ui=list_ui['beam'])
        o_gui.set_text(value=session_dict["instrument"]["distance source detector"], ui=list_ui['distance'])

        for _key in list_ui.keys():
            list_ui[_key].blockSignals(False)

        o_gui.set_text(value=session_dict["instrument"]["detector value"], ui=list_ui['detector'])
