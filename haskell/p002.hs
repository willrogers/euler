
limit = 4000000

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib 2 = 1
fib x = fib (x-1) + fib (x-2)


sumfib count limit tot = let fc = fib count in 
                         if (fc > limit) 
                         then tot
                         else 
                            if even fc 
                            then tot + fc +  sumfib (count + 1) limit tot 
                            else tot + sumfib (count + 1) limit tot

sumfib' count limit = sumfib count limit 0

main = print (sumfib' 2 limit)
