# Power Pivot Principles: Properly Calculating Weighted Totals with the ISFILTERED Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-properly-calculating-weighted-totals-with-the-isfiltered-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Properly Calculating Weighted Totals with the ISFILTERED Function

*   October 7, 2019

Power Pivot Principles: Properly Calculating Weighted Totals with the ISFILTERED Function
=========================================================================================

Power Pivot Principles: Properly Calculating Weighted Totals with the ISFILTERED Function
=========================================================================================

8 October 2019

_Welcome back to our Power Pivot blog. Today, we look at the ISFILTERED function._

The **ISFILTERED** function uses the following syntax to operate:

**ISFILTERED( <ColumnName> )**

The **<ColumnName>** parameter is a column that currently exists in a table that is currently loaded in the Data Model (_i.e._ it is a pre-existing field).

The **ISFILTERED** function returns with a **TRUE** value when the **<ColumnName>** parameter is filtered in the PivotTable (by definition, all simple, non-total rows and columns in a PivotTable are filtered by a given context). If there is no filter related to the **<ColumnName>**,the function will return with **FALSE**.

Let’s consider an example:

![](<Base64-Image-Removed>)

After loading the table above into our data model, we create the following PivotTable:

![](<Base64-Image-Removed>)

We simply want to create a ‘Weighted Sales’ column that will multiply the sale value with the corresponding weights. However, upon close inspection the Grand Total is returning with the value of ’70’. This is incorrect: it should rightfully evaluate to 24 (15 + 0.5 + 1 + 7.5 = 24).

The solution is to use a combination of the **ISFILTERED**, **IF** and **SUMX** (you can read more about the **IF** and **SUMX** functions [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-conditional-custom-columns-using-if-and-and)
 and [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-sumx-function)
, respectively) functions:

![](<Base64-Image-Removed>)

The **IF** function will calculate the weighted totals of our sales when the **ISFILTERED** function returns with **TRUE** for each row that contains a Product. In this PivotTable **ISFILTERED** will return with **TRUE** for each of the product rows and will return with **FALSE** on the Grand Total row. The **IF** function will then evaluate the **SUMX** portion of the measure instead. This will properly calculate the total weighted sales in our PivotTable.

![](<Base64-Image-Removed>)

There you have it – how to properly calculate weighted totals in a PivotTable.

That’s it for this week; tune in next week for more Power Pivot! Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-properly-calculating-weighted-totals-with-the-isfiltered-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-properly-calculating-weighted-totals-with-the-isfiltered-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-properly-calculating-weighted-totals-with-the-isfiltered-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-properly-calculating-weighted-totals-with-the-isfiltered-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-properly-calculating-weighted-totals-with-the-isfiltered-function/#0 "close")

top