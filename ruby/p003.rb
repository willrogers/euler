
TARGET = 600851475143


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
