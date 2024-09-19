import csv
import json
from datetime import datetime, timedelta

_date = [(datetime.utcnow() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, 7)]
output = {}

for i in _date:
    with open(f'{i}.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] not in output:
                output[row[0]] = {"READ": 0, "UPDATE": 0, "DELETE": 0, "CREATE": 0}
            output[row[0]][row[1]] += 1

with open('output.csv', 'w') as file:
    file.write(f"email,read_count,update_count,delete_count,create_count\n")

    for key, value in output.items():
        file.write(f"{key},{','.join([str(v) for k, v in value.items()])}\n")

