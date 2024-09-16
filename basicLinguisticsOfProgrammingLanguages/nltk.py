import nltk

nltk.download('punkt')      # Для токенизации
nltk.download('stopwords')  # Для загрузки стоп-слов

# with open("C:\kms.auto\gorod\python\tttt.txt" , 'r', encoding='utf-8') as file:
#     text = file.read()
#
# tokens = word_tokenize(text)
# stop_words = set(stopwords.words('russian'))
# filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
#
# print("Оригинальные токены:", tokens)
# print("Токены без стоп-слов:", filtered_tokens)
