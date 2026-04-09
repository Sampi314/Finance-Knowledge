# Power Query: Fully Anti M – Part 2

**Source:** https://sumproduct.com/blog/power-query-fully-anti-m-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Fully Anti M – Part 2

*   December 10, 2025

Power Query: Fully Anti M – Part 2
==================================

_Welcome to our Power Query blog.  This week, we look at an alternative reconciliation method._

For this series on reconciliation, I have both bank and invoice data:

![](<Base64-Image-Removed>)

I need to find out if there are any values in the Bank data that are missing from the Invoice data and vice versa.  I have converted my data into two Tables, **Bank** and **Data**, which I have extracted into Power Query:

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/)
, the method I used was to perform a ‘Left Anti’ join for each query:

![](<Base64-Image-Removed>)

I also added a ‘Custom Column’ to determine the source of the rows that were not matched.

![](<Base64-Image-Removed>)

This week, let’s look at another method, which may be quicker for large datasets, particularly if you are extracting data from a database that supports query folding.  Since anti joins did not originally have an equivalent in **SQL**, they interrupted query folding.  Newer versions of Power Query can use query folding for anti joins for some databases and you should consult the latest Microsoft documentation for the most up to date information for your source.

The first step for this method is to perform a full outer join on **Bank** and **Invoice**.  Starting in the **Invoice** query, I choose ‘Merge Queries as New’ from the ‘Merge Queries’ dropdown menu on the Home tab:

![](<Base64-Image-Removed>)

I have chosen a ‘Full Outer’ join, which gives me all rows from both queries.  When I click OK, this gives me a row for all possible values, regardless of whether they are matched:

![](<Base64-Image-Removed>)

I expand the data in the **Bank** column:

![](<Base64-Image-Removed>)

I take the defaults, and for once I will use the original column name as a prefix, since I will have the same column names, and I need to know which source the data has come from.

![](<Base64-Image-Removed>)

I need the rows which have a _null_ value either in the **Bank** columns or in the **Invoice** columns.  I will select those rows where **First Name** or **Bank.First Name** contains a _null_ value.  Note that I know that no names are missing.  If there were a possibility of any first name containing a _null_ value before the merge, I would need to replace any _null_ values before merging.

To filter on two \[2\] columns, I can add a ‘Conditional Column’ from the ‘Add Column’ tab.  If you find this option is greyed out, ensure you don’t have more than one column selected.

![](<Base64-Image-Removed>)

I choose to create a new column **Include**, which is “Y” if either first name contains a _null_ value, otherwise it is “N”.  This gives me a column I can filter on:

![](<Base64-Image-Removed>)

When I filter on **Include** and select the value “Y”, six \[6\] rows are returned.  These are the same values returned [last week’s](https://sumproduct.com/blog/power-query-fully-anti-m-part-1/)
 solution.

![](<Base64-Image-Removed>)

I can tidy this up, but I have all the data I need, including the source.   

For those of you more comfortable with **M** code, notice that the ‘Filtered Rows’ step uses the **Table.SelectRows()** function.  Rather than adding the **Include** column, you could use a customised **Table.SelectRows()** step after expanding the **Bank** column:

![](<Base64-Image-Removed>)

The **M** code for this step is:

> **\= Table.SelectRows(#”Expanded Bank”, each (\[First Name\] = null or \[Bank.First Name\] = null))**

If you like using the **M** code approach, join me next week when I will look at another **M** code method…

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-fully-anti-m-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fully-anti-m-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fully-anti-m-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fully-anti-m-part-2/#0)

[](https://sumproduct.com/blog/power-query-fully-anti-m-part-2/#0 "close")

top