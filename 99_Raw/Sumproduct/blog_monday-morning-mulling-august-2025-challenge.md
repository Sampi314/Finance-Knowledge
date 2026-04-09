# Monday Morning Mulling: August 2025 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-august-2025-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: August 2025 Challenge

*   September 1, 2025

Monday Morning Mulling: August 2025 Challenge
=============================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

This month’s Final Friday Fix invited you to return the final weekdays of each month of the year in 2025.  We assumed a weekday was Monday through Friday.

You should have arrived at the following solution:

![](<Base64-Image-Removed>)

You can download the original question file [here](https://sumproduct.com/wp-content/uploads/2025/08/SP-Last-Working-Dates-Challenge.xlsx)
.

Guidelines that would’ve helped you get the most out of this challenge:

*   you may have used a reference cell that contains the year (2025)
*   the formula needed to be in just one cell (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA.

**_Suggested Solutions_**

You can find our Excel file [here](https://sumproduct.com/wp-content/uploads/2025/08/SP-Last-Working-Dates-Suggested-Solutions.xlsx)
, which shows our suggested solutions.

**SOLUTION A: USING WEEKDAY FUNCTION**

Firstly, use the [**LET**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-let-function)
 function as the basis for this entire calculation.  This will allow you to set up the first variable, variable **x**, which will represent the last date of each month using the following formula:

**_\=EOMONTH(DATE(E10,SEQUENCE(12),1),0)_**

where:

*   the [**SEQUENCE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-sequence-function)
     function generates a list of 12 month numbers from one \[1\] to 12
*   the [**DATE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-date-function)
     function creates a list of the first dates of all months in 2025 using the **year** argument as cell **E10**, **month** argument as the [**SEQUENCE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-sequence-function)
     above and **day** argument as one \[1\]
*   we finally use the [**EOMONTH**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-eomonth-function)
     function to find the last dates of all months based upon the date list created above.

![](<Base64-Image-Removed>)

Now, to set up the **y**\-variable, which will be the days subtracted from **x** to get to the last weekday of a month under the condition that the last date of the month falls on a weekend day.  This is achieved by using the **WEEKDAY** function.

First, enter in **y** as the variable, also, enter in the **WEEKDAY** function which has two \[2\] arguments.  For the **serial\_number** argument enter in **x**, and for **return\_type** enter in 16.  This will produce a number classification for **x** depending on the day of the week.  For context, this is the number sequencing shown using the **WEEKDAY** dialog box:

**_WEEKDAY(x,16)_**

![](<Base64-Image-Removed>)

Specifically, for option 16, Saturdays will be given the ID of one \[1\], Sundays two \[2\] and so forth with Fridays classified as seven \[7\].

All the variables in the [**LET**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-let-function)
 function have now been defined.  The final addition formula puts both variables **x** and **y** together by subtracting the last date of the month **x** by the number classification **y**

Note: the subtraction only occurs if the last day of the month is a weekend.

To perform the subtraction, use the [**IF**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-if-function)
 statement

**IF(y>2,0,y))**

where:

For any day classified as greater than two \[2\] (every weekday excluding weekends), the deduction will be zero \[0\].  Otherwise, use the day classification **y**.  In the case where a weekend day is the final day of the month, subtracting their classifications from their dates **x** will return the last Friday in the month, and therefore the last weekday date:

![](<Base64-Image-Removed>)

The full formula is:

**_\=LET(x,EOMONTH(DATE(E10,SEQUENCE(12),1),0),  
y,WEEKDAY(x,16),x-IF(y>2,0,y))_**

**SOLUTION B: USING WORKDAY FUNCTION**

If you’d like to simplify solution A, Excel has a function that excludes weekends and holidays automatically.  It does this through the **WORKDAY** function:

**_\=WORKDAY(DATE(E10,SEQUENCE(12)+1,1),-1)_**

where:

*   the [**SEQUENCE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-sequence-function)
     function generates a list of 12 month numbers from two \[2\] to 13
*   we then use the [**DATE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-date-function)
     function similarly to solution A.  For month 13, the [**DATE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-date-function)
     function will return the first month of the following year
*   finally, the **WORKDAY** function calculates the workday from a specific date.  Entering negative one \[-1\] in the **days** argument returns the previous working day of all respective dates.  This will provide the last working dates of all months:

![](<Base64-Image-Removed>)

_The Final Friday Fix will return on Friday 26 Sept 2025 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-august-2025-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-august-2025-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-august-2025-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-august-2025-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-august-2025-challenge/#0 "close")

top