# Power Query: Power Query in Excel for the web Part 3

**Source:** https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query in Excel for the web Part 3

*   February 4, 2026

Power Query: Power Query in Excel for the web Part 3
====================================================

_Welcome to our Power Query blog.  This week, we continue to look at some of the features of Power Query in Excel for the web by importing a CSV file – quite timely given Excel’s new **[IMPORTCSV](https://sumproduct.com/news/excel-has-import-ant-new-functions/)** function!_

[Recently](https://sumproduct.com/blog/power-query-now-in-excel-for-the-web-properly/)
, I welcomed the arrival of more Power Query functionality to Excel for the web.  I have looked at how I can now create a query from data in the current online workbook (aka project) and this week I will extract data from other online workbooks.

It’s time to enlist the help of my imaginary salespeople (I know you’ve missed them!).

I plan to extract data from a workbook called **PQ\_StandardExpense\_CSV\_1**.   To access the data, I begin in the Data tab where I access the ‘Get Data’ dialog box from the ‘Get Data’ dropdown.  I will be using the Text/CSV option:

![](<Base64-Image-Removed>)

When I click on this option, the ‘Connect to data source’ dialog box appears.  Since the data source I wish to access is online, I am prompted for the ‘File path or URL’. 

![](<Base64-Image-Removed>)

On the left, there is a page icon and a link where I can ‘Learn more’.  This will take me to the Microsoft Learn Text/CSV Power Query connectors page.  I have the option to ‘Link to file’ or ‘Upload file’.  If I choose to ‘Upload file’ then according to the ToolTip, the file will be uploaded to my OneDrive:

![](<Base64-Image-Removed>)

If I select this option, the ‘File path or URL’ prompt is replaced by a facility to upload the file:

![](<Base64-Image-Removed>)

For my current example, the file already exists on the company OneDrive.  I will explore the upload option in another blog post.

I select the ‘Link to file’ option.  I could choose to ‘Browse OneDrive’:

![](<Base64-Image-Removed>)

However, this will allow me to browse my personal OneDrive, rather than the SumProduct OneDrive, which I am currently using.  I need to use the URL which I can get from the file.  There are two steps.   I go to the File tab, and from Info on the dropdown I choose to ‘Open in Desktop’:

![](<Base64-Image-Removed>)

I may access the location in the Desktop app by choosing to ‘Copy Path’:

![](<Base64-Image-Removed>)

I may paste this into the URL box using the shortcut **CTRL** + **V**, but there is one more change I need to make:

![](<Base64-Image-Removed>)

When I click Next, I get an error:

![](<Base64-Image-Removed>)

I remove the end of the path as requested, and try again:

![](<Base64-Image-Removed>)

Success!  This looks similar to the Navigator dialog in the desktop version of Excel but the options at the bottom of each dialog are not the same:

![](<Base64-Image-Removed>)

In the desktop version of Excel, I can ‘Load’ to the workbook, ‘Transform Data’ or Cancel.  In Excel for the web, in addition to Cancel and ‘Transform data’, I have the option to ‘Add table using examples’. 

I will investigate how the option ‘Add table using examples’ works in Excel for the web next time.

Come back next time for more ways to use Power Query!            

*   [Log in](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/#0)

[](https://sumproduct.com/blog/power-query-power-query-in-excel-for-the-web-part-3/#0 "close")

top