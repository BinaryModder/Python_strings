def main():

    inp = input().split(" ")
    result = ""

    for i in range(0, len(inp)):
        for y in range(len(inp[i]), 0, -1):
            result += inp[i][y - 1]
        result += " "
    print(result)


if __name__ == "__main__":
    main()
