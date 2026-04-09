# Power Pivot Principles: Introducing the HASONEFILTER Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-hasonefilter-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the HASONEFILTER Function

*   August 3, 2020

Power Pivot Principles: Introducing the HASONEFILTER Function
=============================================================

Power Pivot Principles: Introducing the HASONEFILTER Function
=============================================================

4 August 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about the **HASONEFILTER** function in DAX._

The **HASONEFILTER** function returns TRUE when the number of directly filtered values on **columnName** is one; otherwise, it will return FALSE.

The **HASONEFILTER** function has the following syntax:

**HASONEFILTER(columnName)**

For example, we have **Sales** data of a few products in four selected stores. This has already been loaded into the Power Pivot Data Model:

![](<Base64-Image-Removed>)

We will create the **HASONEFILTER Test** and the **Total Sales Test** measures to illustrate the **HASONEFILTER** function:

**HASONEFILTER Test := HASONEFILTER(Sales\[Product\])**

**Total Sales Test := Var Total Sales Test = SUM(Sales\[Sales Amount\]) Return IF(HASONEFILTER(Sales\[Product\]), Total Sales Test, BLANK())**

![](<Base64-Image-Removed>)

To make it clearer, we will add two additional measures to the list:

**Total Sales (HASONEFILTER) := IF(HASONEFILTER(Sales\[Product\]), SUM(Sales\[Sales\]), BLANK())**

**Total Sales (SUM) := SUM(Sales\[Sales Amount\])**

Returning to Excel, we create a PivotTable, with Slicers for **Product** and **Store Key**:

![](<Base64-Image-Removed>)

When nothing is chosen from the Slicers, the **HASONEFILTER Test** column returns TRUE for each filtered **Product** and returns FALSE for the **Grand Total** row. With the same logic, the **Total Sales Test** and **Total Sales (HASONEFILTER)** columns display the **Sales Amount** for each row, but not the **Grand Total**. Meanwhile, the **Total Sales (SUM)** column is not impacted by the filter.

Now if we select one **Product** from the Slicers, we may see the **Grand Total** row shows TRUE for the **HASONEFILTER Test** column and grand total sales for all other columns:

![](<Base64-Image-Removed>)

However, if we select one **Store Key** from the Slicers, our PivotTable doesn’t behave as it does with the single **Product** filter. The reason is simple: all of our measures are based on the **Product** filter, not the **Store Key**!

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-hasonefilter-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-hasonefilter-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-hasonefilter-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-hasonefilter-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-hasonefilter-function/#0 "close")

top