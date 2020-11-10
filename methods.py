import numpy
import pandas
class Methods:

    @staticmethod
    def encode_cat_col(col) -> list:
        """encodes a categorical column using the first item encountered

        input: col -> a pandas series

        output: res -> a list of encodings
        """
        counts = list(col.value_counts())
        uniques = col.unique()
        target = uniques[counts.index(max(counts))] #gets the item that corresponds to the index in the uniques array
        res = []
        for item in col:
            if item == target:
                res.append(1)
            else:
                res.append(0)
        return res

    @staticmethod
    def encode_num_col(col) -> list:
        """encodes a numerical column using the mean as fill for NaN values and doing it in place
        
        input: col -> a pandas series"""
        mean = col.mean()
        res = []
        for item in col:
            if item == numpy.nan:
                res.append(mean)
            else:
                res.append(item)
        return res

    @staticmethod
    def encode_all_col(df: pandas.DataFrame) -> pandas.DataFrame:
        """encodes a dataframe by filling nan values with most appeared
        item in a categorical column and the mean in a numerical col"""
        fin = dict()
        for name,col in df.iteritems():
            if col.dtype == numpy.dtype('O'):
                tem = Methods.encode_cat_col(col)
                fin[name] = tem
            else:
                tem = col.fillna(col.mean())
                fin[name] = tem
        return pandas.DataFrame(fin)