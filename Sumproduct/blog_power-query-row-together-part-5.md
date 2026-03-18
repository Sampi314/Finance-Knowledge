# Power Query: Row Together Part 5

**Source:** https://sumproduct.com/blog/power-query-row-together-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 5

*   July 23, 2025

Power Query: Row Together Part 5
================================

_Welcome to our Power Query blog.  This week, I begin a new row challenge._

Over the last few weeks, I have been looking at how to solve tasks involving the manipulation of data to form new rows.  This week, I have a slightly different version of the challenge.  The data I will be transforming is in an Excel Table called **SalesResults**.

![](https://sumproduct.com/wp-content/uploads/2025/07/image1-11.png)

I have a list of amounts accrued by each **Salesperson** for our suppliers.  The task is to create a row for each **Salesperson** for each **Company** they have sold to detailing the total **Amount**, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/07/image2-10.png)

I begin by extracting the Table into Power Query by selecting the Table and using the right-click menu to access the option ‘Get Data from Table/Range…’.

This creates a new query **SalesResults**:

![](https://sumproduct.com/wp-content/uploads/2025/07/image3-5.png)

I will keep the ‘Changed Type’ step as I will be summing the **Amount**.  The key to ensuring that the total line is in the correct place is to create an index.  To begin, I need to make sure that my data is in **Salesperson** order:

![](https://sumproduct.com/wp-content/uploads/2025/07/image4-2.png)

Now I can add an ‘Index column’ from the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/07/image5-2.png)

I choose to create an index that starts ‘From 1’, although for this example it doesn’t matter where I start from.  Having created my index, the next step is to group the data to create the total line for each salesperson.  I access the ‘Group By’ option from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/07/image6-1.png)

I have used the Advanced form of the ‘Group By’ dialog.  I am grouping by **Salesperson**, and I would like new columns grouping **Company** and **Amount**.  I also need the maximum **Index** so that I can put the total row at the bottom of each **Salesperson** group.  I click OK to group my data:

![](<Base64-Image-Removed>)

This issue is familiar from [Part 1](https://sumproduct.com/blog/power-query-row-together-part-1/)
.  Since I am summing Company, I need to change the **M** code for the ‘Grouped Rows’ step.

![](<Base64-Image-Removed>)

I need to change the **M** code from this:

> **`= Table.Group(#"Added Index", {"Salesperson"}, {{"Company", each List.Sum([Company]), type nullable text}, {"Amount", each List.Sum([Amount]), type nullable number}, {"Index", each List.Max([Index]), type number}})`**

to this:

> **`= Table.Group(#"Added Index", {"Salesperson"}, {{"Company", each Text.Combine([Company], ", "), type nullable text}, {"Amount", each List.Sum([Amount]), type nullable number}, {"Index", each List.Max([Index]), type number}})`**

I now have the total rows:

![](<Base64-Image-Removed>)

There are several more changes I need to make to the total rows, which is where I will continue next week.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-5/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-5/#0 "close")

top