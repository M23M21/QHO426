print("Program started!")
x = abs(int(input("Please enter an ASCII code: ")))
if x in range(32, 127):
    print(f"The character represented by ASCII code {x} is {chr(x)}")
else:
    print("Oh-no. Cannot convert!")
print("Program ended!")