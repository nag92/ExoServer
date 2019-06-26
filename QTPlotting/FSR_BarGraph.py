import numpy as np

from TK_Plotter import TK_Plotter


class FSR_BarGraph(TK_Plotter):
    """
    Creates a bar graph for plotting the FSR
    """

    def __init__(self, name, object, numbars=6):
        """

        :type object: List(FSR)
        """
        self.num_bars = np.arange(numbars)
        super(FSR_BarGraph, self).__init__(object, name)

    def initilize(self, root, position):
        """
        Create the plot

        :param root: window to put the plot
        :param position: position in window to put the plot
        :return: None
        """

        self.ax.set_ylim([0, 1])
        self.bars = self.ax.bar(self.num_bars, [0] * len(self.num_bars), align='center', alpha=0.5)
        super(FSR_BarGraph, self).initilize(root, position)

    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return 1

    def update(self):
        """
        callback for to update the plot with new data
        :return:
        """
        data = []
        for sensor in self.object:
            data.append(sensor.get_values()[0])

        [rect.set_height(h) for rect, h in zip(self.bars, data)]
