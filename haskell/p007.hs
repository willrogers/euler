
prime :: Int -> Bool
prime 1 = False
prime 2 = True
-- use fromIntegral to ensure that the input to sqrt is consistent
prime n = let x = truncate (sqrt (fromIntegral n::Double)) in
            all (\z-> n `mod` z /= 0) [x, x-1..2]

primes n count target = if count == target then n - 1
                 else if prime n then primes (n + 1) (count + 1) target
                 else primes (n + 1) count target

main = do print (primes 2 0 10001)
