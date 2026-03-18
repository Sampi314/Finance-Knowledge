# Conditionally Format Chart Backgrounds » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/conditionally-format-chart-backgrounds

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Conditionally Format Chart Backgrounds
======================================

*   Last updated on March 31, 2015

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Recently, Paul, a reader, of the Chandoo Blog Post: [Colors-in-excel-chart-labels-trick](http://chandoo.org/wp/2009/01/29/colors-in-excel-chart-labels-trick/ "Colors in Excel")
 asked a question:

_“Hi Chandoo,_

_Is it possible to change the background label color on chart depending on the value? ”  
_

I answered with a general “Yes” and offered two solutions  
1\. Using CF to color the background cells behind the chart  
2\. A VBA Solution to change the chart colors

This post will examine how to implement each method:

I have attached sample files which includes both examples [Excel 2007-13 Sample](https://chandoo.org/wp/wp-content/uploads/2015/03/Change-Chart-background.xlsm "2007-13 sample File")
 or [Excel 97-2003 Sample](https://chandoo.org/wp/wp-content/uploads/2015/03/Change-Chart-background.xls "97-2003 Sample file")
  
You can follow along in this file before attempting it on your own data.

Using Conditional Formatting to Color the background cells
----------------------------------------------------------

In the sample file goto the **CF Technique** worksheet

In CF Technique worksheet you will see a set of data with dates and Scores for each date

[![CFCBG01](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG01.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG01.png)

Below the main table is a calculation of the slope of the line of best fit through the data  
This shows either a positive number when the data is trending upwards or a negative number when it is trending downwards

For the purpose of this we can simply change the yellow cell C13 from 90 to 10 to change the slope from a Positive to a Negative value

[![CFCBG02](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG02.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG02.png)

Next to the chart is a simple X-Y Chart showing the Scores vs the Date (Blue) and a Line of best fit (Dashed Red)

The chart is exactly covering the range E3:L15, this is achieved by placing the chart roughly in position and then holding the Alt Button whilst dragging the corners or edges of the chart.

**Note**: The use of Alt forces Excel to Snap the object onto the cell edges and lock it there, so that when the column width or row height changes, the Chart will resize with it.  

Next we set the colors of the Chart Area and Plot Area to Transparent (No Color)

The Chart area is the Background area of the chart, White in the following example

The Chart area is the Background area of the chart, Yellow in the following example

[![CFCBG05](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG05.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG05.png)

We can see that the chart area has no color in the above picture as we can see the Grid Lines through the Chart Area.

### Format the Chart Area

Select the Chart

Right Click in the Chart Area,

[![CFCBG03](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG03.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG03.png)

Format Chart Area

[![CFCBG04](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG04.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG04.png)
  
Click on the Fill Tab and set the Fill to No Fill

### Format the Plot Area

With the chart selected, Right Click in the Plot Area,  
Format Plot Area  
Click on the Fill Tab and set the Fill to No Fill

Click outside the chart

### Apply a Conditional Formatting to the Range behind the Chart

Select the range E3:L15 (You won’t be able to use a mouse) or drag the chart out of the way first.

Goto Conditional Formatting Tab  
New Rule  
Use a formula to determine which cells to format  
Enter the formula: =$C$15>0  
Select the Format Button and select a Light Redish Color  
Ok

Goto Conditional Formatting Tab  
New Rule  
Use a formula to determine which cells to format  
Enter the formula: =$C$15<=0  
Select the Format Button and select a Light Greenish Color  
Ok

[![CFCBG06](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG06.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG06.png)

Now change the value of C15 from 90 to 10

The chart should change as per the below image:

[![CBG01](https://chandoo.org/wp/wp-content/uploads/2015/03/CBG01.gif)](https://chandoo.org/wp/wp-content/uploads/2015/03/CBG01.gif)

### Advantages:

*   Doesn’t require VBA (VBA not permitted on some corporate systems)
*   Simple to setup for those unfamiliar with VBA

### Disadvantages:

*   The Chart is locked to the cells and can’t be moved moved independently of the background cells
*   More difficult to implement multiple color scenarios
*   Harder to permit independent changes to the Chart and Plot areas

Using VBA to directly change the color of the Chart Chart Area
--------------------------------------------------------------

In the sample file goto the VBA Technique worksheet

You will see the same set of data with dates and Scores for each date

Select the Chart and notice that the Chart is called “Chart 1”

[![CFCBG07](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG07.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG07.png)

Goto VBA, Press Alt+F11

Double click on the VBA Technique code module

[![CFCBG08](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG081.png)](https://chandoo.org/wp/wp-content/uploads/2015/03/CFCBG081.png)

Copy and paste the following code into the module

> Private Sub Worksheet\_Calculate()
> 
> Dim myColor As Long
> Dim myChart As String
> 
> Application.EnableEvents = False
> 
> If ActiveSheet.Name <> "VBA Technique" Then Exit Sub
> 
> myChart = "Chart 1"
> 
> If \[c15\] <> \[OldSlope\] Then
> 
>   If \[c15\] > 0 Then
>     myColor = RGB(250, 190, 145) 'Apricot
>   Else
>     myColor = RGB(135, 235, 145) 'Pale Green
>   End If
>   
>   ActiveSheet.ChartObjects(myChart).Activate
>   ' Color the Chart Area
>   With ActiveSheet.Shapes(myChart).Fill
>     .Visible = msoTrue
>     .ForeColor.RGB = myColor
>     .Transparency = 0
>     .Solid
>   End With
>   
>   ' Color the Plot Area
>   ActiveChart.PlotArea.Select
>   With Selection.Format.Fill
>     .Visible = msoTrue
>     .ForeColor.RGB = myColor
>     .Transparency = 0
>     .Solid
>   End With
>   
>   ActiveWorkbook.Names.Add Name:="OldSlope", RefersToR1C1:="=" + CStr(Cells(15, 3).Value)
> End If
> 
> Application.EnableEvents = True
> Range("C17").Select
> 
> End Sub

Return to the Excel worksheet

Now change the value of C15 from 90 to 10

[![CBG02](https://chandoo.org/wp/wp-content/uploads/2015/03/CBG02.gif)](https://chandoo.org/wp/wp-content/uploads/2015/03/CBG02.gif)

If the Chart area doesn’t change color follow the following few steps

Goto VBA (Alt+F11)  
Open the Immediate window (Ctrl+G)  
Type in Application.EnableEvents = True press enter  
Go back to Excel (Alt+F11)

### Advantages:

*   Allows the Chart to be moved independently of the background cells
*   Allows a much simpler implementation of multiple color scenarios
*   Allows independent changes to the Chart and Plot areas as well as other Chart Elements

### Disadvantages:

*   Requires VBA (not permitted on some corporate systems)

Other Chart Conditional Formatting Posts
----------------------------------------

You may also be interested in the following Chart Formatting posts:

[http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/](http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/ "http://chandoo.org/wp/2011/08/19/selective-chart-axis-formating/")

[http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/](http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/ "http://chandoo.org/wp/2011/08/22/custom-chart-axis-formating-part-2/")

Closing
-------

What do you think of these techniques?

Let us know in the comments below.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [19 Comments](https://chandoo.org/wp/conditionally-format-chart-backgrounds/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/conditionally-format-chart-backgrounds/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousFormatting shortcuts for keyboard junkies](https://chandoo.org/wp/formatting-shortcuts/)

[NextUse apply names to create readable formulas \[quick tip\]Next](https://chandoo.org/wp/use-apply-names-to-create-readable-formulas-quick-tip/)

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
    
    [Reply](https://chandoo.org/wp/conditionally-format-chart-backgrounds/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/conditionally-format-chart-backgrounds/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/conditionally-format-chart-backgrounds/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ