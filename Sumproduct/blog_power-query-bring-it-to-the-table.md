# Power Query: Bring it to the Table

**Source:** https://sumproduct.com/blog/power-query-bring-it-to-the-table/

---

[Home](https://sumproduct.com/)

\> Power Query: Bring it to the Table

*   October 3, 2017

Power Query: Bring it to the Table
==================================

Power Query: Bring it to the Table
==================================

4 October 2017

Welcome to our Power Query blog. This week I look at how to create a table in M code.

I like finding ways to save time. That’s why I get someone else to write this. So when I come across a method to create data quickly, then that makes me very happy. This particular method of creating data is ideal for those scenarios where I don’t want Excel users to change any values. Since the values are specified in **M** code, the only way to change them is to change the query.

The Microsoft description of the **#table()** function is shown below:

*   **#table**(**columns** as any, **rows** as any) as any
*   Creates a table value from columns (**columns**) and the list (**rows**) where each element of the list is an inner list that contains the column values for a single row; **columns** may be a list of column names, a table type, a number of columns or null.

This all sound very simple…or not. What I need is an example. In an empty workbook (nothing up my sleeves), I elect to create a new, empty query (Blank Query):

![](https://sumproduct.com/wp-content/uploads/2025/05/4f85ad540a13180ccc899835fe9af88c.jpg)

In the Query Editor, I choose the Advanced Editor option from the ‘Home’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/a8533a4da5ab912a699dcc35e063b1fa.jpg)

I begin with something simple: my aim is to create a small table with some basic employee data, none of which is genuine…

![](https://sumproduct.com/wp-content/uploads/2025/05/f89150fc35a88d51c7eeef5214b35a49.jpg)

My **M** code is as follows

**#table({“Employee Surname”, “Employee First Name”}, {{“Smith”, “John”},{“Jones”, “Gareth”},{“Brown”,”Brian”}})**

This means create a table with two columns (these are in a list) **_Employee Surname_** and **_Employee First Name_**_._ Then, the values for each pair of columns are provided three times. Each set of data (surname value and first name value) is grouped into a list and all three pairs are grouped into a larger list. The list is indicated in each case by the use of curly brackets **{ }**. This makes the ‘inner list’ in the description a little clearer, as it just means that I am specifying a list of values for each row, and the rows belong to a list too. I select ‘Done’ to create my table.

![](<Base64-Image-Removed>)

The columns in the example above use text values, but I can use other data types in my columns; it depends what I want to create. I decide to add a start date for my three employees. For this I will use another function, **#date**

*   `**#date(year**` `as number, **month** as number, **day** as number**)** as date`
*   Creates a date value from year (`**year**``)`, month (`**month**``)`, and day (`**day**``)`. Raises an error if these are not true:
    *   1≤ year ≤ 9999
    *   1≤ month ≤ 12
    *   1 ≤ day ≤ 31

This function is easy to follow, so I go back into the Advanced Editor and expand my lists, _viz._

![](<Base64-Image-Removed>)

As the line is getting longer, I organise my **M** code so that I can follow where the lists are constructed to make it easier for me to add to my table. (I covered basic **M** code syntax and how to make it easier to read in [M-Body Personified](https://sumproduct.com/blog/power-query-m-body-personified/)
.

Once I am happy with what I have added, I click ‘Done’.

![](<Base64-Image-Removed>)

Power Query has added my column as type ‘Any’, so I opt to change it to a date. However, I’d really like this to happen when I create my table, rather than adding another step, and there is a way to specify the data type. The syntax is slightly different, as the method of defining the table changes. Instead of using a list of column names,

**#table({“Employee Surname”, “Employee First Name”, “Start Date”}**

I specify the name and type for each column (and the table type) as follows:

**#table(type table \[#”Employee Surname”=text, #”Employee First Name”=text, #”Start Date”=date\]**

I go back to the Advanced Editor and amend my code:

![](<Base64-Image-Removed>)

I choose ‘Done’ to make my changes.

![](<Base64-Image-Removed>)

All my columns in my newly created table have been given the correct type without the need for a ‘Change Type’ step. Easy when you know how…

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-bring-it-to-the-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-bring-it-to-the-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-bring-it-to-the-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-bring-it-to-the-table/#0)

[](https://sumproduct.com/blog/power-query-bring-it-to-the-table/#0 "close")

top