# Power Pivot Principles: Calculating Cumulative Totals with Variables

**Source:** https://sumproduct.com/blog/power-pivot-principles-calculating-cumulative-totals-with-variables/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Calculating Cumulative Totals with Variables

*   September 16, 2019

Power Pivot Principles: Calculating Cumulative Totals with Variables
====================================================================

Power Pivot Principles: Calculating Cumulative Totals with Variables
====================================================================

17 September 2019

_Welcome back to our Power Pivot blog. Today, we look at an alternative method of calculating cumulative sums without using the EARLIER function._

Last week, we looked at the **EARLIER** function and used it to create a cumulative column. You can read more on the **EARLIER** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-earlier-function)
. As a refresher, we used the following measure to calculate the cumulative total:

\=CALCULATE**(**

                SUM(SaleDataDates\[Total Sales\]),

                FILTER(‘SaleDataDates’,

                SaleDataDates\[Date\] <= EARLIER(SaleDataDates\[Date\])

                )

**)**

![](<Base64-Image-Removed>)

The alternative method of calculating a cumulative total involves the use of variables. If you are wondering what variables in **DAX** are, you can read about them [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-variables-in-dax)
.

When writing the new measure, we begin by defining a variable:

\= 

VAR SaleDate = SaleDataDates\[Date\]

Evaluating this variable alone will result in this calculated column:

![](<Base64-Image-Removed>)

As you can see the variable evaluates to the current row’s Sale date. This isthe same evaluation result as the **EARLIER** function in:

EARLIER(SaleDataDates\[Date\])

The next step is to replace the **EARLIER** function segment with the variable:

\=

VAR SaleDate = SaleDataJul1\[Date\]

Return

CALCULATE(

                SUM(\[Total Sales\]),

                FILTER(‘SaleDataJul1’,

                SaleDataJul1\[Date\] <= SaleDate

                ) 

)

The logic of the measure remains the same as the measure with the **EARLIER** function, and we have been able to replicate the results without the **EARLIER** function:

![](<Base64-Image-Removed>)

Wonder if this method works with numeric columns as well?

![](<Base64-Image-Removed>)

Yes, it does! There you have it: an alternative method of calculating cumulative totals for different columns.

That’s it for this week, come back next week for more Power Pivot. Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-calculating-cumulative-totals-with-variables/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-calculating-cumulative-totals-with-variables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-calculating-cumulative-totals-with-variables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-calculating-cumulative-totals-with-variables/#0)

[](https://sumproduct.com/blog/power-pivot-principles-calculating-cumulative-totals-with-variables/#0 "close")

top