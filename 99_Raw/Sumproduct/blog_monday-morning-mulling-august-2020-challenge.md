# Monday Morning Mulling: August 2020 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-august-2020-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: August 2020 Challenge

*   August 30, 2020

Monday Morning Mulling: August 2020 Challenge
=============================================

Monday Morning Mulling: August 2020 Challenge
=============================================

31 August 2020

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

Welcome to the **50th** Monday Morning Mulling. On this special occasion, it seems timely to have a time series challenge.

**_The Challenge_**

When building a financial model, time series are important. Most people know how to build a time series when each column represents a year, a quarter, a month, _etc._ (if you don’t, it is highly recommended that you take our [Financial Modelling course](https://www.sumproduct.com/courses/financial-modelling)
). Here is such an example:

![](<Base64-Image-Removed>)

But what do you do when you want a time period that is less than a day, with dynamic blocks in hours, say, like the one below? This was our Friday challenge.

![](<Base64-Image-Removed>)

The requirement was that when you change the inputs, the time series automatically updates:

![](<Base64-Image-Removed>)

To aid understanding of our suggested solution, please feel free to refer to the [associated Excel file](https://sumproduct.com/assets/blog-pictures/2020/fff-mmm/aug/fff/sp-time-series-challenge.xlsm)
.

**_Suggested Solution_**

First, we will prepare our ‘**Daily Time Series**‘ sheet. In cell **J6**, we use the **TODAY** function to get today’s date, then format it as a text ‘**Today**‘ and give it the range name **_Today_** in the Name Box. We will also need a few inputs, being the number of days in the time series, the number of blocks of hours per day and the number of hours per day (which should be a constant, rather than a variable, assuming you are a resident of Earth). These input cells are given a corresponding name in the Name Box, _viz._

![](<Base64-Image-Removed>)

Having all our inputs ready, we will calculate the **Hour** series by using the **[MOD](https://www.sumproduct.com/thought/a-modicum-of-mod)
**and **[\>SEQUENCE](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
**functions.

The **MOD** function, **MOD(number, divisor)**, returns the remainder after the **number** (first argument) is divided by the **divisor** (second argument). The result has the same sign as the **divisor**. Here, the **MOD** function is used to set up the hour block number _e.g._ 0 / 6 / 12 / 18, if we are breaking the day into quarters.

The **SEQUENCE** function, **SEQUENCE(rows, \[columns\], \[start\], \[step\])**, allows you to generate a list of sequential numbers in an array, such as 1, 2, 3, 4. For example, **SEQUENCE(4)** will generate the numbers 1, 2, 3 and 4 down a column, whereas **SEQUENCE(1,4)** will generate the same sequence across a row – which is what we want. In this case, we require a time series which automatically propagates across a row with a width of **Number\_of\_days\*Blocks\_per\_day**, _i.e._ 4\*3 = 12 columns, in our example above. We will nest this **SEQUENCE** formula inside the **MOD** formula to get the width of the series:

**\=MOD(Today+(SEQUENCE(1,Number\_of\_days\*Blocks\_per\_day)),1)**

![](<Base64-Image-Removed>)

In the first part of the formula, we want to get the block separations in a day unit, hence, we need to divide the numerator by **Blocks\_per\_day**:

**\=MOD(Today+(SEQUENCE(1,Number\_of\_days\*Blocks\_per\_day))/Blocks\_per\_day,1)**

![](<Base64-Image-Removed>)

The series is now not starting from zero but ending at zero, while we want it to count from zero. The trick here is we will subtract one (1) in the numerator part to bring it back to the normal zero starting series. If we have a series that starts from one (1), _e.g._ counting the month number in a quarter, just add one (1) after the final close bracket.

**\=MOD(Today+(SEQUENCE(1,Number\_of\_days\*Blocks\_per\_day)-1)/Blocks\_per\_day,1)**

![](<Base64-Image-Removed>)

We need to multiply the series with the number of hours per day to get the correct hour block:

**\=MOD(Today+(SEQUENCE(1,Number\_of\_days\*Blocks\_per\_day)-1)/Blocks\_per\_day,1)\*Hours\_per\_day**

![](<Base64-Image-Removed>)

With the **Hour** series ready, we can calculate the **Date** series. The **Date** will be filled only at the zero-hour marks. Similarly, we use the **SEQUENCE** function to work out the actual date series; and we use the **TEXT** function to keep the correct date formatting:

**\=IF(J10#,””,TEXT(Today+(SEQUENCE(1,Number\_of\_days\*Block\_per\_day)-1)/Block\_per\_day,”d/mm/yyyy”))**

![](<Base64-Image-Removed>)

It’s true this solution requires dynamic arrays to work, but as we hit our 50th challenge, we thought we should look to the future of Excel rather than remain in the past.

Until next month!

_The Final Friday Fix will return on Friday 25 September with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-august-2020-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-august-2020-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-august-2020-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-august-2020-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-august-2020-challenge/#0 "close")

top