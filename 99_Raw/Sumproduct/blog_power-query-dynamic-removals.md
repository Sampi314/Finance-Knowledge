# Power Query: Dynamic Removals

**Source:** https://sumproduct.com/blog/power-query-dynamic-removals/

---

[Home](https://sumproduct.com/)

\> Power Query: Dynamic Removals

*   March 3, 2020

Power Query: Dynamic Removals
=============================

Power Query: Dynamic Removals
=============================

4 March 2020

_Welcome to our Power Query blog. This week, I look at how to remove columns without referencing column names._

_John, my reliable imaginary salesperson, has been filling in data again. This time, he has added a few extra columns to his data._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-262.jpg)

_John has been keeping track of how the expenses have been paid for, but I don’t need this information. I will extract the data into Power Query. To do this, I use ‘From Table’ on the ‘Get & Transform’ section of the ‘Data’ tab._

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-263-1.jpg)

_My data has headers, so I accept the suggested options in the dialog._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-248-1.jpg)

_I select the columns I want to remove, keeping **CTRL** pressed, and right-click to remove columns._

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-222-1.jpg)

_I want to check the **M** code generated for this step._

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-193-1.jpg)

_The **M** code generated is_

_**\= Table.RemoveColumns(#”Changed Type”,{“Card”, “Cash”, “Mike”})**_

_The problem with this, is that John will come up with other column names next time. I need a more dynamic way of choosing which columns to remove. To do this, I go back to my initial ‘Source’ step and delete the other steps. I will add a new step using the **fx** button next to the Formula bar._

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-170-1.jpg)

_The step I am going to add will create a list of my column names._

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-145-1.jpg)

_The **M** code I am using is:_

_**\= Table.ColumnNames(Source)**_

_I also used **Table.ColumnNames** in [Power Query: Name or Number](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-name-or-number)
, when I was renaming columns using their position instead of their column names._

![](<Base64-Image-Removed>)

_I have a list of my column names. I want to convert this to a table using the ‘Convert to Table’ option on the ‘List Tools, Transform’ tab._

![](<Base64-Image-Removed>)

_I accept the defaults and create my table._

![](<Base64-Image-Removed>)

_I want to filter my table so that I only have the columns I want to remove._

![](<Base64-Image-Removed>)

_I click OK to leave the columns I want to remove._

![](<Base64-Image-Removed>)

_I need to reference this table when I remove columns. I add a new step that will take the source and remove the columns in this table._

![](<Base64-Image-Removed>)

_The **M** code I have used is:_

_**\= Table.RemoveColumns(Source,#”Filtered Rows”\[Column1\])**_

![](<Base64-Image-Removed>)

_This removes the other columns without referencing their names. I can check that this will work if John adds other columns. I ‘Close & Load’ my data first, and then add another expense to John’s table:_

![](<Base64-Image-Removed>)

_I have added another column,_ _**Cheque**__, to pay for a hotel bill. I refresh the query to see the results._

![](<Base64-Image-Removed>)

_The hotel expense has been added, but new column_ _**Cheque**_ _is not shown. It works!_

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-dynamic-removals/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-dynamic-removals/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-dynamic-removals/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-dynamic-removals/#0)

[](https://sumproduct.com/blog/power-query-dynamic-removals/#0 "close")

top