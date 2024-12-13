"""8. Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times"."""

while True:
    num = int(input("Enter a number between -12 and 12 for the times table: "))

    if -12 <= num <= 12:
        if num >= 0:
            for i in range(13):
                print(num, "x", i , "=" , i * num)
        else:
            for i in range(12, -1, -1):
                print(num, "x", i ,"=", i * num)
    else:
        print("Invalid input!")
