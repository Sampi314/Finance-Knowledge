# Excel Speedup & Optimization Tips by Experts

**Source:** https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Excel Speedup & Optimization Tips by Experts \[Speedy Spreadsheet Week\]
========================================================================

*   Last updated on March 26, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

As part of [Speedy Spreadsheet Week](http://chandoo.org/wp/tag/ssw/)
, I have emailed a few renowned Excel experts and asked them to share their tips & ideas to speedup Excel. Today, I am glad to present a collection of the tips shared by them.

![Excel Speedup & Optimization Tips by Experts](https://img.chandoo.org/optimize/excel-expert-tips-for-optimization-speedup.jpg)

Excel Speeding up & Optimization Tips by Hui
--------------------------------------------

**About Hui:**  
Hui (Ian Huitson) has been writing & contributing to Chandoo.org for more than 2 years. Many of you know him from Formula Forensics & Data table related articles on Chandoo.org. See [about Hui](http://chandoo.org/wp/about-hui/)
 page for more about him.

**In no particular order:**

*   Minimize the use of Volatile Functions
*   Organize your workbook layout and data methodically
*   Where possible use fixed values or Named formulas instead of lookups even if the values only change rarely, flag those for manual checking
*   Don’t Start equations with a + that actually adds 0.4% calculation time
*   Minimize use of the Data Table command to running summaries only at the end of a project
*   Review the logic of the model and all if’s or lookup choices for necessity or alternatives
*   Use negatives instead of multiple positives where appropriate in conjunction with If’s and Lookups
*   Learn about Conjunctive Truth Tables, they Rock for reporting
*   Array formulas can do the work of dozens of normal cells, but use cautiously
*   Use Named Formulas and UDF’s instead of multiple Helper Cells/Rows or Columns
*   Minimize of us Conditional Formatting
*   Minimize use of linked workbooks especially if over network drives
*   Take an advanced Excel course like the ExcelHero Academy
*   Minimize the use of Excel 2007

**Links:**

*   [http://www.decisionmodels.com/calcsecretsi.htm](http://www.decisionmodels.com/calcsecretsi.htm)
    
*   [http://msdn.microsoft.com/en-us/library/bb687891.aspx](http://msdn.microsoft.com/en-us/library/bb687891.aspx)
    
*   [http://www.ozgrid.com/News/GoodVsBadDesignSpeedUpEvents.htm](http://www.ozgrid.com/News/GoodVsBadDesignSpeedUpEvents.htm)
    

Excel Speeding up & Optimization Tips by George
-----------------------------------------------

**About George:**  
George runs [Excel Unusual](http://excelunusual.com/)
, where you can learn about using Excel for engineering, simulations & games. In his work, he builds complex spreadsheet models all the time. So I asked him to share a few tactics with us. He wrote 2 articles in response to my request.

**Links:**

*   [http://excelunusual.com/archive/2012/03/about-the-speed-of-spreadsheets-1/](http://excelunusual.com/archive/2012/03/about-the-speed-of-spreadsheets-1/)
    
*   [http://excelunusual.com/archive/2012/03/about-the-speed-of-spreadsheets-2/](http://excelunusual.com/archive/2012/03/about-the-speed-of-spreadsheets-2/)
    

Excel Speeding up & Optimization Tips by Gregory
------------------------------------------------

**About George:**  
Gregory runs [Excel Semipro](http://excelsemipro.com/)
, where he shares Excel tips & ideas. I asked him to contribute to the Speedy Spreadsheet Week. This is what he says,

**Tips by George:**

To speed up my worksheet files, I have one primary rule: do not use the OFFSET function, which is volatile and can slow things down considerably. In newer spreadsheets I use Tables and The imposing INDEX function to keep ranges automatically updated. In Excel 2003 I use an event-based approach, with named ranges, the worksheet deactivate module, and VBA to keep lists and ranges updated.

**Links:**

*   [The Imposing INDEX](http://excelsemipro.com/d/Data_Validation_List_Update.xlsm)
    
*   [How to Update a List or Range without OFFSET](http://excelsemipro.com/2012/03/how-to-update-a-list-or-range-without-offset/)
    
*   [Example worksheet](http://excelsemipro.com/d/Data_Validation_List_Update.xlsm)
    

Excel Speeding up & Optimization Tips by Luke
---------------------------------------------

**About Luke:**  
[Luke](http://chandoo.org/forums/profile/luke-m)
 is one of the Excel Ninjas at Chandoo.org where he contributed more than 1000 posts. I asked Luke to share some optimization tips based on his vast experience of using Excel & helping others. This is what he suggests:

1.  In VB, whenever I see a line like Selection.something that’s usually an indicator that I’m using extra lines. Either I need to apply the method directly to the object instead of selecting it, or I need to use a With statement.
2.  With Event macros, don’t forget the all-important lines of Application.EnableEvents = False and Application.EnableEvents = True so that you don’t cause multiple events to be triggered.
3.  See a section of code that you’re repeating? Probably need to make this a separate Sub or Function that you can then reference from the main code.
4.  When building your formula page, think top-down. Cells near the top of worksheet should be referenced in formulas that are below, not vice-versa. XL likes to calculate left to right, top to bottom. Scattering cell references around makes it work harder.
5.  When using large amounts of data that you want to be charted, sometimes I’ll build a formula sheet within the workbook with data, and then just build another workbook that uses a data query (referencing the formula results) to generate the charts.
6.  This might be more along the lines of auditing a worksheet, but sometimes it’s hard to see how I’ve laid out my constants and formulas, and using a worksheet map helps bring things into focus (related: [create a worksheet map](http://spreadsheetpage.com/index.php/site/tip/creating_a_worksheet_map/)
    )

Want to become better in Excel? Join Chandoo.org courses
--------------------------------------------------------

|     |     |
| --- | --- |
| ### Excel School<br><br>Learn Excel from basics to advanced level. Create awesome reports, dashboards & workbooks.<br><br>**[Click here to know more](http://chandoo.org/wp/excel-school/)<br>** | ### VBA Classes<br><br>Learn VBA & Macros step-by-step. Build complex workbooks, automate boring tasks and do awesome stuff.<br><br>**[Click here to know more](http://chandoo.org/wp/vba-classes/)<br>** |

Excel Speeding up & Optimization Tips by Narayan
------------------------------------------------

**About Narayan:**  
[Narayan](http://chandoo.org/forums/profile/narayank991)
 is one of the Excel Ninjas at Chandoo.org where he contributed more than 1000 posts. I asked Narayan to share some optimization tips based on his vast experience of using Excel & helping others. This is what he suggests:

**Period-to-Date and Cumulative SUMs  
**There are two methods of doing period-to-date or cumulative SUMs. Suppose the numbers that you want to cumulatively SUM are in column A, and you want column B to contain the cumulative sum; you can do either of the following:  
You can create a formula in column B such as =SUM($A$1:$A2) and drag it down as far as you need. The beginning cell of the SUM is anchored in A1, but because the finishing cell has a relative row reference, it automatically increases for each row.  
You can create a formula such as =$A1 in cell B1 and =$B1+$A2 in B2 and drag it down as far as you need. This calculates the cumulative cell by adding this row’s number to the previous cumulative SUM.  
For 1,000 rows, the first method makes Excel do about 500,000 calculations, but the second method makes Excel do only about 2,000 calculations.  
**  
Subtotals**  
[Use the SUBTOTAL function](http://chandoo.org/wp/2010/02/09/subtotal-formula-excel/)
 to SUM filtered lists. The SUBTOTAL function is useful because, unlike SUM, it ignores the following:  
Hidden rows that result from filtering a list. Starting in Excel 2003, you can also make SUBTOTAL ignore all hidden rows, not just filtered rows.  
Other SUBTOTAL functions.

**Using SUMPRODUCT to Multiply and Add Ranges and Arrays.**  
In cases like weighted average calculations, where you need to multiply a range of numbers by another range of numbers and sum the results, using the comma syntax for SUMPRODUCT can be 20 to 25 percent faster than an array-entered SUM.  
`{=SUM($D$2:$D$10301*$E$2:$E$10301)}   =SUMPRODUCT($D$2:$D$10301*$E$2:$E$10301)   =SUMPRODUCT($D$2:$D$10301,$E$2:$E$10301)`  
These three formulas all produce the same result, but the third formula, which uses the comma syntax for SUMPRODUCT, takes only about 77 percent of the time to calculate that the other two formulas need.

**Dynamic Ranges**

These are most often created using the OFFSET and COUNTA functions , as in the following :  
`=OFFSET(Sheet1!$A$1,0,0,COUNTA(Sheet1!$A:$A)-1,1)`

Sometimes , when data is stored in the form of records , so that all columns have data to the same extent , there may be several dynamic ranges ; say we have ORDER\_ID in column A , CUSTOMER\_ID in column B , and the AMOUNT in column C. Thus there may be several dynamic ranges as follows :  
`=OFFSET(Sheet1!$A$1,0,0,COUNTA(Sheet1!$A:$A)-1,1)   =OFFSET(Sheet1!$B$1,0,0,COUNTA(Sheet1!$B:$B)-1,1)   =OFFSET(Sheet1!$C$1,0,0,COUNTA(Sheet1!$C:$C)-1,1)`  
These can be simplified to :  
`=OFFSET(Sheet1!$A$1,0,0,COUNTA(Sheet1!$A:$A)-1,1)   =OFFSET(Sheet1!$B$1,0,0,COUNTA(Sheet1!$A:$A)-1,1)   =OFFSET(Sheet1!$C$1,0,0,COUNTA(Sheet1!$A:$A)-1,1)`  
These can then be optimized by storing the COUNTA value in a cell , and using the cell reference within the OFFSET formula :  
`=OFFSET(Sheet1!$A$1,0,0,Sheet1!$F$1,1)   =OFFSET(Sheet1!$B$1,0,0, Sheet1!$F$1,1)   =OFFSET(Sheet1!$C$1,0,0, Sheet1!$F$1,1)`  
Where Sheet1!$F$1 contains the formula : `=COUNTA(Sheet1!$A:$A)-1`  
For more, [refer to MSDN](http://msdn.microsoft.com/en-us/library/ff726673.aspx)
.

**Resetting the USED RANGE**

Pressing CTRL END will take the cursor and place it on the cell which Excel thinks is the last used cell in the worksheet.  
Suppose you do this , and the cursor lands on D27 ; now navigate to any cell which is as far away as you can imagine , say AA3456 ; enter any character , even a space will do ; then clear the cell contents by pressing the DEL key.  
Pressing CTRL END will now take the cursor to AA3456.  
To reset the USED RANGE , go to the Immediate Window of the VBA Project , and enter the following statement :  
`Application.ActiveSheet.UsedRange`  
Your used range should now be reset to its earlier value of D27 ; pressing CTRL END will now take the cursor to D27.  
Refer to [this Stackoverflow discussion](http://stackoverflow.com/questions/7423022/excel-getting-the-actual-usedrange)
 for more.

Excel Speeding up & Optimization Tips by Jordan
-----------------------------------------------

**About Jordan:**  
Jordan runs [Option Explicit](http://optionexplicitvba.blogspot.com/)
, an Excel VBA blog. He shared these tips with us,

*   When reading and writing to ranges, use .value2 (this is noticeable for large, iterative calculations)
*   Ensure that ALL spreadsheet errors are handled. The most common errors I see ignored are #Ref errors and #Div (for dividing by zero). Use Go To Special… to find these errors and either delete them or use IFERROR to handle them. In my opinion, Excel errors are one of the biggest contributing factors to slow spreadsheets.
*   When using INDEX, include the row or column number even if you don’t need it. For example, if I’m pulling data from only one column, I need only write =INDEX(A1:A10, 1) to pull the first item. However, =INDEX(A1:A10, 1, 1) appears to be a hair faster. Try it.
*   Cut down on Lookup functions. In many instances, the lookup table has already encoded information in the correct order. Instead of looking up, say, Stage 2, just use INDEX on the desired column and pull from row 2.

Thanks to Hui, George, Gregory, Luke, Narayan & Jordan
------------------------------------------------------

Many thanks to all of you for sharing these ideas & tips so that we can speed up Excel. If you found these tips useful, say thanks to the contributors.

More on Excel Optimization & Speeding up:
-----------------------------------------

Read these articles too,

*   [Optimization & Speeding-up Tips for Excel Formulas](http://chandoo.org/wp/2012/03/20/optimize-speedup-excel-formulas/ "Speed up your Excel Formulas [Speedy Spreadsheet Week]")
    
*   [Charting & Formatting Tips to Optimize & Speed up Excel](http://chandoo.org/wp/2012/03/21/excel-optimization-charting-formatting-tips/ "Speeding up & Optimizing Excel – Tips for Charting & Formatting [Speedy Spreadsheet Week]")
    
*   [Optimization Tips & Techniques for Excel VBA & Macros](http://chandoo.org/wp/2012/03/22/vba-macros-optimization-techniques/ "Optimization Tips & Techniques for Excel VBA & Macros [Speedy Spreasheet Week]")
    
*   Excel Optimization tips submitted by our readers

Want to become better in Excel? Join Chandoo.org courses
--------------------------------------------------------

|     |     |
| --- | --- |
| ### Excel School<br><br>Learn Excel from basics to advanced level. Create awesome reports, dashboards & workbooks.<br><br>**[Click here to know more](http://chandoo.org/wp/excel-school/)<br>** | ### VBA Classes<br><br>Learn VBA & Macros step-by-step. Build complex workbooks, automate boring tasks and do awesome stuff.<br><br>**[Click here to know more](http://chandoo.org/wp/vba-classes/)<br>** |

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel links](https://chandoo.org/wp/tag/excel-links/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [ssw](https://chandoo.org/wp/tag/ssw/)
    , [SUBTOTAL](https://chandoo.org/wp/tag/subtotal/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousHappy Ugadi](https://chandoo.org/wp/happy-ugadi/)

[Next75 Excel Speeding up Tips Shared by YOU! \[Speedy Spreadsheet Week\]Next](https://chandoo.org/wp/75-excel-speeding-up-tips/)

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
    
    [Reply](https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ