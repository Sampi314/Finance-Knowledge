# Monday Morning Mulling: November 2017 Challenge – Freaky Friday!

**Source:** https://sumproduct.com/blog/monday-morning-mulling-november-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: November 2017 Challenge – Freaky Friday!

*   November 26, 2017

Monday Morning Mulling: November 2017 Challenge – Freaky Friday!
================================================================

Monday Morning Mulling: November 2017 Challenge – Freaky Friday!
================================================================

27 November 2017

Last Friday’s Final Friday Fix was about Black Friday. A quick recap:

*   For any given Friday – like Black Friday 24th, when can I expect it to be Friday the 24th again?
*   For any given year, which date is the Black Friday so one can get specials?
*   And as a bonus question, when will we have another Black Friday sale on the 24th of November?

Let’s look at the first problem

**Calculating the next Friday 24th**

As one knows about Friday 13th, the longest period that can occur without a Friday the 13th.

Breaking that down:

*   Generate the next 14 months combination with that day
*   Check if they lie on a Friday
*   Return the result

Firstly, let’s check the next 14 months to see if that particular number day of the month lies on a Friday and return with that first result. This can be done in a line, in a single formula, using an array calculation to get all 14 months. Then enter the WEEKDAY() Function. Weekday takes a date and then returns a numeric value representing the day of the week, Friday being the 6th day of the week (where Sunday is the 1st). Combine that with the MATCH function to find which month it is the next in the series.

A trick to generate an array of numbers without typing them {1,2,3,4,5…} is to use the ROW function. By using the ROW function, that returns an array with the numbers of the rows in question. To generate {1..14} use the following:

ROW(A1:A14)

To generate the dates, use the DATE function to generate the serial dates (dates in Excel formats), it takes three parameters, the year, month and day.

For the year, simply either enter a year number or find the year of any given date like today, TODAY(), by using the formula:

YEAR(TODAY())

The month and day can be generated in the same way.

To find the next month, combining match with Row, let’s assume that looking from TODAY():

NextCorrespondingMonth = MATCH(TRUE,WEEKDAY(DATE(YEAR(TODAY()),ROW($A$1:$A$15)+MONTH(TODAY())+IF(DAY(TODAY())<24 ,-1,0),24))=6,0)

The IF statement, checking if today is less than the 24th is to ensure that it checks the rest of the existing month as well, hence subtracting 1.

Then, by adding the number of months to the current date, the next occurrence will occur.

NextBlackFriday = DATE(YEAR(TODAY), MONTH(TODAY) + NextCorrespondingMonth, 24)

However, as the match is operated on an ARRAY, Ctrl + Shift + Enter must be used in order for Excel to recognise the array function and calculate correctly.

**Calculating the date of Black Friday**

Thanksgiving in the USA is defined to be the fourth Thursday in the month of November. So given the year, look at the fourth Thursday and check what the date is + 1 for Black Friday. How is this done in Excel?

What can be done is by checking through all the combinations of dates for that period, finding which one would be a Friday. This is done on the DAY instead of the MONTH.

To calculate Thanksgiving, the initial Thursday can start with a number between 1 to 7. Add 22 days to get the Black Friday (3 weeks to give the 4th Thursday and then 1 extra day)

So for 2017, Black Friday can be calculated as

\=DATE(2017,11,MATCH(TRUE,WEEKDAY(DATE(Input\_BFYear,11,ROW($A$1:$A$7)+22))=6,0)+22)

Remember, this is an array calculation as well so Ctrl + Shift + Enter!

**Calculating the date of the next identical Black Friday**

The Gregorian Calendar identically loops on a 400 year cycle. Why is this the case? This is because despite that every year shifts each calendar day by one, each leap year shifts each calendar day by TWO days. But leap years don’t always occur every four years. When it is a 100 year like 1900, unless it is divisible by 400 like 2000, they aren’t leap years.

Though a collision of an identical Black Friday is more likely to occur within a 28 year period when the full combination of common and leaps years can occur. Just in case our dataset includes a centennial we should include another 28 years into our set to counteract this phenomenon.

Hence, the next identical Black Friday can be calculated as:

\=DATE(YEAR(TODAY())+MATCH(TRUE,WEEKDAY(DATE(YEAR(TODAY())+ROW($A$1:$A56),11,24))=6,0),11,24)

![](<Base64-Image-Removed>)

[Check out the workbook here](https://sumproduct.com/assets/blog-pictures/2017/final-friday/nov-17/sp-next-friday.xlsm)
 that performs these tricks with a few bonus extras! It includes an input date instead of using TODAY() and choosing not just Friday 24 but Monday 24 as well. Enjoy.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-november-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-november-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-november-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-november-2017-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-november-2017-challenge/#0 "close")

top