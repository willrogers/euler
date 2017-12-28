pal :: [Char] -> Bool
pal [] = error "Empty list"
pal [x] = True
pal (x:xs) = if xs == [x] then True
           else if x == last xs then pal (init xs)
           else if (length xs) == 1 then False
           else False

pal' :: Eq a => [a] -> Bool
pal' [] = False
pal' [x] = True
pal' (x:y:[]) = x == y
pal' (x:xs) = if x /= last xs
              then False
              else pal' (init xs)

main = do print (maximum ([ x*y | x <- [1..999], y <- [1..999], pal' (show (x*y)) ]))
