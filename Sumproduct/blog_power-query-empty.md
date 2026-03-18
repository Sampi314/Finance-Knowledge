# Power Query: Empty

**Source:** https://sumproduct.com/blog/power-query-empty/

---

[Home](https://sumproduct.com/)

\> Power Query: Empty

*   March 10, 2020

Power Query: Empty
==================

Power Query: Empty
==================

11 March 2020

_Welcome to our Power Query blog. This week, I look at how to achieve the opposite of fill up / down._

Maureen is in charge of my imaginary salespeople. She has been looking at the following data and she has a request…

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-257-1.jpg)

Maureen doesn’t want to see the salesperson’s name on each row, she wants to only see it on the first row for that salesperson. She’s not interested in PivotTables!

I begin by extracting the data to Power Query using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-257-1.jpg)

Since I want to essentially split my data into groups under each name, I start by sorting by name using the filter next to **Name**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-242-1.jpg)

Having ordered by data, I need to group it. I can do this using ‘Group by’ on the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-218-1.jpg)

I include a simple aggregation to count all rows:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-189-1.jpg)

_I click OK to see my grouping._

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-167-1.jpg)

I now need a method of linking all the rows with the same name, so I use an index column. I want to effectively add an index column to each table in **Name\_Count** so I do this by adding a ‘Custom Column’ from the ‘Add Column’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-143-1.jpg)

The **M** code I have used is:

**\= Table.AddIndexColumn(\[Name\_Count\],”Row”,1,1)**

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-115-1.jpg)

I can see that all my information is in my new **Custom** column, so I can remove the other columns by selecting **Custom**, right-clicking and choosing ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

I can now expand my column.

![](<Base64-Image-Removed>)

I am almost there. I only need to show the value in **Name** if **Row** is one (1). There are several ways to do this, but I will add a ‘Conditional Column’:

![](<Base64-Image-Removed>)

I click OK to view my data.

![](<Base64-Image-Removed>)

Now I can remove the original **Name**, rename my new column and remove the **Row** column I created to help me achieve my goal.

![](<Base64-Image-Removed>)

I have also reordered my columns to resemble the original table. I ‘Close & Load’ to Excel from the Home tab.

![](<Base64-Image-Removed>)

I have emptied the other cells in the column so that the data is formatted for Maureen.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-empty/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-empty/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-empty/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-empty/#0)

[](https://sumproduct.com/blog/power-query-empty/#0 "close")

top