def main():
    text = input()
    words = text.split(" ")
    result = ""

    for i in range(0, len(words)):
        for y in range(len(words[i]), 0, -1):
            result += words[i][y - 1]
        result += " "

    print(result)


if __name__ == "__main__":
    main()
