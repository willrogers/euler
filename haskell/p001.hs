-- list comprehensions
s = [1..999]
a = [x | x <- s, rem x 3 == 0 || rem x 5 == 0]
c = sum a

-- filter
d = sum (filter threeOrFive [1..999])
    where threeOrFive x = rem x 3 == 0 || rem x 5 == 0

main = do print d
