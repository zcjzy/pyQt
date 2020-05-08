import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class MainWin(QMainWindow):
    def  __init__(self,parent=None):
        super(MainWin, self).__init__(parent)
        self.setWindowTitle('第1个窗口')
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('ddd',5000)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w = MainWin()
    w.resize(600, 300)
    w.move(700, 400)

    w.show()
    sys.exit(app.exec_())
