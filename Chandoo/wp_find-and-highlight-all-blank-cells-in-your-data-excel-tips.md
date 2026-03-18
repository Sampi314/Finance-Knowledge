# Find and Highlight all blank cells in your data [Excel tips] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Find and Highlight all blank cells in your data \[Excel tips\]
==============================================================

*   Last updated on April 19, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_True story:_

On Friday (17th April – 2015), I flew from Vizag (my town) to Hyderabad so that I can catch a flight to San Francisco to attend a conference. As I had 10 hours of overlay between the flights in Hyderabad, I checked in to a lounge area so that I can watch some sports, eat food while pretending to do work on my laptop. There was a gentleman sitting in adjacent space doing some work in Excel. As I began to compose few emails, the gentleman in next sitting space asked me what I do for living. Our conversation went like this.

Me: I run a software company  
He: Oh, so you must be good with computers  
Me: _smiles and cringes at the stereotyping_  
He: What is the formula to select all the blank cells in my Excel data and highlight them in Yellow color

Mind you, he had no idea that I work in Excel. We were 2 random guys in airport lounge watching sports and eating miserable food.

Me: Well, what are you trying to do?  
He: You see, I am auditing this data. I need to locate all the blank rows and set them in different color so that my staff can fill up missing information. Right now, I am selecting one row at a time and filling the colors. Is there a one step solution to this problem?

Needless to say, I showed him how to do it faster, which led to an interesting 3 hours at the lounge.

_**End of true story.**_

So today, let’s understand how to find & highlight all the blank cells in the data.

### Let’s take a look at the data:

Here is a sample of data.

![find-highlight-blank-cells-in-excel](https://chandoo.org/wp/wp-content/uploads/2015/04/find-highlight-blank-cells-in-excel.png)

**One important thing to keep in mind:**

*   This data is not structured as table.

**There are 3 powerful & simple methods** to find & highlight blank cells.

### Method 1: Selection & Highlight approach

In this method, we **just select all the blank cells in one go and fill them with yellow color**.

First select the entire range of cells where you data is located. Using CTRL+Arrow keys is not going to work because of the blank cells in-between. Instead, follow this:

1.  Select the top-left cell of your data (say B2)
2.  Click and drag the little rectangular box in vertical-scrollbar all the way down.
3.  Hold Shift and click on the very last cell (bottom-right)

Now that all the data is selected,

1.  Press F5 and click on Special
2.  Choose blanks. Click ok.
3.  This will select only the blank cells.
4.  Fill yellow (or other) color by clicking the fill icon and selecting the color
5.  Done!

_Here is a quick demo of this:_

[https://chandoo.org/wp/wp-content/uploads/2015/04/method1.mp4](https://chandoo.org/wp/wp-content/uploads/2015/04/method1.mp4)

### Method 2: Filter approach

The above approach (selection & highlight) works fine if you care about blank cells anywhere. What **if you just want to find & highlight only rows have blanks in a certain column**. Say, you want to highlight all rows where comments are empty.

In this case,

1.  Select all data using the steps in method 1.
2.  Press CTRL+Shift+L to activate filters
3.  Keep the selection on & Filter the column you want to show only blank values
4.  Now fill yellow color
5.  Done!

### Method 3: Conditional formatting approach

Both method 1 & method 2 have a draw back. _If your data changes_, you must clean up & highlight again.

This is where [conditional formatting](http://chandoo.org/wp/2009/03/13/excel-conditional-formatting-basics/)
 shines. **You can tell Excel to highlight cells only if they are blank**. Once some data is typed in (or copy pasted or connection refreshed), the color will go away automatically.

To set up conditional formatting,

1.  Select all the data
2.  Go to Home > Conditional Formatting > New rule
3.  Click on “Format only cells that contain”
4.  Change “Cell Value” option to “Blanks”
5.  Set up formatting you want by clicking on Formatting button
6.  Click ok and you are done!

![highlight-blanks-conditional-formatting](https://chandoo.org/wp/wp-content/uploads/2015/04/highlight-blanks-conditional-formatting.png)

This will automatically highlight all blank cells in your favorite color.

### Oh wait, what if I want to highlight entire row if a certain column is blank?

You can use conditional formatting in such cases too. Follow these steps.

Assuming you want to check for blanks in Column G and your first data point is in G4.

1.  Select all the data (just data, no headers)
2.  Go to Home > Conditional Formatting > New rule
3.  Select rule type as “Use a formula…”
4.  Type the formula as `=LEN($G4)=0`
5.  Set up formatting you want
6.  Click ok and you are done.

![highlight-blanks-conditional-formatting-2](https://chandoo.org/wp/wp-content/uploads/2015/04/highlight-blanks-conditional-formatting-2.png)

### Wait a sec, What is the `LEN($G4)=0` thing?

**LEN()** formula tells us what is the length of a cell’s content. So if a cell is blank, LEN(cell) would be 0.

**$G4 is a mixed reference style**. This way, even when conditional formatting is checking other columns, it still looks in column G to see if that is really empty.

_**Related:**_ [An introduction to Excel cell references](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/ "Relative vs. Absolute References in Formulas [spreadcheats]")
.

### Bonus tips:

_Q) How to highlight if either of column G or H are blank?_  
A) =OR(LEN($G4)=0, LEN($H4)=0)

_Q) How to highlight if both column G & H are blank?_  
A) =AND(LEN($G4)=0, LEN($H4)=0)

**Go ahead and whack them blank cells.**

### How do you deal with blank cells?

Do you sneak up on an unsuspecting fellow passenger in an airport lounge and ask them how to deal with the blank problem? Do you manually select the blank cells and deal with them one at a time? Or do you use some ninja level trickery to fix the blanks?

**Go ahead and tell me your blank story in the comments.**

### Fill the blanks in your Excel knowledge

If you have gaps in your Excel know-how, then you have come to right place. Use below links and fill those blanks.

*   [Delete blank rows in Excel](http://chandoo.org/wp/2010/01/26/delete-blank-rows-excel/ "Delete Blank Rows in Excel [Quick Tip]")
    
*   [Introduction to Excel conditional formatting](http://chandoo.org/wp/excel-tutorial/using-conditional-formatting/ "Introduction Conditional Formatting in Excel")
     – video
*   [Excel basics](http://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel concepts & techniques](http://chandoo.org/wp/advanced-excel-skills/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips/#respond)
    
*   Tagged under [blank cells](https://chandoo.org/wp/tag/blank-cells/)
    , [blank rows](https://chandoo.org/wp/tag/blank-rows/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [len()](https://chandoo.org/wp/tag/len/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousHow to insert a blank column in pivot table?](https://chandoo.org/wp/how-to-insert-a-blank-column-in-pivot-table/)

[NextCP034: Advanced Excel Essentials book talk with Jordan GoldmeierNext](https://chandoo.org/wp/cp034-advanced-excel-essentials-book-review/)

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
    
    [Reply](https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/find-and-highlight-all-blank-cells-in-your-data-excel-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ