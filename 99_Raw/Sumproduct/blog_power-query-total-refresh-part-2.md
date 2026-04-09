# Power Query: Total Refresh – Part 2

**Source:** https://sumproduct.com/blog/power-query-total-refresh-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Total Refresh – Part 2

*   April 11, 2023

Power Query: Total Refresh – Part 2
===================================

Power Query: Total Refresh – Part 2
===================================

12 April 2023

_Welcome to our Power Query blog. This week, I look at how PivotTables may be created directly from queries._

I have some sales data for my salespeople.

![](<Base64-Image-Removed>)

I have been asked to show this data in a pivoted Table and a PivotTable. [Last week](https://sumproduct.com/blog/power-query-total-refresh-part-1/)
, I created a query **SalesIncreases**.

![](<Base64-Image-Removed>)

I loaded it to the same sheet as the original data and created a PivotTable using the Table **SalesIncreases**.

![](<Base64-Image-Removed>)

However, when I updated the original data and used ‘Refresh All’ from the Data tab, the PivotTable was not initially updated.

![](<Base64-Image-Removed>)

I had to refresh again to get the changes to go through to the PivotTable:

![](<Base64-Image-Removed>)

This week, I am going to remove the need to refresh twice. I right-click on **SalesIncreases** in the Queries tab in the ‘Queries & Connections’ window:

![](<Base64-Image-Removed>)

I choose to create a Reference query, which I call **SalesIncreasesPT**:

![](<Base64-Image-Removed>)

Since this query uses the query **SalesIncreases** as the source, it will be updated after **SalesIncreases** when the ‘Refresh All’ occurs.

I choose to ‘Close & Load To…’ from the Home tab:

![](<Base64-Image-Removed>)

This time, I choose to load to a ‘PivotTable Report’, and I choose to create the PivotTable at cell **F19:**

![](<Base64-Image-Removed>)

Before I change the labels, I will test whether this PivotTable needs to be refreshed twice. Mary’s results for January have changed again, and now the increase is 20. I change the original table:

![](<Base64-Image-Removed>)

I use ‘Refresh All’ from the Data tab:

![](<Base64-Image-Removed>)

The Table **SalesIncreases** updates, but the PivotTable created from the Table has not updated yet.

![](<Base64-Image-Removed>)

However, the PivotTable created directly from the reference query **SalesIncreasesPT** has been updated.

Creating a PivotTable from the query rather than the loaded Table removes the need to refresh twice. If I need to see the output Table and the PivotTable, I can create the PivotTable directly from a reference query. The reference query will be updated if the original query is changed, therefore the Table and the PivotTable will always use the same data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-total-refresh-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-total-refresh-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-total-refresh-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-total-refresh-part-2/#0)

[](https://sumproduct.com/blog/power-query-total-refresh-part-2/#0 "close")

top