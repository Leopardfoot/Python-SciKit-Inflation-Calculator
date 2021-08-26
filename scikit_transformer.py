import csv
from sklearn.base import TransformerMixin

class ScikitTest(TransformerMixin):

    #Set a dictionary so that the Consumer Price Index can work on a key value pair of Year: CPI. Very easy to source
    #for future use.
    yearindex = {}

    def __init__(self):

        rows = []
        #example = [[2010, 193.84], [2013, 708.80]]

        #Opens the csv and reads it then populates a list with each index another list item of two values the year
        #and CPI
        with open('./yearly_med_index.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                rows.append(row)

        #remove the heading
        headings = rows.pop(0)
        for x in rows:
            self.yearindex[x[0]] = x[1]



    #fit only needs to take the argument and return self.
    def fit(self, X):

        return self

    #transform takes an array of paramaters [[year, price], [year, price], ...] and adjusts the price for each array
    #item based on inflation.
    def transform(self, X):
        X_out = []
        for i in X:
            tmp = []
            year = str(i[0])
            price = i[1]
            pointchange = float(self.yearindex['2021']) - float(self.yearindex[year])
            percentchange = pointchange / float(self.yearindex[year])
            adjprice = float(price) + (price * percentchange)
            roundprice = round(adjprice, 2)
            tmp.append(year)
            tmp.append(roundprice)
            X_out.append(tmp)
        return X_out




