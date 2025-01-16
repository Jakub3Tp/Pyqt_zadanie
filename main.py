import os.path
import sys
from itertools import product
from statistics import quantiles

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add_product)
        self.ui.save.clicked.connect(self.addToList)
        self.read_list()
        self.show()

    def add_product(self):
        product = self.ui.product.text()
        if len(product) > 50:
            self.ui.alert.setText("Tekst jest za długi")
        quintity = self.ui.quintity.text()
        if len(product) == 0:
            self.ui.alert.setText("Puste pola")
        elif len(quintity) == 0:
            self.ui.alert.setText("Puste pola")
        else:
            self.ui.shoplist.addItem(product + " " + quintity)

    def read_list(self):
        if os.path.exists('Lista.txt'):
            self.ui.shoplist.clear()
            with open('Lista.txt', 'r') as file:
                products = file.read().splitlines()
                for product in products:
                    self.ui.shoplist.addItem(product)

    #Coś popsułem
    #def delete(self):
    #    for p in range(self.ui.shoplist.count()):
    #        for self.ui.shoplist.item(p) == items:
    #             self.ui.shoplist.takeItem(p)
    #             break

    def addToList(self):
        with open('./Lista.txt', 'w') as file:
            for p in range(self.ui.shoplist.count()):
                file.write(f"{product}") # Pokozanie że zapisuje do pliku. nie wiem jak zapisać produkty :(
                file.write('\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())