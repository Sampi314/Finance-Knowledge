# Power Pivot Principles: Introducing ALL

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-all/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing ALL

*   June 11, 2018

Power Pivot Principles: Introducing ALL
=======================================

Power Pivot Principles: Introducing ALL
=======================================

12 June 2018

_Welcome back to our Power Pivot blog. Today we discuss how to use the ALL function in DAX._

In Power Pivot, the **ALL** function returns all of the records in a table, or all of the values in a column ignoring any filters that might have been applied for the filed under scrutiny. This function is useful for clearing filters and creating calculations on all rows in a given table.

This blog will expand upon the **CALCULATE** function, first introduced in [t](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-calculate)
[his blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-calculate)
. Let’s take it further. Here, I am going to create a simple ‘**All Months Sales**‘ measure:

**\=CALCULATE(\[Sales\],ALL(Sales\[OrderDate (Month)\]))**

![](https://sumproduct.com/wp-content/uploads/2025/05/72026c78bcbe9ce5570498c34dbccc5c.jpg)

Our resulting PivotTable will look something like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/c73eefccba9c8965d7ffa3043c292e77.jpg)

What next? It sort of stands out doesn’t it? From the **CALCULATE** and **ALL** functions, I can now combine them to create a percentage sales measure which will reflect the inherent seasonality (well, for the last six months anyway):

![](https://sumproduct.com/wp-content/uploads/2025/05/cc9dde21a1ef5b625cc53deeb16ffdfe.jpg)

Remember to include an error trap (you can read more about error traps in this [blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-drawing-a-blank-on-error-traps)
).

Our PivotTable should look something like this now:

![](https://sumproduct.com/wp-content/uploads/2025/05/467560ad26e04e1a5239f3e75741910d.jpg)

Not only is this percentage calculated from 2014’s total sales, this measure will _always_ be a percentage. This is subtly different from a normal PivotTable, where percentages may be viewed by changing the Value Field Settings rather than an absolute (dollar) amount. Since this measure is based on a month’s sales divided by all months’ sales, this figure will remain a value between zero and one no matter how it is formatted or displayed.

That’s it for this week, stay tuned to our [blog](https://www.sumproduct.com/blog)
 for more on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-all/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-all/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-all/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-all/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-all/#0 "close")

top