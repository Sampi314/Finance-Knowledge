# Fixing bloated file size and slow calculation in Excel

**Source:** https://chandoo.org/wp/big-trouble-in-little-spreadsheet

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

Big trouble in little spreadsheet
=================================

*   Last updated on January 18, 2014

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Howdy folks. Jeff here. I recently gave a presentation on Excel efficiency to a bunch of analysts, in which – among other things – I’d pointed out that if you ever find yourself having to switch calculation to Manual, there’s probably something wrong with your spreadsheet. Here’s the slide:  
   
[![Chandoo_Big Trouble in Little Spreadsheet_Slide](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Slide.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Slide.gif)

This prompted one of the participants to come to me for advise regarding restructuring a spreadsheet with that very problem. This analyst had a file with only 6000 rows of data in it, but the file size was something like 35MB, and after each and every change she had to wait at least a minute for the file to recalculate before she could do something else.

It turns out there were two problems with her files that were easy to resolve.

The Conf_used_ range
--------------------

First, there was a problem with the Used Range – the area within a worksheet that Excel _thinks_ contains all your workings and data. You can find out what this is for each spreadsheet by pushing \[Ctrl\] + \[End\], and seeing what cell this takes you to. Hopefully it will take you to the bottom-most, right-most cell that you’ve actually used in the sheet:  
[![Chandoo_Big Trouble in Little Spreadsheet_Good Used Range](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Good-Used-Range.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Good-Used-Range.gif)

But occasionally, you’ll see that it might take you far, far below that cell. Maybe all the way to the very bottom of the grid:  
[![Chandoo_Big Trouble in Little Spreadsheet_Bad Used Range](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Bad-Used-Range.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Bad-Used-Range.gif)
  
   
This is bad. Why? Because when Excel saves a file, it includes information about things such as what type of Cell Formatting is used within the used range. If the used range includes millions of cells that aren’t even used, then the information that Excel saves regarding these cells can really blow out the file size. This is exactly what had happened in the case of the spreadsheet concerned. After we reset the used range, the filesize plummeted from 35MB to around 2MB.

Often you can reset the Used Range simply by selecting all the the empty rows under your data, and then deleting them. To do this, select the entire row immediately below your data, then press \[Ctrl\] + \[Down Arrow\] to extend the selection right to the bottom of the sheet, then right click and select Delete:  
[![Chandoo_Big Trouble in Little Spreadsheet_Delete](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Delete.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Delete.gif)

**Note that you’ve got to use the Right-Click>DELETE option, NOT the Delete key on the keyboard.** Pushing that Delete key **does not** reset the used range. In fact, this is often why the used range is wrong…it still reflects some data that used to be in the sheet, but that the user subsequently deleted using the keyboard.

When you’ve done this, then push \[Ctrl\] + \[End\] again and see where you end up – **hopefully** at the bottom right corner of your data.

S_ometimes_ this doesn’t fix the problem, and you still find yourself well below your data. In this case, a bit of VBA will usually suffice. I’d suggest putting the below code into your Personal Macro Workbook, for times like this:  

    
    Sub ResetUsedRange()
        Dim sht As Worksheet
        Dim lng As Long
    

To see what to do with this code, read [What would James Bond have in his Personal Macro Workbook](http://chandoo.org/wp/2013/11/18/using-personal-macro-workbook/ "What would James Bond have in his Personal Macro Workbook?")
.

Too much SUMIF
--------------

The second problem is that each file contained something like 60,000 SUMIF formulas in them. And each one of these formulas referenced two entire columns, rather than just the 2500 rows that actually contained data. It’s really easy to see just how big a problem you might have, simply by doing a Find All for the name of the particular function you’re after:  
   
[![Chandoo_Big Trouble in Little Spreadsheet_Find](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Find.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Find.gif)

You can throw 60,000 VLOOKUPS or IF statements or other run-of-the-mill functions at Excel and it won’t even blink. But 60,000 resource-intensive number-crunching functions such as SUMIF, SUMPRODUCT, COUNTIF etc pointed at very large ranges will cause Excel to flinch, if not shut it’s eyes completely for large periods of time.

That’s because these functions are like Ferrari’s…very powerful, but very expensive. One SUMIF is going to travel very fast down the highway. A few hundred SUMIFS on the same stretch are still going to whiz by pretty fast. Tens of thousands of them are just going to crash in to each other:  
   
[](http://www.nytimes.com/2011/12/06/world/asia/traffic-accident-wrecks-a-dozen-luxury-cars-in-japan.html?_r=0)
[![Chandoo_Big Trouble in Little Spreadsheet_Crashed Ferraris](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Crashed-Ferraris.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Crashed-Ferraris.jpg)
  
   
(The image above comes from [this New York Times article](http://www.nytimes.com/2011/12/06/world/asia/traffic-accident-wrecks-a-dozen-luxury-cars-in-japan.html?_r=0)
 detailing a spectacular traffic pileup in Japan in 2011 that left a highway strewn with the smashed wreckage of eight Ferrari’s, a Lamborghini and three Mercedes sports cars. No-one seriously hurt apart from severely injured pride and a marked increase in insurance premiums the following year.)

Often you can use a PivotTable to do the same thing as a whole bunch of functions like SUMIF, COUNTIF, SUMPRODUCT et cetera. PivotTables are natural aggregation and filtering tools. In this case I **could** use just one PivotTable to replace those 60,000 SUMIFs, and recalculation time dropped from minutes to milliseconds. Now, reporting on this business process is effortless.

One spreadsheet, two morals
---------------------------

I’ve got two morals to share regarding this.

The first is to keep your eyes peeled for signs of trouble in your spreadsheets. Think of FileSize and Recalculation Time as the rev-counter of your car…if it’s getting further and further into the red, then pull over, and check under the hood.

The second – and I can’t underscore this enough – is the importance to organizations of educating all users on how to _recognize symptoms_ of inefficiency. They don’t all have to know how to _treat_ it (although that would be good), but just how to _diagnose_ it. Because if it goes undiagnosed, avoidable inefficiency imposes significant, on-going, and very real opportunity cost. A real dollar amount.

Raising awareness of danger signs is possibly the biggest efficiency gain and risk-reducing opportunity that any training initiative can offer, at the least cost. It’s a game-changer.

Two morals, multiple remedies.
------------------------------

Over at the Daily Dose of Excel blog, I recently posted a [mock business case](http://dailydoseofexcel.com/archives/2014/01/12/the-case-for-corporate-excel-training-investment/)
 centered around corporate investment in Excel training programme. There’s much more food for thought there, and even more in the comments, so go take a look, and please do leave a comment there with your own thoughts.

While this business case revolves around an internal corporate training programme, another great way of reducing this opportunity cost is through courses such as Chandoo.org’s own [Excel School](http://chandoo.org/wp/excel-school/)
, [VBA Classes](http://chandoo.org/wp/vba-classes/)
, and [other Chandoo courses](http://chandoo.org/wp/training-programs/)
.  
[![excel-school-v5-1](https://chandoo.org/wp/wp-content/uploads/2014/01/excel-school-v5-1.png)](http://chandoo.org/wp/training-programs/)

Not to mention other fantastic courses that you’ll find advertised on the web if you look.

And yet another is though interactions in places like the [Chandoo Forum](http://chandoo.org/forum/)
, where you’ll find an army of ninjas with more collective experience than the Borg from Star Trek. The hive mind that is a forum knows no equal.

And of course, you’ll find a wealth of information on this very blog, in articles like [I said your spreadsheet is really FAT, not real PHAT!](http://chandoo.org/wp/2013/09/29/i-said-your-spreadsheet-is-really-fat-not-real-phat/ "I said your spreadsheet is really FAT, not real PHAT!")

About the Author.
=================

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure #VALUE!

Find out more at http:www.heavydutydecisions.co.nz

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [46 Comments](https://chandoo.org/wp/big-trouble-in-little-spreadsheet/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/big-trouble-in-little-spreadsheet/#respond)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

[PrevPreviousFind first non-blank item in a list with formulas](https://chandoo.org/wp/find-first-non-blank-item-in-a-list-excel-formulas/)

[NextRight-click from the keyboard, not the mouse.Next](https://chandoo.org/wp/right-click-from-the-keyboard-not-the-mouse/)

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
    
    [Reply](https://chandoo.org/wp/big-trouble-in-little-spreadsheet/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/big-trouble-in-little-spreadsheet/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/big-trouble-in-little-spreadsheet/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ