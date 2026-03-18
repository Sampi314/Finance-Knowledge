# Power Pivot Principles: Working with Averages – Part 1

**Source:** https://sumproduct.com/blog/power-pivot-principles-working-with-averages-part-1/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Working with Averages – Part 1

*   October 26, 2020

Power Pivot Principles: Working with Averages – Part 1
======================================================

Power Pivot Principles: Working with Averages – Part 1
======================================================

27 October 2020

_Welcome back to the Power Pivot Principles blog. This week, we will discuss working with averages in DAX._

The **AVERAGE** function returns the average (arithmetic mean) of all the numbers in a column:

**AVERAGE(column).**

The **AVERAGEA** function does a similar thing, and is distinguished by its ability to handle text and non-numeric values:

**AVERAGEA(column).**

For example, consider we have a **Sales** table with **Date** and **Sales** by date as below (obviously, there are some “unusual” cell values in the **Sales** column):

![](<Base64-Image-Removed>)

Now, we take July 2017 as an example to calculate the average in Excel. In the range **B2:B32**, there are blank cells and cells with text. We illustrate the **[\>AVERAGE](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-average-function)
** and **[AVERAGEA](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-averagea-function)
** functions, as below. We notice that the **AVERAGE** function does not take blank cells and those containing text into its computation. Meanwhile, the **AVERAGEA** only excludes blank cells.

![](<Base64-Image-Removed>)

If we change the blank cells to formula-driven cells (=””), the **AVERAGEA** function will take all the cells into account:

![](<Base64-Image-Removed>)

We load this **Sales** table into the Power Pivot Data Model and create two measures:

**Sales\_AVERAGE:=AVERAGE(‘Sales'\[Sales\])**

**Sales\_AVERAGEA:=AVERAGEA(‘Sales'\[Sales\])**

The **Sales\_AVERAGE** measure will give us an error. This is because the Data Type of the **Sales** column is now Text, and the **AVERAGE** function cannot handle text. Meanwhile, the **AVERAGEA** counts everything and return a zero (0).

![](<Base64-Image-Removed>)

When we try to change the Data Type of the column to ‘Whole Number’, an error appears:

![](<Base64-Image-Removed>)

If we remove all the text cells in the **Sales** column and refresh the Power Pivot Data Model, we can now change the Data Type of the **Sales** column to ‘Whole Number’. Also, the **Sales\_AVERAGE** and **Sales\_AVERAGEA** measures will now provide the same results:

![](<Base64-Image-Removed>)

That is just one thing we need to consider when dealing with averages in DAX…

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-working-with-averages-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-working-with-averages-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-working-with-averages-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-working-with-averages-part-1/#0)

[](https://sumproduct.com/blog/power-pivot-principles-working-with-averages-part-1/#0 "close")

top