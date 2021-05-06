from PyQt5 import QtGui, QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from data import *

class Model(QtGui.QStandardItemModel):
    def __init__(self):
        QtGui.QStandardItemModel.__init__(self, 2, len(x))
        # инициализация
        # заполнение ячеек пустым текстом, чтобы их можно было закрасить
        for i in enumerate(x):
            self.setItem(0, i[0], self.get_item(str(round(i[1]))))
        for i in enumerate(y):
            self.setItem(1, i[0], self.get_item(str(i[1])))
        # изменение заголовков
        self.setVerticalHeaderLabels(["X", "Y"])

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
        self.setFixedSize(700,90)
        self.horizontalHeader().setStyleSheet( "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:white;")
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
        self.axes.grid()
        super(MplCanvas, self).__init__(self.fig)






class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # parent_layout===============================================
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.addLayout(self.GetGrid())
        self.LeftLayout.addLayout(self.GetPushButtonLayout())

        self.GraphicLayout = self.GetGraphicLayout()
        self.parent_layout = QtWidgets.QHBoxLayout()
        self.parent_layout.addLayout(self.LeftLayout)
        self.parent_layout.addLayout(self.GraphicLayout)

        self.grid_ListView = QtWidgets.QGridLayout()

        self.main_Layout = QtWidgets.QVBoxLayout()
        self.main_Layout.addLayout(self.parent_layout)
        self.main_Layout.addWidget(Table())

        # widget==============================================
        widget = QtWidgets.QWidget()
        widget.setLayout(self.main_Layout)
        self.setCentralWidget(widget)
        self.show()

    def GetPushButtonLayout(self):
        PushButtons = [QtWidgets.QPushButton() for i in range(3)]
        PushButtons[0].setText("Линейная аппроксимация")
        PushButtons[1].setText("Степенная аппроксимация")
        PushButtons[2].setText("Экспоненциальная аппроксимация")
        PushButtons[0].clicked.connect(self.LinearAp)
        PushButtons[1].clicked.connect(self.PowAp)
        PushButtons[2].clicked.connect(self.ExpAp)

        layout = QtWidgets.QVBoxLayout()
        for button in PushButtons:
            layout.addWidget(button)
        return layout

    def GetGraphicLayout(self):
        self.funcs = None
        sc = MplCanvas()
        self.old_sc = sc
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(sc)
        return layout

    def GetGrid(self):
        grid = QtWidgets.QGridLayout()
        # формирование списка label
        Qlabels = [QtWidgets.QLabel("") for i in range(6)]
        Qlabels[0].setText("a")
        Qlabels[1].setText("b")
        Qlabels[2].setText("M")
        Qlabels[3].setText("D")
        Qlabels[4].setText("R")
        Qlabels[5].setText("Y")
        # добавление label на слой
        for label in enumerate(Qlabels):
            grid.addWidget(label[1], label[0], 0)
        # формирование списка edit
        self.grid_lineEdits = []
        self.grid_lineEdits = [QtWidgets.QLineEdit("") for i in range(6)]
        # отключение доступа к edit
        for edit in self.grid_lineEdits:
            edit.setReadOnly(True)
        # добавление edit на слой
        for edit in enumerate(self.grid_lineEdits):
            grid.addWidget(edit[1], edit[0], 1)

        grid.setAlignment(QtCore.Qt.AlignTop)
        return grid

    def add_graphic(self, x, y, fx):
        sc = MplCanvas()
        for i in range(self.GraphicLayout.count()):
            self.GraphicLayout.takeAt(0).widget().deleteLater()
        self.GraphicLayout.addWidget(sc)
        sc.axes.plot(x, y)
        sc.axes.plot(x, fx, color='red', linestyle=':')

    def LinearAp(self):
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
        self.grid_lineEdits[5].setText(f'{round(b, 4)}^(x)*{round(a, 4)}')
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
