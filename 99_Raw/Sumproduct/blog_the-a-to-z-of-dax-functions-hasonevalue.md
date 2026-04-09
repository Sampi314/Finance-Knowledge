# The A to Z of DAX Functions – HASONEVALUE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonevalue/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – HASONEVALUE

*   March 12, 2024

The A to Z of DAX Functions – HASONEVALUE
=========================================

Power Pivot Principles: The A to Z of DAX Functions – HASONEVALUE
=================================================================

12 March 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **HASONEVALUE**._

![](https://sumproduct.com/wp-content/uploads/2025/06/c0d6d665feb248609e4eaf75312d923d.jpg)

The _**HASONEVALUE**_ function is one of the information functions. It returns TRUE when the context for **columnName** has beenfiltered down to one \[1\] distinct value only; otherwise it returns FALSE. It employs the following syntax:

**HASONEVALUE (columnName)**

This function has one parameter:

*   **columnName**: this is required and represents the name of an existing column, using standard DAX syntax and it cannot be an expression.

The function returns a Boolean value:

*   TRUE if there is exactly one unique value in the specified column in the current context
*   FALSE if there are multiple values or no values in the specified column in the current context.

It should be noted that:

*   an equivalent expression for **HASONEVALUE** function is

**COUNTROWS(VALUES(columnNames))=1**

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following example where we have the **tbl\_Example** Table:

![](<Base64-Image-Removed>)

We will write the following DAX to check if the how to filter context affect the output:

**DEFINE**

**VAR Filter\_Out\_A=CALCULATE(**

     **HASONEVALUE(tbl\_Example\[Group\]),**

     **tbl\_Example\[Group\]=”A”)**

**VAR Filter\_Out\_A\_n\_B= CALCULATE(**

     **HASONEVALUE(tbl\_Example\[Group\]),**

     **tbl\_Example\[Group\]=”A”||tbl\_Example\[Group\]=”B”)**

**VAR Filter\_Out\_A\_n\_C=CALCULATE(**

     **HASONEVALUE(tbl\_Example\[Group\]),**

     **tbl\_Example\[Group\]=”A”||tbl\_Example\[Group\]=”C”)**

**EVALUATE**

**{**

     **(“A  
Only”,Filter\_Out\_A),**

     **(“A  
and B”,Filter\_Out\_A\_n\_B),**

     **(“A  
and C”,Filter\_Out\_A\_n\_C)**

**}**

![](<Base64-Image-Removed>)

In the [**DEFINE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-define)
 statement, we construct the following variables:

*   the first variable is filter out A in **Group** column
*   the second variable is filter A and B in **Group** column
*   the last variable is filter A and C in **Group** column.

In the [**EVALUATE**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-evaluate)
 statement, we output those variables. It will give us the following Table:

![](<Base64-Image-Removed>)

Since we filtered “A” only for the first row, the **HASONEVALUE** return TRUE. Whilst in the last row, we filtered for “A” and “C”, in the **tbl\_Example** there is no “C” hence, “A” is the only unique value, so it returns TRUE for the last variable. For the second row, because we filtered for “A” and “B”, and “A” and “B” exist in **tbl\_Example**, the output is FALSE.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonevalue/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonevalue/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonevalue/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonevalue/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-hasonevalue/#0 "close")

top