class RectCorrectError(Exception):
   pass

def isCollisionRect():
    first=[(-3.4, 1),(9.2, 10)]
    second=[(-7.4, 0),(13.2, 12)]
    x1_first=first[0][0]
    x2_first=first[1][0]
    x1_second=second[0][0]
    x2_second=second[1][0]
    y1_first=first[0][1]
    y2_first=first[1][1]
    y1_second=second[0][1]
    y2_second=second[1][1]
    if((y2_first<y1_second)or(y2_second<y1_first)):
        raise RectCorrectError('1й прямоугольник некоректный')
    elif((x2_first<x1_second) or(x2_second<x1_first)):
        print("False")
    else:
            print("True")