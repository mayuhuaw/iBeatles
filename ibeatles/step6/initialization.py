import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from qtpy.QtWidgets import QVBoxLayout
import pyqtgraph as pg

from ibeatles import ANGSTROMS, LAMBDA, SUB_0
from ibeatles import DataType
from ibeatles.utilities.mplcanvas import MplCanvas
from ibeatles.step6 import ParametersToDisplay
from ibeatles.step6.get import Get


class Initialization:

    def __init__(self, parent=None, grand_parent=None):
        self.parent = parent
        self.grand_parent = grand_parent

    def all(self):
        self.labels()
        self.parameters()
        self.pyqtgraph()
        self.matplotlib()
        self.data()

    def labels(self):
        self.parent.ui.range_selected_from_units_label.setText(ANGSTROMS)
        self.parent.ui.range_selected_to_units_label.setText(ANGSTROMS)
        self.parent.ui.d0_units1_label.setText(ANGSTROMS)
        self.parent.ui.d0_units2_label.setText(ANGSTROMS)
        self.parent.ui.reference_material_lambda0_units_label.setText(ANGSTROMS)

        self.parent.ui.reference_material_lambda0_label.setText(LAMBDA + SUB_0)

    def parameters(self):
        from_lambda = self.grand_parent.fitting_ui.ui.lambda_min_lineEdit.text()
        to_lambda = self.grand_parent.fitting_ui.ui.lambda_max_lineEdit.text()
        hkl_selected = self.grand_parent.fitting_ui.ui.hkl_list_ui.currentText()
        lambda_0 = np.float(self.grand_parent.fitting_ui.ui.bragg_edge_calculated.text())
        element = self.grand_parent.fitting_ui.ui.material_groupBox.title()

        self.parent.ui.from_lambda.setText(from_lambda)
        self.parent.ui.to_lambda.setText(to_lambda)
        self.parent.ui.hkl_value.setText(hkl_selected)
        self.parent.ui.d0_value.setText("{:.03f}".format(lambda_0 / 2.))
        self.parent.ui.material_name.setText(element)
        self.parent.ui.lambda_0.setText("{:.03f}".format(lambda_0))
        self.parent.ui.d0_user_value.setText("{:.03f}".format(lambda_0 / 2.))

    def data(self):
        live_data = self.grand_parent.data_metadata[DataType.normalized]['data']
        integrated_image = np.mean(live_data, 0)
        self.parent.integrated_image = np.transpose(integrated_image)
        [self.parent.image_size['height'], self.parent.image_size['width']] = np.shape(integrated_image)

    def pyqtgraph(self):
        image_view = pg.ImageView(view=pg.PlotItem())
        image_view.ui.roiBtn.hide()
        image_view.ui.menuBtn.hide()
        self.parent.image_view = image_view
        layout = QVBoxLayout()
        layout.addWidget(image_view)
        self.parent.ui.integrated_widget.setLayout(layout)

    def matplotlib(self):

        def _matplotlib(parent=None, widget=None):
            sc = MplCanvas(parent, width=5, height=2, dpi=100)
            # sc.axes.plot([0,1,2,3,4,5], [10, 1, 20 ,3, 40, 50])
            toolbar = NavigationToolbar(sc, parent)
            layout = QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(sc)
            widget.setLayout(layout)
            return sc

        self.parent.matplotlib_plot = _matplotlib(parent=self.parent,
                                                  widget=self.parent.ui.matplotlib_widget)

    def min_max_values(self):
        d_array = self.parent.d_array
        self.parent.min_max[ParametersToDisplay.d] = {'min': np.min(d_array),
                                                      'max': np.max(d_array)}

        o_get = Get(parent=self.parent)
        strain_mapping = o_get.strain_mapping()

        self.parent.min_max[ParametersToDisplay.strain_mapping] = {'min': np.min(strain_mapping),
                                                                   'max': np.max(strain_mapping)}
