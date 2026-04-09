# Power Query: Workbook Parameter Table Tip Part 1

**Source:** https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Workbook Parameter Table Tip Part 1

*   September 10, 2025

Power Query: Workbook Parameter Table Tip Part 1
================================================

_Welcome to our Power Query blog.  This week, I describe how to use a parameter from an Excel Table of parameter data in an Excel workbook._

During training, attendees often ask how to use parameters to make their Power Query reports more flexible.  I have covered parameters in detail in the past, most recently in the [Split Folder series](https://sumproduct.com/blog/split-folder-part-1/)
.  [Last week](https://sumproduct.com/uncategorized/power-query-workbook-parameter-tip/)
, I looked at how to add a single parameter to your report.  I took an existing report and added a parameter to the process.

The data for the report is held in an Excel workbook called **Parameter Source**.

![](https://sumproduct.com/wp-content/uploads/2025/09/image-78.png)

The report created from this data is in another Excel workbook called **Parameter Report**.

![](https://sumproduct.com/wp-content/uploads/2025/09/image-80.png)

There are two \[2\] queries, called **Itinerary** and **Source File**.  **Itinerary** contains the steps to transform the data into the required format for the report:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-81.png)

The Source step for this query is the **Source File** query:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-82.png)

The **Source File** query accesses the data from the **Parameter Source** workbook and performs some simple transformations:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-83.png)

The Source step of this query is accessing the **Parameter Source** workbook.

![](https://sumproduct.com/wp-content/uploads/2025/09/image-84.png)

[Last week](https://sumproduct.com/uncategorized/power-query-workbook-parameter-tip/)
, I changed this to use a parameter in the workbook instead:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-86.png)

I created a named range for cell **C1** by entering the name “**P\_File\_Location**” in the name box and extracted the named range to Power Query.  After a few simple transformations, I replaced the location string with the parameter **P\_File\_Location**:

![](<Base64-Image-Removed>)

I filter the **Salesperson** column so that only data associated with the value “Mary” is selected.

![](<Base64-Image-Removed>)

I need another parameter for the **Salesperson** that I want to see the itinerary for.  I could create another named range in the Excel workbook, but I may add other parameters and I would like a more flexible solution.

I ‘Close & Load’ from the Home tab to save my change to **Source File**.  Since I may add more parameters, I enter the data on a new sheet called Parameters.  I enter the parameter names in a column under a heading “Parameter” and the parameter values in a column under a heading “Value”, _viz._

![](<Base64-Image-Removed>)

The next step is to insert this data into a Table.  I must select either one cell in the data or the whole dataset.  To create the Table, I may choose Insert Table from the  Insert tab or use the keyboard shortcut **CTRL + T**:

![](<Base64-Image-Removed>)

In the ‘Create Table’ dialog, I check the data location is correct and indicate that ‘My table has headers’.  I rename the table to “Parameters” in the ‘Table Name’ box accessible in the ‘Table Design’ tab:

![](<Base64-Image-Removed>)

I right-click from within the Table and choose to ‘Get Data from Table /Range’.

![](<Base64-Image-Removed>)

Next time, I will look at how to extract a parameter from the **Parameters** query.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/#0)

[](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/#0 "close")

top