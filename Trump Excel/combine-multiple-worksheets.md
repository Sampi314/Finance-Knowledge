# Combine Data From Multiple Worksheets into a Single Worksheet in Excel

**Source:** https://trumpexcel.com/combine-multiple-worksheets

---

[Skip to content](https://trumpexcel.com/combine-multiple-worksheets/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combine-multiple-worksheets/#below-title)

I recently got a question from a reader about combining multiple worksheets in the same workbook into one single worksheet.

I asked him to use [Power Query](https://trumpexcel.com/power-query-course/)
 to combine different sheets, but then I realized that for someone new to Power Query, doing this can be tough.

So I decided to write this tutorial and show the exact steps to combine multiple sheets into one single table using Power Query.

Below a video where I show how to combine data from multiple sheets/tables using Power Query:

Below are written instructions on how to combine multiple sheets (in case you prefer written text over video).

Note: [Power Query](https://trumpexcel.com/power-query/)
 can be used as an add-in in Excel 2010 and 2013, and is an inbuilt feature from Excel 2016 onwards. Based on your version, some images may look different (image captures used in this tutorial are from Excel 2016).

![Combine Data from Multiple sheets into one single sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20400'%3E%3C/svg%3E)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Combine Data from Multiple Worksheets Using Power Query
-------------------------------------------------------

When combining data from different sheets using Power Query, it’s required to have the data in an [Excel Table](https://trumpexcel.com/excel-table/)
 (or at least in [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
). If the data is not in an Excel Table, the method shown here would not work.

Suppose you have four different sheets – East, West, North, and South.

Each of these worksheets has the data in an Excel Table, and the structure of the table is consistent (i.e., the headers are same).

![Combine Data from Multiple sheets - Data in Excel Tables](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20427'%3E%3C/svg%3E)

**[Click here to download the data and follow along](https://www.dropbox.com/s/g4jkc657l9oa0q0/Region%20wise%20Sales%20Data.xlsx?dl=0)
**.

This kind of data is extremely easy to combine using Power Query (which works really well with data in Excel Table).

For this technique to work best, it’s better to have names for your Excel Tables (work without it too, but it’s easier to use when the tables are named).

I have given the tables the following names: _East\_Data, West\_Data, North\_Data, and South\_Data_.

Here are the steps to combine multiple worksheets with Excel Tables using Power Query:

1.  Go to the Data tab.![Combine Data from Multiple sheets - Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20198'%3E%3C/svg%3E)
2.  In the Get & Transform Data group, click on the ‘Get Data’ option.![Combine Data from Multiple sheets - Get Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20168'%3E%3C/svg%3E)
3.  Go the ‘From Other Sources’ option.
4.  Click the ‘Blank Query’ option. This will open the Power Query editor.![Combine Data from Multiple sheets - Blank Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20286%20505'%3E%3C/svg%3E)
5.  In the Query editor, type the following formula in the formula bar: **\=Excel.**CurrentWorkbook**()**. Note that the Power Query formulas are case sensitive, so you need to use the exact formula as mentioned (else you will get an error). ![Combine Multiple sheets - Excel CurrentWorkbook formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20223'%3E%3C/svg%3E)
6.  Hit the Enter key. This will show you all the table names in the entire workbook (it will also show you the named ranges and/or connections in case it exists in the workbook).![Combine Multiple sheets - List of tables](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20194'%3E%3C/svg%3E)
7.  _**\[Optional Step\]**_ In this example, I want to combine all the tables. If you want to combine specific Excel Tables only, then you can click the drop-down icon in the name header and select the ones you want to combine. Similarly, if you have named ranges or connections, and you only want to combine tables, you can remove those named ranges as well.
8.  In the Content header cell, click on the double pointed arrow.![Combine Multiple sheets click on the double pointed arrow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20194'%3E%3C/svg%3E)
9.  Select the columns that you want to combine. If you want to combine all columns, make sure (Select All Columns) is checked.
10.  Uncheck the ‘Use original column name as prefix’ option.![Uncheck Use Original Column name as prefix in Power Query Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20468'%3E%3C/svg%3E)
11.  Click OK.

The above steps would combine the data from all the worksheets into one single table.

![Combined data from all the worksheets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20884%20488'%3E%3C/svg%3E)

If you look closely, you’ll find the last column (rightmost) has the name of the Excel tables (East\_Data, West\_Data, North\_Data, and South\_Data). This is an identifier that tells us which record came from which Excel Table. This is also the reason I said it’s better to have descriptive names for the Excel tables.

Here are a few modifications you can do to the combined data in Power Query itself:

1.  Drag and place the Name column to the beginning.
2.  Remove the “\_Data” from the name column (so you’re left with East, West, North, and South in the name column). To do this, right-click on the Name header and click on Replace Values. In the  Replace Values dialog box, replace \_Data with a blank.
3.  Change the Data column to show only dates (and not the time). To do this, click the Date column header, go to the ‘Transform’ tab and change the Data type to Date.
4.  Rename the Query to ConsolidatedData.

Now that you have the combined data from all the worksheets in Power Query, you can load it in Excel – as a new table in a new worksheet.

To do this. follow the below steps:

1.  Click the ‘File’ tab.
2.  Click on Close and Load To.![Close and Load to in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20213%20227'%3E%3C/svg%3E)
3.  In the Import Data dialog box, select Table and New worksheet options.![Combine Multiple Sheets in Excel - Import Data dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20387%20351'%3E%3C/svg%3E)
4.  Click Ok.

The above steps would combine data from all the worksheets and give you that combined data in a new worksheet.

#### One Issue You Must Resolve when Using This Method

In case you have used the above method to combine all the tables in the workbook, you’re likely to face an issue.

See the number of rows of the combined data – 1304 (which is right).

![Combine Multiple sheets number of rows when loaded first time](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20235'%3E%3C/svg%3E)

Now, if I refresh the query, the number of rows changes to 2607. Refresh again and it will change to 3910.

![Combine Multiple sheets number of rows when refreshed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20235'%3E%3C/svg%3E)

Here is the problem.

Every time you refresh the query, it adds all the records in the original data to the combined data.

Note: You’ll face this issue only if you have used Power Query to combine **ALL THE EXCEL TABLES** in the workbook. In case you selected specific tables to be combined, you’ll not face this issue.

**Let’s understand the cause of this problem and how to correct this.**

When you refresh a query, it goes back and follows all the steps that we took to combine the data.

In the step where we used the formula **\=Excel.CurrentWorkbook()**, it gave us a list of all the tables. This worked fine the first time as there were only four tables.

But when you refresh, there are five tables in the workbook – including the new table that Power Query inserted where we have the combined data.

So every time you refresh the query, apart from the four Excel Tables that we want to combine, it also adds the existing query table to the resulting data.

This is called recursion.

Here is how to solve this issue.

Once you insert =Excel.CurrentWorkbook() in the  Power Query formula bar and hit enter, you get a list of Excel Tables. To make sure you only get to combine the tables from the worksheet, you need to somehow filter only these tables that you want to combine and remove everything else.

Here are the steps to make sure you only have the required tables:

1.  Click the drop-down and hover the cursor on Text Filters.
2.  Click on the Contains option.![Combine Data from Multiple sheets - Filter data to avoif recursion](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20744%20458'%3E%3C/svg%3E)
3.  In the Filter Rows dialog box, enter \_Data in the field next to the ‘contains’ option.![Filter Rows in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20873%20345'%3E%3C/svg%3E)
4.  Click OK.

You may not see any change in the data, but doing this will prevent the resulting table from being added over again when the query is refreshed.

Note that in the above steps we have used “**\_Data**” to filter as we named out tables that way. But what if your tables are not named consistently. What if all the table names are random and have nothing in common.

Here is the way to solve this – use the ‘does not equal’ filter and enter the name of the Query (which would be ConsolidatedData in our example). This will ensure that everything remains the same and the resulting query table which is created is filtered out.

Apart from the fact that Power Query makes this entire process of combining data from different sheets (or even the same sheet) quite easy, another benefit of using it that it makes it dynamic. If you add more records to any of the tables and refresh the Power Query, it will automatically give you the combined data.

Important Note: In the example used in this tutorial, the headers were same. In case the headers are different, Power Query will combine and create all the columns in the new table. If the data is available for that column, it will be shown, else it will show null.

**You May Also Like the Following Power Query Tutorials:**

*   [Combine Data from Multiple Workbooks in Excel (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    .
*   [How to Unpivot Data in Excel using Power Query (aka Get & Transform)](https://trumpexcel.com/unpivot-data/)
    
*   [Get a List of File Names from Folders & Sub-folders (using Power Query)](https://trumpexcel.com/list-file-names-power-query/)
    
*   [Combining Two Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)
    
*   [Merge Tables in Excel Using Power Query.](https://trumpexcel.com/merge-tables/)
    
*   [How to Compare Two Excel Sheets/Files](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Switch Between Sheets in Excel? (7 Better Ways)](https://trumpexcel.com/switch-between-sheets-excel/)
    
*   [Combine CSV Files With Inconsistent Column Headers](https://trumpexcel.com/power-query/combine-csv-inconsistent-headers/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

29 thoughts on “Combine Data From Multiple Worksheets into a Single Worksheet in Excel”
---------------------------------------------------------------------------------------

1.  Thank you. great explanation!!!  
    made my day
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-14803)
    
2.  One issue i have is to eliminate the blank rows from the source tables (from multiple excel files). Each table has about 500 rows predefined, but current data is about 100 rows and keeps growing. So my consolidated file has about 5000 rows (blanks are imported as “null”) from 10 different files where as the real data is about 600 rows all together. How do i limit my power query to load only legitimate rows ignoring blanks. Thank you for any help!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-14639)
    
3.  Sir – this video was absolutely perfect. Thank you so much for the easy to follow explanation. Helped me out tremendously.
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-14365)
    
4.  Followed step by step up to entering formula =Excel.CurrentWorkbook()…which did not return the tables in the workbook that I want to append into one table…in fact only two error returned  
    baffled
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-14328)
    
5.  This documents helped my query. Thanks
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-13938)
    
6.  This just saved me loads of time at work! Thank you so much
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-13923)
    
7.  Hi Friend, thanks a lot for your guide in this tutorial. But I’m having a problem to combine my data file. Everything’s goes fine, until =Excel.CurrentWorkbook. Whereas it shown “Error” under Content header, and there’s no Double Point Arrow. May you help me regarding this issue?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-13569)
    
8.  How to code for Pivot Table using excel VBA?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-13078)
    
9.  What about the steps in Excel 2016.Getting date format error when using combine binary option.
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-13065)
    
10.  Hi mate, thanks for your help, this was useful. I am having an issue where i’ve imported all the tables as per your instructions, but refreshing the query does not work. Do you have any tips? Thanks
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-12732)
    
11.  Really helpful… just a pity that MS don’t provide the same functionality on Mac as they do in Windows…
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-12409)
    
12.  This has been really helpful! Thank you for the guidance!!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-12404)
    
13.  Rinardo
    
    This has been a tremendous help! Although I do have a question, I am trying to combine 4 worksheets into a single table and all three have columns labeled as “Warehouse”, “Count Date” and “ABS ($ VARIANCE”). The information from all 4 sheets is being pulled into my consolidated table with the exception of some of the count dates. When I look back at my query, some of the rows are returning a “null” value for some of the dates, thus leaving the cell blank in my consolidated table. Would you be able to provide insight on how I can correct this issue?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-12090)
    
14.  Great explanation with clear steps. Appreciate your help!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11801)
    
15.  This is great thank you.  
    I need some help with combining only certain info from Worksheets into one workbook – do you have a tutorial on that also perhaps?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11783)
    
16.  Hi. This is very informative. I have a question I removed a row from the source data but it the row remained in the combined table because of the added row with the table name. Do you know how I would remove the row completely in the combined table when removing a row from one of the source tables?
    
    Thanks so much  
    Mary
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11635)
    
17.  fantastic
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11578)
    
18.  This was fantastic. It was exactly what I needed and worked just as described. I have a different version of excel but it was easy enough adjust. This is going to be a huge time saver for me!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11505)
    
19.  it is good but I have excel 2016 So I am facing a problem. There is the different step
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11309)
    
    *   how is work with excel 2016
        
        [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11310)
        
20.  Just what I needed – very easy to follow and worked like a dream – thanks!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11260)
    
21.  This was extremely helpful and I did a test on my computer – worked wonderfully. I work for a company that uses google drive – is there a way to do this with google sheets?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11216)
    
22.  Wow – great stuff. Have excel 2010 and had to download the query add-on but it works.  
    However – it was a bit cumbersome trying to figure out how to actually do this. With the add-on, it will not show the “current workbook” at least it didn’t on my couple tries. So instead of loading a “blank query,” I started with “start query from file” and then selected the file I wanted.” In the “NAVIGATOR” I selected the whole folder (i.e. workbook) not an individual sheet.
    
    From there, I had to go to “EDIT QUERY.” Then, I had to figure out how to delete the columns in the query in order to get the same two columns (“CONTENT” (table) and “Name” (sheet name).” From there, I right clicked on the “double arrow” as explained above. It preloaded all the columns and I hit “OK.” Now I was able to simply “RENAME” each column with the headers I needed from each of the sheets. Then I clicked “Close and Load” and done.
    
    Thanks again for this post!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11172)
    
23.  too complicated …did not work, but then i had an emergency ,maybe if i had spent some time ,could have worked
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11129)
    
24.  This method worked fine, until I was going to load it to a new sheet, then Excel crashes. Can I get around this, I wonder?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11021)
    
25.  Hi, it took me a while but I finally got through, although not as neat as you. For some reason my column names changed to Data.Column1, Data.Column2 etc. while my regular headers became text and are mixed in in my data now. When I change the names from DataColumn1 etc to the original names and save it, they will reverse back to DataColumn1,2,3…etc. as soon as I refresh. Any ideas?
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-10756)
    
    *   You can rename each name for the “DataColumn1” etc. by editing the query and right-clicking the column name. Look toward the bottom of the pop-up context menu. Click on “Rename” with the header names you like and voila – it’s done. Then, once you close and load the sheet, you can simply erase rows 1-2 which are likely the rows you didn’t want/need. Hope that helps.
        
        [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-11173)
        
26.  This is great – THANKS !!!!!!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-10716)
    
27.  This was awesome! Thank you!
    
    [Reply](https://trumpexcel.com/combine-multiple-worksheets/#comment-10255)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/combine-multiple-worksheets/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK