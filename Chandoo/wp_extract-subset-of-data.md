# Extract data using Advanced Filter and VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/extract-subset-of-data

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Extract data using Advanced Filter and VBA
==========================================

*   Last updated on November 27, 2012

![Picture of Vijay Sharma](https://secure.gravatar.com/avatar/b8604c6f79c8db3f79e17c562e6f7cd888a268d59501100720b70a6c3046ee1f?s=300&d=mm&r=g)

#### Vijay Sharma

Share

Facebook

Twitter

LinkedIn

In this post we will learn how to use the [Advanced Filter](http://chandoo.org/wp/2011/10/10/how-to-use-advanced-filters/)
 option using VBA to allow us to filter our data on a separate sheet. This has been requested by a lot of our readers and here is how we will use them.

![Filter records using advanced filter and vba](https://chandoo.org/wp/wp-content/uploads/2012/11/filter-records-using-advanced-filter-and-vba.gif "filter records using advanced filter and vba")

What we need to get this done.
------------------------------

1\. Some data that we need filtering on.  
2\. Define what options we need as drop down lists  
3\. A cup of coffee

In the sample data, I have defined 4 options to be available as drop down list; this has been done by creating a new sheet called as “Master”. I then copied the existing columns data into this sheet and used the Remove Duplicates feature to get the unique list of items that was required for the drop downs.

![](https://chandoo.org/wp/wp-content/uploads/2012/11/Filter_records_using_Advanced_Filter_and_VBA_master_sheet.png "Filter_records_using_Advanced_Filter_and_VBA_master_sheet")

The named ranges were created using the INDEX function as shown below

|     |     |
| --- | --- |
| Named Range | Formula |
| prd | \=Master!$A$2:INDEX(Master!$A:$A,COUNTA(Master!$A:$A)) |
| rgn | \=Master!$B$2:INDEX(Master!$B:$B,COUNTA(Master!$B:$B)) |
| cust | \=Master!$C$2:INDEX(Master!$C:$C,COUNTA(Master!$C:$C)) |
| agnt | \=Master!$D$2:INDEX(Master!$D:$D,COUNTA(Master!$D:$D)) |

Now we need to setup the sheet where we need the filtered data to be displayed. Headings were put in cells B5 to B8 and the drop down (using the Data Validation—List) feature was put in cells C5 to C8. Now we need to create or criteria fields in the RawData sheet, this is a requirement and cannot be any place else. When you use the Advanced Filter dialog box and try to place the output onto another sheet Excel will display a message saying “You can only copy data to the Active Sheet”. We will overcome this limit by using VBA and telling Excel where to put the filtered data. I used the cells M1 to P1 to define the headings and cells M2 to P2 to get the actual options from the “Filter Sheet”

|     |     |
| --- | --- |
| Cells | Formula |
| M2  | \=Filter!C5 |
| N2  | \=Filter!C6 |
| O2  | \=Filter!C7 |
| P2  | \=Filter!C8 |

Macro to run advanced filter and extract data
---------------------------------------------

`   Sub FilterData()   Sheets("Filter").Select   Range("B10").Select   Range(Selection, Selection.End(xlToRight)).Select   Range(Selection, Selection.End(xlDown)).Select   Selection.Clear`

Sheets(“RawData”).Range(“Table1\[#All\]”).AdvancedFilter Action:=xlFilterCopy, CriteriaRange:= \_  
Sheets(“RawData”).Range(“M1:P2”), CopyToRange:=Sheets(“Filter”).Range(“B10”), Unique:=True

Columns.AutoFit  
Range(“B10”).Select  
End Sub

First we ensure the current filtered data (in any) is cleared out before we run the code again and then we get the new filtered data from cell B10 onwards. Now let’s understand the actual code that filters our data here.

`    Sheets("RawData").Range("Table1[#All]").AdvancedFilter   Action:=xlFilterCopy,   CriteriaRange:=Sheets("RawData").Range("M1:P2"),   CopyToRange:=Sheets("Filter").Range("B10"),   Unique:=True    `

We converted our raw data into an excel table (Structured Reference [Structured Reference](http://chandoo.org/wp/2009/09/10/data-tables/)
), by doing this we no longer need to know how many rows our data actually goes down to, the “Table1\[#All\]” takes care of that for us.

We also need to specify that our data is in another sheet and we are trying to run Advanced Filter on that data range, this is done using the first line ” Sheets(“RawData”).Range(“Table1\[#All\]”).AdvancedFilter “.

Next we specify the action that we need which is Copy in our case, the other option is “xlFilterInPlace” which would filter right on our data itself.

Then we have specified the Criteria Range (which needs to be on the same sheet where the data is).

And finally we have specified where the output has to be sent to by using : “CopyToRange:=Sheets(“Filter”).Range(“B10″)”

We have also made sure that only Unique records are returned to us by turning Unique:=True.

Download Advanced Filter Demo File
----------------------------------

[Click here to download the demo file](https://chandoo.org/wp/wp-content/uploads/2012/11/extract_data_using_advanced_filer_with_vba.xlsm)
 & use it to understand this technique.

Do you use Advanced filters to extract sub-sets of data?
--------------------------------------------------------

[Advanced filters](http://chandoo.org/wp/2011/10/10/how-to-use-advanced-filters/)
 are very powerful and very simple to setup. I use them often to quickly extract what I want.

**What about you?** Do you use them often? Please share your experiences, techniques & ideas using comments.

Learn more about extracting / consolidating data using VBA
----------------------------------------------------------

Data extraction and consolidation are one of the most common activities done by reporting professionals & analysts. No wonder we speak about these areas a lot here too. Please check out these pages to learn more:

*   [Split an excel file in to many using Advanced Filters & VBA](http://chandoo.org/wp/2011/10/19/split-excel-file-into-many/)
     \[with video\]
*   [Move data from one sheet to many using VBA](http://chandoo.org/wp/2012/05/14/vba-move-data-from-one-sheet-to-multiple-sheets/)
    
*   [Split text on new line using VBA](http://chandoo.org/wp/2011/08/23/split-text-on-new-line-macro/)
    
*   [Consolidate data from multiple files in to one using VBA Macros](http://chandoo.org/wp/2012/04/09/consolidate-data-from-different-excel-files-vba/)
    

**Want to lean more? Consider joining our VBA Classes**

If you would like to learn more about VBA programming, Excel automation, creation of user forms, manipulating data in Access thru Excel etc., consider joining our online VBA Classes. This step-by-step program helps you become awesome in VBA.

[**Click here to know more & Join our classes**](http://chandoo.org/wp/vba-classes/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [126 Comments](https://chandoo.org/wp/extract-subset-of-data/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-subset-of-data/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [advanced filters](https://chandoo.org/wp/tag/advanced-filters/)
    , [advanced vba](https://chandoo.org/wp/tag/advanced-vba/)
    , [Automation](https://chandoo.org/wp/tag/automation/)
    , [consolidation](https://chandoo.org/wp/tag/consolidation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [split](https://chandoo.org/wp/tag/split/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExcel Links – Lets meet in Chennai this Sunday edition](https://chandoo.org/wp/excel-links-lets-meet-in-chennai-this-sunday-edition/)

[NextMacros for Automatically Implementing Modeling Best PracticesNext](https://chandoo.org/wp/macros-for-best-practice-modeling/)

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
    
    [Reply](https://chandoo.org/wp/extract-subset-of-data/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-subset-of-data/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-subset-of-data/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ