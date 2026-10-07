
import os
import csv
import sys
import math


from neural_npfp.neural_npfp.get_fp import fingerprints

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    return fingerprints(smiles_list)


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
# first column is the natural product score, followed by the 64 fingerprint features
# molecules that could not be processed are written as empty cells
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["np_score"] + [f"feat_{i:02}" for i in range(64)])  # header
    for o in outputs:
        writer.writerow([None if math.isnan(v) else v for v in o])









  
