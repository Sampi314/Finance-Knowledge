# Power Pivot Principles: Introducing the DATEADD Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-dateadd-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the DATEADD Function

*   November 19, 2018

Power Pivot Principles: Introducing the DATEADD Function
========================================================

Power Pivot Principles: Introducing the DATEADD Function
========================================================

20 November 2018

_Welcome back to our Power Pivot blog. Today, we introduce the DATEADD function._

The **DATEADD** function is a time intelligence function just like the **[TOTALYTD](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-totalytd-function)
**and **[DATESYTD](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-datesytd-function)
**functions. They all require a calendar table with strict ascending and contiguous dates with no gaps (read more about calendar tables and contiguous dates [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-importance-of-contiguous-dates)
).

The syntax of this function is:

**DATEADD(dates, number\_of\_intervals, interval)**

The **DATEADD** function returns the table of column of dates that is shifted either forward or backwards in time specified by the **number\_of\_intervals**.

To illustrate, let’s create a simple measure with the **DATEADD** function:

![](<Base64-Image-Removed>)

The first parameter we have to specify is the **dates** argument; in this case, we shall use our contiguous date table ‘Date Table'\[Dates\].

The next parameter is the **number\_of\_intervals**. This can be any integer which Power Pivot will use to add or subtract the from the dates. In our example we use ‘1’.

The final parameter to define is the **interval**. We can specify the **interval** to be **YEAR**, **QUARTER**, **MONTH** or **DAY**. In this case, we are looking for the sales one year ago so we shall use **YEAR**.

Upon checking the formula Power Pivot returns with ‘no errors in formula’. However, after clicking ‘OK’ we receive this error:

![](<Base64-Image-Removed>)

This is because we have not specified what value we want Power Pivot to calculate. Including ‘**CALCULATE(\[Sales\],**‘ (with an additional closed bracket at the end) to our formula should suffice:

![](<Base64-Image-Removed>)

As long as the dates are contiguous, our measure should work fine now:

![](<Base64-Image-Removed>)

Hang on, it seems that our measure is returning with the sales one year in the future not one year ago. Another slight modification to our measure should address this:

![](<Base64-Image-Removed>)

Note, if we wish for **DATEADD** to return with the sales amounts from the past we have to use a negative integer and a positive integer for sales amounts in the future.

![](<Base64-Image-Removed>)

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-dateadd-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-dateadd-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-dateadd-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-dateadd-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-dateadd-function/#0 "close")

top