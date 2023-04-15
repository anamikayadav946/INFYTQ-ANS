#15.
def translate(b_dict,list_words):

    swedish_word_list =[]
    for word in list_words:
        swedish_word_list.append(b_dict[word])
    return swedish_word_list

b_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list_words = ["merry","christmas"]

print(translate(b_dict,list_words))