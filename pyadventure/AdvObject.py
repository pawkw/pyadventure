

class AdvObject:
    def __init__(self, description=None):
        self._description = description
        self._vocab = set()

    def set_description(self, description):
        if description is None:
            raise ValueError("AdvObject.set_description is None")
        self._description = description

    def get_description(self):
        return self._description

    def add_vocab(self, *vocab):
        for word in vocab:
            self._vocab.add(word)

    def get_vocab(self):
        return self._vocab
