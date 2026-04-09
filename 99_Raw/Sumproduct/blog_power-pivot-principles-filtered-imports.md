# Power Pivot Principles: Filtered Imports

**Source:** https://sumproduct.com/blog/power-pivot-principles-filtered-imports/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Filtered Imports

*   February 5, 2018

Power Pivot Principles: Filtered Imports
========================================

Power Pivot Principles: Filtered Imports
========================================

6 February 2018

_Welcome back to our Power Pivot blog, today we look at filtering the data a little before importing it form Excel. This blog builds on our previous blog [Power Pivot Principles: Importing from Excel](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-importing-data-from-excel)
._

Returning to the Table Import Wizard _(introduced last time)_, instead of selecting ‘Finish’ immediately, you can select ‘Preview and Filter’. This is recommended as it is always best (especially with large datasets) to import only what you need – “less is more”. You can always return and pick up extra data should you need it later.

![](<Base64-Image-Removed>)

The Table Import Wizard will appear _(below)_. This window allows us to uncheck the check box on each column of data to prevent that column from being brought into the model. We can also use the drop-down arrow on each column to filter the data and select only relevant data should this be required. You can download our sample dataset [here](https://sumproduct.com/assets/blog-pictures/2018/power-pivot/power-pivot-training-database.xlsx)
.

*   In our example, unselect the checkbox for ‘Suffix’ and ‘AddressLine2’ – there isn’t any data in these columns and therefore we don’t need to bring these columns in to the model
*   Select ‘OK’
*   Ensure that all worksheets are brought into the model except for ‘DimPromotion$’
*   Select ‘Finish’ to import.

![](<Base64-Image-Removed>)

A message will appear showing that the import was successful:

![](<Base64-Image-Removed>)

When importing multiple tables simultaneously, sometimes the final row may contain an error which does not relate to any particular table. Always read the error, but often this pertains to the fact that Power Pivot cannot recognise how the tables may be related. Take note if this is the case, but it is not an issue that has prevented a successful import of your data.

The data will now appear in separate tabs in the Power Pivot window as shown below:

![](<Base64-Image-Removed>)

Whoops! I forgot to bring in the ‘DimPromotion$’ table into the model. So, let’s import it now!

*   Click on ‘Existing Connections’ under the ‘Get External Data’ group:

![](<Base64-Image-Removed>)

*   The following dialog box will appear:

![](<Base64-Image-Removed>)

*   Select the connection to the original data source
*   Select ‘Open’
*   The ‘Table Import Wizard’ will appear:

![](<Base64-Image-Removed>)

*   We can select the table we missed on the original import ‘DimPromotion$’
*   Either ‘Preview and Filter’ the data or select ‘Finish’.

Great – now we have the ‘DimPromotion$’ table in our data set. It’s that easy!

Stay tuned for our next post on Power Pivot. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-filtered-imports/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-filtered-imports/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-filtered-imports/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-filtered-imports/#0)

[](https://sumproduct.com/blog/power-pivot-principles-filtered-imports/#0 "close")

top