# Power Query: Reconcilable Differences

**Source:** https://sumproduct.com/blog/power-query-reconcilable-differences/

---

[Home](https://sumproduct.com/)

\> Power Query: Reconcilable Differences

*   January 21, 2020

Power Query: Reconcilable Differences
=====================================

Power Query: Reconcilable Differences
=====================================

22 January 2020

_Welcome to our Power Query blog. This week, we look at a common problem in Finance – performing that pesky bank reconciliation!_

Imagine you had two data sets – it could be your bank statement and a spreadsheet – and you wanted to perform a reconciliation. Here, let’s have ‘Revenues’ and ‘Costs’ data:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-286.jpg)

Do you see both use a five-digit code number? I want to see which items do not reconcile. Yes, this could be performed with **COUNTIF** formulae in Excel, but again, manual manipulation is required.

An alternative is to both merge and then append queries:

*   **Merging** is when columns from one table are added to another (this requires a column that can be used to identify which rows match)
*   **Appending** is when rows from one table are added to another (this requires the tables to share the same column names).

The first thing is to import both tables into Power Query.  I also sort the data into **Code** order. I may then select one of the tables (say **Revenues**) and then click on the Merge dropdown on the Home tab and choose to  ‘Merge Queries as New’ (to generate a new query, rather than merge with the current one).

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-291-1.jpg)

This gives rise to the Merge dialog box, where the two tables and matching columns may be selected:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-275.jpg)

There are several join kinds _(pictured above)_; the one required is the ‘Left Anti’ (“left” is the top table and “right” is the bottom one). This creates a table where records in the top table do not have a corresponding item in the second table (_i.e._ cannot be reconciled). I click OK:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-248-1.jpg)

Notice the final column, **Sorted Costs** says ‘Table’ (in green). This is each empty **Sorted Costs** row, since I have selected a Left Anti join, which selects those **Sorted Revenue** rows that don’t reconcile. If I select the expand icon in the heading of the **Sorted Costs** column, I can prove that the values in **Sorted Costs** are _null_.

![](<Base64-Image-Removed>)

I have the first part of the answer, i.e. the revenues that don’t reconcile. I can repeat this entire process starting from **Sorted Revenues** again, but this time I pick the ‘Right Anti’ join where I get rows in the second table that can not be found in the first.

I can use ‘Append Queries as New’ from the Home tab to join the unreconciled data from both data sets.  I sort the new query by **Code** and load the data to the workbook:

![](<Base64-Image-Removed>)

This might be an involved process but with Power Query, it only ever has to be performed once – refreshing is all that’s required for future reconciliations. Tedious bank reconciliation tasks will become a thing of the past!

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-reconcilable-differences/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-reconcilable-differences/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-reconcilable-differences/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-reconcilable-differences/#0)

[](https://sumproduct.com/blog/power-query-reconcilable-differences/#0 "close")

top