# Excel Tips Submitted by You [Part 1] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-tips-by-you-1

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel Tips Submitted by You \[Part 1\]
======================================

*   Last updated on May 10, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This week we are celebrating [Your Week @ PHD](http://chandoo.org/wp/2009/05/08/your-week-your-tips/)
. That means you get to read the [excel tips](http://chandoo.org/wp/category/excel/)
 shared by other readers of this blog.

**Unhide all the sheets using simple macro** _by **Kat**_

> My single favourite simple macro ever – to fill in the gap that Excel leaves. Unhiding -all- hidden tabs in a workbook at once. I install it in the personal.xls workbook, and save myself hours of clicking.
> 
> Sub Unhide\_All\_Sheets()
>  Dim wsSheet As Worksheet 
> 
>  For Each wsSheet In ActiveWorkbook.Worksheets 
> 
>  wsSheet.Visible = xlSheetVisible 
> 
>  Next wsSheet
> End Sub

**A KPI Dashboard using VBA and Charts** _by_ **_David_**

> After learning a whole lot over the past few months from this site and others (so many I can’t even remember right now – but I will make a list soon of where I found things), I constructed a KPI spreadsheet (see link below).  This spreadsheet allows our institution to create standardized KPI reports for university consumption.
> 
> I attempted to keep the colors muted even though I chose school colors (from the publishing guide) for the actual graph.
> 
> **Features**
> 
> The chart is dynamically configured in numerous ways.  The user can control the title (via cell entry on left), color of bars (via color of data labels), number format (via number format of the first data cell), and the display and printing of the trend line.  The KPI name comes from the sheet, and the vertical axis is determined based on the data (I find the maximum value and divide by 4).
> 
> **To-dos**
> 
> I would like the user to be able to enter new descriptive items via a form with the option to include variables (KPI\_Name, KPI\_Category, etc.).  I would like the user to be able to include more than one chart on a page (some KPIs actually need to track parts of the whole).
> 
> I am sure there are more features I will think of as time goes on but I wanted to let others see this and hopefully be able to incorporate it into their/your own work.  The file is available here: [http://dl.getdropbox.com/u/749941/KPIs\_PHD.xlsm](http://dl.getdropbox.com/u/749941/KPIs_PHD.xlsm)
> .  Hopefully I will be starting a blog soon to talk more about what we are doing here with excel and other products.

**Using Find Dialog to Solve a Tricky Problem** _by_ [_**Christy Lee**_](http://www.linkedin.com/in/ChristyLeeDollar)

> **Introduction:**
> 
> On a project I recently worked, we crunched several hundred (about 400) rows of data. The creator of the original document did not have any way to foresee the life this project would take on! So…there was only one field for ‘Name’ which contained the names of the team members for the corresponding step of the overall project.
> 
> **Challenge:**
> 
> As the project progressed, an individual may be added to multiple task teams. So, your name might be one of three in four records, one of ten in fifteen records, etc. Also, the team members could be added on the fly…you see how the complications arise quickly! Oh, and the project was run on three continents in four countries….
> 
> Each person was responsible for updating their pertinent information. Because of the complexity of that one name cell, filtering and sorting became cumbersome.
> 
> **Solution:**
> 
> Hide all rows except for the header row.
> 
> Do a search on your name (fortunately, in about three dozen team members, we had no duplicate last names!)
> 
> When the search results dialog comes up, select all of the records (select first, shift+select last)
> 
> Go to Format>Row>Show.
> 
> Whoo Hoo!  There are all (and ONLY) the records that belong to you.

**Array Formulas to the Rescue** _by_ **_Rajinikanth_**

> This is the formula to find out Employees first login time and last logout time for the day.
> 
> Example : Suppose employee table is starting form Column B
> 
> then the table looks like :  
> `Name Code   1001 rajinikanth   1002 srinivas   1003 vardhan`  
> and the Login Data is starting from Column G in a sheet
> 
> ![Array Formulas - User Session Times ](https://chandoo.org/img/n/array-formulas-user-session-times.png)
> 
> Then The formula for First login :
> 
> {=1/MAX((B8=$G$7:$G$15)\*($H$7:$H$15<>0)\*(1/$H$7:$H$15))}
> 
> and the formula for Last Logout :
> 
> {=MAX(($G$7:$G$15=B7)\*($I$7:$I$15))}

**A Big Warm Lovely Heartfelt Thank you to Kat, David, Christy and Rajinikanth. You are truly wonderful.**

### Be a part of the “your week” @ PHD

Come, be part of the your week celebrations at PHD. [Click here to submit your excel tips](http://spreadsheets.google.com/viewform?formkey=cjJSRkdlY25CdjJmZjlUUjRGdEoyQXc6MA..)
. Your tips will be shared with all our readers during this week (May 11-15, 2009)

PS: If you have already shared your tips and not seeing them in this post, don’t worry. I am posting only a few everyday, so yours will be in the next 3 posts.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [9 Comments](https://chandoo.org/wp/excel-tips-by-you-1/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tips-by-you-1/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [find replace](https://chandoo.org/wp/tag/find-replace/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    , [unhide sheets](https://chandoo.org/wp/tag/unhide-sheets/)
    , [using excel](https://chandoo.org/wp/tag/using-excel/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousAnnouncing “Your Week” @ PHD](https://chandoo.org/wp/your-week-your-tips/)

[NextA Good Chart is a Story \[Charting Principles\]Next](https://chandoo.org/wp/charts-are-stories/)

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
    
    [Reply](https://chandoo.org/wp/excel-tips-by-you-1/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tips-by-you-1/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tips-by-you-1/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ