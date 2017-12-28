-- The problem
file = "data/p008_bignumber.txt"


bigdig :: Integer -> Integer -> Integer
bigdig n best
    | q == 0 = next
    | otherwise = bigdig q next
    where q = n `div` 10
          r = n `mod` 10
          next = max r best

nmult' :: Integer -> Integer -> Integer -> Integer -> Integer
nmult' n big tot count 
    | count < 0 = error "Can't select less than one number"
    | count > n = error "Started too high"
    | count == n = tot
    | otherwise = nmult' n q (tot*r) (count+1)
    where q = big `div` 10
          r = big `mod` 10

nmult :: Integer -> Integer -> Integer
nmult n big = nmult' n big 1 0

maxmult :: Integer -> Integer -> Integer
maxmult 0 _ = 0
maxmult _ 0 = 0
maxmult n big = max (nmult n big) (maxmult n (big `div` 10))

remNewLine [] = []
remNewLine xs = [ x | x <- xs, x /= '\n' ]


main = do fileString <- readFile file
          let ifile = (read (remNewLine fileString)) :: Integer
          print $ maxmult 13 ifile

