import System.IO

datafile = "../data/triangle.txt"

maxRoute :: [[Int]] -> Int -> Int -> Int -> Int
maxRoute triangle x y tot
    | length triangle == x = tot
    | otherwise = y


main = do
    contents <- readFile datafile
    let rows = lines contents
    let ws = [words r | r <- rows]
    let nums = [[read n :: Int | n <- ns ] | ns  <- ws]
    print nums
    print $ maxRoute nums 0 0 
    print $ nums !! 0 !! 0

