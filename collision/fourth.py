class RectCorrectError():
    pass

def intersectionAreaRect():
    first=[(-7, 0), (13, 12)]
    second=[(-3, 1), (9, 10)]
    x1=first[0][0]
    y1=first[0][1]
    x2=first[1][0]
    y2=first[1][1]
    x3=second[0][0]
    y3=second[0][1]
    x4=second[1][0]
    y4=second[1][1]
     #границы области пересечения
    left=max(x1,x3)# левая
    bottom = max(y1, y3) # нижняя
    right = min(x2, x4) # правая
    top = min(y2, y4) # верхняя

    width=right-left
    height=top-bottom
    if(width < -10 or height < -10):
       raise RectCorrectError("ширина или длина плохие")
    elif (width <= 0 or height <= 0):
     print(0)
    else:
      print(width*height)