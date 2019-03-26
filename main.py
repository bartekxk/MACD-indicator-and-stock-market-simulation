import sys,pandas as pd, matplotlib.pyplot as plt

fields = ['Data', 'Zamkniecie']
csvFile = pd.read_csv("mwig40.csv", skipinitialspace=True, usecols=fields)

MONEY = 1000.0
DATA_SIZE = 1000

class MACD:
    def __init__(self, csv):
        self.csvFile = csv
    def rollingAverage(self,columnTo,columnFrom,period,data_size):
        self.csvFile[columnTo] = 0.0
        alpha = float(2/(period+1))
        for i in range(26,data_size):
            emaDenominator = 0.0
            emaNumerator=0.0
            for j in range (0,period+1):
                emaNumerator += self.csvFile.at[i-j, columnFrom]*((1-alpha)**j)
                emaDenominator+=((1-alpha)**j)
            ema=float(emaNumerator/emaDenominator)
            ema=round(ema,2)
            self.csvFile.at[i,columnTo]=ema
    def macd(self,data_size):
        self.csvFile['macd'] = 0.0
        for i in range(0, data_size):
            self.csvFile.at[i, 'macd'] = self.csvFile.at[i, 'ema12']-self.csvFile.at[i, 'ema26']
    def print(self):
        print(self.csvFile)
        self.csvFile.plot(y=['macd','signal'],color=['blue', 'red'])
        plt.legend(['MACD', 'SIGNAL'], loc='upper left')
        plt.xlabel('Days', fontsize=18)
        plt.ylabel('Value', fontsize=16)
        plt.show()
        self.csvFile.plot(y=['macd', 'Zamkniecie'], color=['blue', 'red'])
        plt.legend(['MACD', 'Input'], loc='upper left')
        plt.xlabel('Days', fontsize=18)
        plt.ylabel('Value', fontsize=16)
        plt.show()
    def calculate(self,data_size):
        self.rollingAverage('ema12', 'Zamkniecie', 12,data_size)
        self.rollingAverage('ema26', 'Zamkniecie', 26,data_size)
        self.macd(data_size)
        self.rollingAverage('signal', 'macd',9,data_size)
    def simulate(self,wallet,days):
        money=wallet
        shares=0.0
        macd=self.csvFile.at[26, 'macd']
        signal=self.csvFile.at[26, 'signal']
        upperCross=True
        if macd > signal:
            upperCross=False
        for day in range(27,days):
            macd = self.csvFile.at[day, 'macd']
            signal = self.csvFile.at[day, 'signal']
            sharePrice = self.csvFile.at[day, 'Zamkniecie']
            if upperCross:
                if macd > signal:
                    upperCross = False
                    if money != 0.0:
                        ratio = float(((0-macd)+100)/200)
                        if ratio > 1.0:
                            ratio = 1.0
                        if ratio > 0.0:
                            shares += (money*ratio)/sharePrice
                            money = money-(money*ratio)
            else:
                if macd < signal:
                    upperCross = True
                    ratio = float(((0 - macd) + 100) / 200)
                    if ratio > 1.0:
                        ratio = 1.0
                    if ratio > 0.0:
                        money+=sharePrice*(shares*ratio)
                        shares=shares-(shares*ratio)
        profit = (money + shares*self.csvFile.at[days-1, 'Zamkniecie'])/(self.csvFile.at[0, 'Zamkniecie']*wallet)
        print ('Units: ',money,' Shares: ',shares)
        print ('Profit: ',profit)

macdCalculate = MACD(csvFile)
macdCalculate.calculate(DATA_SIZE)
macdCalculate.print()
macdCalculate.simulate(MONEY,DATA_SIZE)