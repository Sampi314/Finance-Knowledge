# Power Pivot Principles: Introducing the SUMX function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-sumx-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the SUMX function

*   February 18, 2019

Power Pivot Principles: Introducing the SUMX function
=====================================================

Power Pivot Principles: Introducing the SUMX function
=====================================================

19 February 2019

_Welcome back to our Power Pivot blog. Today, we discuss the **SUMX** function._

Last week we showed how the **SUM** function did not properly calculate the total revenue from this data table:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-485.jpg)

As a refresher the **SUM** function calculated a total revenue of $1,330,880.76 (we were surprised too, we didn’t make that much money!):

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-500.jpg)

Upon closer inspection the results of the **SUM** function do not make sense, $72,563.58 + $94,124.16 + $279,326.94 does not equal $1,330,880.76. What on earth is going on?

It appears that the **SUM** function is aggregating column values based on the row labels (years, grand total) and then multiplying the Sum of # Units Sold with the Sum of Price Per Unit. This approach will not correctly calculate the total revenue. We will need a function that iterates the calculation row by row, cue the **SUMX** function.

The **SUMX** function requires the following syntax to operate:

**SUMX(<table>, <expression>)**

We can use the **SUMX** function to create the following measure:

\=SUMX(

‘Unit Price and Volume Sold’,

‘Unit Price and Volume Sold'\[# of Units Sold\] \* ‘Unit Price and Volume Sold'\[Price Per Unit\]

)

![](<Base64-Image-Removed>)

The resulting PivotTable yields:

![](<Base64-Image-Removed>)

Just to check here’s our quick and dirty check from the last blog:

![](<Base64-Image-Removed>)

We can see that the **SUMX** formula is correctly calculating the total revenue. This is because it is calculating the total revenue for each row item individually ($2.99 \* 474 = $1,417.26, $2.95 \* 457 = $1,348.15, etc…), unlike the **SUM** function. Therefore, we should use the **SUMX** function when we need Power Pivot to perform a calculation that needs to be iterated row by row.

For those of you thinking, why don’t we just use a calculated column? Yes, you can, but we have to be wary of [resource management](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-resource-management-with-calculated-columns)
.

Until then happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-sumx-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-sumx-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-sumx-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-sumx-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-sumx-function/#0 "close")

top