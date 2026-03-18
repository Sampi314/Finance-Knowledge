# Power Query: Keeping it Current – Part 3

**Source:** https://sumproduct.com/blog/power-query-keeping-it-current-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Keeping it Current – Part 3

*   July 19, 2022

Power Query: Keeping it Current – Part 3
========================================

Power Query: Keeping it Current – Part 3
========================================

20 July 2022

_Welcome to our Power Query blog. This week, I complete the query to look for data in the current workbook._

In [Power Query: Sheets Ahead – Part 1](https://sumproduct.com/blog/power-query-sheets-ahead-part-1/)
, I uploaded data from multiple sheets into another workbook. I had some simple monthly data:

![](https://sumproduct.com/wp-content/uploads/2025/05/829ca9de49c71caea81adc130ba56eca.jpg)

This sheet is for January; I had a similar sheet in the same workbook for February:

![](https://sumproduct.com/wp-content/uploads/2025/05/6da87bd0cbdcd279e723d6b4119c5455.jpg)

I created a query that not only concatenated this data, but also included the sheets for other months as they appeared if I refreshed it. This query was in a separate external workbook:

![](https://sumproduct.com/wp-content/uploads/2025/05/2ee68679436ccd64e7e7ebe9389da5ec.jpg)

[Last week](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/)
, I amended a copy of this query in the original workbook containing the source data.

![](https://sumproduct.com/wp-content/uploads/2025/05/8413d0b23fec08493c49a058d327eeed.jpg)

However, I have an issue with accessing data from within the workbook: I can see the tables (and Named Ranges) but not data on the sheets.

[Last week](https://sumproduct.com/blog/power-query-keeping-it-current-part-2/)
, I received access errors treating this workbook as an external file by using **Excel.Workbook()**. Now, I can’t see data that is not in a Table or a Named Range now that I am using **Excel.Current.Workbook()**. Therefore, I need to amend the data. If the data is likely to be added to, then converting each month’s data to a Table is a good idea.

In the Excel, I use **CTRL + T** (**Insert -> Table**) to convert each sheet to a Table, making sure I am in a cell within the data when I do this:

![](https://sumproduct.com/wp-content/uploads/2025/05/8717aa8e9dd6080309c1c3d2b27281a0.jpg)

I rename the Tables to make them easier to identify, though the names will not be referenced by the query.

![](https://sumproduct.com/wp-content/uploads/2025/05/48d5b6e94d69b643acb3ea3b0c0064a3.jpg)

I repeat this for each month and go back to the **Monthly Sales** query:

![](<Base64-Image-Removed>)

I can see the data now. You should note that if there were Excel Tables or Named Ranges which should not be included in the query, I could filter here on **Name** to remove the data that should be excluded. This is not a problem in my example, but I have another issue to address. This step gives different results to the Source step in the external version of the query. In particular, the data is now in the **Content** column rather than the **Data** column:

![](<Base64-Image-Removed>)

I will need to change the steps that expand the data. I remove the ‘Removed Other Columns’ and ‘Expanded Data’ steps, and expand the data in **Content**. I ignore any warnings about deleting and inserting steps:

![](<Base64-Image-Removed>)

As the data was already in Excel Tables, I do not need to promote the headers this time, so I can delete the ‘Promoted Headers’ step. I do need to remove any duplicate rows, as the results of the query will be in the same workbook.

![](<Base64-Image-Removed>)

The data can now be loaded to the Excel workbook using the ‘Close & Load’ option from the Home tab:

![](<Base64-Image-Removed>)

The data appears in the same workbook:

![](<Base64-Image-Removed>)

The final test is to add another tab for April – which must also be a Table.

![](<Base64-Image-Removed>)

The new data is picked up when I refresh.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-keeping-it-current-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-keeping-it-current-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-keeping-it-current-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-keeping-it-current-part-3/#0)

[](https://sumproduct.com/blog/power-query-keeping-it-current-part-3/#0 "close")

top