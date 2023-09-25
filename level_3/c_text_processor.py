"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""
import re


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        cleared_text = re.sub(r'[^a-zA-Z\s]', '', self.text)
        return super().summarize() + f', total number of words in the text: {len(cleared_text.split())}'


if __name__ == '__main__':
    text_processor = TextProcessor('hello, ! world! (&*&)')
    print(text_processor.to_upper())
    print(text_processor.summarize())

    print('---')

    advanced_text_processor = AdvancedTextProcessor('hello, ! world! (&*&)')
    print(advanced_text_processor.to_upper())
    print(advanced_text_processor.summarize())

