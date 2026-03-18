# Power Query: Cell Referencing

**Source:** https://sumproduct.com/blog/power-query-cell-referencing/

---

[Home](https://sumproduct.com/)

\> Power Query: Cell Referencing

*   February 6, 2018

Power Query: Cell Referencing
=============================

Power Query: Cell Referencing
=============================

7 February 2018

_Welcome to our Power Query blog. This week, I take a look at how to reference a cell in an Excel workbook from Power Query._

I will begin by creating a query from the item data below:

![](<Base64-Image-Removed>)

On the ‘Data’ tab, in the ‘Get and Transform’ section, I choose to create a new query ‘From Table’.

![](<Base64-Image-Removed>)

This all looks fine, but now I want to add the ‘Grand Total’ from another sheet in my Workbook.

![](<Base64-Image-Removed>)

My first step is to name my cell using the Name Box (highlighted above, currently displaying the cell **K5**). I will call it ‘**Grand\_Total**‘.

I go back to my query, and I choose to create a ‘Custom Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I have entered the following formula:

**Excel.CurrentWorkbook(){\[Name=”Grand\_Total”\]}\[Content\]{0}\[Column1\]**

When I click ‘OK’, my new column is added.

![](<Base64-Image-Removed>)

This method works for character and numeric cells (including dates).

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-cell-referencing/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-cell-referencing/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-cell-referencing/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-cell-referencing/#0)

[](https://sumproduct.com/blog/power-query-cell-referencing/#0 "close")

top