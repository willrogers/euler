-- too slow!
gridSize = 12

paths' :: Integral a => a -> a -> a -> a
paths' x y size
    | x == size = 1
    | y == size = 1
    | otherwise  = paths' (x+1) y size + paths' x (y+1) size

paths :: Integral a => a -> a
paths size = paths' 0 0 size

npaths num = [ paths n | n <- [1..num] ]

main = do print $ paths gridSize
          print $ npaths 14
