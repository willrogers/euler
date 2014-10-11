
LIMIT = 999
tot = 0

(1..LIMIT).each do |n|
	if n % 3 == 0
		tot += n
	elsif n % 5 == 0
		tot += n
	end
end

puts tot
