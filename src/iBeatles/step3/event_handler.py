import logging

from ..all_steps.event_handler import EventHandler as TopEventHandler
from ..step1.data_handler import DataHandler
from ..step1.plot import Step1Plot
from .gui_handler import Step3GuiHandler

from ..utilities.retrieve_data_infos import RetrieveGeneralDataInfos

from .. import DataType


class EventHandler(TopEventHandler):

    def import_button_clicked(self):
        logging.info(f"{self.data_type} import button clicked")

        self.parent.loading_flag = True
        o_load = DataHandler(parent=self.parent,
                             data_type=self.data_type)
        _folder = o_load.select_folder()
        o_load.import_files_from_folder(folder=_folder, extension=[".tif", ".fits", ".tiff"])
        o_load.import_time_spectra()

        if self.parent.data_metadata[self.data_type]['data']:

            self.parent.data_metadata[self.data_type]['folder'] = _folder
            self.parent.select_load_data_row(data_type=self.data_type, row=0)
            self.parent.retrieve_general_infos(data_type=self.data_type)
            self.parent.retrieve_general_data_infos(data_type=self.data_type)
            o_plot = Step1Plot(parent=self.parent, data_type=self.data_type)
            o_plot.initialize_default_roi()
            o_plot.display_bragg_edge(mouse_selection=False)
            o_gui = Step3GuiHandler(parent=self.parent)
            o_gui.check_widgets()

    def sample_list_selection_changed(self):
        if not self.parent.loading_flag:
            o_retrieve_data_infos = RetrieveGeneralDataInfos(parent=self.parent, data_type=DataType.normalized)
            o_retrieve_data_infos.update()
            self.parent.roi_normalized_image_view_changed(mouse_selection=False)
        else:
            self.parent.loading_flag = False
