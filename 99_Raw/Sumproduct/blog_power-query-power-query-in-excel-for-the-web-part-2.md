# Power Query: Power Query in Excel for the web Part 2

**Source:** https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query in Excel for the web Part 2

*   January 28, 2026

Power Query: Power Query in Excel for the web Part 2
====================================================

_Welcome to our Power Query blog.  This week, we continue to look at some of the features of Power Query in Excel for the web._

Recently, I welcomed the arrival of more Power Query functionality to Excel for the web.  [Last week](https://sumproduct.com/blog/power-query-in-excel-for-the-web-part-1/)
, I began to compare the process of uploading data from the workbook between Excel for the web and the desktop version of Excel.  The example data I am using is from the recent blog [Power Query: Missing Replace Values](https://sumproduct.com/blog/power-query-missing-replace-values/)
.

![](<Base64-Image-Removed>)

I had a Table called **Orders**, which is missing some information.  Whilst most of my salespeople have provided the figures, Newbie is still crunching the numbers and has put “(not ready)” after his name and “TBA” in the amount cell in some of the rows.  I am going to use this data to check if the Power Query “feature” (aka “bug”) I covered in [Power Query: Missing Replace Values](https://sumproduct.com/blog/power-query-missing-replace-values/)
 is also present in the Excel for the web version.

[Last week](https://sumproduct.com/blog/power-query-in-excel-for-the-web-part-1/)
, I checked out the settings that would allow me to automate ‘Changed Type’ steps and extracted the data to Power Query, creating a new query called **Orders**:

![](<Base64-Image-Removed>)

To tidy the data and make it consistent, I begin by selecting the **Salesperson** column and right-clicking to access ‘Replace Values…’:

![](<Base64-Image-Removed>)

I then remove any “ (not ready)” values (complete with preceding space):

![](<Base64-Image-Removed>)

Note: In Excel for the web, this dialog box features a help icon next to the title.  This icon allows you to access the Microsoft Learn pages to find out more about how to replace values and errors.

The **Salesperson** column is now consistent:

![](<Base64-Image-Removed>)

Now to do the same to **OrderAmount**.  You may recall from the blog [Power Query: Missing Replace Values](https://sumproduct.com/blog/power-query-missing-replace-values/)
 that the option to ‘Replace Values’ was missing from the right-click menu in the desktop version of Excel:

![](<Base64-Image-Removed>)

After checking other columns before the data types had been determined, I concluded that the presence of data with inconsistent data types in **OrderAmount** was causing an issue with the context specific properties of the right-click menus for the column or any cells in the column.  

However, in Excel for the web the option _is_ available in the right-click menu:

![](<Base64-Image-Removed>)

I open the dialog and enter the value I need to replace:

![](<Base64-Image-Removed>)

Since I am dealing with a numerical column, I replace “TBA” with _null_.  When I click OK, the column is cleaned and I may convert it to use the ‘Decimal Number’ data type. 

![](<Base64-Image-Removed>)

The bug does not exist in Excel for the web, which hopefully means it will be fixed in the desktop version of Excel in due course. 

Next time, I will explore the process of creating queries from other data sources in Excel for the web.

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-2/#0)

[](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-2/#0 "close")

top