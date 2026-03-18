# Power Query: Row Together Part 4

**Source:** https://sumproduct.com/blog/power-query-row-together-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 4

*   July 16, 2025

Power Query: Row Together Part 4
================================

_Welcome to our Power Query blog.  This week, I look at how to keep a group in order._

Over the last few weeks, I have been looking at how to solve tasks involving the manipulation of data to form new rows.  When I was grouping the data I was reminded of an issue and a trick that I haven’t covered in this blog series.  Let’s start with the **SalesRegionsColumns** query I created in [Part 2](https://www.sumproduct.com/blog/power-query-row-together-part-2)
.  I have filtered on **Region** to remove region data that is blank or _null_. 

![](https://sumproduct.com/wp-content/uploads/2025/07/ROWTOGETHER01.jpg)

The task is to create a row for each **Salesperson** containing all the regions, but with the regions in alphabetical order. 

![](https://sumproduct.com/wp-content/uploads/2025/07/ROWTOGETHER02.jpg)

I will use the same approach I used in [Part 1](https://www.sumproduct.com/blog/power-query-row-together-part-1)
.  First, I sort the data in alphabetical order by Region.

![](https://sumproduct.com/wp-content/uploads/2025/07/ROWTOGETHER03.jpg)

Next, I group the regions by ‘summing’ them for each Salesperson:

![](https://sumproduct.com/wp-content/uploads/2025/07/ROWTOGETHER04.jpg)

I change the **M** code from:

> **`= Table.Group(#"Sorted Rows", {"Salesperson"}, {{"Regions", each List.Sum([Region]), type nullable text}})`**

to:

> **`= Table.Group(#"Sorted Rows", {"Salesperson"}, {{"Regions", each Text.Combine([Region],", "), type nullable text}})`**

I check the results:

![](https://sumproduct.com/wp-content/uploads/2025/07/ROWTOGETHER05.jpg)

They are not in alphabetical order!  Now for the trick.  Insert a step before the ‘Grouped Rows1’ step by selecting to view the ‘Sorted Rows’ step and then choosing to add an ‘Index Column’ from the ‘Add Column’ tab: 

![](<Base64-Image-Removed>)

Ignore the warning that you are inserting a step and choose to Insert.

![](<Base64-Image-Removed>)

This creates an **Index** column. 

![](<Base64-Image-Removed>)

Go back to step ‘Grouped Rows1’ and view the data:

![](<Base64-Image-Removed>)

The **Regions** data is now in alphabetical order.  You can delete the **Index** column, and your data is in the correct order.  The reason is not obvious and probably has something to do with the language used to create **M** code.  I think you’ll agree it is a useful trick to know about.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-4/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-4/#0 "close")

top