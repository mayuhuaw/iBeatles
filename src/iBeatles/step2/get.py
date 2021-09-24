class Get:

    def __init__(self, parent=None):
        self.parent = parent

    def roi_table_row(self, row=-1):
        if row == -1:
            return []

        # use flag
        _flag_widget = self.parent.ui.normalization_tableWidget.cellWidget(row, 0)
        if _flag_widget is None:
            raise ValueError
        flag = _flag_widget.isChecked()

        # x0
        _item = self.parent.ui.normalization_tableWidget.item(row, 1)
        if _item is None:
            raise ValueError
        x0 = str(_item.text())

        # y0
        _item = self.parent.ui.normalization_tableWidget.item(row, 2)
        if _item is None:
            raise ValueError
        y0 = str(_item.text())

        # width
        _item = self.parent.ui.normalization_tableWidget.item(row, 3)
        if _item is None:
            raise ValueError
        width = str(_item.text())

        # height
        _item = self.parent.ui.normalization_tableWidget.item(row, 4)
        if _item is None:
            raise ValueError
        height = str(_item.text())

        # region type
        _text_widget = self.parent.ui.normalization_tableWidget.cellWidget(row, 5)
        region_type = _text_widget.currentText()

        return [flag, x0, y0, width, height, region_type]