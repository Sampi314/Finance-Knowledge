# Power Pivot Principles: Importing from an Access Database (Continued) and Formatting Data

**Source:** https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database-continued-and-formatting-data/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Importing from an Access Database (Continued) and Formatting Data

*   February 19, 2018

Power Pivot Principles: Importing from an Access Database (Continued) and Formatting Data
=========================================================================================

Power Pivot Principles: Importing from an Access Database (Continued) and Formatting Data
=========================================================================================

20 February 2018

_Welcome back to our Power Pivot blog series. Today we discuss formatting and changing table properties. This blog picks up right after our previous blog, [Importing from an Access Database](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-importing-from-an-access-database)
._

If you wish to follow along, please download the data file [here](https://sumproduct.com/assets/blog-pictures/2018/power-pivot/power-pivot-training-database.xlsx)
 and first undertake the actions from [last time’s blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-importing-from-an-access-database)
.

Not all databases are created equal; some are perfect, some need formatting adjustments. Our Access Database is not perfect – let’s perform some formatting adjustments!

Rename the table ‘FactInternetSales’ to ‘Sales’ by typing it in, in the bottom tab (simply double-click or right-click on the tab). This will clearly identify each table that’s imported into PowerPivot.

![](<Base64-Image-Removed>)

Some columns will have to be updated to ensure they are showing the correct Data Type and Format, _e.g._ a whole number, currency, text, date. We also have to specify if they are a whole number, decimal number, currency _etc_.

![](<Base64-Image-Removed>)

Do remember the following:

*   **Formatting:** Changing the formatting changes the appearance but not the actual contents. It is merely ‘cosmetic’. For example, the value ‘3.7’ formatted as a whole number would appear as ‘4’, but if you multiplied it by 10 you would get ’37’
*   **Data Type:** Changing the data type may remove information. For example, changing the Data Type from ‘Decimal Number’ to ‘Whole Number’ for the value ‘3.7’ would round this number to ‘4’. Multiplying this value would give a result of ’40’. When information is at risk, Power Pivot will provide a warning before the change takes place. In any case, the data may be restored simply by refreshing the source. **You cannot damage the underlying data.**

In the ‘Formatting’ section of the ‘Home’ tab select the drop-down box next to ‘Data-Type’. Go through each column and format each field to ensure that it is showing the correct data type and in the correct format: for instance, the ‘SalesAmount’ column, the format should be changed from ‘General’ to ‘Currency’, _viz._

![](<Base64-Image-Removed>)

If a column in our original data was not originally brought in, we can bring it in by going to the ‘Design’ tab of the Power Pivot window and then select the ‘Table Properties’ on the Ribbon:

![](<Base64-Image-Removed>)

The ‘Edit Table Properties’ dialog box will appear, allowing us to select any columns that we have missed out earlier. Scroll across, select the ‘Freight’ column and click Save:

![](<Base64-Image-Removed>)

The Freight column will now appear on the sheet:

![](<Base64-Image-Removed>)

Format it into a currency and save the file.

![](<Base64-Image-Removed>)

There you have it: we have just cleaned up the data from our Access database.

Stay tuned for our next post on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database-continued-and-formatting-data/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database-continued-and-formatting-data/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database-continued-and-formatting-data/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database-continued-and-formatting-data/#0)

[](https://sumproduct.com/blog/power-pivot-principles-importing-from-an-access-database-continued-and-formatting-data/#0 "close")

top