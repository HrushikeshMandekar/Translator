# Exercise: Translator
# NOTE: To run this you will need INTERNET

from translate import Translator
translator = Translator(to_lang = 'ja') 
# To decide which language we want.

try:
    with open('tfile.txt' ) as my_file:
        text = my_file.read()  # 1 read
        translation = translator.translate(text)  # 2 we translate
        print(translation)
        with open('translatedText.txt', mode = 'w',encoding="utf-8") as my_file2: # 3 new file 
            # encoding="utf-8" used to avoid the error UnicodeEncodeError
            my_file2.write(translation)
except FileNotFoundError as err :
    print('File does not exist! :(')
    raise err