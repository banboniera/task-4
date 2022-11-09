import random
import string


def get_random_string(length=8):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_int(a=300, b=1000):
    return random.randint(a, b)
