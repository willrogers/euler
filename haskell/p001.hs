

s = [1..1000]

a = [x | x <- s, rem x 3 /= 0, rem x 5 /= 0]
c = sum a

main = print c
