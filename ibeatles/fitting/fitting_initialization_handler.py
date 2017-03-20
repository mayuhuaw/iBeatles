try:
    import PyQt4
    import PyQt4.QtCore as QtCore
    from PyQt4.QtGui import QApplication         
except:
    import PyQt5
    import PyQt5.QtCore as QtCore
    from PyQt5.QtWidgets import QApplication

import numpy as np

from ibeatles.table_dictionary.table_dictionary_handler import TableDictionaryHandler
from ibeatles.fitting.initialization_sigma_alpha import InitializationSigmaAlpha


class FittingInitializationHandler(object):

    all_variables_initialized = True
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def make_all_active(self):
        o_table = TableDictionaryHandler(parent=self.parent)
        o_table.full_table_selection_tool(status=True)
        self.parent.fitting_ui.update_table()
        self.parent.fitting_ui.update_bragg_edge_plot()
        
    def run(self):
        self.advanced_mode = self.parent.fitting_ui.ui.advanced_table_checkBox.isChecked()
        o_init_sigma_alpha = InitializationSigmaAlpha(parent=self.parent)
        
    def finished_up_initialization(self):
        if self.parent.fitting_ui.sigma_alpha_initialized:
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.retrieve_parameters_and_update_table()
            self.parent.fitting_ui.update_table()
            QApplication.restoreOverrideCursor()
        
    def retrieve_parameters_and_update_table(self):
        table_handler = TableDictionaryHandler(parent=self.parent)

        d_spacing = self.get_d_spacing()
        if np.isnan(d_spacing):
            self.all_variables_initialized = False
        table_handler.fill_table_with_variable(variable_name = 'd_spacing',
                                               value = d_spacing,
                                               all_keys = True)

        sigma = self.get_sigma()
        if np.isnan(sigma):
            self.all_variables_initialized = False
        table_handler.fill_table_with_variable(variable_name = 'sigma',
                                               value = sigma,
                                               all_keys = True)
        
        alpha = self.get_alpha()
        if np.isnan(alpha):
            self.all_variables_initialized = False
        table_handler.fill_table_with_variable(variable_name = 'alpha',
                                               value = alpha,
                                               all_keys = True)
        
        a1 = self.get_a1()
        if np.isnan(a1):
            self.all_variables_initialized = False
        table_handler.fill_table_with_variable(variable_name = 'a1',
                                               value = a1,
                                               all_keys = True)
        
        a2 = self.get_a2()
        if np.isnan(a2):
            self.all_variables_initialized = False
        table_handler.fill_table_with_variable(variable_name = 'a2',
                                               value = a2,
                                               all_keys = True)

        
    def get_a1(self):
        return np.NaN
    
    def get_a2(self):
        return np.NaN
        
    def get_sigma(self):
        return np.NaN
    
    def get_alpha(self):
        return np.NaN

    def get_d_spacing(self):
        '''
        calculates the d-spacing using the lambda range selection and using the central lambda
        
        2* d_spacing = lambda
        '''
        lambda_min = np.float(str(self.parent.fitting_ui.ui.lambda_min_lineEdit.text()))
        lambda_max = np.float(str(self.parent.fitting_ui.ui.lambda_max_lineEdit.text()))
        
        average_lambda = np.mean([lambda_min, lambda_max])
        
        d_spacing = average_lambda / 2.
        
        return d_spacing