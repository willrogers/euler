
TARGET = 600851475143

def is_prime(n)
  if n < 1
    return false
  end
  (2..n-1).each do |x|
    if n % x == 0
      return false
    end
  end
  return true
end

factors = []
test = TARGET
x = 2

while test > 1 do
  if test % x == 0
    factors << x
    test /= x
    x = 2
  else
    x += 1
  end
end

factors.sort
puts factors[-1]
