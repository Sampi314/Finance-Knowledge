# How to create animated charts in Power Point [VBA] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/animated-charts-in-power-point

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Office Tips](https://chandoo.org/wp/category/office-tips/)
    

How to create animated charts in Power Point \[VBA\]
====================================================

*   Last updated on March 17, 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is a guest post by _[Chirayu](http://chandoo.org/forum/members/chirayu.11314/)
,_ a member of Chandoo.org forum.

### Foreword

I mainly write VBA code in Excel. I am in no means a PowerPoint VBA coder. It’s just that once you understand one type of VBA code it’s simple enough to do a bit of research & figure out the rest through trial and error.

This guide was created because of the question posted [here](http://chandoo.org/forum/threads/interactive-charts-in-power-point.27101/)
 which intrigued me & I drafted up a sample file for the same.

Animating charts in Power Point
-------------------------------

Animating Charts in PowerPoint cannot be done without the help of 3rd party software’s that create a flash file of the chart & embed it into the presentation.

However there is a workaround for this. Save your chart as multiple images & insert them (overlapping on top of each other). Use VBA on Developer tab Controls such as Combo Box, Option Button, Check Box etc. to “Bring To Front”” the corresponding image. Thus giving the illusion of an Animated Chart in PowerPoint.

This guide will teach you how to animate the charts, using the three Developer tab Controls that were mentioned before. The code & functionality only works in Slide Show Mode. File must be saved as PowerPoint Macro-Enabled Presentation (\*.pptm)

### First a quick demo of the chart:

We are going to build this.

![animated-power-point-chart-demo](https://chandoo.org/wp/wp-content/uploads/2016/03/animated-power-point-chart-demo.gif)

### How to Add Developer tab?

1.  Click on the office button / file menu at the top left in PowerPoint
2.  Go to Power Point options
3.  Tick the _Show developer tab in the ribbon_ option in the popup menu
    1.  If you are using PP 2010 or above, go to “Customize ribbon” tab and check the “Developer” ribbon to enable it.
4.  Close the Power Point options window.

### How to add selection pane?

In order to name the chart pictures, we need to use _selection pane. Y_ou can enable this by

**In Office 2013 or above:**

*   Go to Home > Select and click on Selection Pane.

**In Office 2010 or 2007:**

*   Go to Power Point Options
*   Click on Customize
*   From left hand side, choose “All commands”
*   Scroll down and select “Selection Pane”
*   Add this to the quick access toolbar
*   Now selection pane will be available on Quick Access Toolbar of PP.

### How to Insert & Rename the Developer tab Controls?

1.  Go to the Developer tab
2.  To insert a control, simply click on the one you want & then a + cursor should appear
3.  Use this to drag & create the Control you chose
4.  As an example for renaming the Control let’s add an Option Button. Which will look like this:![option-button-power-point](https://chandoo.org/wp/wp-content/uploads/2016/03/option-button-power-point.png)
5.  To rename this to Q1, right click it & select properties
6.  Then change name & caption as you want.

![option-button-properties](https://chandoo.org/wp/wp-content/uploads/2016/03/option-button-properties.png)

### How to Insert & Rename Images?

The reason you need to rename the images is:

*   Easier for identifying chart images when they need to be updated in future
*   Uniform VBA code that does not need alteration as all images having same naming convention as that listed in the VBA code

**To insert an image:**

1.  Click on the Insert tab and click on Picture
2.  Then browse to the image you want & click on it & then click OK. Repeat this step if you are creating an animated graph.
3.  To rename these pictures we just click on the **Selection Pane** button we added earlier. This will show us all the images & their names in the PowerPoint slide you are on. We can then rename these images to whatever we want. I chose Pic1, Pic2, Pic3, Pic4 as the Chart has a Quarterly data.
4.  Note that when you are creating dynamic charts, the images will need to be of the same size & must overlap each other. Otherwise it won’t look like a dynamic chart, as it will still do all the work but look out of sync. Example below of Quarterly chart overlap, where Q1, Q2, Q3, Q4 have been placed on top of each other.

![center-aligned-chart-images](https://chandoo.org/wp/wp-content/uploads/2016/03/center-aligned-chart-images.png)

VBA code to animate the chart
-----------------------------

This VBA code will mainly be used when we have the overlapping image scenario as all we are doing is bringing the image to the front.

The VBA code will also go in the same slide as where the Option Buttons were added.

Since Q1, Q2, Q3, Q4 buttons are in Sheet1. VBA code will be pasted in Sheet1.

*   To open the VBA screen Click on the Developer tab & & then on the left hand side menu of the popup
*   Write the below code in the white area that shows up

  

    
    Private Sub OptionButton1_Click()
    ActivePresentation.Slides(1).Shapes("Pic1").ZOrder msoBringToFront
    End Sub
    
    Private Sub OptionButton2_Click()
    ActivePresentation.Slides(1).Shapes("Pic2").ZOrder msoBringToFront
    End Sub
    
    Private Sub OptionButton3_Click()
    ActivePresentation.Slides(1).Shapes("Pic3").ZOrder msoBringToFront
    End Sub
    
    Private Sub OptionButton4_Click()
    ActivePresentation.Slides(1).Shapes("Pic4").ZOrder msoBringToFront
    End Sub
    

**How this code works?**

*   `OptionButton1_Click`: Means run the macro when the button is clicked
*   `ActivePresentation`: Means the current PowerPoint file you are using
*   `.Slides(1)`: Means the first slide of that file
*   `.Shapes("Pic1")`: Means the shape you are referring to. Images are also considered as shapes and as you remember Pic1 is actually the name given to the image of Q1 for the Dynamic graph
*   `.ZOrder msoBringToFront`: Means bring the shape to the front

### Download the Example Presentation

**[Click here to download the animated charts power point presentation](https://chandoo.org/wp/wp-content/uploads/2016/03/animated-charts.pptm)
**. Play with the animations in slides 2 & 3 to learn more. Examine the VBA code by using Developer ribbon > VBA.

### Summary

As you can see, it’s not that difficult to animate charts in PowerPoint. It just requires a workaround in order to do so. I have included few more examples in the downloadable presentation. Check them out and learn more. I hope that this guide is useful to you in animating your PowerPoint files.

### Thank you Chirayu

Thank you Chirayu for sharing this awesome technique with us. I really enjoyed playing with the animated charts file.

**_If you enjoyed this post,_** Please say thanks to Chirayu.

### Want more animated & interactive charts?

If you want to build interactive & animated charts using Excel, check out below examples & case studies:

*   [“How Trump happened” making animated chart in Excel](http://chandoo.org/wp/2016/03/02/how-trump-happened-in-excel/)
    
*   [How to create animated charts in Excel – podcast](http://chandoo.org/wp/2015/11/12/how-to-create-animated-charts-in-excel/)
    
*   [Fourth of July fireworks in Excel](http://chandoo.org/wp/2014/07/04/4th-of-july-fireworks-excel-animation/)
    
*   [Journey of hurricane Sandy – Interactive Excel chart](http://chandoo.org/wp/2012/10/31/hurricane-sandy-animated-chart/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [16 Comments](https://chandoo.org/wp/animated-charts-in-power-point/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/animated-charts-in-power-point/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [animation](https://chandoo.org/wp/tag/animation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [interactive charts](https://chandoo.org/wp/tag/interactive-charts/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [powerpoint](https://chandoo.org/wp/tag/powerpoint/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Office Tips](https://chandoo.org/wp/category/office-tips/)
    

[PrevPreviousCP053: Excel Data Validation for Dummies](https://chandoo.org/wp/cp053-excel-data-validation-for-dummies/)

[NextThese icons are so pretty, can I get them in green? \[conditional formatting trick\]Next](https://chandoo.org/wp/green-down-arrow-cf-trick/)

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
    
    [Reply](https://chandoo.org/wp/animated-charts-in-power-point/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/animated-charts-in-power-point/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/animated-charts-in-power-point/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ