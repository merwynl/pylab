from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import pymel.core as pm


"""
[Creating a dialog window using Qt module]
"""

WINDOW_TITLE = "Main Window"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class test_dialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(test_dialog, self).__init__(parent)

        self.setWindowTitle(WINDOW_TITLE)
        self.setMinimumWidth(WINDOW_WIDTH)
        self.setMinimumHeight(WINDOW_HEIGHT)

        # Remove the ? from the dialog on Windows
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)


if __name__ == "__main__":
    dialog = test_dialog()
    dialog.show()