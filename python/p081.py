"""
Minimal path sum.

I used lists rather than numpy.
"""
import utils


FILE = 'p081_matrix.txt'


def load(filename):
    content = utils.load_data(FILE)

    rows = content.split('\n')
    data = [[int(i) for i in row.split(',')] for row in rows]
    return data


def process(matrix):
    minsum = [[0 for i in data] for j in data[0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                minsum[i][j] = matrix[i][j]
            elif i == 0:
                minsum[i][j] = minsum[i][j-1] + matrix[i][j]
            elif j == 0:
                minsum[i][j] = minsum[i-1][j] + matrix[i][j]
            else:
                minsum[i][j] = min(minsum[i][j-1], minsum[i-1][j]) + matrix[i][j]
    return minsum


if __name__ == '__main__':
    data = load(FILE)
    minsum = process(data)
    print(minsum[len(minsum)-1][len(minsum[0])-1])
