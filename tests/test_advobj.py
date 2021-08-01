import unittest
import pyadventure.AdvObject as AdvObject

class TestObject:
    greenBall = None

    @classmethod
    def setup_class(cls):
        cls.greenBall = AdvObject.AdvObject()

    def test_instantiate(self):
        assert self.greenBall is not None

