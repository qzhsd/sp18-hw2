# compute the application throughput from raw data
import numpy as np

time = [19507.879249, 19632.451128, 19630.458821]
time_arr = np.asarray(time)
num_of_int = 2200000
time_arr = num_of_int / time_arr
print (time_arr)
print ("--------------------------------")

time = [19204.500465, 19662.215222, 19155.964547]
time_arr = np.asarray(time)
num_of_int = 2800000
time_arr = num_of_int / time_arr
print (time_arr)
print ("--------------------------------")

time = [22216.61539, 21801.379021, 21131.186786]
time_arr = np.asarray(time)
num_of_int = 2000000
time_arr = num_of_int / time_arr
print (time_arr)
print ("--------------------------------")

time = [20656.116915, 21183.522286, 20999.368883]
time_arr = np.asarray(time)
num_of_int = 3500000
time_arr = num_of_int / time_arr
print (time_arr)
print ("--------------------------------")