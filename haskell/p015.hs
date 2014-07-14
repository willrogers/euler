-- too slow!
gridSize = 20

paths x y size
    | x == size = 1
    | y == size = 1
    | otherwise  = paths (x+1) y size + paths x (y+1) size


main = do print $ paths 0 0 gridSize
