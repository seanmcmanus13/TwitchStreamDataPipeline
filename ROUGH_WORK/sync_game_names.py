import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.sparse import csr_matrix
import sparse_dot_topn.sparse_dot_topn as ct  # Leading Juice for us
import time
pd.set_option('display.max_colwidth', -1)

##see link below for simple means of matching:
##as an aside there's no point developing this until we've ran the other scrapers and have a dataset to work off of
##https://github.com/maladeep/Name-Matching-In-Python/blob/master/Surprisingly%20Effective%20Way%20To%20Name%20Matching%20In%20Python.ipynb

##match the amazon best sellers against the names in the games table