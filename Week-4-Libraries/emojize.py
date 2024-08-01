import emoji

def main():
    code = input("Input: ")
    emoji_transform(code)

def emoji_transform(code):
    print(emoji.emojize(f"Output: {code}"))

main()
