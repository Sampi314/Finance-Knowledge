# Power Pivot Principles: How to Create the CAGR Measure, Part 2

**Source:** https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-2/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: How to Create the CAGR Measure, Part 2

*   March 18, 2019

Power Pivot Principles: How to Create the CAGR Measure, Part 2
==============================================================

Power Pivot Principles: How to Create the CAGR Measure, Part 2
==============================================================

19 March 2019

_Welcome back to our Power Pivot blog. We continue on our CAGR series: today, we shall look into fixing our measures so we can calculate CAGR._

Last week we attempted to calculate CAGR. However, we ran into a couple of issues where our **\[First Year\]** and **\[Last Year\]** measures did not return with our intended results.

As a quick recap, our measures returned with the following results:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-468.jpg)

The first and last year measures return with the row’s first and last year. This is because these measures are subject to the PivotTable row filters. We are going to have to tweak the measures for them to consider the entire range of data, despite these row filters.

In this case we will have to use the **ALL** function. You can read more about the **ALL** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-all)
.

We have to modify the first and last year measures. The **\[First Year\]** measure should be revised as follows:

\=CALCULATE(

MIN(

‘Calendar'\[Year\]),

ALL(

‘Calendar’

)

)

![](<Base64-Image-Removed>)

Similarly, the **\[Last Year\]** measure should be adapted too:

\=CALCULATE(

MAX(

‘Calendar'\[Year\]),

ALL(

‘Calendar’

)

)

![](<Base64-Image-Removed>)

Our **\[CAGR\]** measure now calculates on the PivotTable:

![](<Base64-Image-Removed>)

Great, we finally have a working CAGR measure! But the measure only calculates the CAGR for the last year, what if we want the progressive CAGR for each year? Well, that’s the subject of next week’s article…

Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-2/#0)

[](https://sumproduct.com/blog/power-pivot-principles-how-to-create-the-cagr-measure-part-2/#0 "close")

top