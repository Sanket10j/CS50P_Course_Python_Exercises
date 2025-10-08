def main():
    t = input("What time is it?")
    t2 = convert(t)

    if 8.00 >= t2 >= 7.00:
      print("breakfast time")
    elif 13.00 >= t2 >= 12.00:
      print("lunch time")
    elif 19.00 >= t2 >= 18.00:
      print("dinner time")


def convert(time):
    hrs, mins = time.split(":")
    mins = round(float(int(mins) * 1 / 60), 2)
    hrs = float(hrs)
    n_time = mins + hrs
    return n_time

main()