# Power Query: Expendable Expand

**Source:** https://sumproduct.com/blog/power-query-expendable-expand/

---

[Home](https://sumproduct.com/)

\> Power Query: Expendable Expand

*   January 17, 2023

Power Query: Expendable Expand
==============================

Power Query: Expendable Expand
==============================

18 January 2023

_Welcome to our Power Query blog. This week, I investigate how to avoid expanding data after merging._

In [Join or List Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
, I merged queries to get all the data I needed in one table. I had two queries, **Expenses** and **Permissions:**

![](https://sumproduct.com/wp-content/uploads/2025/05/004917558011874d4a99997852b2ba3e.jpg)

I merged the tables to find out who has expenses that are not allowed or that require more information. I started in **Expenses**, and I chose ‘Merge Queries’ from the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/1bb4d34548a5315af68a2ebcfc94d889.jpg)

This enabled the ‘Merge Queries’ dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/d9d444d23e15b4fd69e0f008ee71fcf3.jpg)

I matched the data on **Expense**:

![](https://sumproduct.com/wp-content/uploads/2025/05/d911221fe62fc5349bfa4749219aa74f.jpg)

I used the icon in the **Permissions** column to extract the data from the tables:

![](https://sumproduct.com/wp-content/uploads/2025/05/fd1027b093e85f57f1e234dd3579e8d8.jpg)

I only needed the information in **Column2.**

![](https://sumproduct.com/wp-content/uploads/2025/05/bbc26d8f2fdb29a41107b06a92941f25.jpg)

I had the data I needed, and I renamed the column **Allowed to Claim?** However, did I need to expand the data in **Permissions** to achieve this? There is another way I could have extracted the data:

Let’s revisit. I am starting at the ‘Merged Queries’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/161b2beb7c43bd1d8d92c335cdd1ac7b.jpg)

I choose to add a ‘Custom Column’ from the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/6563a370905cb531a2090cbd7c957472.jpg)

I call the new column **Allowed to Claim?**, as above:

![](https://sumproduct.com/wp-content/uploads/2025/05/067dd0884b861fecddf0f0bca8205e8a.jpg)

The **M** code for this is:

**\=  
Table.FirstValue(Table.SelectColumns(\[Permissions\], {“Column2”}))**

This is made up of two steps. Since **Permissions** is a column of tables, the first step is to use **Table.SelectColumns()** to extract only **Column2** from each table. However, **Table.SelectColumns()** will return a table with one value in it. In order to extract the data, I use **Table.FirstValue()** to get the data in the first column and row.

![](<Base64-Image-Removed>)

This merely extracts the data from the column. I could also use table functionality to create columns using conditions that compare the data in the query with the data in the table.

![](<Base64-Image-Removed>)

The **M** code here has been extended to:

**if  
(Table.FirstValue(Table.SelectColumns(\[Permissions\], {“Column2”})) =  
“No”) then “Requires Intervention”**

**else null**

I am creating a new column which contains ‘Requires Intervention’ if the salesperson has tried to claim a restricted item.

![](<Base64-Image-Removed>)

In this case, I have avoided expanding the **Permissions** tables and created a column that uses a condition using the data in **Permissions**. I would of course need to set the data type for my new columns, but this technique can save me from extracting columns that I don’t need to include in the query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-expendable-expand/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-expendable-expand/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-expendable-expand/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-expendable-expand/#0)

[](https://sumproduct.com/blog/power-query-expendable-expand/#0 "close")

top