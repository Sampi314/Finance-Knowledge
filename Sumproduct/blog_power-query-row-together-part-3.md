# Power Query: Row Together Part 3

**Source:** https://sumproduct.com/blog/power-query-row-together-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 3

*   July 9, 2025

Power Query: Row Together Part 3
================================

_Welcome to our Power Query blog.  This week, I look at the problem I encountered when I combined rows of data._

Often when using Power Query to solve a problem, there is more than one way to attack it.  This is true when it comes to combining multiple rows to make one row.  The solution will depend upon the requirements of the data and how the rows are connected.  In [Part 1](https://www.sumproduct.com/blog/power-query-row-together-part-1)
, I started with a simple scenario.

![](https://sumproduct.com/wp-content/uploads/2025/07/RT3-01.jpg)

The task was to create a row for each **Salesperson** containing all the regions.  The end result looked like this:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT3-02.jpg)

[Last time](https://www.sumproduct.com/blog/power-query-row-together-part-2)
, I created two \[2\] versions of the query, one that outputs the region data to one column and one that outputs the region data to multiple columns.  I called them **SalesRegionsRows** and **SalesRegionsColumns**.  I loaded both queries to the Outputs worksheet:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT3-03.jpg)

I then changed the data on the Inputs worksheet:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT3-04.jpg)

I added a row for Mary.  When I refreshed the queries.  **SalesRegionsColumns** had a row with a space, but all the data was returned:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT3-05.jpg)

From this testing, I know I need to filter out spaces from the **Region** column.  When I looked at **SalesRegionsRows**, there was a problem:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT3-06.jpg)

There are still only seven \[7\] columns, which means that the new data is missing.  This is because when I only have one row for each salesperson and I choose to create columns, the new column names appear in the step:

> **`= Table.SplitColumn(#"Grouped Rows", "Region", Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv), {"Region.1", "Region.2", "Region.3", "Region.4", "Region.5", "Region.6"})`**

![](<Base64-Image-Removed>)

This means that even though the new data was picked up when I grouped rows:

![](<Base64-Image-Removed>)

There are not enough columns in the ‘Split Column by Delimiter’ step to hold the data.  However, there is a surprising way to fix this.  I can change the **M** code for the step to:

> **`= Table.SplitColumn(#"Grouped Rows", "Region", Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv)`**

I simply do not specify the columns.  It does mean that I must change the data type of the column **Salesperson** before I split the column:

![](<Base64-Image-Removed>)

Let’s try it:

![](<Base64-Image-Removed>)

It is not perfect, as it assumes that **Region 2** on the added line has a value of blank and includes it as **Region.8** (this is also what causes the blank row in the single column solution), but it is dynamic.

Finally, I add a new **Salesperson**:

![](<Base64-Image-Removed>)

When I refresh the queries all the data is returned:

![](<Base64-Image-Removed>)

I will look at more examples of combining row data next time.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-3/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-3/#0 "close")

top