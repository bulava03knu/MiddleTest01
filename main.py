import re


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', ' ')
    return data


def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def sort_words(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]
