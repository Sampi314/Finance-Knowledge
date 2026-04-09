# Power Query: Keeping it Current – Part 2

**Source:** https://sumproduct.com/blog/power-query-keeping-it-current-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Keeping it Current – Part 2

*   July 12, 2022

Power Query: Keeping it Current – Part 2
========================================

Power Query: Keeping it Current – Part 2
========================================

13 July 2022

_Welcome to our Power Query blog. This week, I start to convert the query to look for data in the current workbook._

In [Power Query: Sheets Ahead – Part 1](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/)
, I uploaded data from multiple sheets into another workbook. I had some simple monthly data:

![](https://sumproduct.com/wp-content/uploads/2025/05/3249abeb14f353251598037c379f8cd0.jpg)

This sheet is for January; I had a similar sheet in the same workbook for February:

![](https://sumproduct.com/wp-content/uploads/2025/05/9df3164243f5c90afb4410bb5ef15f65.jpg)

I created a query that not only concatenated this data, but also included the sheets for other months as they appeared if I refreshed it. This query was in a separate workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/d5316f5de32001c015e0e99822625645.jpg)

[Last week](https://sumproduct.com/blog/power-query-keeping-it-current-part-1/)
, I copied this query to the original workbook containing the source data:

![](https://sumproduct.com/wp-content/uploads/2025/05/b46349a2f25e1f7d22fa8240effcfbe2.jpg)

The message is telling me the query can’t access the workbook because I have it open. This is true since it is this workbook. However, I have the **M** code, and this week, I will change it to point to the current workbook.

I close the error dialog and right-click on the **Monthly Sales** query, so that I may Edit:

![](https://sumproduct.com/wp-content/uploads/2025/05/f6984742529e5eb329a84efcaee2d9a0.jpg)

This takes me to the Power Query editor, where I select the first step (Source).

![](https://sumproduct.com/wp-content/uploads/2025/05/40baef84d3d3a43a26ad9a6e55cc2d27.jpg)

The **M** code for this step is:

**\=  
Excel.Workbook(File.Contents(“C:UserskathrOneDriveDocumentsSUMPRODUCTPQ  
BlogPQ blog 279 and 280 Sheets Ahead.xlsm”), null, true)**

Instead of pointing at an external workbook, I need to change this to use the current workbook.

I can use Intellisense to help me here. If I delete ‘**Excel.Workbook’** and start typing, I can see the following available functions:

![](<Base64-Image-Removed>)

Therefore, instead of **Excel.Workbook()**, I can use **Excel.CurrentWorkbook()**.

![](<Base64-Image-Removed>)

Since I have a location, I don’t need the parameters, so I may delete them. Note that the **Expression.Error** dialog tells me that no arguments are required.

![](<Base64-Image-Removed>)

Here, I have the current issue with accessing data from within the workbook: I can see the tables (and Named Ranges) but not data on the sheets.

Next time, I will adapt the query and the data to get the results I need.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/#0)

[](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/#0 "close")

top