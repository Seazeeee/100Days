# CSV

They are a common way of showing tabular data.

CSV = Comma Separated Values

Python has a library that you need to import called csv.

```python

import csv

```

An example doing this with a weather based CSV would look like this.

```python
import csv

with open("Projects/csv_example/weather_data.csv", encoding="utf-8") as file:
    data = csv.reader(file)

    for row in data:
        print(row)
```

You can also extract different parts of the data by using slices

The example below shows how you would take the temp. and add it into a a list.

```python

import csv

with open("Projects/csv_example/weather_data.csv", encoding="utf-8") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)

```

## Pandas

Pandas is a library that works with tabular data as well and houses powerful in-built functionalities for these files.

Below is an example of how we would use Pandas to access this data.

```python
import pandas

data = pandas.read_csv("Projects/csv_example/weather_data.csv")
print(data["temp"])
```

### Dataframe

Similar to a excel spreadsheet.

### Series

Equivalent to a list or single column in an excel spreadsheet.