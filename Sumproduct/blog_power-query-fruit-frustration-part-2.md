# Power Query: Fruit Frustration – Part 2

**Source:** https://sumproduct.com/blog/power-query-fruit-frustration-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Fruit Frustration – Part 2

*   August 31, 2021

Power Query: Fruit Frustration – Part 2
=======================================

Power Query: Fruit Frustration – Part 2
=======================================

1 September 2021

_Welcome to our Power Query blog. This week, I explain the problems when changing steps._

[Last week](https://sumproduct.com/blog/power-query-fruit-frustration-part-1/)
 I asked a question. I had created a query to extract data from an Excel Workbook.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-137.jpg)

I had then compared the data extracted to the source:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-185.jpg)

When I looked again at my query, although I hadn’t changed it, I had a fetching red line under the columns? Why?

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-149.jpg)

The answer becomes apparent if I refresh the data:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-146.jpg)

I can’t have the source file open while I am accessing it in Power Query. Even more annoying, I can’t close the source Excel Workbook while I have my query open! This is linked to the rule that if I have Power Query open, I can’t do anything in Excel anywhere on the same computer.

**Please Note**: since this blog was written, it is now possible to extract and refresh data from an open source file in some versions of Excel. To get the latest version of the data you must make sure the source file has been saved prior to the extraction or refresh.

Once I have closed the source, the error may persist, in which case I must refresh the data again.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-120.jpg)

Having resolved that issue, I am left with the problem I had when I changed a step in my query. I changed the ‘Filtered Rows’ step to pick Oranges instead of Apples:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-104.jpg)

The data in my ‘Expanded Data’ step was missing an orange.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-95.jpg)

Oh my darling, no clementine. The reason is that Power Query is great at changing steps, but it has some weaknesses. One of these is column names. If I take a closer look at the ‘Expanded Data’ step:

**\= Table.ExpandTableColumn(#”Removed Other Columns”, “Data”, {“1”, “2”, “3”}, {“1”, “2”, “3”})**

This is telling me that Columns from the **Data** table in the table “Remove Other Columns” are being extracted. The column names in the **Data** table are **1**,**2** and **3**, and these columns are being extracted to columns **1**, **2** and **3** in the query. However, if I look at the gear icon next to ‘Expanded Data’

![](<Base64-Image-Removed>)

I can see that there is a Column **4**, which I may select.

![](<Base64-Image-Removed>)

The **M** code for this step is now:

**\= Table.ExpandTableColumn(#”Removed Other Columns”, “Data”, {“1”, “2”, “3”, “4”}, {“1”, “2”, “3”, “4”})**

This now extracts Column **4** successfully. Therefore, although it may be tempting to change steps to save time, it’s important to check the results, especially where column names are concerned.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fruit-frustration-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fruit-frustration-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fruit-frustration-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fruit-frustration-part-2/#0)

[](https://sumproduct.com/blog/power-query-fruit-frustration-part-2/#0 "close")

top