# Power Query: Fully Anti M – Part 3

**Source:** https://sumproduct.com/blog/power-query-fully-anti-m-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Fully Anti M – Part 3

*   December 17, 2025

Power Query: Fully Anti M – Part 3
==================================

_Welcome to our Power Query blog.  This week, we look at an **M** code reconciliation method._

For this series on reconciliation, I have both bank and invoice data:

![](https://sumproduct.com/wp-content/uploads/2025/11/image-78.png)

I need to find out if there are any values in the Bank data that are missing from the Invoice data and vice versa.  I have converted my data into two Tables, **Bank** and **Data**, which I have extracted into Power Query:

![](https://sumproduct.com/wp-content/uploads/2025/11/image-79.png)

In [Part 1](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/)
, the method I used was to perform a ‘Left Anti’ join for each query:

![](https://sumproduct.com/wp-content/uploads/2025/11/image-80.png)

I also added a ‘Custom Column’ to determine the source of the rows that were not matched.

![](https://sumproduct.com/wp-content/uploads/2025/11/image-81.png)

I appended the unmatched row queries to achieve the result I required:

![](https://sumproduct.com/wp-content/uploads/2025/11/image-83.png)

[Last week](https://sumproduct.com/blog/power-query-fully-anti-m-part-2/)
, I used another method where I performed a full outer join on **Bank** and **Invoice**.  

![](https://sumproduct.com/wp-content/uploads/2025/11/image-84.png)

I then filtered the data to get similar results.

![](https://sumproduct.com/wp-content/uploads/2025/11/image-85.png)

I promised an **M** code method this week, and it centres on the **M** function **Table.RemoveMatchingRows()**.  Let’s start by looking at the syntax for this function:

> **Table.RemoveMatchingRows(table** as table, **rows** as list, optional **equationCriteria** as any**)** as table

This function removes all occurrences of the specified rows from the **table**.  I will be using the second required parameter **rows**, which is a list containing information about the rows to be removed.  In the current example, this holds the records containing the columns to be compared in the second query.  A record is a row, but it also includes the column name information.  There is another optional parameter **equationCriteria,** which can specify how values are compared.  I will use this parameter to identify the columns to compare in the current query for each record.

I begin by creating a new blank query by right-clicking in the Queries pane and choosing the option from the ‘Other Sources’ on the dropdown menu.

![](<Base64-Image-Removed>)

This gives me the framework for a new query.  I choose to access the ‘Advanced Editor’ from the Home tab:

![](<Base64-Image-Removed>)

I am going to build up the query in steps.  Let’s start by looking at this from the perspective of the **Bank** query:

> **Source = Table.RemoveMatchingRows(Bank,Table.ToRecords(Invoice\[\[First Name\],\[Last Name\],\[Email Address\], \[Amount\]\] ),{“First Name”, “Last Name”, “Email Address”, “Amount”})**

I am using the **Table.RemoveMatchingRows()** function to take the **Bank** query and for each row, specify the column values from the **Invoice** query to create records for comparison.  Finally, I compare that record to the specified columns on in the current **Bank** record.  When I click Done, I can see the results for this step:

![](<Base64-Image-Removed>)

I have called this query **Method 3**.  Now you may be thinking this is the same as the anti join method I used in [Part 1](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/)
.  I could do the same from the perspective of **Invoice** and append them.  However, since the result is a set of records, I can use a different method:

![](<Base64-Image-Removed>)

I am concatenating the rows from the first result to the rows from the second result.  This is a more advanced method, but it is unashamedly sleek:

![](<Base64-Image-Removed>)

Adding a comment is prudent to make the purpose clearer.  If you need a source reminder, you can add a column to one of the queries:

![](<Base64-Image-Removed>)

I have used a reference query which I have called ‘Invoice with Indicator’ because I am using **Invoice** for the other methods.  I will now use the reference query in **Method 3**:

![](<Base64-Image-Removed>)

The results are shown with a new **Invoice** column, indicating the source of the rows.

You should note that there is also another method you can use to achieve a full anti join which uses grouping; I will demonstrate that method next week…

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-fully-anti-m-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fully-anti-m-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fully-anti-m-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fully-anti-m-part-3/#0)

[](https://sumproduct.com/blog/power-query-fully-anti-m-part-3/#0 "close")

top