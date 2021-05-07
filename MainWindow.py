from PyQt5 import QtGui, QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from data import *

class Model(QtGui.QStandardItemModel):
    def __init__(self):
        QtGui.QStandardItemModel.__init__(self,len(x), 2)
        # инициализация
        # заполнение ячеек пустым текстом, чтобы их можно было закрасить
        for i in enumerate(x):
            self.setItem(i[0], 0, self.get_item(str(i[1])))
        for i in enumerate(y):
            self.setItem(i[0], 1, self.get_item(str(i[1])))
        # изменение заголовков
        self.setHorizontalHeaderLabels(["X", "Y"])

    @staticmethod
    def get_item(str):
        item = QtGui.QStandardItem(str)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setEditable(False)
        item.setSelectable(False)
        return item

class Table(QtWidgets.QTableView):
    def __init__(self):
        QtWidgets.QTableView.__init__(self)
        model = Model()
        self.setModel(model)
        for i in range(model.columnCount()):
            self.setColumnWidth(i, 100)
        self.resizeRowsToContents()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlabel("X")
        self.axes.set_ylabel("Y")
        super(MplCanvas, self).__init__(self.fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.funcs = None
        sc = MplCanvas()
        self.old_sc = sc
        toolbar = NavigationToolbar(sc, self)
        # menubar============================================
        menuBar = self.menuBar()
        action = menuBar.addAction("Линейная аппроксимация", self.LinearAp)
        action = menuBar.addAction("Степенная аппроксимация", self.PowAp)
        action = menuBar.addAction("Экспоненциальная аппроксимация", self.ExpAp)

        # grid2=============================================
        self.grid1 = QtWidgets.QGridLayout()
        # формирование списка label
        Qlabels = [QtWidgets.QLabel("") for i in range(6)]
        for label in Qlabels:
            label.setAlignment(QtCore.Qt.AlignHCenter)
        Qlabels[0].setText("a")
        Qlabels[1].setText("b")
        Qlabels[2].setText("M")
        Qlabels[3].setText("D")
        Qlabels[4].setText("R")
        Qlabels[5].setText("Y")
        Qlabels[5].setFixedWidth(150)
        # добавление label на слой
        for label in enumerate(Qlabels):
            self.grid1.addWidget(label[1], 0, label[0])
        # формирование списка edit
        self.grid_lineEdits = []
        self.grid_lineEdits = [QtWidgets.QLineEdit("") for i in range(6)]
        # отключение доступа к edit
        for edit in self.grid_lineEdits:
            edit.setReadOnly(True)
        # добавление edit на слой
        for edit in enumerate(self.grid_lineEdits):
            self.grid1.addWidget(edit[1], 1, edit[0])
        # child_layout===============================================
        self.child_layout = QtWidgets.QVBoxLayout()
        self.child_layout.addWidget(toolbar)
        self.child_layout.addWidget(sc)
        # parent_layout===============================================
        self.parent_layout = QtWidgets.QVBoxLayout()
        self.parent_layout.addLayout(self.grid1)
        self.parent_layout.addLayout(self.child_layout)

        self.grid_ListView = QtWidgets.QGridLayout()

        self.main_Layout = QtWidgets.QHBoxLayout()
        self.main_Layout.addWidget(Table())
        self.main_Layout.addLayout(self.parent_layout)

        # widget==============================================
        widget = QtWidgets.QWidget()
        widget.setLayout(self.main_Layout)
        self.setCentralWidget(widget)

        self.show()

    def add_graphic(self, x, y, fx):
        sc = MplCanvas()
        toolbar = NavigationToolbar(sc, self)
        for i in range(self.child_layout.count()):
            self.child_layout.takeAt(0).widget().deleteLater()
        self.child_layout.addWidget(toolbar)
        self.child_layout.addWidget(sc)
        sc.axes.plot(x, y)
        sc.axes.plot(x, fx)

    def LinearAp(self):
        sc = MplCanvas()
        toolbar = NavigationToolbar(sc, self)
        for i in range(self.child_layout.count()):
            self.child_layout.takeAt(0).widget().deleteLater()
        self.child_layout.addWidget(toolbar)
        self.child_layout.addWidget(sc)

        a = a0(x, y)
        b = a1(x, y)

        f = lambda x: a + b * x
        fx = f(x)

        self.grid_lineEdits[0].setText(str(a))
        self.grid_lineEdits[1].setText(str(b))
        self.grid_lineEdits[2].setText(str(M(y, fx)))
        self.grid_lineEdits[3].setText(str(D(y, fx)))
        self.grid_lineEdits[4].setText(str(R(y, fx)))
        self.grid_lineEdits[5].setText(f'{round(b, 4)}x+{round(a, 4)}')
        self.add_graphic(x, y, fx)

    def PowAp(self):
        _a = a0(LnX, LnY)
        a = np.exp(_a)
        b = a1(LnX, LnY)

        def f(x):
            return a * x ** b

        fx = f(x[1:])

        self.grid_lineEdits[0].setText(str(a))
        self.grid_lineEdits[1].setText(str(b))
        self.grid_lineEdits[2].setText(str(M(y[1:], fx)))
        self.grid_lineEdits[3].setText(str(D(y[1:], fx)))
        self.grid_lineEdits[4].setText(str(R(y[1:], fx)))
        self.grid_lineEdits[5].setText(f'{round(a, 4)}*x^({(round(b, 4))})')
        self.add_graphic(x[1:], y[1:], fx)

    def ExpAp(self):
        _a = a0(x[1:], LnY)
        a = np.exp(_a)
        b = a1(x[1:], LnY)

        f = lambda x: a * np.exp(b * x)
        fx = f(x[1:])
        self.grid_lineEdits[0].setText(str(a))
        self.grid_lineEdits[1].setText(str(b))
        self.grid_lineEdits[2].setText(str(M(y[1:], fx)))
        self.grid_lineEdits[3].setText(str(D(y[1:], fx)))
        self.grid_lineEdits[4].setText(str(R(y[1:], fx)))
        self.grid_lineEdits[5].setText(f'{round(a, 4)}*exp^({round(b, 4)}*x)')
        self.add_graphic(x[1:], y[1:], fx)
