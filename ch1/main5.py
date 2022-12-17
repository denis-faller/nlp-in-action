from itertools import permutations
a = [" ".join(combo) for combo in permutations("Good morning Rosa!".split(), 3)]
print(a)