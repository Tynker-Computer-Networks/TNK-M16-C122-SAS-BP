import random
import string


def random_string(length):
    alphanumeric_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))


def get_random_url():
    url = "/?"
    for i in range(random.randint(1, 8)):
        key = random_string(random.randint(1, 5))
        value = random_string(random.randint(1, 5))
        url += f"{key}={value}&"
    return url
