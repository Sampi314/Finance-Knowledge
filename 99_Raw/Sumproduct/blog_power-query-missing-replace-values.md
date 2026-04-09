# Power Query: Missing Replace Values

**Source:** https://sumproduct.com/blog/power-query-missing-replace-values/

---

[Home](https://sumproduct.com/)

\> Power Query: Missing Replace Values

*   January 7, 2026

Power Query: Missing Replace Values
===================================

_Welcome to our Power Query blog.  This week, we look at an issue with replacing values._

The team at SumProduct have noticed an issue with Power Query when replacing values, so I offered to investigate.  Consider the following data:

![](<Base64-Image-Removed>)

I have a Table called **Orders**, which is missing some information.  Whilst most of my salespeople have provided the figures, Newbie is still crunching the numbers and has put “(not ready)” after his name and “TBA” in the amount cell in some of the rows.  I am going to use this data to illustrate a Power Query “feature” (aka “bug”) that you should be aware of.

I begin by extracting the Table into Power Query, by right-clicking and choosing to ‘Get Data from Table / Range’:

![](<Base64-Image-Removed>)

This creates a new query called **Orders**:

![](<Base64-Image-Removed>)

To tidy the data and make it consistent, I begin by selecting the **Salesperson** column and right-clicking to access ‘Replace Values…’:

![](<Base64-Image-Removed>)

I then remove any “ (not ready)” values:

![](<Base64-Image-Removed>)

The **Salesperson** column is now consistent:

![](<Base64-Image-Removed>)

Now to do the same to **OrderAmount**.  I select the column and right-click:

![](<Base64-Image-Removed>)

There is no ‘Replace Values…’ option!  You may be thinking this may be because the data type of **OrderAmount** is currently Any.  This is not the case.  I can prove this by selecting the right-click menu for **Salesperson** before the data types are detected:

![](<Base64-Image-Removed>)

This suggests that the presence of data with inconsistent data types in **OrderAmount** is causing an issue with the context specific properties of the right-click menus.  The ‘Replace Values…’ option also missing from the cell right-click menu for any cells in **OrderAmount**.  The following image compares the menu for a cell in **Salesperson** with a cell in **OrderAmount**:

![](<Base64-Image-Removed>)

Before I give up on using ‘Replace Values…’ there is another place I can check.  I select the **OrderAmount** column and access ‘Replace Values…’ from the Transform tab:

![](<Base64-Image-Removed>)

I open the dialog and enter the value I need to replace:

![](<Base64-Image-Removed>)

Since I am dealing with a numerical column, I replace “TBA” with _null_.  When I click OK, the column is cleaned, and I may convert it to use the ‘Decimal Number’ data type:

![](<Base64-Image-Removed>)

This is one to look out for when you need to replace values with a data type that is inconsistent with the surrounding data.  

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-missing-replace-values/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-missing-replace-values/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-missing-replace-values/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-missing-replace-values/#0)

[](https://sumproduct.com/blog/power-query-missing-replace-values/#0 "close")

top