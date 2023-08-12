"""
We divided Morze alphabet to 4 tables

1 -> 1 dot/dash -> ./-
2 -> 2 comb of dots/dashes -> .-/-./--/..
3 -> 3 comb of dots/dashes -> .../..-/.--/--./-../---/-.-/.-./
4 -> 4 comb of dots/dashes -> ..../...-/..--/.---/---./--../-.../---- etc.
In each next table, the number of codes is more than 2 times the previous one.

We can write these diagrams to understand
__________________________________________
| Dots and dashes count | 1 | 2 | 3 | 4  |
|      Codes count      | 2 | 4 | 8 | 16 |
__________________________________________

We can write this diagram with another format
__________________________________________
| Dots and dashes count | 1 | 2 | 3 | 4  |
|      Codes count      | 2¹| 2²| 2³| 2⁴ |
__________________________________________

Code Morze is called binary.
We always can describe Binary codes and objects as degree 2(2², 2³ etc.)
"""
