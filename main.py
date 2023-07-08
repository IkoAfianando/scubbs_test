import unittest

def sort_people_by_name(data):
    if type(data) == dict:
        sorted_people = sorted(data)
        result = ", ".join(sorted_people)
        return result
    else:
        return False

def go_outside(raining, warm, daytime):
    if raining is False and ( warm or daytime):
        return "Go Outside"
    else:
        return "Go Inside"

def discount_rate(discount):
    if discount > 100:
        return False
    else:
        return discount / 100

def calculate_price(price, discount):
        rate = discount_rate(discount)
        if rate is False:
            return False
        return price / (1 - discount_rate(discount))



class TestHello(unittest.TestCase):
    def test_sort_people_by_name(self):
        data = {"Mary": 17, "Bob": 62, "John": 32}
        self.assertEqual(sort_people_by_name(data), "Bob, John, Mary")

    def test_sort_people_by_name_false(self):
        data = ["iko", "afianando"]
        self.assertFalse(sort_people_by_name(data), False)

    def test_go_outside(self):
        self.assertEqual(go_outside(False, True, False), "Go Outside")

    def test_go_inside(self):
        self.assertEqual(go_outside(True, True, False), "Go Inside")

    def test_calculate_price(self):
        price = 1000
        discount = 20
        self.assertEqual(calculate_price(price, discount), 1250.0)

    def test_calculate_false(self):
        price = 1000
        discount = 1000
        self.assertFalse(calculate_price(price, discount))
