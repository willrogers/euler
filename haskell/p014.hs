
collatz :: [Int] -> Int -> [Int]
collatz x 1 = 1:x
collatz x n
    | n `mod` 2 == 0 = collatz (a:x) a
    | otherwise = collatz (b:x) b
    where a = n `div` 2
          b = 3*n + 1

collatz' :: Int -> [Int]
collatz' n = collatz [] n

lenCollatz :: Int -> Int
lenCollatz n = length $ collatz' n

bigCollatz :: Int -> Int -> Int -> Int -> Int
bigCollatz count target max biggest
    | count == target = biggest
    | lc > max = bigCollatz (count + 1) target lc count
    | otherwise = bigCollatz (count + 1) target max biggest
    where lc = lenCollatz count

bigCollatz' :: Int -> Int
bigCollatz' target = bigCollatz 1 target 0 1

main = do print $ bigCollatz' 1000000
