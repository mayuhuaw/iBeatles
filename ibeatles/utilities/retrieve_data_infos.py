import os
import time
import numpy as np

# import matplotlib.pyplot as plt
# from matplotlib.widgets import RectangleSelector

from ..utilities.image_handler import ImageHandler
from ..step1.plot import Step1Plot


class RetrieveDataInfos(object):

    def __init__(self, parent=None, data_type='sample'):
        self.parent = parent
        self.data_type = data_type

        self.general_infos_ui = {'sample': self.parent.ui.data_general_infos,
                                 'ob': self.parent.ui.data_general_infos,
                                 'normalized': self.parent.ui.normalized_general_infos}

        # self.selected_infos_ui = {'sample': self.parent.ui.data_selected_infos,
        #                           'ob': self.parent.ui.data_selected_infos,
        #                           'normalized': self.parent.ui.normalized_selected_infos}

        self.path = self.parent.data_metadata[data_type]['folder']

        self.table_ui = {'sample': self.parent.ui.list_sample,
                         'ob': self.parent.ui.list_open_beam,
                         'normalized': self.parent.ui.list_normalized}

        self.preview_widget = {'sample': self.parent.ui.image_view,
                               'ob': self.parent.ui.image_view}


class RetrieveGeneralDataInfos(RetrieveDataInfos):

    selected_infos = {'acquisition_duration': {'name': "Acquisition Duration",
                                               'value': 0},
                      'acquisition_time': {'name': 'Acquisition Time',
                                           'value': ''},
                      'image_size': {'name': 'Image(s) Size',
                                     'value': '512x512'},
                      'image_type': {'name': 'Image Type',
                                     'value': '16 bits'},
                      'min_counts': {'name': 'min counts',
                                     'value': 0},
                      'max_counts': {'name': 'max counts',
                                     'value': 0}}

    data = []

    def update(self):

        list_row_selected = list(np.sort(self.get_list_row_selected()))

        if not list_row_selected:

            if self.parent.data_metadata[self.data_type]['data'] == []:
                self.selected_infos = {}
                self.data = []
            else:

                list_files_selected = self.parent.list_file_selected[self.data_type]
                self.table_ui[self.data_type].blockSignals(True)
                for _row_selected in list_files_selected:
                    _item = self.table_ui[self.data_type].item(_row_selected)
                    _item.setSelected(True)
                self.table_ui[self.data_type].blockSignals(False)

                data = self.parent.data_metadata[self.data_type]['data']
                self.data = np.sum(data, axis=0)

        else:

            full_data = self.parent.data_metadata[self.data_type]['data']
            _data = []
            for index in list_row_selected:
                _data.append(full_data[index])
            self.data = np.sum(_data, axis=0)

            if self.data_type == 'normalized':
                self.parent.data_metadata['normalized']['data_live_selection'] = _data

            self.parent.list_file_selected[self.data_type] = list_row_selected

        self.display()

    def display(self):

        # # metadata
        # text = ''
        # for key in self.selected_infos:
        #     text += '<b>{}</b>: {}<br/>'.format(self.selected_infos[key]['name'],
        #                                         self.selected_infos[key]['value'])
        # self.selected_infos_ui[self.data_type].setHtml(text)

        o_plot = Step1Plot(parent=self.parent,
                           data_type=self.data_type,
                           data=self.data)
        o_plot.display_image()

    def get_list_files_selected(self):
        list_files = [str(x.text()) for x in self.table_ui[self.data_type].selectedItems()]
        return list_files

    def get_list_row_selected(self):
        selection = self.table_ui[self.data_type].selectedIndexes()
        _list_row_selected = []
        for _index in selection:
            _list_row_selected.append(_index.row())
        return _list_row_selected


class RetrieveGeneralFileInfos(RetrieveDataInfos):
    general_infos = {'number_of_files': {'name': 'Number of Files',
                                         'value': -1},
                     'time_stamp_files': {'name': 'Acquisition Time of Files',
                                          'value': -1},
                     'size_mb': {'name': 'Individual File Size (MB)',
                                 'value': ''},
                     'total_size_folder': {'name': 'Total Size of Folder (MB)',
                                           'value': ''},
                     }

    def update(self):
        data_files = self.parent.list_files[self.data_type]
        if data_files == []:
            self.general_infos = {}  # no files so no infos to display

        else:
            folder = self.parent.data_metadata[self.data_type]['folder']

            _nbr_files = len(data_files)
            self.general_infos['number_of_files']['value'] = _nbr_files

            _first_file = data_files[0]
            first_file_full_name = os.path.join(folder, _first_file)

            _timestamp_first_file = self.get_formated_time(first_file_full_name)
            self.general_infos['time_stamp_files']['value'] = _timestamp_first_file

            _size_of_one_file_kb = float(os.path.getsize(first_file_full_name))
            _file_size_mb = "{:.2f}".format(_size_of_one_file_kb / 1000000.0)
            self.general_infos['size_mb']['value'] = _file_size_mb

            _total_size_mb = _size_of_one_file_kb * _nbr_files / 1000000.0
            _total_size_mb = "{:.2f}".format(_total_size_mb)
            self.general_infos['total_size_folder']['value'] = _total_size_mb

        self.display()

    def get_formated_time(self, full_file_name):
        _time = time.strftime('%m/%d/%Y %H:%M:%S',
                              time.gmtime(os.path.getmtime(full_file_name)))
        return _time

    def display(self):
        text = ''
        for key in self.general_infos:
            text += '<b>{}</b>: {}<br/>'.format(self.general_infos[key]['name'],
                                                self.general_infos[key]['value'])

        self.general_infos_ui[self.data_type].setHtml(text)
