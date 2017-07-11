import random

def introduce():
    print("Hello, I'm Gittie!")


def add(a, b):
    return a+b


def joke():
    jokes = [["Why was the stadium so cold?", "Because there were a lot of fans."], ["What did one plate say to the other?", "Lunch is on me."], ["Where do animals go when their tails fall off?", "The retail store."], ["What do you call a sad cup of coffee?", "Depresso"]]
    joke = random.choice(jokes)
    input(joke[0])
    print(joke[1])

