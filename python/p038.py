

from utils import is_pandigital

answers = []

for i in range(10000):
    s = ""
    for j in range(1, 20):
        k = j * i
        s += str(k)
        if len(s) > 8:
            if len(s) == 9:
                if is_pandigital(s):
                    answers.append(int(s))
            else:
                continue


print max(answers)

