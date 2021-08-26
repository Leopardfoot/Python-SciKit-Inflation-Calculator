from scikit_transformer import ScikitTest

if __name__ == '__main__':
    medexpenses = [['2010', 193.84], ['2013', 708.80]]

    ex1 = ScikitTest()

    print(ex1.transform(medexpenses))

    print(ex1.fit_transform(medexpenses))

