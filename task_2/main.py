def main():
    text = input("Введите текст: ")
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_length = 0
    k = 0

    for char in text:
        if char in lowercase or char in uppercase:
            current_length += 1
            if current_length > k:
                k = current_length
        else:
            current_length = 0

    encrypted = ""

    for char in text:
        if char in lowercase:
            for i in range(len(lowercase)):
                if lowercase[i] == char:
                    encrypted += lowercase[(i + k) % 26]
        elif char in uppercase:
            for i in range(len(uppercase)):
                if uppercase[i] == char:
                    encrypted += uppercase[(i + k) % 26]
        else:
            encrypted += char

    print(encrypted)
    print(k)


if __name__ == "__main__":
    main()
