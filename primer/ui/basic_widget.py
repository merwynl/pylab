from PySide2 import QtGui, QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

"""
[Creating a dialog with some Widgets using PySide2 module]
"""

WINDOW_TITLE = "Main Window"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle(WINDOW_TITLE)
        self.setMinimumWidth(WINDOW_WIDTH)
        self.setMinimumHeight(WINDOW_HEIGHT)

        # Remove the ? from the dialog on Windows
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        # Attach widgets and layouts to window
        self.create_widget()
        self.create_layouts()

    def create_widget(self):
        """
        [Create widgets]
        """
        self.line_edit = QtWidgets.QLineEdit()
        self.check_box1 = QtWidgets.QCheckBox('Checkbox 1')
        self.check_box2 = QtWidgets.QCheckBox('Checkbox 2')
        self.button1 = QtWidgets.QPushButton('Button 1')
        self.button2 = QtWidgets.QPushButton('Button 2')

    def create_layouts(self):
        # Creating a vertical box layout and connecting the the dialog instance to the layout
        main_layout = QtWidgets.QVBoxLayout(self)

        # Adding the widgets to the layout
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(self.check_box1)
        main_layout.addWidget(self.check_box2)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)


if __name__ == "__main__":
    dialog = TestDialog()
    dialog.show()


