# The A to Z of DAX Functions – COUNTBLANK

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countblank/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COUNTBLANK

*   September 20, 2022

The A to Z of DAX Functions – COUNTBLANK
========================================

Power Pivot Principles: The A to Z of DAX Functions – COUNTBLANK
================================================================

20 September 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COUNTBLANK**._

**_The COUNTBLANK function_**

When I explain this function sometimes I get **BLANK()** expressions from the audience…

![](https://sumproduct.com/wp-content/uploads/2025/06/40eac61e081df88628e4e85f8c00801e.jpg)

Aw shoot, I will try to explain regardless.

The **COUNTBLANK** function counts the number of blank cells in a column (field). It employs the following syntax to operate:

**COUNTBLANK(column)**

The **COUNTBLANK** function has just the one argument:

*   **column**: this is required and represents the column (field) that (possibly) contains the blank cells to be counted.

It should be further noted that:

*   the function returns a whole number (integer). If no rows are found that meet the condition (_i.e._ the value is blank), blanks are returned instead
*   the only argument allowed to this function is a column (field). You may use columns containing any type of data, but only blank cells are counted. Cells that have the value zero \[0\] are not counted, as zero is considered a numeric value and not a blank
*   whenever there are no rows to aggregate, the function returns a blank. However, if there are rows, but none of them meet the specified criteria, the function returns zero \[0\]. Microsoft Excel also returns a zero if no rows are found that meet the conditions
*   therefore, if the **COUNTBLANK** function finds no blanks, the result will be zero, but if there are no rows to check, the result will be blank
*   any empty string is considered as a blank for **COUNTBLANK** purposes, even though **ISBLANK** would return FALSE for an empty string
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

The following expressions are similar (semantically) to

**\=COUNTBLANK(Example\[Column\])**

Where the columns do not contain text strings:

**\=CALCULATE(COUNTROWS(Example),  
KEEPFILTERS(ISBLANK(Example\[Column\])))**

Where the columns contain text strings:

**\=CALCULATE(COUNTROWS(Example),  
KEEPFILTERS(Example\[Column\]=“”))**

The **CALCULATE** alternatives may calculate faster than the **COUNTBLANK** counterpart.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countblank/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countblank/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countblank/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countblank/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countblank/#0 "close")

top