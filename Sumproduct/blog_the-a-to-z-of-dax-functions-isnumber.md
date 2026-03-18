# The A to Z of DAX Functions – ISNUMBER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnumber/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISNUMBER

*   December 9, 2025

The A to Z of DAX Functions – ISNUMBER
======================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **_**ISNUMBER**_**._

**_The_** _**_**ISNUMBER**_**_ **_function_**

**_**_**_T_**_**_**

![](<Base64-Image-Removed>)

The **ISNUMBER** function examines whether a value is a number:

> **ISNUMBER(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the value the function performs the number check on.

Here are a few remarks about the **ISNUMBER** function:

*   it returns TRUE when a value is a number
*   it returns FALSE when a value is anything other than a number
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s perform a test to see how the function operates under different conditions.  A table named **NumberTypesWithChecks** was created (**Modeling -> New table**) which contains different value types and a check using **ISNUMBER**:

![](<Base64-Image-Removed>)

**NumberTypesWithChecks =  
ADDCOLUMNS (  
    ROW (  
        “As Integer”,     7,  
        “As Decimal”,     7.5,  
        “As Currency”,    CURRENCY ( 7 ),  
        “As Date”,        DATE ( 2024, 1, 1 ),  
        “As Text”,        “7”,  
        “As Boolean”,     TRUE()  
    ),  
    “Integer Check”,     ISNUMBER ( \[As Integer\] ),  
    “Decimal Check”,     ISNUMBER ( \[As Decimal\] ),  
    “Currency Check”,    ISNUMBER ( \[As Currency\] ),  
    “Date Check”,        ISNUMBER ( \[As Date\] ),  
    “Text Check”,        ISNUMBER ( \[As Text\] ),  
    “Boolean Check”,     ISNUMBER ( \[As Boolean\] )  
)**

Each data type has been placed into separate columns as Power BI does not allow for variance of data types within the same column.  This is a better view of the data using visuals:

![](<Base64-Image-Removed>)

Notice, the **ISNUMBER** function has only classified numerical values as being numbers, and even though it is visually identical, has not included the text value in that group.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnumber/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnumber/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnumber/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnumber/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnumber/#0 "close")

top