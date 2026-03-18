# Power Query: Total Refresh – Part 1

**Source:** https://sumproduct.com/blog/power-query-total-refresh-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Total Refresh – Part 1

*   April 4, 2023

Power Query: Total Refresh – Part 1
===================================

Power Query: Total Refresh – Part 1
===================================

5 April 2023

_Welcome to our Power Query blog. This week, I look at PivotTables created from queries._

I have some sales data for my salespeople.

![](<Base64-Image-Removed>)

I have been asked to show this data in a pivoted Table and a PivotTable. I start by extracting the data to Power Query. In the ‘Get & Transform’ section of the Data tab, I use ‘From Table/Range’:

![](<Base64-Image-Removed>)

I take the defaults and click OK. I call the new query **SalesIncreases**.

![](<Base64-Image-Removed>)

Power Query has generated a ‘Changed Type’ step, which I delete, as I am going to be unpivoting the columns. I select **Salesperson**, and on the Transform tab, I select the ‘Unpivot Columns’ dropdown, and then ‘Unpivot Other Columns’:

![](<Base64-Image-Removed>)

This gives me the data in the format I require, and I can rename the columns:

![](<Base64-Image-Removed>)

As I am going to be loading this data to Excel, I change the data types. There are a several ways to do this; I choose to select **Salesperson** and **Amount** and use the ‘Detect Data Type’ option from the ‘Any Column’ section of the Transform tab:

![](<Base64-Image-Removed>)

My data is ready to be loaded:

![](<Base64-Image-Removed>)

I choose the ‘Close & Load To…’ option from the Home tab, so that I can choose where to put the Table:

![](<Base64-Image-Removed>)

As the requirement is for all the data to appear on the same sheet, I choose cell **A9**.

![](<Base64-Image-Removed>)

The next step is to create the PivotTable. I click anywhere in Table **SalesIncreases** and choose PivotTable from the Insert tab:

![](<Base64-Image-Removed>)

I choose ‘From Table/Range’ from the dropdown menu:

![](<Base64-Image-Removed>)

The ‘Table/Range’ defaults to **SalesIncreases**, and I choose to put the PivotTable on the ‘Existing Worksheet’ in cell **F11**:

![](<Base64-Image-Removed>)

I rename the labels and my PivotTable is ready:

![](<Base64-Image-Removed>)

I receive news that Mary’s increase for January has changed to 13. I update the source table:

![](<Base64-Image-Removed>)

I choose ‘Refresh All’ from the Data tab:

![](<Base64-Image-Removed>)

However, this only refreshes table **SalesIncreases** and not the PivotTable (it does change the column widths though):

![](<Base64-Image-Removed>)

Since the Pivot Table is accessing the data from the Table **SalesIncreases**, and the PivotTable is updated before the Table, I must press ‘Refresh All’ again in order to update the data in the PivotTable:

![](<Base64-Image-Removed>)

Next time, I’ll show a way to solve this issue.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-total-refresh-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-total-refresh-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-total-refresh-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-total-refresh-part-1/#0)

[](https://sumproduct.com/blog/power-query-total-refresh-part-1/#0 "close")

top