"""6. Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on."""


num = 7
i=1
for i in range(0,13):
    print(i, "x", num, "=", num*i)

