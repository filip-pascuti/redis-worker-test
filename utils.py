import requests
import time


def count_words_at_url(url):
    resp = requests.get(url)
    result = len(resp.text.split())
    say_hello()
    print(result)
    time.sleep(2)
    return result


def say_hello():
    print("hello the result is: ")
