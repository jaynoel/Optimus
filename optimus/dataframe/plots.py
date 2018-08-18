import numpy as np
import seaborn as sns
from pyspark.ml.stat import Correlation
from pyspark.sql import DataFrame

from optimus.functions import plot_hist, plot_freq
from optimus.helpers.decorators import add_attr
from optimus.helpers.functions import parse_columns


def plots(self):
    @add_attr(plots)
    def hist(columns=None, buckets=10):
        """
        Plot histogram
        :param columns: Columns to be printed
        :param buckets: Number of buckets
        :return:
        """
        columns = parse_columns(self, columns)

        for col_name in columns:
            data = self.cols.hist(col_name, buckets)
            plot_hist({col_name: data}, output="image")

    @add_attr(plots)
    def frequency(columns=None, buckets=10):
        """
        Plot frequency chart
        :param columns: Columns to be printed
        :param buckets: Number of buckets
        :return:
        """
        columns = parse_columns(self, columns)

        for col_name in columns:
            data = self.cols.frequency(col_name, buckets)
            plot_freq({col_name: data}, output="image")

    @add_attr(plots)
    def correlation(vec_col, method="pearson"):
        """
        Compute the correlation matrix for the input dataset of Vectors using the specified method. Method
        mapped from  pyspark.ml.stat.Correlation.
        :param vec_col: The name of the column of vectors for which the correlation coefficient needs to be computed.
        This must be a column of the dataset, and it must contain Vector objects.
        :param method: String specifying the method to use for computing correlation. Supported: pearson (default),
        spearman.
        :return: Heatmap plot of the corr matrix using seaborn.
        """

        assert isinstance(method, str), "Error, method argument provided must be a string."

        assert method == 'pearson' or (
                method == 'spearman'), "Error, method only can be 'pearson' or 'sepearman'."

        cor = Correlation.corr(self._df, vec_col, method).head()[0].toArray()
        return sns.heatmap(cor, mask=np.zeros_like(cor, dtype=np.bool), cmap=sns.diverging_palette(220, 10,
                                                                                                   as_cmap=True))

    return plots


DataFrame.plots = property(plots)