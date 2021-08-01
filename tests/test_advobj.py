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

    # TODO: Test adding vocab

    # TODO: Test match vocab

    # TODO: Add child object and parent object

    # TODO: Find child with vocab
