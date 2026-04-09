# Calculating Accumuldated Depreciation using Mixed References in Excel [Financial Modeling in Excel]

**Source:** https://chandoo.org/wp/accumulated-depreciation-using-mixed-references

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    

Accumulated Depreciation using Mixed References
===============================================

*   Last updated on July 28, 2011

![Picture of paramdeep@gmail.com](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=300&d=mm&r=g)

#### paramdeep@gmail.com

Share

Facebook

Twitter

LinkedIn

Last time we had discussed the [use of SumProduct()](http://chandoo.org/wp/2011/07/12/sumproduct-function-to-consolidate-revenues/)
 to ease your life for calculation of consolidated revenues and depreciation. This time we would be using the sum function! Yes you heard it right – The Sum function.

But we would use the Sum function with a small trick! We would use it to calculate running cumulative sum! And believe me, you would need this function so many times – to calculate accumulated depreciation, cumulative debt, Profits to Retained Earnings and almost all the accounts that would consolidate into the balance sheet.

### Using Sum function to calculate cumulative values

Most of the accounts in the Balance sheet are cumulative accounts (For example, cumulative debt, accumulated depreciation, etc.). In models, we need to have these as running numbers

[![image](https://chandoo.org/wp/wp-content/uploads/2011/07/image_thumb3.png "image")](https://chandoo.org/wp/wp-content/uploads/2011/07/image3.png)

You would encounter this problem of calculating running cumulative values often and Sum formula (Used with slight intelligence) does come in very handy for the purpose.

### Using Sum() function for calculating running cumulative values

Sum function uses an array as an input. If used intelligently – starting element of the array with fixed reference and the second part of the array as moving, it can help you get a running cumulative value. \[read more: [Relative & Absolute References in Excel Formulas](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)\
\]

[![image](https://chandoo.org/wp/wp-content/uploads/2011/07/image_thumb4.png "image")](https://chandoo.org/wp/wp-content/uploads/2011/07/image4.png)

The basic trick is very simple. In the first cell in the sum function, I fix the first array argument using “$” and sum till the same cell.

[![image](https://chandoo.org/wp/wp-content/uploads/2011/07/image_thumb5.png "image")](https://chandoo.org/wp/wp-content/uploads/2011/07/image5.png)

Now when I copy this function to the right, the first reference remains constant, whereas the second one keeps moving (as it is relative). This results in a growing array and hence a cumulative sum for accumulated depreciation.

[![image](https://chandoo.org/wp/wp-content/uploads/2011/07/image_thumb6.png "image")](https://chandoo.org/wp/wp-content/uploads/2011/07/image6.png)

### Where else can this function be useful in Finance?

As I had pointed our earlier, most of the balance sheet numbers are accumulated numbers (Balance sheet is like a bucket, which accumulates values) and hence you can find the application of this running sum in almost all such accounts. I have used it (Can’t remember how many times!!) for converting Profits to Retained Earnings (when there are no dividends paid out), Debt Raised to accumulated debt (when there are no repayments), Debt for Interest During Construction, etc.

### How do you accumulate numbers?

There are obviously multiple ways of doing the same thing in excel. I have shown you one way to get accumulated values. Conceptually accumulation is very simple – New Accumulated value = Old Accumulated Value + New Value. You can use this concept (maybe I will demonstrate in my next tutorial) to get the accumulation.

How do you accumulate numbers in excel. I would encourage you to share your experience!

### Templates to download

I have created a template for you, where the subheadings are given and you have use the functions to get the right values for you! You can [download the same from here](https://chandoo.org/wp/wp-content/uploads/2011/07/Par-Accumulated-Depreciation.xlsx)
**.** You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download this filled template and check, if the information you recorded, [matches mine or not](https://chandoo.org/wp/wp-content/uploads/2011/07/Ins-Accumulated-Depreciation.xlsx)
!

### Join our Financial Modeling Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**

The article is written by Paramdeep from [Pristine](http://edupristine.com/)
.

_Chandoo.org has partnered with Pristine to launch a Financial Modeling Course. [**For details click here**](http://chandoo.org/wp/financial-modeling/ "Financial Modeling Online Training Program - Chandoo.org")
.  
_

[![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/accumulated-depreciation-using-mixed-references/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/accumulated-depreciation-using-mixed-references/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel 2007](https://chandoo.org/wp/tag/excel-2007/)
    , [finance](https://chandoo.org/wp/tag/finance/)
    , [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [references](https://chandoo.org/wp/tag/references/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    

[PrevPreviousDetails about our Financial Modeling Class](https://chandoo.org/wp/financial-modeling-class-details/)

[NextInteractive Dashboard in Excel using HyperlinksNext](https://chandoo.org/wp/interactive-dashboard-using-hyperlinks/)

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
    
    [Reply](https://chandoo.org/wp/accumulated-depreciation-using-mixed-references/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/accumulated-depreciation-using-mixed-references/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/accumulated-depreciation-using-mixed-references/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ