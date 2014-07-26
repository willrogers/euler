module Utils where


-- count from 2 to n/2; could still be more efficient
factor' :: Integer -> [Integer] -> Integer -> [Integer]
factor' 1 factors _ = factors
factor' 2 factors _ = 2:factors
factor' n factors count 
                    | (fromIntegral count :: Double) > ((fromIntegral n :: Double) / 2) = n:factors -- prime so add to the list
                    | (n `mod` count == 0) = factor' d (count:factors) 2
                    | otherwise = factor' n factors (count + 1)
                    where d = n `div` count

-- simplify function to make it more user-friendly
factor :: Integer -> [Integer]
factor n = factor' n [] 2

factorialn :: Integer -> Integer
factorialn 0 = 1
factorialn n = n * factorialn (n - 1)

factorial' :: Integer -> Integer -> Integer
factorial' 0 count = count
factorial' n count = factorial' (n - 1) (count * n)

factorial :: Integer -> Integer
factorial n = factorial' n 1


sumdign :: Integer -> Integer
sumdign n 
    | d == 0 = n
    | otherwise = r + sumdign d
    where d = n `div` 10
          r = n `mod` 10

sumdig' :: Integer -> Integer -> Integer
sumdig' n count
    | d == 0 = count + n
    | otherwise = sumdig' d (count+r)
    where d = n `div` 10
          r = n `mod` 10

sumdig :: Integer -> Integer
sumdig n = sumdig' n 0
