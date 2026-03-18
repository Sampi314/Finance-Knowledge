# Power Query: Join or List – Part 2

**Source:** https://sumproduct.com/blog/power-query-join-or-list-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Join or List – Part 2

*   December 6, 2022

Power Query: Join or List – Part 2
==================================

Power Query: Join or List – Part 2
==================================

7 December 2022

_Welcome to our Power Query blog. This week, I continue comparing alternative approaches to extracting data from another table._

I know you’ve missed them: my imaginary salespeople are back! They are going to help me compare alternative approaches to pulling in data from one query to another, namely merging and using list functions. There are two examples that I am going to use in this series. The first example, and the simplest, is **exact** matching. Later in the series I will also look at **approximate** matching.

I have two tables. The first is a list of item types that my salespeople have been putting under ‘Personal’ on expenses. The second is a list indicating which are allowed and which are not, and any that require further information.

![](<Base64-Image-Removed>)

I extracted both sets of data into Power Query by using the ‘From Table/Range’ option in the ‘Get & Transform’ section of the Data tab, one set at a time:

![](<Base64-Image-Removed>)

To begin with, I chose to ‘Close & Load To’ from the Home tab in the Power Query editor to trigger the ‘Import Data’ dialog:

![](<Base64-Image-Removed>)

I chose to ‘Only Create Connection’, and loaded the other set of data:

![](<Base64-Image-Removed>)

This gave me two queries, which I renamed to **Expenses** and **Permissions**.

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
, I merged the queries to get the following result:

![](<Base64-Image-Removed>)

This time, I will use the **List** functions to achieve the same result. Of course **Expenses** and **Permissions** are tables, not lists, but each column in those tables can be thought of as a list.

This approach is similar to using **VLOOKUP** (or as Liam would prefer, **INDEX MATCH**) in Excel _(actually, Liam would even prefer using a cheese grater to scratch an itch – Ed.)_. I am going to create a column in **Expenses** which looks up the **Expense** on **Permissions** and returns the data in **Column2**.

I start with a new query of the expense data (since [last week](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
 I added a new column to **Expenses**). This query is called **ExpensesList**.

![](<Base64-Image-Removed>)

This time, I am going to add a new ‘Custom Column’ to **ExpensesList** using the option on the ‘Add Column’ tab. I can use Intellisense to help me create the **M** code:

![](<Base64-Image-Removed>)

The column I have created will locate the matching **Expense** on **Permissions**.

![](<Base64-Image-Removed>)

The **M** code is:

**\= List.PositionOf(Permissions\[Expense\],  
\[Expense\])**

**List.PositionOf()** has the following syntax:

List.PositionOf(**list** as list, **value** as any, optional **occurrence** as nullable number, optional **equationCriteria** as any) as any.

This returns the offset at which the **value** appears in the **list**, or returns -1 if the **value** doesn’t appear. An optional **occurrence** parameter can be specified to determine the maximum number of occurrences to report.

This gives me the following results:

![](<Base64-Image-Removed>)

Now, I have the index, I need to bring the data in using that index. I create another ‘Custom Column’:

![](<Base64-Image-Removed>)

The **M** code is:

**\= Permissions\[Column2\]{\[Permissions Index\]}**

This is extracting the information from **Column2** at the position indicated by **Permissions Index**. This gives me my result:

![](<Base64-Image-Removed>)

I can remove **Permissions Index** as I don’t need it in my final table, and change the data type of **Allowed to Claim?** to text. Note that I could have combined the **M** code for the two Custom columns into one step:

**\= Permissions\[Column2\]{ List.PositionOf(Permissions\[Expense\],  
\[Expense\])}**

I stepped it out here to make it easier to follow.

Now I can see that the results are the same:

![](<Base64-Image-Removed>)

Note that for **ExpensesList** the dates have remained in chronological order. I can do the same for the **Expenses** query by buffering the **Expenses** table before extracting the data from the merged table:

![](<Base64-Image-Removed>)

To do this, I have changed the ‘Expanded Permissions’ step:

![](<Base64-Image-Removed>)

The **M** code is now:

**\=  
Table.ExpandTableColumn(Table.Buffer(#”Merged Queries”),  
“Permissions”, {“Column2”},  
{“Permissions.Column2”})**

By using **Table.Buffer()**, I have preserved the order from the previous step, ‘Merged Queries’. Now the results are identical!

Next time, I’ll look at an example with an approximate match.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-join-or-list-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-join-or-list-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-join-or-list-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-join-or-list-part-2/#0)

[](https://sumproduct.com/blog/power-query-join-or-list-part-2/#0 "close")

top