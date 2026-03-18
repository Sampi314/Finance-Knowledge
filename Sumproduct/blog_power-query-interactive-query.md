# Power Query: Interactive Query

**Source:** https://sumproduct.com/blog/power-query-interactive-query/

---

[Home](https://sumproduct.com/)

\> Power Query: Interactive Query

*   April 9, 2019

Power Query: Interactive Query
==============================

Power Query: Interactive Query
==============================

10 April 2019

_Welcome to our Power Query blog. This week, I look at how to make a functional query more interactive._

Last week, I created a query that could receive date parameters.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-454.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-468.jpg)

This week, I amend my query so that it’s more flexible for users by allowing the parameters to come from the worksheet. The first step is to put the dates into the worksheet:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-439.jpg)

I don’t need to worry about making this a Table, as when I extract this information using ‘From Table’ in the ‘Get & Transform’ section on the ‘Data’ tab, Power Query will automatically convert it to a Table. Having said that, it’s a good practice to convert to a Table first, as you get to choose the name of the Table before importing.

Having said that, let’s pretend I ignored my advice:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-407.jpg)

I confirm the defaults to extract the information to Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-345.jpg)

Now I need to connect these parameters to the query I created last week, ‘Expenses\_Folder’. To do this, I create a new custom column from the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-301.jpg)

Since ‘Expenses\_Folder’ is a function, I can use the **M** code

**\= Expenses\_Folder(\[datefrom\], \[dateto\])**

which calls my original query as a function, using the dates in the columns in my current query.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-254.jpg)

The content of my new column is a Table. I can use the ‘Expand’ icon next to the title of the column to view the contents of that Table.

![](<Base64-Image-Removed>)

As usual, I don’t want to use the original column name as a prefix (that would make for very long column names!). I select all columns in the Table and choose to expand.

![](<Base64-Image-Removed>)

All the data from my original expenses information is shown where the date falls into the range I have specified. I remove the **_datefrom_** and **_dateto_** columns and save the query by using ‘Close & Load’ from the ‘File’ tab.

![](<Base64-Image-Removed>)

I have renamed my new query ‘Interactive Expenses\_Folder’.

If I go back to the original data worksheet, I can change the dates and see what happens to my query.

![](<Base64-Image-Removed>)

Once ‘Interactive Expense\_Folder’ is refreshed, I can see that the expenses from May are displayed.

![](<Base64-Image-Removed>)

This is a quick and easy way to reduce the amount of data that I have to deal with.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-interactive-query/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-interactive-query/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-interactive-query/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-interactive-query/#0)

[](https://sumproduct.com/blog/power-query-interactive-query/#0 "close")

top