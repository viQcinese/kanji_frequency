import operator


def get_text(source):
    with open(source, "r", encoding='utf-8') as f:
        text_string = f.read()
        return text_string


def clean_text(text_string):
    split = text_string.split("底本：")
    text_string = split[0]
    text_list = list(text_string)
    return text_list


def get_kanji_list():
    with open("japanese_texts/joyou_kanji.txt", "r", encoding='utf-8') as f:
        kanji_string = f.read()
        kanji_list = list(kanji_string)
        return kanji_list


def build_kanji_frequency_list(text_list, kanji_list):
    kanji_occurrences = {}
    for kanji in kanji_list:
        occurrences = text_list.count(kanji)
        kanji_occurrences[kanji] = occurrences
    kanji_frequency_list = sorted(kanji_occurrences.items(), key=lambda kv: kv[1])
    kanji_frequency_list.reverse()

    for i in range(len(kanji_frequency_list)):
        if kanji_frequency_list[-1][1] == 0:
            kanji_frequency_list.pop(-1)

    return kanji_frequency_list


def create_frequency_file(kanji_frequency):
    target = source.replace(".txt", "") + "_kanji_frequency.txt"
    kanji_frequency_formatted = ""
    for i in range(len(kanji_frequency)):
        kanji_frequency_formatted += str(kanji_frequency[i][0]) + " - " \
                                     + str(kanji_frequency[i][1]) + "\n"
    with open(target, "w", encoding='utf-8') as f:
        f.write(kanji_frequency_formatted)


def main(source):
    text_list = clean_text(get_text(source))
    kanji_list = get_kanji_list()
    kanji_frequency = build_kanji_frequency_list(text_list, kanji_list)
    print("\nMost frequent Kanjis:")
    for i in range(0, 20):
        print(str(kanji_frequency[i][0]) + " - " + str(kanji_frequency[i][1]))
    print("\n" + str(len(kanji_frequency)) + " different Kanjis")
    create_frequency_file(kanji_frequency)


def pygal_kanji_list(source):
    text_list = clean_text(get_text(source))
    kanji_list = get_kanji_list()
    kanji_frequency = build_kanji_frequency_list(text_list, kanji_list)
    pygal_kanji_list = []

    for i in range(len(kanji_frequency)):
        pygal_kanji_list.append(kanji_frequency[i][0])

    return pygal_kanji_list

def pygal_frequency_list(source):
    text_list = clean_text(get_text(source))
    kanji_list = get_kanji_list()
    kanji_frequency = build_kanji_frequency_list(text_list, kanji_list)
    pygal_frequency_list = []

    for i in range(len(kanji_frequency)):
        pygal_frequency_list.append(kanji_frequency[i][1])

    return pygal_frequency_list


