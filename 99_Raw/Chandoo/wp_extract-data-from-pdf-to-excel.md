# Convert PDF data to Excel - One file or combine many - Easy process

**Source:** https://chandoo.org/wp/extract-data-from-pdf-to-excel

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

Extract data from PDF to Excel – Step by Step Tutorial
======================================================

*   Last updated on April 14, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![get data from pdf to excel](https://chandoo.org/wp/wp-content/uploads/2021/04/get-data-from-pdf-to-excel.jpg)

In this tutorial learn how to,

*   Extract tabular data from one PDF to Excel
*   Combine and extract tables from multiple PDFS to Excel

We will be using Excel 365 & Power Query to do this. If you have different version of Excel (2016, 2013 or older), read the FAQ section at the end for another way to do this.

How to extract PDF table to Excel
---------------------------------

_**Optional:**  If you need a sample PDF to practice these concepts, use the randomly made credit card statements I created._ [Download them from here](https://chandoo.org/wp/wp-content/uploads/2021/04/sample-PDF-credit-card-statements.zip)
.

### Step 1: Go to Data ribbon & click on Get Data > File > PDF

From data ribbon, use the PDF option  and point to the location on your computer (or web address).

![data from PDF option - power query get data excel](https://chandoo.org/wp/wp-content/uploads/2021/04/data-from-PDF-option-power-query-get-data-excel.png)

### Step 2: Select the table(s) you want in the navigator screen

Power Query will open up a **navaigator** screen. Just specify the table(s) you want. Refer to below illustration to know more about the navigator screen.

![navigator screen for pdf - power query](https://chandoo.org/wp/wp-content/uploads/2021/04/navigator-screen-for-pdf-power-query.png)

**💡 Bonus tip: Use the composite table** if you want to get a data table in your PDF that spans multiple pages. This is excellent for bank or credit card statements.

### Step 3: Load or Transform data

If the preview in navigator looks satisfactory, just load it. Otherwise, click on “Transform data” to open query editor to make any final adjustments.

Combine & Extract data from multiple PDFs
-----------------------------------------

### Step 0: Place all your PDFs in a folder

### Step 1: Folder connection

Instead of PDF option, use the Folder option in the Get Data.

![from folder option - get data - power query - excel](https://chandoo.org/wp/wp-content/uploads/2021/04/from-folder-option-get-data-power-query-excel.png)

### Step 2: Choose “Combine” in file listing screen

Power Query will show you a screen with a list of all files it found in the folder. Choose any of the combine options here to combine the data from all files to one table.

![File listing screen - Power Query - Folder connection option](https://chandoo.org/wp/wp-content/uploads/2021/04/folder-connection-file-listing-power-query.png)

### Step 3: Select the table you want from Transfer Sample Screen

Now, you will see another _navigator_ like screen. Just select the table you want in here. Power Query will go to each file in the folder, get the same table and combine them.

### Step 4: Load or Edit the query

And enjoy.

Practice PDF Credit Card Statements
-----------------------------------

_If you need a sample PDF to practice these concepts, use the randomly made credit card statements I created._ [Download them from here](https://chandoo.org/wp/wp-content/uploads/2021/04/sample-PDF-credit-card-statements.zip)
.

Video - Convert PDF to Excel
----------------------------

Still not sure how to extract data tables from PDF to Excel? Watch this short video and get it. See it below or [on my YouTube channel](https://youtu.be/5I0pnj_-LLA)
.

PDF to Excel - FAQs
-------------------

**I don’t have PDF option in my Excel. What do I do?**

You can use free Power BI Desktop to do the same. ([Download Power BI for free here](https://powerbi.com/)
)

Once you have Power BI, open it, go to Get Data > PDF and follow the same steps as above tutorial.

Instead of loading the data, copy the entire table from Query Editor and paste it to Excel. See below illustration.

![copy entire table - power query in Power BI](https://chandoo.org/wp/wp-content/uploads/2021/04/copy-entire-table-power-query-in-Power-BI.png)

**I have new files, how do I refresh?**

Just place the files in the same folder.

Go to Excel and right click on the extracted table and select “Refresh”. Excel will update the details.

**I want to exclude certain files in the folder when combining…**

Open the query editor and go to the query that is responsible for your combining PDF process. Go to source step. This will show all the files in the folder. 

Include a filter condition here. Power Query will warn about inserting a step. Proceed and you will be able to exclude files based on conditions.

Examples:

*   Process files that have file name starting with certain letters
*   Files created after certain date
*   Having specific extension.

_Remember: Power Query is case sensitive._  

**I want to pre-process or clean-up data before loading it into Excel**

Open the query editor and add any necessary data transformation steps at the end. 

Examples:

*   Removing all foreign currency transactions from credit card statements
*   Cleaning up account codes
*   Rearranging columns in the PDF data table

For more on what you can do with [Power Query, check out this tutorial](https://chandoo.org/wp/power-bi-play-date-is-here/)
.

**Other questions…**

Post a comment and I will try to help you.

**More examples on Power Query…**

*   [Introduction & 4 full examples of Power Query](https://chandoo.org/wp/power-query-tutorial/)
    
*   [Combine files with Power Query](https://chandoo.org/wp/combine-excel-files-using-power-query/)
    
*   [Extract common values between two tables](https://chandoo.org/wp/compare-two-tables/)
    
*   [5 Power Query tips for accounting & finance people](https://chandoo.org/wp/power-query-tips-for-accountants/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/extract-data-from-pdf-to-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-data-from-pdf-to-excel/#respond)
    
*   Tagged under [consolidation](https://chandoo.org/wp/tag/consolidation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [pdf](https://chandoo.org/wp/tag/pdf/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPrevious10 Advanced IF formula tricks you must know](https://chandoo.org/wp/advanced-if-tricks/)

[NextGetting Started with Power Pivot & DAX – FREE Live MasterclassNext](https://chandoo.org/wp/powerpivot-dax-free-live-event/)

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
    
    [Reply](https://chandoo.org/wp/extract-data-from-pdf-to-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-data-from-pdf-to-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-data-from-pdf-to-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ