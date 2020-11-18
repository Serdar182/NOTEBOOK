import sys
from Sql import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pen = Pencere()
        self.setCentralWidget(self.pen)
        self.init_ui()

    def init_ui(self):
        menu = self.menuBar()
        dosya = menu.addMenu("Dosya")
        dosya_kayıt = QAction("Dosya Kayıt et", self)
        dosya_kayıt.setShortcut("Ctrl+S")
        dosya_ac = QAction("Dosya aç", self)
        dosya_ac.setShortcut("Ctrl+O")
        kapat = QAction("Çık", self)
        kapat.setShortcut("Ctrl+Q")
        dosya.addAction(dosya_kayıt)
        dosya.addAction(dosya_ac)
        dosya.addAction(kapat)
        dosya_kayıt.triggered.connect(self.pen.Veri_K)
        dosya_ac.triggered.connect(self.pen.Veri_A)
        kapat.triggered.connect(self.cik)
        self.show()

    def cik(self):
        qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = Main()
    sys.exit(app.exec_())