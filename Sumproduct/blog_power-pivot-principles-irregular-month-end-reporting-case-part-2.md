# Power Pivot Principles: Irregular Month-End Reporting Case – Part 2

**Source:** https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-2/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Irregular Month-End Reporting Case – Part 2

*   August 24, 2020

Power Pivot Principles: Irregular Month-End Reporting Case – Part 2
===================================================================

Power Pivot Principles: Irregular Month-End Reporting Case – Part 2
===================================================================

25 August 2020

_Welcome back to the Power Pivot Principles blog. This week, we will continue with our irregular month-end reporting case study._

To recap, we have a sales data set of four product lines in a supermarket over four years. This supermarket has a rule for month-end reporting, which is the reporting end of month day is the final Thursday of a month, regardless of whether it matches the end of the calendar month.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-158-1.jpg)

[Last week](https://www.sumproduct.com/)
, by using the **EOMONTH** and the **WEEKDAY** functions, we worked out the calendar end of month day and day in week. Then, we used a set of comparison rules to work out the ‘**Reporting End of Month’**:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-146-1.jpg)

At the end of the last blog, we hinted about using ‘Fill Up’ as another way to find the final Thursday of the month. To do this, we will still need the helper columns we have calculated, being ‘**End of Month**‘, ‘**Days to EOM**‘, ‘**Final Week Flag**‘, ‘**Day of Week**‘, ‘**Final Thursday Flag**‘:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-138-1.jpg)

Therefore, we will figure out the ‘**Final Thursday**‘ and leave blanks for days that are not the final Thursday of the month:

**Final Thursday = IF(Sales\[Final Thursday Flag\]=1, Sales\[Date\], BLANK())**

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-121-1.jpg)

Next, we will try filling up by combining the **[CALCULATE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-calculate)
**, **MIN**, **[FILTER](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-filter-function)
** and **[EARLIER](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-earlier-function)
** functions:

**Final Thursday Fill Up = CALCULATE(MIN(Sales\[Final Thursday\]), FILTER(Sales, \[Date\]>EARLIER(Sales\[Date\])))**

![](https://sumproduct.com/wp-content/uploads/2025/05/e00c9a68b449e54559ecbf52ded48bf3-3.jpg)

We notice that all the blank ‘**Final Thursday**‘ cells have been filled up, for example, in January 2016, the blank cells prior to 28/01/2016 are filled with 28/01/2016. However, at the 28/01/2016 point, it is filled with the final Thursday of February 2016, which is 25/02/2016. One way to fix this is to nest the combined functions in the **IF** function to get the ‘**Reporting End of Month**‘:

**\=IF(ISBLANK(Sales\[Final Thursday\]), CALCULATE(MIN(Sales\[Final Thursday\]), FILTER(Sales, \[Date\]>EARLIER(Sales\[Date\]))), Sales\[Final Thursday\])**

![](<Base64-Image-Removed>)

The logic comparison from the last blog takes the calendar end of month as the reporting end of month, meanwhile, using this ‘Fill Up’ method, we are able to get the reporting end of month day as the particular final Thursday of that month.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-2/#0)

[](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-2/#0 "close")

top