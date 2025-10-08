g = input("Greeting:")

if g.lower().strip().startswith("hello"):
    print("$0")
elif g.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")
