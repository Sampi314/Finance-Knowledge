# Dynamic Dashboard in Excel - Pulling it all together [Part 4 of 4] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-dashboard-tutorial-4

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Dynamic Dashboard in Excel – Pulling it all together \[Part 4 of 4\]
====================================================================

*   Last updated on May 26, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Dynamic Dashboard in Excel - Part 4 of 4](https://chandoo.org/img/ed/excel-dynamic-dashboard-final-th.png)This is a guest post by _**Myles Arnott**_ from [Clarity Consultancy Services – UK](http://www.clarityconsultancyservices.co.uk/)
.

*   Part 1: [Introduction & overview](http://chandoo.org/wp/2010/03/16/excel-dashboard-tutorial-1/)
    
*   Part 2: [Dynamic Charts in the Dashboard](http://chandoo.org/wp/2010/03/30/excel-dashboard-tutorial-2/)
    
*   Part 3: [VBA behind the Dynamic Dashboard a simple example](http://chandoo.org/wp/2010/04/22/excel-dashboard-tutorial-3/)
    
*   **Part 4: Pulling it all together**

In this the final post we are going to pull it all together to create our final Dynamic Dashboard model.

**The dynamic dashboard VBA example can be downloaded [here](https://chandoo.org/wp/excel-dashboard-tutorial-4/chandoo.org/img/ed/dynamic-dashboard-vba-example.xls)
** \[[Mirror](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/dynamic-dashboard-vba-example.xls)\
\]

### Firstly a quick recap of what we have covered so far:

*   How to structure a workbook with user friendly front page and user notes
*   Using a structured inputs or driver page
*   How to create a range of dynamic charts
*   Some simple VBA to move items around a page based on the user’s parameters

Ok, so lets get to work to combine all of the above into a workable model. There is a lot to cover here so as Chandoo often says, may be time to grab a coffee!

First things first you need to bring all of the charts that you want to have in your dashboard into the spreadsheet and label up the tabs accordingly.

Homepage
--------

I find that for a model that has multiple tabs a homepage allows any user to easily understand the contents and easily navigate to the page they are interested in.

Obviously you can make the homepage look entirely how you want. I use this design as my standard layout with a relevant title, business logo and contents structured to suit the model.

I use the free form shape to draw my boxes. This can be a bit fiddly to achieve but I think that the end result is worth the effort.

![Using Freeform shapes in Dashboard](https://chandoo.org/img/ed/free-form-shapes-in-dashboard.png)

Links are achieved by inserting hyperlinks. I choose to reformat these to change the color and remove the underlining. \[related: [create a table of contents sheet in excel](http://chandoo.org/wp/2009/02/16/excel-table-of-contents-etc/)\
\]

![Hyperlinks - Creating an index page in Excel Dashboard](https://chandoo.org/img/ed/hyperlins-index-sheet-excel.png)

The help sheet is courtesy of John Walkenbach. Of all of the possible user note solutions I have encountered this to me offers the simplest and most user friendly approach. I use this in all the models that I develop for clients.

Now on to the central point of the model: The Dynamic Dashboard
---------------------------------------------------------------

There are three key parts to the dashboard, the driver area, the report area and the chart location matrix.

### Driver area

This is the user interface which allows the user to hide, view or position a particular chart.  
![Driver Area - Dynamic Dashboard](https://chandoo.org/img/ed/driver-area-dynamic-dashboard.png)  
Each title is hyperlinked to the page containing the chart in question. Each location cell is a named range with data validation to control the inputs. I have also added an input message via the data validation function.

The named range relates to the chart eg: Chart one is CH\_1, chart 2 is CH\_2 etc.

The [validation list](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
 is based on a named range Position\_Range (in the Inputs tab)  
![Data Validation settings - Dynamic Dashboard](https://chandoo.org/img/ed/data-validation-settings-dynamic-dashboard.png)  
The input message is defined in the Input message tab within the validation function menu.

### Report area

This is your dashboard, the area to contain your charts. It is simply an area defined and formatted to be the container for the dashboard charts that the user chooses.

### The Chart Location Matrix

The entries for this matrix are made in the inputs tab and pull through to the dynamic dashboard tab. Each cell of the matrix in the dynamic dashboard tab is a named range. These named ranges are referenced in the VBA. I will discuss this later in the post.  
![Chart Location Matrix - Dynamic Dashboard in Excel](https://chandoo.org/img/ed/chart-location-matrix-dynamic-dashboard.png)  
This matrix defines where each chart will be placed. Getting these positioning references correct takes a little bit of trial and error but is pretty simple to achieve.

Now onto the images themselves. The images that the model moves around are pictures of the charts in each tab. This is achieved using the camera tool. Chandoo has written an [excellent post on the camera tool](http://chandoo.org/wp/2008/12/02/excel-camera-tool-help/)
 so I will not repeat that here.

I have then renamed the images by selecting the image and changing the name in the name box.

As you can see the chart below is called Chart4. You will also notice that in the formula bar it refers to =’CH4′!$B$2:$F$17. This is the image that it has taken from the CH4 tab.  
![Using Camera Tool - dynamic dashboard in excel](https://chandoo.org/img/ed/using-camera-tool-dynamic-dashboard.png)

The final step is to add a hyperlink back to the chart page so that the user can navigate to the relevant page by clicking on the image.

So now we have a structured model, images of our charts and everything in place to put in the VBA.

The VBA
-------

The basics for the VBA were covered in part 3 – [VBA behind the Dynamic Dashboard a simple example](http://chandoo.org/wp/2010/04/22/excel-dashboard-tutorial-3/)
.

### Location

Unlike in part 3, as we would like to avoid clicking on a button every time we want to update the layout, the VBA is located in the Dynamic Dashboard sheet itself rather than in a module.  
![Project Explorer area](https://chandoo.org/img/ed/project-explorer-vba.png)

### The event target

It important to restrict the event function to specific cells. This stops the macro running completely every time any cell is changed in the sheet. In this case I have restricted it to the cells where the user chooses the chart’s position.

### Variables

We need to define the variable in the VBA so that Excel knows where to put the images we have moved.

To do this we firstly define the variables and then link them to the named ranges in the chart location matrix.

To manage the loop code I have also used “I” as the current iteration and “ix” as the last desired iteration.

### Moving the charts

This is based on the VBA used in part three of the post.

### Loop

To avoid having to rewrite the code for each chart we instead use a loop that continues to loop as long as the current iteration “I” is less than the last desired iteration “ix”. I.e. loop for the eight charts and then stop.

The variable “I” is also passed to the position part of the VBA to select the relevant image to move:

ActiveSheet.Shapes(“chart” & i).Select

### Ok So here is the full code:

Private Sub Worksheet\_Change(ByVal Target As Range)If Not Intersect(Target, Range(“C7,C8,C9,C10,F7,F8,F9,F10”)) Is Nothing Then

Dim Topleft\_T As Integer  
Dim Topleft\_L As Integer  
Dim MiddleLeft\_T As Integer  
Dim MiddleLeft\_L As Integer  
Dim BottomLeft\_T As Integer  
Dim BottomLeft\_L As Integer  
Dim Topright\_T As Integer  
Dim Topright\_L As Integer  
Dim Middleright\_T As Integer  
Dim Middleright\_L As Integer  
Dim Bottomright\_T As Integer  
Dim Bottomright\_L As Integer  
Dim Hide\_T As Integer  
Dim Hide\_L As Integer  
Dim View\_T As Integer  
Dim View\_L As Integer  
Dim i As Integer  
Dim ix As Integer

‘Define the position values (based on named ranges)

Topleft\_T = Range(“Top\_Left\_T”).Value  
Topleft\_L = Range(“Top\_Left\_L”).Value  
MiddleLeft\_T = Range(“Middle\_left\_T”).Value  
MiddleLeft\_L = Range(“Middle\_left\_L”).Value  
BottomLeft\_T = Range(“Bottom\_left\_T”).Value  
BottomLeft\_L = Range(“Bottom\_left\_L”).Value  
Topright\_T = Range(“Top\_right\_T”).Value  
Topright\_L = Range(“Top\_right\_L”).Value  
Middleright\_T = Range(“Middle\_right\_T”).Value  
Middleright\_L = Range(“Middle\_right\_L”).Value  
Bottomright\_T = Range(“Bottom\_right\_T”).Value  
Bottomright\_L = Range(“Bottom\_right\_L”).Value  
View\_T = Range(“View\_T”).Value  
View\_L = Range(“View\_L”).Value  
Hide\_T = Range(“Hide\_T”).Value  
Hide\_L = Range(“Hide\_L”).Value

‘Set ix to be the number of charts  
ix = 8

‘reset i  
i = 1

”Select the shape and position it  
Do While i <= ix

ActiveSheet.Shapes(“chart” & i).Select  
If UCase(Range(“CH\_” & i).Value) = “TOP LEFT” Then  
Selection.ShapeRange.Top = Topleft\_T  
Selection.ShapeRange.Left = Topleft\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “MIDDLE LEFT” Then  
Selection.ShapeRange.Top = MiddleLeft\_T  
Selection.ShapeRange.Left = MiddleLeft\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “BOTTOM LEFT” Then  
Selection.ShapeRange.Top = BottomLeft\_T  
Selection.ShapeRange.Left = BottomLeft\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “TOP RIGHT” Then  
Selection.ShapeRange.Top = Topright\_T  
Selection.ShapeRange.Left = Topright\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “MIDDLE RIGHT” Then  
Selection.ShapeRange.Top = Middleright\_T  
Selection.ShapeRange.Left = Middleright\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “BOTTOM RIGHT” Then  
Selection.ShapeRange.Top = Bottomright\_T  
Selection.ShapeRange.Left = Bottomright\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “VIEW” Then  
Selection.ShapeRange.Top = View\_T  
Selection.ShapeRange.Left = View\_L  
ElseIf UCase(Range(“CH\_” & i).Value) = “HIDE” Then  
Selection.ShapeRange.Top = Hide\_T  
Selection.ShapeRange.Left = Hide\_L  
End If

i = i + 1

Loop

End If

End Sub

### Closing Thoughts

We now have a model that provides pertinent summary information to aid management decision making. It combines a high level of flexibility within each report and then allows the user to choose which reports to include and where to position them. This allows an enormous amount of flexibility over the message to be communicated.

I hope you enjoyed the post and please feel free to make comments and suggestions on the model.

Finally a huge thank you for Chandoo for agreeing to host this post for me.

### Download the complete dashboard

Go ahead and download the dashboard excel file. The dynamic dashboard can be downloaded [here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.xlsm)
 \[[mirror](http://chandoo.org/img/ed/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
, [ZIP Version](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/dynamic-dashboard/Dynamic%20Dashboard%20Illustration%20V1.1.zip)\
\]

It works on Excel 2007 and above. You need to enable macros and links to make it work.

### Added by Chandoo:

Myles has taken various important concepts like Microcharts, form controls, macros, camera snapshot, formulas etc and combined all these to create a truly outstanding dashboard. I am honored to feature his ideas and implementation here on PHD. I have learned several valuable tricks while exploring his dashboard. I am sure you would too.

**If you like this tutorial please say thanks to Myles.**

### Related Material & Resources

*   [Excel Dashboards – Tutorials & Templates Section of PHD](http://chandoo.org/wp/management-dashboards-excel/)
    
*   [6 Part Tutorial on Making KPI Dashboards in Excel](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/)
    
*   [Excel Dynamic Charts – Tutorials, Examples and Demos](http://chandoo.org/wp/tag/dynamic-charts)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/excel-dashboard-tutorial-4/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-dashboard-tutorial-4/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [charts](https://chandoo.org/wp/tag/charts/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [excel drawing](https://chandoo.org/wp/tag/excel-drawing/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [kpi dashboards](https://chandoo.org/wp/tag/kpi-dashboards/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [table of contents](https://chandoo.org/wp/tag/table-of-contents/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousDisplay Alerts in Dashboards to Grab User Attention \[Quick Tip\]](https://chandoo.org/wp/alerts-in-dashboards/)

[NextUse CTRL+Back Space to jump to active cell \[Shortcut\]Next](https://chandoo.org/wp/use-ctrlback-space-to-jump-to-active-cell/)

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
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-4/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-4/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-dashboard-tutorial-4/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ