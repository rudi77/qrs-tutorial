import wfdb as wf
import numpy as np
from datasets import mitdb as dm
from matplotlib import pyplot as plt
from utils import plotters

# load data files
records = dm.get_records()

print("#record files: {}".format(len(records)))

# select one record
path = records[28]
print("loading file {}".format(path))

# read data
record = wf.rdsamp(path)
annotation = wf.rdann(path, 'atr')

# print some meta information
print("Sampling frequency: ", record.fs)
print("Shape of loaded data array: ", record.p_signals.shape)

print("Number of loaded annotations: ", len(annotation.sample))
print("Third annotation is of type:", annotation.symbol[2])

plotters.show_objective()

#$plotters.show_annotations(path)

# # Select one of the channels (there are two)
# chid = 0
# data = record.p_signals
# channel = data[:, chid]
#
# print("ECG channel type: ", record.signame[chid])
#
# # Plot only the first 2000 samples
# howmany = 2000
#
# # Calculate time values in seconds
# times = np.arange(howmany, dtype = 'float') / record.fs
# plt.plot(times, channel[ : howmany])
# plt.xlabel('Time [s]')
# plt.show()