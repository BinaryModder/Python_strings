def main():
    text = input("Введите текст: ")
    words = []
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

    mirrored_words = ""
    for i in range(len(words) - 1, -1, -1):
        if mirrored_words:
            mirrored_words += " "
        mirrored_words += words[i]

    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    print(mirrored_words)
    print(reversed_text)


if __name__ == "__main__":
    main()
