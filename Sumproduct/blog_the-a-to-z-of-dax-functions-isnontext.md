# The A to Z of DAX Functions – ISNONTEXT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnontext/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISNONTEXT

*   December 2, 2025

The A to Z of DAX Functions – ISNONTEXT
=======================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **_**ISNONTEXT**_**._

**_The_** _**_**ISNONTEXT**_**_ **_function_**

**_**_**_T_**_**_**

![](<Base64-Image-Removed>)

The **ISNONTEXT** function examines whether a **value** type is anything other than text:

> **ISNONTEXT(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the value the function performs the text check on.

Here are a few remarks about the **ISNONTEXT** function:

*   it returns TRUE when a value is not text
*   it returns FALSE when a value is text
*   empty text strings are considered as text
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s perform a test to see how the function operates under different conditions.  A table named **NonTextTypesWithChecks** was created which contains different value types and a check using **ISNONTEXT**:

![](<Base64-Image-Removed>)

**NonTextTypesWithChecks =  
ADDCOLUMNS (  
    ROW (  
        “As Number”,     42,  
        “As Text”,       “42”,  
        “As Boolean”,    TRUE(),  
        “As Date”,       DATE ( 2024, 1, 1 ),  
        “As Blank”,      BLANK(),  
        “As Empty Text”, “”  
    ),  
    “Number Check”,     ISNONTEXT ( \[As Number\] ),  
    “Text Check”,       ISNONTEXT ( \[As Text\] ),  
    “Boolean Check”,    ISNONTEXT ( \[As Boolean\] ),  
    “Date Check”,       ISNONTEXT ( \[As Date\] ),  
    “Blank Check”,      ISNONTEXT ( \[As Blank\] ),  
    “Empty Text Check”, ISNONTEXT ( \[As Empty Text\] )  
)**

Each data type has been placed into separate columns as Power BI does not allow for variance of data types within the same column.  This is a better view of the data using visuals:

![](<Base64-Image-Removed>)

Notice, the **ISNONTEXT** function has only classified text values as being text, even though some type variants, such as the given number or Boolean value, may be visually identical to text values.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnontext/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnontext/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnontext/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnontext/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isnontext/#0 "close")

top