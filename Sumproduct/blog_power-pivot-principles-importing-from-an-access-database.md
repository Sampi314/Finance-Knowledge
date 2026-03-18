# Power Pivot Principles: Importing from an Access Database

**Source:** https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Importing from an Access Database

*   February 12, 2018

Power Pivot Principles: Importing from an Access Database
=========================================================

Power Pivot Principles: Importing from an Access Database
=========================================================

13 February 2018

_Welcome back to our Power Pivot blog. In this post, we discuss how to import data from an Access database._

**Example**

If you wish to follow along, please download the data file [here](https://sumproduct.com/assets/blog-pictures/2018/power-pivot/power-pivot-training-database.xlsx)
.

Open Excel, then select the ‘Power Pivot’ tab on the Ribbon:

![](<Base64-Image-Removed>)

Select the ‘Manage’ option in the Ribbon:

![](<Base64-Image-Removed>)

The Power Pivot window will popup. We can now select the ‘From Database’ option in the ‘Get External Data’ group.

![](<Base64-Image-Removed>)

The ‘Table Import Wizard’ dialog box will appear, allowing us to designate a connection name in this case we write ‘Sales’, and provide login details if the database requires. From a security perspective, I do not recommend entering your login details and saving them. If you do this, it will mean anyone who opens this file can access the data in this way.

![](<Base64-Image-Removed>)

Power Pivot will then prompt us to choose from two methods of importing data. More advanced users (_e.g._ those who have experienced the delights of SQL) may select ‘Write a query that will specify the data to import’. For us lesser mortals, for this example we will pick ‘Select from a list of tables and views to choose the data to import’.

![](<Base64-Image-Removed>)

Then select the ‘FactInternetSales’ Table from the Table Import Wizard:

![](<Base64-Image-Removed>)

Before we hit ‘Finish’, it’s good practice to ‘Preview & Filter’ the data. This allows us to unselect any data that isn’t needed for the Power Pivot model.

![](<Base64-Image-Removed>)

Unselect all of the fields, allowing us to individually select all of the fields that we want to import instead. For this instance, I am going to choose ‘Product Key’, ‘OrderDate’, ‘CustomerKey’, ‘OrderQuantity’ and ‘SalesAmount’.

![](<Base64-Image-Removed>)

For better efficiencies, tables should be long and thin, where possible: not too many columns and plenty of rows.

![](<Base64-Image-Removed>)

We have now successfully imported a dataset from an Access Database.

Stay tuned for our next post on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database/#0)

[](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database/#0 "close")

top