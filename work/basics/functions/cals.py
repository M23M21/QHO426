def box(word):
    l = len(word)
    print("#"*(l+4))
    print("# " + word + " #")
    print("#"*(l+4))

def low(word):
    print(word.lower())

def up(word):
    print(word.upper())

def mirror(word):
   print(word, "|", word[::-1]) 

def repeat(word):
    n = int(input("Number of times to reapeat: "))
    for times in range(n):
        if times % 2 == 0:
            up(word)
        else:
            low(word)

def run():
    w = input("Enter a word:")
    print("Choose an option:\n1-Box\n2-Lower\n3-Upper\n4-Miror\n5-Repetition")
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