import requests
import time


def count_words_at_url(url):
    resp = requests.get(url)
    result = len(resp.text.split())
    util = Util()
    util.say_hello()
    print(result)
    return result


class Util:
    def say_hello(self):
        print("hello the result is: ")
