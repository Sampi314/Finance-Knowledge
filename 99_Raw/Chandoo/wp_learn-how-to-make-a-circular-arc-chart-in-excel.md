# Circular Arc - Doughnut Charts » Chandoo.org - Learn Excel, Power BI & Charting Online Chandoo.org Arc, Chart

**Source:** https://chandoo.org/wp/learn-how-to-make-a-circular-arc-chart-in-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Circular Arc – Doughnut Charts
==============================

*   Last updated on May 16, 2019

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

A few weeks back **Jhouz** asked a question in the [Chandoo.org Forums](https://chandoo.org/forum/threads/excel-doughnut-chart-with-round-edges.41541/)
 “_Is is possible to create a doughnut chart like this one in excel?_”

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_01.png)

This post will examine how to make it

**Alert:** It isn’t as straight forward as you may first think!

A couple of users responded with a Doughnut Chart

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_02.png)

Which at first glance looks quite similar.

But the original author wanted round ends on the ends of the Doughnut segment. He also wanted a smooth chart.

A quick scan through the properties of a Doughnut Chart reveals there is no optionality to control the ends of the Doughnuts Segments. An alternative approach was required.

### A Solution

Before starting, if you want to you can follow along using a sample file with the worked examples shown below: [Download Here](https://chandoo.org/wp/wp-content/uploads/2019/05/Pct_Circle-Chart.xlsx)

The solution I posed was to use an X-Y Scatter chart for the line segments and apply a thick Line style.

The part of this approach that makes it work is that Line Styles have a property for the Lines End including an option for a round end.

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_03.png)

The solution chart above consists of 2 lines

The first is the Background (Grey) line, which is a complete circle

The second line is the green line, which is a segment of the circle equal to in this case 45% of a circle or 162 Degrees (0.45 x 360). It is in front of the Grey line.

To apply this technique I used a number of Named Formula, and based the chart on these named formula:

**First for the Background Grey chart segment**

To define the Grey segment I applied 3 Named Formula:

|     |     |
| --- | --- |
| **c1\_Rad** | \=RADIANS(-(ROW(OFFSET(Sheet1!$A$1,,,360+1,1))-91)) |
| **\_x1** | \=COS(c1\_Rad) |
| **\_y1** | \=SIN(c1\_Rad) |

The Grey circle is defined by an Array of Radians of each degree between 0 and 360 of a circle.

C1\_Rad                =RADIANS(-(ROW(OFFSET(Sheet1!$A$1,,,360+1,1))-91))

This works by using the Excel Row() and Offset() function to generate an array of Degrees from 0 to 360

The formula **ROW(OFFSET(Sheet1!$A$1,,,360+1,1))**

Will return **\={1;2;3;4;5;6; …. ;358;359;360;361}**

Note that we have taken the array 1 degree past 360 because the Row’s lowest value is Row 1, not row 0.

We then subtract 91 degrees from this to allow the Chart to start at the top of the circle.

The adjusted formula **ROW(OFFSET(Sheet1!$A$1,,,360+1,1))-91**

Returns: **\={-90;-89;-88;-87; … ;268;269;270}**

Finally the **–** in front of the array changes the direction of the circle from Anticlockwise to clockwise.

Returns: **\={90;89;88;87; … ;-268;-269;-270}**

The Radians() function is used to convert the array of Degrees into an array of Radians

Returns: **\={1.57;1.55;1.53; … ;-1.22;-1.23;-1.25}**

The Radians above were rounded to 2 decimals places for display on this post, but Excel internally is using the full 15 decimal place precision.

We can now use this array of Radians to draw the background circle

To do this setup 2 new Named Formula

**\_x1**: =COS(c1\_Rad)

**\_y1**: =SIN(c1\_Rad)

Each of these will return an array of the X and Y values corresponding to each of the Radians from the previous **c1\_Rad** array. The X and Y values will vary between -1 and 1. You may need these for Chart Scaling later.

If you want a circle of different radius simply multiply the x and y formulas like  
**\_x1**: =COS(c1\_Rad)\*5 for a radius of 5 and the same for the **\_y1** named formula

To plot these we add a X-Y Scatter Chart.

Select a single cell. Then goto the **Insert**, **Chart**, **Scatter Chart** menu and select a **Scatter Chart with Smooth lines**. This will give you a blank chart.

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_04.png)

With the Chart Selected, Right click on the chart area and choose **Select Data…**

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_05.png)

Add a Series using the **Add** button. Use the Worksheet Name **Sheet1** and Named Formula **\_x1** & **\_y1** for the X and Y values

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_06a.png)

You can leave the Series Name blank or enter a value like “Background Circle”.  
Note that you must enter the Sheet Name including the **!** preceding the Named Formula name. Once you have accepted the inputs, if you return to the Edit Series dialog, notice that Excel now displays the Workbooks name instead of the Worksheets name. That’s quite ok.

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_07.png)

You will now have a chart which looks like:

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_08.png)

Finally Right click on the first series and select **Format Data Series.**

Set the Line Color to a Light Grey and set the Line Width to 12 . Check that Markers are set to None

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_09.png)

**Next the Foreground Green chart segment**

To draw the front arc of the circle we add a few more Named Formula

|     |     |
| --- | --- |
| **\_pct** | \=Sheet1!$C$6 |
| **c2\_Rad** | \=RADIANS(-(ROW(OFFSET(Sheet1!$A$1,,,\_pct\*360+1,1))-91)) |
| **\_x2** | \=COS(c2\_Rad) |
| **\_y2** | \=SIN(c2\_Rad) |

**\_pct** stores the value of the percentage of the circle directly from the reference cell on the worksheet eg: 45%

To draw an arc we only need to factor the 360 Degrees for a full circle back to the percentage required for the arc: ie: from 0 to 45% x 360 degrees = 162 Degrees. Hence drawing an Arc from 0 degrees to 162 Degrees.

To do this we use the same formula as before except that we set the range to the 45% of 360 degrees using the Named Formula:

**C2\_Rad**: =RADIANS(-(ROW(OFFSET(Sheet1!$A$1,,,**\_pct**\*360+1,1))-91))

Add another series to the chart using.

With the Chart Selected, Right click on the chart area and choose **Select Data…**

**X values**: =Sheet1!\_x2

**Y values**: =Sheet1!\_y2

Next select the chart and ensure that the 45% circle is in front of the full circle

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_10.png)

Select the Chart’s 2nd series and change the line width and line color to suit the impact you want.

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_11.png)

Finally select the 45% line

Goto the Lines properties and set the **Cap type** to **Round**  

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_12.png)

**Add the Measurement**

With the Chart selected, goto the **Insert**, **Text Box** dialog and select a text box style and insert it.

With the text box selected, goto the **Formula Bar** and enter the Formula **\=\_pct** and press **Enter** or click the **Tick** icon to accept.

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_13.png)

Finally with the text box selected, Change the Font Size to suit eg: 64 and Format the Text using an appropriate style from the **Drawing Tools**, **Format** Menu

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_14.png)

Ensure the Text box is wide enough to display up to 100% include the percentage sign

The Final Chart

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_15a.png)

and with another value…

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DC_16.png)

**Other line type endings**

Experiment with other Line Ends and see what you can make?

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DH_17.png)

**and Line Styles and Thicknesses?**

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DH_18.png)

### Multiple Series

By careful use of  chart series you can add multiple measurements to the same chart and use a combination of display properties to enhance your chart

![](https://chandoo.org/wp/wp-content/uploads/2019/05/DH_19.png)

### Conclusion

In conclusion I have demonstrated a successful solution to Jhouz’s original post and then extended it a bit further.

The Author acknowledges that there is limited use for doughnut charts and only recommends them in limited circumstances.

I hope these enhancements allow you to better use and emphasise your data in your situation as well as add another Excel technique to your arsenal.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/learn-how-to-make-a-circular-arc-chart-in-excel/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/learn-how-to-make-a-circular-arc-chart-in-excel/#respond)
    
*   Tagged under [Circular Arc](https://chandoo.org/wp/tag/circular-arc/)
    , [Doughnut Chart](https://chandoo.org/wp/tag/doughnut-chart/)
    , [Scatter Chart](https://chandoo.org/wp/tag/scatter-chart/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPrevious5 simple rules for making awesome column charts](https://chandoo.org/wp/rules-for-making-awesome-column-charts/)

[NextHow to trace precedents in Excel formulas? \[tip+music from Prague\]Next](https://chandoo.org/wp/how-to-trace-precedents-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/learn-how-to-make-a-circular-arc-chart-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/learn-how-to-make-a-circular-arc-chart-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/learn-how-to-make-a-circular-arc-chart-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ