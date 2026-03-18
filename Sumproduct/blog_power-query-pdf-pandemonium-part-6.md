# Power Query: PDF Pandemonium – Part 6

**Source:** https://sumproduct.com/blog/power-query-pdf-pandemonium-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: PDF Pandemonium – Part 6

*   October 19, 2021

Power Query: PDF Pandemonium – Part 6
=====================================

Power Query: PDF Pandemonium – Part 6
=====================================

20 October 2021

_Welcome to our Power Query blog. This week, I continue transforming some data that is coming in from a PDF file by working with last week’s function._

The tent business is doing well, and the UK division have plans to expand the workforce. I have a PDF file, and it contains tables for 10 stores. [Last week](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-5/)
, I created a function to apply to the **Stores** table.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-119.jpg)

In the **Stores** query, I need to make sure I only have the columns I need. To do this, I will remove the ‘Demote Headers’ step. I can reapply it before I invoke the function.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-159.jpg)

This means I have the store names in the headings to choose:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-124.jpg)

This gives me the store columns, and I can demote the headers again:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-123.jpg)

**Stores** is ready to use as the Source for **fn\_store**. I go back to **fn\_store**:

![](https://sumproduct.com/wp-content/uploads/2025/05/5df9a796bc6a544983e0fc6deb1d280d.jpg)

I need to provide a column from the **Stores** query.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-101.jpg)

I use **Column1**:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-89.jpg)

Invoking this query will give me a table:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-82.jpg)

I rename this table **Expansion by Store**. I am going to use the **M** code already generated as a basis for this query.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-67.jpg)

I take the **M** code created for **Column1**, and replicate it for 10 columns. I have renamed the steps to make it clear what I am planning. I will rename the final ‘in’ statement when I have finished:

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-59.jpg)

I have created a table for each store; now I just need to append them. The **M** code function to append is **Table.Combine({table1, table2,….})**. I add this line to the **M** code in the Advanced Editor.

![](<Base64-Image-Removed>)

I click ‘Done’ to see the results:

![](<Base64-Image-Removed>)

I have the results in the format I wanted for all stores. I can now ‘Close & Load’. I will choose ‘Close & Load to…’ so that I can load to ‘Connection Only’ to begin with to avoid loading all queries.

![](<Base64-Image-Removed>)

I can then right-click on the queries I want to load, and position them together:

![](<Base64-Image-Removed>)

I load the tables onto a worksheet:

![](<Base64-Image-Removed>)

I check the data types and the report is ready.

![](<Base64-Image-Removed>)

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-6/#0)

[](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-6/#0 "close")

top