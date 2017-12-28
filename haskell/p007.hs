import Utils

primes n count target = if count == target then n - 1
                 else if prime n then primes (n + 1) (count + 1) target
                 else primes (n + 1) count target

main = do print $ primes 2 0 10001
