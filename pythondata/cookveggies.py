# read vegetables.py

import csv

with open('vegetable.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader]

import json

with open('vegetables.json', 'w') as f:
    data = json.dump(vegetables, f, indent=2)
    
