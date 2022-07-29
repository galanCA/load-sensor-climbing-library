from cgitb import handler
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

### TODO:
# get_critical_force
# get anaerobic capacity
# Add line to plot

class LongEndurance:
    def __init__(self, filename) -> None:
        self.handData = pd.read_table(filename,sep='\t')
        self.handData = self.handData.set_index('Time')

        ### Clean data
        # Delete data before the test
        offset = self.handData[self.handData['Data'] != 0].index[0]
        self.handData = self.handData.set_index(self.handData.index - offset)
        self.handData = self.handData[ self.handData.index >= 0 ]

        # Delete data after the test
        # Get all data that is not 0
        # lastData finds the last non-zero value in the test
        lastData = self.handData[self.handData['Data'] != 0 ].iloc[::-1].index[0]

        # last data index adds an index to the last non-zero value in the test
        lastDataIndex = self.handData.index.get_loc(lastData) + 2

        self.handData = self.handData.iloc[:lastDataIndex]

    def get_data(self):
        return self.handData['Data']

    def get_max(self):
        return max(self.handData['Data'])

    def get_integral(self):
        return sum(self.handData.groupby(self.handData.Data).apply(lambda g: integrate.trapz(g.Data, x=g.index)))

    def get_critical_force(self):
        # Critical force is the force at which in theory you could go forever
        # Last 6 contracions in a 4 min test
        # One standard diviation cut-off was used
        pass

    def get_aerobic_capacity(self):
        # Get the integral
        # find the line
        pass

    def get_anaerobic_capacity(self):
        pass

    def plot(self):
        labelSize = 18

        g = sns.relplot(data=self.handData, kind='line', legend=False)
        g.set_xlabels("Time [sec]", fontsize=labelSize)
        g.set_ylabels("Force [lb]", fontsize=labelSize)
        g.set(xlim= (min(self.handData.index), max(self.handData.index)))
        plt.show()
        #concatenated = pd.concat([rightHandData.assign(dataset='set1'), leftHandData.assign(dataset='set2')])
    

