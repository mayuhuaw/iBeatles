import numpy as np
from qtpy.QtWidgets import QCheckBox, QTableWidgetItem
from qtpy import QtGui
# import pyqtgraph as pg


class FillingTableHandler(object):
    table_dictionary = {}
    advanced_mode_flag = True

    def __init__(self, parent=None):
        self.parent = parent

    def set_mode(self, advanced_mode=True):
        self.advaanced_mode_flag = advanced_mode
        list_header_table_advanced_columns = [10, 11]
        list_value_table_advanced_columns = [15, 16, 17, 18]

        self.parent.fitting_ui.ui.header_table.horizontalHeader().blockSignals(True)
        self.parent.fitting_ui.ui.value_table.horizontalHeader().blockSignals(True)

        # hide column a5 and a6
        for _col_index in list_header_table_advanced_columns:
            self.parent.fitting_ui.ui.header_table.setColumnHidden(_col_index, not advanced_mode)
        for _col_index in list_value_table_advanced_columns:
            self.parent.fitting_ui.ui.value_table.setColumnHidden(_col_index, not advanced_mode)

        self.parent.fitting_ui.ui.header_table.horizontalHeader().blockSignals(False)
        self.parent.fitting_ui.ui.value_table.horizontalHeader().blockSignals(False)

        # repopulate table
        self.fill_table()

    def get_row_to_show_state(self):
        """
        return 'all', 'active' or 'lock'
        """
        if self.parent.fitting_ui.ui.show_all_bins.isChecked():
            return 'all'
        elif self.parent.fitting_ui.ui.show_only_active_bins.isChecked():
            return 'active'
        else:
            return 'lock'

    def fill_table(self):
        self.clear_table_ui()
        table_dictionary = self.parent.table_dictionary

        row_to_show_state = self.get_row_to_show_state()

        if table_dictionary is None:
            table_dictionary = self.table_dictionary
        nbr_row = len(table_dictionary)

        value_table_ui = self.parent.fitting_ui.ui.value_table
        # nbr_column = value_table_ui.columnCount()

        self.parent.fitting_ui.ui.value_table.blockSignals(True)

        for _index in np.arange(nbr_row):
            _str_index = str(_index)
            _entry = table_dictionary[_str_index]

            # add new row
            value_table_ui.insertRow(_index)

            # row and column index (columns 0 and 1)
            self.set_item(table_ui=value_table_ui,
                          row=_index,
                          col=0,
                          value=_entry['row_index'] + 1)  # +1 because table starts indexing at 1

            self.set_item(table_ui=value_table_ui,
                          row=_index,
                          col=1,
                          value=_entry['column_index'] + 1)  # +1 because table starts indexing at 1

            # add lock button in first cell (column: 2)
            _lock_button = QCheckBox()
            _is_lock = _entry['lock']

            _lock_button.setChecked(_is_lock)
            _lock_button.stateChanged.connect(lambda state=0,
                                              row=_index: self.parent.fitting_ui.lock_button_state_changed(state,
                                                                                                           row))

            value_table_ui.setCellWidget(_index, 2, _lock_button)

            # add active button in second cell (column: 3)
            _active_button = QCheckBox()
            _is_active = _entry['active']

            _active_button.setChecked(_is_active)
            _active_button.stateChanged.connect(lambda state=0,
                                                row=_index: self.parent.fitting_ui.active_button_state_changed(state,
                                                                                                               row))

            value_table_ui.setCellWidget(_index, 3, _active_button)

            # bin # (column: 1)
            # _bin_number = QTableWidgetItem("{:02}".format(_index))
            # value_table_ui.setItem(_index, 1, _bin_number)

            # from column 2 -> nbr_column
            list_value = [_entry['fitting_confidence'],
                          _entry['d_spacing']['val'],
                          _entry['d_spacing']['err'],
                          _entry['sigma']['val'],
                          _entry['sigma']['err'],
                          _entry['alpha']['val'],
                          _entry['alpha']['err'],
                          _entry['a1']['val'],
                          _entry['a1']['err'],
                          _entry['a2']['val'],
                          _entry['a2']['err'],
                          _entry['a5']['val'],
                          _entry['a5']['err'],
                          _entry['a6']['val'],
                          _entry['a6']['err']]

            list_fixed_flag = [False,
                               _entry['d_spacing']['fixed'],
                               _entry['d_spacing']['fixed'],
                               _entry['sigma']['fixed'],
                               _entry['sigma']['fixed'],
                               _entry['alpha']['fixed'],
                               _entry['alpha']['fixed'],
                               _entry['a1']['fixed'],
                               _entry['a1']['fixed'],
                               _entry['a2']['fixed'],
                               _entry['a2']['fixed'],
                               _entry['a5']['fixed'],
                               _entry['a5']['fixed'],
                               _entry['a6']['fixed'],
                               _entry['a6']['fixed']]

            for _local_index, _value in enumerate(list_value):
                self.set_item(table_ui=value_table_ui,
                              row=_index,
                              col=_local_index + 4,
                              value=_value,
                              fixed_flag=list_fixed_flag[_local_index])

            if row_to_show_state == 'active':
                if not _is_active:
                    value_table_ui.hideRow(_index)
            elif row_to_show_state == 'lock':
                if not _is_lock:
                    value_table_ui.hideRow(_index)

        self.parent.fitting_ui.ui.value_table.blockSignals(False)

    def set_item(self, table_ui=None, row=0, col=0, value="", fixed_flag=False):
        item = QTableWidgetItem(str(value))
        if fixed_flag:
            item.setTextColor(QtGui.QColor(255, 0, 0, alpha=255))

        table_ui.setItem(row, col, item)

    def clear_table_ui(self):
        self.parent.fitting_ui.ui.value_table.blockSignals(True)
        nbr_row = self.parent.fitting_ui.ui.value_table.rowCount()
        for _row in np.arange(nbr_row):
            self.parent.fitting_ui.ui.value_table.removeRow(0)
        self.parent.fitting_ui.ui.value_table.blockSignals(False)

    def clear_table(self):
        self.unselect_full_table()
        self.parent.fitting_ui.ui.value_table.blockSignals(True)
        nbr_row = self.parent.fitting_ui.ui.value_table.rowCount()
        for _row in np.arange(nbr_row):
            self.parent.fitting_ui.ui.value_table.removeRow(0)
        self.parent.fitting_ui.ui.value_table.blockSignals(False)

        self.parent.fitting_ui.selection_in_value_table_changed()
