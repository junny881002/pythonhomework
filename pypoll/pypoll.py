import pandas as pd 
import os

poll = pd.read_csv("./election_data.csv", engine="python")

total_rows = len(poll["Voter ID"].unique())

grouped = poll["Candidate"].value_counts()
percentage = grouped / total_rows

winner = percentage.idxmax()

print("Election Results")
print("------------------")
print("Total Votes:", total_rows)
print("------------------")
candidates = grouped.index.tolist()
for i in range(0, len(candidates)):
    print("{}:".format(candidates[i]), "{0:.3%}".format(percentage[i]), "({})".format(grouped[i]))
print("------------------")
print("Winner:", winner)
print("------------------")
