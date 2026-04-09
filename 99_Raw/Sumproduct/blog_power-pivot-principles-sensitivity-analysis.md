# Power Pivot Principles: Sensitivity Analysis

**Source:** https://sumproduct.com/blog/power-pivot-principles-sensitivity-analysis/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Sensitivity Analysis

*   March 1, 2021

Power Pivot Principles: Sensitivity Analysis
============================================

Power Pivot Principles: Sensitivity Analysis
============================================

2 March 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll perform a sensitivity analysis for different rates of Goods & Services Tax (GST) on the Sales transactions._

I know I left most of you wondering [last week](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-creating-a-disconnected-table-for-gst)
 about the use of a disconnected table for GST. I know you might have had a busy week, so let’s refresh your memory with a brief recap of last week’s outcome.

![](<Base64-Image-Removed>)

To perform a sensitivity analysis, I start of by creating a measure as shown below:

**\=MAX(GST\[Percentage\])**

![](<Base64-Image-Removed>)

The next step is to create a new **Sales****(including GST)** measure that accommodates for the changes in GST rate:

**\=CALCULATE((-SUM(Budget\[Amount\])/\[GST Rate\]), COA\[Group\] = “P”)**

![](<Base64-Image-Removed>)

Now, let us include the **Sales (including GST)** in our Pivot table.

![](<Base64-Image-Removed>)

We now add the **GST Percentage** as a slicer.

![](<Base64-Image-Removed>)

This is what the slicer looks like:

![](<Base64-Image-Removed>)

In the Slicer tab on the Ribbon, select two columns to make it look more presentable in a single view:

![](<Base64-Image-Removed>)

In the Slicer tab on the Ribbon, select two columns to make it look more presentable in a single view:

![](<Base64-Image-Removed>)

Let’s click on another rate for double checking:

![](<Base64-Image-Removed>)

Our sensitivity analysis is now created. That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-sensitivity-analysis/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-sensitivity-analysis/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-sensitivity-analysis/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-sensitivity-analysis/#0)

[](https://sumproduct.com/blog/power-pivot-principles-sensitivity-analysis/#0 "close")

top