import pyadventure.AdvObject as AdvObject


class TestObject:
    greenBall = None
    redBall = None

    @classmethod
    def setup_class(cls):
        cls.greenBall = AdvObject.AdvObject()
        cls.redBall = AdvObject.AdvObject("red ball")

    def test_instantiate(self):
        assert self.greenBall is not None

    def test_description(self):
        self.greenBall.set_description("green ball")
        assert self.greenBall.get_description() == "green ball"

    # Test adding and getting vocab
    def test_add_vocab(self):
        self.greenBall.add_vocab(["green", "ball"])
        assert self.greenBall.get_vocab() == ["green", "ball"]


    # Add child object and parent object

    # Find child with vocab
