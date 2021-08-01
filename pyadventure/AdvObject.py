

class AdvObject:
    def __init__(self, description=None):
        self._description = description

    def set_description(self, description):
        if description is None:
            raise ValueError("AdvObject.set_description is None")
        self._description = description

    def get_description(self):
        return self._description