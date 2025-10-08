d = {}
x = 1
while True:
    try:
        item = input()
        if item in d:
            while d[x] != item:
                x += 1
            x += 1
        d[x] = item
        x = 1
    except EOFError:
        break

print(d)


d = {}
x = 1  # Initialize x to 1

while True:
    try:
        item = input()
        if x in d and d[x] == item:
            x += 1
        else:
            d[x] = item
            x = 1

    except EOFError:
        break

print(d)


my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()

print(values)

for value in values:
    print(value)



import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
           'Age': [25, 30, 35]}
print(data)

df = pd.DataFrame(data)
print(df)
array = df.values
print(array)


























