from main import solve

words = {
                       #1000   # tens #elevens 
    "one"      : 190 + 1,
    "two"      : 190,
    "three"    : 190,
    "four"     : 190,
    "five"     : 190,
    "six"      : 190,
    "seven"    : 190,
    "eight"    : 190, 
    "nine"     : 190, 
    "ten"      : 10, 
    "eleven"   : 10, 
    "twelve"   : 10, 
    "thirteen" : 10, 
    "fourteen" : 10, 
    "fifteen"  : 10, 
    "sixteen"  : 10, 
    "seventeen": 10, 
    "eighteen" : 10, 
    "nineteen" : 10,
    "twenty"   : 100, 
    "thirty"   : 100, 
    "forty"   : 100,
     "fifty"   : 100, 
     "sixty"   : 100, 
     "seventy" : 100, 
     "eighty"  : 100, 
     "ninety"  : 100, 
     "hundred" : 900,
    "thousand" : 1,
    "and"      : 891
}

length = 0
for word in words:
    length += len(word) * words[word]
solve(length)
