# Power Pivot Principles: Calculated Field vs. Measure

**Source:** https://sumproduct.com/blog/power-pivot-principles-calculated-field-vs-measure/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Calculated Field vs. Measure

*   June 7, 2021

Power Pivot Principles: Calculated Field vs. Measure
====================================================

Power Pivot Principles: Calculated Field vs. Measure
====================================================

8 June 2021

_Welcome back to the Power Pivot Principles blog. This week, we consider the differences between creating a calculated field and a calculated measure._

Let’s revisit our dataset from [last week](https://www.sumproduct.com/blog/article/power-pivot-principles/power-pivot-principles-initial-measures-a-pro-tip)
:

![](<Base64-Image-Removed>)

Similar to last week, I want to calculate **Gross Profit**. Last week, we did this by creating two measures:

**Total Sales := SUM(Example\[Sales\])**

**Total Costs := SUM(Example\[Costs\])**

**Gross Profit := \[Total Sales\] – \[Total Costs\]**

Alternatively, I could just create a calculated field in the source Table, _viz._

![](<Base64-Image-Removed>)

Here, I have just added a column and subtracted **Costs** from **Sales**. Simple.

But which is the better way?

The difference between the two represents the context of **evaluation**. A measure is evaluated in aggregate in the context of the cell evaluated in a report, PivotTable or DAX query, whereas a calculated column is computed at the row level within the table it belongs to.

In general, measures are used to calculate aggregates, such as the sum or average of a column. Moreover, measures are calculated at the time the query is displayed, which means that they aren’t stored in your database. They are simply executed and processed at the time of your request (_e.g._ when you place them in a PivotTable). Since measures are not stored in memory, they are generally faster, although it is important to recognise the trade-off between using in-memory storage or processing power in an instance where either a measure or a calculated field (column) could be used.

As usual, it depends, but it is a numbers game. If my dataset contained millions of rows, the measure would win hands down.

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-calculated-field-vs-measure/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-calculated-field-vs-measure/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-calculated-field-vs-measure/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-calculated-field-vs-measure/#0)

[](https://sumproduct.com/blog/power-pivot-principles-calculated-field-vs-measure/#0 "close")

top