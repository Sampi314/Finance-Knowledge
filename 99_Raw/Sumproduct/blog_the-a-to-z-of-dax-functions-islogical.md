# The A to Z of DAX Functions – ISLOGICAL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-islogical/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISLOGICAL

*   November 25, 2025

The A to Z of DAX Functions – ISLOGICAL
=======================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISLOGICAL**._

**_The_** _**ISLOGICAL**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/10/image-200.png)

The **ISLOGICAL** function examines whether a value is logical (true or false):

> **ISLOGICAL(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the value the function performs the logical check on.

Here are a few remarks about the **ISLOGICAL** function:

*   it returns TRUE when a value is logical (TRUE or FALSE)
*   it returns FALSE when a value is anything other than logical (for example a number or text)
*   it does not recognise one \[1\] or zero \[1\] as logical TRUE or FALSE values
*   it does not recognise TRUE or FALSE (no matter the case) in text format as a logical value
*   it has the same arguments and provides identical output as the **ISBOOLEAN** function
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s perform a test to see how the function operates under different conditions.  A table named **LogicalTypesWithChecks** was created which contains different logical value types and a check using **ISLOGICAL**:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-201.png)

**LogicalTypesWithChecks =**

**ADDCOLUMNS (**

    **ROW (**

        **“As True”,      TRUE(),**

        **“As False”,     FALSE(),**

        **“As Number”,    1,**

        **“As Text”,      “TRUE”,**

        **“As Expression”, 1 = 10**

    **),**

    **“True Check”,       ISLOGICAL ( \[As True\] ),**

    **“False Check”,      ISLOGICAL ( \[As False\] ),**

    **“Number Check”,     ISLOGICAL ( \[As Number\] ),**

    **“Text Check”,       ISLOGICAL ( \[As Text\] ),**

    **“Expression Check”, ISLOGICAL ( \[As Expression\] )**

**)**

Each data type has been placed into separate columns as Power BI does not allow for variance of data types within the same column.  This is a better view of the data using visuals:

![](<Base64-Image-Removed>)

Notice, the **ISLOGICAL** function has only classified the values that could be used directly in conditional logic as being a logical value, whereas values like text or numbers are classified as not logical.  That’s illogical, captain!

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-islogical/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-islogical/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-islogical/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-islogical/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-islogical/#0 "close")

top