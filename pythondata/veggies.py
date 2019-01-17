vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


import csv

with open('vegetable.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name" , 'color'])

    for vegetable in vegetables:
        name = vegetable["name"]
        color = vegetable["color"]
        writer.writerow([name, color])

