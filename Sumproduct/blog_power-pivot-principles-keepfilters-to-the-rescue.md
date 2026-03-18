# Power Pivot Principles: KEEPFILTERS to the Rescue

**Source:** https://sumproduct.com/blog/power-pivot-principles-keepfilters-to-the-rescue/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: KEEPFILTERS to the Rescue

*   January 14, 2019

Power Pivot Principles: KEEPFILTERS to the Rescue
=================================================

Power Pivot Principles: KEEPFILTERS to the Rescue
=================================================

15 January 2019

_Welcome back to our Power Pivot blog. Today, we discuss an alternate way to keep the CALCULATE function from misbehaving._

Last week, we looked at using the **CALCULATE**, **FILTER** and **VALUES** functions to stop measures from overriding the row context values (you can read about it [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-when-the-calculate-function-misbehaves)
).

Here is how we used the three functions last week:

![](<Base64-Image-Removed>)

There is an alternative way to avoid the measure from overriding row context values. This can be achieved by employing the **KEEPFILTERS** function. We can use the **KEEPFILTERS** function directly after the **CALCULATE** function, as in this following example:

\=CALCULATE(

\[Sales\],

KEEPFILTERS( ‘Product SubCategory'\[ProductCategoryKey\] = 2 )

)

![](<Base64-Image-Removed>)

As you can see (in the picture below) we have achieved the same result in fewer steps, which is usually good when coding!

![](<Base64-Image-Removed>)

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-keepfilters-to-the-rescue/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-keepfilters-to-the-rescue/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-keepfilters-to-the-rescue/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-keepfilters-to-the-rescue/#0)

[](https://sumproduct.com/blog/power-pivot-principles-keepfilters-to-the-rescue/#0 "close")

top