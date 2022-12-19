from fredapi import Fred
from economic_data import FRED_API_KEY
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

fred = Fred(api_key=FRED_API_KEY)

plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns', 5)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]