# How to make a 5 Star Chart (Similar to Amazon)

**Source:** https://chandoo.org/wp/how-to-make-a-5-star-chart

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

How to make a 5 Star Chart (Similar to Amazon)
==============================================

*   Last updated on April 27, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Earlier in the week Chandoo presented [Give more details by showing average and distribution](http://chandoo.org/wp/2011/04/06/show-average-and-distribution/)

At the top of the post was a small screen capture from Amazon.com showing a 5 Star chart  showing that Twilight had a 3.5 Star Rating (way over-rated if you ask me).

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/Chandoo.jpg "Chandoo")](https://chandoo.org/wp/wp-content/uploads/2011/04/Chandoo.jpg)

I received an email shortly afterwards from Rajiv, “**How can I make one of those charts ?** ” with the Stars Circled

It’s actually very simple and this post will show you how.

**The Technique**
-----------------

The technique involves putting a mask in front of a single bar from a Bar Chart

The mask has a plain background and has cut-outs where the Stars are, which are transparent and so only the bar chart shows through in those areas which are cut out.

**Lets Do It**
--------------

On a worksheet we need a cell where we have a Rating Value, lets use **B2**

Make the value in Cell **B2**, 5

Select the cell **B2** and **Insert Chart**

Insert a Bar Chart (Clustered Bar)

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star1.png "5Star1")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star1.png)

Delete the following chart objects

*   Title
*   Legend
*   Major Grid Lines

_[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star2.png "5Star2")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star2.png)
  
_

Select the Horizontal Axis

Format Axis

Change the Horizontal Axis Scale to

*   Minimum 0
*   Maximum 5

_[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star3.png "5Star3")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star3.png)
  
_

Delete the Horizontal and Vertical Axis

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star4.png "5Star4")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star4.png)

Move the chart and resize the Bar to your requirements

Change the Bar’s Fill to suit

Set Border color to No Color

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star5.png "5Star5")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star5.png)

Insert Picture

Import the 5 Star mask [attached here](https://chandoo.org/wp/wp-content/uploads/2011/04/Mask-5Stars.png "5 Star Mask")

Position the mask in front of the charts Bar

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star6.png "5Star6")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star6.png)

With the mask selected shift the Right hand side and then left hand side so that you can just see the edges of the bar.

Check the placement by trying the numbers from 0, 1, 2, 3, 4, 5 and 0.1 in B2

You should see all the stars perfectly when the placement is correct

_[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star7.png "5Star7")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star7.png)
_

Select the Chart and 5 Star Mask together

Use Shift while selecting each one

Group the Chart and Mask together, so that they can’t be moved

_[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star8.png "5Star8")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star8.png)
_

Your are free to shift and resize this combined object on your worksheet as required

**Vertical Charts**
-------------------

A Similar technique can be used for Vertical Charts using a Column Chart instead of a Bar Chart

**[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star10.png "5Star10")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star10.png)
**

**Masks**
---------

The masks used here were made in CorelDRAW, but can be made in any Drawing/Paint program like Paint.NET, that allows you to save PNG’s with Transparency effects

The masks consists of:

*   5 Stars which have no outline color and are transparent
*   1 Rectangle which is White with no Outline color

The 6 objects are then Joined enabling the holes of the Stars to show through the White Rectangle

Using this technique any shape can be used as a mask

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star-Random.png "5Star Random")](https://chandoo.org/wp/wp-content/uploads/2011/04/5Star-Random.png)

I have included the following masks for you to practice with or use:

[5 Stars Mask](https://chandoo.org/wp/wp-content/uploads/2011/04/Mask-5Stars.png "5 Star Mask")
,

[5 Stars Mask with Outlined Stars](https://chandoo.org/wp/wp-content/uploads/2011/04/Mask-5-Stars-outlined.png "5 Stars Mask with Outlines")
,

[5 Circles Mask](https://chandoo.org/wp/wp-content/uploads/2011/04/Mask-5Circles.png "5 Circles Mask")
,

[Swirling Line Mask](https://chandoo.org/wp/wp-content/uploads/2011/04/Mask-Swirl.png "Swirling Line Mask")
,

[Footsteps Mask.](https://chandoo.org/wp/wp-content/uploads/2011/04/Mask-Feet.png "Footsteps Mask")

**If anybody knows how to join objects together in Excel to make holes through them as required here, Please let us know in the comments below:**

Thermometer Charts
------------------

The above technique is great for application to Thermometer Charts, where the Thermometer can take on all values from 0 to 100% or 0 to $200,000

or whatever you require.

[![](https://chandoo.org/wp/wp-content/uploads/2011/04/5StarThermometer1.png "5StarThermometer")](https://chandoo.org/wp/wp-content/uploads/2011/04/5StarThermometer1.png)

Files
-----

All the above examples are shown in one file which you can [download here](https://chandoo.org/wp/wp-content/uploads/2011/04/5-Stars1.xlsx "Download Examples")
 or here for the [2003 Version](https://chandoo.org/wp/wp-content/uploads/2011/04/5-Stars-2003.xls "5 Stars (2003) Examples")

Download the [Waves and Chameleon 2007](https://chandoo.org/wp/wp-content/uploads/2011/04/Waves-Cameleon.xlsx "Waves & Cameleon example")
 or [Waves and Chameleon 2003](https://chandoo.org/wp/wp-content/uploads/2011/04/Waves-Cameleon-2003.xls "Waves & Chameleon Example")
 examples

Extensions of the Technique
---------------------------

This technique can be extended in a number of areas

The Thermometer chart above shows one such area

The other is applying multiple Masks to multiple Bars/Columns in one chart, But I’ll leave you to practice that.

Limitations of the Technique
----------------------------

Two main limitations of this technique are:

### Scaling

As Excel charts are scaled, Excel internally decides what space should be between the Plot Area, Titles and the edge of the Chart Area. This is not maintained constantly and hence the Plot Area may scale at a different ratio to the Chart area and overlying mask.

If this happens Ungroup the Chart and mask and reset ecverything at the new size.

### Mask Color

The mask has a Fixed color, in the above examples it is white.

The mask cannot be colored in Excel to Match the background color of the Worksheet if it isn’t white.

So a new Mask will need to be made.

What Do you Think of this Technique  

--------------------------------------

What Do you Think of this Technique?

How else can you see this technique being extended?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [33 Comments](https://chandoo.org/wp/how-to-make-a-5-star-chart/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-make-a-5-star-chart/#respond)
    
*   Tagged under [5 Circle Chart](https://chandoo.org/wp/tag/5-circle-chart/)
    , [5 Star Chart](https://chandoo.org/wp/tag/5-star-chart/)
    , [charts](https://chandoo.org/wp/tag/charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [thermometer charts](https://chandoo.org/wp/tag/thermometer-charts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousAuditing Spreadsheets? – Disable Direct Editing Mode to save time \[quick tip\]](https://chandoo.org/wp/spreadsheet-auditing-tip-disable-direct-editing-mode/)

[NextCelebrating India’s Worldcup Cricket Victory – In Excel Dashboard Style!Next](https://chandoo.org/wp/cricket-worldcup-dashboard/)

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
    
    [Reply](https://chandoo.org/wp/how-to-make-a-5-star-chart/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-make-a-5-star-chart/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-make-a-5-star-chart/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ