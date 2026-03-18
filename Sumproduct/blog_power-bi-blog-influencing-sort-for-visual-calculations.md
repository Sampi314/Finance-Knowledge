# Power BI Blog: Influencing Sort for Visual Calculations

**Source:** https://sumproduct.com/blog/power-bi-blog-influencing-sort-for-visual-calculations/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Influencing Sort for Visual Calculations

*   September 18, 2025

Power BI Blog: Influencing Sort for Visual Calculations
=======================================================

_Welcome back to this week’s edition of the Power BI blog series._  _This week, we look at sorting visual calculations._

Microsoft has added a highly requested feature to visual calculations.  Most visual calculations exclusive functions now have an optional **ORDERBY** parameter, using the **ORDERBY** function.  Previously available in window functions like **INDEX**, **OFFSET** and **WINDOW**, this option is now included in functions such as **RUNNINGSUM**, **MOVINGAVERAGE**, **PREVIOUS** and more.

This improvement increases the flexibility and capability of visual calculations, allowing for advanced computations based on data sorting.  For instance, you can now use **RUNNINGSUM** for Pareto analysis by sorting data in descending order.

To visualise your top-selling product colours, you can use a chart as demonstrated in the example:

![](<Base64-Image-Removed>)

This chart is sorted by sales amount in descending order, so the colours are not arranged alphabetically.  To include the Pareto analysis, first calculate the percentage of the grand total sales that each colour represents, using the provided visual calculation template ‘Percent of grand total’:

> **Percent of grand total = DIVIDE(\[Sales Amount\], COLLAPSEALL (\[Sales Amount\], ROWS))**

Then, include the Pareto line by employing another visual calculation using the ‘Running sum’ template:

> **Pareto = RUNNINGSUM(\[Percent of grand total\])**

However, this issue arises because the colours are not organised alphabetically in the visual representation, only within the matrix.

![](<Base64-Image-Removed>)

Creating a true Pareto line requires a more complex **DAX** statement, for example, using **SUMX** and **WINDOW**:

> **Pareto using WINDOW =**
> 
> **SUMX(**
> 
> **WINDOW(0, ABS, 0, REL, ROWS, ORDERBY(\[Sales Amount\], DESC )),**
> 
> **\[Percent of grand total\]**
> 
> **)**

Whilst this method is functional, utilising **RUNNINGSUM** with the new **ORDERBY** parameter offers greater convenience.  It significantly simplifies the process of adding the Pareto line:

> **Easy Pareto = RUNNINGSUM(\[Percent of grand total\], ORDERBY(\[Sales Amount\], DESC))**

Following a brief application of visual level formatting, your Pareto analysis will then be complete:

![](<Base64-Image-Removed>)

This is an example of how this new parameter enables more advanced and flexible calculations using visual methods.  Have fun exploring!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/training)
 .  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
 . 

*   [Log in](https://sumproduct.com/blog/power-bi-blog-influencing-sort-for-visual-calculations/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-influencing-sort-for-visual-calculations/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-influencing-sort-for-visual-calculations/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-influencing-sort-for-visual-calculations/#0)

[](https://sumproduct.com/blog/power-bi-blog-influencing-sort-for-visual-calculations/#0 "close")

top