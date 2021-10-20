from qtpy.QtWidgets import QDialog
import os

from .. import load_ui
from .session_handler import SessionHandler

from .. import DataType


class LoadPreviousSessionLauncherMultipleChoice(QDialog):

    def __init__(self, parent=None, config=None, list_tabs_to_load=None):
        self.parent = parent
        QDialog.__init__(self, parent=parent)
        ui_full_path = os.path.join(os.path.dirname(__file__),
                                    os.path.join('ui',
                                                 'ui_load_previous_session_multiple_choice.ui'))
        self.ui = load_ui(ui_full_path, baseinstance=self)
        self.setWindowTitle("Select Tabs to Load?")
        self.ui.ok_pushButton.setFocus(True)

        self.init_widgets(list_tabs_to_load=list_tabs_to_load)

    def init_widgets(self, list_tabs_to_load=None):
        if DataType.sample in list_tabs_to_load:
            self.ui.sample_and_ob_checkBox.setEnabled(True)
            self.ui.sample_and_ob_checkBox.setChecked(True)
        if DataType.normalized in list_tabs_to_load:
            self.ui.normalized_checkBox.setEnabled(True)
            self.ui.normalized_checkBox.setChecked(True)
            if self.parent.data_metadata[DataType.bin]['ui_accessed']:
                self.ui.bin_checkBox.setEnabled(True)
                self.ui.bin_checkBox.setChecked(True)
            if self.parent.data_metadata[DataType.fitting]['ui_accessed']:
                self.ui.fitting_checkBox.setEnabled(True)
                self.ui.fitting_checkBox.setChecked(True)

    def _get_list_tabs_to_load(self):
        list_tabs_to_load = []
        if self.ui.sample_and_ob_checkBox.isChecked():
            list_tabs_to_load.append(DataType.sample)
        if self.ui.normalized_checkBox.isChecked():
            list_tabs_to_load.append(DataType.normalized)
        if self.ui.bin_checkBox.isChecked():
            list_tabs_to_load.append(DataType.bin)
        if self.ui.fitting_checkBox.isChecked():
            list_tabs_to_load.append(DataType.fitting)
        return list_tabs_to_load

    def ok_clicked(self):
        self.close()
        o_session = SessionHandler(parent=self.parent)
        o_session.load_to_ui(tabs_to_load=self._get_list_tabs_to_load())
        self.parent.loading_from_config = False

    def cancel_clicked(self):
        self.close()
