# Power Pivot Principles: DATEADD Comparison

**Source:** https://sumproduct.com/blog/power-pivot-principles-dateadd-comparison/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: DATEADD Comparison

*   April 26, 2021

Power Pivot Principles: DATEADD Comparison
==========================================

Power Pivot Principles: DATEADD Comparison
==========================================

27 April 2021

_Welcome back to the Power Pivot Principles blog. This week, we are going to work on an alternate approach from last week to compare monthly data._

While conducting my analysis for building the financial performance report of company XYZ, I decided to review the monthly changes in some of the line items. Out of the options I had in mind, let me show you the one that is my favourite.

Let me use monthly **Sales** as an example by pulling it in a table:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-211.jpg)

Now to analyse month on month performance, let us compare it to the preceding month. To calculate this, I will use the function **DATEADD**. I believe it is one of the most versatile time series functions. The syntax is as follows:

**DATEADD(dates, number\_of\_intervals, interval)**

I can simply use this to and create the following measure:

**\=CALCULATE(\[Sales (including GST)\], DATEADD(‘Calendar'\[Date\], -1, MONTH))**

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-270.jpg)

Notice how I use the **CALCULATE** function: using **DATEADD** alone would serve no purpose. Now I simply pull this measure in a field to generate the following results:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-215.jpg)

Yes, it was as simple as that! Now we can easily compare each month’s sale to its preceding month.

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-dateadd-comparison/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-dateadd-comparison/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-dateadd-comparison/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-dateadd-comparison/#0)

[](https://sumproduct.com/blog/power-pivot-principles-dateadd-comparison/#0 "close")

top