module Utils where


-- count from 2 to n/2; could still be more efficient
factor' :: Int -> [Int] -> Int -> [Int]
factor' 1 factors _ = factors
factor' 2 factors _ = 2:factors
factor' n factors count 
                    | (fromIntegral count :: Double) > ((fromIntegral n :: Double) / 2) = n:factors -- prime so add to the list
                    | (n `mod` count == 0) = factor' d (count:factors) 2
                    | otherwise = factor' n factors (count + 1)
                    where d = n `div` count

-- simplify function to make it more user-friendly
factor :: Int -> [Int]
factor n = factor' n [] 2
