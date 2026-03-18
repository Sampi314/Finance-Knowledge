# Apply Conditional Formatting to Chart Data Labels

**Source:** https://chandoo.org/wp/conditional-formatting-chart-data-labels

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Conditional Formatting – Chart Data Labels
==========================================

*   Last updated on October 9, 2017

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

This week in the Chandoo.org Forums, Greg asked the question, “_I would like to conditionally format the data labels position to be above the plot line in a scatter plot if a certain cell contains ‘True’ and below the plot line if that cell contains ‘False’.”_

Greg also wanted a Non-VBA Solution.

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl01.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl01.png)

This post will describe how this is achieved as well as extend the idea into the fourth dimension.

All the charts in this post are available in the sample file: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2017/10/Conditional-Labels-in-a-Chart.xlsx)
.

The Concept
-----------

The concept applied here to achieve the final result that Greg wants is that charts can use multiple data series.

These data series do not have to be visible but they can, at the same time, have Data Labels or other formatting applied.

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl20.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl20.png)

The Application
---------------

First setup a set of data,

I have used values A to P as X Axis Labels and used a formula \=Randbetween(10,20) in column C for the Y Values for the chart

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl02.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl02.png)

Now add a Data Validation to a cell **G3**

Goto the **Data, Data Validation Tab** and select **Data Validation**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl03.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl03.png)

next add 2 columns

**D3**: \=IF($G$3,C3,NA())

**E3**: \=IF($G$3,NA(),C3)

![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl04.png)

Copy these down to Row 18

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl05.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl05.png)

Select the Range **B3:E18**, note it includes the X Axis Labels and Headers

Now goto the **Insert, Chart** tab and select the chart type you want to use. I have chosen a Line Chart

Excel will draw a Chart with 3 series of lines

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl06.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl06.png)

Now is a simple job of applying labels and formatting as applicable

The first thing to notice is that the chart has 3 series, Random Value, True and False

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl07.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl07.png)

We can only see the True series, as it is in front of the Random Value series, The False series is hidden for now.

Select the True Series by Clicking on it

Then Right Click on it and Add Data Label

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl08.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl08.png)

Excel adds the Data Labels to the True Series

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl09.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl09.png)

Right click on any of the Data Labels and select Format Data Label

For the True values we will plot them above the Data Point

Change the values as shown above

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl10.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl10.png)

Right click on the Data Series Line (the orange line) and select Format Data Series

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl11.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl11.png)

Change the Line Type to No Line

The Orange line is gone and there is now a Blue Line, this is the Random Values series

Note we can still see the Data Labels for the True Series, even though the True Series Line is not visible

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl12.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl12.png)

You can set or disable markers whilst you are here as well

Next select the False Series, by changing the Data Validation cell to FALSE

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl13.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl13.png)

We can now see the False Data Series and the Random Values Series which is behind the Grey Line as before.

Right click the False Data Series, Add Data Labels

Then Right Click the New Data Labels and Change there settings to be below

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl14.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl14.png)

Finally set the False Data Series Line Line Type to No Line

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl15.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl15.png)

Now we can see the Rand Value series (Blue line) with the Data Labels showing for the False Series below the line

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl16.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl16.png)

Change the Data validation from True to False and vice-versa and observe that Excel is only showing the series Labels for the Data Series which has values and doesn’t have #N/A errors in Columns D & E

So we are seeing 3 Series and 2 sets of Data Labels, it is just that we have set Two of the Line Types to No Line and Excel doesn’t display Series Values where the Value is the error value #N/A.

Now set the data Validation to True and select the Data Labels Font Color to Blue

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl17.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl17.png)

Repeat the Process for the False Data Labels and set them to Red

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl18.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl18.png)

Finally clean up the legend

Select the Chart, then click on the legend

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl19.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl19.png)

Then click on TRUE and press the Delete Key

Repeat for the FALSE Legend

**Our Final Chart**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl01.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl01.png)

Change the Data Validation cell to True/False to verify that the system is working.

The techniques described above can be applied to most chart types.

Care must be taken with Column and Bar and other cumulative chart types.

Extensions
----------

Having seen how Excel treats the #N/A error we can use that to create a number of variations for our Data Labels

**Conditionally Format Data Labels above and below a set value**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl21.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl21.png)

This is achieved by using a formula that applies to individual data points in each series

so that when a Data Point in a series (>15) is less than 15 it will return a #N/A error and not be displayed and also when a Data Point in a series (<=15) is greater than 15 it will return a #N/A error and not be displayed

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl22.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl22.png)

**Add a Third or more Set of Conditional Data Labels**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl23.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl23.png)

This is achieved by simply adding a Fourth Data Series to the chart and adjusting the formulas as appropriate

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl24.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl24.png)

**Add Conditional Formatted Text Data Labels to Highlight Points  
**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl25.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl25.png)

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl26.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl26.png)

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl27.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl27.png)

These are achieved by using the above techniques but instead of Displaying **Values** for the Data Label Series, we use the **Value From Cells** option

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl28.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl28.png)

**Add Conditionally Formatted Markers to Highlight Points**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl33.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl33.png)

This is achieved by using the above techniques but alter the markers for the two helper Columns as well as the Data Labels

**Explore**

You can explore how these are constructed using the sample file.

All the above charts are shown in the sample file: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2017/10/Conditional-Labels-in-a-Chart.xlsx)
.

Selecting Chart Series
----------------------

One of the annoying aspects of dealing with charts and formatting individual series is the ability to select hidden or covered series

Fortunately there are a number of ways to get around this.

**Use the arrows Keys**

In older versions of Excel, you can select a Chart, then use the Up/Down arrow keys to cycle through all the chart objects.

Once you had the object you wanted Press Ctrl+F1 to bring up it’s format Properties

Unfortunately Microsoft in its wisdom has removed this functionality in recent versions of Excel, so try it, If it works, Enjoy, If it doesn’t keep reading

**Use the Tab Menu**

If you select a Chart you will see two extra menu items on the Tab Menu[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl29.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl29.png)

These are the Chart Design and Chart format Tabs

Select the **Chart Format** Tab

Then Goto the Drop down on the Far Left of the Tab

It contains a list of all the available Chart Objects,

Select the Chart Object you want, then press **Ctrl+1** to bring up the format options

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl30.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl30.png)

**Use the Chart Format Menu**

If you select a Chart and select any part of the chart press **Ctrl+1** and the **Format** Menu for that object is shown

Now use the small drop down just under the **Format** Title and select the Object you wish to change

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl31.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl31.png)

Warning
-------

Despite being able to use the Excel \=NA() function to force an **#N/A** error, which is ignored by Excel, future versions of Excel maybe about to change this behavior.

Some people using the Excel 365 Insider Fast Edition are noticing a new Dialog option.

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl32.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/condlbl32.png)

So keep in mind if all of a sudden this behavior changes, you may have upgraded Excel and introduced this new menu

You can read more about how to use this new functionality here:

[http://www.exceluser.com/excel\_dashboards/two-business-uses-for-excels-new-chart-feature.html](http://www.exceluser.com/excel_dashboards/two-business-uses-for-excels-new-chart-feature.html)

Comments
--------

If you have any other ideas about how to use this functionality let us all know in the comments below

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/conditional-formatting-chart-data-labels/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/conditional-formatting-chart-data-labels/#respond)
    
*   Tagged under [chart](https://chandoo.org/wp/tag/chart/)
    , [Chart Data Label](https://chandoo.org/wp/tag/chart-data-label/)
    , [Condional Format](https://chandoo.org/wp/tag/condional-format/)
    , [Data Label](https://chandoo.org/wp/tag/data-label/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousHistograms & Pareto charts in Excel – tutorial, tips and downloadable template](https://chandoo.org/wp/histograms-pareto-charts-in-excel/)

[NextHow to Distribute Players Between Teams – EvenlyNext](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/)

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
    
    [Reply](https://chandoo.org/wp/conditional-formatting-chart-data-labels/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/conditional-formatting-chart-data-labels/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/conditional-formatting-chart-data-labels/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ