import os
import sys
import ctypes
from hutil.Qt import QtCore, QtUiTools, QtWidgets, GtGui

panel_path = r"C:/Users/merwy/Desktop"
sys.path.append(panel_path)


def onCreateInterface():
    global mainWidget

    # Load the interface layout from the .ui file
    ui_file_path = r"C:\\Users\\merwy\\Desktopdemo.ui"
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(ui_file_path)
    ui_file.open(QtCore.QFile.ReadOnly)
    main_widget = loader.load(ui_file)

    # Connect push button to event handlers
    submit_btn = main_widget.findChild(QtWidgets.QPushButton, "pushButtonGrab")
    submit_btn.clicked.connect(Main)

    return mainWidget

def Main():
    try:
        clip = clipboardGrab()
        file = createObj(clip)
        checkCenter(file)
        checkMats(file)
    except:
        import traceback
        traceback.print_exc()