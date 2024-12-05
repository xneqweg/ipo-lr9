from collision import fifth,second,third,fourth
second.isCorrectRect()
third.isCollisionRect()
fourth.intersectionAreaRect()
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
fifth.intersectionAreaMultiRect(rectangles)