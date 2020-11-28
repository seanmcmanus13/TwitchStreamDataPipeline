##this is all oldcode...rework this

import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind
import time 
import random
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import pandas_datareader.data as web
import datetime as dt
from datetime import date
import re
import pandas_market_calendars as mcal


# Pull up to date data for the companies we're interested in
start = dt.datetime(2015,1,1)
end = date.today()

####[web.DataReader('ATVI','yahoo', start, end)]
##EA = pd.concat([web.DataReader('EA','yahoo', start, end)]).reset_index()
##TT = pd.concat([web.DataReader('TTWO','yahoo', start, end)]).reset_index()
##NIN = pd.concat([web.DataReader('NTDOY','yahoo', start, end)]).reset_index()
