from googletrans import Translator

translator = Translator()

def load_japanese(file_path):
    text_file = open(file_path, "r", encoding="utf-8")
    word_arr = []
    for word in text_file:
        word2 = word.replace("\n", '')
        if word2 != '':
            word_arr.append(word2)
    text_file.close()
    return word_arr

def translate(word_arr):
    for src in word_arr:
        dst = translator.translate(src, src='ja', dest='en')
        dst_text = dst.text
        #Allow(可)をとる
        dst_text = dst_text.replace(' Allowed', '')
        #全て小文字
        dst_text = dst_text.lower()
        dst_text = dst_text.replace(' ', '_')
        print("%s,%s" % (src, dst_text))


word_arr = load_japanese('jawords.txt')
#print(word_arr)
translate(word_arr)
