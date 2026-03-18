# Power Query: All Dates Must Change

**Source:** https://sumproduct.com/blog/power-query-all-dates-must-change/

---

[Home](https://sumproduct.com/)

\> Power Query: All Dates Must Change

*   December 1, 2020

Power Query: All Dates Must Change
==================================

Power Query: All Dates Must Change
==================================

2 December 2020

_Welcome to our Power Query blog. This week, I look at how to dynamically set the Data Type on all my datetime columns to date._

I have some employee data for my imaginary salespeople:

![](<Base64-Image-Removed>)

I extract my data to Power Query by using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](<Base64-Image-Removed>)

As usual, I accept the defaults.

![](<Base64-Image-Removed>)

I can see that all my date columns have defaulted to Data Type ‘Date/Time’. I want to change them all to Data Type ‘Date’.

I start by getting a list of columns with my target Data Type ‘Date/Time’. The **M** function I will use is **Table.ColumnsOfType()**:

**Table.ColumnsOfType(table** as table, **listOfTypes** as list**)** as list

This returns a list with the names of the columns from **table** that match the types specified in **listOfTypes**

![](<Base64-Image-Removed>)

I have entered a new step with the **M** code:

**\= Table.ColumnsOfType( #”Changed Type”, {type nullable datetime})**

When I enter my step, I should get a list of the columns with Data Type ‘Date/Time’.

![](<Base64-Image-Removed>)

I have my list, now I need to change the datatype for all the columns in my list. To do this I will combine two **M** functions, **Table.TransformColumnTypes()** and **List.Transform()**.

**Table.TransformColumnTypes(table** as table, **typeTransformations** as list, optional **culture** as nullable text**)** as table

This parameter returns a table from the input **table** by applying the transform operation to the columns specified in the parameter **typeTransformations** (where format is **{ column name, type name}**), using the specified culture in the optional parameter **culture** (for example, “en-US”). If the column doesn’t exist, an exception is thrown.

**List.Transform(list** as list, **transform** as function**)** as list

This returns a new list of values by applying thetransform function **transform** to the **list.**

I create a new step:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.TransformColumnTypes**

**(#”Changed Type”, List.Transform(#”Custom1″,each {\_, type date}))**

I have transformed my list to specify the Data Type to change to, creating a list of pairs of data (column name, Data Type). This list can then be used to transform the columns that the list refers to. When I enter my step, the datatype should change on all the columns in the list created at step ‘Custom1’.

![](<Base64-Image-Removed>)

I can see that all the columns in my list have been updated to Data Type ‘Date’. Since I have done this by creating a list, adding or removing date columns will not break my code.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-all-dates-must-change/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-all-dates-must-change/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-all-dates-must-change/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-all-dates-must-change/#0)

[](https://sumproduct.com/blog/power-query-all-dates-must-change/#0 "close")

top