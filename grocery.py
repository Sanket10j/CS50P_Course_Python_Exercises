d = {}

x = 1
while True:
    try:
        item = input()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    except EOFError:
        break

for key in sorted(d):
    print(d[key], key.upper())


"""d = {}
x = range(1,100)
while True:
        try:
           item = input()
           if d[x] == item:
               x += 1
               d[x] = item

           else:
               x = 1
               d[x] = item

        except EOFError:
              break

print(d)"""
