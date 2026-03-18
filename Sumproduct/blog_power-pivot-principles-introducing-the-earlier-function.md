# Power Pivot Principles: Introducing the EARLIER Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-earlier-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the EARLIER Function

*   September 2, 2019

Power Pivot Principles: Introducing the EARLIER Function
========================================================

Power Pivot Principles: Introducing the EARLIER Function
========================================================

3 September 2019

_Welcome back to our Power Pivot blog. Today, we look at the EARLIER function._

We will need to explain several concepts before covering the **EARLIER** function. The first concept we are going to cover is the idea of **Row Context**.

In **DAX**, the **Row Context** is a term that means: “a row by row evaluation”. Essentially, it means that the formula is executed one row at a time. This may return with different results on each row of a table.

Let’s take a look at an example. We are going to use the following data set (the picture below is not exhaustive):

![](<Base64-Image-Removed>)

After loading this data into our data model, we can create the following calculated column:

**\=SaleTbl\[Price\]\*SaleTbl\[Amount Sold\]**

![](<Base64-Image-Removed>)

This would give us the total **Sale Amount**, since we are multiplying the price per product with the amount sold. This single **DAX** formula is calculating a different sale amounts for each row. This is because the **Sale Amount** is being multiplied individually for each product one row at a time.

Simple? Now, we can look at **Nested Row Contexts**. This means that there are multiple Row Contexts, or multiple row by row calculations in each row. Perhaps this is better illustrated in the following example.

Using the same dataset as before we can create the calculated column:

\=RANKX**(**SaleTbl,\[Sale Amount\],,ASC**)**

![](<Base64-Image-Removed>)

The **RANKX** formula has two nested row contexts. It has two steps:

1.  It works out the total **Sale Amount** for each **Product ID**. This is the **outer row context**
2.  It ranks the **Product ID** on the current row verses the entire table based on the total **Sale Amount**. This is the **inner row context**.

Now that we are all on the same page regarding inner and outer row contexts, we can move on to the **EARLIER** function.

The **EARLIER** function uses the following syntax to operate:

**EARLIER (<column>, \[<number>\])**

*   the **<column>** parameter **must** refer to a column that has numeric values or dates
*   the **<number>** parameter is optional, it delineates the number of row contexts to step out of before evaluation. If omitted it will default to 1.

Let’s recreate the **Rank Sales** column, this time with the **EARLIER** function.

\=  
COUNTROWS(

FILTER(SaleTbl,

                \[Sale Amount\] > EARLIER(\[Sale Amount\])

                )

) + 1

![](<Base64-Image-Removed>)

This formula has two nested row contexts:

1.  the first one (inner row context) is in the **FILTER** function where each row of the table is evaluated based on the condition
2.  the second (outer row context) is the **Sale Amount** calculation (**Price \* Amount Sold**).

Another way to think about it is that this formula has two loops: an inner and outer loop. The inner loop is where the **FILTER** function has to evaluate all of the **Sale Amounts** in the table. The outer loop is when the **EARLIER** function instructs the program disregard the inner loop and evaluate the outer loop, defined as **\[Sale Amount\]**, which is the current row’s **Price \* Amount Sold**.

To further step it out, the formula evaluates as follows:

*   the **COUNTROWS** function requires a table input
*   the **FILTER** returns with a table, based on a condition
    *   the **FILTER** function begins by evaluating the first row of the **SaleTbl**, where it evaluates all the **Sale Amount** values for each row, then returns with a table of all the **Sale Amount** values that are greater than **EARLIER(\[Sale Amount\])**
*   the **EARLIER** function instructs the formula to disregard the current row context in the **FILTER** function jump one level up to the ‘outer loop’ where the **EARLIER** function will evaluate to ‘0.00’ on the first row
    *   the outer loop of this evaluation is the **Sale Amount** calculation, which is **Price** \* **Amount Sold**

The **FILTER** function can now return with a table where all of the rows have a value greater than $0.00. The **COUNTROWS** function then counts all of the rows in that table, which is 49. This is why we had to add a “+1” at the end of the formula to return with 50. This loop is repeated for each of the remaining rows and the ranking column is calculated.

We only had two nested row contexts in this formula, therefore we omitted the second parameter (**\[<number>\]**) in this formula. If we had more levels of nested row contexts (say three) and wanted the **EARLIER** function to evaluate at the first level, we would enter ‘2’ as the **\[<number>\]**.

That brings us to an end to this, er, simple blog!

That’s it for this week, come back next week for more Power Pivot. Until then happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-earlier-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-earlier-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-earlier-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-earlier-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-earlier-function/#0 "close")

top