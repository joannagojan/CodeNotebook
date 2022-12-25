import random
how_big = 6
snow = ["°", "☆", "●", "★", "*", " ", " "]

for x in range(how_big):
    for n in range(how_big - x):
        print(*random.choices(snow), end="")
    for z in range(x):
        print("/", end="")
    for y in range(x):
        print('\u005c', end="")
    for n in range(how_big - x):
        print(*random.choices(snow), end="")
    print()
print(x*" " + "||")
print("𝓜𝓮𝓻𝓻𝔂 𝓒𝓱𝓻𝓲𝓼𝓽𝓶𝓪𝓼")