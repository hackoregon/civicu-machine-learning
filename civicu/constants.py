from __future__ import print_function, unicode_literals, division, absolute_import
from future import standard_library
standard_library.install_aliases()  # noqa
from builtins import *  # noqa

import matplotlib
get_ipython().magic(u'matplotlib inline')
from IPython.display import display, HTML 

import os
from decimal import Decimal

import pandas as pd
from pandas import np


display(HTML("<style>.container { width:100% !important; }</style>"))
pd.set_option('display.max_rows', 8)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)
