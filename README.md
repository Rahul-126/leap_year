# leap_year
a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
This is how you work out whether if a particular year is a leap year.

 1) -> on every year that is divisible by 4 with no remainder
 2) -> except every year that is evenly divisible by 100 with no remainder
 3) -> unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using this flow chart .

e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.

But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, including spelling an punctuation.

Example Input 1
2400
Example Output 1
Leap year
Example Input 2
1989
Example Output 2
Not leap year
