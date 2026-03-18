# The A to Z of DAX Functions – COMBINEVALUES

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combinevalues/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COMBINEVALUES

*   May 24, 2022

The A to Z of DAX Functions – COMBINEVALUES
===========================================

Power Pivot Principles: The A to Z of DAX Functions – COMBINEVALUES
===================================================================

24 May 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COMBINEVALUES**._

**_The COMBINEVALUES function_**

![](<Base64-Image-Removed>)

This function joins two or more text strings into one text string. This is used primarily to support multi-column relationships in DirectQuery models.

The **COMBINEVALUES** function employs the following syntax to operate:

**COMBINEVALUES(delimiter, expression, expression\[, expression, …\])**

The **COMBINEVALUES** function has the following arguments:

*   **delimiter****:** this is required and represents the separator used during concatenation. This must be a constant value
*   **expression:** the first two arguments are required and represent DAX expressions whose values will be joined into a single text string.

It should be further noted that:

*   the **COMBINEVALUES** function assumes, but does not validate, that when the input values are different, the output strings are also different. Based upon this assumption, when **COMBINEVALUES** is used to create calculated columns in order to build a relationship that joins multiple columns from two DirectQuery tables, an optimised join condition is generated at query time.For example, if users want to create a relationship between **Table1(Column1, Column2)** and **Table2(Column1, Column2)**, they can create two calculated columns, one on each table, as:

**Table1\[CalcColumn\] = COMBINEVALUES(“,”, Table1\[Column1\], Table1\[Column2\])**

and

**Table2\[CalcColumn\] = COMBINEVALUES(“,”, Table2\[Column1\], Table2\[Column2\])**,

and then create a relationship between **Table1\[CalcColumn\]** and **Table2\[CalcColumn\]**. Unlike other DAX functions and operators, which are translated literally to the corresponding SQL operators and functions, the above relationship generates a SQL join predicate as:

**(Table1.Column1 = Table2.Column1 OR Table1.Column1 IS NULL AND Table2.Column1 IS NULL)**

and

**(Table1.Column2 = Table2.Column2 OR Table1.Column2 IS NULL AND Table2.Column2 IS NULL)  
**

·

*   the join predicate can potentially deliver much better query performance than one that involves complex SQL operators and functions
*   the **COMBINEVALUES** function relies upon users to choose the appropriate delimiter to ensure that unique combinations of input values produce distinct output strings, but it does not validate that the assumption is true. For example, if users choose “| ” as the delimiter, but one row in **Table1** has **Table1\[Column1\]** = “| ” and **Table2 \[Column2**\] = ” “, while one row in **Table2** has **Table2\[Column1\]** = ” ” and **Table2\[Column2\]** = “| “, the two concatenated outputs will be the same “|| “, which seem to indicate that the two rows are a match in the join operation. The two rows are not joined together if both tables are from the same DirectQuery source although they are joined together if both tables are imported.

Please see my example below:

The DAX query

**EVALUATE DISTINCT(SELECTCOLUMNS(DimDate, “Month”, COMBINEVALUES(“, “, \[MonthName\], \[CalendarYear\])))**

would return the single column table _(say)_:

January, 2021  
February, 2021  
March, 2021  
April, 2021  
May, 2021  
June, 2021  
July, 2021  
August, 2021  
September, 2021  
October, 2021  
November, 2021  
December, 2021  
January, 2022  
February, 2022  
March, 2022  
April, 2022  
May, 2022  
June, 2022  
July, 2022  
August, 2022  
September, 2022  
October, 2022  
November, 2022  
December, 2022  
_etc._

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combinevalues/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combinevalues/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combinevalues/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combinevalues/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combinevalues/#0 "close")

top