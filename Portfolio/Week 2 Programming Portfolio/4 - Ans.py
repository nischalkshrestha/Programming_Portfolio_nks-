"""4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over."""

sweets = int(input("Number of sweets: "))
pupils = int(input("Number of pupils: "))
sweets_pupil = sweets // pupils
leftover_sweets = sweets % pupils
print("The sweets given to each pupil is",sweets_pupil,"and the number of left over sweets is",leftover_sweets) 