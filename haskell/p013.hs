file = "data/longs.txt"


main = do fileString <- readFile file
          let ints = [read l::Integer | l <- lines fileString]
          let firstTen = take 10 (show (sum ints))
          print $ (read firstTen :: Integer)

