# Power Query: Fully Anti M – Part 1

**Source:** https://sumproduct.com/blog/power-query-fully-anti-m-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Fully Anti M – Part 1

*   December 3, 2025

Power Query: Fully Anti M – Part 1
==================================

_Welcome to our Power Query blog.  This week, we look at reconciliation methods._

This week, I have both bank and invoice data:

![](<Base64-Image-Removed>)

I need to find out if there are any values in the Bank data that are missing from the Invoice data and vice versa.  I begin by converting my data into two Tables, **Bank** and **Data**.  I select a single cell within the invoice data and use **CTRL + T** to insert a Table:

![](<Base64-Image-Removed>)

I accept the defaults and ensure that I name the Table:

![](<Base64-Image-Removed>)

I repeat this process for the **Bank** data:

![](<Base64-Image-Removed>)

I select any cell in the **Invoice** Table, and right-click to access the option to ‘Get Data from Table / Range’:

![](<Base64-Image-Removed>)

This extracts the Table into a query:

![](<Base64-Image-Removed>)

I ‘Close & Load To…’ and create a Connection Only query.

![](<Base64-Image-Removed>)

I repeat this process for the **Bank** Table:

![](<Base64-Image-Removed>)

I can now use ‘Merge Queries as New’ from the ‘Merge Queries’ dropdown in the Combine section on the Home tab.

![](<Base64-Image-Removed>)

I am going to select the all the columns on each of the tables and perform a ‘Left Anti’ join.  This will give me the rows that are only in **Bank**.

![](<Base64-Image-Removed>)

Note that I must select the columns in the same order on each Table.  Since 94 of 97 rows are excluded, I expect to get three \[3\] rows:

![](<Base64-Image-Removed>)

The new query contains the rows and columns from the **Bank** query and a new **Invoice** column, which is empty, as shown in the previous image.  The **Invoice** column represents the missing data in the **Invoice** query.  I delete this column and add a ‘Custom Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

This new column will indicate the source of the rows that are not in both queries, in this case “Bank”.

![](<Base64-Image-Removed>)

I change the data type of **Source** to Text.  I can do this by using the dropdown accessed from the ‘Data Type’ icon to the left of the heading “Source”.  I rename the query **Unreconciled**.

![](<Base64-Image-Removed>)

Now I need the rows from the **Invoice** Table that do not exist in the **Bank** Table.  I repeat the process starting from the **Invoice** query and I give the **Source** column the value “Invoice”.  I will not be keeping the name of the query, so I don’t need to rename it.

![](<Base64-Image-Removed>)

Now to add these rows to the **Unreconciled** query.  Beginning from the **Unreconciled** query, I ‘Append Queries’ from the Combine section of the Home tab:

![](<Base64-Image-Removed>)

When I click OK, I have the information I need:

![](<Base64-Image-Removed>)

Whilst this method is easy to follow, there are other ways to achieve this result which may be quicker if you have large datasets to compare.  I will look at another method next week.

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/#0)

[](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/#0 "close")

top