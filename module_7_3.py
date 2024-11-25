import re 

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read().lower()
                text = re.sub(r"[',.=?;:!+-]", '', text)
                words = text.split()  # Разбиваем на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        for name, words in self.get_all_words().items():
            if word in words:
                results[name] = words.index(word) + 1
        return results

    def count(self, word):
        word = word.lower()
        results = {}
        for name, words in self.get_all_words().items():
            results[name] = words.count(word)
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего