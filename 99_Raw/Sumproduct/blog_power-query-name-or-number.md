# Power Query: Name or Number

**Source:** https://sumproduct.com/blog/power-query-name-or-number/

---

[Home](https://sumproduct.com/)

\> Power Query: Name or Number

*   August 20, 2019

Power Query: Name or Number
===========================

Power Query: Name or Number
===========================

21 August 2019

_Welcome to our Power Query blog. Today, I look at an example where renaming a column is performed by column position._

I have some expense data that Mary, my reliable fictional salesperson has supplied:

![](<Base64-Image-Removed>)

I want to rename **_expense_** to **_Expense Type_**. I can double click the column or right-click and select ‘Rename’:

![](<Base64-Image-Removed>)

I have created a new step with the following **M** code

**\= Table.RenameColumns(Source,{{“expense “, “Expense Type”}})**

I make a few other changes and save my query.

![](<Base64-Image-Removed>)

I have similar data from Paul:

![](<Base64-Image-Removed>)

I use the **Expenses** query for this data too.

![](<Base64-Image-Removed>)

However, the results are not ideal:

![](<Base64-Image-Removed>)

Paul has called the column holding the expense type data **_Type_**, so column name **_expense_** is not recognised. I need a way of renaming my column without using the original name. I will use the formula **Table.ColumnNames()** instead of the original name of the column.

Table.ColumnNames(**table** as table) as {Text}

This function returns the names of columns from a **table**.

**Table.ColumnNames** will return all the column names from my table in a list, so **Table.ColumnNames(Source)** will give me all the column names in my source. In order to select a particular column name, I need to specify where my column appears in the list, starting at 0 for the first column. The expense type data is in the third column, so its index will be two (2). Therefore, instead of my original step,

**\=Table.RenameColumns(Source,{{“expense “, “Expense Type”}})**

I will use

**\=Table.RenameColumns(Source,{{Table.ColumnNames(Source){2}, “Expense Type”}})**

![](<Base64-Image-Removed>)

My column has been renamed without referencing the original column name. This is great so I save my query…

![](<Base64-Image-Removed>)

Another problem! This time, Paul has not used a capital letter on the **_Amount_** column. I can use a similar approach for the **_Expense Type_** column. Instead of the step

**\=Table.TransformColumnTypes(#”Filled Down”,{{“Amount”, Currency.Type}})**

I will use

**\=Table.TransformColumnTypes(#”Filled Down”,{{Table.ColumnNames(Source){3}, Currency.Type}})**

This time, I need to direct my change at the fourth column, identified by index 3:

![](<Base64-Image-Removed>)

I have now created a more robust query that can cope with my salespeople’s column names.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-name-or-number/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-name-or-number/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-name-or-number/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-name-or-number/#0)

[](https://sumproduct.com/blog/power-query-name-or-number/#0 "close")

top