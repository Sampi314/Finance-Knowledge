# Power Query: Refreshing Challenges on the Web – Part 2

**Source:** https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Refreshing Challenges on the Web – Part 2

*   January 31, 2023

Power Query: Refreshing Challenges on the Web – Part 2
======================================================

Power Query: Refreshing Challenges on the Web – Part 2
======================================================

1 February 2023

_Welcome to our Power Query blog. This week,_ _I continue investigating refreshing queries in Excel for the Web by looking at an example with a query and a PivotTable._

Please Note: Excel for the web has been enhanced since this blog was written.  To find out more about Excel for the web, please see the [series on Excel for the web.](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/)

[Last time](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/)
, I looked at the web-based counterpart of Excel Power Query. I looked at the Refresh feature in Excel for the web and how it interacts with queries. I learned that the Refresh button on the Data tab does not update queries:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

If I want to refresh a query online, I need to use the Queries button on the Data tab (shown on the screenshot earlier). On the right-hand side of the screen, the Queries panel appears:

![](<Base64-Image-Removed>)

If I use the button highlighted above, which I will refer to as ‘Refresh All’, most of the queries that have a connection to the workbook will update:

![](<Base64-Image-Removed>)

I can see that the **FilePath** query did not refresh because it is ‘Connection only’. The **PQ\_fromWorkbook** query, which accesses another workbook, didn’t refresh either:

![](<Base64-Image-Removed>)

This message appeared:

![](<Base64-Image-Removed>)

The ‘Refresh All’ button refreshed all the queries that have a source from Table / Range within the Workbook. However, it issued an error because the queries are from sources that Excel Online does not currently support.

This time, I look at an example where I have a query and a PivotTable to see how refreshing affects the results. I will create a PivotTable from the table **PQ\_fromTable\_Range**. I select the data in the table, and on the Insert tab I select PivotTable. A pane appears on the right of the screen:

![](<Base64-Image-Removed>)

I create the following PivotTable:

![](<Base64-Image-Removed>)

I go to the source table (_i.e._ the source of the query) and add one \[1\] more customer here with details as shown:

![](<Base64-Image-Removed>)

When I use the ‘Refresh All’ button on the Data tab once, the table **PQ\_fromTable\_Range** is updated (so the query is updated), but the PivotTable is not. To update the PivotTable, I need to use the ‘Refresh All’ button again:

![](<Base64-Image-Removed>)

This implies that ‘Refresh All’ will update the query _after_ it updates the PivotTable. At the point the PivotTable is updated, the query does not have the extra row. Once the extra row is on the query, then refreshing again updates the PivotTable. I need to be careful when I refresh data in Excel for the web!

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-2/#0)

[](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-2/#0 "close")

top