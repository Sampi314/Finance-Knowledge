# Power Query: Rental Wrangles Receipts – Part 2

**Source:** https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Rental Wrangles Receipts – Part 2

*   August 17, 2021

Power Query: Rental Wrangles Receipts – Part 2
==============================================

Power Query: Rental Wrangles Receipts – Part 2
==============================================

18 August 2021

_Welcome to our Power Query blog. This week, I continue with my example where I need to transform my data after I applied a function._

[Last time](https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-1/)
, I was looking at how to extract the correct rental information for an event, where I had a list of tents required for each event:

![](<Base64-Image-Removed>)

I had applied a function and calculated the rent for each **Tent Type**.

![](<Base64-Image-Removed>)

To get all the information for the event in one row, I need to recombine the **Tent Type** with the **Quantity**, and combine the **Tent Types** for each event into one row.

I start by using ‘Merge Columns’ on the Transform tab, while I have **Quantity** and **Tent Type** selected. I select **Quantity** first and then hold down **CTRL** while I select **Tent Type**.

![](<Base64-Image-Removed>)

I choose to separate the data with a space, and call the column **Tent Types**.

![](<Base64-Image-Removed>)

I now have the **Tent Types** in one column.

![](<Base64-Image-Removed>)

The next step is to combine my rows. In this context, **Rental Rate** will not make sense (since I have different tent types for one event), so I delete this column.

![](<Base64-Image-Removed>)

I need to group my data so that I have one row per **Event** / **Date** combination. I select ‘Group By’ from the Transform tab:

![](<Base64-Image-Removed>)

I group by **Date** and **Event**. For **Tent Types**, I will need the values from ‘All Rows’ and I sum the **Rental Amount**.

![](<Base64-Image-Removed>)

I currently have a table of data in each field of the **Tent Types** column. I need to extract the **Tent Types** data from the table. To do this, I add a new Custom Column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I am extracting **Tent Types** from the table, currently in the **Tent Types** column.

![](<Base64-Image-Removed>)

Now I have the **Tent Types** in a list in each field of **Custom.** I delete the original **Tent Types** column, and rename **Custom** to **Tent Types**. I use the extract icon.

![](<Base64-Image-Removed>)

I choose to ‘Extract Values’:

![](<Base64-Image-Removed>)

I opt to put the comma with a space (**,** ) back.

![](<Base64-Image-Removed>)

I have all the data I want; I just need to tidy up by re-ordering my columns and setting the data type of **Rental Amount** to currency.

![](<Base64-Image-Removed>)

I now have **Event Data** with the original format of one row per event, and I have added the rental information.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-2/#0)

[](https://sumproduct.com/blog/power-query-rental-wrangles-receipts-part-2/#0 "close")

top