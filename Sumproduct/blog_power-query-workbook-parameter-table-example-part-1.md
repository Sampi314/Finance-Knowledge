# Power Query: Workbook Parameter Table Example Part 1

**Source:** https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Workbook Parameter Table Example Part 1

*   October 1, 2025

Power Query: Workbook Parameter Table Example Part 1
====================================================

_Welcome to our Power Query blog.  This week, I start to look an extended example where a parameter table is useful._

During training, attendees often ask how to use parameters to make their Power Query reports more flexible.  I recently looked at this in two \[2\] blog collections: [Workbook Parameter Tip](https://sumproduct.com/uncategorized/power-query-workbook-parameter-tip/)
 and [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
.  My fictional salespeople can take some well-earned leave since I will be applying the same method to a much larger dataset.  I will show how I can quickly create the same Parameters query in a new workbook and use it to access specific information.  I will be using car data I have extracted from the Kaggle website.

![](https://sumproduct.com/wp-content/uploads/2025/09/image-217.png)

Let’s start by looking at how many rows of data I have for this example.  There are a few different ways I could do this; I choose to use the **[ROWS](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/)
** function:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-218.png)

The formula I have used is:

> **\=ROWS(Car\_Sales\[#Data\])**

This calculates how many rows of data there are in the **Car\_Sales** Table: 241,205.

Some of the filters required have been entered on the Outputs sheet:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-219.png)

I will begin by converting this data into the format required to use the Parameters Table method.  The requires two \[2\] columns, named **Parameter** and **Value**, in a Table called **Parameters**.  I enter the required labels in cells **C10** and **D10** and click **CTRL** + **T** to ‘Create Table’.  I ensure that the cell range for the Table is correctly identified.

![](<Base64-Image-Removed>)

I click OK, and change the Table name to **Parameters**:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-221.png)

Note that, to access the ‘Table Name’ box, I have selected the Table and ensured that I am in the ‘Table Design’ tab.

There are several ways to proceed from this point.  I could extract the data to Power Query and repeat the process I followed in the Workbook Parameter Table series, but since I already have the query in that workbook, I will copy it from there instead.  I open the workbook containing the query I would like to copy:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-223.png)

On the Data tab, I open the ‘Queries & Connections’ pane.  I may then right-click on the query **fnGetParameter** and choose to ‘Copy’:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-224.png)

Having copied the query, I open the ‘Queries & Connections’ pane in my destination workbook and right-click:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-225.png)

Note that the Paste icon is enabled.  When I choose to paste, the query is copied to the pane:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-226.png)

I am now ready to import the car sales data.  Next time, I’ll create the query for the car sales data and set up the filters.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/#0)

[](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/#0 "close")

top