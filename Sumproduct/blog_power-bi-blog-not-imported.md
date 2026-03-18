# Power BI Blog: Not Imported

**Source:** https://sumproduct.com/blog/power-bi-blog-not-imported/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Not Imported

*   March 30, 2022

Power BI Blog: Not Imported
===========================

Power BI Blog: Not Imported
===========================

31 March 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at an issue when importing data from Excel._

Consider the following Excel data:

![](<Base64-Image-Removed>)

In Power BI, I can ‘Import data from Excel’.

![](<Base64-Image-Removed>)

This takes me to a browser window where I can select my file, and I choose the Excel Workbook and see the data on the Navigator dialog:

![](<Base64-Image-Removed>)

In [Power BI Blog: Fully Imported](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-fully-imported)
, I described how I could load the whole Excel data model by accessing the File tab. To show why this should only be used when there is a data model to be preserved, I will repeat the process for this simpler Excel workbook:

![](<Base64-Image-Removed>)

On the Import tab, there is an option to Import from ‘Power Query, Power Pivot, Power View’. I choose this option, and if I haven’t already saved my current Power BI file, I may get a warning:

![](<Base64-Image-Removed>)

Having saved my Power BI file, I browse and choose my Excel Workbook:

![](<Base64-Image-Removed>)

I choose Start, and Power BI updates me as it progresses:

![](<Base64-Image-Removed>)

This time however, I don’t get the results I was looking for:

![](<Base64-Image-Removed>)

Notice the name of the option on the Import tab:

![](<Base64-Image-Removed>)

I have no queries, so the data cannot be uploaded this way. Clearly the best way to import this data, is to use the ‘Import from Excel’ option I started with, which can also be accessed from the ‘Get Data’ dropdown. The Import ‘Power Query, Power Pivot, Power View’ option is not designed to cope with this. Let’s see what happens if I persist with this method…

If I extract all my data to queries in the Excel Workbook using ‘From Table/Range’ on the ‘Get & Transform’ section of the Data tab:

![](<Base64-Image-Removed>)

I can then ‘Close and Load To’ from the Power Query Editor:

![](<Base64-Image-Removed>)

I don’t need two copies of the data, so I only create a connection:

![](<Base64-Image-Removed>)

Having done this for all the data I want to import, I can save and close the Excel Workbook and try again, and this time I get an extra step:

![](<Base64-Image-Removed>)

I can opt to ‘Keep connection’:

![](<Base64-Image-Removed>)

I am then prompted to ‘Apply changes’:

![](<Base64-Image-Removed>)

The Fields pane doesn’t look promising!

![](<Base64-Image-Removed>)

If I choose to ‘Transform data’ from the Home tab, the data is in the Power Query editor:

![](<Base64-Image-Removed>)

Everything is in italics in the Queries pane, so I can ‘Enable Load’ for Table5 by right-clicking:

![](<Base64-Image-Removed>)

It then appears in the Fields pane:

![](<Base64-Image-Removed>)

Now, what if I had used ‘Copy data’ instead:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

The tables with the information option have not been copied as they are too large, the connection has been kept instead. The results are actually worse this way; not only is everything still set not to load, but some of the data hasn’t been copied in the correct format:

![](<Base64-Image-Removed>)

Only use the Import ‘Power Query, Power Pivot, Power View’ option to import data from Excel when there is a data model and relationships to preserve. Power Query really is the best tool for importing Excel data to Power BI in all other circumstances!

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-not-imported/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-not-imported/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-not-imported/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-not-imported/#0)

[](https://sumproduct.com/blog/power-bi-blog-not-imported/#0 "close")

top