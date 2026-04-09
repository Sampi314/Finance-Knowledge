# Power Pivot Principles: Annual / Monthly Comparisons

**Source:** https://sumproduct.com/blog/power-pivot-principles-annual-monthly-comparisons/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Annual / Monthly Comparisons

*   April 19, 2021

Power Pivot Principles: Annual / Monthly Comparisons
====================================================

Power Pivot Principles: Annual / Monthly Comparisons
====================================================

20 April 2021

_Welcome back to the Power Pivot Principles blog. This week, I will be comparing my Actuals data for different years._

Let us say I received a request from my manager asking for a financial performance report of the company. As an ‘excellent’ analyst, I decided to compare Charts of Accounts for two years to show the relative change in performance monthly.

From previous blogs, you will note I have been running my financial ‘analyses’ for the past few weeks already. Let me quickly pull in my **Actuals** data by selecting the following fields:

![](<Base64-Image-Removed>)

My summary table looks like this:

![](<Base64-Image-Removed>)

Wait, this is not right! I cannot use this summary table to compare between two different years. I am running late, so I will simply [create a Calendar table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-calendar-table)
, _viz._

![](<Base64-Image-Removed>)

In the diagram view, I will create a relationship between **Actuals** and **Calendar** query:

![](<Base64-Image-Removed>)

Now that I am prepared, I will replace the ‘Month’ field with the ‘Date Hierarchy’ in my summary table:

![](<Base64-Image-Removed>)

My summary table looks like the following:

![](<Base64-Image-Removed>)

All I must do now is expand both the years, _viz._

![](<Base64-Image-Removed>)

There it is! I can finally begin writing my report. I have my numbers right here to begin with.

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-annual-monthly-comparisons/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-annual-monthly-comparisons/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-annual-monthly-comparisons/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-annual-monthly-comparisons/#0)

[](https://sumproduct.com/blog/power-pivot-principles-annual-monthly-comparisons/#0 "close")

top