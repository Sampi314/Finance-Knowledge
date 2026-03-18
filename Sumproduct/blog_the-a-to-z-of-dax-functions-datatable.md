# The A to Z of DAX Functions – DATATABLE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datatable/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DATATABLE

*   January 10, 2023

The A to Z of DAX Functions – DATATABLE
=======================================

Power Pivot Principles: The A to Z of DAX Functions – DATATABLE
===============================================================

10 January 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_DATATABLE_**_._

**_The DATATABLE function_**

The **DATATABLE** function provides a mechanism for declaring an inline set of data values and employs the following syntax:

**DATATABLE(ColumnName1, DataType1, ColumnName2, DataType2…, ｛｛value1, value2…｝, ｛valueN, valueN+1…｝…｝)**

There are three \[3\] main arguments in this function:

*   **ColumnName**:this argument is required, and it is column name to be defined
*   **DataType**:this argument is required, and it is an enumeration that includes INTEGER, DOUBLE, STRING, BOOLEAN, CURRENCY and DATETIME
*   **value**: a single argument using Excel syntax for a one-dimensional array constant, nested to provide an array of arrays. This argument represents the set of data values that will be in the table.

As an example, consider the following DAX query:

![](https://sumproduct.com/wp-content/uploads/2025/06/d2989bd279806c4f35fe49f6b9eac6a5.jpg)

The result is as follows:

![](https://sumproduct.com/wp-content/uploads/2025/06/67c56afb7031af19a72bbd2627c8dbae.jpg)

It should be noted that:

*   the **value** arguments in the syntax of the **DATATABLE** function cannot be expressions; they need to be constant. The following syntax will generate an error:

![](<Base64-Image-Removed>)

After pressing OK the following error dialog box will appear:

![](<Base64-Image-Removed>)

*   like the **DATATABLE** function, Table Constructor also allows users to create tables, but Table Constructor allows any scalar expressions as an input value while the **DATATABLE** function does not
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datatable/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datatable/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datatable/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datatable/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datatable/#0 "close")

top