# Power Query: Refreshing Challenges on the Web – Part 1

**Source:** https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Refreshing Challenges on the Web – Part 1

*   January 24, 2023

Power Query: Refreshing Challenges on the Web – Part 1
======================================================

Power Query: Refreshing Challenges on the Web – Part 1
======================================================

25 January 2023

_Welcome to our Power Query blog. This week, I investigate how to refresh queries in Excel for the web._

Please Note: Excel for the web has been enhanced since this blog was written.  To find out more about Excel for the web, please see the [series on Excel for the web.](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/)

This time, let’s take a look at the web-based counterpart of Excel Power Query. Whilst Power Query in Excel for the web is being enhanced, there are still differences in functionality when compared with Excel Power Query offline. This week, I will look at the refresh feature in Excel for the web and how it interacts with queries.

Before I start, I will need to create an Excel file offline that already has the queries I want to use loaded, as Excel for the web currently does not let me create queries (yet!). If I were looking for places to refresh my query, I might assume that the Refresh button on the Data tab would be a good place to start:

![](https://sumproduct.com/wp-content/uploads/2025/05/afb67b0cc4fbecc8fcbb0944b7c49996.jpg)

However, this does not work even if I select all of the refreshable regions; it will return this message box instead:

![](https://sumproduct.com/wp-content/uploads/2025/05/d71a851a92d4534e8eca847b0c8ac392.jpg)

Unfortunately, this Refresh button will only update features like PivotTables. If I want to refresh a query online, I need to use the Queries button on the Data tab (shown on the screenshot earlier). On the right-hand side of the screen, the Queries panel appears:

![](https://sumproduct.com/wp-content/uploads/2025/05/b4a3b19d60d08ad60a0489bc8bb8cd19.jpg)

If I use the button highlighted above, which I will refer to as ‘Refresh All’, most of the queries that have a connection to the workbook will update:

![](https://sumproduct.com/wp-content/uploads/2025/05/0ed0a8ef8ff75fb9694eb2e495f7c38a.jpg)

I can see that the **FilePath** query did not refresh. If I hover the mouse over it, the refresh symbol is greyed out for the **FilePath** query because it is ‘Connection only’. This makes sense, as it is not being loaded to the workbook.

When I press the Refresh symbol for the **PQ\_fromWorkbook** query, which accesses another workbook, the process will fail:

![](<Base64-Image-Removed>)

This message appears:

![](<Base64-Image-Removed>)

Currently, Excel Online only allows the user to refresh data from Table / Range and OData Feed. Therefore, for **PQ\_fromTable\_Range**,I can use refresh successfully, but I cannot use it for **PQ\_fromWorkbook**.

The ‘Refresh All’ button will work as I might expect now I know the limitations: it will refresh all the queries that have a source from Table / Range within the Workbook. However, it will issue an error if I have a query from a source that Excel Online does not currently support.

The ‘Refresh All’ button will work in the Viewing mode of Excel online, which is equivalent to the Read-Only mode of Excel Offline. However, the Queries button will not. Thus, in order to view the Queries panel, I must open it in the Editing mode of Excel online and then change to Viewing mode. I can then access the refresh option for each query or use the ‘Refresh All’ option.

Next time, I will look at an example where I have queries and PivotTables, to see how refreshing affects the results.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/#0)

[](https://sumproduct.com/blog/power-query-refreshing-challenges-on-the-web-part-1/#0 "close")

top