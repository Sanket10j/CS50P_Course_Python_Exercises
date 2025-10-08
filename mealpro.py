def main():
    t = input("What time is it?")
    if t.endswith(("p.m.","a.m.")):
       t2 = convert_24(t)
    else:
       t2 = convert(t)

    if 8.00 >= t2 >= 7.00:
      print("breakfast time")
    elif 13.00 >= t2 >= 12.00:
      print("lunch time")
    elif 19.00 >= t2 >= 18.00:
      print("dinner time")

def convert_24(time):
    first, second = time.split()
    if second == "p.m.":
       time = first
       hrs, mins = time.split(":")
       mins = round(float(int(mins) * 1 / 60), 2)
       hrs = float(int(hrs) + 12)
       n_time = mins + hrs
       return n_time
    else:
        time = first
        return convert(time)



int def convert(time):
    hrs, mins = time.split(":")
    mins = round(float(int(mins) * 1 / 60), 2)
    hrs = float(hrs)
    n_time = mins + hrs
    return n_time

main()