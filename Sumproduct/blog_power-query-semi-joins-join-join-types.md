# Power Query: Semi joins join join types

**Source:** https://sumproduct.com/blog/power-query-semi-joins-join-join-types/

---

[Home](https://sumproduct.com/)

\> Power Query: Semi joins join join types

*   December 31, 2025

Power Query: Semi joins join join types
=======================================

_Welcome to our Power Query blog.  This week, we welcome the new join types to Power Query with an example of when to use the left semi join._

Semi joins are similar to an Inner join, but with one important difference.  When I use a left semi join, I only get the data that is on the first (‘Left’) query.  Let’s look at an example where we don’t need the data from the second query.  Consider the following data:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-14.png)

I have a Table called **Client\_List** which summarises which clients each salesperson has been working with.  I need to know which of these combinations have resulted in at least one \[1\] order.  There are 100 combinations.  I also have another Table called **Orders** which contains the orders I wish to check against:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-15.png)

There are 10,000 orders.

I extract both Tables to Power Query by right-clicking anywhere in the Table and choosing to ‘Get Data from Table/Range’.  I create ‘Connection Only’ queries for each Table:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-16.png)

In the Power Query Editor, I access the **Client\_List** query and choose to ‘Merge Queries as New’ from the ‘Merge Queries’ dropdown menu.

![](https://sumproduct.com/wp-content/uploads/2025/12/image-17.png)

Using the default ‘Left Outer’ join, I can see that 81 of the combinations have been successful.  I need to find out which 81 have been successful.  There are six \[6\] join types available to me on the User Interface (UI).

![](https://sumproduct.com/wp-content/uploads/2025/12/image-18.png)

Note that I cannot select a left semi join here (yet).  The best option I have is an Inner join, since that will give me the matching rows.  In this example, I must make sure the first query in the merge is the one I am checking.

![](<Base64-Image-Removed>)

This matches 81 rows from the **Client\_List** query, but it is also checking and loading 8,284 rows from the **Orders** query!  This number also indicates another issue, which I will cover in a moment.

I click OK, which creates a **Merge1** query consisting of the matching rows and the columns from **Client\_List** and a new column called **Orders**. 

![](https://sumproduct.com/wp-content/uploads/2025/12/image-21.png)

The Tables in the **Orders** column contain the **Orders** rows, which I could extract for a different scenario, but here I only need to know they exist.  It would be more efficient not to load these rows.  I can delete the **Orders** column and get my answer.  However, let’s first look more closely at the code in the Source step:

> **\= Table.NestedJoin(Client\_List, {“Salesperson”, “Client”}, Orders, {“Salesperson”, “Client”}, “Orders”, JoinKind.Inner)**

Are you ready for the huge change to the **M** code I need to make to avoid loading the **Orders** rows to the Tables in the **Orders** column?

> **\= Table.NestedJoin(Client\_List, {“Salesperson”, “Client”}, Orders, {“Salesperson”, “Client”}, “Orders”, JoinKind.LeftSemi)**

I don’t even need to know how to spell it!

![](https://sumproduct.com/wp-content/uploads/2025/12/image-22.png)

When I commit the change, I have the same data from **Client\_List**, but the **Orders** column contains empty Tables:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-24.png)

I can delete the **Orders** column to get the list of successful combinations.  That is, I have most of them.  As I pointed out when I tried the Inner join, the number of **Orders** matched indicated a problem.  The point here is that I wouldn’t have been alerted to this if I had created the source step myself and started with a left semi join, or if I had started with **Orders** and selected a right-semi join.  There is another issue too.  The cog next to the Source step is available, but if you try to use it to change any columns when you are using a semi join you will encounter an error.

![](<Base64-Image-Removed>)

Not pretty.  If you use the left or right semi joins you will need to make any changes via the **M** code and not the UI (for now at least).  

Let’s end by finding out who has been completing orders for other salespeople’s clients.  In the **Orders** query, I choose to ‘Merge Queries as New’ with **Client\_List**, and use a ‘Left Anti’ join to see which combinations are missing:

![](<Base64-Image-Removed>)

The culprits are…

![](<Base64-Image-Removed>)

Mary is clearly the ringleader!

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-semi-joins-join-join-types/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-semi-joins-join-join-types/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-semi-joins-join-join-types/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-semi-joins-join-join-types/#0)

[](https://sumproduct.com/blog/power-query-semi-joins-join-join-types/#0 "close")

top