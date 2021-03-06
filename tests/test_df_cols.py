from pyspark.sql.types import *
from optimus import Optimus
from pyspark.ml.linalg import Vectors, VectorUDT, DenseVector
import numpy as np

nan = np.nan
import datetime
from pyspark.sql import functions as F

op = Optimus(master='local')
source_df = op.create.df(
    [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
     ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
     ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
     ('date arrival', StringType(), True), ('last date seen', StringType(), True),
     ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
     ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
     ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000,
                                                                                  4.300000190734863,
                                                                                  ['Inochi', 'Convoy'],
                                                                                  '19.442735,-99.201111', '1980/04/10',
                                                                                  '2016/09/10',
                                                                                  [8.53439998626709, 4300.0],
                                                                                  datetime.date(2016, 9, 10),
                                                                                  datetime.datetime(2014, 6, 24, 0, 0),
                                                                                  True, bytearray(b'Leader'), None), (
                                                                                 'bumbl#ebéé  ', 17, 'Espionage', 7,
                                                                                 5000000, 2.0, ['Bumble', 'Goldback'],
                                                                                 '10.642707,-71.612534', '1980/04/10',
                                                                                 '2015/08/10',
                                                                                 [5.334000110626221, 2000.0],
                                                                                 datetime.date(2015, 8, 10),
                                                                                 datetime.datetime(2014, 6, 24, 0, 0),
                                                                                 True, bytearray(b'Espionage'), None), (
                                                                                 'ironhide&', 26, 'Security', 7,
                                                                                 5000000, 4.0, ['Roadbuster'],
                                                                                 '37.789563,-122.400356', '1980/04/10',
                                                                                 '2014/07/10',
                                                                                 [7.924799919128418, 4000.0],
                                                                                 datetime.date(2014, 6, 24),
                                                                                 datetime.datetime(2014, 6, 24, 0, 0),
                                                                                 True, bytearray(b'Security'), None), (
                                                                                 'Jazz', 13, 'First Lieutenant', 8,
                                                                                 5000000, 1.7999999523162842,
                                                                                 ['Meister'], '33.670666,-117.841553',
                                                                                 '1980/04/10', '2013/06/10',
                                                                                 [3.962399959564209, 1800.0],
                                                                                 datetime.date(2013, 6, 24),
                                                                                 datetime.datetime(2014, 6, 24, 0, 0),
                                                                                 True, bytearray(b'First Lieutenant'),
                                                                                 None), (
                                                                                 'Megatron', None, 'None', 10, 5000000,
                                                                                 5.699999809265137, ['Megatron'], None,
                                                                                 '1980/04/10', '2012/05/10',
                                                                                 [None, 5700.0],
                                                                                 datetime.date(2012, 5, 10),
                                                                                 datetime.datetime(2014, 6, 24, 0, 0),
                                                                                 True, bytearray(b'None'), None), (
                                                                                 'Metroplex_)^$', 300, 'Battle Station',
                                                                                 8, 5000000, None, ['Metroflex'], None,
                                                                                 '1980/04/10', '2011/04/10',
                                                                                 [91.44000244140625, None],
                                                                                 datetime.date(2011, 4, 10),
                                                                                 datetime.datetime(2014, 6, 24, 0, 0),
                                                                                 True, bytearray(b'Battle Station'),
                                                                                 None)])


class Testdf_cols(object):
    @staticmethod
    def test_cols_min():
        actual_df = source_df.cols.min('height(ft)')
        expected_value = 13
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_min_all_columns():
        actual_df = source_df.cols.min('*')
        expected_value = {'names': {'min': 'Jazz'}, 'height(ft)': {'min': 13}, 'function': {'min': 'Battle Station'},
                          'rank': {'min': 7}, 'age': {'min': 5000000}, 'weight(t)': {'min': 1.8},
                          'japanese name': {'min': ['Bumble', 'Goldback']},
                          'last position seen': {'min': '10.642707,-71.612534'}, 'date arrival': {'min': '1980/04/10'},
                          'last date seen': {'min': '2011/04/10'}, 'attributes': {'min': [None, 5700.0]},
                          'DateType': {'min': datetime.date(2011, 4, 10)},
                          'Tiemstamp': {'min': datetime.datetime(2014, 6, 24, 0, 0)}, 'Cybertronian': {'min': 1},
                          'function(binary)': {'min': bytearray(b'Battle Station')}, 'NullType': {'min': None}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_max():
        actual_df = source_df.cols.max('height(ft)')
        expected_value = 300
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_max_all_columns():
        actual_df = source_df.cols.max('*')
        expected_value = {'names': {'max': 'ironhide&'}, 'height(ft)': {'max': 300}, 'function': {'max': 'Security'},
                          'rank': {'max': 10}, 'age': {'max': 5000000}, 'weight(t)': {'max': 5.7},
                          'japanese name': {'max': ['Roadbuster']},
                          'last position seen': {'max': '37.789563,-122.400356'}, 'date arrival': {'max': '1980/04/10'},
                          'last date seen': {'max': '2016/09/10'}, 'attributes': {'max': [91.44000244140625, None]},
                          'DateType': {'max': datetime.date(2016, 9, 10)},
                          'Tiemstamp': {'max': datetime.datetime(2014, 6, 24, 0, 0)}, 'Cybertronian': {'max': 1},
                          'function(binary)': {'max': bytearray(b'Security')}, 'NullType': {'max': None}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_range():
        actual_df = source_df.cols.range('height(ft)')
        expected_value = {'height(ft)': {'min': 13, 'max': 300}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_range_all_columns():
        actual_df = source_df.cols.range('*')
        expected_value = {'names': {'min': 'Jazz', 'max': 'ironhide&'}, 'height(ft)': {'min': 13, 'max': 300},
                          'function': {'min': 'Battle Station', 'max': 'Security'}, 'rank': {'min': 7, 'max': 10},
                          'age': {'min': 5000000, 'max': 5000000}, 'weight(t)': {'min': 1.8, 'max': 5.7},
                          'japanese name': {'min': ['Bumble', 'Goldback'], 'max': ['Roadbuster']},
                          'last position seen': {'min': '10.642707,-71.612534', 'max': '37.789563,-122.400356'},
                          'date arrival': {'min': '1980/04/10', 'max': '1980/04/10'},
                          'last date seen': {'min': '2011/04/10', 'max': '2016/09/10'},
                          'attributes': {'min': [None, 5700.0], 'max': [91.44000244140625, None]},
                          'DateType': {'min': datetime.date(2011, 4, 10), 'max': datetime.date(2016, 9, 10)},
                          'Tiemstamp': {'min': datetime.datetime(2014, 6, 24, 0, 0),
                                        'max': datetime.datetime(2014, 6, 24, 0, 0)},
                          'Cybertronian': {'min': 1, 'max': 1},
                          'function(binary)': {'min': bytearray(b'Battle Station'), 'max': bytearray(b'Security')},
                          'NullType': {'min': None, 'max': None}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_median():
        actual_df = source_df.cols.median('height(ft)')
        expected_value = 13.0
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_median_all_columns():
        actual_df = source_df.cols.median('*')
        expected_value = {'weight(t)': 1.7999999523162842, 'rank': 7.0, 'age': 5000000.0, 'height(ft)': 13.0}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_percentile():
        actual_df = source_df.cols.percentile('height(ft)', [0.05, 0.25], 1)
        expected_value = {0.05: 13.0, 0.25: 13.0}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_percentile_all_columns():
        actual_df = source_df.cols.percentile('*', [0.05, 0.25], 1)
        expected_value = {'weight(t)': {0.05: 1.7999999523162842, 0.25: 1.7999999523162842},
                          'rank': {0.05: 7.0, 0.25: 7.0}, 'age': {0.05: 5000000.0, 0.25: 5000000.0},
                          'height(ft)': {0.05: 13.0, 0.25: 13.0}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_mad():
        actual_df = source_df.cols.mad('height(ft)')
        expected_value = 0.0
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_mad_all_columns():
        actual_df = source_df.cols.mad('*')
        expected_value = {'weight(t)': 0.0, 'rank': 0.0, 'age': 0.0, 'height(ft)': 0.0}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_std():
        actual_df = source_df.cols.std('height(ft)')
        expected_value = 124.92678
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_std_all_columns():
        actual_df = source_df.cols.std('*')
        expected_value = {'weight(t)': {'stddev': 1.64712}, 'rank': {'stddev': 1.36626}, 'age': {'stddev': 0.0},
                          'height(ft)': {'stddev': 124.92678}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_kurt():
        actual_df = source_df.cols.kurt('height(ft)')
        expected_value = 0.23772
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_mean():
        actual_df = source_df.cols.mean('height(ft)')
        expected_value = 76.8
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_mean_all_columns():
        actual_df = source_df.cols.mean('*')
        expected_value = {'weight(t)': {'mean': 3.56}, 'rank': {'mean': 8.33333}, 'age': {'mean': 5000000.0},
                          'height(ft)': {'mean': 76.8}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_skewness():
        actual_df = source_df.cols.skewness('height(ft)')
        expected_value = 1.49074
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_sum():
        actual_df = source_df.cols.sum('height(ft)')
        expected_value = 384
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_sum_all_columns():
        actual_df = source_df.cols.sum('*')
        expected_value = {'weight(t)': {'sum': 17.8}, 'rank': {'sum': 50}, 'age': {'sum': 30000000},
                          'height(ft)': {'sum': 384}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_variance():
        actual_df = source_df.cols.variance('height(ft)')
        expected_value = 15606.7
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_variance_all_columns():
        actual_df = source_df.cols.variance('*')
        expected_value = {'weight(t)': {'variance': 2.713}, 'rank': {'variance': 1.86667}, 'age': {'variance': 0.0},
                          'height(ft)': {'variance': 15606.7}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_abs():
        actual_df = source_df.cols.abs('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_abs_all_columns():
        actual_df = source_df.cols.abs('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_mode():
        actual_df = source_df.cols.mode('height(ft)')
        expected_value = [{'height(ft)': None}]
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_mode_all_columns():
        actual_df = source_df.cols.mode('*')
        expected_value = [{'names': None}, {'height(ft)': None}, {'function': None}, {'rank': [8, 7, 10]},
                          {'age': 5000000}, {'weight(t)': None}, {'japanese name': None}, {'last position seen': None},
                          {'date arrival': '1980/04/10'}, {'last date seen': None}, {'attributes': None},
                          {'DateType': None}, {'Tiemstamp': datetime.datetime(2014, 6, 24, 0, 0)},
                          {'Cybertronian': True}, {'function(binary)': None}, {'NullType': None}]
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count():
        actual_df = source_df.cols.count()
        expected_value = 16
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count_na():
        actual_df = source_df.cols.count_na('height(ft)')
        expected_value = 1
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count_na_all_columns():
        actual_df = source_df.cols.count_na('*')
        expected_value = {'names': 0,
                          'height(ft)': 1,
                          'function': 0,
                          'rank': 0,
                          'age': 0,
                          'weight(t)': 1,
                          'japanese name': 0,
                          'last position seen': 2,
                          'date arrival': 0,
                          'last date seen': 0,
                          'attributes': 0,
                          'DateType': 0,
                          'Tiemstamp': 0,
                          'Cybertronian': 0,
                          'function(binary)': 0,
                          'NullType': 0}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count_zeros():
        actual_df = source_df.cols.count_zeros('height(ft)')
        expected_value = 0
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count_zeros_all_columns():
        actual_df = source_df.cols.count_zeros('*')
        expected_value = {'weight(t)': 0, 'rank': 0, 'age': 0, 'height(ft)': 0}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count_uniques():
        actual_df = source_df.cols.count_uniques('height(ft)')
        expected_value = 5
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_count_uniques_all_columns():
        actual_df = source_df.cols.count_uniques('*')
        expected_value = {'names': {'approx_count_distinct': 5}, 'height(ft)': {'approx_count_distinct': 5},
                          'function': {'approx_count_distinct': 6}, 'rank': {'approx_count_distinct': 3},
                          'age': {'approx_count_distinct': 1}, 'weight(t)': {'approx_count_distinct': 5},
                          'japanese name': {'approx_count_distinct': 6},
                          'last position seen': {'approx_count_distinct': 4},
                          'date arrival': {'approx_count_distinct': 1}, 'last date seen': {'approx_count_distinct': 6},
                          'attributes': {'approx_count_distinct': 6}, 'DateType': {'approx_count_distinct': 6},
                          'Tiemstamp': {'approx_count_distinct': 1}, 'Cybertronian': {'approx_count_distinct': 1},
                          'function(binary)': {'approx_count_distinct': 6}, 'NullType': {'approx_count_distinct': 0}}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_unique():
        actual_df = source_df.cols.unique('height(ft)')
        expected_df = op.create.df([('height(ft)', ShortType(), True)], [(28,), (300,), (26,), (None,), (13,), (17,)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_add():
        actual_df = source_df.cols.add(['height(ft)', 'rank'])
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', FloatType(), True), ('function', StringType(), True),
             ('rank', FloatType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True), ('sum', FloatType(), True)], [(
                                                                                                                     "Optim'us",
                                                                                                                     28.0,
                                                                                                                     'Leader',
                                                                                                                     10.0,
                                                                                                                     5000000,
                                                                                                                     4.300000190734863,
                                                                                                                     [
                                                                                                                         'Inochi',
                                                                                                                         'Convoy'],
                                                                                                                     '19.442735,-99.201111',
                                                                                                                     '1980/04/10',
                                                                                                                     '2016/09/10',
                                                                                                                     [
                                                                                                                         8.53439998626709,
                                                                                                                         4300.0],
                                                                                                                     datetime.date(
                                                                                                                         2016,
                                                                                                                         9,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Leader'),
                                                                                                                     None,
                                                                                                                     38.0),
                                                                                                                     (
                                                                                                                     'bumbl#ebéé  ',
                                                                                                                     17.0,
                                                                                                                     'Espionage',
                                                                                                                     7.0,
                                                                                                                     5000000,
                                                                                                                     2.0,
                                                                                                                     [
                                                                                                                         'Bumble',
                                                                                                                         'Goldback'],
                                                                                                                     '10.642707,-71.612534',
                                                                                                                     '1980/04/10',
                                                                                                                     '2015/08/10',
                                                                                                                     [
                                                                                                                         5.334000110626221,
                                                                                                                         2000.0],
                                                                                                                     datetime.date(
                                                                                                                         2015,
                                                                                                                         8,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Espionage'),
                                                                                                                     None,
                                                                                                                     24.0),
                                                                                                                     (
                                                                                                                     'ironhide&',
                                                                                                                     26.0,
                                                                                                                     'Security',
                                                                                                                     7.0,
                                                                                                                     5000000,
                                                                                                                     4.0,
                                                                                                                     [
                                                                                                                         'Roadbuster'],
                                                                                                                     '37.789563,-122.400356',
                                                                                                                     '1980/04/10',
                                                                                                                     '2014/07/10',
                                                                                                                     [
                                                                                                                         7.924799919128418,
                                                                                                                         4000.0],
                                                                                                                     datetime.date(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Security'),
                                                                                                                     None,
                                                                                                                     33.0),
                                                                                                                     (
                                                                                                                     'Jazz',
                                                                                                                     13.0,
                                                                                                                     'First Lieutenant',
                                                                                                                     8.0,
                                                                                                                     5000000,
                                                                                                                     1.7999999523162842,
                                                                                                                     [
                                                                                                                         'Meister'],
                                                                                                                     '33.670666,-117.841553',
                                                                                                                     '1980/04/10',
                                                                                                                     '2013/06/10',
                                                                                                                     [
                                                                                                                         3.962399959564209,
                                                                                                                         1800.0],
                                                                                                                     datetime.date(
                                                                                                                         2013,
                                                                                                                         6,
                                                                                                                         24),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'First Lieutenant'),
                                                                                                                     None,
                                                                                                                     21.0),
                                                                                                                     (
                                                                                                                     'Megatron',
                                                                                                                     None,
                                                                                                                     'None',
                                                                                                                     10.0,
                                                                                                                     5000000,
                                                                                                                     5.699999809265137,
                                                                                                                     [
                                                                                                                         'Megatron'],
                                                                                                                     None,
                                                                                                                     '1980/04/10',
                                                                                                                     '2012/05/10',
                                                                                                                     [
                                                                                                                         None,
                                                                                                                         5700.0],
                                                                                                                     datetime.date(
                                                                                                                         2012,
                                                                                                                         5,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'None'),
                                                                                                                     None,
                                                                                                                     None),
                                                                                                                     (
                                                                                                                     'Metroplex_)^$',
                                                                                                                     300.0,
                                                                                                                     'Battle Station',
                                                                                                                     8.0,
                                                                                                                     5000000,
                                                                                                                     None,
                                                                                                                     [
                                                                                                                         'Metroflex'],
                                                                                                                     None,
                                                                                                                     '1980/04/10',
                                                                                                                     '2011/04/10',
                                                                                                                     [
                                                                                                                         91.44000244140625,
                                                                                                                         None],
                                                                                                                     datetime.date(
                                                                                                                         2011,
                                                                                                                         4,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Battle Station'),
                                                                                                                     None,
                                                                                                                     308.0)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_add_all_columns():
        actual_df = source_df.cols.add('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', FloatType(), True), ('function', StringType(), True),
             ('rank', FloatType(), True), ('age', FloatType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True), ('sum', FloatType(), True)], [(
                                                                                                                     "Optim'us",
                                                                                                                     28.0,
                                                                                                                     'Leader',
                                                                                                                     10.0,
                                                                                                                     5000000.0,
                                                                                                                     4.300000190734863,
                                                                                                                     [
                                                                                                                         'Inochi',
                                                                                                                         'Convoy'],
                                                                                                                     '19.442735,-99.201111',
                                                                                                                     '1980/04/10',
                                                                                                                     '2016/09/10',
                                                                                                                     [
                                                                                                                         8.53439998626709,
                                                                                                                         4300.0],
                                                                                                                     datetime.date(
                                                                                                                         2016,
                                                                                                                         9,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Leader'),
                                                                                                                     None,
                                                                                                                     5000042.5),
                                                                                                                     (
                                                                                                                     'bumbl#ebéé  ',
                                                                                                                     17.0,
                                                                                                                     'Espionage',
                                                                                                                     7.0,
                                                                                                                     5000000.0,
                                                                                                                     2.0,
                                                                                                                     [
                                                                                                                         'Bumble',
                                                                                                                         'Goldback'],
                                                                                                                     '10.642707,-71.612534',
                                                                                                                     '1980/04/10',
                                                                                                                     '2015/08/10',
                                                                                                                     [
                                                                                                                         5.334000110626221,
                                                                                                                         2000.0],
                                                                                                                     datetime.date(
                                                                                                                         2015,
                                                                                                                         8,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Espionage'),
                                                                                                                     None,
                                                                                                                     5000026.0),
                                                                                                                     (
                                                                                                                     'ironhide&',
                                                                                                                     26.0,
                                                                                                                     'Security',
                                                                                                                     7.0,
                                                                                                                     5000000.0,
                                                                                                                     4.0,
                                                                                                                     [
                                                                                                                         'Roadbuster'],
                                                                                                                     '37.789563,-122.400356',
                                                                                                                     '1980/04/10',
                                                                                                                     '2014/07/10',
                                                                                                                     [
                                                                                                                         7.924799919128418,
                                                                                                                         4000.0],
                                                                                                                     datetime.date(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Security'),
                                                                                                                     None,
                                                                                                                     5000037.0),
                                                                                                                     (
                                                                                                                     'Jazz',
                                                                                                                     13.0,
                                                                                                                     'First Lieutenant',
                                                                                                                     8.0,
                                                                                                                     5000000.0,
                                                                                                                     1.7999999523162842,
                                                                                                                     [
                                                                                                                         'Meister'],
                                                                                                                     '33.670666,-117.841553',
                                                                                                                     '1980/04/10',
                                                                                                                     '2013/06/10',
                                                                                                                     [
                                                                                                                         3.962399959564209,
                                                                                                                         1800.0],
                                                                                                                     datetime.date(
                                                                                                                         2013,
                                                                                                                         6,
                                                                                                                         24),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'First Lieutenant'),
                                                                                                                     None,
                                                                                                                     5000023.0),
                                                                                                                     (
                                                                                                                     'Megatron',
                                                                                                                     None,
                                                                                                                     'None',
                                                                                                                     10.0,
                                                                                                                     5000000.0,
                                                                                                                     5.699999809265137,
                                                                                                                     [
                                                                                                                         'Megatron'],
                                                                                                                     None,
                                                                                                                     '1980/04/10',
                                                                                                                     '2012/05/10',
                                                                                                                     [
                                                                                                                         None,
                                                                                                                         5700.0],
                                                                                                                     datetime.date(
                                                                                                                         2012,
                                                                                                                         5,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'None'),
                                                                                                                     None,
                                                                                                                     None),
                                                                                                                     (
                                                                                                                     'Metroplex_)^$',
                                                                                                                     300.0,
                                                                                                                     'Battle Station',
                                                                                                                     8.0,
                                                                                                                     5000000.0,
                                                                                                                     None,
                                                                                                                     [
                                                                                                                         'Metroflex'],
                                                                                                                     None,
                                                                                                                     '1980/04/10',
                                                                                                                     '2011/04/10',
                                                                                                                     [
                                                                                                                         91.44000244140625,
                                                                                                                         None],
                                                                                                                     datetime.date(
                                                                                                                         2011,
                                                                                                                         4,
                                                                                                                         10),
                                                                                                                     datetime.datetime(
                                                                                                                         2014,
                                                                                                                         6,
                                                                                                                         24,
                                                                                                                         0,
                                                                                                                         0),
                                                                                                                     True,
                                                                                                                     bytearray(
                                                                                                                         b'Battle Station'),
                                                                                                                     None,
                                                                                                                     None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_z_score():
        actual_df = source_df.cols.z_score('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('height(ft)z_col_', DoubleType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000, 4.300000190734863,
                                                          ['Inochi', 'Convoy'], '19.442735,-99.201111', '1980/04/10',
                                                          '2016/09/10', [8.53439998626709, 4300.0],
                                                          datetime.date(2016, 9, 10),
                                                          datetime.datetime(2014, 6, 24, 0, 0), True,
                                                          bytearray(b'Leader'), None, 0.3906288147345189), (
                                                         'bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                         ['Bumble', 'Goldback'], '10.642707,-71.612534', '1980/04/10',
                                                         '2015/08/10', [5.334000110626221, 2000.0],
                                                         datetime.date(2015, 8, 10),
                                                         datetime.datetime(2014, 6, 24, 0, 0), True,
                                                         bytearray(b'Espionage'), None, 0.47868039182631617), (
                                                         'ironhide&', 26, 'Security', 7, 5000000, 4.0, ['Roadbuster'],
                                                         '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                         [7.924799919128418, 4000.0], datetime.date(2014, 6, 24),
                                                         datetime.datetime(2014, 6, 24, 0, 0), True,
                                                         bytearray(b'Security'), None, 0.4066381923875729), (
                                                         'Jazz', 13, 'First Lieutenant', 8, 5000000, 1.7999999523162842,
                                                         ['Meister'], '33.670666,-117.841553', '1980/04/10',
                                                         '2013/06/10', [3.962399959564209, 1800.0],
                                                         datetime.date(2013, 6, 24),
                                                         datetime.datetime(2014, 6, 24, 0, 0), True,
                                                         bytearray(b'First Lieutenant'), None, 0.5106991471324243), (
                                                         'Megatron', None, 'None', 10, 5000000, 5.699999809265137,
                                                         ['Megatron'], None, '1980/04/10', '2012/05/10', [None, 5700.0],
                                                         datetime.date(2012, 5, 10),
                                                         datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'None'),
                                                         None, None), (
                                                         'Metroplex_)^$', 300, 'Battle Station', 8, 5000000, None,
                                                         ['Metroflex'], None, '1980/04/10', '2011/04/10',
                                                         [91.44000244140625, None], datetime.date(2011, 4, 10),
                                                         datetime.datetime(2014, 6, 24, 0, 0), True,
                                                         bytearray(b'Battle Station'), None, 1.7866465460808323)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_iqr():
        actual_df = source_df.cols.iqr('height(ft)')
        expected_value = 0.0
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_iqr_all_columns():
        actual_df = source_df.cols.iqr('*')
        expected_value = 0.0
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_lower():
        actual_df = source_df.cols.lower('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_lower_all_columns():
        actual_df = source_df.cols.lower('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("optim'us", 28, 'leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'jazz', 13, 'first lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'megatron', None, 'none', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'metroplex_)^$', 300,
                                                                                         'battle station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_upper():
        actual_df = source_df.cols.upper('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_upper_all_columns():
        actual_df = source_df.cols.upper('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("OPTIM'US", 28, 'LEADER', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'BUMBL#EBÉÉ  ', 17,
                                                                                         'ESPIONAGE', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'IRONHIDE&', 26, 'SECURITY', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'JAZZ', 13, 'FIRST LIEUTENANT',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'MEGATRON', None, 'NONE', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'METROPLEX_)^$', 300,
                                                                                         'BATTLE STATION', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_trim():
        actual_df = source_df.cols.trim('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [(
                                                                                         "Optim'us", '28', 'Leader', 10,
                                                                                         5000000, 4.300000190734863,
                                                                                         ['Inochi', 'Convoy'],
                                                                                         '19.442735,-99.201111',
                                                                                         '1980/04/10', '2016/09/10',
                                                                                         [8.53439998626709, 4300.0],
                                                                                         datetime.date(2016, 9, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', '17',
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', '26', 'Security',
                                                                                          7, 5000000, 4.0,
                                                                                          ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         ('Jazz', '13',
                                                                                          'First Lieutenant', 8,
                                                                                          5000000, 1.7999999523162842,
                                                                                          ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', '300',
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_trim_all_columns():
        actual_df = source_df.cols.trim('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', StringType(), True), ('age', StringType(), True), ('weight(t)', StringType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', StringType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', StringType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", '28', 'Leader',
                                                                                          '10', '5000000', '4.3',
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          '2016-09-10',
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0),
                                                                                          'true', bytearray(b'Leader'),
                                                                                          None), ('bumbl#ebéé', '17',
                                                                                                  'Espionage', '7',
                                                                                                  '5000000', '2.0',
                                                                                                  ['Bumble',
                                                                                                   'Goldback'],
                                                                                                  '10.642707,-71.612534',
                                                                                                  '1980/04/10',
                                                                                                  '2015/08/10',
                                                                                                  [5.334000110626221,
                                                                                                   2000.0],
                                                                                                  '2015-08-10',
                                                                                                  datetime.datetime(
                                                                                                      2014, 6, 24, 0,
                                                                                                      0), 'true',
                                                                                                  bytearray(
                                                                                                      b'Espionage'),
                                                                                                  None), (
                                                                                         'ironhide&', '26', 'Security',
                                                                                         '7', '5000000', '4.0',
                                                                                         ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         '2014-06-24',
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0),
                                                                                         'true', bytearray(b'Security'),
                                                                                         None), ('Jazz', '13',
                                                                                                 'First Lieutenant',
                                                                                                 '8', '5000000', '1.8',
                                                                                                 ['Meister'],
                                                                                                 '33.670666,-117.841553',
                                                                                                 '1980/04/10',
                                                                                                 '2013/06/10',
                                                                                                 [3.962399959564209,
                                                                                                  1800.0], '2013-06-24',
                                                                                                 datetime.datetime(2014,
                                                                                                                   6,
                                                                                                                   24,
                                                                                                                   0,
                                                                                                                   0),
                                                                                                 'true', bytearray(
                b'First Lieutenant'), None), ('Megatron', None, 'None', '10', '5000000', '5.7', ['Megatron'], None,
                                              '1980/04/10', '2012/05/10', [None, 5700.0], '2012-05-10',
                                              datetime.datetime(2014, 6, 24, 0, 0), 'true', bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', '300',
                                                                                         'Battle Station', '8',
                                                                                         '5000000', None, ['Metroflex'],
                                                                                         None, '1980/04/10',
                                                                                         '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         '2011-04-10',
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0),
                                                                                         'true',
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_reverse():
        actual_df = source_df.cols.reverse('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_reverse_all_columns():
        actual_df = source_df.cols.reverse('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("su'mitpO", 28, 'redaeL', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '111102.99-,537244.91',
                                                                                          '01/40/0891', '01/90/6102',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         '  éébe#lbmub', 17,
                                                                                         'eganoipsE', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '435216.17-,707246.01',
                                                                                         '01/40/0891', '01/80/5102',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         '&edihnori', 26, 'ytiruceS', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '653004.221-,365987.73',
                                                                                         '01/40/0891', '01/70/4102',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'zzaJ', 13, 'tnanetueiL tsriF',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '355148.711-,666076.33',
                                                                                         '01/40/0891', '01/60/3102',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'nortageM', None, 'enoN', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '01/40/0891', '01/50/2102',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         '$^)_xelporteM', 300,
                                                                                         'noitatS elttaB', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '01/40/0891', '01/40/1102',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_remove_white_spaces():
        actual_df = source_df.cols.remove_white_spaces('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [(
                                                                                         "Optim'us", '28', 'Leader', 10,
                                                                                         5000000, 4.300000190734863,
                                                                                         ['Inochi', 'Convoy'],
                                                                                         '19.442735,-99.201111',
                                                                                         '1980/04/10', '2016/09/10',
                                                                                         [8.53439998626709, 4300.0],
                                                                                         datetime.date(2016, 9, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', '17',
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', '26', 'Security',
                                                                                          7, 5000000, 4.0,
                                                                                          ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         ('Jazz', '13',
                                                                                          'First Lieutenant', 8,
                                                                                          5000000, 1.7999999523162842,
                                                                                          ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', '300',
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_remove_white_spaces_all_columns():
        actual_df = source_df.cols.remove_white_spaces('*')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', StringType(), True), ('age', StringType(), True), ('weight(t)', StringType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', StringType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', StringType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", '28', 'Leader',
                                                                                          '10', '5000000', '4.3',
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          '2016-09-10',
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0),
                                                                                          'true', bytearray(b'Leader'),
                                                                                          None), ('bumbl#ebéé', '17',
                                                                                                  'Espionage', '7',
                                                                                                  '5000000', '2.0',
                                                                                                  ['Bumble',
                                                                                                   'Goldback'],
                                                                                                  '10.642707,-71.612534',
                                                                                                  '1980/04/10',
                                                                                                  '2015/08/10',
                                                                                                  [5.334000110626221,
                                                                                                   2000.0],
                                                                                                  '2015-08-10',
                                                                                                  datetime.datetime(
                                                                                                      2014, 6, 24, 0,
                                                                                                      0), 'true',
                                                                                                  bytearray(
                                                                                                      b'Espionage'),
                                                                                                  None), (
                                                                                         'ironhide&', '26', 'Security',
                                                                                         '7', '5000000', '4.0',
                                                                                         ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         '2014-06-24',
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0),
                                                                                         'true', bytearray(b'Security'),
                                                                                         None), ('Jazz', '13',
                                                                                                 'FirstLieutenant', '8',
                                                                                                 '5000000', '1.8',
                                                                                                 ['Meister'],
                                                                                                 '33.670666,-117.841553',
                                                                                                 '1980/04/10',
                                                                                                 '2013/06/10',
                                                                                                 [3.962399959564209,
                                                                                                  1800.0], '2013-06-24',
                                                                                                 datetime.datetime(2014,
                                                                                                                   6,
                                                                                                                   24,
                                                                                                                   0,
                                                                                                                   0),
                                                                                                 'true', bytearray(
                b'First Lieutenant'), None), ('Megatron', None, 'None', '10', '5000000', '5.7', ['Megatron'], None,
                                              '1980/04/10', '2012/05/10', [None, 5700.0], '2012-05-10',
                                              datetime.datetime(2014, 6, 24, 0, 0), 'true', bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', '300',
                                                                                         'BattleStation', '8',
                                                                                         '5000000', None, ['Metroflex'],
                                                                                         None, '1980/04/10',
                                                                                         '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         '2011-04-10',
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0),
                                                                                         'true',
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_date_transform():
        actual_df = source_df.cols.date_transform('date arrival', 'yyyy/MM/dd', 'dd-MM-YYYY')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('date arrival_data_transform', StringType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000,
                                                                     4.300000190734863, ['Inochi', 'Convoy'],
                                                                     '19.442735,-99.201111', '1980/04/10', '2016/09/10',
                                                                     [8.53439998626709, 4300.0],
                                                                     datetime.date(2016, 9, 10),
                                                                     datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                     bytearray(b'Leader'), None, '10-04-1980'), (
                                                                    'bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                                    ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                                    '1980/04/10', '2015/08/10',
                                                                    [5.334000110626221, 2000.0],
                                                                    datetime.date(2015, 8, 10),
                                                                    datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                    bytearray(b'Espionage'), None, '10-04-1980'), (
                                                                    'ironhide&', 26, 'Security', 7, 5000000, 4.0,
                                                                    ['Roadbuster'], '37.789563,-122.400356',
                                                                    '1980/04/10', '2014/07/10',
                                                                    [7.924799919128418, 4000.0],
                                                                    datetime.date(2014, 6, 24),
                                                                    datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                    bytearray(b'Security'), None, '10-04-1980'), (
                                                                    'Jazz', 13, 'First Lieutenant', 8, 5000000,
                                                                    1.7999999523162842, ['Meister'],
                                                                    '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                                    [3.962399959564209, 1800.0],
                                                                    datetime.date(2013, 6, 24),
                                                                    datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                    bytearray(b'First Lieutenant'), None, '10-04-1980'),
                                                                    ('Megatron', None, 'None', 10, 5000000,
                                                                     5.699999809265137, ['Megatron'], None,
                                                                     '1980/04/10', '2012/05/10', [None, 5700.0],
                                                                     datetime.date(2012, 5, 10),
                                                                     datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                     bytearray(b'None'), None, '10-04-1980'), (
                                                                    'Metroplex_)^$', 300, 'Battle Station', 8, 5000000,
                                                                    None, ['Metroflex'], None, '1980/04/10',
                                                                    '2011/04/10', [91.44000244140625, None],
                                                                    datetime.date(2011, 4, 10),
                                                                    datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                    bytearray(b'Battle Station'), None, '10-04-1980')])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_date_transform_all_columns():
        actual_df = source_df.cols.date_transform(['date arrival', 'last date seen'], 'yyyy/MM/dd', 'dd-MM-YYYY')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('date arrival_data_transform', StringType(), True),
             ('last date seen_data_transform', StringType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000,
                                                                       4.300000190734863, ['Inochi', 'Convoy'],
                                                                       '19.442735,-99.201111', '1980/04/10',
                                                                       '2016/09/10', [8.53439998626709, 4300.0],
                                                                       datetime.date(2016, 9, 10),
                                                                       datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                       bytearray(b'Leader'), None, '10-04-1980',
                                                                       '10-09-2016'), (
                                                                      'bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                                      ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                                      '1980/04/10', '2015/08/10',
                                                                      [5.334000110626221, 2000.0],
                                                                      datetime.date(2015, 8, 10),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'Espionage'), None, '10-04-1980',
                                                                      '10-08-2015'), (
                                                                      'ironhide&', 26, 'Security', 7, 5000000, 4.0,
                                                                      ['Roadbuster'], '37.789563,-122.400356',
                                                                      '1980/04/10', '2014/07/10',
                                                                      [7.924799919128418, 4000.0],
                                                                      datetime.date(2014, 6, 24),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'Security'), None, '10-04-1980',
                                                                      '10-07-2014'), (
                                                                      'Jazz', 13, 'First Lieutenant', 8, 5000000,
                                                                      1.7999999523162842, ['Meister'],
                                                                      '33.670666,-117.841553', '1980/04/10',
                                                                      '2013/06/10', [3.962399959564209, 1800.0],
                                                                      datetime.date(2013, 6, 24),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'First Lieutenant'), None,
                                                                      '10-04-1980', '10-06-2013'), (
                                                                      'Megatron', None, 'None', 10, 5000000,
                                                                      5.699999809265137, ['Megatron'], None,
                                                                      '1980/04/10', '2012/05/10', [None, 5700.0],
                                                                      datetime.date(2012, 5, 10),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'None'), None, '10-04-1980',
                                                                      '10-05-2012'), (
                                                                      'Metroplex_)^$', 300, 'Battle Station', 8,
                                                                      5000000, None, ['Metroflex'], None, '1980/04/10',
                                                                      '2011/04/10', [91.44000244140625, None],
                                                                      datetime.date(2011, 4, 10),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'Battle Station'), None, '10-04-1980',
                                                                      '10-04-2011')])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_years_between():
        actual_df = source_df.cols.years_between('date arrival', 'yyyyMMdd')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('date arrival_years_between', FloatType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000,
                                                                   4.300000190734863, ['Inochi', 'Convoy'],
                                                                   '19.442735,-99.201111', '1980/04/10',
                                                                   '2016/09/10', [8.53439998626709, 4300.0],
                                                                   datetime.date(2016, 9, 10),
                                                                   datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                   bytearray(b'Leader'), None, None), (
                                                                      'bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                                      ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                                      '1980/04/10', '2015/08/10',
                                                                      [5.334000110626221, 2000.0],
                                                                      datetime.date(2015, 8, 10),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'Espionage'), None, None), (
                                                                      'ironhide&', 26, 'Security', 7, 5000000, 4.0,
                                                                      ['Roadbuster'], '37.789563,-122.400356',
                                                                      '1980/04/10', '2014/07/10',
                                                                      [7.924799919128418, 4000.0],
                                                                      datetime.date(2014, 6, 24),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'Security'), None, None), (
                                                                      'Jazz', 13, 'First Lieutenant', 8, 5000000,
                                                                      1.7999999523162842, ['Meister'],
                                                                      '33.670666,-117.841553', '1980/04/10',
                                                                      '2013/06/10', [3.962399959564209, 1800.0],
                                                                      datetime.date(2013, 6, 24),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'First Lieutenant'), None, None), (
                                                                      'Megatron', None, 'None', 10, 5000000,
                                                                      5.699999809265137, ['Megatron'], None,
                                                                      '1980/04/10', '2012/05/10', [None, 5700.0],
                                                                      datetime.date(2012, 5, 10),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'None'), None, None), (
                                                                      'Metroplex_)^$', 300, 'Battle Station', 8,
                                                                      5000000, None, ['Metroflex'], None, '1980/04/10',
                                                                      '2011/04/10', [91.44000244140625, None],
                                                                      datetime.date(2011, 4, 10),
                                                                      datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                      bytearray(b'Battle Station'), None, None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_years_between_multiple_columns():
        actual_df = source_df.cols.years_between(['date arrival', 'last date seen'], 'yyyyMMdd')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('date arrival_years_between', FloatType(), True),
             ('last date seen_years_between', FloatType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000,
                                                                     4.300000190734863, ['Inochi', 'Convoy'],
                                                                     '19.442735,-99.201111', '1980/04/10',
                                                                     '2016/09/10', [8.53439998626709, 4300.0],
                                                                     datetime.date(2016, 9, 10),
                                                                     datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                     bytearray(b'Leader'), None, None, None), (
                                                                        'bumbl#ebéé  ', 17, 'Espionage', 7, 5000000,
                                                                        2.0, ['Bumble', 'Goldback'],
                                                                        '10.642707,-71.612534', '1980/04/10',
                                                                        '2015/08/10', [5.334000110626221, 2000.0],
                                                                        datetime.date(2015, 8, 10),
                                                                        datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                        bytearray(b'Espionage'), None, None, None), (
                                                                        'ironhide&', 26, 'Security', 7, 5000000, 4.0,
                                                                        ['Roadbuster'], '37.789563,-122.400356',
                                                                        '1980/04/10', '2014/07/10',
                                                                        [7.924799919128418, 4000.0],
                                                                        datetime.date(2014, 6, 24),
                                                                        datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                        bytearray(b'Security'), None, None, None), (
                                                                        'Jazz', 13, 'First Lieutenant', 8, 5000000,
                                                                        1.7999999523162842, ['Meister'],
                                                                        '33.670666,-117.841553', '1980/04/10',
                                                                        '2013/06/10', [3.962399959564209, 1800.0],
                                                                        datetime.date(2013, 6, 24),
                                                                        datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                        bytearray(b'First Lieutenant'), None, None,
                                                                        None), ('Megatron', None, 'None', 10, 5000000,
                                                                                5.699999809265137, ['Megatron'], None,
                                                                                '1980/04/10', '2012/05/10',
                                                                                [None, 5700.0],
                                                                                datetime.date(2012, 5, 10),
                                                                                datetime.datetime(2014, 6, 24, 0, 0),
                                                                                True, bytearray(b'None'), None, None,
                                                                                None), (
                                                                        'Metroplex_)^$', 300, 'Battle Station', 8,
                                                                        5000000, None, ['Metroflex'], None,
                                                                        '1980/04/10', '2011/04/10',
                                                                        [91.44000244140625, None],
                                                                        datetime.date(2011, 4, 10),
                                                                        datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                        bytearray(b'Battle Station'), None, None,
                                                                        None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_impute():
        actual_df = source_df.cols.impute('rank')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', FloatType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('rank_impute', FloatType(), True)], [("Optim'us", 28, 'Leader', 10.0, 5000000, 4.300000190734863,
                                                    ['Inochi', 'Convoy'], '19.442735,-99.201111', '1980/04/10',
                                                    '2016/09/10', [8.53439998626709, 4300.0],
                                                    datetime.date(2016, 9, 10), datetime.datetime(2014, 6, 24, 0, 0),
                                                    True, bytearray(b'Leader'), None, 10.0), (
                                                   'bumbl#ebéé  ', 17, 'Espionage', 7.0, 5000000, 2.0,
                                                   ['Bumble', 'Goldback'], '10.642707,-71.612534', '1980/04/10',
                                                   '2015/08/10', [5.334000110626221, 2000.0],
                                                   datetime.date(2015, 8, 10), datetime.datetime(2014, 6, 24, 0, 0),
                                                   True, bytearray(b'Espionage'), None, 7.0), (
                                                   'ironhide&', 26, 'Security', 7.0, 5000000, 4.0, ['Roadbuster'],
                                                   '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                   [7.924799919128418, 4000.0], datetime.date(2014, 6, 24),
                                                   datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Security'),
                                                   None, 7.0), (
                                                   'Jazz', 13, 'First Lieutenant', 8.0, 5000000, 1.7999999523162842,
                                                   ['Meister'], '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                   [3.962399959564209, 1800.0], datetime.date(2013, 6, 24),
                                                   datetime.datetime(2014, 6, 24, 0, 0), True,
                                                   bytearray(b'First Lieutenant'), None, 8.0), (
                                                   'Megatron', None, 'None', 10.0, 5000000, 5.699999809265137,
                                                   ['Megatron'], None, '1980/04/10', '2012/05/10', [None, 5700.0],
                                                   datetime.date(2012, 5, 10), datetime.datetime(2014, 6, 24, 0, 0),
                                                   True, bytearray(b'None'), None, 10.0), (
                                                   'Metroplex_)^$', 300, 'Battle Station', 8.0, 5000000, None,
                                                   ['Metroflex'], None, '1980/04/10', '2011/04/10',
                                                   [91.44000244140625, None], datetime.date(2011, 4, 10),
                                                   datetime.datetime(2014, 6, 24, 0, 0), True,
                                                   bytearray(b'Battle Station'), None, 8.0)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_hist():
        actual_df = source_df.cols.hist('rank', 4)
        expected_value = [{'count': 2, 'lower': 7.0, 'upper': 7.75}, {'count': 2, 'lower': 7.75, 'upper': 8.5},
                          {'count': 0, 'lower': 8.5, 'upper': 9.25}, {'count': 2, 'lower': 9.25, 'upper': 10.0}]
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_frequency():
        actual_df = source_df.cols.frequency('rank', 4)
        expected_value = {'rank': [{'value': 10, 'count': 2}, {'value': 8, 'count': 2}, {'value': 7, 'count': 2}]}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_frequency_all_columns():
        actual_df = source_df.cols.frequency('*', 4)
        expected_value = {'names': [{'value': 'ironhide&', 'count': 1}, {'value': 'bumbl#ebéé  ', 'count': 1},
                                    {'value': "Optim'us", 'count': 1}, {'value': 'Metroplex_)^$', 'count': 1}],
                          'height(ft)': [{'value': 300, 'count': 1}, {'value': 28, 'count': 1},
                                         {'value': 26, 'count': 1}, {'value': 17, 'count': 1}],
                          'function': [{'value': 'Security', 'count': 1}, {'value': 'None', 'count': 1},
                                       {'value': 'Leader', 'count': 1}, {'value': 'First Lieutenant', 'count': 1}],
                          'rank': [{'value': 10, 'count': 2}, {'value': 8, 'count': 2}, {'value': 7, 'count': 2}],
                          'age': [{'value': 5000000, 'count': 6}],
                          'weight(t)': [{'value': 5.699999809265137, 'count': 1},
                                        {'value': 4.300000190734863, 'count': 1}, {'value': 4.0, 'count': 1},
                                        {'value': 2.0, 'count': 1}],
                          'japanese name': [{'value': ['Roadbuster'], 'count': 1}, {'value': ['Metroflex'], 'count': 1},
                                            {'value': ['Meister'], 'count': 1}, {'value': ['Megatron'], 'count': 1}],
                          'last position seen': [{'value': None, 'count': 2},
                                                 {'value': '37.789563,-122.400356', 'count': 1},
                                                 {'value': '33.670666,-117.841553', 'count': 1},
                                                 {'value': '19.442735,-99.201111', 'count': 1}],
                          'date arrival': [{'value': '1980/04/10', 'count': 6}],
                          'last date seen': [{'value': '2016/09/10', 'count': 1}, {'value': '2015/08/10', 'count': 1},
                                             {'value': '2014/07/10', 'count': 1}, {'value': '2013/06/10', 'count': 1}],
                          'attributes': [{'value': [91.44000244140625, None], 'count': 1},
                                         {'value': [8.53439998626709, 4300.0], 'count': 1},
                                         {'value': [7.924799919128418, 4000.0], 'count': 1},
                                         {'value': [5.334000110626221, 2000.0], 'count': 1}],
                          'DateType': [{'value': datetime.date(2016, 9, 10), 'count': 1},
                                       {'value': datetime.date(2015, 8, 10), 'count': 1},
                                       {'value': datetime.date(2014, 6, 24), 'count': 1},
                                       {'value': datetime.date(2013, 6, 24), 'count': 1}],
                          'Tiemstamp': [{'value': datetime.datetime(2014, 6, 24, 0, 0), 'count': 6}],
                          'Cybertronian': [{'value': True, 'count': 6}],
                          'function(binary)': [{'value': bytearray(b'Security'), 'count': 1},
                                               {'value': bytearray(b'None'), 'count': 1},
                                               {'value': bytearray(b'Leader'), 'count': 1},
                                               {'value': bytearray(b'First Lieutenant'), 'count': 1}],
                          'NullType': [{'value': None, 'count': 6}]}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_schema_dtype():
        actual_df = source_df.cols.schema_dtype('rank')
        expected_value = ByteType()
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_dtypes():
        actual_df = source_df.cols.dtypes('rank')
        expected_value = 'tinyint'
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_dtypes_all_columns():
        actual_df = source_df.cols.dtypes('*')
        expected_value = {'names': 'string', 'height(ft)': 'smallint', 'function': 'string', 'rank': 'tinyint',
                          'age': 'int', 'weight(t)': 'float', 'japanese name': 'array<string>',
                          'last position seen': 'string', 'date arrival': 'string', 'last date seen': 'string',
                          'attributes': 'array<float>', 'DateType': 'date', 'Tiemstamp': 'timestamp',
                          'Cybertronian': 'boolean', 'function(binary)': 'binary', 'NullType': 'null'}
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_select_by_dtypes_int():
        actual_df = source_df.cols.select_by_dtypes('int')
        expected_df = op.create.df([('age', IntegerType(), True)],
                                   [(5000000,), (5000000,), (5000000,), (5000000,), (5000000,), (5000000,)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_select_by_dtypes_float():
        actual_df = source_df.cols.select_by_dtypes('float')
        expected_df = op.create.df([('weight(t)', FloatType(), True)],
                                   [(4.300000190734863,), (2.0,), (4.0,), (1.7999999523162842,), (5.699999809265137,),
                                    (None,)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_names():
        actual_df = source_df.cols.names()
        expected_value = ['names', 'height(ft)', 'function', 'rank', 'age', 'weight(t)', 'japanese name',
                          'last position seen', 'date arrival', 'last date seen', 'attributes', 'DateType', 'Tiemstamp',
                          'Cybertronian', 'function(binary)', 'NullType']
        assert (expected_value == actual_df)

    @staticmethod
    def test_cols_qcut():
        actual_df = source_df.cols.qcut('rank', 4)
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('rank_qcut', DoubleType(), True)], [("Optim'us", 28, 'Leader', 10, 5000000, 4.300000190734863,
                                                   ['Inochi', 'Convoy'], '19.442735,-99.201111', '1980/04/10',
                                                   '2016/09/10', [8.53439998626709, 4300.0], datetime.date(2016, 9, 10),
                                                   datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Leader'),
                                                   None, 3.0), ('bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                                ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                                '1980/04/10', '2015/08/10', [5.334000110626221, 2000.0],
                                                                datetime.date(2015, 8, 10),
                                                                datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                bytearray(b'Espionage'), None, 1.0), (
                                                  'ironhide&', 26, 'Security', 7, 5000000, 4.0, ['Roadbuster'],
                                                  '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                  [7.924799919128418, 4000.0], datetime.date(2014, 6, 24),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Security'),
                                                  None, 1.0), (
                                                  'Jazz', 13, 'First Lieutenant', 8, 5000000, 1.7999999523162842,
                                                  ['Meister'], '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                  [3.962399959564209, 1800.0], datetime.date(2013, 6, 24),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True,
                                                  bytearray(b'First Lieutenant'), None, 2.0), (
                                                  'Megatron', None, 'None', 10, 5000000, 5.699999809265137,
                                                  ['Megatron'], None, '1980/04/10', '2012/05/10', [None, 5700.0],
                                                  datetime.date(2012, 5, 10), datetime.datetime(2014, 6, 24, 0, 0),
                                                  True, bytearray(b'None'), None, 3.0), (
                                                  'Metroplex_)^$', 300, 'Battle Station', 8, 5000000, None,
                                                  ['Metroflex'], None, '1980/04/10', '2011/04/10',
                                                  [91.44000244140625, None], datetime.date(2011, 4, 10),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True,
                                                  bytearray(b'Battle Station'), None, 2.0)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_clip():
        actual_df = source_df.cols.clip('rank', 3, 5)
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', IntegerType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 5,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 5, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 5,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         5, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 5,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 5, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_clip_all_columns():
        actual_df = source_df.cols.clip('*', 3, 5)
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', IntegerType(), True), ('function', StringType(), True),
             ('rank', IntegerType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 5, 'Leader', 5, 5,
                                                                                          4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 5, 'Espionage',
                                                                                         5, 5, 3.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', 5, 'Security', 5,
                                                                                          5, 4.0, ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         ('Jazz', 5, 'First Lieutenant',
                                                                                          5, 5, 3.0, ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', None, 'None', 5, 5,
                                                                                         5.0, ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 5,
                                                                                         'Battle Station', 5, 5, None,
                                                                                         ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_replace():
        actual_df = source_df.cols.replace('function', [('Security', 'Leader')], 'Match')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', 26, 'Leader', 7,
                                                                                          5000000, 4.0, ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_replace_all_columns():
        actual_df = source_df.cols.replace('*', [('Jazz', 'Leader')], 'Match')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         ('Leader', 13,
                                                                                          'First Lieutenant', 8,
                                                                                          5000000, 1.7999999523162842,
                                                                                          ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_append_number():
        actual_df = source_df.cols.append('new col', 1)
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('new col', IntegerType(), False)], [("Optim'us", 28, 'Leader', 10, 5000000, 4.300000190734863,
                                                   ['Inochi', 'Convoy'], '19.442735,-99.201111', '1980/04/10',
                                                   '2016/09/10', [8.53439998626709, 4300.0], datetime.date(2016, 9, 10),
                                                   datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Leader'),
                                                   None, 1), ('bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                              ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                              '1980/04/10', '2015/08/10', [5.334000110626221, 2000.0],
                                                              datetime.date(2015, 8, 10),
                                                              datetime.datetime(2014, 6, 24, 0, 0), True,
                                                              bytearray(b'Espionage'), None, 1), (
                                                  'ironhide&', 26, 'Security', 7, 5000000, 4.0, ['Roadbuster'],
                                                  '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                  [7.924799919128418, 4000.0], datetime.date(2014, 6, 24),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Security'),
                                                  None, 1), (
                                                  'Jazz', 13, 'First Lieutenant', 8, 5000000, 1.7999999523162842,
                                                  ['Meister'], '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                  [3.962399959564209, 1800.0], datetime.date(2013, 6, 24),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True,
                                                  bytearray(b'First Lieutenant'), None, 1), (
                                                  'Megatron', None, 'None', 10, 5000000, 5.699999809265137,
                                                  ['Megatron'], None, '1980/04/10', '2012/05/10', [None, 5700.0],
                                                  datetime.date(2012, 5, 10), datetime.datetime(2014, 6, 24, 0, 0),
                                                  True, bytearray(b'None'), None, 1), (
                                                  'Metroplex_)^$', 300, 'Battle Station', 8, 5000000, None,
                                                  ['Metroflex'], None, '1980/04/10', '2011/04/10',
                                                  [91.44000244140625, None], datetime.date(2011, 4, 10),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True,
                                                  bytearray(b'Battle Station'), None, 1)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_rename():
        actual_df = source_df.cols.rename('rank', 'rank(old)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank(old)', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_rename_list():
        actual_df = source_df.cols.rename(['height(ft)', 'height(ft)(tons)', 'rank', 'rank(old)'])
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_drop():
        actual_df = source_df.cols.drop('rank')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader',
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', 26, 'Security',
                                                                                          5000000, 4.0, ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None',
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_cast():
        actual_df = source_df.cols.cast('function', 'string')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', 300,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_cast_all_columns():
        actual_df = source_df.cols.cast('*', 'string')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', StringType(), True), ('age', StringType(), True), ('weight(t)', StringType(), True),
             ('japanese name', StringType(), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', StringType(), True), ('DateType', StringType(), True), ('Tiemstamp', StringType(), True),
             ('Cybertronian', StringType(), True), ('function(binary)', StringType(), True),
             ('NullType', StringType(), True)], [(
                                                 "Optim'us", '28', 'Leader', '10', '5000000', '4.3', '[Inochi, Convoy]',
                                                 '19.442735,-99.201111', '1980/04/10', '2016/09/10', '[8.5344, 4300.0]',
                                                 '2016-09-10', '2014-06-24 00:00:00', 'true', 'Leader', None), (
                                                 'bumbl#ebéé  ', '17', 'Espionage', '7', '5000000', '2.0',
                                                 '[Bumble, Goldback]', '10.642707,-71.612534', '1980/04/10',
                                                 '2015/08/10', '[5.334, 2000.0]', '2015-08-10', '2014-06-24 00:00:00',
                                                 'true', 'Espionage', None), (
                                                 'ironhide&', '26', 'Security', '7', '5000000', '4.0', '[Roadbuster]',
                                                 '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                 '[7.9248, 4000.0]', '2014-06-24', '2014-06-24 00:00:00', 'true',
                                                 'Security', None), (
                                                 'Jazz', '13', 'First Lieutenant', '8', '5000000', '1.8', '[Meister]',
                                                 '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                 '[3.9624, 1800.0]', '2013-06-24', '2014-06-24 00:00:00', 'true',
                                                 'First Lieutenant', None), (
                                                 'Megatron', None, 'None', '10', '5000000', '5.7', '[Megatron]', None,
                                                 '1980/04/10', '2012/05/10', '[, 5700.0]', '2012-05-10',
                                                 '2014-06-24 00:00:00', 'true', 'None', None), (
                                                 'Metroplex_)^$', '300', 'Battle Station', '8', '5000000', None,
                                                 '[Metroflex]', None, '1980/04/10', '2011/04/10', '[91.44,]',
                                                 '2011-04-10', '2014-06-24 00:00:00', 'true', 'Battle Station', None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_keep():
        actual_df = source_df.cols.keep('rank')
        expected_df = op.create.df([('rank', ByteType(), True)], [(10,), (7,), (7,), (8,), (10,), (8,)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_move():
        actual_df = source_df.cols.move('rank', 'after', 'attributes')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('rank', ByteType(), True),
             ('DateType', DateType(), True), ('Tiemstamp', TimestampType(), True),
             ('Cybertronian', BooleanType(), True), ('function(binary)', BinaryType(), True),
             ('NullType', NullType(), True)], [("Optim'us", 28, 'Leader', 5000000, 4.300000190734863,
                                                ['Inochi', 'Convoy'], '19.442735,-99.201111', '1980/04/10',
                                                '2016/09/10', [8.53439998626709, 4300.0], 10,
                                                datetime.date(2016, 9, 10), datetime.datetime(2014, 6, 24, 0, 0), True,
                                                bytearray(b'Leader'), None), (
                                               'bumbl#ebéé  ', 17, 'Espionage', 5000000, 2.0, ['Bumble', 'Goldback'],
                                               '10.642707,-71.612534', '1980/04/10', '2015/08/10',
                                               [5.334000110626221, 2000.0], 7, datetime.date(2015, 8, 10),
                                               datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Espionage'),
                                               None), ('ironhide&', 26, 'Security', 5000000, 4.0, ['Roadbuster'],
                                                       '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                       [7.924799919128418, 4000.0], 7, datetime.date(2014, 6, 24),
                                                       datetime.datetime(2014, 6, 24, 0, 0), True,
                                                       bytearray(b'Security'), None), (
                                               'Jazz', 13, 'First Lieutenant', 5000000, 1.7999999523162842, ['Meister'],
                                               '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                               [3.962399959564209, 1800.0], 8, datetime.date(2013, 6, 24),
                                               datetime.datetime(2014, 6, 24, 0, 0), True,
                                               bytearray(b'First Lieutenant'), None), (
                                               'Megatron', None, 'None', 5000000, 5.699999809265137, ['Megatron'], None,
                                               '1980/04/10', '2012/05/10', [None, 5700.0], 10,
                                               datetime.date(2012, 5, 10), datetime.datetime(2014, 6, 24, 0, 0), True,
                                               bytearray(b'None'), None), (
                                               'Metroplex_)^$', 300, 'Battle Station', 5000000, None, ['Metroflex'],
                                               None, '1980/04/10', '2011/04/10', [91.44000244140625, None], 8,
                                               datetime.date(2011, 4, 10), datetime.datetime(2014, 6, 24, 0, 0), True,
                                               bytearray(b'Battle Station'), None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_select():
        actual_df = source_df.cols.select(0, 'height(ft)')
        expected_df = op.create.df([('names', StringType(), True)],
                                   [("Optim'us",), ('bumbl#ebéé  ',), ('ironhide&',), ('Jazz',), ('Megatron',),
                                    ('Metroplex_)^$',)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_select_regex():
        actual_df = source_df.cols.select('n.*', regex=True)
        expected_df = op.create.df([('names', StringType(), True)],
                                   [("Optim'us",), ('bumbl#ebéé  ',), ('ironhide&',), ('Jazz',), ('Megatron',),
                                    ('Metroplex_)^$',)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_sort():
        actual_df = source_df.cols.sort()
        expected_df = op.create.df(
            [('Cybertronian', BooleanType(), True), ('DateType', DateType(), True), ('NullType', NullType(), True),
             ('Tiemstamp', TimestampType(), True), ('age', IntegerType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('date arrival', StringType(), True),
             ('function', StringType(), True), ('function(binary)', BinaryType(), True),
             ('height(ft)', ShortType(), True), ('japanese name', ArrayType(StringType(), True), True),
             ('last date seen', StringType(), True), ('last position seen', StringType(), True),
             ('names', StringType(), True), ('rank', ByteType(), True), ('weight(t)', FloatType(), True)], [(True,
                                                                                                             datetime.date(
                                                                                                                 2016,
                                                                                                                 9, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000, [
                                                                                                                 8.53439998626709,
                                                                                                                 4300.0],
                                                                                                             '1980/04/10',
                                                                                                             'Leader',
                                                                                                             bytearray(
                                                                                                                 b'Leader'),
                                                                                                             28,
                                                                                                             ['Inochi',
                                                                                                              'Convoy'],
                                                                                                             '2016/09/10',
                                                                                                             '19.442735,-99.201111',
                                                                                                             "Optim'us",
                                                                                                             10,
                                                                                                             4.300000190734863),
                                                                                                            (True,
                                                                                                             datetime.date(
                                                                                                                 2015,
                                                                                                                 8, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000, [
                                                                                                                 5.334000110626221,
                                                                                                                 2000.0],
                                                                                                             '1980/04/10',
                                                                                                             'Espionage',
                                                                                                             bytearray(
                                                                                                                 b'Espionage'),
                                                                                                             17,
                                                                                                             ['Bumble',
                                                                                                              'Goldback'],
                                                                                                             '2015/08/10',
                                                                                                             '10.642707,-71.612534',
                                                                                                             'bumbl#ebéé  ',
                                                                                                             7, 2.0), (
                                                                                                            True,
                                                                                                            datetime.date(
                                                                                                                2014, 6,
                                                                                                                24),
                                                                                                            None,
                                                                                                            datetime.datetime(
                                                                                                                2014, 6,
                                                                                                                24, 0,
                                                                                                                0),
                                                                                                            5000000, [
                                                                                                                7.924799919128418,
                                                                                                                4000.0],
                                                                                                            '1980/04/10',
                                                                                                            'Security',
                                                                                                            bytearray(
                                                                                                                b'Security'),
                                                                                                            26, [
                                                                                                                'Roadbuster'],
                                                                                                            '2014/07/10',
                                                                                                            '37.789563,-122.400356',
                                                                                                            'ironhide&',
                                                                                                            7, 4.0), (
                                                                                                            True,
                                                                                                            datetime.date(
                                                                                                                2013, 6,
                                                                                                                24),
                                                                                                            None,
                                                                                                            datetime.datetime(
                                                                                                                2014, 6,
                                                                                                                24, 0,
                                                                                                                0),
                                                                                                            5000000, [
                                                                                                                3.962399959564209,
                                                                                                                1800.0],
                                                                                                            '1980/04/10',
                                                                                                            'First Lieutenant',
                                                                                                            bytearray(
                                                                                                                b'First Lieutenant'),
                                                                                                            13,
                                                                                                            ['Meister'],
                                                                                                            '2013/06/10',
                                                                                                            '33.670666,-117.841553',
                                                                                                            'Jazz', 8,
                                                                                                            1.7999999523162842),
                                                                                                            (True,
                                                                                                             datetime.date(
                                                                                                                 2012,
                                                                                                                 5, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000,
                                                                                                             [None,
                                                                                                              5700.0],
                                                                                                             '1980/04/10',
                                                                                                             'None',
                                                                                                             bytearray(
                                                                                                                 b'None'),
                                                                                                             None, [
                                                                                                                 'Megatron'],
                                                                                                             '2012/05/10',
                                                                                                             None,
                                                                                                             'Megatron',
                                                                                                             10,
                                                                                                             5.699999809265137),
                                                                                                            (True,
                                                                                                             datetime.date(
                                                                                                                 2011,
                                                                                                                 4, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000, [
                                                                                                                 91.44000244140625,
                                                                                                                 None],
                                                                                                             '1980/04/10',
                                                                                                             'Battle Station',
                                                                                                             bytearray(
                                                                                                                 b'Battle Station'),
                                                                                                             300, [
                                                                                                                 'Metroflex'],
                                                                                                             '2011/04/10',
                                                                                                             None,
                                                                                                             'Metroplex_)^$',
                                                                                                             8, None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_sort_desc():
        actual_df = source_df.cols.sort('desc')
        expected_df = op.create.df(
            [('weight(t)', FloatType(), True), ('rank', ByteType(), True), ('names', StringType(), True),
             ('last position seen', StringType(), True), ('last date seen', StringType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('height(ft)', ShortType(), True),
             ('function(binary)', BinaryType(), True), ('function', StringType(), True),
             ('date arrival', StringType(), True), ('attributes', ArrayType(FloatType(), True), True),
             ('age', IntegerType(), True), ('Tiemstamp', TimestampType(), True), ('NullType', NullType(), True),
             ('DateType', DateType(), True), ('Cybertronian', BooleanType(), True)], [(
                                                                                      4.300000190734863, 10, "Optim'us",
                                                                                      '19.442735,-99.201111',
                                                                                      '2016/09/10',
                                                                                      ['Inochi', 'Convoy'], 28,
                                                                                      bytearray(b'Leader'), 'Leader',
                                                                                      '1980/04/10',
                                                                                      [8.53439998626709, 4300.0],
                                                                                      5000000,
                                                                                      datetime.datetime(2014, 6, 24, 0,
                                                                                                        0), None,
                                                                                      datetime.date(2016, 9, 10), True),
                                                                                      (2.0, 7, 'bumbl#ebéé  ',
                                                                                       '10.642707,-71.612534',
                                                                                       '2015/08/10',
                                                                                       ['Bumble', 'Goldback'], 17,
                                                                                       bytearray(b'Espionage'),
                                                                                       'Espionage', '1980/04/10',
                                                                                       [5.334000110626221, 2000.0],
                                                                                       5000000,
                                                                                       datetime.datetime(2014, 6, 24, 0,
                                                                                                         0), None,
                                                                                       datetime.date(2015, 8, 10),
                                                                                       True), (4.0, 7, 'ironhide&',
                                                                                               '37.789563,-122.400356',
                                                                                               '2014/07/10',
                                                                                               ['Roadbuster'], 26,
                                                                                               bytearray(b'Security'),
                                                                                               'Security', '1980/04/10',
                                                                                               [7.924799919128418,
                                                                                                4000.0], 5000000,
                                                                                               datetime.datetime(2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                               None,
                                                                                               datetime.date(2014, 6,
                                                                                                             24), True),
                                                                                      (1.7999999523162842, 8, 'Jazz',
                                                                                       '33.670666,-117.841553',
                                                                                       '2013/06/10', ['Meister'], 13,
                                                                                       bytearray(b'First Lieutenant'),
                                                                                       'First Lieutenant', '1980/04/10',
                                                                                       [3.962399959564209, 1800.0],
                                                                                       5000000,
                                                                                       datetime.datetime(2014, 6, 24, 0,
                                                                                                         0), None,
                                                                                       datetime.date(2013, 6, 24),
                                                                                       True), (
                                                                                      5.699999809265137, 10, 'Megatron',
                                                                                      None, '2012/05/10', ['Megatron'],
                                                                                      None, bytearray(b'None'), 'None',
                                                                                      '1980/04/10', [None, 5700.0],
                                                                                      5000000,
                                                                                      datetime.datetime(2014, 6, 24, 0,
                                                                                                        0), None,
                                                                                      datetime.date(2012, 5, 10), True),
                                                                                      (None, 8, 'Metroplex_)^$', None,
                                                                                       '2011/04/10', ['Metroflex'], 300,
                                                                                       bytearray(b'Battle Station'),
                                                                                       'Battle Station', '1980/04/10',
                                                                                       [91.44000244140625, None],
                                                                                       5000000,
                                                                                       datetime.datetime(2014, 6, 24, 0,
                                                                                                         0), None,
                                                                                       datetime.date(2011, 4, 10),
                                                                                       True)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_sort_asc():
        actual_df = source_df.cols.sort('asc')
        expected_df = op.create.df(
            [('Cybertronian', BooleanType(), True), ('DateType', DateType(), True), ('NullType', NullType(), True),
             ('Tiemstamp', TimestampType(), True), ('age', IntegerType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('date arrival', StringType(), True),
             ('function', StringType(), True), ('function(binary)', BinaryType(), True),
             ('height(ft)', ShortType(), True), ('japanese name', ArrayType(StringType(), True), True),
             ('last date seen', StringType(), True), ('last position seen', StringType(), True),
             ('names', StringType(), True), ('rank', ByteType(), True), ('weight(t)', FloatType(), True)], [(True,
                                                                                                             datetime.date(
                                                                                                                 2016,
                                                                                                                 9, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000, [
                                                                                                                 8.53439998626709,
                                                                                                                 4300.0],
                                                                                                             '1980/04/10',
                                                                                                             'Leader',
                                                                                                             bytearray(
                                                                                                                 b'Leader'),
                                                                                                             28,
                                                                                                             ['Inochi',
                                                                                                              'Convoy'],
                                                                                                             '2016/09/10',
                                                                                                             '19.442735,-99.201111',
                                                                                                             "Optim'us",
                                                                                                             10,
                                                                                                             4.300000190734863),
                                                                                                            (True,
                                                                                                             datetime.date(
                                                                                                                 2015,
                                                                                                                 8, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000, [
                                                                                                                 5.334000110626221,
                                                                                                                 2000.0],
                                                                                                             '1980/04/10',
                                                                                                             'Espionage',
                                                                                                             bytearray(
                                                                                                                 b'Espionage'),
                                                                                                             17,
                                                                                                             ['Bumble',
                                                                                                              'Goldback'],
                                                                                                             '2015/08/10',
                                                                                                             '10.642707,-71.612534',
                                                                                                             'bumbl#ebéé  ',
                                                                                                             7, 2.0), (
                                                                                                            True,
                                                                                                            datetime.date(
                                                                                                                2014, 6,
                                                                                                                24),
                                                                                                            None,
                                                                                                            datetime.datetime(
                                                                                                                2014, 6,
                                                                                                                24, 0,
                                                                                                                0),
                                                                                                            5000000, [
                                                                                                                7.924799919128418,
                                                                                                                4000.0],
                                                                                                            '1980/04/10',
                                                                                                            'Security',
                                                                                                            bytearray(
                                                                                                                b'Security'),
                                                                                                            26, [
                                                                                                                'Roadbuster'],
                                                                                                            '2014/07/10',
                                                                                                            '37.789563,-122.400356',
                                                                                                            'ironhide&',
                                                                                                            7, 4.0), (
                                                                                                            True,
                                                                                                            datetime.date(
                                                                                                                2013, 6,
                                                                                                                24),
                                                                                                            None,
                                                                                                            datetime.datetime(
                                                                                                                2014, 6,
                                                                                                                24, 0,
                                                                                                                0),
                                                                                                            5000000, [
                                                                                                                3.962399959564209,
                                                                                                                1800.0],
                                                                                                            '1980/04/10',
                                                                                                            'First Lieutenant',
                                                                                                            bytearray(
                                                                                                                b'First Lieutenant'),
                                                                                                            13,
                                                                                                            ['Meister'],
                                                                                                            '2013/06/10',
                                                                                                            '33.670666,-117.841553',
                                                                                                            'Jazz', 8,
                                                                                                            1.7999999523162842),
                                                                                                            (True,
                                                                                                             datetime.date(
                                                                                                                 2012,
                                                                                                                 5, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000,
                                                                                                             [None,
                                                                                                              5700.0],
                                                                                                             '1980/04/10',
                                                                                                             'None',
                                                                                                             bytearray(
                                                                                                                 b'None'),
                                                                                                             None, [
                                                                                                                 'Megatron'],
                                                                                                             '2012/05/10',
                                                                                                             None,
                                                                                                             'Megatron',
                                                                                                             10,
                                                                                                             5.699999809265137),
                                                                                                            (True,
                                                                                                             datetime.date(
                                                                                                                 2011,
                                                                                                                 4, 10),
                                                                                                             None,
                                                                                                             datetime.datetime(
                                                                                                                 2014,
                                                                                                                 6, 24,
                                                                                                                 0, 0),
                                                                                                             5000000, [
                                                                                                                 91.44000244140625,
                                                                                                                 None],
                                                                                                             '1980/04/10',
                                                                                                             'Battle Station',
                                                                                                             bytearray(
                                                                                                                 b'Battle Station'),
                                                                                                             300, [
                                                                                                                 'Metroflex'],
                                                                                                             '2011/04/10',
                                                                                                             None,
                                                                                                             'Metroplex_)^$',
                                                                                                             8, None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_fill_na():
        actual_df = source_df.cols.fill_na('height(ft)', 'N/A')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [(
                                                                                         "Optim'us", '28', 'Leader', 10,
                                                                                         5000000, 4.300000190734863,
                                                                                         ['Inochi', 'Convoy'],
                                                                                         '19.442735,-99.201111',
                                                                                         '1980/04/10', '2016/09/10',
                                                                                         [8.53439998626709, 4300.0],
                                                                                         datetime.date(2016, 9, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', '17',
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', '26', 'Security',
                                                                                          7, 5000000, 4.0,
                                                                                          ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         ('Jazz', '13',
                                                                                          'First Lieutenant', 8,
                                                                                          5000000, 1.7999999523162842,
                                                                                          ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', 'N/A', 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', '300',
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_fill_na_all_columns():
        actual_df = source_df.cols.fill_na('*', 'N/A')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', StringType(), True), ('function', StringType(), True),
             ('rank', StringType(), True), ('age', StringType(), True), ('weight(t)', StringType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", '28', 'Leader',
                                                                                          '10', '5000000', '4.3',
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', '17',
                                                                                         'Espionage', '7', '5000000',
                                                                                         '2.0', ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         ('ironhide&', '26', 'Security',
                                                                                          '7', '5000000', '4.0',
                                                                                          ['Roadbuster'],
                                                                                          '37.789563,-122.400356',
                                                                                          '1980/04/10', '2014/07/10',
                                                                                          [7.924799919128418, 4000.0],
                                                                                          datetime.date(2014, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Security'), None),
                                                                                         ('Jazz', '13',
                                                                                          'First Lieutenant', '8',
                                                                                          '5000000', '1.8', ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', 'N/A', 'None',
                                                                                         '10', '5000000', '5.7',
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', '300',
                                                                                         'Battle Station', '8',
                                                                                         '5000000', 'N/A',
                                                                                         ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_nest():
        actual_df = source_df.cols.nest(['height(ft)', 'rank'], 'new col', separator=' ')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('new col', StringType(), False)], [("Optim'us", 28, 'Leader', 10, 5000000, 4.300000190734863,
                                                  ['Inochi', 'Convoy'], '19.442735,-99.201111', '1980/04/10',
                                                  '2016/09/10', [8.53439998626709, 4300.0], datetime.date(2016, 9, 10),
                                                  datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Leader'),
                                                  None, '28 10'), ('bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                                   ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                                   '1980/04/10', '2015/08/10',
                                                                   [5.334000110626221, 2000.0],
                                                                   datetime.date(2015, 8, 10),
                                                                   datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                   bytearray(b'Espionage'), None, '17 7'), (
                                                 'ironhide&', 26, 'Security', 7, 5000000, 4.0, ['Roadbuster'],
                                                 '37.789563,-122.400356', '1980/04/10', '2014/07/10',
                                                 [7.924799919128418, 4000.0], datetime.date(2014, 6, 24),
                                                 datetime.datetime(2014, 6, 24, 0, 0), True, bytearray(b'Security'),
                                                 None, '26 7'), (
                                                 'Jazz', 13, 'First Lieutenant', 8, 5000000, 1.7999999523162842,
                                                 ['Meister'], '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                 [3.962399959564209, 1800.0], datetime.date(2013, 6, 24),
                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                 bytearray(b'First Lieutenant'), None, '13 8'), (
                                                 'Megatron', None, 'None', 10, 5000000, 5.699999809265137, ['Megatron'],
                                                 None, '1980/04/10', '2012/05/10', [None, 5700.0],
                                                 datetime.date(2012, 5, 10), datetime.datetime(2014, 6, 24, 0, 0), True,
                                                 bytearray(b'None'), None, '10'), (
                                                 'Metroplex_)^$', 300, 'Battle Station', 8, 5000000, None,
                                                 ['Metroflex'], None, '1980/04/10', '2011/04/10',
                                                 [91.44000244140625, None], datetime.date(2011, 4, 10),
                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                 bytearray(b'Battle Station'), None, '300 8')])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_nest_array():
        actual_df = source_df.cols.nest(['height(ft)', 'rank', 'rank'], 'new col', shape='array')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('new col', ArrayType(ShortType(), True), False)], [("Optim'us", 28, 'Leader', 10, 5000000,
                                                                  4.300000190734863, ['Inochi', 'Convoy'],
                                                                  '19.442735,-99.201111', '1980/04/10', '2016/09/10',
                                                                  [8.53439998626709, 4300.0],
                                                                  datetime.date(2016, 9, 10),
                                                                  datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                  bytearray(b'Leader'), None, [28, 10, 10]), (
                                                                 'bumbl#ebéé  ', 17, 'Espionage', 7, 5000000, 2.0,
                                                                 ['Bumble', 'Goldback'], '10.642707,-71.612534',
                                                                 '1980/04/10', '2015/08/10',
                                                                 [5.334000110626221, 2000.0],
                                                                 datetime.date(2015, 8, 10),
                                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                 bytearray(b'Espionage'), None, [17, 7, 7]), (
                                                                 'ironhide&', 26, 'Security', 7, 5000000, 4.0,
                                                                 ['Roadbuster'], '37.789563,-122.400356', '1980/04/10',
                                                                 '2014/07/10', [7.924799919128418, 4000.0],
                                                                 datetime.date(2014, 6, 24),
                                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                 bytearray(b'Security'), None, [26, 7, 7]), (
                                                                 'Jazz', 13, 'First Lieutenant', 8, 5000000,
                                                                 1.7999999523162842, ['Meister'],
                                                                 '33.670666,-117.841553', '1980/04/10', '2013/06/10',
                                                                 [3.962399959564209, 1800.0],
                                                                 datetime.date(2013, 6, 24),
                                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                 bytearray(b'First Lieutenant'), None, [13, 8, 8]), (
                                                                 'Megatron', None, 'None', 10, 5000000,
                                                                 5.699999809265137, ['Megatron'], None, '1980/04/10',
                                                                 '2012/05/10', [None, 5700.0],
                                                                 datetime.date(2012, 5, 10),
                                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                 bytearray(b'None'), None, [None, 10, 10]), (
                                                                 'Metroplex_)^$', 300, 'Battle Station', 8, 5000000,
                                                                 None, ['Metroflex'], None, '1980/04/10', '2011/04/10',
                                                                 [91.44000244140625, None], datetime.date(2011, 4, 10),
                                                                 datetime.datetime(2014, 6, 24, 0, 0), True,
                                                                 bytearray(b'Battle Station'), None, [300, 8, 8])])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_unnest_array_all_columns():
        actual_df = source_df.cols.unnest('attributes', '-', index=1)
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('attributes_0', FloatType(), True), ('attributes_1', FloatType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None,
                                                                                          8.53439998626709, 4300.0), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None,
                                                                                         5.334000110626221, 2000.0), (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None,
                                                                                         7.924799919128418, 4000.0), (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None, 3.962399959564209,
                                                                                         1800.0), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None, None,
                                                                                         5700.0), ('Metroplex_)^$', 300,
                                                                                                   'Battle Station', 8,
                                                                                                   5000000, None,
                                                                                                   ['Metroflex'], None,
                                                                                                   '1980/04/10',
                                                                                                   '2011/04/10',
                                                                                                   [91.44000244140625,
                                                                                                    None],
                                                                                                   datetime.date(2011,
                                                                                                                 4, 10),
                                                                                                   datetime.datetime(
                                                                                                       2014, 6, 24, 0,
                                                                                                       0), True,
                                                                                                   bytearray(
                                                                                                       b'Battle Station'),
                                                                                                   None,
                                                                                                   91.44000244140625,
                                                                                                   None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_unnest_array():
        actual_df = source_df.cols.unnest('attributes')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('attributes_0', FloatType(), True), ('attributes_1', FloatType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None,
                                                                                          8.53439998626709, 4300.0), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None,
                                                                                         5.334000110626221, 2000.0), (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None,
                                                                                         7.924799919128418, 4000.0), (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None, 3.962399959564209,
                                                                                         1800.0), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None, None,
                                                                                         5700.0), ('Metroplex_)^$', 300,
                                                                                                   'Battle Station', 8,
                                                                                                   5000000, None,
                                                                                                   ['Metroflex'], None,
                                                                                                   '1980/04/10',
                                                                                                   '2011/04/10',
                                                                                                   [91.44000244140625,
                                                                                                    None],
                                                                                                   datetime.date(2011,
                                                                                                                 4, 10),
                                                                                                   datetime.datetime(
                                                                                                       2014, 6, 24, 0,
                                                                                                       0), True,
                                                                                                   bytearray(
                                                                                                       b'Battle Station'),
                                                                                                   None,
                                                                                                   91.44000244140625,
                                                                                                   None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_unnest_array_all_columns():
        actual_df = source_df.cols.unnest('attributes')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', ShortType(), True), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True),
             ('attributes_0', FloatType(), True), ('attributes_1', FloatType(), True)], [("Optim'us", 28, 'Leader', 10,
                                                                                          5000000, 4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None,
                                                                                          8.53439998626709, 4300.0), (
                                                                                         'bumbl#ebéé  ', 17,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None,
                                                                                         5.334000110626221, 2000.0), (
                                                                                         'ironhide&', 26, 'Security', 7,
                                                                                         5000000, 4.0, ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None,
                                                                                         7.924799919128418, 4000.0), (
                                                                                         'Jazz', 13, 'First Lieutenant',
                                                                                         8, 5000000, 1.7999999523162842,
                                                                                         ['Meister'],
                                                                                         '33.670666,-117.841553',
                                                                                         '1980/04/10', '2013/06/10',
                                                                                         [3.962399959564209, 1800.0],
                                                                                         datetime.date(2013, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'First Lieutenant'),
                                                                                         None, 3.962399959564209,
                                                                                         1800.0), (
                                                                                         'Megatron', None, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None, None,
                                                                                         5700.0), ('Metroplex_)^$', 300,
                                                                                                   'Battle Station', 8,
                                                                                                   5000000, None,
                                                                                                   ['Metroflex'], None,
                                                                                                   '1980/04/10',
                                                                                                   '2011/04/10',
                                                                                                   [91.44000244140625,
                                                                                                    None],
                                                                                                   datetime.date(2011,
                                                                                                                 4, 10),
                                                                                                   datetime.datetime(
                                                                                                       2014, 6, 24, 0,
                                                                                                       0), True,
                                                                                                   bytearray(
                                                                                                       b'Battle Station'),
                                                                                                   None,
                                                                                                   91.44000244140625,
                                                                                                   None)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_is_na_all_columns():
        actual_df = source_df.cols.is_na('*')
        expected_df = op.create.df(
            [('names', BooleanType(), False), ('height(ft)', BooleanType(), False), ('function', BooleanType(), False),
             ('rank', BooleanType(), False), ('age', BooleanType(), False), ('weight(t)', BooleanType(), False),
             ('japanese name', BooleanType(), False), ('last position seen', BooleanType(), False),
             ('date arrival', BooleanType(), False), ('last date seen', BooleanType(), False),
             ('attributes', BooleanType(), False), ('DateType', BooleanType(), False),
             ('Tiemstamp', BooleanType(), False), ('Cybertronian', BooleanType(), False),
             ('function(binary)', BooleanType(), False), ('NullType', BooleanType(), False)], [(False, False, False,
                                                                                                False, False, False,
                                                                                                False, False, False,
                                                                                                False, False, False,
                                                                                                False, False, False,
                                                                                                True), (
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               True), (
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               True), (
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               True), (
                                                                                               False, True, False,
                                                                                               False, False, False,
                                                                                               False, True, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               True), (
                                                                                               False, False, False,
                                                                                               False, False, True,
                                                                                               False, True, False,
                                                                                               False, False, False,
                                                                                               False, False, False,
                                                                                               True)])
        assert (expected_df.collect() == actual_df.collect())

    @staticmethod
    def test_cols_is_na():
        actual_df = source_df.cols.is_na('height(ft)')
        expected_df = op.create.df(
            [('names', StringType(), True), ('height(ft)', BooleanType(), False), ('function', StringType(), True),
             ('rank', ByteType(), True), ('age', IntegerType(), True), ('weight(t)', FloatType(), True),
             ('japanese name', ArrayType(StringType(), True), True), ('last position seen', StringType(), True),
             ('date arrival', StringType(), True), ('last date seen', StringType(), True),
             ('attributes', ArrayType(FloatType(), True), True), ('DateType', DateType(), True),
             ('Tiemstamp', TimestampType(), True), ('Cybertronian', BooleanType(), True),
             ('function(binary)', BinaryType(), True), ('NullType', NullType(), True)], [("Optim'us", False, 'Leader',
                                                                                          10, 5000000,
                                                                                          4.300000190734863,
                                                                                          ['Inochi', 'Convoy'],
                                                                                          '19.442735,-99.201111',
                                                                                          '1980/04/10', '2016/09/10',
                                                                                          [8.53439998626709, 4300.0],
                                                                                          datetime.date(2016, 9, 10),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(b'Leader'), None), (
                                                                                         'bumbl#ebéé  ', False,
                                                                                         'Espionage', 7, 5000000, 2.0,
                                                                                         ['Bumble', 'Goldback'],
                                                                                         '10.642707,-71.612534',
                                                                                         '1980/04/10', '2015/08/10',
                                                                                         [5.334000110626221, 2000.0],
                                                                                         datetime.date(2015, 8, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Espionage'), None),
                                                                                         (
                                                                                         'ironhide&', False, 'Security',
                                                                                         7, 5000000, 4.0,
                                                                                         ['Roadbuster'],
                                                                                         '37.789563,-122.400356',
                                                                                         '1980/04/10', '2014/07/10',
                                                                                         [7.924799919128418, 4000.0],
                                                                                         datetime.date(2014, 6, 24),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Security'), None),
                                                                                         ('Jazz', False,
                                                                                          'First Lieutenant', 8,
                                                                                          5000000, 1.7999999523162842,
                                                                                          ['Meister'],
                                                                                          '33.670666,-117.841553',
                                                                                          '1980/04/10', '2013/06/10',
                                                                                          [3.962399959564209, 1800.0],
                                                                                          datetime.date(2013, 6, 24),
                                                                                          datetime.datetime(2014, 6, 24,
                                                                                                            0, 0), True,
                                                                                          bytearray(
                                                                                              b'First Lieutenant'),
                                                                                          None), (
                                                                                         'Megatron', True, 'None', 10,
                                                                                         5000000, 5.699999809265137,
                                                                                         ['Megatron'], None,
                                                                                         '1980/04/10', '2012/05/10',
                                                                                         [None, 5700.0],
                                                                                         datetime.date(2012, 5, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'None'), None), (
                                                                                         'Metroplex_)^$', False,
                                                                                         'Battle Station', 8, 5000000,
                                                                                         None, ['Metroflex'], None,
                                                                                         '1980/04/10', '2011/04/10',
                                                                                         [91.44000244140625, None],
                                                                                         datetime.date(2011, 4, 10),
                                                                                         datetime.datetime(2014, 6, 24,
                                                                                                           0, 0), True,
                                                                                         bytearray(b'Battle Station'),
                                                                                         None)])
        assert (expected_df.collect() == actual_df.collect())
