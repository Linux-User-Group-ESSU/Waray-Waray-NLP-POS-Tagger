#!/usr/bin/python3

import csv

header = ["sentence", "tag"]

with open("dataset.csv",  "w") as file:
	file_data = csv.DictWriter(file, delimiter=",", fieldnames=header)
	file_data.writeheader()

