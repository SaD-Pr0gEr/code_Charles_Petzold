"""
Braille and binary codes

Louis Braille alphabet
Every symbol(letter, number, signs punctuation) encoded as 1 or more
dots in a two-by-three-dot cell. These dots in cell are numerated
from 1 to 6

    1   4
    2   5
    3   6

Braille code is binary too(cause dots are convex or flat)
So, this system obeys to same system Morze, and we can calculate
count of unique combinations(aka symbols)
2x2x2x2x2x2 = 64
As we can see, in Braille system we can see 64 unique codes

From A to J used 4 upper dots(1, 2, 4, 5)
From K to T used 5 dots(1, 2, 3, 4, 5)
From U to Z used all 6 dots(1, 2, 3, 4, 5, 6)
"""
