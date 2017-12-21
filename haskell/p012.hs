import Utils

target = 500

ndivs :: Integer -> Integer -> Bool
ndivs x limit = (length (divs x)) < fromIntegral limit

nd :: Integer -> Bool
nd x = ndivs x target

main = do
    let tris = dropWhile (nd) triangle
    print $ head tris
