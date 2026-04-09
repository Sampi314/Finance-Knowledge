# The A to Z of DAX Functions – DISTINCTCOUNT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distinctcount/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DISTINCTCOUNT

*   May 23, 2023

The A to Z of DAX Functions – DISTINCTCOUNT
===========================================

Power Pivot Principles: The A to Z of DAX Functions – DISTINCTCOUNT
===================================================================

23 May 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DISTINCTCOUNT**._

**_The DISTINCTCOUNT function_**

The **DISTINCTCOUNT** function is one of the aggregation functions. It helps to count the number of distinct values in a column. It has the following syntax:

**DISTINCTCOUNT(column)**

The **DISTINCTCOUNT** function has only one \[1\] argument:

*   **column**: this is required, and it represents the **column** that contains the values to be counted.

Some comments about the **DISTINCTCOUNT** function:

*   the only argument allowed in this function is a **column**. The **column** argument can contain any type of data
*   if the function finds no row to count it will return a BLANK. Otherwise, it returns the count of the distinct values
*   the **DISTINCTCOUNT** function counts the BLANK value, whereas the **DISTINCTCOUNTNOBLANK** function does not count BLANK values
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules
*   you may replicate the **DISTINCTCOUNT** function with the **[DISTINCT](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-distinct-column)
    ** function and the **[COUNTROWS](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-countrows)
    **function. For instance, you may write the following DAX code to compare the **DISTINCTCOUNT** function with the nested **[DISTINCT](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-distinct-column)
    **and the **[COUNTROWS](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-countrows)
    **functions:
    *   **DISTINCTCOUNT(Table\[Column Name\])**
    *   **COUNTROWS(DISTINCT(Table\[Column Name\]))**.

Let’s consider the following example where we have the following **Customer** table (data is displayed in full):

![](<Base64-Image-Removed>)

We may write the following DAX code to count the unique **Customer Name** records and group them by **Customer Group**:

![](<Base64-Image-Removed>)

This will result in the following table:

![](<Base64-Image-Removed>)

If we add one \[1\] more product key with a BLANK **Customer Name** in the **Customer** table, it will be counted as well _(see last row)_:

![](<Base64-Image-Removed>)

After refreshing the data, it should return the following table (assuming the addition is to “Wholesale”):

![](<Base64-Image-Removed>)

Thus, you can see that the Wholesale **Customer Group** received one \[1\] more count from the last row even though the **Customer Name** is BLANK. Therefore, to avoid this issue you should consider the **DISTINCTCOUNTNOBLANK** function.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distinctcount/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distinctcount/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distinctcount/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distinctcount/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-distinctcount/#0 "close")

top