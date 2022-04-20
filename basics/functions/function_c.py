def box(word):
    length = len(word)
    print("#"*(length+4))
    print(f"# {word} #")
    print("#"*(length+4))

def low(word):
    print(word.lower())

def up(word):
    print(word.upper())

def mirror(word):
    print(f"{word} | {word[::-1]}")

def repeat(word):
    n = int(input("Enter number of times to repeat: "))
    for i in range(n):
        if i % 2 == 0:
            low(word)
        else:
            up(word)
    
def run():
    w = input("Enter a word: ")
    print("Choose one of the options:\n1-Box\n2-Lowercase\n3-Uppercase\n4-Mirror\n5-Repetition\n")
    opt = int(input())
    if opt == 1:
        box(w)
    elif opt == 2:
        low(w)
    elif opt == 3:
        up(w)
    elif opt == 4:
        mirror(w)
    elif opt == 5:
        repeat(w)
    else:
        print("No such option")

run()
# w = "Harry Potter"
# print(w[::-1])
#range(start, end, step)