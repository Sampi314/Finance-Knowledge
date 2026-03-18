# Power Query: All Change for Values

**Source:** https://sumproduct.com/blog/power-query-all-change-for-values/

---

[Home](https://sumproduct.com/)

\> Power Query: All Change for Values

*   August 4, 2020

Power Query: All Change for Values
==================================

Power Query: All Change for Values
==================================

5 August 2020

_Welcome to our Power Query blog. This week, I look at replacing values in all columns in a table._

I have the following data, and I decide to select all my columns and replace the null values with a space:

![](<Base64-Image-Removed>)

I click ‘OK’ and Power Query generates a line of **M** code for my step.

![](<Base64-Image-Removed>)

The **M** code generated is:

**\= Table.ReplaceValue(#”Duplicated Column”,null,” “,Replacer.ReplaceValue,{“Column1”, “Column2”, “Column3”, “Index”, “Column3 – Copy”})**

This code clearly relies on the column names staying the same. I want to adjust this step so that the column names are calculated right before I replace the null values. I can do this by using **Table.ColumnNames()**:

**Table.ColumnNames(table** as table**)** as list

This function returns the column names in the **table** as a list of text.

Since each step is a table, I can use the step name:

![](<Base64-Image-Removed>)

I can now see a list of my column names. The **M** code I have used is:

**\= Table.ColumnNames(#”Duplicated Column”)**

This refers to the step before ‘Replaced Value’. I can then change my ‘Replaced Value’ step to use this list.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.ReplaceValue(#”Duplicated Column”,null,” “,Replacer.ReplaceValue,Custom1)**

This means I am using the list generated in the ‘Custom1’ step to replace values in the ‘Duplicated Column’ step. I have generated the steps in this order to show the process. It’s best to create the list before trying to replace the values in practice!

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-all-change-for-values/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-all-change-for-values/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-all-change-for-values/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-all-change-for-values/#0)

[](https://sumproduct.com/blog/power-query-all-change-for-values/#0 "close")

top