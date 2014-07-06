
target = 600851475143


prime :: Int -> Bool
prime 1 = False
prime 2 = True
-- use fromIntegral to ensure that the input to sqrt is consistent
prime n = let x = truncate (sqrt (fromIntegral n::Double)) in
            all (\z-> n `mod` z /= 0) [x, x-1..2]

-- this works but it's too slow
factor :: Integral a => a -> [a] -> a -> [a]
factor 1 factors _ = factors
factor 2 factors _ = 2:factors
factor n factors 1 = n:factors
factor n factors count = if n `mod` count == 0 
                         then factor count (d:factors) (count - 1)
                         else factor n factors (count - 1)
                         where d = n `div` count

factor' n = factor n [] (n `div` 2)

main = do print (prime 2)
          print (prime 3)
          print (prime 4)
          print (prime 5)
          print (prime 104)
          print (factor' 2)
          print (factor' 103)
          print (factor' 4)
          print (factor' 8)
          print (factor' 21)
          print (factor' target)

