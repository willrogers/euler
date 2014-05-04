
limit = 10

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib 2 = 1
fib x = fib (x-1) + fib (x-2)

fibs = [ fib x | x <- [0..10] ] 

fibs2 = [ x | x <- fibs, x < limit]

main = print (sum fibs2)
