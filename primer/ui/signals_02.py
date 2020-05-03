from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import QLineEdit
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
        # self.setMinimumHeight(WINDOW_HEIGHT)

        # Remove the ? from the dialog on Windows
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        # Attach widgets and layouts to window
        self.create_widget()
        self.create_layouts()
        self.create_connections()

    def create_widget(self):
        """
        [Create widgets]
        """
        self.line_edit = QtWidgets.QLineEdit()
        self.checkbox_hidden = QtWidgets.QCheckBox()
        self.checkbox_locked = QtWidgets.QCheckBox()
        self.btn_ok = QtWidgets.QPushButton('Ok')
        self.btn_cancel = QtWidgets.QPushButton('Cancel')

    def create_layouts(self):
        # Creating a form layout and adding rows to it
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('Name: ', self.line_edit)
        form_layout.addRow('Hidden: ', self.checkbox_hidden)
        form_layout.addRow('Locked: ', self.checkbox_locked)

        # Creating a horizontal layout and adding the button widgets to it
        btn_layout = QtWidgets.QHBoxLayout()

        # Maintains relative sizing of buttons
        btn_layout.addStretch()

        # Add widgets
        btn_layout.addWidget(self.btn_ok)
        btn_layout.addWidget(self.btn_cancel)

        # Creating a vertical box layout and connecting the the dialog instance to the layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)

    def create_connections(self):
        """
        [Creates a series of signals to connect the buttons to some functionality]
        """
        #  Initiates the close function and attach it to a button
        self.line_edit.editingFinished.connect(self.print_hello_name)

        #  Initiates the close function and attach it to a button
        self.btn_cancel.clicked.connect(self.close)

        #  Initiates the close function and attach it to a button
        self.checkbox_hidden.toggled.connect(self.print_is_hidden)

    def print_hello_name(self):
        """
        [Creates a series of signals to connect the buttons to some functionality]
        """
        name = self.line_edit.text()
        print('Hello {0}!'.format(name))

    def print_is_hidden(self):
        """
        [Print hidden status]
        """
        hidden = self.checkbox_hidden.isChecked()
        if hidden:
            print('Hidden')
        else:
            print('Visible')


if __name__ == "__main__":
    # Using a try and except in order to close an existing dialog instance before launching
    try:
        # noinspection PyUnboundLocalVariable
        test_dialog.close()  # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
