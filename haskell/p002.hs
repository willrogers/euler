limit = 4000000

-- infinite list of fibonacci numbers
fib = 0 : scanl (+) 1 fib

evenList :: (Integral a) => [a] -> [a]
evenList [] = []
evenList (x:xs) = if even x then x:evenList xs else evenList xs

maxSumListAcc :: (Num a, Ord a) => a -> [a] -> a -> a
maxSumListAcc _ [] tot = tot
maxSumListAcc max (x:[]) tot = if x > max then tot else tot + x
maxSumListAcc max (x:xs) tot = if x > max
                                 then tot
                                 else maxSumListAcc max xs (tot + x)

maxSumList :: (Num a, Ord a) => a -> [a] -> a
maxSumList max xs = maxSumListAcc max xs 0

maxVal = maxSumList limit $ evenList fib

-- alternative using more Haskell features
fib' = scanl1 (+) (0:1:fib')
maxVal' = sum (takeWhile (\x -> x <= limit) (filter even fib'))


main = do print maxVal'
