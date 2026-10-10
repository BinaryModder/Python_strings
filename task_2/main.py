def main():
    text = input("Enter text: ").replace(",", " ").replace(".", " ")
    words = text.split(" ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    k = max((len(word) for word in words), default=0)

    for char in text:
        if char.lower() in alphabet:
            index_in_alp = alphabet.find(char.lower())
            new_char = alphabet[(index_in_alp+k) % 26]

            if char.isupper():
                encrypted += new_char.upper()
            else:
                encrypted += new_char
        else:
            encrypted += char

    print(f"encrypted : {encrypted}")
    print(f"K : {k}")


if __name__ == "__main__":
    main()
