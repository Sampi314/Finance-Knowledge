# The A to Z of DAX Functions – HASONEFILTER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonefilter/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – HASONEFILTER

*   March 5, 2024

The A to Z of DAX Functions – HASONEFILTER
==========================================

Power Pivot Principles: The A to Z of DAX Functions – HASONEFILTER
==================================================================

5 March 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **HASONEFILTER**._

**_The_** _**HASONEFILTER**_ **_function_**

![](<Base64-Image-Removed>)

The **HASONEFILTER** function is one of the information functions. It returns TRUE when the number of direct filtered values on **columnName** is one; otherwise, it returns FALSE. It employs the following syntax:

**HASONEFILTER (columnName)**

This function has one parameter:

*   **columnName**: this is required and represents the name of an existing column, using standard DAX syntax and it cannot be an expression.

It has the following remarks:

*   this function is similar to **HASONEVALUE** function with the difference that **HASONEVALUE** works based in cross-filters while **HASONEFILTER** works by a direct filter
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following Table call **tbl\_Example**:

![](<Base64-Image-Removed>)

We can write a DAX to check if **Group** has only one \[1\] filter:

![](<Base64-Image-Removed>)

Then we may place this measure onto the PivotTable to check the result:

![](<Base64-Image-Removed>)

We can add more inputs in the **tbl\_Example**:

![](<Base64-Image-Removed>)

After refresh the Data Model the result is as follow:

![](<Base64-Image-Removed>)

We can use this function inside the [**CALCULATE**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculate/)
 function:

![](<Base64-Image-Removed>)

The [**CALCULATE**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculate/)
 function will filter out the **tbl\_Example** for value “A” only then the **HASONEFILTER** will perform its function which give us the following:

![](<Base64-Image-Removed>)

However, if the filter context of [**CALCULATE**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-calculate/)
 has two \[2\] (or more) filters, even though the output data will only contain “A”, the **HASONEFILTER** will output a FALSE result, _viz._

![](<Base64-Image-Removed>)

It will output the following:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonefilter/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonefilter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonefilter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonefilter/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonefilter/#0 "close")

top