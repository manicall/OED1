from MainWindow import MainWindow
from PyQt5 import QtWidgets
from sys import argv
app = QtWidgets.QApplication(argv)
window = MainWindow()
window.setWindowTitle("Решение уравнений")
window.show()
app.exec()
