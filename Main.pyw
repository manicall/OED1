from MainWindow import MainWindow
from PyQt5 import QtWidgets
from sys import argv
app = QtWidgets.QApplication(argv)
app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
window = MainWindow()
window.setWindowTitle("Построение графиков аппроксимации")
window.show()
app.exec()
