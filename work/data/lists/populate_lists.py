from simple_list import directions

def menu():
    print("Please select a direction: ")
    dire = directions()
    for i in range(len(dire)):
        print(f"{i}: {dire[i]}")
    choice = int(input())
    return dire[choice]

def run():
    route = list()
    print("Working out the escape route...")
    for i in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

run()