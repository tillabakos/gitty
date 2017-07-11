import random


def introduce():
    print("Hello, I'm Gittie!")




def add(a, b):
    return a+b



def joke():
    jokes = [
            ["Why was the stadium so cold?", "Because there were a lot of fans."],
            ["What did one plate say to the other?", "Lunch is on me."],
            ["Where do animals go when their tails fall off?", "The retail store."],
            ["What do you call a sad cup of coffee?", "Depresso"]
            ["How does Moses make his tea?", "Hebrews it."]
            ["Why do shoemakers go to heaven?", "Because they have good soles."]
            ["Why can't a bike stand up on it's own?", "Because it's two tired."]
            ["Why can't pirates finish the alphabet?", "Because they got lost at C!"]
            ["What do you call a fake noodle?", "An impasta!"]
            ["Why did the baker stop making doughnuts?", "He got tired of the hole thing!"]
            ]
    joke = random.choice(jokes)
    input(joke[0])
    print(joke[1])

