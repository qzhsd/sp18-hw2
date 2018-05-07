import numpy as np

time_all = np.asarray([19507.879249, 19632.451128, 19630.458821])
time_sort = np.asarray([1006.562846, 1304.933873, 989.699507])
time_transfer = (time_all - time_sort) / 2
num_of_int = 2200000
network_thr = num_of_int / time_transfer
print (network_thr)
print ("--------------------------------")

time_all = np.asarray([19204.500465, 19662.215222, 19155.964547 ])
time_sort = np.asarray([1424.178395, 1894.493671, 1336.20583])
time_transfer = (time_all - time_sort) / 2
num_of_int = 2800000    
network_thr = num_of_int / time_transfer
print (network_thr)
print ("--------------------------------")

time_all = np.asarray([22216.61539, 21801.379021, 21131.186786])
time_sort = np.asarray([2061.071872, 1219.832304, 1024.331339])
time_transfer = (time_all - time_sort) / 2
num_of_int = 2000000
network_thr = num_of_int / time_transfer
print (network_thr)
print ("--------------------------------")

time_all = np.asarray([20656.116915, 21183.522286, 20999.368883])
time_sort = np.asarray([1708.661064, 2315.338683, 2312.151004])
time_transfer = (time_all - time_sort) / 2
num_of_int = 3500000   
network_thr = num_of_int / time_transfer
print (network_thr)
print ("--------------------------------")