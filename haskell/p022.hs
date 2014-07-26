import Data.Text
import Data.List 

file = "data/names.txt"

alpha = ['A'..'Z']
charVal c =  case (elemIndex c alpha) of 
                Nothing -> 0
                Just val  -> val + 1


score :: String -> Int
score [] = 0
score (x:xs) = (charVal x) + (score xs)

main = do
   content <- readFile file
   let content2 = Prelude.lines content
   let names = splitOn (pack ",") (pack (Prelude.head content2))
   let names2 = [unpack name | name <- names]
   let names3 = [Prelude.init (Prelude.tail name) | name <- names2]
   let names4 = sort names3
   let tot = sum  [x * (score y) | (x,y) <- Prelude.zip [1..] names4]
   print tot 
