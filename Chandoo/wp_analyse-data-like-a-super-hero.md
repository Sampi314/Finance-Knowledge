# Data Analysis using Linest and the Data Table function.

**Source:** https://chandoo.org/wp/analyse-data-like-a-super-hero

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Analyse Data like a Super Hero
==============================

*   Last updated on June 23, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In mid May, Anup47 asked a question in the [Chandoo.org forums](http://chandoo.org/forums/ "Chandoo.org Forums")
 about the use of a VBA macro to run a number of iterations of a variable against two sets of X values, you can see the post [here](http://chandoo.org/forums/topic/multivariate-regression-analysis-vba "Multivariate Regression Analysis VBA")
. It turns out that the number of iterations was 500 columns of data with each column having 27 values.

On examination of the problem, it was going to be a straight forward matter of setting up a statistical function Linest and then using the Data Table command to run each set of data through the function.

The Linest will take the input data and return the statistics that Anup wanted.

The Data Table function will feed in the source data and tabulate the Input and Output data.

This Post follows through a worked example which you can follow along, download the Sample file to suit [Sample File 97/2003](https://chandoo.org/wp/wp-content/uploads/2011/06/DASH-97-03.xls "Sample File 97/03")
 or [Sample File 2007/10](https://chandoo.org/wp/wp-content/uploads/2011/06/DASH-07-10.xlsx "Sample File 07/10")
 version. The Sample File contains a worked example of the completed model as well as a Practice Page of the original data. Download the Excel 95/2003 or 2007/10 version above.

Please note that the sample file only contains 14 sets of data as opposed to the 500 Anup47 wanted to process.

**Setup**
---------

There are a few things that needed setting up before the work starts.

*   Headers
*   Linest Area
*   Link Area
*   Data Table Area

Once these areas are setup we simply use the Excel Data Table function.

Once the Data Table function has run, the results can be processed or analysed as required.

**Headers**
-----------

The original data was just that, a tabulation of raw data. The two X sets of Data were in Columns 1 & 2. Each Column from D onwards has a set of Y data that was to be processed.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup1.png "Anup1")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup1.png)

The first thing that was required was some Headers for the Input Data.

This isn’t strictly required but it is good practice and makes it easier to tabulate and analyse results later.

Insert a Row above the first line

Put **X1**, **X2** in A1, B1 and **Y1** in D1 and then drag the lower right Black Handle across top to the right and Excel will autofill the remaining cells.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup2.png "Anup2")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup2.png)

**Linest Area**
---------------

To get the statistics which Anup wanted we will use the Excel Linest function.

Linest is a Statistical Function that takes a set of data and compares it, in this case to two sets of X Values and produces a set of statistical measure relevant to the correlation between the data sets.

This post isn’t going to explain the intricacies of Linest and I refer you to the Links section at the end where you can read more about the Linest function at your leisure.

For our purposes we need to know that Linest is an Array Formula and requires a 5 Row x 5 Column area to be entered into. For now we will just Array Enter the function =Linest($D$2:$D$28,A2:B28,True,  True) into B32:F36.

To do that select the range B32:F36, Press F2 and type/paste the equation in, then Array Enter with **Ctrl Shift Enter**.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup3.png "Anup3")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup3.png)

**Link Area**
-------------

To Link the Linest equation to a Data Table we need a link cell, which we will put just above the Linest area.

For now just enter a 1 in it.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup4.png "Anup4")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup4.png)

We can now go back to the Linest area and link the Linest equation to our link area using the equation, =LINEST(OFFSET($C$2:$C$28,,$B$30),A2:B28,TRUE,  TRUE)

To do that select the range B32:F36, Press F2 and type/paste the equation in, then Array Enter with **Ctrl Shift Enter**.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup5.png "Anup5")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup5.png)

What this does is allow the Linest formula to access different columns Y1 to Y500 depending on the value of the Link cell B30 which is now 1.

**Data Table Area**
-------------------

To setup a Data Table area we need a column of Inputs which will be the Run Numbers and the Row Inputs will be links to the Input and Output Cells.

In a range J33:J46 put the values 1 to 14. These will be the Run Numbers. ie Run No 1, Run No 2 etc (Green in the example below).

Across the top of the Data Table area we can put a number of links and associated labels (Yellow and Blue)

In this case there are 4 Output links =B31, =C31, =B34 and =B33 and their associated labels above them, as well as 2 Input equations and there Labels. The Input equations are simple Offset function that retrieves a value from Rows 1 or 2 based on the value of the Link Cell B30.

These are technically not required but make data analysis and identification of individual results later on a lot simpler.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup6.png "Anup6")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup6.png)

**Run Data Table**
------------------

We can now run the data Table by selecting the Data Table area: J32:P46

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup7.png "Anup7")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup7.png)

Noting that we will be using a Column Input cell and that it will link to $B$30, the Link cell for the Linest command.

What this does is takes the first value from the Column J32:J46 and puts it into B30, then the Linest command will be calculated and the results put into the Data Table area along with the Inputs.

This is repeated for each cell in J32:J46 automatically.

The final Data Table is now populated as below:

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup8b.png "Anup8b")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup8b.png)

You can see by extending the Data Table input column from 14 to 500 that the full 500 columns of Input Data could easily be processed.

**Results**
-----------

You now have a set-off data that can be analyzed using normal statistics, Min, Max, Std Deviation etc, or can be fed into a Pivot Table/Chart for analysis etc.

[![](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup8.png "Anup8")](https://chandoo.org/wp/wp-content/uploads/2011/06/Anup8.png)
  

**References**
--------------

### Linest References

[http://chandoo.org/wp/2011/01/26/trendlines-and-forecasting-in-excel-part-2/](http://chandoo.org/wp/2011/01/26/trendlines-and-forecasting-in-excel-part-2/)

[http://newtonexcelbach.wordpress.com/2011/01/19/using-linest-for-non-linear-curve-fitting/](http://newtonexcelbach.wordpress.com/2011/01/19/using-linest-for-non-linear-curve-fitting/)

### Data Table References

[http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)

**How can the Data Table command help you become a data processing super hero?**
--------------------------------------------------------------------------------

How can the Data Table command help you become a data processing super hero?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [8 Comments](https://chandoo.org/wp/analyse-data-like-a-super-hero/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/analyse-data-like-a-super-hero/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [Data Table](https://chandoo.org/wp/tag/data-table/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Linest](https://chandoo.org/wp/tag/linest/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousRegister for our Excel & Financial Modeling Bootcamp in Singapore \[Details inside\]](https://chandoo.org/wp/singapore-workshop-details/)

[NextWe Want Your IdeasNext](https://chandoo.org/wp/we-want-your-ideas/)

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
    
    [Reply](https://chandoo.org/wp/analyse-data-like-a-super-hero/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/analyse-data-like-a-super-hero/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/analyse-data-like-a-super-hero/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ