# Power Pivot Principles: Introducing the Function DISTINCTCOUNT

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-distinctcount/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the Function DISTINCTCOUNT

*   January 27, 2020

Power Pivot Principles: Introducing the Function DISTINCTCOUNT
==============================================================

Power Pivot Principles: Introducing the Function DISTINCTCOUNT
==============================================================

28 January 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a method to derive the unique values in a column by using DAX._

The DAX function **DISTINCTCOUNT** counts the number of distinct (unique) values in a column. It has the following syntax to operates:

**DISTINCTCOUNT**(**<column>**)

where:

*   <**column**\> is the column that contains the values to be counted.

This function returns the number of distinct values in **column**. The only argument allowed in this function is a column. We can use columns containing any type of data. When the function finds no rows to count, it returns **BLANK**; otherwise, it returns the count of distinct values.

Let’s look at one simple example. Consider the following data table:

![](<Base64-Image-Removed>)

In order to get the count of unique value for column **Brand**, we can write the following measure:

![](<Base64-Image-Removed>)

This measure calculates the distinct values in column **Brand** of the table **FactsTable**. In order to compare the distinct values with total counts of **Brand**, we create another measure:

![](<Base64-Image-Removed>)

We create a PivotTable based on the measure we created and select **Brand** as the **Rows** parameter. The result would be:

![](<Base64-Image-Removed>)

The table above explained the difference between distinct values and the total counts of brand. If we want to include the **Country** as additional selection criteria, we need add another measure:

![](<Base64-Image-Removed>)

In this measure, we use function **ALLEXCEPT** to filter the context except for the **Country** and then calculates the distinct count. Then we create a PivotTable contains all the columns and the result would be:

![](<Base64-Image-Removed>)

The table above shows that for Australia, the unique value is four (4) and for USA, the unique value is six (6). The grand total value is seven (7) because the measure calculates the total unique value without considering the context of **Country**.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-distinctcount/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-distinctcount/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-distinctcount/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-distinctcount/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-distinctcount/#0 "close")

top