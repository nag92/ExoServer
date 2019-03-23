import abc
from TK_Plotter import TK_Plotter
import numpy as np

class FSR_BarGraph(TK_Plotter):


    def __init__(self, ID, positition, numbars=6):
        self.num_bars = np.arange(numbars)
        super(FSR_BarGraph, self).__init__(ID)

    def initilize(self,root, position):
        self.ax.set_ylim([0,1])
        self.bars = self.ax.bar(self.num_bars, [0] * len(self.num_bars), align='center', alpha=0.5)
        super(FSR_BarGraph, self).initilize(root, position)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self, data):

       [rect.set_height(h) for rect, h in zip(self.bars, data)]
       self.flush()