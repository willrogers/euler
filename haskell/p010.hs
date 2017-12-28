import Utils

target = 2000000

sumPrimes n = sum $ filter prime (2:[3,5..n])

main = do print $ sumPrimes target
