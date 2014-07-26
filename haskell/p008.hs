-- The problem
file = "data/bignumber.txt"
--longno = 35345246345745745646867891
longno = 2340200020020030304245040


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
-- remNewLine (x:xs) = if x == '\n' then remNewLine xs else x: (remNewLine xs)
remNewLine xs = [ x | x <- xs, x /= '\n' ]
            

main = do fileString <- readFile file
          let ifile = (read (remNewLine fileString)) :: Integer
          print $ maxmult 13 ifile

