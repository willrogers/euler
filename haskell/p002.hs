
limit = 4000000

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib 2 = 1
fib x = fib (x-1) + fib (x-2)

-- fibs = [ fib x | x <- [1..], fib x < limit ] 

-- fibs2 = [ x | x <- fibs, x < limit]

sumfib count limit tot = if (fib count > limit) then tot
                   else if even(fib count) then tot + fib count +  sumfib (count + 1) limit tot else tot + sumfib (count + 1) limit tot

sumfib' count limit = sumfib count limit 0

main = print (sumfib' 2 limit)
