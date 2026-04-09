# Macros for Automatically Implementing Modeling Best Practices » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/macros-for-best-practice-modeling

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Macros for Automatically Implementing Modeling Best Practices
=============================================================

*   Last updated on November 30, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This article is written by _**Myles Arnott**_ from [Excel Audit](http://www.excelaudit.co.uk/)

In the [first part on our Modeling Best Practices series](http://chandoo.org/wp/2012/08/29/best-practice-modeling-5tips/)
, we learned 5 best practices to follow. This article shows how to automatically implement the best practices using macros.

![Best Practice Modeling using Excel - Make these 5 changes to your Excel models today](https://img.chandoo.org/fm/best-practice-modeling-using-excel.png "Best Practice Modeling using Excel - Make these 5 changes to your Excel models today")

### Quick Re-cap on Modeling Best Practices

**Make cell content and cell purpose visually identifiable at all times**

In the first article I highlighted the fact that the content and purpose of every cell should be easily identifiable to the user at all times.

At a basic level we can identify two basic cell types:

|     |     |     |     |
| --- | --- | --- | --- |
| **Type** | **Background** | **Font** | **Protection** |
| Assumption or constant | White | Blue | No  |
| Output | Grey | Black | Yes |

### Best Practice formatting made easy

In order to make the application of Best Practice formatting quicker and easier I have created three simple macros. These macros use Excel’s [Go To Special function](http://chandoo.org/wp/2012/03/12/go-to-special/)
 and then some simple formatting to the active sheet.

### Demo of the macros

Please watch this 5 minute demo to understand how the macros work.

\[[Click here to watch the video](http://chandoo.org/wp/2012/11/29/macros-for-best-practice-modeling/)\
\]

### Overview of best practice macros

**Auto\_Format:**  automatically formats cells depending on their type:

*   Number constants (i.e. input cells) are white background, blue font & unprotected
*   Non number constants (e.g. formulae) are grey background, black text & protected

**Constants\_Format:**  formats selected cells as white background, blue text & unprotected

**Formula\_Format:** formats selected cells as grey background, black text & protected

#### And a couple of extras:

**Simple\_Audit:**  A Simple Audit Macro that uses the go to special function to select and highlight specific cell types. This is the macro from the [Managing Spreadsheet Risk article](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/)
.

**Clear\_format:** formats all cells as white background, black text & protected

**A word of warning: These macros apply formatting to your spreadsheets. This formatting cannot be undone.**

### File to download

Since formatting steps vary for Excel 2003 & 2007, we have 2 versions of the files. Please download the appropriate file below:

[Excel 2007 and above version](https://img.chandoo.org/fm/Best%20Practice%20Modelling%20Part%202%20file.xls)

[Excel 2003 & below version](https://img.chandoo.org/fm/Best%20Practice%20Modelling%20Part%202%20file%20%28pre2007%29.xls)

These files have the macros embedded in them. You will need to move these macros into your personal workbook. [Help on this.](http://chandoo.org/forums/topic/how-can-i-reuse-macros)

Once in your personal workbook you can then [add these to your QAT](http://chandoo.org/wp/2010/06/08/add-macros-to-excel-toolbars/)
, [or Ribbon](http://chandoo.org/wp/2012/02/27/how-to-add-your-own-macros-to-excel-ribbon/)
.

### Conclusion

Have a play with the macros on the example workbook and then, once you are happy with how to use them, you can start applying best practice formatting at the click of a button.

Let us know how you are implementing these best practices and your suggestions using comments.

### Thanks to Myles

Many thanks to Myles for compiling all the tips & sharing this with us. If you have enjoyed this article, please say thanks to Myles. You can also reach him at [Excel Audit](http://www.excelaudit.co.uk/)
 or [his linkedin profile](http://uk.linkedin.com/in/clarityconsultancyservicesma)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/macros-for-best-practice-modeling/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/macros-for-best-practice-modeling/#respond)
    
*   Tagged under [cell styles](https://chandoo.org/wp/tag/cell-styles/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [myles arnott](https://chandoo.org/wp/tag/myles-arnott/)
    , [risk management](https://chandoo.org/wp/tag/risk-management/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExtract data using Advanced Filter and VBA](https://chandoo.org/wp/extract-subset-of-data/)

[NextChandoo.org Holiday SALE, Starts on Monday – 3rd December!Next](https://chandoo.org/wp/holiday-sale-dates/)

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
    
    [Reply](https://chandoo.org/wp/macros-for-best-practice-modeling/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/macros-for-best-practice-modeling/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/macros-for-best-practice-modeling/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ