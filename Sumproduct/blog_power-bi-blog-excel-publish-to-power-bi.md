# Power BI Blog: Excel Publish to Power BI

**Source:** https://sumproduct.com/blog/power-bi-blog-excel-publish-to-power-bi/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Excel Publish to Power BI

*   January 30, 2019

Power BI Blog: Excel Publish to Power BI
========================================

Power BI Blog: Excel Publish to Power BI
========================================

31 January 2019

_Last week we showed you how to set up Teams and how it is linked to Power BI. This time, we’re going to talk about linking Teams and Excel, and how you can link it up to Power BI._

In Teams, I’ve created a new team called “SP Blog Example”. Here, I’ve uploaded a couple of files. The first one is our “Data file – PowerPivot example.xlsx” file, which contains our usual cut-down version of the AdventureWorks dataset.

![](<Base64-Image-Removed>)

The second file is a new one that I’ve created called “Excel to Power BI.xlsx”. This file is very simple – it’s just a blank Excel file that has four queries inside, connecting to the AdventureWorks dataset.

![](<Base64-Image-Removed>)

Then, I’ve saved the new file into the SharePoint folder relating to the SP Blog Example team, in the General channel, which is why you see it in the first screenshot.

Now, what we’re going to do is publish this file to Power BI. This is a bit different from creating a PBIX file and publishing that instead. Within Excel, in the File tab, there is a Publish button, giving you options to either Upload or Export your workbook to Power BI. We want to Export it, so that we can create Power BI reports from the Data Model that was created using the four aforementioned queries.

![](<Base64-Image-Removed>)

Once I do this, I’ll see that my file, Excel to Power BI, appears as a new dataset in My Workspace, as follows:

![](<Base64-Image-Removed>)

Now, I can use this dataset to build a report. After clicking on the first action, Create Report, I can build a simple visualisation, plotting sales against the geographical country.

![](<Base64-Image-Removed>)

Whoops – what have I done? It appears that I haven’t set up relationships in my Excel file. Ok, no harm done, we can go back to Excel and set up the relationships we need in Power Pivot, and save the file.

To update Power BI, we now have to… simply sit back and wait for Power BI to update. Because the file is saved on SharePoint and published to Power BI from there, Power BI will regularly check back to the file every hour or two and process any updates to the file. It won’t run a refresh of the Data Model and the queries used, but it will pick up any changes to the file, such as new relationships or calculated columns and measures, and any new tables that might have been created.

<…one hour later…>

![](<Base64-Image-Removed>)

No manual intervention needed!

Come back next week to see how we can publish our reports back to Teams!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-excel-publish-to-power-bi/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-excel-publish-to-power-bi/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-excel-publish-to-power-bi/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-excel-publish-to-power-bi/#0)

[](https://sumproduct.com/blog/power-bi-blog-excel-publish-to-power-bi/#0 "close")

top