import numpy as np
import glob
import re
import os

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# Get the file path
all_file =sorted(glob.glob("G*/G*.txt"), key=natural_keys)

# Generate graph from file
for i in range(len(all_file)):
    line_ct = 0
    with open(all_file[i]) as f:
        for line in f:
            if line_ct == 0: # Get graph size
                graph = np.zeros((int(line.split()[0]), int(line.split()[0])), dtype=int)
            else:
                idx_i = int(line.split()[0]) - 1
                idx_j = int(line.split()[1]) - 1
                weight = int(line.split()[2])
                graph[idx_i, idx_j] = weight
            line_ct += 1

    # Save graph
    dir_name = re.sub(".txt", "", all_file[i])
    dir_name = re.sub(".*/", "", dir_name)
    np.savetxt(dir_name + "/matrix.txt", graph, fmt="%d")