
def convert(text):
    text = text.replace(":)", "\U0001F60A")
    text = text.replace(":(", "\U0001F641")
    return text

def main():
    emoji = input("")
    nemoji = convert(emoji)
    print(nemoji)

main()
