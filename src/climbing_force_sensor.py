from cgitb import handler
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

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
        lastData = self.handData[self.handData['Data'] != 0 ].iloc[::-1].index[0]
        # todo: figure out how to add one more index
        self.handData = self.handData.loc[:lastData]

    def get_data(self):
        return self.handData['Data']

    def get_max(self):
        return max(self.handData['Data'])

    def get_integral(self):
        return sum(self.handData.groupby(self.handData.Data).apply(lambda g: integrate.trapz(g.Data, x=g.index)))

    def get_aerobic_capacity(self):
        pass

    def plot(self):
        labelSize = 18

        g = sns.relplot(data=self.handData, kind='line', legend=False)
        g.set_xlabels("Time [sec]", fontsize=labelSize)
        g.set_ylabels("Force [lb]", fontsize=labelSize)
        g.set(xlim= (min(self.handData.index), max(self.handData.index)))
        plt.show()
        #concatenated = pd.concat([rightHandData.assign(dataset='set1'), leftHandData.assign(dataset='set2')])
    

