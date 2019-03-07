#!/usr/bin/env python
# coding: utf-8
import pandas as pd

path = "budget_data.csv"
budget = pd.read_csv(path)

month = len(budget["Date"].unique())

total = budget["Profit/Losses"].sum()

difference = budget["Profit/Losses"].diff()

average = difference.mean()
max_difference = difference.max()
max_month = budget["Date"][difference.idxmax()]
min_difference = difference.min()
min_month = budget["Date"][difference.idxmin()]

print("Financial Analysis")
print("----------------------------")
print("Total Months:", month)
print("Total:", "${0:.0f}".format(total))
print("Average Change:", "${0:.2f}".format(average))
print("Greatest Increase in Profits:", max_month, "(${0:.0f})".format(max_difference))
print("Greatest Decrease in Profits:", min_month, "(${0:.0f})".format(min_difference))
