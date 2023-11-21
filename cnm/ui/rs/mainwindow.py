from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from PyQt5.QtWidgets import QStatusBar, QLabel

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.label = self.findChild(QLabel, "MyStatusBarNewLabel")
        self.edit = self.findChild(QStatusBar, "statusbar")
        self.edit.messageChanged.connect(self.changeText)

    def changeText(self):
        self.label.setText(self.edit.currentMessage())

    # add any custom methods hereeee

    def on_exitAppBtn_clicked(self):
        self.app.quit()

