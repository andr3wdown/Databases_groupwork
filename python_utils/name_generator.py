import random as rnd

def generate_name(lenght):
    consonants = 'bcdfghjklmnpqrstvwxz'
    vocals = 'aeiouy'
    name = ''
    for i in range(lenght):
        name += rnd.choice(consonants) if i % 2 == 0 else rnd.choice(vocals)
    return name