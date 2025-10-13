def rotate(matrix: list[list[int]]) -> None:
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if y < x: matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    
    for y in range(len(matrix)):
        right = len(matrix)-1
        for left in range(0, len(matrix)):
            if right <= left: break

            matrix[y][left], matrix[y][right] = matrix[y][right], matrix[y][left]

            right -= 1

    print(matrix)

rotate(matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]
                 ])
rotate(matrix = [[5, 1, 9, 11],
                 [2, 4, 8, 10],
                 [13,3, 6, 7 ],
                 [15,14,12,16]
                 ])
