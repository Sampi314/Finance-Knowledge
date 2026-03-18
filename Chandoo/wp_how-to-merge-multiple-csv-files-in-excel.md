# How to Merge Multiple CSV Files in Excel (Step-by-Step Guide)

**Source:** https://chandoo.org/wp/how-to-merge-multiple-csv-files-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

How to Merge Multiple CSV Files in Excel (Step-by-Step Guide)
=============================================================

*   Last updated on June 11, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0138.png)

Have a bunch of CSV files in a folder and want to merge or combine them to one big file? Follow these simple instructions to combine multiple CSV files in to one spreadssheet using Microsoft Excel (2016 or above).

What you need?
--------------

*   A folder with CSV files (click here to download sample files, if you need some)
*   Microsoft Excel (2016 or above version)

![folder of CSV files we want to merge](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0139.png)

Method 1: Merge CSV Files using Power Query (Recommended)
---------------------------------------------------------

This is by far the easiest and quickest way to combine data from CSV files in a folder using Excel.

Follow these steps:

1.  **Close any opened CSV files**: Before proceeding, close any of the opened CSV files. Make a note of the folder path too.
2.  **Open Excel and make a new file:** This will be our merged CSV data file. Here, we will setup Power Query to combine all the files.
3.  Go to Data Ribbon > Get Data and click on **From Folder**

![Get data from folder option in Excel Power Query](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0140.png)

Paste the folder path or navigate to the folder and click “select”.

4.  **For simple CSV files:** If your CSVs are already clean and you just want to merge them, select the Combine > Combine & Load option.
5.  **For complex CSVs or if you need to clean-up data before merge**: Select the Combine > Combine & Transform Data option. This will open up “Power Query Editor” so you can clean up data or apply “transformations”.

![Combine & Load options in Excel Folder Merge](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0141.png)

6.  Click “OK” in the next screen: This next screen shows a sample of your data (usually the first file) so you can confirm to Excel how your data looks. If your delimiter is not comma (for example, you have TSV files instead of CSV), you can also tell Excel about that using this screen.

![Use this screen to tell Excel about your file and delimiter structure. ](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0142.png)

7.  **If you selected “Combine & Load” option:** Your merge is done! The combined data from your CSV files is now loaded into Excel. This is how it will look (see below). You can use the “Source name” column to figure out which file each row came from.

![Example merged CSV files in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0143.png)

For “Advanced” Merge Scenarios – Combine & Transform Data
---------------------------------------------------------

If your CSV files are not so simple or you want to _further_ clean-up data after merging, you can follow these steps.

Select the “Combine & Transform Data” option in after Step 3 (ie once you point the folder). This will take you to Power Query editor (after you confirm the file details, as shown in step 6 above).

Once you are in Power Query Editor screen, you can apply any data clean-up and transformation steps on your data easily. I will share a few examples below. But refer to my [Power Query tutorial page](https://chandoo.org/wp/power-query-tutorial/)
 or [video](https://youtu.be/UAFExySaSPY)
 for detailed information on how to use Power Query for data cleaning and transformations.

### Example 1: Removing the “Total” column from merged CSV files

Let’s say you don’t want the “total” column from these merged budget files. In the Power Query editor, right click on the “total” column and select “remove”. This will remove the total budget column. Don’t worry, it is not going to remove data from original CSV files. But when you merge the data, you won’t just see the “total” column.

![Removing unwanted columns in merged CSV Data](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0144.png)

### Example 2: Reshaping the 12 columns to month & value column structure

While the 12 monthly column structure works best for gathering budget data, it may not be ideal for data analysis. So let’s reshape our merged data to a format like this:

*   File name
*   Budget Category
*   Month
*   Budget value

Essentially, each row of the data in original CSV file becomes 12 rows in merged file. This process is caleld “unpivoting”. It looks like this:

![how unpivoting works - illustration](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0145.png)

**To unpivot data in Power Query Editor**:

1.  Select the file name & cost category columns (and any other columns you want to retain).
2.  Tip: You can hold Shift or CTRL to multi-select columns in Power Query Editor.
3.  Right click on the selected columns and select “Unpivot _other_ columns” option.

![Unpivoting budget data in the merged CSV files](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0146.png)

This will replace the 12 monthly columns with a new “Attribute” and “Value” columns. These are nothing but our Month and Budget columns!

![After unpivot - much better combined CSV file](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0147.png)

**Renaming the columns:** You can double click on the column header and rename it to Month and Budget.

Load combined CSV data to Excel:
--------------------------------

When you finish the data clean up and transformations you want to do, go to the Home ribbon in Power Query editor and click on “Close & Load” to bring the finalized data to Excel.

![How to load merged or combined data to Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0148.png)

Why this method is the best?
----------------------------

I have been using (and advocating) Power Query for more than 10 years. I can’t tell you how much time and effort this little trick has saved me. Here are my top reasons for why Power Query is the best way to merge CSV files.

*   **Fully Dynamic:** You don’t need to worry about changing files or growing (or even shrinking) data. Once you properly set up the Power Query connection, your data will be merged _automatically_ even if there are 1000s of files.
*   **Automated:** One of the biggest challenges with data merges like this is that your raw data files change often. With Power Query, updating the “merged” dataset is really simple. Open the merged file, right click anywhere on the merged data table and select “Refresh” to automatically update the merged CSV data.

![Refreshing or updating merged CSV data when the folder changes or you have new files](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0149.png)

*   **Works even if the columns are out of order**\*: This method works just as perfectly even if your CSV files have columns in jumbled order, _as long as the column headings are same across files._ That means if file 1 has “Cost category” as column 1 and file 3 has “Cost category” as column 14, the merge still works, as the column heading is matching in both cases. I talk about how to deal with more complex situations of [mismatched headers in this video.](https://youtu.be/ECtJQDc8uF8)
    

Other ways to combine or merge CSV files with Excel
---------------------------------------------------

We can also use below techniques to merge CSV files with Excel (I prefer Power Query btw).

*   **Using VBA Macros to combine CSV files:** Excel’s own coding language – VBA offers a powerful and proven way to combine multiple files (CSV, Text or even other Excel files) and get merged data in one place. This is an advanced method and not really recommended for beginners. Refer to this article for a detailed step-by-step instruction on [how to combine data with Excel VBA](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/)
    
*   **Manual Copy Pasting:** For something quick and dirty, you can also manually open the CSV files and copy paste the data into master Excel file. This is an error-prone and labor intensive process and should only be used in one-off cases.
*   **Command Line Utilities:** As CSVs are just text files, you can also use a simple command line utility to combine multiple CSVs to one file. This has the disadvantage of repeating headers and not working when the headers don’t match up or columns don’t align. Here is the command for Windows. This combines the CSV files in the sub-folder “merge csv” to a new file named “combined\_file.csv”.

    copy /b "merge csv"\*.csv combined_file.csv

![DOS command to merge CSV files ](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0150.png)

*   **Using online tools:** Plenty of online tools offer CSV merge functionality. You can upload your files on these websites and they will combine them for you. I suggest checking the privacy policies of these websites and using them only if you can’t apply Power Query or VBA or manual methods. Here are a few that offer this service: [MergeCSV](https://merge-csv.com/)
    , [CSV Combiner](https://csvcombiner.com/)
    

Best Practices when Merging CSV Files (with PQ in Excel):
---------------------------------------------------------

*   **Columns should match (need not be in same order):** The merge options in Power Query work best if your columns match, even if they are out of order across files.
*   **Keep the folder clean:** By default, Power Query is going to combine all the files in the folder you point to. So keep the folder clean and tight. Don’t copy or create files in the folder that you don’t want to merge.
*   **Close files before refresh:** Power Query refresh can fail or miss the files if you keep them open when updating the query. So close everything before you hit refresh.
*   **Data Format Issues (especially with Dates):** If you have CSVs containing dates and these files use different date formats, the merged file can be a mess and throw date formatting issues. Synchronize date and currency formats across files before merging them to avoid such data format issues.

In conclusion – Use Power Query to Merge your CSVs
--------------------------------------------------

Excel’s own Power Query offers a superior, easy and automatic way to combine CSV files. It works beautifully even when combining 1000s of files. For a recent client project, I combined 340 different budget files with Excel Power Query in under 10 minutes. Needless to say, the client’s jaw dropped when they saw the demo!

But for whatever reason, you can’t use Power Query, try either VBA or command line utilities or one of the online CSV combine options.

Bonus: Sample Files & CSV Combine Template
------------------------------------------

If you need a hand with combining CSV files, download my sample data files and CSV combiner template using below links. Unzip the files and adjust folder path in Power Query (source step of the merged query) to make it work with your computer’s path.

*   [CSV Combiner Template](https://chandoo.org/wp/wp-content/uploads/2025/06/merged-data-file.xlsx)
    
*   [Raw Data CSV Files](https://1drv.ms/u/c/e7c6dec249ad257b/EWYiCPTbc1BEv-b-T7AOpjABJ2N7awgpL1n6wmRwjWa-hg?e=QFa8Bp)
    

Resources on Power Query
------------------------

If you want to learn a bit more about what Power Query can do for your data problems, check out below resources:

*   [Power Query Tutorial with 4 AWESOME Examples](https://chandoo.org/wp/power-query-tutorial/)
    
*   [Combine multiple Excel files with Power Query](https://chandoo.org/wp/combine-excel-files-using-power-query/)
    
*   [How to extract common values between two tables in Excel?](https://chandoo.org/wp/compare-two-tables/)
    
*   [Learn Power Query for Excel in 15 minutes – Video](https://youtu.be/UAFExySaSPY)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/how-to-merge-multiple-csv-files-in-excel/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-merge-multiple-csv-files-in-excel/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [combine files](https://chandoo.org/wp/tag/combine-files/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousHow to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[NextHow to use XLOOKUP in Excel?Next](https://chandoo.org/wp/xlookup-examples/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/how-to-merge-multiple-csv-files-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-merge-multiple-csv-files-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-merge-multiple-csv-files-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ