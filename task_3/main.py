def main():
    text = input().replace(",", " ").replace(".", " ")
    words = text.split(" ")
    dict_words = dict()
    sorted_dict = dict()
    sorted_words = ""

    for word in words:
        if word in dict_words:
            dict_words[word.lower()] += 1
        else:
            dict_words[word.lower()] = 1

    sorted_dict = sorted(dict_words.items(),
                         key=lambda item: item[1], reverse=True)
    for i in range(0, len(sorted_dict)):
        sorted_words += sorted_dict[i][0]
        sorted_words += " "

    print(sorted_words.split(" ")[:5])


if __name__ == "__main__":
    main()
