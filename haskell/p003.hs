
target = 600851475143


-- this works but it's too slow
-- schoolboy error: trying high numbers first
factor :: Integral a => a -> [a] -> a -> [a]
factor 1 factors _ = factors
factor 2 factors _ = 2:factors
factor n factors 1 = n:factors
factor n factors count = if n `mod` count == 0 
                         then factor count (d:factors) (count - 1)
                         else factor n factors (count - 1)
                         where d = n `div` count

-- simplify function to make it more user-friendly
factor' n = factor n [] (n `div` 2)


-- count from 2 to n/2; could still be more efficient
factor2 :: Int -> [Int] -> Int -> [Int]
factor2 1 factors _ = factors
factor2 2 factors _ = 2:factors
factor2 n factors count 
                    | (fromIntegral count :: Double) > ((fromIntegral n :: Double) / 2) = n:factors -- prime so add to the list
                    | (n `mod` count == 0) = factor2 d (count:factors) 2
                    | otherwise = factor2 n factors (count + 1)
                    where d = n `div` count

-- simplify function to make it more user-friendly
factor2' :: Int -> [Int]
factor2' n = factor2 n [] 2


main = do print (factor2' target)

