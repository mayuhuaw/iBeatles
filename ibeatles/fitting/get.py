import numpy as np

from . import KropffTabSelected, FittingTabSelected
from ..utilities.table_handler import TableHandler
from ibeatles.utilities.array_utilities import find_nearest_index
from ibeatles.fitting.kropff.fitting_functions import kropff_high_lambda, kropff_bragg_peak_tof, kropff_low_lambda


class Get:

    def __init__(self, parent=None, grand_parent=None):
        self.parent = parent
        self.grand_parent = grand_parent

    def main_tab_selected(self):
        tab_selected_index = self.parent.ui.tabWidget.currentIndex()
        if tab_selected_index == 0:
            return FittingTabSelected.march_dollase
        elif tab_selected_index == 1:
            return FittingTabSelected.kropff
        else:
            raise IndexError("Fitting algorithm not implemented")

    def kropff_tab_selected(self):
        tab_selected_index = self.parent.ui.kropff_tabWidget.currentIndex()
        if tab_selected_index == 0:
            tab_selected = KropffTabSelected.high_tof
        elif tab_selected_index == 1:
            tab_selected = KropffTabSelected.low_tof
        else:
            tab_selected = KropffTabSelected.bragg_peak
        return tab_selected

    def kropff_tab_ui_selected(self):
        tab_selected = self.kropff_tab_selected()
        if tab_selected == KropffTabSelected.high_tof:
            return self.parent.ui.high_lda_tableWidget
        elif tab_selected == KropffTabSelected.low_tof:
            return self.parent.ui.low_lda_tableWidget
        elif tab_selected == KropffTabSelected.bragg_peak:
            return self.parent.ui.bragg_edge_tableWidget
        else:
            raise ValueError("Tab Selected is invalid!")

    def kropff_matplotlib_ui_selected(self):
        tab_selected = self.kropff_tab_selected()
        if tab_selected == KropffTabSelected.high_tof:
            return self.parent.kropff_high_plot
        elif tab_selected == KropffTabSelected.low_tof:
            return self.parent.kropff_low_plot
        elif tab_selected == KropffTabSelected.bragg_peak:
            return self.parent.kropff_bragg_peak_plot
        else:
            raise ValueError("Tab selected is invalid!")

    def kropff_fitting_parameters_radioButton_selected(self):
        tab_selected = self.kropff_tab_selected()
        if tab_selected == KropffTabSelected.high_tof:
            if self.parent.ui.kropff_a0_radioButton.isChecked():
                return 'a0'
            elif self.parent.ui.kropff_b0_radioButton.isChecked():
                return 'b0'
            else:
                raise ValueError("fitting parameters is invalid!")
        elif tab_selected == KropffTabSelected.low_tof:
            if self.parent.ui.kropff_ahkl_radioButton.isChecked():
                return 'ahkl'
            elif self.parent.ui.kropff_bhkl_radioButton.isChecked():
                return 'bhkl'
            else:
                raise ValueError("fitting parameters is invalid!")
        elif tab_selected == KropffTabSelected.bragg_peak:
            if self.parent.ui.kropff_lda_hkl_radioButton.isChecked():
                return 'lambda_hkl'
            elif self.parent.ui.kropff_tau_radioButton.isChecked():
                return 'tau'
            elif self.parent.ui.kropff_sigma_radioButton.isChecked():
                return 'sigma'
            else:
                raise ValueError("fitting parameters is invalid!")
        else:
            raise ValueError("Tab selected is invalid!")


    def fitting_bragg_edge_linear_selection(self):
        if self.grand_parent.fitting_bragg_edge_linear_selection == []:
            linear_region_left_index = 0
            x_axis = self.grand_parent.normalized_lambda_bragg_edge_x_axis
            linear_region_right_index = len(x_axis) - 1
            self.grand_parent.fitting_bragg_edge_linear_selection = [linear_region_left_index,
                                                                     linear_region_right_index]
            return [linear_region_left_index, linear_region_right_index]

        else:
            return self.grand_parent.fitting_bragg_edge_linear_selection

    def y_axis_fitted_for_given_rows_selected(self):
        table_ui_selected = self.kropff_tab_ui_selected()
        row_selected = self.row_selected_for_this_table_ui(table_ui=table_ui_selected)
        table_dictionary = self.grand_parent.kropff_table_dictionary
        kropff_tab_selected = self.kropff_tab_selected()

        list_of_yaxis_fitted = []
        xaxis = []

        for _row in row_selected:
            _row = str(_row)
            _bin_entry = table_dictionary[_row]

            if _bin_entry['fitted'][kropff_tab_selected]['yaxis'] is None:
                xaxis, _yaxis_fitted = self.calculate_yaxis_fitted_using_fitted_parameters(
                        kropff_tab_selected=kropff_tab_selected,
                        row=_row)

                if _yaxis_fitted is None:
                    return [], []

                else:
                    table_dictionary[_row]['fitted'][kropff_tab_selected]['xaxis'] = xaxis
                    table_dictionary[_row]['fitted'][kropff_tab_selected]['yaxis'] = _yaxis_fitted
                    list_of_yaxis_fitted.append(_yaxis_fitted)

            else:
                xaxis = _bin_entry['fitted'][kropff_tab_selected]['xaxis']
                list_of_yaxis_fitted.append(_bin_entry['fitted'][kropff_tab_selected]['yaxis'])

        return xaxis, list_of_yaxis_fitted

    def calculate_yaxis_fitted_using_fitted_parameters(self, kropff_tab_selected=KropffTabSelected.high_tof,
                                                       row='0'):
        table_dictionary = self.grand_parent.kropff_table_dictionary
        full_xaxis = table_dictionary[row]['xaxis']

        a0 = table_dictionary[row]['a0']['val']
        b0 = table_dictionary[row]['b0']['val']
        if np.isnan(a0):
            return [], []

        if kropff_tab_selected == KropffTabSelected.high_tof:

            right = table_dictionary[row]['bragg peak threshold']['right']
            nearest_index = find_nearest_index(full_xaxis, right)
            xaxis = full_xaxis[nearest_index:-1]
            yaxis_fitted = kropff_high_lambda(xaxis, a0, b0)

            return xaxis, yaxis_fitted

        else:

            ahkl = table_dictionary[row]['ahkl']['val']
            bhkl = table_dictionary[row]['bhkl']['val']
            if np.isnan(ahkl):
                return [], []

            if kropff_tab_selected == KropffTabSelected.low_tof:

                left = table_dictionary[row]['bragg peak threshold']['left']
                nearest_index = find_nearest_index(full_xaxis, left)
                xaxis = full_xaxis[: nearest_index+1]
                yaxis_fitted = kropff_low_lambda(xaxis, a0, b0, ahkl, bhkl)

                return xaxis, yaxis_fitted

            elif kropff_tab_selected == KropffTabSelected.bragg_peak:

                lambda_hkl = table_dictionary[row]['lambda_hkl']['val']
                tau = table_dictionary[row]['tau']['val']
                sigma = table_dictionary[row]['sigma']['val']

                xaxis = full_xaxis
                yaxis_fitted = kropff_bragg_peak_tof(xaxis, a0, b0, ahkl, bhkl, lambda_hkl, sigma, tau)

                return xaxis, yaxis_fitted

            else:
                raise NotImplementedError


    def y_axis_and_x_axis_for_given_rows_selected(self):
        table_ui_selected = self.kropff_tab_ui_selected()
        row_selected = self.row_selected_for_this_table_ui(table_ui=table_ui_selected)
        table_dictionary = self.grand_parent.kropff_table_dictionary

        # data_2d = np.array(self.grand_parent.data_metadata['normalized']['data'])
        data_2d = self.grand_parent.data_metadata['normalized']['data']

        # index of selection in bragg edge plot
        [left_index, right_index] = self.fitting_bragg_edge_linear_selection()

        list_of_yaxis = []

        if row_selected == []:
            return [], []

        for _row in row_selected:
            _bin_entry = table_dictionary[str(_row)]

            if _bin_entry['yaxis'] is None:

                _bin_x0 = _bin_entry['bin_coordinates']['x0']
                _bin_x1 = _bin_entry['bin_coordinates']['x1']
                _bin_y0 = _bin_entry['bin_coordinates']['y0']
                _bin_y1 = _bin_entry['bin_coordinates']['y1']

                yaxis = data_2d[left_index: right_index,
                                 _bin_x0: _bin_x1,
                                 _bin_y0: _bin_y1,
                                 ]  # noqa: E124
                yaxis = np.nanmean(yaxis, axis=1)
                yaxis = np.array(np.nanmean(yaxis, axis=1), dtype=float)
                _bin_entry['yaxis'] = yaxis
                self.grand_parent.kropff_table_dictionary[str(_row)] = _bin_entry

                # index of selection in bragg edge plot
                # [left_index, right_index] = self.grand_parent.fitting_bragg_edge_linear_selection
                full_x_axis = self.parent.bragg_edge_data['x_axis']
                xaxis = np.array(full_x_axis[left_index: right_index], dtype=float)
                _bin_entry['xaxis'] = xaxis

            else:
                yaxis = _bin_entry['yaxis']
                xaxis = _bin_entry['xaxis']

            list_of_yaxis.append(yaxis)

        return list_of_yaxis, xaxis

    def row_selected_for_this_table_ui(self, table_ui=None):
        if table_ui is None:
            return []

        o_table = TableHandler(table_ui=table_ui)
        row_selected = o_table.get_rows_of_table_selected()
        return row_selected

    def kropff_row_selected(self):
        kropff_tab_ui_selected = self.kropff_tab_ui_selected()
        o_table = TableHandler(table_ui=kropff_tab_ui_selected)
        row_selected = o_table.get_rows_of_table_selected()
        return row_selected

    def is_automatic_bragg_peak_threshold_finder_activated(self):
        return self.parent.ui.kropff_automatic_bragg_peak_threshold_finder_checkBox.isChecked()
