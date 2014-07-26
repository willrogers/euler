
-- True if all numbers up to n divide x
divall :: Int -> Int -> Bool
divall x 1 = True
divall x n 
        | x `mod` n /= 0 = False
        | otherwise = divall x (n-1)


mindivall :: Int -> Int -> Int
mindivall x n = if divall x n then x
                else mindivall (x + 1) n

mindivall' :: Int -> Int
mindivall' x = mindivall 1 x

main = do print (mindivall' 20)
