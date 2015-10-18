limit = 4000000

-- infinite list of fibonacci numbers
-- http://www.techrepublic.com/article/infinite-list-tricks-in-haskell/
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


main = do print $ maxSumList limit $ evenList fib
