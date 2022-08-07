import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

class LongEndurance:
    def __init__(self, filename) -> None:
        self.handData = pd.read_table(filename,sep='\t')
        self.handData = self.handData.set_index('Time')

        # Convert data to Kg
        self.handData['Data'] = self.handData['Data'] / 2.20462262185

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

    def get_max(self, BW=None):

        self.max_force = max(self.handData['Data'])
        if not BW is None:
            self.max_force_BW = self.max_force / BW * 100
            return self.max_force, self.max_force_BW

        return self.max_force 

    #def get_
    def get_critical_force(self, BW = None):
        # Critical force is the force at which in theory you could go forever
        # Last 6 contracions in a 4 min test
        # One standard diviation cut-off was used 177.199

        closestIndex = np.abs(self.handData.index - (self.handData.index[-1] - 60)).argmin()
        lastContractionData = self.handData.iloc[closestIndex:]
        lcForce = lastContractionData['Data'][ lastContractionData['Data'] != 0]
        stdLCF = np.std(lcForce)
        meanLCF = np.mean(lcForce)
        # Critical force
        self.CF = meanLCF#+stdLCF

        # Add a cut off of 1 standard deviation
        stdCutOff = meanLCF-stdLCF
        self.CF = np.mean(lcForce[lcForce >= stdCutOff])

        if not BW is None:
            self.CF_BW = self.CF / BW * 100
            return self.CF, self.CF_BW

        return self.CF

    def get_aerobic_capacity(self):
        # Get the integral
        # find the line
        pass

    def get_anaerobic_capacity(self, BW=None):
        # Get critical force
        if 'self.CF' in locals(): # Test this
            self.get_critical_force()
        
        # Using full
        fullData = False
        if fullData:
            full_impulse = integrate.trapz(self.handData['Data'], x=self.handData.index)

            critical_force = self.handData.copy()
            nonZeroCF = critical_force['Data'] != 0
            critical_force[nonZeroCF] = self.CF

            # Integrate critical force
            full_critical_impulse = integrate.trapz(critical_force['Data'], x=critical_force.index)
            self.anaerobic_capacity = full_impulse - full_critical_impulse
        else:
            # Using part of the data
            closestIndex = np.abs(self.handData.index - 120.1).argmin()
            PEContractionData = self.handData.iloc[:closestIndex]
            PE_impulse = integrate.trapz(PEContractionData['Data'], x=PEContractionData.index)

            # Make critical force on all non-zero data points
            critical_force = PEContractionData.copy()
            nonZeroCF = critical_force['Data'] != 0
            critical_force[nonZeroCF] = self.CF
            
            # # Integrate critical force
            PE_critical_impulse = integrate.trapz(critical_force['Data'], x=critical_force.index)
            self.anaerobic_capacity = PE_impulse - PE_critical_impulse

        if not BW is None:
            self.anaerobic_capacity_BW = self.anaerobic_capacity / BW
            return self.anaerobic_capacity, self.anaerobic_capacity_BW
        
        return self.anaerobic_capacity

    def plot(self):
        labelSize = 18
        # Get critical force
        if not 'self.CF' in locals():
            self.get_critical_force()
        g = sns.relplot(data=self.handData, kind='line', legend=False)
        g.set_xlabels("Time [sec]", fontsize=labelSize)
        g.set_ylabels("Force [lb]", fontsize=labelSize)
        g.set(xlim= (min(self.handData.index), max(self.handData.index)))
        plt.axhline(y=self.CF, color='r', linestyle='--')
        plt.show()
        #concatenated = pd.concat([rightHandData.assign(dataset='set1'), leftHandData.assign(dataset='set2')])
    

