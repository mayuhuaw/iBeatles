import sys
import os
import glob
import pprint

import PyQt4.QtGui as QtGui


from ibeatles.utilities.load_images import LoadImages, LoadTimeSpectra
from ibeatles.utilities.file_handler import FileHandler



class DataHandler(object):
    
    user_canceled = False

    def __init__(self, parent=None):
        self.parent = parent


        self.list_ui = {'sample': {'list': self.parent.ui.list_sample,
                                   'folder': self.parent.ui.sample_folder},
                        'ob': {'list': self.parent.ui.list_open_beam,
                               'folder': self.parent.ui.open_beam_folder},
                        'time_spectra': {'text': self.parent.ui.time_spectra,
                                         'folder': self.parent.ui.time_spectra_folder}}
    
    def retrieve_files(self, data_type='sample'):
        """
        type = ['sample', 'ob', 'normalized', 'time_spectra']
        """
        
        self.data_type = data_type
        
        mydialog = FileDialog()
        mydialog.setDirectory(self.parent.sample_folder)
        mydialog.exec_()

        selectedFiles = mydialog.filesSelected()
        if selectedFiles:
            if len(selectedFiles) == 1:
                if os.path.isdir(selectedFiles[0]):
                    self.load_directory(selectedFiles[0])
                else:
                    self.load_files(selectedFiles[0])
            else:
                self.load_files(selectedFiles)

            if data_type == 'sample':
                self.retrieve_time_spectra()
                
        else:
            self.user_canceled = True

    def retrieve_time_spectra(self, auto_load=True):
        if auto_load:
            folder = self.parent.data_metadata['sample']['folder']
            o_time_spectra = LoadTimeSpectra(folder = folder, auto_load=auto_load)
            if o_time_spectra.file_found:
                time_spectra = o_time_spectra.time_spectra
                # save path   #FIXME
                base_time_spectra = FileHandler.get_base_filename(time_spectra)
                self.list_ui['time_spectra']['text'].setText(base_time_spectra)
                folder_name = FileHandler.get_parent_folder(time_spectra)
                self.list_ui['time_spectra']['folder'].setText(folder_name)
                        
        else:
            folder = self.parent.data_metadata['time_spectra']['folder']
            time_spectra_name_format = '*_Spectra.txt'
            file_name = QtGui.QFileDialog.getOpenFileName(caption = "Select the Time Spectra File",
                                                          directory = folder,
                                                          filter = "Txt ({});;All (*.*)".format(time_spectra_name_format))        
            if file_name:
                base_file_name = FileHandler.get_base_filename(file_name)
                self.list_ui['time_spectra']['text'].setText(base_file_name)
                folder_name = FileHandler.get_parent_folder(file_name)
                self.list_ui['time_spectra']['folder'].setText(folder_name)
                
        
    def load_directory(self, folder):
        list_files = glob.glob(folder + '/*.*')
        image_type = self.get_image_type(list_files)
        o_load_image = LoadImages(image_ext = image_type, 
                                  folder = folder)
        self.populate_list_widget(o_load_image)
        self.parent.data_files[self.data_type] = o_load_image.list_of_files
        self.parent.data_metadata[self.data_type]['folder'] = o_load_image.folder
        
    def populate_list_widget(self, o_loader):
        list_of_files = o_loader.list_of_files

        _list_ui = self.list_ui[self.data_type]['list']
        _list_ui.clear()
        for _row, _file in enumerate(list_of_files):
            _item = QtGui.QListWidgetItem(_file)
            _list_ui.insertItem(_row, _item)
    
        _folder = o_loader.folder
        self.folder = _folder
        
        _parent_folder = FileHandler.get_parent_folder(_folder)
        self.list_ui[self.data_type]['folder'].setText(_parent_folder)
    
    
    def load_files(self, list_of_files):
        image_type = self.get_image_type(list_of_files)
        o_load_image = LoadImages(image_ext = image_type,
                                  list_of_files = list_of_files)
        self.populate_list_widget(o_load_image)
        self.parent.data_files[self.data_type] = o_load_image.list_of_files
        self.parent.data_metadata[self.data_type]['folder'] = o_load_image.folder


    def get_image_type(self, list_of_files):
        raw_file, ext = os.path.splitext(list_of_files[0])
        return ext
        

        
class FileDialog(QtGui.QFileDialog):

    selectedFiles = []
    
    def __init__(self, *args):
        QtGui.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, False)
        self.setFileMode(self.ExistingFiles)
        btns = self.findChildren(QtGui.QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.openClicked)
        self.tree = self.findChild(QtGui.QTreeView)

    def openClicked(self):
        inds = self.tree.selectionModel().selectedIndexes()
        files = []
        for i in inds:
            if i.column() == 0:
                files.append(os.path.join(str(self.directory().absolutePath()),str(i.data().toString())))
        self.selectedFiles = files
        self.hide()

    def filesSelected(self):
        return self.selectedFiles