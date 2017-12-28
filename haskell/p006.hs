
target = 100

sumSq n = sum ( [x*x | x <- [1..n]] )

sqSum n = x * x where x = sum [1..n]

main = do print (sqSum target - sumSq target)
