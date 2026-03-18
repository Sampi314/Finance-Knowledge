# Power Pivot Principles: Doing More with CALCULATE

**Source:** https://sumproduct.com/blog/power-pivot-principles-doing-more-with-calculate/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Doing More with CALCULATE

*   May 28, 2018

Power Pivot Principles: Doing More with CALCULATE
=================================================

Power Pivot Principles: Doing More with CALCULATE
=================================================

29 May 2018

_Welcome back to our Power Pivot blog. Today we discuss how to do more with the CALCULATE function._

In Power Pivot we can use the **CALCULATE** function to filter our total sales amount by the Product Type, Weeks, or Months. You can read more about it [here](https://www.sumproduct.com/)
. That blog just covered a single criterion, so let’s extend it – what if we have two criteria that we wish to filter by instead?

In our data [here](https://sumproduct.com/assets/blog-pictures/2018/power-pivot/05-may/power-pivot-calculate-with-or--example-20-v1.00.xlsx)
, we have four **PromotionKey** types: 1, 2, 13, 14. Promotion keys 2 and 14 represent refunds. The aim is to ascertain the total amount of refunds.

The solution is simple:

![](<Base64-Image-Removed>)

We simply add two formulas together. However, in another subtly different scenario, what if we only want to sum the refunds if it is classified as promotion key 2 or 14? We could use the **OR** function:

![](<Base64-Image-Removed>)

This works like the Excel version of the function. However, there is an alternative which has no Excel equivalent – the **OR** operator:

![](<Base64-Image-Removed>)

The **OR** operator is two straight lines ‘**||**‘, (you get this by holding down the **SHIFT** key and pressing the Backslash ‘‘ key twice).

That’s it for this week, stay tuned to our [blog](https://www.sumproduct.com/blog)
 for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-doing-more-with-calculate/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-doing-more-with-calculate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-doing-more-with-calculate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-doing-more-with-calculate/#0)

[](https://sumproduct.com/blog/power-pivot-principles-doing-more-with-calculate/#0 "close")

top