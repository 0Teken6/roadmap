class Iterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration()
        else:
            index = self.index
            self.index += 1
            return self.lst[index]


# ls = Iterator([1, 2, 5, 7])
# a = iter('hei')
# while True:
#     try:
#         print(next(a))
#     except StopIteration:
#         break


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence.split()
        self.index = 0
        self.current = self.sentence[self.index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sentence):
            raise StopIteration()
        else:
            index = self.index
            self.index += 1
            return self.sentence[index]


# sen = Sentence('Hello my friend')
# print(next(sen))
# print(next(sen))
# print(next(sen))
