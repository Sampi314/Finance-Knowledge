# Power Pivot Principles: Tables, Fields and Measures

**Source:** https://sumproduct.com/blog/power-pivot-principles-tables-fields-and-measures/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Tables, Fields and Measures

*   April 2, 2018

Power Pivot Principles: Tables, Fields and Measures
===================================================

Power Pivot Principles: Tables, Fields and Measures
===================================================

3 April 2018

_Welcome back to our Power Pivot blog series, today let’s go over the syntax between a table, a field, and a measure._

Before we go into **D**ata **A**nalytics E**X**pressions (**DAX**), we first have to learn how to refer to a Table, a Field and a Measure in DAX.

Imagine that we have a table such as the following:

![](<Base64-Image-Removed>)

In DAX:

*   If the **table** above is called ‘Sales’ we would refer to it as ‘Sales’ in DAX
*   If we want to refer to any of the **fields** in this table, ‘Sales ID’ or ‘Sales Amount’, we would have to write it as ‘Sales\[Sales ID\]’, or ‘Sales\[Sales Amount\]’
*   If we create a **measure** (_i.e._ a formula which manipulates the aggregated summaries of one or more fields or other calculations) to calculate tax and call it ‘Sales Tax’, we will refer to it as \[SalesTax\] with square brackets around it. The reference to a table is not required (and would be confusing) as calculations based upon fields are portable (_i.e._ they may be transferred from one table to another).

This may be summarised as follows:

![](<Base64-Image-Removed>)

That’s it for this week. Stay tuned for our next post on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-tables-fields-and-measures/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-tables-fields-and-measures/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-tables-fields-and-measures/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-tables-fields-and-measures/#0)

[](https://sumproduct.com/blog/power-pivot-principles-tables-fields-and-measures/#0 "close")

top