# Power Pivot Principles: HASONEFILTER vs. HASONEVALUE vs. ISFILTERED

**Source:** https://sumproduct.com/blog/power-pivot-principles-hasonefilter-vs-hasonevalue-vs-isfiltered/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: HASONEFILTER vs. HASONEVALUE vs. ISFILTERED

*   August 10, 2020

Power Pivot Principles: HASONEFILTER vs. HASONEVALUE vs. ISFILTERED
===================================================================

Power Pivot Principles: HASONEFILTER vs. HASONEVALUE vs. ISFILTERED
===================================================================

11 August 2020

_Welcome back to the Power Pivot Principles blog. This week, we will compare the **HASONEFILTER** function to the **HASONEVALUE** and **ISFILTERED** functions in DAX._

To recap, The **[HASONEFILTER](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-hasonefilter)
**function returns TRUE when the number of directly filtered values on **columnName** is one (1); otherwise, it will return FALSE. The **HASONEFILTER** function has the following syntax:

**HASONEFILTER(columnName)**

The **[HASONEVALUE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-hasonevalue-function)
**function returns TRUE when the context of a specific column has been filtered down to one distinct value only; otherwise, the function returns FALSE. The **HASONEVALUE** follows the syntax:

**HASONEVALUE(columnName)**

The **[ISFILTERED](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-properly-calculating-weighted-totals-with-the-isfiltered-function)
** function has the following syntax:

**ISFILTERED(columnName)**

This returns a TRUE value when the **columnName** parameter is filtered in the PivotTable (by definition, all simple, non-total rows and columns in a PivotTable are filtered by a given context). If there is no filter applied to the **columnName**, the function will return with FALSE.

Let’s get illustrated by returning to our **Sales** data example:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-166-1.jpg)

The **HASONEFILTER Test** and the **Total Sales (HASONEFILTER)** measures have been created to illustrate the **HASONEFILTER** function:

**HASONEFILTER Test := HASONEFILTER(Sales\[Product\])**

**Total Sales (HASONEFILTER) := IF(HASONEFILTER(Sales\[Product\]), SUM(Sales\[Sales Amount\]), BLANK())**

We will create similar **Test** and **Total Sales** measures for the **HASONEVALUE** and the **ISFILTERED** functions:

**HASONEVALUE Test := HASONEVALUE(Sales\[Product\])**

**Total Sales (HASONEVALUE) := IF(HASONEFILTER(Sales\[Product\]), SUM(Sales\[Sales Amount\]), BLANK())**

**ISFILTERED Test := ISFILTERED(Sales\[Product\])**

Returning to Excel, we create a PivotTable by dragging the **Product** field to Columns and the six measures to Values. In addition, we create two Slicers: **Product** and **Store Key**. At first glance, when nothing is chosen from the Slicers, all the three functions seem to behave in the same way:

![](<Base64-Image-Removed>)

When we select one product **Accessories** from the **Product** slicer, all the three functions show TRUE in the **Test** columns and **Total Sales** as well as **Grand Total Sales** in the **Total Sales** columns:

![](<Base64-Image-Removed>)

The similar thing happens when one filter is applied in the **Store Key** slicer:

![](<Base64-Image-Removed>)

However, if we select two fields, say, **Accessories** and **Clothing** in the **Product** slicer, only the **ISFILTERED Test** and **Total Sales (ISFILTERED)** columns display TRUE / a value in the **Grand Total** row:

![](<Base64-Image-Removed>)

Similar results occur when we select multiple fields from the **Store Key** slicer. It is because among the three functions, only the **ISFILTERED** function returns values for multiple direct filters:

![](<Base64-Image-Removed>)

Let’s add an additional table called ‘**Product List**‘, which stores the list of products. We load this table into the Power Pivot Data Model:

![](<Base64-Image-Removed>)

In the diagram view, we define the relationship between tables by connecting the **Product** field from the **Sales** table with the ‘**Product from Product List**‘ in the ‘**Product List**‘ table:

![](<Base64-Image-Removed>)

Returning to Excel, we create a Slicer with ‘**Product from Product List**‘. If we select one product, say **Accessories**, from this Slicer, only the **HASONEVALUE Test** and **Total Sales (HASONEVALUE)** columns show TRUE and a Total Sales number respectively in the **Grand Total** row. While the **HASONEVALUE Test** column returns FALSE for the four unchosen products, the **HASONEFILTER Test** and the **ISFILTERED Test** column return TRUE for all products regardless.

![](<Base64-Image-Removed>)

If we select one more product from the Slicer, the **HASONEVALUE Test** and **Total Sales (HASONEVALUE)** columns will no longer show TRUE in **Grand Total Sales**:

![](<Base64-Image-Removed>)

In summary:

*   the **HASONEFILTER** function: provides a single return for a direct filter
*   the **HASONEVALUE** function: provides a single return for a direct and / or cross filter
*   the **ISFILTERED** function: provides a single return for multiple direct filters.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-hasonefilter-vs-hasonevalue-vs-isfiltered/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-hasonefilter-vs-hasonevalue-vs-isfiltered/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-hasonefilter-vs-hasonevalue-vs-isfiltered/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-hasonefilter-vs-hasonevalue-vs-isfiltered/#0)

[](https://sumproduct.com/blog/power-pivot-principles-hasonefilter-vs-hasonevalue-vs-isfiltered/#0 "close")

top