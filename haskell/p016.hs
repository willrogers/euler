
import Utils

twotox :: Integer -> Integer
twotox 0 = 1
twotox n = 2 * twotox (n - 1)

main = do print $ sumdig $ twotox 1000
