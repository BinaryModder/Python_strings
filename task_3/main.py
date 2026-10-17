def main():
    text = input("Введите текст : ").replace(",", " ").replace(".", " ")
    words = []
    dict_words = dict()
    sorted_words = []
    current_word = ""

    for char in text:
        if char == " ":
            if current_word:
                words.append(current_word)
            current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)

    for word in words:
        if word.lower() in dict_words:
            dict_words[word.lower()] += 1
        else:
            dict_words[word.lower()] = 1

    sorted_dict = sorted(dict_words.items(),
                         key=lambda item: item[1], reverse=True)
    for i in range(0, len(sorted_dict)):
        sorted_words.append(sorted_dict[i][0])

    for word in sorted_words[:5]:
        print(word)


if __name__ == "__main__":
    main()
