

LIMIT = 4000000

f1 = 1
f2 = 2

tot = 2

while f2 < LIMIT do
  tmp = f2
  f2 = f2 + f1
  f1 = tmp
  if f2 % 2 == 0
    tot += f2
  end
end

puts tot
