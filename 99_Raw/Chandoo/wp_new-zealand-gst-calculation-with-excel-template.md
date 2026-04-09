# New Zealand GST Calculation with Excel [Free Template] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

New Zealand GST Calculation with Excel \[Free Template\]
========================================================

*   Last updated on July 2, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

If you operate a business in New Zealand (NZ) like me, chances are you too need to calculate GST on purchases & sales. Today, let me share the excel formulas needed to calculate GST as per NZ laws. I have also attached a free GST calculator template to help you if you are in a hurry.

How to calculate NZ GST using Excel?
------------------------------------

Assuming you have the sale price in cell C5, the GST is calculated by the below formula.

    =C5 * 0.15

We multiply the “sale” or “service” price by 0.15 (or 15%) as the official GST rate in New Zealand is 15% \[[ref](https://www.ird.govt.nz/gst/what-gst-is)\
\].

![NZ GST Calculation - Excel formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)

Excel formula for NZ GST from “total” price
-------------------------------------------

Let’s say you want to figure out the GST from total price (GST inclusive price) of something. This is quite common in retail scenarios. You have an item for $140 on the shelves, but you need to figure out what the GST should be on this. In this case, you can use the below Excel formula.

Assuming your “total” price is in cell C15, the GST is calculated with this formula:

    =C15 * 15/115

![GST from total price - Excel formula](https://chandoo.org/wp/wp-content/uploads/2025/07/SNAG-0166.png)

GST Reverse Calculation – What is the “sale price” if I know GST?
-----------------------------------------------------------------

Occasionally, we may have the reverse problem. We know how much the GST is, but just need to figure out the total. In this case, you can use the below formula.

Assuming your GST is in cell I5, the sale price can be calculated with below Excel formula

    =I5*100/15

![Reverse GST calculation - sale price from GST](https://chandoo.org/wp/wp-content/uploads/2025/07/SNAG-0167.png)

and total price can be calculated with this formula

    =I5*115/15

The 3 / 23rds and 3/20ths rules
-------------------------------

Here is a handy shortcut to quickly figure out the GST from total or sale prices.

### 3/23rds rule – GST from total

If your total amount is known, just multiply that with 3 and divide by 23 to get the GST.

For example, if your total is $230, then GST would be $30.

    =230 x 3 / 23
    =690 / 23
    =30

### 3/20ths rule – GST from Sale Price

If you know the “sale” price, just multiply it with 3 and divide by 20 get the GST.

For example, if your sale price is $140, then GST would be $21

    =140 x 3 / 20
    =420 / 20
    =21

GST for hourly rates, services
------------------------------

If you work as a plumber / electrician / some other type of service provider and you charge by hour, then you can use below formulas for calculating GST.

Assuming your hourly rate is in cell I15 and hours worked in cell I16, the GST formula looks like this:

    =I15*I16*0.15

![GST on hourly services - excel formula](https://chandoo.org/wp/wp-content/uploads/2025/07/SNAG-0168.png)

FREE NZ GST calculator workbook
-------------------------------

[![free NZ GST Calculator Excel Template\
](https://chandoo.org/wp/wp-content/uploads/2025/07/SNAG-0169.png)](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculator.xlsx)

I have created a simple, plug-n-play GST calculator workbook for you. Please download it here, enter your price / total / hourly information and the file automatically calculates the GST for you. It also has the GST formulas / patterns that you can apply to your own data.

**[Click here to download the NZ GST Calculator.](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculator.xlsx)
**

* * *

Need Spreadsheet help?
----------------------

If you are an NZ business and need spreadsheet help or automation services, please get in touch with me. I am a Wellington based Excel / automation expert and I have been helping clients for the past 15 years in creating simple & easy automation and Excel solutions. Please email me on hello@chandoo.org to discuss more.

Other Excel Templates to help you
---------------------------------

*   [Free 2025 Calendar & To-do list template](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2025/)
    
*   [Free Project Tracker Template](https://chandoo.org/wp/drill-down-gantt-chart-template/)
    
*   [Free Household budget template](https://chandoo.org/wp/budget-spreadsheet-download/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel](https://chandoo.org/wp/tag/excel-2/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

[PrevPreviousMake a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[NextWho is my boss’s boss? \[Data Analytics Challenge – 001\]Next](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

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
    
    [Reply](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ