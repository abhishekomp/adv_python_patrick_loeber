try:
    a = 5 / 1
    # b = a + "b"
    c = 5 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Try completed fine")
finally:
    print("Finally cleaning done")
