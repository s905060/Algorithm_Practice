#/usr/bin/env python2.7

"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
"""

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

top = 0
bottom = len(matrix)
left = 0
right = len(matrix[0])

while top != bottom and left != right:
    for i in xrange(left, right):
        print matrix[top][i]
    top +=1

    for i in xrange(top, bottom):
        print matrix[i][right-1]
    right -=1

    for i in xrange(right-1, left, -1):
        print matrix[bottom-1][i]
    bottom -=1

    for i in xrange(bottom, top-1, -1):
        print matrix[i][left]
    left +=1
