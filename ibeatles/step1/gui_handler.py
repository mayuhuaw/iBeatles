try:
    import PyQt4
    import PyQt4.QtCore as QtCore
    import PyQt4.QtGui as QtGui
except:
    import PyQt5
    import PyQt5.QtCore as QtCore
    import PyQt5.QtGui as QtGui

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


from ibeatles.step1.plot import Step1Plot
from ibeatles.utilities.retrieve_data_infos import RetrieveGeneralFileInfos, RetrieveSelectedFileDataInfos
import ibeatles.step1.math_utilities


from ibeatles.interfaces.my_mplwidget import Qt4MplCanvas
import pyqtgraph as pg
from pyqtgraph.dockarea import *


class Step1GuiHandler(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def load_data_tab_changed(self, tab_index=0):
        data_type = 'sample'
        
        if tab_index == 0:
            data_preview_box_label = "Sample Image Preview"
            o_general_infos = RetrieveGeneralFileInfos(parent = self.parent, 
                                                       data_type = 'sample')
            o_selected_infos = RetrieveSelectedFileDataInfos(parent = self.parent,
                                                                  data_type = 'sample')
        else:
            data_preview_box_label = "Open Beam Image Preview"
            o_general_infos = RetrieveGeneralFileInfos(parent = self.parent, 
                                                       data_type = 'ob')
            o_selected_infos = RetrieveSelectedFileDataInfos(parent = self.parent,
                                                                  data_type = 'ob')
            data_type = 'ob'
        
        o_general_infos.update()            
        o_selected_infos.update()

        row_selected = self.row_selected(data_type=data_type)
        data = self.parent.data_metadata[data_type]['data']
        if not data == []:
            data = data[row_selected]
        o_gui = Step1Plot(parent = self.parent, 
                          data_type = data_type,
                          data = data)
        o_gui.all_plots()
        
        
    def row_selected(self, data_type='sample'):
        return self.parent.data_metadata[data_type]['list_widget_ui'].currentRow()
        
    def init_statusbar(self):
        self.parent.eventProgress = QtGui.QProgressBar(self.parent.ui.statusbar)
        self.parent.eventProgress.setMinimumSize(20, 14)
        self.parent.eventProgress.setMaximumSize(540, 100)
        self.parent.eventProgress.setVisible(False)
        self.parent.ui.statusbar.addPermanentWidget(self.parent.eventProgress)
        
    def init_gui(self):
        # define position and size
        rect = self.parent.geometry()
        self.parent.setGeometry(10, 10, rect.width(), rect.height())
        self.parent.ui.sample_ob_splitter.setSizes([850, 20])
        self.parent.ui.load_data_splitter.setSizes([200, 500])
        self.parent.ui.normalized_splitter.setSizes([150, 600])

    def init_labels(self):
        #micross
        self.parent.ui.micro_s.setText(u"\u00B5s")
        #distance source detector
        self.parent.ui.distance_source_detector_label.setText("d<sub> source-detector</sub>")
        #delta lambda
        self.parent.ui.delta_lambda_label.setText(u"\u0394\u03BB:")

    def select_load_data_row(self, data_type='sample', row=0):
        if data_type == 'sample':
            self.parent.ui.list_sample.setCurrentRow(row)
        else:
            self.parent.ui.list_open_beam.setCurrentRow(row)
            
    def general_init_pyqtgrpah(self, roi_function,
                               base_widget):

        area = DockArea()
        d1 = Dock("Image Preview", size=(200, 300))
        d2 = Dock("Bragg Edge", size=(200, 100))
        
        area.addDock(d1, 'top')
        area.addDock(d2, 'bottom')
    
        preview_widget = pg.GraphicsLayoutWidget()
        pg.setConfigOptions(antialias=True) # this improve display
    
        vertical_layout = QtGui.QVBoxLayout()
        preview_widget.setLayout(vertical_layout)
        
        # image view
        image_view = pg.ImageView()
        image_view.ui.roiBtn.hide()
        image_view.ui.menuBtn.hide()
        roi = pg.ROI([0,0],[1,1])
        roi.addScaleHandle([1,1],[0,0])
        image_view.addItem(roi)
        roi.sigRegionChanged.connect(roi_function)
        d1.addWidget(image_view)
    
        # bragg edge plot
        bragg_edge_plot = pg.PlotWidget()
        bragg_edge_plot.plot()
        d2.addWidget(bragg_edge_plot)
    
        vertical_layout.addWidget(area)
        base_widget.setLayout(vertical_layout)
    
        return [image_view, roi, bragg_edge_plot]
                  

    def init_pyqtgraph(self):


        #sample
        [self.parent.ui.image_view, 
         self.parent.ui.image_view_roi, 
         self.parent.ui.bragg_edge_plot] = self.general_init_pyqtgrpah(self.parent.roi_image_view_changed,
                                    self.parent.ui.preview_widget)

        #ob
        [self.parent.ui.ob_image_view,
        self.parent.ui.ob_image_view_roi,
        self.parent.ui.ob_bragg_edge_plot] = self.general_init_pyqtgrpah(self.parent.roi_ob_image_view_changed,
                                    self.parent.ui.ob_preview_widget)
        
        #normalized
        [self.parent.ui.normalized_image_view,
        self.parent.ui.normalized_image_view_roi,
        self.parent.ui.normalized_bragg_edge_plot] = self.general_init_pyqtgrpah(self.parent.roi_normalized_image_view_changed,
                                    self.parent.ui.normalized_preview_widget)



        return

        # sample tab
        area = DockArea()
        d1 = Dock("Image Preview", size=(200, 300))
        d2 = Dock("Bragg Edge", size=(200, 100))
        
        area.addDock(d1, 'top')
        area.addDock(d2, 'bottom')

        preview_widget = pg.GraphicsLayoutWidget()
        pg.setConfigOptions(antialias=True) # this improve display

        vertical_layout = QtGui.QVBoxLayout()
        preview_widget.setLayout(vertical_layout)
        
        # image view
        image_view = pg.ImageView()
        image_view.ui.roiBtn.hide()
        image_view.ui.menuBtn.hide()
        roi = pg.ROI([0,0],[1,1])
        roi.addScaleHandle([1,1],[0,0])
        image_view.addItem(roi)
        roi.sigRegionChanged.connect(self.parent.roi_image_view_changed)        
        d1.addWidget(image_view)

        # bragg edge plot
        bragg_edge_plot = pg.PlotWidget()
        bragg_edge_plot.plot()
        d2.addWidget(bragg_edge_plot)

        vertical_layout.addWidget(area)
        self.parent.ui.preview_widget.setLayout(vertical_layout)

        self.parent.ui.image_view = image_view
        self.parent.ui.image_view_roi = roi
        self.parent.ui.bragg_edge_plot = bragg_edge_plot

        # =================
        # ob tab
        area = DockArea()
        d1 = Dock("Image Preview", size=(200, 300))
        d2 = Dock("Bragg Edge", size=(200, 100))
        
        area.addDock(d1, 'top')
        area.addDock(d2, 'bottom')

        preview_widget = pg.GraphicsLayoutWidget()
        pg.setConfigOptions(antialias=True) # this improve display

        vertical_layout = QtGui.QVBoxLayout()
        preview_widget.setLayout(vertical_layout)
        
        # image view
        image_view = pg.ImageView()
        image_view.ui.roiBtn.hide()
        image_view.ui.menuBtn.hide()
        roi = pg.ROI([0,0],[1,1])
        roi.addScaleHandle([1,1],[0,0])
        image_view.addItem(roi)
        roi.sigRegionChanged.connect(self.parent.roi_ob_image_view_changed)        
        d1.addWidget(image_view)

        # bragg edge plot
        bragg_edge_plot = pg.PlotWidget()
        bragg_edge_plot.plot()
        d2.addWidget(bragg_edge_plot)

        vertical_layout.addWidget(area)
        self.parent.ui.ob_preview_widget.setLayout(vertical_layout)

        self.parent.ui.ob_image_view = image_view
        self.parent.ui.ob_image_view_roi = roi
        self.parent.ui.ob_bragg_edge_plot = bragg_edge_plot


    def update_delta_lambda(self):
        distance_source_detector = float(str(self.parent.ui.distance_source_detector.text()))
        frequency = float(str(self.parent.ui.beam_rate.currentText()))
        
        delta_lambda = ibeatles.step1.math_utilities.calculate_delta_lambda(distance_source_detector = distance_source_detector,
                                                                            frequency = frequency)

        self.parent.ui.delta_lambda_value.setText("{:.2f}".format(delta_lambda))