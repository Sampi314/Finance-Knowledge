# Power Query: Row Together Part 2

**Source:** https://sumproduct.com/blog/power-query-row-together-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 2

*   July 2, 2025

Power Query: Row Together Part 2
================================

_Welcome to our Power Query blog.  This week, I look at alternative ways of displaying the combined rows._

Often when using Power Query to solve a problem, there is more than one way to attack it.  This is true when it comes to combining multiple rows to make one row.  The solution will depend upon the requirements of the data and how the rows are connected.  [Last week](https://www.sumproduct.com/blog/power-query-row-together-part-1)
, I started with a simple scenario.

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-01.jpg)

The task was to create a row for each **Salesperson** containing all the regions.  The end result looked like this:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-02.jpg)

Before I move on to testing the solution, I would like to point out how easy it is to change the format of the solution to this: 

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-03.jpg)

If I go back to my original query **SalesRegions**:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-04.jpg)

I can use the cog icon next to the ‘Split Column by Delimiter’ step to change the settings for this step:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-05.jpg)

If I open the ‘Advanced options’ I see more settings:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-06.jpg)

Notice that I have the option to ‘Split into’ Columns or Rows.  If I change this setting to Rows, I have all the region data in one column:

![](https://sumproduct.com/wp-content/uploads/2025/07/RT2-07.jpg)

This solution has another advantage.  To show this, I will create two \[2\] versions of the query, one that outputs the region data to one column and one that outputs the region data to multiple columns.  I will call them **SalesRegionsRows** and **SalesRegionsColumns**.  I load both queries to the Outputs worksheet:

![](<Base64-Image-Removed>)

Now, I will change the data on the Inputs worksheet:

![](<Base64-Image-Removed>)

I have added a row for Mary.  Let’s see what happens when I refresh the queries.  **SalesRegionsColumns** has a row with a space, but all the data has been returned:

![](<Base64-Image-Removed>)

From this testing, I know I need to filter out spaces from the **Region** column.  Now, let’s look at **SalesRegionsRows**:

![](<Base64-Image-Removed>)

There are still only seven \[7\] columns, which means that the new data is missing.  Next time, I will look at why this happened and how to fix it.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-2/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-2/#0 "close")

top