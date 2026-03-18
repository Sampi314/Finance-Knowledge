# Power Pivot Principles: Measure Creation in Practice

**Source:** https://sumproduct.com/blog/power-pivot-principles-measure-creation-in-practice/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Measure Creation in Practice

*   April 30, 2018

Power Pivot Principles: Measure Creation in Practice
====================================================

Power Pivot Principles: Measure Creation in Practice
====================================================

1 May 2018

_Welcome back to our Power Pivot blog series. Today we discuss proper practices we should adopt when creating measures._

This blog builds on what was mentioned in the previous blog [Power Pivot Principles – Measures and Aggregation](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-tables-fields-and-measures)
.

Before we create more complicated measures, it is good practice to convert each field that we are going to use into a measure. There’s a good reason to do this, even if it seems like an unnecessary chore. In Excel, if you add / remove rows or columns Excel’s formulae will update automatically. However, if you change a field name in Power Pivot, the dependent measures will not update and will not calculate as a consequence.

Therefore, in order to avoid changing many measures when a field is renamed, it is simpler to create an aggregate measure of that field first and then have all further measures refer to that intermediate measure. Therefore, this will save us a lot of time if we turn fields into ‘simple’ measures first.

Converting fields into measures first yields two benefits:

1.  It saves time in the long run; we avoid having to use an aggregation function each time we reference the field
2.  It simplifies the formula when creating complex measures.

Let’s create a measure for the ‘Product Cost’. In this example, we have completed the measure dialog box with the following details:

![](<Base64-Image-Removed>)

Next up, we’ll construct a similar ‘Sales’ measure:

![](<Base64-Image-Removed>)

We can now move on to modify the ‘Profit’ measure. From the ‘Measures’ drop-down menu, select ‘Manage Measures…’:

![](<Base64-Image-Removed>)

The ‘Manage Measures’ dialog box appears displaying all measures along with their formulae. Select the Profit measure and then press ‘Edit’ button:

![](<Base64-Image-Removed>)

The measures dialog box appears allowing us to edit the formula.

![](<Base64-Image-Removed>)

We can now condense the formula down to:

![](<Base64-Image-Removed>)

See how complicate the new formula is? Simple!

That’s it for this week, stay tuned to our blog page for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-measure-creation-in-practice/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-measure-creation-in-practice/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-measure-creation-in-practice/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-measure-creation-in-practice/#0)

[](https://sumproduct.com/blog/power-pivot-principles-measure-creation-in-practice/#0 "close")

top