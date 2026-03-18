# The A to Z of DAX Functions – EVALUATE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-evaluate/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EVALUATE

*   September 5, 2023

The A to Z of DAX Functions – EVALUATE
======================================

Power Pivot Principles: The A to Z of DAX Functions – EVALUATE
==============================================================

5 September 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EVALUATE**._

**_The_** _**EVALUATE**_ **_statement_**

![](<Base64-Image-Removed>)

The **EVALUATE** statement is a DAX statement that is needed to execute a query. **EVALUATE** followed by any table expression returns the result of the table expression. It has the following syntax:

**EVALUATE(table)**

It has one \[1\] argument:

*   **table**: this represents a **table** expression.

Here are a few remarks about this statement:

*   a DAX query can contain multiple **EVALUATE** statements and the entire batch of **EVALUATE** statements executed together
*   an **EVALUATE** statement is divided into three parts:

![](<Base64-Image-Removed>)

*   **Definition section**: which is introduced by the **[DEFINE](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-define)
    ** statement. This section is optional. It contains the definition of local entities like tables, columns, variables, and measurements. For one or more inquiries, there can be just one definition section
*   **Query expression**: introduced by the **EVALUATE** statement. It contains the table expression to evaluate and return the result. There could be several query phrases, each with its own set of result modifiers introduced by the **EVALUATE** statement
*   **Result modifiers**: introduced by the **ORDER BY** statement. This section is optional or additional to the **EVALUATE** statement. By specifying a starting point with the **START AT** statement, it contains the result’s sort order and the optional determination of which rows to return.

Let’s consider the following example, where we have the following **EVALUATE** statement in ‘Edit DAX’ of Excel:

**EVALUATE**

      **{1,2,3,4,5}**

![](<Base64-Image-Removed>)

This DAX code will return us a table with just one column named **Value** as follows:

![](<Base64-Image-Removed>)

Other than using ‘Table constructor’ to manipulate the table here with the **EVALUATE** statement. We can use the **EVALUATE** statement to call upon the table we have in our Data Model. For example, we have the **Customer** table within our Data Model. We can write the following DAX code to call to our spreadsheet here:

**EVALUATE**

        **Customer**

![](<Base64-Image-Removed>)

This DAX code will return us the following table:

![](<Base64-Image-Removed>)

As we know from our previous blog for the **[DEFINE](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-define)
** statement, we can simply declare a variable using this code:

![](<Base64-Image-Removed>)

In a similar fashion, you can use the **EVALUATE** statement to declare a variable here:

![](<Base64-Image-Removed>)

Both of these codes will return us same table as follows:

![](<Base64-Image-Removed>)

On the other hand, we can use the **EVALUATE** statement directly to create a measure here. Please consider the following example here where we have the following **Sales** table (not displayed in full)

![](<Base64-Image-Removed>)

The **Customers** table is as follows:

![](<Base64-Image-Removed>)

In our previous blog for the **DEFINE** statement we wrote this code to create a brand-new table where ‘**Total Sales**’ are sorted by **Country**:

**DEFINE**

      **MEASURE Sales\[Total  \
Sales\] = SUM(Sales\[SalesAmount\])**

**EVALUATE**

      **SUMMARIZECOLUMNS(Customer\[Country\],**

                  **“Total Sales”, \[Total Sales\])**

We can achieve the same result of this code just using the **EVALUATE** statement:

**EVALUATE**

      **SUMMARIZECOLUMNS(Customer\[Country\],**

      **“Total Sales”,  
SUM(Sales\[SalesAmount\])**

      **)**

Both of these DAX code above will give us the following table:

![](<Base64-Image-Removed>)

Writing DAX code to generate the table above using the **EVALUATE** statement is shorter than the **DEFINE** statement. However, if we have a much more complex query here, using both statements would be an effective way to organise your DAX code.

Another feature of this DAX statement is that if you declare a **VAR** statement in the **DEFINE** statement, it may be overwritten in the **EVALUATE** statement. Take a look at the following example:

**DEFINE  
VAR A = {1,2,3,4,5}  
EVALUATE  
VAR A = {14}  
RETURN  
A**

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-evaluate/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-evaluate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-evaluate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-evaluate/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-evaluate/#0 "close")

top