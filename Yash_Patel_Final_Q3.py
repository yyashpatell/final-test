class AnalyseTriangle:
    def __int__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def validateTriangle(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    a1 = int(input("please enter the first angle: "))
    a2 = int(input("please enter the second angle: "))
    a3 = int(input("please enter the third angle: "))
        
    if a1 + a2>= a3 and a2 +a3>= a1 and a3 + a1>=a2:
        print("the entered angles form a triangle")
    else:
        print("the entered values do not form a tringle")

    if a1 == a2 == a3:
        print("the angle formed from given values is a EQUILATERAL TRIANGLE")
    elif a1 == a2 or a2 == a3 or a1 == a3:
        print("the angle formed from given values is a ISOSCELES TRIANGLE ")
    else:
        print("the angle formed from given values is a SCALENE TRIANGLE")

    import datetime
    now = datetime.datetime.now()
    print("\ntodays date: ,todays time: ")
    print(now.strftime("%m-%d-%Y"), now.strftime("%H-%M-%S"))

