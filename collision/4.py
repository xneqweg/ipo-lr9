class RectCorrectError(Exception):
    pass

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0

    for rect in rectangles:
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}")

    tot = rectangles[0]
    
    for rect in rectangles[1:]:
        (x1, y1), (x2, y2) = tot
        (x3, y3), (x4, y4) = rect

        #границы области пересечения
        left=max(x1,x3)# левая
        bottom = max(y1, y3) # нижняя
        right = min(x2, x4) # правая
        top = min(y2, y4) # верхняя

        width=right-left
        height=top-bottom

        if left<right and bottom<top:
            width=right-left
            height=top-bottom
        else:
            return 0  # Если нет пересечения, возвращаем 0

    return width*height

# Пример использования
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")