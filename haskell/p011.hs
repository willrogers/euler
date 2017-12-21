filename = "../data/grid.txt"

intify :: [[Char]] -> [Int]
intify nums = [read x::Int | x <- nums]

col :: Int -> [[Int]] -> [Int]
col x matrix = [row !! x | row <- matrix]

first4prod :: [Int] -> Int
first4prod ns = product $ take 4 ns

inc :: Int -> Int
inc x = x + 1

enumerate :: [a] -> [(Int, a)]
enumerate ls = zip (iterate inc 0) ls

iterateN :: Int -> ([a] -> [a]) -> [a] -> [[a]]
iterateN n f l = take n (iterate f l)

-- avoid the exception from calling tail on an empty list
prod4_ :: [Int] -> [Int]
prod4_ ns = [first4prod x | x <- iterateN (length ns) tail ns]

main = do
    file <- readFile filename
    let ls = lines file
    let numStrings = [words l | l <- ls]
    let ints = [intify ns | ns <- numStrings]
    let cols = [col n ints | n <- [0..length (head ints) - 1]]
    let x = maximum $ [maximum (prod4_ row) | row <- ints]
    let y = maximum $ [maximum (prod4_ col) | col <- cols]
    -- so far only rows and columns
    print $ maximum [x, y]
