cal = input("Expression:").lower().strip()

def itp(str):
    x, y, z = str.split(" ")
    x = round(float(x),1)
    z = round(float(z),1)
    if y == "+":
        ans = x + z
    elif y == "-":
        ans = x - z
    elif y == "*":
        ans = x * z
    elif y == "/" and z != 0:
        ans = x / z
    return ans

res = float(itp(cal))

print(res)