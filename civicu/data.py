from __future__ import print_function, unicode_literals, division, absolute_import
from future import standard_library
standard_library.install_aliases()  # noqa
from builtins import *  # noqa

import pandas as pd
from pugnlp.util import clean_columns, make_name


df_data = pd.read_csv(os.path.join(DATA_PATH, 'data_info.csv'))


def get_data(name='food_carbon', url=None):
    """ Retrieve data from local cache in data/ or download from url

    >>> get_data('food_carbon').shape
    (16, 4)
    """
    name = make_name(name)  # replace spaces with _ ,etc)
    if name == 'food_carbon':
        df = pd.read_html('http://www.greeneatz.com/foods-carbon-footprint.html', header=0)[0]
        df.to_csv('food_carbon.csv')
    elif name == 'capitals':
        df = pd.read_html('https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States', header=0)[0]
    df.columns = clean_columns(df.columns)
    return df
