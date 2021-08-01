import pyadventure.AdvObject as AdvObject


class TestObject:
    greenBall = None
    redBall = None
    basket = None

    @classmethod
    def setup_class(cls):
        cls.greenBall = AdvObject.AdvObject()
        cls.redBall = AdvObject.AdvObject("red ball")
        cls.basket = AdvObject.AdvObject("basket")

    def test_instantiate(self):
        assert self.greenBall is not None

    def test_description(self):
        self.greenBall.set_description("green ball")
        assert self.greenBall.get_description() == "green ball"

    # Test adding and getting vocab
    def test_vocab(self):
        self.greenBall.add_vocab("green", "ball")
        assert self.greenBall.get_vocab() == {"green", "ball"}
        assert self.greenBall.match_vocab("green", "ball")
        assert self.greenBall.match_vocab("red", "ball") is False

    # Add child object and parent object
    def test_parent_child(self):
        self.basket.add_child(self.redBall)
        assert(self.basket.has_child(self.redBall))
        self.greenBall.set_parent(self.basket)
        assert(self.basket.has_child(self.greenBall))
        assert(self.greenBall.get_parent() is self.basket)

    # Find child with vocab
    def test_find(self):
        self.redBall.add_vocab("red", "ball")
        self.basket.add_child(self.redBall)
        self.basket.add_child(self.greenBall)
        assert(self.basket.find("ball") == [self.redBall, self.greenBall])
