# Power Pivot Principles: Introducing the Function FIRSTNONBLANK

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-firstnonblank/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the Function FIRSTNONBLANK

*   April 6, 2020

Power Pivot Principles: Introducing the Function FIRSTNONBLANK
==============================================================

Power Pivot Principles: Introducing the Function FIRSTNONBLANK
==============================================================

7 April 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a new DAX function, FIRSTNONBLANK._

The DAX function **FIRSTNONBLANK** returns the first value in the column filtered by the current context, where the expression is not blank. It is a useful function to extract the first non-blank value and can be used as a filter for other calculations.

It has following syntax to operate:

**FIRSTNONBLANK(column, expression)**

where:

· **column** represents a column expression

· **expression** is an expression evaluated for blanks for each value of column.

Let’s look at one simple example. Suppose we have a following data table:

![](<Base64-Image-Removed>)

After we have loaded the table into Power Pivot and created a PivotTable, we can populate it with some measures:

![](<Base64-Image-Removed>)

**\=SUM(Sales\[Amount\])**

This DAX expression calculates the total sales.

![](<Base64-Image-Removed>)

**\=FIRSTNONBLANK(Sales\[Category\],\[Total Sales\])**

We export the result into a PivotTable and the result would be:

![](<Base64-Image-Removed>)

We can see that the measure is in fact returning the category two (2), which is what we would expect.

Now, what if we want a measure that will retrieve the value of the first sale? Following the logic of the previous measure we can write:

![](<Base64-Image-Removed>)

**\=FIRSTNONBLANK(Sales\[Amount\],\[Total Sales\])**

The result would be:

![](<Base64-Image-Removed>)

We can see that the sales amount returning five (5), which is correct according to the data table.

  
  
That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-firstnonblank/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-firstnonblank/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-firstnonblank/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-firstnonblank/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-firstnonblank/#0 "close")

top