# A Technique for Analysing Large Tables of Data

**Source:** https://chandoo.org/wp/analysing-large-tables

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

A Technique for Analysing Large Tables of Data
==============================================

*   Last updated on November 4, 2010

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Once you start using Excel to develop systems, budget, forecast and large tables of data you may come across the dilemma of “How do I know this is right” or “How do I truth check this”.

This post, Huis second, will add a tool to your arsenal to help you out.

The technique below allows for the rapid visual evaluation of 12 or more days/months/years of data via a chart of 2 variables and the ratio between them, utilising 2 sliders to rapidly change input variables.

### **DATA**

Typically all businesses deal in 3 types of numbers, ie: Dates or Times, Physicals and Dollars.

Dates may include Times, Days, Weeks, Months, Years or any periods in between

Physicals directly relate to the business you are in but may include inputs and or outputs: eg: metal, tyres and cars, sugar, flour and cakes or whatever your business makes, strangely Physicals may also include Dollars, if you’re in the financial services sector. People are a Physical.

And Dollars which could be revenue, costs, cashflows or profit types of numbers.

I have found one of the best methods of looking at large tables of data is to look at a key input or output physical and then interactively scroll through the cost or income and calculate a ratio between the two.

I am going to use as an example a budget which has 40 rows of data including Physicals and Costs. But you will see that the techniques here can easily be extended to hundreds of rows. You can download this file here: [Bobs Homes](https://chandoo.org/wp/wp-content/uploads/2010/11/Bobs-Homes.xlsx "Bobs Homes")

The technique below allows rapid visual evaluation of 12 or more months data a chart of 2 variables and the ratio between them.

Using 2 sliders the user can rapidly move between variables and evaluate the variance over a given time frame against another variable.

![](https://chandoo.org/wp/wp-content/uploads/2010/10/Main1.png "Main1")

The technique involves the charting of 3 ranges which in turn will be controlled by 2 sliders.

The first Range and slider will allow the selection of a Physical.

The second Range and slider will allow the selection of the Cost/Income component.

The third range will be the ratio of these, but specifically cost or income per physical.

I have attached a workbook, Bobs Homes, which contains 2 models, an example model for you to practice the following techniques on and a completed model which you can examine and pull apart to see how it works.

[Bobs Homes](https://chandoo.org/wp/wp-content/uploads/2010/10/Bobs-Homes.xlsx)

Load the model and scroll around and see what data is available. You will notice a time scale across the top with Physicals and Dollars down the left side. The Physicals and Dollars are grouped into common areas like inputs, outputs and costs, income and profit.

You will also note that there are 10 blank rows at the top of the worksheet. I do this so that I can perform simple calculations, charts or other workings without upsetting the data and other calculations below and for macro’s which automatically find the bottom of the data I know there is nothing below my data to upset the calculations.

Let’s jump in

### **SETUP**

We’re going to add the following components

#### Headings

![](https://chandoo.org/wp/wp-content/uploads/2010/10/Headings.png "Headings")

A2: Physical

A3: Cost/Revenue

A4: Ratio

E1: =E12

and copy across to Q1

#### Data

[![](https://chandoo.org/wp/wp-content/uploads/2010/11/Data.png "Data")](https://chandoo.org/wp/wp-content/uploads/2010/11/Data.png)

C2: 1

C3: 1

D2: =CONCATENATE(OFFSET(B$13,$C$2,0),OFFSET(C$13,$C$2,0))

D3: =CONCATENATE(OFFSET(B$22,$C$3,0),OFFSET(C$22,$C$3,0))

D4: =CONCATENATE(D3,”/”,D2)

E2: =OFFSET(E$13,$C$2,0)

E3: =OFFSET(E$22,$C$3,0)/1000

Copy E2:E4 across to Q2:Q4

#### Chart

Select Area D1:Q4

Insert Chart, Line Chart with or without markers to your liking

Suggestion – Place the Chart between the Data and the new Headings and formulas you have just added

Adjust the Legend to be at the Bottom of the chart

#### Sliders

Insert 2 Sliders

Developer Tab, Insert Scroll Bar (Form Control)

If you don’t have the Developer Tab, Have a read of: [http://chandoo.org/wp/2009/05/26/excel-2007-productivity-tips/](https://chandoo.org/wp/2009/05/26/excel-2007-productivity-tips/ "Developer Tab")

Position the scroll bars so they are vertically next to the Chart, Use Alt whilst dragging to snap to Cell corners or edges

Link the sliders to the lookup cells

![](https://chandoo.org/wp/wp-content/uploads/2010/10/Sliders.png "Sliders")

**Slider 1**  
Current value: 1  
Minimum: 1  
Maximum: 7 (This is the number of Rows of Physicals data)  
Incremental Change: 1  
Page Change: 0  
Cell Link: $C$2  

**Slider 2**  
Current value: 1  
Minimum: 1  
Maximum: 19  (This is the number of Rows of Cost/Revenue data)  
Incremental Change: 1  
Page Change: 0 (set this to maybe 10 if you have more than 30/40 rows)  
Cell Link: $C$3

### ********FINAL MODEL********

You can now select a Physical by dragging the Left Scroll bar

You can now select a Revenue/Cost by dragging the Right Scroll bar

The Ratio of Cost/Revenue to the Physical is calculated and the 3 are all charted

Examine the model and see what variances in inputs/outputs can be seen.

![](https://chandoo.org/wp/wp-content/uploads/2010/10/Final.png "Final")

### **HOW DOES THIS WORK?**

The Formula in E2:Q3, are extracting the physicals and Cost/revenue data from the main body of the report by simply using an **Offset** function from the top of the Physicals and Cost/Revenue area.

The Distance they offset is retrieved from the control Cells C2:C3

The labels for the Physicals and Costs/Revenues are also retrieved using 2 Offsets inside a **Concatenate**. This is done to allow Heading Rows and Sub Headings to be displayed and joined if available from 2 separate columns.

The Chart is a simple Line Chart which is charting the 3 Data Rows (E2:Q4) against the Time Period (E1:Q1) at the top of the work area.

You can customise the chart to your content.

The 2 sliders control the control Cells C2:C3, and allow for interactive selection of Physicals and costs.

In use often you will find that one of the Physicals, Costs/Revenue or Ratio is generally much smaller in scale than the other 2 measures. Generally it is a good idea to plot the odd scale against a secondary Y axis.

Select the series line, Right Click and select Format Data Series

### FUNCTIONS USED:

Offset: [http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/ "Offset")

Concatenate: [http://chandoo.org/excel-formulas/concatenate.html](http://chandoo.org/excel-formulas/concatenate.html "Concatenate")

**How do you truth check your data? Let us all know in the comments below:**

**How are you finding the content level of my posts? Let me know in the comments below:**

### Next Thursday – Selecting Individual Data Points in Charts and More Sliders

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [24 Comments](https://chandoo.org/wp/analysing-large-tables/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/analysing-large-tables/#respond)
    
*   Tagged under [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [concatenate()](https://chandoo.org/wp/tag/concatenate/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [Slider](https://chandoo.org/wp/tag/slider/)
    , [tables](https://chandoo.org/wp/tag/tables/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousExcel Hero Academy – Recommended Online Excel Training Program](https://chandoo.org/wp/excel-hero-academy-review/)

[Next3 Lookup Formula Challenges + 2 Jokes + 1 Link \[VLOOKUP Week\]Next](https://chandoo.org/wp/lookup-formula-challenges/)

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
    
    [Reply](https://chandoo.org/wp/analysing-large-tables/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/analysing-large-tables/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/analysing-large-tables/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ