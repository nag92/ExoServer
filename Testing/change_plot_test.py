import random
import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.ax1 = self.figure1.add_subplot(111)
        self.line1, = self.ax1.plot([], [], 'r', lw=2)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.ax2 = self.figure2.add_subplot(111)
        self.line2, = self.ax2.plot([], [], 'b', lw=2)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)

        self.m_stacked_layout = QtGui.QStackedLayout()

        for canvas, toolbar in ((self.canvas1, self.toolbar1), (self.canvas2, self.toolbar2)):
            widget = QtGui.QWidget()
            lay = QtGui.QVBoxLayout(widget)
            lay.addWidget(toolbar)
            lay.addWidget(canvas)
            self.m_stacked_layout.addWidget(widget)

        self.button = QtGui.QPushButton("Plot", clicked=self.onClicked)
        layout = QtGui.QVBoxLayout(self)
        layout.addLayout(self.m_stacked_layout)
        layout.addWidget(self.button)

        timer = QtCore.QTimer(self, timeout=self.update, interval=1)
        timer.start()
        self.update()

    @QtCore.pyqtSlot()
    def update(self):
        datax = [random.random() for i in range(10)]
        datay = [random.random() for i in range(10)]

        self.line1.set_xdata(datax)
        self.line1.set_ydata(datay)
        self.ax1.relim()
        self.ax1.autoscale_view()

        self.line2.set_xdata(datax)
        self.line2.set_ydata(datay)
        self.ax2.relim()
        self.ax2.autoscale_view()

        self.canvas1.draw()
        self.canvas2.draw()

    def onClicked(self):
        ix = self.m_stacked_layout.currentIndex()
        self.m_stacked_layout.setCurrentIndex(0 if ix == 1 else 1)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())