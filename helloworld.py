
import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(600,300)
    w.move(700,400)
    w.show()
    sys.exit(app.exec_())