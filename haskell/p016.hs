

twotox 0 = 1
twotox n = 2 * twotox (n - 1)

sumdig n 
    | d == 0 = n
    | otherwise = r + sumdig d
    where d = n `div` 10
          r = n `mod` 10

main = do print $ sumdig $ twotox 1000
