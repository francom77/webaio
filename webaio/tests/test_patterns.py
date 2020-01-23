from ..patterns import Singleton


class TestSingleton(object):

    def test_creation(self):
        class ExampleSingleton(Singleton):
            pass

        first_object = ExampleSingleton()
        second_object = ExampleSingleton()

        assert id(first_object) == id(second_object)
