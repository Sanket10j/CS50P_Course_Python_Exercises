while True:
    try:
        x = input('Fraction: ')
        a, b = x.split('/')
        z = round((int(a) / int(b)) * 100)

        if z == 99 or z == 100:
            print('F')
        elif z == 1 or z == 0:
            print('E')
        elif z > 100:
            continue
        else:
            print(f'{z}%')
        break  # Exit the loop if the input is valid
    except (ValueError, ZeroDivisionError):
        pass

