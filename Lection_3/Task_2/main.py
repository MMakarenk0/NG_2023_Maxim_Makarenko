def rhombus(counter1 = 6, counter2 = 0):
    print(" "*(counter1-1) + "*" + " "*(counter2) + "*")
    if counter1 > 3:
        rhombus(counter1-1, counter2+2)
    print(" "*(counter1-1) + "*" + " "*(counter2) + "*")

rhombus()
rhombus(10)
rhombus(20)
rhombus(40)