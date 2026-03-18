# Power Query: Workbook Parameter Table Example Part 9

**Source:** https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-9/

---

[Home](https://sumproduct.com/)

\> Power Query: Workbook Parameter Table Example Part 9

*   November 26, 2025

Power Query: Workbook Parameter Table Example Part 9
====================================================

_Welcome to our Power Query blog.  This week, I complete the example._

During training, attendees often ask how to use parameters to make their Power Query reports more flexible.  I recently looked at this in two \[2\] blog collections: [Workbook Parameter Tip](https://sumproduct.com/uncategorized/power-query-workbook-parameter-tip/)
 and [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
.  My fictional salespeople can take some well-earned leave since I will be applying the same method to a much larger dataset.  I will show how I can quickly create the same Parameters query in a new workbook and use it to access specific information.  I will be using car data I have extracted from the Kaggle website.  There are 241,205 rows.

![](https://sumproduct.com/wp-content/uploads/2025/10/image-40.png)

Some of the filters required have been entered on the Outputs sheet:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-41.png)

In [Part 1](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/)
, I converted this into the Table I need for the **fnGetParameter** method I used in the [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
 series. In [Part 2](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/)
 , I imported the car sales data into Power Query and temporarily reduced the data in the query. [In Part 3](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-3/)
, I added a filter on the **Date** column and used **fnGetParameter** to pass the range parameters from the workbook to the query.  This currently gives me no data, as the parameters don’t have values:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-43.png)

[In Part 4](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-4/)
, I entered **M** code to determine how to filter the **Date** based on how many of the date parameters the user entered.  I tested various combinations of ‘Date from’ and ‘Date to’ values. [In Part 5](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-5/)
, I moved on to the ‘Top 10 salespeople’.  Although this refers to ‘Top 10’ the user can enter any number of salespeople here.  If they leave it empty or enter zero \[0\], then no filtering will take place.  I began by taking a reference copy of **Car\_Sales**, which I called **Top Ten**. I grouped and sorted the data and created the framework for the filter by opting to keep the top 10 rows.

[In Part 6](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/)
, I refined the **M** code to ensure that the steps in this query only access **Car\_Sales** if the ‘Top 10 salespeople’ parameter were not _null_ or zero \[0\].

![](https://sumproduct.com/wp-content/uploads/2025/10/image-72.png)

I have the salespeople, but I need to show all the date rows for each of them.  [In Part 7](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/)
, I  combined **Top Ten** and **Car\_Sales**:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-77.png)

[Last week](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-8/)
, I created two \[2\] scenarios.  If the ‘Top 10 salespeople’ parameter is not _null_ or zero \[0\], then the **Top Ten** is merged with **Car\_Sales** and the data is expanded, sorted and repositioned.  Otherwise, the merge and subsequent steps do not occur.   I tested my solution:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-86.png)

This is all looking good, but I have a final change to make to both **Car\_Sales** and **Car\_Sales Reference**.  I need to remove the ‘Kept first rows’ step so that all the data is processed:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-87.png)

I ignore the warning, delete the step from both queries and ‘Close & Load’:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-88.png)

It worked, but I can see I have another sort to add.  If I have multiple rows for each **Salesperson**, I need to sort by **Date** too.  I change the ‘Sorted Rows’ step in **Car\_Sales** from this:

> **\= if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.Sort(#”Expanded Top Ten”,{{“Total Sales”, Order.Descending}}) else #”Filtered Rows”**

to this:

> **\= if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.Sort(#”Expanded Top Ten”,{{“Total Sales”, Order.Descending}, {“Date”, Order.Ascending}}) else #”Filtered Rows”**

The data will now be sorted by the **Total Sales** in descending order and the **Date** in ascending order, but only if there is a value in the ‘Top 10 salespeople’ parameter.

![](<Base64-Image-Removed>)

Since I am dealing with a large dataset, I should add a buffer to the ‘Merged Queries’ step.  I change the **M** code from this:

> **\= if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.NestedJoin(#”Filtered Rows”, {“Salesperson”}, #”Top Ten”, {“Salesperson”}, “Top Ten”, JoinKind.RightOuter) else #”Filtered Rows”**

to this:

> **\= if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.NestedJoin(Table.Buffer(#”Filtered Rows”), {“Salesperson”}, Table.Buffer(#”Top Ten”), {“Salesperson”}, “Top Ten”, JoinKind.RightOuter) else #”Filtered Rows”**

This reads the Tables into memory, rather than reading each row as the join is performed.  For more on **Table.Buffer()**, see [Power Query – merging matters](https://sumproduct.com/blog/power-query-merging-matters/)
.

![](<Base64-Image-Removed>)

I can now ‘Close & Load’ from the Home tab, and my queries are complete.

![](<Base64-Image-Removed>)

Michael is doing well!  That completes the Power Query part of this task.  I suggested using [Data Validation](https://sumproduct.com/thought/data-validation/)
 in the **Parameters Table** earlier, which may be accessed from the Data tab.  This would be needed on cells **D11:D13** to ensure users enter a valid positive integer in cell **D11** and enter valid dates in cells **D12:D13**.  The values in cells **C11:C13** must not be changed, otherwise the parameter names will not be recognised.  This could be achieved by using [Protect Sheet](https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/)
 functionality.

Come back next time for more ways to use Power Query!              

*   [Log in](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-9/#0)

[](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-9/#0 "close")

top