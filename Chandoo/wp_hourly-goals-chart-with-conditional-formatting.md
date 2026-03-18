# Hourly Goals Chart with Conditional Formatting » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Hourly Goals Chart with Conditional Formatting
==============================================

*   Last updated on September 1, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

A while back I developed a solution to a Chandoo.org Forum question, where the user wanted a 4 level doughnut chart where each doughnut was made up of 12 segments and each segment was to be colored based on a value within a range.

[![HGC01](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC01.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC01.png)

You can read the original post here: [http://forum.chandoo.org/threads/hourly-goals-chart.30621/](http://forum.chandoo.org/threads/hourly-goals-chart.30621/)

This post will examine the techniques I used for the solution.

Data
----

Download the sample file: Download [Hourly Goals Chart File](https://chandoo.org/wp/wp-content/uploads/2016/09/Hourly-Goals-Chart.xlsm)

[![HGC02](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC02.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC02.png)

The first thing to note is that there are 4 column of data, one for each measure of Safety, Quality, Delivery and Cost.

Secondly is that each measurement has 12 values representing the times from 4:30 am to 3:30 pm.

We need to setup a Doughnut Chart with 4 layers of 12 segments each

The easiest way to do this is to replicate the data area, but fill it with the same value in all cells,

I choose 1, but as long as all values are the same value, it can be any value

[![HGC03](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC03.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC03.png)

### Add a Doughnut Chart

Select the Range A16:E28

Goto the Insert, Chart and select the Pie/Doughnut menu

[![HGC04](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC04.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC04.png)

[![HGC05](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC05.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC05.png)

We have a bit of work to do yet to get the charts format correct

First select the chart then select the Chart’s Legend and press **Delete**

[![HGC06](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC06.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC06.png)

Next with the chart still selected, Right Click on any Doughnut and select **Format Data Series**

Set the Doughnut Hole Size to **25%**

Do not change the angle of the first slice

[![HGC07](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC07.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC07.png)

Right  click on the Outer Doughnut and select **Add Data Labels, Data Labels**

[![HGC08](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC08.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC08.png)

Right Click on any Data Label and Select **Format Data Labels**

Tick Value From Cells, Select a range **A17:A28**

Untick Value

Untick Leader Lines

[![HGC09b](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC09b.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC09b.png)

Now manually click and drag each data label outwards to its final location

[![HGC10](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC10.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC10.png)

Finally set the Border Color for the doughnuts

Right Click on each Doughnut in turn

Set the Doughnut’s Border Line to a Grey Color and a 2 Pt line size

[![HGC11](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC11.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC11.png)

We can now add a text box for the Doughnut Labels

With the chart selected, goto the **Insert, Text Box** menu

Drag a Text Box inside the chart

Right click on the Text Box and edit Text and type in the value **Cost**

Now repeat this for the other 3 Doughnuts

[![HGC31](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC31.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC31.png)

Connect the Doughnut Segments to the Data Area
----------------------------------------------

We now have a basic Doughnut chart with all the facilities we require.

Unfortunately, Excel doesn’t have a built-in Conditional Formatting option for charts.

So we will need to develop a system using some simple VBA.

### Understand the Doughnut Chart

To write a piece of code we will need to loop through each segment of each doughnut and reference it back to the source data area

Then use some code to set the fill color

then repeat for each segment

To do this we need to understand which doughnut is which column of data and which segment in the doughnut is which time period

First select the inner Doughnut, Note that when you select it, Excel highlights the Safety Series as well as showing the Series Number in the Formula Bar

[![HGC12a](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC12a.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC12a.png)

Repeat with the outer Series and you will see that Doughnut 4 is connected to the Cost Data and is series 4.

[![HGC12b](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC12b.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC12b.png)

To determine which segment is which goto cell E17 and change the value from 1 to 2

[![HGC13b](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC13b.png)](https://chandoo.org/wp/wp-content/uploads/2016/08/HGC13b.png)

So we understand that the series go from Value 1 to 4, Inner to Outer Doughnuts and that the segments go from value 1 to 12 clockwise, starting to the right of 12 O’Clock.

Finally select the Chart and make note of it’s name.

The Charts Name is shown in the Name Dialog above cell A1

[![HGC16a](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC16a.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC16a.png)

### Now for some VBA

Lets start by first manually recording a macro in VBA and we will then edit and add to the macro to get our final result

Start the macro Recorder by Pressing the Macro Button in the lower left corner of the Excel Window

[![HGC14a](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC14a.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC14a.png)

Note the Macro Name, which is most likely Macro1 and press Ok

Now everything that you do is being recorded by the Visual Basic Editor (VBE)

Select the Outer Doughnut, then select Segment one, then Right Click on Segment one, **Format Data Point**

Select the Fill & Line menu

Set the Fill to a Solid Fill and Select a Color Red

You can now stop macro recording by pressing the Macro button again

[![HGC15a](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC15a.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC15a.png)

Lets look at our code

To change to VBA press the Alt+F11 button

You should have a screen similar to this:

[![HGC17](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC17.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC17.png)

Take note of the above.

We can see that we have a Macro1 subroutine, located in Module 1 of our Excel file.

If you can’t see a Properties or Immediate window, don’t worry.

Looking at the VBA Code we can see

[![HGC18](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC18.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC18.png)

1.  That the chart is called Chart 1
2.  We selected Doughnut 4, the outer doughnut
3.  We selected the first segment in Doughnut 4
4.  We set the Fill Color of Segment 1 to Red  = RGB(255, 0, 0)

So this little bit of code will form the basis of our macro

What we need to do next is to place that within 2 loops, one loop for the Doughnut and one loop for the Segment

So lets do that:

[![HGC19](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC19.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC19.png)

You can see above that we have initialised two variables Doughnut and Segment as Integers

We have setup two loops, one for the Doughnut which will loop from 1 to 4 and a second loop for the Segment, which will loop from 1 to 12.

We can now use these variables within the code to reference each Doughnut / Segment as relevent

[![HGC20](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC20.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC20.png)

The next thing is to add lines to lookup the value of the measure in the original data table.

We can use our variables to assist us with this:

I have added a new variable declaration myVal and declared it an Integer as it is only storing the values from, 0 to 3.

Then we retrieve the value from the data area by using a Range(“”).Offset(Row,Column) combination.

We know that the segment loops from 1 to 12 and this is the Row Offset in each Doughnut.

The Doughnut loops from 1 to 4 and this is the Column Offset from the cell A1

[![HGC21](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC21.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC21.png)

Next we need to allow for each fill color remembering that the data area has a legend

[![HGC22](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC22.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC22.png)

We could loop from a value of 0 to 3 and check the new variable myVal against each value and set the color.

But VBA has a Select Case function which is ideally suited to this task

[![HGC23](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC23.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC23.png)

A also took the opportunity to streamline the Chart selection process in the previous step

That allowed the use of the With Object construct, allowing the Select case to use the myVal to apply different colors to the fill property of each segment

At this stage we can run the code, by simply pressing F5 in VBA

[![HGC24](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC24.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC24.png)

We can change the code to allow it to update automatically when Data range changes

To do this we need to shift the code to a Sheet1 Code Module associated with Worksheet Sheet 1

[![HGC26](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC26.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC26.png)

Note above that the code is now located in a **Private Sub Worksheet\_Change event**. This means that the code runs whenever worksheet1 chnages.

The next line If Intersect(ActiveCell, Range(“B2:E13”)) Is Nothing Or Target.Count > 1 Then Exit Sub

Checks whether the cell that changed was not part of our Data Area or that multiple cells were selected.

If either are are true the macro ends

Then finally I removed the MyVal calculation and made it part of the Select Case function.

because we aren’t using myVal I removed the **Dim myVal** statement

We can now also remove **Module 1**, right click on it and Remove Module.

Save the file and return to Excel with Alt+F11

You can now change any cells in the data area and the macro updates the chart accordingly

Can we tidy up the layout of the worksheet?
-------------------------------------------

Although we now have a fully functional model, we are stuck with an ugly worksheet layout because our template of 1’s is being used to support the framework of the 4 Doughnuts in the chart.

What if there was another way to achieve that?

Well there is.

Firstly, we could simply shift the range A18:ER30 well away from the Chart and data area or even move it to another worksheet.

[![HGC27](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC27.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC27.png)

This will work, but risks a person adding data, rows or columns and messing up the layout

But there is a better way

I am going to add 4 Named Formula to the worksheet, one for each Doughnut

Goto the **Formula, Name Manager** Tab and add 4 Names as listed below:

\_Safety      =1+(ROW(OFFSET(Sheet1!$A$1,,,12,1))-1)\*0

\_Cost        =\_Safety

\_Delivery  =\_Safety

\_Quality  =\_Safety

[![HGC28](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC28.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC28.png)

The 4 Names now contain an array of 12 x 1 each with a value 1.

We can use that to link the Doughnuts to instead of the Physical Range

Right click on the chart and **Select Data**

[![HGC30](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC30.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC30.png)

Select each Doughnut in term and **Edit**

Change the Series Name to Row 1 and insert the Names into the Series values dialog.

Note that the formula must include the Worksheet name **\=Sheet1!\_Safety** etc

[![HGC29](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC29.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC29.png)

Repeat this for the 4 Series

You can now select the framework range: A18:E30 and press **Delete**

[![HGC32](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC32.png)](https://chandoo.org/wp/wp-content/uploads/2016/09/HGC32.png)

The chart remains intact and is now supported by the Named Formula

Change some values in the Data range at the top and the Chart updates as it should.

You can download the final version of the file here: [Download Completed File](https://chandoo.org/wp/wp-content/uploads/2016/09/Hourly-Goals-Chart-Final.xlsm)

Final Thoughts
--------------

The technique applied to the doughnut chart above can fairly easily be modified to any chart type or in fact any other shapes.

Let me know what you think in the comments below:

ps: This has been one of my hardest posts to write, simply because Microsoft has misspelt Doughnut. In my native Australian English it is Donut.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting/#respond)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousVisualizing Financial Metrics – 30 Alternatives](https://chandoo.org/wp/visualizing-financial-metrics/)

[Next18 ways to turn analysis projects into a nightmareNext](https://chandoo.org/wp/analysis-worst-practices/)

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
    
    [Reply](https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ