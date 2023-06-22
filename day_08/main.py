def count_words(text):
    return len(text.split())


def count_words_iter(text):
    count = 0
    for c in text:
        if c == " ":
            count += 1
    return count + 1


if __name__ == "__main__":
    text = input("Enter text: ")
    print("There are {} words in the text.".format(count_words(text)))
