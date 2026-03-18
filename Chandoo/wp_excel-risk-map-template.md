# Free Excel Risk Map Template » Project Management » Chandoo.org

**Source:** https://chandoo.org/wp/excel-risk-map-template

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    

Free Excel Risk Map Template
============================

*   Last updated on August 28, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

> Risk comes from not knowing what you are doing.
> 
> Warren Buffet

If you ever ask a project manager what they are up to, they will tell you “_I have no idea_“. So risks are quite common in project management. That is why I made this awesome **free Excel risk map template** to keep track and visualize risks.

![Risk map template for Excel - demo](https://chandoo.org/wp/wp-content/uploads/2019/08/excel-risk-map-template.png)

Download Risk Map Template
--------------------------

If you just want risk map template, **[click here to download it](https://chandoo.org/wp/wp-content/uploads/2019/08/risk-map.xlsx)
**.

For more templates on **[Project Management, click here](https://chandoo.org/pmt/pmt-index-1.html)
**.

### Create your own Risk Tracker & Risk Map in Excel – Tutorial

If you want to make something similar for your work situation, then follow this tutorial.

**1\. Set up your risk register**. For this you could use Excel Tables. Just add necessary columns – Risk ID, description, impact, likelihood and any other columns you want. Here is a sample risk register. Imagine, this table is named _**risks**_

![Example risk register - Excel Template](https://chandoo.org/wp/wp-content/uploads/2019/08/risk-register-excel-table.png)

**2\. Make a 5×5 empty grid and color it.** In a separate Excel tab, create 5×5 (or 4×4 etc.) grid and color it as per risk color coding you follow. _Make sure_ you add the Impact & Likelihood scale. This is how it would look.

![blank risk map grid](https://chandoo.org/wp/wp-content/uploads/2019/08/blank-risk-map-grid.png)

**3\. Write formulas to print matching risks.** We can use TEXTJOIN() formula to get all the risks that have a given impact and likelihood value.

Note: TEXTJOIN() is available only in Excel 2019 & 365.

If you do not have TEXTJOIN(), please use the [**_VBA Excel Risk Map Generator_**](https://chandoo.org/wp/excel-risk-map/)
.

For example, the formula in D2 cell (Likelihood=5, Impact=1) would be,

\="• " & TEXTJOIN(CHAR(10)&"• ",TRUE,
IF(risks\[Likelihood\]=**$C2**,IF(risks\[Impact\]=**D$7**,risks\[Title\],""),""))

_This is an array formula, so press CTRL+Shift+Enter to get the result._

**How does this formula work?**

*   We use two nested IF conditions to check if risks\[Likelihood\] and risks\[Impact\] matches $C2 and D$7 respectively.
*   If they both match, we get risks\[Title\], else blank space “”
*   We then pass this resulting array to TEXTJOIN() which combines all the matching risks with the CHAR(10)**bullet**_space_.
*   We add an extra **bullet**_space_ at start for the first risk (as TEXTJOIN will only print bullet symbol between risks, but not at front)
*   **CHAR(10) is the newline symbol.** So when you word wrap the cell, Excel prints each risk in a new line.

**What about cells with no risks?** Would they not print a bullet point?

You are right my dear. We can use conditional formatting to suppress such cells. We can set the cell format code ;;; to those cells.

_Related: [Make cell value disappear with custom format codes](https://chandoo.org/wp/cp031-excel-invisibility/)
_

How to make this template – Video
---------------------------------

Please watch this video tutorial to learn how the template is constructed. You can use the ideas to make something similar for your work easily.

Download Risk Map Template
--------------------------

*   [FREE Risk Map Template](https://chandoo.org/wp/wp-content/uploads/2019/08/risk-map.xlsx)
     – works in Excel 365, 2019 with TEXTJOIN
*   [Excel Risk Map Generator](https://chandoo.org/wp/excel-risk-map/)
     – uses VBA, works in most versions of Excel
*   [Project Management Templates](https://chandoo.org/pmt/pmt-index-1.html)
     – 24 templates to help you manage projects better.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [24 Comments](https://chandoo.org/wp/excel-risk-map-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-risk-map-template/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [project management templates](https://chandoo.org/wp/tag/project-management-templates/)
    , [risk management](https://chandoo.org/wp/tag/risk-management/)
    , [risk map](https://chandoo.org/wp/tag/risk-map/)
    , [Textjoin()](https://chandoo.org/wp/tag/textjoin/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    

[PrevPreviousHow to extract common values in two tables? – Power Query Tip](https://chandoo.org/wp/compare-two-tables/)

[NextJob Title Matching Problem \[Excel Homework\]Next](https://chandoo.org/wp/job-title-matching-problem/)

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
    
    [Reply](https://chandoo.org/wp/excel-risk-map-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-risk-map-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-risk-map-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ