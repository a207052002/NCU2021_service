input_string = input()

if(input_string == "你是不是在哭?"):
    print("是")
else:
    length_of_string = len(input_string)
    if(length_of_string >= 9):
        print("打這麼多誰它媽看得完?")
    elif(length_of_string < 2):
        print("蛤?")
    else:
        print("是喔")

