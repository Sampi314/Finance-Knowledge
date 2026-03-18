# Power Query: Row Together Part 6

**Source:** https://sumproduct.com/blog/power-query-row-together-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 6

*   July 30, 2025

Power Query: Row Together Part 6
================================

_Welcome to our Power Query blog.  This week, I continue a new row challenge._

Over the last few weeks, I have been looking at how to solve tasks involving the manipulation of data to form new rows.  [Last week](https://www.sumproduct.com/blog/power-query-row-together-part-5)
, I began a slightly different version of the challenge.  The data I am  transforming is in an Excel Table **SalesResults**.

![](https://sumproduct.com/wp-content/uploads/2025/07/image-18.png)

I have a list of amounts accrued by each **Salesperson** for our suppliers.  The task is to create a row for each **Salesperson** for each **Company** they have sold to detailing the total **Amount**, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/07/image2-10.png)

[Last week](https://sumproduct.com/blog/power-query-row-together-part-5/)
, I extracted the data to a new query **SalesResults**:

![](https://sumproduct.com/wp-content/uploads/2025/07/image-19.png)

I sorted the data in ascending **Salesperson** order and created an index before grouping the data.

![](https://sumproduct.com/wp-content/uploads/2025/07/image-20.png)

I amended the **M** code to aggregate the **Company** rows correctly and now I have the total rows:

![](https://sumproduct.com/wp-content/uploads/2025/07/image-21.png)

There are a few more changes I need to make to the total rows.  I need to format the **Salesperson** column to include the prefix “Total for “.  I can do this from the Transform tab.  In the ‘Text Column’ group there is a Format dropdown where I can ‘Add Prefix’:

![](https://sumproduct.com/wp-content/uploads/2025/07/image-22.png)

Choosing this option opens the following dialog:

![](https://sumproduct.com/wp-content/uploads/2025/07/image-23.png)

The data in **Salesperson** is now displayed correctly.

![](https://sumproduct.com/wp-content/uploads/2025/07/image-24.png)

The next change I need to make is to the **Index** column.  Currently, it has the same value as the last row for each **Salesperson**.  I need to add a number to each value in **Index** so that it will appear in the correct position.  I can do this from the Transform tab.  In the ‘Number Column’ section, there is a Standard dropdown:

![](<Base64-Image-Removed>)

I can add a specified value to each number in the selected column.  When I choose this option, I access a dialog:

![](<Base64-Image-Removed>)

If I add one \[1\] to each **Index**, it would be part of the data group for the next **Salesperson**.  I need a value that is more than zero \[0\] but less than one.  I choose a half \[0.5\] and click OK.

![](<Base64-Image-Removed>)

My data is ready for the next step, which is where I will continue next week.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-6/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-6/#0 "close")

top