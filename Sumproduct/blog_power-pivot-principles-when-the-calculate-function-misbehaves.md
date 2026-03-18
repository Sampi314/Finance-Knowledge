# Power Pivot Principles: When the CALCULATE Function Misbehaves.

**Source:** https://sumproduct.com/blog/power-pivot-principles-when-the-calculate-function-misbehaves/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: When the CALCULATE Function Misbehaves.

*   January 7, 2019

Power Pivot Principles: When the CALCULATE Function Misbehaves.
===============================================================

Power Pivot Principles: When the CALCULATE Function Misbehaves.
===============================================================

8 January 2019

_Welcome back to our Power Pivot blog. Today, we discuss how to stop the CALCULATE function from overwriting row filters._

Let’s say we wish to create a measure to calculate the total sales of all products classified as **Product Category 2**.

Let’s try this with the **CALCULATE** function:

\=**CALCULATE**(

\[Sales\],

‘Product SubCategory'\[ProductCategoryKey\] = 2

)

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-506.jpg)

The **Only Category 2** measure yields:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-525.jpg)

In this case the **CALCULATE** measure overrides the row context in cells **C4:C7** to be **ProductCategoryKey** = 2 instead of their respective values (_i.e._ 1, 2, 3 or 4).

Let’s try adding the **VALUES** function into a measure:

\=**CALCULATE**(

\[Sales\],

**FILTER**(

**VALUES**( ‘Product SubCategory'\[ProductCategoryKey\]),

‘Product SubCategory'\[ProductCategoryKey\] = 2

)

)

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-494.jpg)

This measure yields:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-453.jpg)

Voilà! Using the **VALUES** function we have managed to alter the **CALCULATE** function’s behaviour and stop it from overriding the row context values. Our data no longer has the same values for each **Product Category**!

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-when-the-calculate-function-misbehaves/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-when-the-calculate-function-misbehaves/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-when-the-calculate-function-misbehaves/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-when-the-calculate-function-misbehaves/#0)

[](https://sumproduct.com/blog/power-pivot-principles-when-the-calculate-function-misbehaves/#0 "close")

top