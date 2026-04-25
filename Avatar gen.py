import random
"""Draws facial features to construct a unique game avatar."""

def draw_bow():
    print("!>o<!")
def draw_eyes(size):
    if size == "small":
        print(".   .")
    elif size == "medium":
        print("o   o")
    elif size == "large":
        print("O   O")
    else:
        raise ValueError("invalid eye size")

def draw_nose(shape):
    if shape == "button":
        print("  @  ")
    elif shape == "triangle":
        print("  >  ")
    else:
        raise ValueError("invalid nose shape")

def draw_mouth(expression):
    if expression == "smile":
        print("\\___/")
    elif expression == "neutral":
        print("-----")
    elif expression == "teeth":
        print("(|||)")
    else:
        raise ValueError("invalid mouth expression")

num = random.randint(1,2)
num2 = random.randint(1,4)
nose = ""
mouth = ""
if num == 1:
    nose = 'triangle'
elif num == 2:
    nose = 'button'

if num2 == 1:
    mouth = 'neutral'
elif num2 == 2:
    mouth = 'teeth'
else:
    mouth = 'smile'

num3= random.randint(1,3)

if num3 ==1 :
    avatar.draw_bow()
avatar.draw_eyes("medium")
avatar.draw_nose(nose)
avatar.draw_mouth(mouth)
if num3 == 2:
    avatar.draw_bow()
