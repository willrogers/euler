"""
Sum the letters of all the words from 1 to 1000 inclusive.
Ignore hyphens and spaces.
http://projecteuler.net/problem=17

I'm not sure if this is a quick way to do it.  Never mind.
"""


one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"
ten = "ten"
eleven = "eleven"
twelve = "twelve"
thirteen = "thirteen"
fourteen = "fourteen"
fifteen = "fifteen"
sixteen = "sixteen"
seventeen = "seventeen"
eighteen = "eighteen"
nineteen = "nineteen"
twenty = "twenty"
thirty = "thirty"
forty = "forty"
fifty = "fifty"
sixty = "sixty"
seventy = "seventy"
eighty = "eighty"
ninety = "ninety"
hundred = "hundred"
thousand = "thousand"

plus = "and"


def len_list(list):
    length = 0
    for item in list:
        length += len(item)  
    return length

one_to_nine = [one, two, three, four, five, six, seven, eight, nine]
one_to_nine_len = len_list(one_to_nine)

teens = [eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]
teens_len = len_list(teens)

ties = [twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety]

hundred_len = 0
hundred_len += one_to_nine_len
hundred_len += len(ten)
hundred_len += teens_len
# Twenty and above
for item in ties:
    hundred_len += len(item) * 10
    hundred_len += one_to_nine_len


thousand_len = 0
thousand_len += hundred_len
for item in one_to_nine:
    thousand_len += (len(item) + len(hundred)) * 100
    thousand_len += len(plus) * 99
    thousand_len += hundred_len
thousand_len += len(one) + len(thousand)


print thousand_len
