import Data.List 

squares = [x * x | x <- [1..1000]]

doubles = [(x, y) | x <- [1..1000], y <- [1..1000], elem (x*x+y*y) squares]

intSqrt :: Integer -> Integer -> Integer
intSqrt x y = floor (sqrt ( fromIntegral (x * x + y * y) ))

triples = [(x, y, (intSqrt x y)) | (x, y) <- doubles]

ttriples = nub [ x * y * z | (x,y,z) <- triples, x + y + z == 1000]

main = do print $ head ttriples
