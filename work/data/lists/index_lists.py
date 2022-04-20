def movement():
    path =["Move Forward",10,"Move Backwards",5,"Turn Left",3, "Turn Right",1]
    return path

def run():
    print("Moving...")
    lista = movement()
    for i in range(0, 8, 2):
        print(f"{lista[i]} for {lista[i+1]} steps")