# Make a Pivot from Another Pivot Table in Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

Make a Pivot from Another Pivot Table in Excel
==============================================

*   Last updated on June 25, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Recently, a client shared data with me that is clearly a pivot table and wanted me to make another pivot from it using Excel. This is a common and annoying problem we all face when working with Excel. Today, let me share my approaches for creating a pivot from another pivot report using Excel.

![pivot from another pivot table in Excel - howto](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)

Option 1: If you have access to “original” data
-----------------------------------------------

Ha, I know, but we _can_ dream eh? So, if you do have access to the original data from which the pivot is generated, just use that data and make the new pivot as you want.

If you need help creating a pivot report in the first place, [learn the process here](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
.

* * *

Option 2: Making a Pivot from Another Pivot when you don’t have access to original data
---------------------------------------------------------------------------------------

Tbh, this is the real scenario for most of us. We have a pivot and don’t have access to the data that was used to make it. Now we need to make another pivot. In this case, follow the below steps.

Pivot from Another Pivot – FREE Excel Template
----------------------------------------------

[![free excel template - pivot from pivot](https://chandoo.org/wp/wp-content/uploads/2025/06/download-excel-template-pivot-from-another-pivot.png)](https://chandoo.org/wp/wp-content/uploads/2025/06/pivot-from-another-pivot.xlsx)

I created a free Excel template to guide you thru the process with sample data. **[Download it here](https://chandoo.org/wp/wp-content/uploads/2025/06/pivot-from-another-pivot.xlsx)
** and use the sample data to understand the process better.

### Step 1: Select and name your pivot range

1.  Select the entire pivot table (including any headers) in Excel.
2.  Go to the name box (next to formula bar on the left)
3.  Type the name “pivot\_range”
4.  Pro tip: If you have multiple pivots, you can use names like “pivot\_range1”, “pivot\_range2”

See this illustration for the step.

![creating a named range for pivot data](https://chandoo.org/wp/wp-content/uploads/2025/06/Snag_b8381c09.png)

### Step 2: Go to Data Ribbon and load up the “pivot” to Power Query

1.  Keep the pivot table selected
2.  Go to Data Ribbon
3.  Click on “From Table/Range” option in the Get & Transform Data area

This will load the Power Query Editor with your Pivot Table Data.

![loading "pivot_range" to Power Query](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0158.png)

### Step 3: Let’s “unpivot” the Pivot Table with Power Query

Now that our “pivot table” is in Power Query, we can “unpivot” it and create a regular table. This can be used to make our new pivot table.

Here is a snapshot of how the Power Query editor looks with the pivot\_range data.

![Power Query editor with pivot data](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0159.png)

### \[optional step\] Promote headers if needed

Depending on how your source Pivot is setup, you may need to adjust the column headings in Power Query. For example, in my case, I need to promote the headers. To do this, click on “Use First Row as Headers” button in the Home ribbon of Power Query editor.

See below illustration.

![fixing the headers with "use first row as header" option](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0160.png)

### Step 4: Replace “null” with value from above

In my sample pivot, you can see that Rep name is not printed in all rows, just the first row. This shows up as _null_ in the Power Query editor for rest of the rows. We just need to fill these down based on the top value.

*   Select the column(s) with this problem
*   Go to “Transform” ribbon in Power Query Editor
*   Click on “Fill” and select Down to fill down all the nulls with the value from above

![Filling nulls with value from above - Before vs. After](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0161.png)

### Step 5: Remove rows with “totals” & “sub-totals”

We don’t need totals or sub-totals any more. We will calculate them in the new pivot as needed. For now, let’s remove all the rows and columns that have totals.

1.  Select the first column that has “total” labels
2.  Click on “filter” button
3.  Uncheck any total labels.
4.  Repeat the steps for any other rows that need this clean-up step.
5.  Pro tip: Use Text Filters > Does not contain to filter out all rows with “total” word in them.

![removing total and sub-total rows.](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0163.png)

### Step 6: Remove Grand total / Sub-total columns (if any)

Let’s also remove any “grand total” columns and “sub-total” columns from our pivot report. Right click on the column with totals and select “remove” to take this column out.

![removing any grand total and sub-total columns](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0164.png)

### Step 7: Unpivot the data

Finally, our pivot report is ready to be unpivoted.

1.  Select the column(s) with row labels. In the above example, I selected “representative” and “day of week” columns
2.  Pro Tip: Hold SHIFT or CTRL to select multiple columns in one go.
3.  Right click on the column headings of either column.
4.  Select “unpivot other columns”
5.  This should reshape the pivoted data to unpivoted format.
6.  See this quick demo (GIF):

![unpivoting / depivoting the data- quick demo](https://chandoo.org/wp/wp-content/uploads/2025/06/2025-06-25_12-16-26.gif)

### Step 8: Rename the new “attribute” & “value” columns

Double click on the newly added “attribute” and “value column headers to rename them to appropriate labels. In my case, I named them – Gender & Calls.

![renaming columns in Power Query (pivot from pivot)](https://chandoo.org/wp/wp-content/uploads/2025/06/rename-columns-pq.png)

### Step 9: Load the data back to Excel so we can make the pivot

Ok. We are done. Just load the data back to Excel. To do this, go to “Home” ribbon and click on “Close & Load” button.

![loading tabular data to Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0165.png)

### Step 10: Create the Pivot from the loaded data

Once the data is in Excel, just select any cell in the data, go to Insert > Pivot Table (shortcut: ALT N V T) and set up the pivot as per your needs. In my case, I needed the pivot report with number of calls by Day of Week & Representative. So here is how I made it (see the quick video demo).

* * *

Things to keep in mind:
-----------------------

The Power Query based approach to create pivot from another pivot is great, but you need to keep a few things in mind.

*   **Doesn’t work for averages:** If your original pivot table has “averages” instead of “sums”, the new pivot will not be correct. This is because you will make the mistake of “averaging averages”. This technique works great for sums & counts only. Any other measures like average / median / min /max, you need “actual” data to make the new pivot.
*   **Power Query steps can get complicated:** If your original pivot has a very complex, nested layout, then the PQ steps needed to “transform” data can be complex (but not impossible). I suggest learning how to use Power Query to solve such issues. [Refer to this article](https://chandoo.org/wp/power-query-tutorial/)
     or [video](https://youtu.be/MMdcczmULrU)
     to start your PQ journey.
*   **Needs refresh for data changes:** If your original Pivot table changes (new values or new rows / columns), you need to update the “pivot\_range” named range and refresh the power query data.
    *   **To update the named range:** Go to Formula ribbon in Excel and click on “Name Manager”. Select the name “pivot\_range” and edit it. Adjust the cell references as per your newly updated pivot.
    *   **To Refresh Power Query:** Right click on the Power Query data you have loaded in Step 9. Select “Refresh’ to update the loaded data with new changes. Now go to the pivot you made (in step 10) and refresh that too (you guessed it right! Right click and Refresh).

What to do if you get an error (in Power Query):
------------------------------------------------

Errors can happen either during the initial process (steps 3 to 9) or when you refresh the power query connection. Solving the error depends on your exact pivot table layout and what changes were made. But here are the most likely reasons for the error.

*   **Column names have changed:** You will get error if your columns (in the original pivot) were changed between updates. Adjust the names in the original pivot or go to Power Query editor, locate the step where the error is happening and adjust the names there.
*   **Data type issues:** If for some reason, your original pivot’s values are read by Power Query as “text”, it can create issues. Right click on the columns with numbers and explicitly convert them to numbers in PQ.
*   **Layout changes:** If your pivot layout changes (say, instead of 2 columns, it now has 3 columns of row labels), then your refresh will fail. You need to select one more column before unpivoting (step 7).
*   **Other issues:** Leave a comment with the issue / error you are facing so I can help.

Pivot from Another Pivot – FREE Excel Template
----------------------------------------------

[![excel template - pivot from pivot](https://chandoo.org/wp/wp-content/uploads/2025/06/download-excel-template-pivot-from-another-pivot.png)](https://chandoo.org/wp/wp-content/uploads/2025/06/pivot-from-another-pivot.xlsx)

I created a free Excel template to guide you thru the process with sample data. **[Download it here](https://chandoo.org/wp/wp-content/uploads/2025/06/pivot-from-another-pivot.xlsx)
** and understand the process better.

In conclusion:
--------------

Power Query in Excel offers an elegant, simple and easy way to deal with the annoying issue of using “pivot tables” as data source. I had plenty of success with this method and I hope will too. If you do have any questions or face issues during the process, leave a comment.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [2 Comments](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [unpivot](https://chandoo.org/wp/tag/unpivot/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousHow to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[NextNew Zealand GST Calculation with Excel \[Free Template\]Next](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

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
    
    [Reply](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ