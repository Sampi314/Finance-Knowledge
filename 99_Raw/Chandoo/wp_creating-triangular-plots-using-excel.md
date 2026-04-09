# Creating Triangular Plots using Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/creating-triangular-plots-using-excel

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Posts by Faseeh](https://chandoo.org/wp/category/posts-by-faseeh/)
    

Creating Triangular Plots using Excel
=====================================

*   Last updated on December 9, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post by [Faseeh](http://chandoo.org/forum/members/faseeh.1922/)
, one of the Excel Ninja’s at our forum._

### Triangular plot…! What is it?

Recently, a Chandoo.org forum member [asked this](http://chandoo.org/forum/threads/triangular-plot-gas-data-plot.12591/)
,

> I want to be able to make a graph that, in some aspects, looks like below, but I have no idea how to do it at all.
> 
> ![Triangular plot example - used in gas composition digrams](https://img.chandoo.org/c/example-triangular-plot.png)

After seeing it, I said to myself in Barney Stinson’s tone, ‘_**Challenge Accepted!**_‘

**The final plot is like this:**

![Triangular plot made using Excel](https://img.chandoo.org/c/triangular-plot-in-excel.png)

Making triangular plot in Excel – Tutorial
------------------------------------------

The first step to create such a chart starts from a manual drawing of how your chart will be looking like; at least you need to mark some important connecting points that will make smaller triangles.

The trick in this chart is _simply to locate points in all three sides of the triangle and connect them in a way that results in smaller triangle._ Here is a step by step approach to make this chart:

1.  Make a rough sketch of the triangle. Divide each side of the triangle roughly into the number of segments that you want, each side with equal number of segments (in this case 05 segments). And give each of them a number including corners of the triangle  
    ![Triangle plot outline. This helps us identify various points in the chart.](https://img.chandoo.org/c/triangle-outline.png)
2.  Now we can split this chart into three types of lines, horizontal, tilted towards right, tilted toward left.  
    ![Individual lines that make the triangle plot](https://img.chandoo.org/c/individual-lines-in-triangular-plot.png)
3.  For each of these lines we need to join certain points and when we combine these lines into a single _series_ we will get our desired chart. So let’s list down the points in each line.
    
    _Horizontal Lines (L1):_ Point 01, 02, 03, 04, 06, 05, 07, 08, 10, 09, 11.  
    _Right Lines (L2):_ Point 01, 11, 09, 12, 13, 07, 05, 14, 15, 03, 02  
    _Left Lines (L3):_ Point 02, 11, 10, 15, 14, 08, 06, 13, 12, 04, 01
    
4.  Now we need to setup a table where the coordinates of these points are listed in tabular order, like this:
    
    ![Data & calculations for triangle plot in Excel](https://img.chandoo.org/c/calculations-for-triangular-plot.png)  
    This can be done by using trigonometric ratio of sine and cosine, by representing each point in terms of _Polar Coordinates_ \[ These coordinates represent each point in terms of a distance “_R”_ and an angle represented by Greek alphabet _Theta_ (q), Line 01 makes an angle of 0° from X-Axis, Line 02 of 60° and Line 03 of 120° from +ive X- Axis, these details can be simply skipped if you don’t like math  😉 \]  
    Avoiding the details of trigonometry you can simply use following two formulas to get these values…
    
    For Value of X (Ordinate) you can use the following formula:  
    \=IF(O6=”H”,N6\*COS(RADIANS(Q6)),IF(O6=”L”,N6\*COS(RADIANS(Q6)),$D$5+N6\*COS(RADIANS(Q6))))
    
    For Y (Abscissa) you can use following:  
    \=IF(O6=”H”,N6\*SIN(RADIANS(Q6)),IF(O6=”L”,N6\*SIN(RADIANS(Q6)),N6\*SIN(RADIANS(Q6))))
    
5.  Once this Lookup Table is created we need to create another table where we list points in accordance to the _Lines_ that we have already created. We will [use VLOOKUP ()](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
     to fetch the corresponding coordinate through this formula and we will do this for all the three Lines. The VLOOKUP() simply looks for the point in the left most column of the first table and bring the corresponding values from the 3rd and 4th column to form the point in second table.
6.  When we are done with bringing the coordinates of all of these points we just need to plot a Scatter Chart. Now use a XY scatter chart to plot the data. You need to add only _one_ series, actually there are three types of lines but we can accommodate them in just _one_ series. When they overlap, they will give smaller triangles in result.

### Download Triangular Plot workbook

[**Click here to download the chart**](https://img.chandoo.org/d/triangular-plots.xls)
. Examine the formulas & chart series to understand how this is made.

**_Added by Chandoo_**

### Do you make such complex charts for your work?

I will be honest. I never had to make a triangle plot. But then, I never had to make _Ratatouille_ either. That doesn’t make me appreciate both of them any less. I think this chart shows fantastic technique. It also proves that Excel is highly flexible if you know which bolt to turn and which screw to tighten.

_**What about you?**_ Do you make such complex charts or visual analysis for your work? What is the most challenging chart you have worked on? _Please share using comments._

### Shape up your Chart skills – Charts + Shapes

If your job involves making charts in all shapes and sizes, then you are in luck. Check out these tutorials to learn how to bend Excel charting rules to get any shape you want:

*   [Simulating a pendulum movement using Excel charts](http://chandoo.org/wp/2011/07/06/3d-dancing-pendulums/)
    
*   [Wall hygrometric physics – modeling wall thickness in Excel chart](http://chandoo.org/wp/2013/04/18/wall-hygrometric-physic-chart/)
    
*   [Stars and lights using Excel Charts, VBA & animation](http://chandoo.org/wp/2012/11/13/happy-diwali-animated-chart/)
    
*   [Mustache shaped chart to measure your stash](http://chandoo.org/wp/2012/08/22/growing-a-money-mustache-using-excel/)
    
*   [Spoke chart](http://chandoo.org/wp/2011/04/13/how-to-make-a-5-star-chart/)
     | [5 star chart](http://chandoo.org/wp/2011/04/13/how-to-make-a-5-star-chart/)
    
*   [Making various country flags using Excel charts](http://chandoo.org/wp/2010/03/08/flag-project/)
    

### Thank you Faseeh

Many thanks to Faseeh for sharing this tutorial with all of us. I really enjoyed this and learned a few tricks from it.

_If you like this chart, say thanks to Faseeh using comments._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/creating-triangular-plots-using-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/creating-triangular-plots-using-excel/#respond)
    
*   Tagged under [Advanced Charting](https://chandoo.org/wp/tag/advanced-charting/)
    , [Cos()](https://chandoo.org/wp/tag/cos/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [Radians()](https://chandoo.org/wp/tag/radians/)
    , [scatter plot](https://chandoo.org/wp/tag/scatter-plot/)
    , [Sin()](https://chandoo.org/wp/tag/sin/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Posts by Faseeh](https://chandoo.org/wp/category/posts-by-faseeh/)
    

[PrevPreviousMaking a slick on/off switch using Excel & little bit of VBA \[case study\]](https://chandoo.org/wp/on-off-switch-in-excel-vba/)

[NextHow to find what is in the hidden cells? \[quick tip\]Next](https://chandoo.org/wp/how-to-find-what-is-in-the-hidden-cells-quick-tip/)

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
    
    [Reply](https://chandoo.org/wp/creating-triangular-plots-using-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/creating-triangular-plots-using-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/creating-triangular-plots-using-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ