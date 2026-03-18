# The A to Z of DAX Functions – DEFINE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-define/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DEFINE

*   April 11, 2023

The A to Z of DAX Functions – DEFINE
====================================

Power Pivot Principles: The A to Z of DAX Functions – DEFINE
============================================================

11 April 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_DEFINE_**_._

**_The DEFINE statement_**

The **DEFINE** statementis a statement with one or more entity definitions that can be applied to one \[1\] or more **EVALUATE** statements of a DAX query. Its typical syntax is as follows:

![](https://sumproduct.com/wp-content/uploads/2025/06/f8b625ee2420ab3eef8eeb325733cd2d.jpg)

There are three \[3\] main parameters in the syntax:

*   **entity**: this can be **MEASURE**, **VAR**, **TABLE**, or **COLUMN**
*   **name**: the name of a **MEASURE**, **VAR**, **TABLE**, or **COLUMN** definition. This cannot be an expression. It does not need to be unique as the name only exists for the period of the query
*   **expression**: any DAX expression with a table or scalar value output. Any of the defined entities may be used in the expression. If you need to transform a scalar expression into a table expression, you may use the **ROW()** function to return a single row table or wrap the expression within a table constructor using curly braces **{}**.

There are a few key notes for this **DEFINE** statement:

*   a DAX query can have multiple **EVALUATE** statements, but it can have only one **DEFINE** statement
*   at least one definition is required in the **DEFINE** statement
*   measure definitions for a query will override model measure of the same name
*   **VAR** names have unique restrictions.

Let’s consider the following example, where we have the following **DEFINE** statement to declare a variable and then use the **EVALUATE** statement to export the result to the spreadsheet:

![](https://sumproduct.com/wp-content/uploads/2025/06/a36746af7bc0600c5b270a95e4062f5e.jpg)

This will return us:

![](https://sumproduct.com/wp-content/uploads/2025/06/0a9e6fdf8d7d65f47c4b3e39a82c9c3c.jpg)

On the other hand, we can use the **DEFINE** statement to declare a measure. Please consider the following example here where we have the following **Sales** table (not displayed in full):

![](<Base64-Image-Removed>)

The **Customers** table is as follows:

![](<Base64-Image-Removed>)

We can write the following DAX code to declare a measure named ‘**Total Sales**’ and summarise ‘**Total Sales**’ by the **Country** column in the **Customers** table:

**DEFINE**

      **MEASURE Sales\[Total  \
Sales\] = SUM(Sales\[SalesAmount\])**

**EVALUATE**

      **SUMMARIZECOLUMNS(Customer\[Country\],**

      **“Total  
Sales”, \[Total Sales\])** 

![](<Base64-Image-Removed>)

This code will give us the following Table:

![](<Base64-Image-Removed>)

Let’s have an example where we use the **DEFINE** statement to declare a table by using the **[DATATABLE](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-datatable)
** function:

**DEFINE**

    **TABLE History =  
DATATABLE(“Name”,    STRING,**

                      **“Region”, STRING,**

                      **“Year”,      INTEGER,**

                             **{**

                        **{“User  
1”, “South”,  1996},**

                        **{“User  
2”, “North”,  1975},**

                        **{“User  
3”, “West” ,  1949},**

                        **{“User  
4”, “East” ,  1999},**

                        **{“User  
5”, “South”,  1998},**

                        **{“User  
6”, “North”,  1944},**

                        **{“User  
7”, “West” ,  1922},**

                        **{“User  
8”, “East” ,  1900}**                               

                            **}**

                  **)**

**EVALUATE**

      **History**

![](<Base64-Image-Removed>)

This DAX code will give us a brand new data table name **History** as in the following picture:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-define/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-define/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-define/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-define/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-define/#0 "close")

top