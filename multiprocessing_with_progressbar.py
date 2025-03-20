import multiprocessing as mp
from time import sleep
import os
import progressbar as pb
from random import random

def task(a):
    sleep(random())
    return (a[0]+a[1]+a[2])

if __name__ == '__main__':
    # Build the full list of arg tuples
    arg1_range = range(1, 5)
    arg2_range = range(10, 12)
    arg3_range = range(100, 103)
    inputs = []
    for arg1 in arg1_range:
        for arg2 in arg2_range:
            for arg3 in arg3_range:
                inputs.append((arg1, arg2, arg3))
    # Setup pb
    ts_total = len(inputs)
    bar = pb.ProgressBar(max_value=ts_total).start()
    #global ts_progress
    ts_progress = 0
    # Run them in a pool
    p = mp.Pool(processes=mp.cpu_count()-4)
    # map list to target function
    # imap_unordered is more efficient than map and allows accessing
    # results as they come in
    result_list = []
    result = p.imap_unordered(task, inputs)
    for r in result:
        ts_progress += 1
        bar.update(ts_progress)
        result_list.append(r)
    p.close()
    p.join()
    print(result_list)
