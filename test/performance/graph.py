#!/usr/bin/env python3
import matplotlib

# For Mac users.
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import pandas
import random
from scipy.stats import zscore

import rating
import genre

plt.style.use("seaborn")

data = pandas.read_csv("test/performance/perf_log.csv")



