def energy(mass):
    E = mass * pow(300000, 2)
    return E


m = int(input('m:'))
E = energy(m)
print("E:",E)
