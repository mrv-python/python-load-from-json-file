# LOAD FROM JSON FILE DEMO by MR. V

# *********************************************************************************
# Demo of how to load Data from a JSON file
# *********************************************************************************

# Import JSON module
import json

# Open a file and use json.load to load JSON data from file as data
with open("point-data.json", "r") as file_ref:
    points = json.load(file_ref)

# Verify contents of points
for point in points:
    print(f"({point['x']}, {point['y']})")
