# A to Z of Excel Functions: The DAVERAGE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-daverage-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DAVERAGE Function

*   April 12, 2018

A to Z of Excel Functions: The DAVERAGE Function
================================================

A to Z of Excel Functions: The DAVERAGE Function
================================================

13 April 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DAVERAGE** function._

**The DAVERAGE function**

This function averages the values in a field (that’s jargon for a column!) of records in a list or table that match one or more conditions you specify.

The **DAVERAGE** function employs the following syntax to operate:

**DAVERAGE(database, field, criteria)**

The **DAVERAGE** function has the following arguments:

*   **database**: this is the range of cells that makes up the list or database. A **database** is a list of related data in which rows of related information are records and columns of data are fields. The first row of the list contains labels for each column
*   **field:** indicates which column is used in the function. Make sure you enter the column label enclosed between inverted commas (double quotation marks), _e.g._ “Age” or “Yield”, or a number (without quotation marks) that represents the position of the column within the list, that is, 1 for the first column, 2 for the second column, and so on
*   **criteria:** is the range of cells that contains the conditions you specify.

It should be further noted that:

*   you can use any range for the **criteria** argument, as long as it includes at least one column label and at least one cell below the column label for specifying the condition, _e.g._ if the range **G1:G2** contains the column label Income in **G1** and the amount 10,000 in **G2**, you could define the range as **MatchIncome** and use that name as the **criteria** argument in the database functions
*   although the **criteria** range can be located anywhere on the worksheet, do not place the **criteria** range below the list. If you add more information to the list, the new information is added to the first row below the list. If the row below the list is not blank, Excel cannot add the new information
*   make sure the **criteria** range does not overlap the list
*   to perform an operation on an entire column in a database, enter a blank line below the column labels in the criteria range.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/8618b691da0fd916442f0614c3173d15.jpg)

**_Criteria Examples_**

Typing an equal sign in a cell indicates you want to enter a formula. To display text that includes an equal sign, surround the text and the equal sign with double quotes, like so:

“=Liam”

You also do that if you’re entering an expression (a combination of formulas, operators, and text) and you want to display the equal sign instead of have Excel use it in a calculation. For example:

**\=”=** _entry_ **“**

Where _entry_ is the text or value you want to find. For example:

![](<Base64-Image-Removed>)

*   When filtering text data, Excel does not distinguish between uppercase and lowercase characters. However, you can use a formula to perform a case-sensitive search _(see below)_.

The following sections provide examples of complex criteria.

**Multiple criteria in one column**

**Boolean logic:** (Salesperson = “Tim” **OR** Salesperson = “Kathryn”)

To find rows that meet multiple criteria for one column, type the criteria directly below each other in separate rows of the criteria range.

_e.g._ In the following data range (**A5:C9**), the criteria range (**B1:B3**) displays the rows that contain either “Tim” or “Kathryn” in the **Salesperson** column (**B5:B9**).

![](<Base64-Image-Removed>)

**Multiple criteria in multiple columns where all criteria must be true**

**Boolean logic:** (Service = “Auditing” **AND** Sales > 1500)

To find rows that meet multiple criteria in multiple columns, type all of the criteria in the same row of the criteria range.

In the following data range (**A5:C9**), the criteria range (**A1:C2**) displays all rows that contain “Auditing” in the **Service** column and a value greater than $1,500 in the **Sales** column (**C5:C9**).

![](<Base64-Image-Removed>)

**Multiple criteria in multiple columns where any criteria can be true**

**Boolean logic:** (Service = “Auditing” **OR** Salesperson = “Kathryn”)

To find rows that meet multiple criteria in multiple columns, where any criteria can be true, type the criteria in different rows of the criteria range.

In the following data range (**A5:C9**), the criteria range (**A1:B3**) displays all rows that contain “Auditing” in the **Service** column (**C5:C9**) or “Kathryn” in the **Salesperson** column (**B5:B9**).

![](<Base64-Image-Removed>)

**Multiple sets of criteria where each set includes criteria for multiple columns**

**Boolean logic:** ( (Salesperson = “Kathryn” **AND** Sales >2000) **OR** (Salesperson = “Tim” **AND** Sales > 1500) )

To find rows that meet multiple sets of criteria, where each set includes criteria for multiple columns, type each set of criteria in separate rows.

In the following data range (**A5:C9**), the criteria range (**B1:C3**) displays the rows that contain both “Kathryn” in the **Salesperson** column and a value greater than $2,000 in the **Sales** column, or displays the rows that contain “Tim” in the **Salesperson** column (**B5:B9**) and a value greater than $1,500 in the **Sales** column (**C5:C9**).

![](<Base64-Image-Removed>)

**Multiple sets of criteria where each set includes criteria for one column**

**Boolean logic:** ( (Sales > 2000 AND Sales <= 3000 ) **OR** (Sales < 1500) )

To find rows that meet multiple sets of criteria, where each set includes criteria for one column, include multiple columns with the same column heading.

In the following data range (**A5:C9**), the criteria range (**C1:D3**) displays rows that contain values between 2,000 and 3,000 and values less than 1,500 in the **Sales** column (**C5:C9**).

![](<Base64-Image-Removed>)

**Criteria to find text values that share some characters but not others**

To find text values that share some characters but not others, do one or more of the following:

*   type one or more characters without an equal sign (=) to find rows with a text value in a column that begin with those characters. For example, if you type the text **Lia** as a criterion, Excel finds “Liam”, “Liar” and “Lianne”
*   use a wildcard character.

The following wildcard characters can be used as comparison criteria:

![](<Base64-Image-Removed>)

In the following data range (**A5:C9**), the criteria range (**A1:B3**) displays rows with “Co” as the first characters in the **Service** column or rows with the second character equal to “i” in the **Salesperson** column (**B5:B9).**

![](<Base64-Image-Removed>)

**Criteria created as the result of a formula**

You can use a calculated value that is the result of a formula as your criterion. Remember the following important points:

*   the formula must evaluate to TRUE or FALSE
*   because you are using a formula, enter the formula as you normally would, and do not type the expression in the following way:

\=_“= entry”_

*   do not use a column label for criteria labels; either keep the criteria labels blank or use a label that is not a column label in the range (in the examples below, **Calculated Average** and **Exact Match**)
*   if you use a column label in the formula instead of a relative cell reference or a range name, Excel displays an error value such as _#NAME?_ or _#VALUE!_ in the cell that contains the criterion. You can ignore this error because it does not affect how the range is filtered
*   the formula that you use for criteria must use a relative reference to refer to the corresponding cell in the first row (in the examples below, **C6** and **A6**)
*   all other references in the formula must be absolute references.

The following subsections provide specific examples of criteria created as the result of a formula.

**Filtering for values greater than the average of all values in the data range**

In the following data range (**A5:C9**), the criteria range (**D1:D2**) displays rows that have a value in the Sales column greater than the average of all the values (**C6:C9**). In the formula, “**C6**” refers to the filtered column (**C**) of the first row of the data range (**6**).

![](<Base64-Image-Removed>)

**Filtering for text by using a case-sensitive search**

In the data range (**A5:C9**), the criteria range (**D1:D2**) displays rows that contain “Auditing” in the **Service** column by using the **EXACT** function to perform a case-sensitive search (**A5:A9**). In the formula, “**A6**” refers to the filtered column (**A**) of the first row of the data range (6).

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-daverage-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-daverage-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-daverage-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-daverage-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-daverage-function/#0 "close")

top