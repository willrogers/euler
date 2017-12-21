import Utils

target = 500

ndivs :: Integer -> Integer -> Bool
ndivs limit x = (length (divs x)) < fromIntegral limit

main = do
    -- (ndivs target) is partial function application
    let tris = dropWhile (ndivs target) triangle
    print $ head tris
