# Power Query: Power Query in Excel for the web Part 1

**Source:** https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query in Excel for the web Part 1

*   January 21, 2026

Power Query: Power Query in Excel for the web Part 1
====================================================

_Welcome to our Power Query blog.  This week, we begin to take a look at some of the features of Power Query in Excel for the web._

[Last week](https://sumproduct.com/blog/power-query-now-in-excel-for-the-web-properly/)
, I welcomed the arrival of more Power Query functionality to Excel for the web.  This week, I compare the process of uploading data from the workbook between Excel for the web and the desktop version of Excel.  The example data I am using is from the recent blog [Power Query: Missing Replace Values](https://sumproduct.com/blog/power-query-missing-replace-values/)
.

![](https://sumproduct.com/wp-content/uploads/2026/01/image-21.png)

I had a Table called **Orders**, which is missing some information.  Whilst most of my salespeople have provided the figures, Newbie is still crunching the numbers and has put “(not ready)” after his name and “TBA” in the amount cell in some of the rows.  I am going to use this data to check if the Power Query “feature” (aka “bug”) I covered in [Power Query: Missing Replace Values](https://sumproduct.com/blog/power-query-missing-replace-values/)
 is also present in the Excel for the web version.

In order to extract data from the same workbook, I can either use the icon in the ‘Get & Transform Data’ section of the Data tab,

![](https://sumproduct.com/wp-content/uploads/2026/01/image-22.png)

or I can click somewhere in the Table, ensuring I either pick one \[1\] cell or the whole Table and use the right-click menu to access ‘Get Data from Table/Range’:

![](https://sumproduct.com/wp-content/uploads/2026/01/image-24.png)

This creates a new query called **Orders**:

![](https://sumproduct.com/wp-content/uploads/2026/01/image-25.png)

The first point I notice is that I do not have an automatically created ‘Changed Type’ step as I did for the desktop version of Excel example:

![](https://sumproduct.com/wp-content/uploads/2026/01/image-26.png)

To see why this step has not been produced, I can check the settings in Options on the Home tab:

![](https://sumproduct.com/wp-content/uploads/2026/01/image-27.png)

The default setting in the Global ‘Data Load’ tab is to ‘Detect column types and headers for unstructured sources according to each project’s setting’:

![](<Base64-Image-Removed>)

This is similar to the default in the desktop version, although the words used are not exactly the same:

![](<Base64-Image-Removed>)

When I select the Project ‘Data Load’ tab, the setting defaults to unchecked for ‘Automatically detect column types for unstructured sources’:

![](<Base64-Image-Removed>)

I would prefer this option to be set, which brings me to my first problem.  If I check the box and then discard the changes so that Power Query will generate the ‘Changed Type’ step, the box will go back to unchecked.  In my version of Excel for the web, I can’t see anywhere else to access this setting!  In the desktop version of Excel, I may access ‘Query Options’ from the ‘Get Data’ dropdown menu, but this option is not available in Excel for the web:

![](<Base64-Image-Removed>)

Currently, the only way to control whether a ‘Changed Type’ step is automatically created is to use the Global setting:

![](<Base64-Image-Removed>)

Now, when I discard the query and load it again, the ‘Changed Type’ step is created:

![](<Base64-Image-Removed>)

I am ready to continue with my query, which is where I will pick this up next week.

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/#0)

[](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-1/#0 "close")

top