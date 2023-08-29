class ValueTooHighException(Exception):
    pass


class ValueTooSmallException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighException("Value is too high")
    if x < 5:
        raise ValueTooSmallException("value is too small", x)


try:
    test_value(4)
except ValueTooHighException as e:
    print(e)
except ValueTooSmallException as e:
    print(e.message, e.value)
