# Mod() function in excel to Implement Escalation Frequency [Financial Modeling Tutorials] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Mod() function in excel to Implement Escalation Frequency \[Financial Modeling Tutorials\]
==========================================================================================

*   Last updated on July 28, 2011

![Picture of paramdeep@gmail.com](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=300&d=mm&r=g)

#### paramdeep@gmail.com

Share

Facebook

Twitter

LinkedIn

### ![](https://chandoo.org/wp/wp-content/uploads/2011/04/EscalationFrequency.gif "EscalationFrequency")

You take an apartment on rent at $1000 per month and the owner puts an escalation clause saying 10% increment each 3 years. How do you model this in excel? In this tutorial we understand how escalations at certain frequency can be implemented using the mod function in excel.

### What is the mod() function

Simply speaking, mod function calculates the remainder in division. For example,

[![clip_image001](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image001_thumb.jpg "clip_image001")](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image001.jpg)

The function is simple, it calculates the remainder, but it can achieve some very complex tasks.

### So what would we like to do?

We want to create a model, where the user can change the escalation freq. For example, if you are able to negotiate for an escalation every 4 years, the model should be flexible enough to incorporate that.

[![clip_image003](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image003_thumb.jpg "clip_image003")](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image003.jpg)

### How do we implement this?

First of all we create a flag to find, if it is an escalation year or not. Here we use the mod() function. For example, if it is a 3 year escalation clause, then we want to take the year number mod 3. If the remainder is non zero, it implies an escalation year (I know it can be confusing… So my suggestion – Play with the mod() function).

[![clip_image005](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image005_thumb.jpg "clip_image005")](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image005.jpg)

Once the escalation is figured out, we can sum-up the escalations and find the total escalations till a particular year.

[![clip_image007](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image007_thumb.jpg "clip_image007")](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image007.jpg)

Then we can simply take the base figures, and implement the number of escalations till that point of time.

[![clip_image009](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image009_thumb.jpg "clip_image009")](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image009.jpg)

### Few more places, where you can use mod function

I have no doubt in my mind that Mod is a powerful (and confusing) function. Confusion arises because of the non-linear nature of the function (It sometimes gives increasing results and sometimes decreasing results!).

If you are planning to implement anything that has cyclicality for example, you want to color every 5th row of your excel, or you want to select every 4th day of a week, or anything of that nature, mod() function can be a very handy function!

### How do you implement cyclicality in your models?

I know the easiest way to do that is to copy paste values in your model and update that manually. It is easy to understand but at the same time is not flexible. So how do you implement such functionality in your models?

### Templates to download

I have created a template for you, where the subheadings are given and you have to link the model to get the cash numbers! You can download the same from [here](https://chandoo.org/wp/wp-content/uploads/2011/04/Par-Escalation-Freq.zip "Empty Template")
**.** You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download [this filled template](https://chandoo.org/wp/wp-content/uploads/2011/05/Ins-Escalation-Freq.zip)
 and check, if the information you recorded, matches mine or not!    
[![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine")
  
For any queries regarding the cash impact or financial modeling, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

### More Resources on Excel Financial Modeling

Financial Modeling is one of the frequent uses of Excel. Please go thru below articles to learn more,

*   [Financial Modeling using Excel](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/ "Introduction to Financial Modeling using Excel [Part 1 of 6]")
     – 6 part tutorial
*   [Introduction to Project Finance using Excel](http://chandoo.org/wp/2011/02/08/introduction-to-project-finance-modeling-in-excel/ "Introduction to Project Finance Modeling in Excel")
    
*   [Modeling Interest during Construction in Excel](http://chandoo.org/wp/2011/02/16/modeling-interest-during-construction/)
    
*   [Displaying and Selecting Scenarios using VBA](http://chandoo.org/wp/2010/09/24/displaying-selecting-a-scenario-using-vba-modeling-in-excel/)
    

### Join our Financial Modeling Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**  
[![clip_image010](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image010_thumb.gif "clip_image010")](https://chandoo.org/wp/wp-content/uploads/2011/04/clip_image010.gif)

This article is written by [Pristine](http://edupristine.com/)
. The author can be contacted on [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)
.  
_Pristine is an awesome training institute for CFA, PRIMA, GARP etc. They have trained folks at HSBC, BoA etc. Chandoo.org is partnering with Pristine to bring an [excel financial modeling online training program](http://chandoo.org/wp/financial-modeling/)
 for you._

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [17 Comments](https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [finance](https://chandoo.org/wp/tag/finance/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [Financial Modeling School](https://chandoo.org/wp/tag/financial-modeling-school/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [pristine](https://chandoo.org/wp/tag/pristine/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousUse Copy & Paste to Preserve References to Tables \[Quick Tip\]](https://chandoo.org/wp/preserve-table-references-while-copying-formulas/)

[NextAdvanced Sumproduct QueriesNext](https://chandoo.org/wp/advanced-sumproduct-queries/)

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
    
    [Reply](https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/mod-function-in-excel-to-implement-escalation-frequency-financial-modeling-tutorials/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ