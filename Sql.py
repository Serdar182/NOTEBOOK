import sqlite3
import os
import sqlite3
import sys
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.baglanmak()
        self.init_ui()

    def baglanmak(self,data="Veri.db"):
        self.bag = sqlite3.connect(data)
        self.cur = self.bag.cursor()
        self.cur.execute("CREATE table if not exists veri (İsim TEXT,No TEXT)")
        self.bag.commit()

    def gorsel(self):
        self.giris1 = QLineEdit()
        self.giris2 = QLineEdit()
        self.button = QPushButton("Bilgiyi Kayıt Et")
        self.buttonS = QPushButton("Bilgiyi Sil")
        self.metin = QTextEdit()

        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()

        h_box3.addWidget(self.button)
        h_box3.addWidget(self.buttonS)
        h_box.addWidget(self.giris1)
        h_box.addWidget(self.giris2)

        v_box.addLayout(h_box)
        v_box.addLayout(h_box3)

        h_box2.addLayout(v_box)
        h_box2.addWidget(self.metin)

        self.setLayout(h_box2)

    def init_ui(self):
        self.gorsel()
        self.button.clicked.connect(self.Bilgi_K)
        self.buttonS.clicked.connect(self.Bilgi_S)
        self.Veri_G()


    def Bilgi_K(self):
        Ad = self.giris1.text()
        No = int(self.giris2.text())
        self.cur.execute("INSERT into veri values(?,?)",(Ad,No))
        self.bag.commit()
        self.Veri_G()

    def Bilgi_S(self):
        Ad = self.giris1.text()
        self.cur.execute("DELETE from veri where İsim = ?",(Ad,))
        self.bag.commit()
        self.Veri_G()

    def Veri_K(self):

        dosya_ismi = QFileDialog.getSaveFileName(self,"Veriyi kayıt et","Veri_1.db",os.getenv("HOME"))
        if dosya_ismi[0] == "":
            pass
        else:
            Date = self.Veri_G2()
            self.baglanmak(dosya_ismi[0])
            for i in Date:
                self.cur.execute("INSERT into veri values(?,?)", (i[0], i[1]))
            self.bag.commit()

    def Veri_A(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Veri Aç","","Data Files (*.db)", os.getenv("HOME"))
        if dosya_ismi[0] == "":
            pass
        else:
            self.baglanmak(dosya_ismi[0])
            print(dosya_ismi[0])
            self.Veri_G()

    def Veri_G(self):
        self.cur.execute("SELECT * from veri")
        Bilgi = self.cur.fetchall()
        a = ""
        for i in Bilgi:
            a += str(i[0])+" "+str(i[1])+"\n"
        self.metin.setText(a)

    def Veri_G2(self):
        self.cur.execute("SELECT * from veri")
        Bilgi = self.cur.fetchall()
        return Bilgi