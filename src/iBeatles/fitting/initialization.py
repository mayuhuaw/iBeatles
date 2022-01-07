from qtpy.QtWidgets import (QMainWindow, QApplication, QTableWidgetSelectionRange, QVBoxLayout, QHBoxLayout, QWidget,
                            QLabel, QSpacerItem, QSlider, QRadioButton, QSizePolicy)
from qtpy import QtCore
from pyqtgraph.dockarea import DockArea, Dock
import pyqtgraph as pg
from .. import DataType


class Initialization:

    def __init__(self, parent=None, grand_parent=None):
        self.parent = parent
        self.grand_parent = grand_parent

    def run_all(self):
        self.pyqtgraph()
        self.table_behavior()
        self.labels()
        self.widgets()

    def table_behavior(self):
        for _column, _width in enumerate(self.parent.header_table_columns_width):
            self.parent.ui.header_table.setColumnWidth(_column, _width)

        for _column, _width in enumerate(self.parent.fitting_table_columns_width):
            self.parent.ui.value_table.setColumnWidth(_column, _width)

        self.parent.hori_header_table = self.parent.ui.header_table.horizontalHeader()
        self.parent.hori_value_table = self.parent.ui.value_table.horizontalHeader()

        self.parent.hori_header_table.sectionResized.connect(self.parent.resizing_header_table)
        self.parent.hori_value_table.sectionResized.connect(self.parent.resizing_value_table)

        self.parent.hori_header_table.sectionClicked.connect(self.parent.column_header_table_clicked)
        self.parent.hori_value_table.sectionClicked.connect(self.parent.column_value_table_clicked)

    def pyqtgraph(self):

        if (len(self.grand_parent.data_metadata['normalized']['data_live_selection']) > 0) and \
                not (self.grand_parent.binning_line_view['pos'] is None):
            status = True
        else:
            status = False

        area = DockArea()
        self.parent.ui.area = area
        area.setVisible(status)
        d1 = Dock("Image Preview", size=(200, 300))
        d2 = Dock("Bragg Edge", size=(200, 100))

        area.addDock(d1, 'top')
        area.addDock(d2, 'bottom')

        preview_widget = pg.GraphicsLayoutWidget()
        pg.setConfigOptions(antialias=True)  # this improve display

        vertical_layout = QVBoxLayout()
        preview_widget.setLayout(vertical_layout)

        # image view (top plot)
        image_view = pg.ImageView(view=pg.PlotItem())
        image_view.ui.roiBtn.hide()
        image_view.ui.menuBtn.hide()
        self.parent.image_view = image_view
        self.grand_parent.fitting_image_view = image_view
        image_view.scene.sigMouseMoved.connect(self.parent.mouse_moved_in_image_view)

        top_widget = QWidget()
        vertical = QVBoxLayout()
        vertical.addWidget(image_view)

        # bin transparency
        transparency_layout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        transparency_layout.addItem(spacer)
        label = QLabel("Bin Transparency")
        transparency_layout.addWidget(label)
        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMaximum(100)
        slider.setMinimum(0)
        slider.setValue(50)
        slider.valueChanged.connect(self.parent.slider_changed)
        self.parent.slider = slider
        transparency_layout.addWidget(slider)
        bottom_widget = QWidget()
        bottom_widget.setLayout(transparency_layout)

        top_widget.setLayout(vertical)
        d1.addWidget(top_widget)
        d1.addWidget(bottom_widget)

        # bragg edge plot (bottom plot)
        bragg_edge_plot = pg.PlotWidget(title='')
        bragg_edge_plot.plot()
        self.parent.bragg_edge_plot = bragg_edge_plot

        # plot all or individual bins
        buttons_layout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        buttons_layout.addItem(spacer)
        label = QLabel("Plot")
        buttons_layout.addWidget(label)

        # all bins button
        active_button = QRadioButton()
        active_button.setText("Active Bins")
        active_button.setChecked(True)
        active_button.pressed.connect(self.parent.active_button_pressed)
        self.parent.ui.active_bins_button = active_button

        # indi bin button
        buttons_layout.addWidget(active_button)
        locked_button = QRadioButton()
        locked_button.setText("Locked Bins")
        locked_button.setChecked(False)
        locked_button.pressed.connect(self.parent.lock_button_pressed)
        self.parent.ui.locked_bins_button = locked_button

        buttons_layout.addWidget(locked_button)
        bottom_widget = QWidget()
        bottom_widget.setLayout(buttons_layout)

        d2.addWidget(bragg_edge_plot)
        d2.addWidget(bottom_widget)

        vertical_layout.addWidget(area)
        self.parent.ui.widget.setLayout(vertical_layout)

        # kropff
        self.parent.ui.kropff_fitting = pg.PlotWidget(title="Fitting")
        fitting_layout = QVBoxLayout()
        fitting_layout.addWidget(self.parent.ui.kropff_fitting)
        self.parent.ui.kropff_widget.setLayout(fitting_layout)

    def labels(self):
        self.parent.ui.lambda_min_label.setText(u"\u03BB<sub>min</sub>")
        self.parent.ui.lambda_max_label.setText(u"\u03BB<sub>max</sub>")
        self.parent.ui.lambda_min_units.setText(u"\u212B")
        self.parent.ui.lambda_max_units.setText(u"\u212B")
        self.parent.ui.bragg_edge_units.setText(u"\u212B")
        self.parent.ui.material_groupBox.setTitle(self.grand_parent.selected_element_name)

    def widgets(self):
        """
        such as material h,k,l list according to material selected in normalized tab
        """
        hkl_list = self.grand_parent.selected_element_hkl_array
        str_hkl_list = ["{},{},{}".format(_hkl[0], _hkl[1], _hkl[2]) for _hkl in hkl_list]
        self.parent.ui.hkl_list_ui.addItems(str_hkl_list)

        # Kropff
        kropff_session_dict = self.grand_parent.session_dict[DataType.fitting]['kropff']
        a0 = str(kropff_session_dict['high tof']['a0'])
        b0 = str(kropff_session_dict['high tof']['b0'])
        ahkl = str(kropff_session_dict['low tof']['ahkl'])
        bhkl = str(kropff_session_dict['low tof']['bhkl'])
        lambda_hkl = str(kropff_session_dict['bragg peak']['lambda_hkl'])
        tau = str(kropff_session_dict['bragg peak']['tau'])
        sigma = str(kropff_session_dict['bragg peak']['sigma'])

        self.parent.ui.kropff_high_lda_a0_init.setText(a0)
        self.parent.ui.kropff_high_lda_b0_init.setText(b0)
        self.parent.ui.kropff_low_lda_ahkl_init.setText(ahkl)
        self.parent.ui.kropff_low_lda_bhkl_init.setText(bhkl)
        self.parent.ui.kropff_bragg_peak_ldahkl_init.setText(lambda_hkl)
        self.parent.ui.kropff_bragg_peak_tau_init.setText(tau)

        index = self.parent.ui.kropff_bragg_peak_sigma_comboBox.findText(sigma)
        self.parent.ui.kropff_bragg_peak_sigma_comboBox.setCurrentIndex(index)
