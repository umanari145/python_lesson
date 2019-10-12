from googletrans import Translator

translator = Translator()

def load_japanese(file_path):
    text_file = open(file_path, "r", encoding="utf-8")
    word_arr = []
    for word in text_file:
        word_arr.append(word.replace("\n", ''))
    text_file.close()
    return word_arr

def translate(word_arr):
    for src in word_arr:
        dst = translator.translate(src, src='ja', dest='en')
        print("%s,%s" % (src, dst.text))


word_arr = load_japanese('jawords.txt')
#print(word_arr)
translate(word_arr)
