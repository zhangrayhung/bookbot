def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as f:
        file_contents = f.read()
        print(f"--- Begin report of {file_path} ---")
        total_words = count_words(file_contents)
        print(f"{total_words} words found in the document")
        count_characters(file_contents)
        print("--- End report ---")


def count_words(file_contents):
    words = file_contents.split()
    count_words = len(words)
    return count_words


def count_characters(file_contents):
    characters_dict = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in characters_dict:
            characters_dict[lowered] += 1
        else:
            characters_dict[lowered] = 1

    sorted_characters_dict = dict(
        sorted(characters_dict.items(), key=lambda x: x[1], reverse=True)
    )

    for i in sorted_characters_dict:
        if i.isalpha() == True:
            print(f"The {i} character was found {sorted_characters_dict[i]} times")
    



if __name__ == "__main__":
    main()