module Utils where

import qualified Data.Set as Set

-- count from 2 to n/2; could still be more efficient
factor' :: Integer -> [Integer] -> Integer -> [Integer]
factor' 1 factors _ = factors
factor' 2 factors _ = 2:factors
factor' n factors count
    -- count is bigger than n/2: we have failed to factorise n so
    -- n is prime and needs to be included in the list of factors
    | (fromIntegral count :: Double) > ((fromIntegral n :: Double) / 2) = n:factors
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

-- naive divisors
divisors' :: Integer -> [Integer] -> Integer -> [Integer]
divisors' n ds count
    -- if count is bigger than half the number, the only divisor left
    -- is the number itself
    | (fromIntegral count :: Double) > ((fromIntegral n ::Double) / 2) = n:ds
    | count < 1 = ds
    | n `mod` count == 0 = divisors' n (count:ds) (count + 1)
    | otherwise = divisors' n ds (count + 1)

divisors :: Integer -> [Integer]
divisors n = divisors' n [] 1

-- more advanced divisors
combs' :: [Integer] -> [Integer] -> [Integer]
combs' [] results = results
combs' (x:xs) results = combs' xs (map (*x) results ++ results ++ [x])

combs :: [Integer] -> [Integer]
combs x = Set.toList (Set.fromList (combs' x []))

divs :: Integer -> [Integer]
divs x = combs (factor x)

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

prime :: Int -> Bool
prime 1 = False
prime 2 = True
-- use fromIntegral to ensure that the input to sqrt is consistent
prime n = let x = truncate (sqrt (fromIntegral n::Double)) in
            all (\z-> n `mod` z /= 0) [2,3..x]

-- different ways of generating counting numbers
inc :: Integer -> Integer
inc x = x + 1

countSimple :: [Integer]
countSimple = iterate inc 0

countLambda :: [Integer]
countLambda = iterate (\x -> x + 1) 0

countCompact :: [Integer]
countCompact = iterate (+1) 0

count :: [Integer]
count = [0..]


-- triangle numbers
triangle :: [Integer]
-- drop the initial zero using tail
triangle = tail (scanl (+) 0 count)
