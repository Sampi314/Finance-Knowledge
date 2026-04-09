# Power Pivot Principles: PREVIOUSMONTH Comparison

**Source:** https://sumproduct.com/blog/power-pivot-principles-previousmonth-comparison/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: PREVIOUSMONTH Comparison

*   May 10, 2021

Power Pivot Principles: PREVIOUSMONTH Comparison
================================================

Power Pivot Principles: PREVIOUSMONTH Comparison
================================================

11 May 2021

_Welcome back to the Power Pivot Principles blog. This week, we are going to compare monthly data using yet another approach._

If you have read my blogs on [**DATEADD**](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-dateadd-comparison)
and **[PARALLELPERIOD](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-parallelperiod-comparison)
**, you must be aware that I have been outlining options to look at monthly changes in **Sales**. This week, I am here to offer you another method of performing the same analysis. Let’s pull the monthly **Sales** data in a table to start the process once again:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-201.jpg)

To analyse month on month performance, I will compare results with the preceding month, using the **PREVIOUSMONTH** function. The syntax is as follows:

**PREVIOUSMONTH(dates)**

I can simply use this and create the following measure:

**\=CALCULATE(\[Sales (including GST)\],PREVIOUSMONTH(‘Calendar'\[Date\]))**

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-260.jpg)

Now, I simply pull this measure into my PivotTable to generate the following results:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-207.jpg)

Now that’s the third option after generating the same results using **DATEADD** and **PARALLELPERIOD**. It’s up to you to choose the one you prefer. Spoiler alert: I will be showing you another alternate next week for the same analysis. I bet you can’t wait…

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-previousmonth-comparison/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-previousmonth-comparison/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-previousmonth-comparison/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-previousmonth-comparison/#0)

[](https://sumproduct.com/blog/power-pivot-principles-previousmonth-comparison/#0 "close")

top