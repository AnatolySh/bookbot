def read_file():
    with open("books/frankenstein.txt", "r", encoding='utf-8') as file:
        text = file.read()
        print(f"{len(text.split())} words found in the document")
        counts = char_count(text)
        counts_list = [[k, v] for k, v in counts.items()]
        counts_list.sort(key=lambda x: x[1])
        for c in counts_list[::-1]:
            print(f"The '{c[0]}' character was found {c[1]} times")


def char_count(text):
    counts = {}
    for c in text.lower():
        counts[c] = counts.get(c, 0) + 1
    return counts


if __name__ == "__main__":
    read_file()
