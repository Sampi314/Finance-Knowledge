# Power Pivot Principles: Introducing the RANKX Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-rankx-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the RANKX Function

*   July 15, 2019

Power Pivot Principles: Introducing the RANKX Function
======================================================

Power Pivot Principles: Introducing the RANKX Function
======================================================

16 July 2019

_Welcome back to our Power Pivot blog. Today, we show you how use set up slicers to dynamically segregate text data based on text inputs._

The **RANKX** function returns with the ranking of the number values in a column in a table. It uses the following syntax:

**RANKX**( <table>, <expression> \[, <value>, <order>, <ties>\] )

The **RANKX** requires a <table> and an <expression> input. The <value>, <order>, and <ties> inputs are optional.

For this example, we are going to look at the following table, note that this table (an Excel Table) is given the name ‘**ProductListKitchen**‘ in Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-397.jpg)

Imagine that we wanted to rank the products in this Excel Table from the highest to lowest price in Power Pivot. Here we may use the **RANKX** function.

After adding the Table to the data model, we can create a calculated column with the following DAX code:

\=RANKX(

                ProductListKitchen,

                \[Price\]

                )

The <table> input in this code is our table ‘**ProductListKitchen**‘, because this is the Table that we wish to evaluate. The <expression> is the column that contains the values that we wish to be ranked, and that would be the **Price** column.

The resulting calculated column will then look like this:

![](<Base64-Image-Removed>)

We can then sort the items:

![](<Base64-Image-Removed>)

The default ranking is applied in decending order where **RANKX** ranks the product type with the highest price first. To swap the ranking order around we have to add ‘ASC’, which is short for ascending, as the <order> input:

\=RANKX(

                ProductListKitchen,

                \[Price\],

                ,

                ASC

                )

The resulting table will now look like this:

![](<Base64-Image-Removed>)

There we have it, we have ranked our products by ascending price in our data table.

That’s it for this week, come back next week for more Power Pivot. Until then happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-rankx-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-rankx-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-rankx-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-rankx-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-rankx-function/#0 "close")

top