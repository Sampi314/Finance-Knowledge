# The A to Z of DAX Functions – IGNORE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ignore/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – IGNORE

*   April 16, 2024

The A to Z of DAX Functions – IGNORE
====================================

Power Pivot Principles: The A to Z of DAX Functions – IGNORE
============================================================

16 April 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **IGNORE**._

**_The_** _**IGNORE function**_

![](https://sumproduct.com/wp-content/uploads/2025/06/1b935eabaf96a379ae61e7c9f33c3c7c.jpg)

The **IGNORE** function is used to modify the behaviour of the **SUMMARIZECOLUMNS** function by omitting specific expressions when evaluating whether to exclude a row based upon BLANK / NULL evaluation. It employs the following syntax:

**IGNORE (expression)**

It is often used with the **SUMMARIZECOLUMNS** function as follows:

**SUMMARIZECOLUMNS(groupBy\_columnName\[,  \
groupBy\_columnName \]…, \[filterTable\]…\[, name, IGNORE(…)\]…)**

The **IGNORE** function has one \[1\] argument:

*   **expression**: can be any valid **DAX** expression that returns a single value (not a table).

The key purposes of **IGNORE** are to:

*   control which expressions contribute to the decision of excluding rows in **SUMMARIZECOLUMNS**
*   include rows that may have BLANK / NULL evaluations in some expressions but provide meaningful data in others
*   preserve valuable data that might be excluded due to missing values in specific columns
*   provide flexibility in controlling which expressions contribute to row exclusion.

It works as follows:

*   **SUMMARIZECOLUMNS** normally excludes rows where all expressions evaluate to BLANK / NULL expressions
*   using **IGNORE** on some expressions tells **SUMMARIZECOLUMNS** to disregard their BLANK / NULL status when deciding row exclusion
*   the row will still be included even if the ignored expressions are BLANK / NULL, as long as at least one other non-ignored expression returns a non-BLANK / NULL evaluation.

It should be noted that **IGNORE** may only be used as an expression argument to **SUMMARIZECOLUMNS**.

In considering Best Practice:

*   use **IGNORE** judiciously to avoid misleading results
*   ensure you still have meaningful data in ignored expressions despite missing values.

Let’s consider the following Table call **TB\_Sales**. Imagine this is a Table with **Sales** data grouped by date and we wish to calculate total sales. Some dates might have missing data (_i.e._ be blank).

![](<Base64-Image-Removed>)

When we use **SUMMARIZECOLUMNS** without **IGNORE**:

**EVALUATE**

**SUMMARIZECOLUMNS (**

**  
‘TB\_Sales'\[Year\]**

     **,”Total  
Amount”, SUMX(TB\_Sales,TB\_Sales\[Sales\])**

**)**

this will exclude dates with missing sales because it will result in **BLANK** for those dates.

![](<Base64-Image-Removed>)

However, with **IGNORE**:

**EVALUATE**

**SUMMARIZECOLUMNS (**

**  
‘TB\_Sales'\[Year\]**

     **,”Total  
Amount”, IGNORE(SUMX(TB\_Sales,TB\_Sales\[Sales\]))**

**))**

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ignore/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ignore/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ignore/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ignore/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ignore/#0 "close")

top