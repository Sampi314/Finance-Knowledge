# Power Pivot Principles: Creating a Disconnected Table for GST

**Source:** https://sumproduct.com/blog/power-pivot-principles-creating-a-disconnected-table-for-gst/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Creating a Disconnected Table for GST

*   February 22, 2021

Power Pivot Principles: Creating a Disconnected Table for GST
=============================================================

Power Pivot Principles: Creating a Disconnected Table for GST
=============================================================

23 February 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll continue last week’s example, and build on the mistake of not including a Goods & Services Tax (GST) on the Sales transactions. For this week, we will create a disconnected table for GST._

Let me remind you that we amended the **Sales** measure [last week](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-amendments-made-easily)
 by changing the measure as shown below.

**\=CALCULATE(-SUM(Budget\[Amount\])****/1.1****, COA\[Group\] = “P”)**

![](<Base64-Image-Removed>)

When I look at my measure, it makes me realise how confident I am about the indirect Goods & Services Tax (GST) rate always staying at 10%. However, that is not how tax and fiscal budgets work. To be able to accommodate for the volatility in GST, I will [create a disconnected table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-variables-and-disconnected-tables-in-power-pivot)
 by constructing a table for a range of GST percentages and add this to the Data Model.

![](<Base64-Image-Removed>)

To make it more presentable, I will add a new column by using the **FORMAT** function and rename it to **GST Percentage** by using the formula

**\=FORMAT(GST\[Percentage\],”0.00%”)**

The GST table will now look like this:

![](<Base64-Image-Removed>)

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-creating-a-disconnected-table-for-gst/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-creating-a-disconnected-table-for-gst/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-creating-a-disconnected-table-for-gst/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-creating-a-disconnected-table-for-gst/#0)

[](https://sumproduct.com/blog/power-pivot-principles-creating-a-disconnected-table-for-gst/#0 "close")

top