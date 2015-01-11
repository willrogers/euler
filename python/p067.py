import utils


FILENAME = 'p067_triangle.txt'


def load_triangle():
    """
    Get the text into a 2D array of ints.
    """
    triangle_string = utils.load_data(FILENAME)
    triangle_lines = [line for line in triangle_string.split('\n')]
    triangle = [[int(x) for x in line.split()] for line in triangle_lines]
    return triangle


def solve(triangle, i, j, answers):
    """
    Simply add the current element to the maximum
    value of the parent solutions.
    """
    try:
        left_parent = answers[i-1, j-1]
    except KeyError:
        left_parent = None
    try:
        right_parent = answers[i-1, j]
    except KeyError:
        right_parent = None
    max_parent = max(left_parent, right_parent)
    return max_parent + triangle[i][j]


def find_max_path(triangle):
    answers = {(0, 0): triangle[0][0]}
    height = len(triangle)

    for i in range(1, height):
        for j in range(i+1):
            answers[(i, j)] = solve(triangle, i, j, answers)

    last_row = []
    for i in range(height-1):
        last_row.append(answers[height-1, i])

    return max(last_row)

TRIANGLE = load_triangle()
print(find_max_path(TRIANGLE))
