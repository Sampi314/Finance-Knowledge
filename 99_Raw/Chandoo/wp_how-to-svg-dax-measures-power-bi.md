# How to create SVG DAX Measures in Power BI (Easy, step-by-step Tutorial with Sample File) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-svg-dax-measures-power-bi

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    

How to create SVG DAX Measures in Power BI (Easy, step-by-step Tutorial with Sample File)
=========================================================================================

*   Last updated on May 6, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2025/05/svg-dax-measures-demo.gif)

SVG (Scalable Vector Graphics) is a great way to add a bit of flavor and pizzazz to your boring Power BI reports. I have been using them for a while and really love how easy and fun they are to work with. So today, let me share the technique and provide sample measure code that you can readily use to make your first SVG DAX graphic in Power BI.

What we are going to build – Demo of SVG DAX
--------------------------------------------

We are going to create this _rectangle bar chart_ with SVG. It is a simple graph that shows a KPI (ex: Attendance Percentage).

![](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0088.png)

What you need?
--------------

*   Any recent version of Power BI Desktop
*   A measure or set of measures that you want to visualize with SVG

Creating your first SVG DAX Measure – Step-by-step Instructions
---------------------------------------------------------------

### Step 1: Make a measure to visualize

If not already done, create a measure to visualize with SVG. In our example, we want to see attendance percentage as a rectangle. So I have the measure `[attendance percentage]` in my model.

    Attendance Percentage = DIVIDE([Total Attendance], [Total Days]) //Example KPI measure

### Step 2: Create the SVG Measure

Create a new measure for our SVG. Use below code as starting point and customize it as per your model.

    SVG Rectangle = 
        var att_pct = [Attendance Percentage] // your KPI goes here
        var rect_width = 300 * att_pct // scaling the KPI to our SVG rectangle width. 100% = 300pixels
        var att_pct_disp = FORMAT(att_pct, "0%") // formatting KPI to display inside the rectangle
    return
    
    "data:image/svg+xml;utf8, 
    <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 60'>
      <rect x='5.522' y='4.682' width='"&rect_width &"' height='50' style='fill:#DE913A; stroke: rgb(0, 0, 0);' rx='5.277' ry='5.277'/>
      <text style='fill: #111111; font-family: "Arial", sans-serif; font-size: 28px; font-weight: 700; white-space: pre;' x='14.165' y='40.696'>"&att_pct_disp&"</text>
    </svg>"

### Step 3: Set Measure Category to Image URL

![](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0089.png)

Now that we have the \[SVG Rectangle\] measure in our model,

*   Select the `[SVG Rectangle]` measure
*   Go to _Measure Tools > Data Category_
*   Set it to **Image URL**

Boom! Now your table or matrix will show SVG bars

### Step 4: Use the SVG Measure inside a visual

Set up a table / matrix visual. Add your SVG rectangle measure to the visual and we can instantly see the rectangles drawn. See this quick demo.

![](https://chandoo.org/wp/wp-content/uploads/2025/05/adding-svg-measure-to-table-in-powerbi.gif)

### Which Visuals can I use to see SVG Images?

Currently (as of May 2025), the below Power BI visuals are supported for SVG based DAX measures.

*   Table
*   Matrix
*   New Card Visual (sometimes buggy)
*   New Button Slicer Visual

SVG DAX Measures – Video Tutorial
---------------------------------

I made a detailed explanation of SVG measures with few different examples and code explanation. You can watch it below or [on my YouTube channel](https://www.youtube.com/watch?v=djUyi4oOAEM)
.

https://www.youtube.com/watch?v=djUyi4oOAEM

Sample File – SVG DAX Measures
------------------------------

[Click here to download Sample Power BI Workbook](https://github.com/chandoo-org/Power-BI/blob/c45a9e06e411beddafa4180e0dd172849581ac2f/SVG/svg-examples-chandoo.pbix)
 with the SVG DAX measure examples. Customize the measures or create new to learn how to apply this technique. [Checkout the SVG Project](https://github.com/chandoo-org/Power-BI/tree/main/SVG)
 on my Github for all the other files and additional resources.

When and Why Use SVG?
---------------------

SVGs let you:

*   Build **pixel-perfect visuals** in Power BI
*   Avoid external custom visuals
*   Add creative KPIs (think calendar heatmaps, progress bars, mini-charts, and more)
*   Control layout and formatting via code

* * *

Watch Out For…
--------------

*   **Performance**: SVGs add some overhead, especially with large datasets.
*   **Measure length**: Power BI has limits (~32k characters per measure).
*   **Visual support**: Works best in _tables_ and _matrix visuals_; new card visuals are hit-or-miss.
*   **Tooltips**: Without customization, Power BI may show raw SVG code as tooltip.

* * *

Pro Tips
--------

*   Use a tool like **[Boxy SVG Editor](https://boxy-svg.com/app)
    ** to design and export SVGs
*   When copying SVG code from elsewhere, Replace all `"` with `'` to simplify embedding in DAX
*   Explore SVG templates from [Kerry Kolosko](https://kerrykolosko.com/portfolio/)
     to fast-track your visuals

* * *

What’s Next?
------------

This is part 1 of my SVG + DAX journey. In the next post, we’ll break down a full SVG-powered attendance dashboard—calendar heatmap, employee cards, and all. We are going to build this in the next part:

![](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0090.png)

Until then, experiment and impress your colleagues with a whole new level of custom Power BI visuals.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/#respond)
    
*   Tagged under [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [dax](https://chandoo.org/wp/tag/dax/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [svg measures](https://chandoo.org/wp/tag/svg-measures/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    

[PrevPreviousHow to Create a Power BI Dashboard for Insurance Analytics (With Examples)](https://chandoo.org/wp/power-bi-insurance-analytics/)

[NextHow to insert dates in Excel automaticallyNext](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

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
    
    [Reply](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-svg-dax-measures-power-bi/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ