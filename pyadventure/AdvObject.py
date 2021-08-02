

class AdvObject:
    def __init__(self, description=None):
        self._description = description
        self._vocab = set()
        self._children = []
        self._parent = None
        self.location = False
        self.surface = False
        self.container = False
        self.openable = False
        self.open = False
        self.lockable = False
        self.locked = False
        self.article = "a"

    def set_description(self, description):
        # If a description generating routine has failed.
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

    def match_vocab(self, *words):
        test_vocab = set(words)
        return self._vocab.intersection(test_vocab) == test_vocab

    def add_child(self, child):
        if child not in self._children:
            self._children.append(child)
        if child.get_parent() is not self:
            child.set_parent(self)

    def get_children(self):
        return self._children

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        if self._parent is not parent:
            self._parent = parent
        if self._parent.has_child(self) is not True:
            self._parent.add_child(self)

    def has_child(self, child):
        return child in self._children

    def has_children(self):
        return len(self._children) > 0

    def find(self, *words):
        result = []
        if self.match_vocab(*words):
            result.append(self)
        for child in self._children:
            if child.match_vocab(*words):
                result.append(child)
        return result
