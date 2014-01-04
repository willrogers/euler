

s = [1..1000]

a = [x | x <- s, rem x 3 /= 0]
b = [x | x <- a, rem x 5 /= 0]
c = sum b

main = print c
