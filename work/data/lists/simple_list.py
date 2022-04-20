def directions():
    directions = list()
    directions.append("Move Forward")
    directions.append("Move Backwards")
    directions.append("Turn Left")
    directions.append("Turn Right")
    #directions =["Move Forward","Move Backwards","Turn Left", "Turn Right"]
    return directions

def run():
    print(directions())
