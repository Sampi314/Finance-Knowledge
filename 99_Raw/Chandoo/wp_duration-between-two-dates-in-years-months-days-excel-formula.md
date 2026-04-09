# How to calculate time between two dates in Years, Months & Days [Excel Formula] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to calculate time between two dates in Years, Months & Days \[Excel Formula\]
=================================================================================

*   Last updated on January 29, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![time between two dates excel formula](https://chandoo.org/wp/wp-content/uploads/2024/01/time-between-two-dates-excel-formula.png)

Let’s say you have two dates in the cells D4 & D5 as above. You want to find out the duration in years, months & days between both. We can use the good-old DATEDIF formula for this.

				
					`'Years: =DATEDIF($D$4,$D$5,"y") 'Months: =DATEDIF($D$4,$D$5,"ym") 'Days: =DATEDIF($D$4,$D$5,"md")  'All in one formula:  =DATEDIF($D$4,$D$5,"y")&" years "&DATEDIF($D$4,$D$5,"ym")&" months "&DATEDIF($D$4,$D$5,"md")&" days"`
				
			

Using LAMBDAs to create a custom function for this
--------------------------------------------------

We can use [Excel’s LAMBDA functions](https://chandoo.org/wp/what-is-lambda-function/)
 to create a custom duration function to get the duration in years, months & days from any two dates.

_**This feature is available with Excel 365.**_ 

Here is one such formula.

				
					`=LAMBDA(start,end, LET(y, DATEDIF(start,end,"y"), m,  DATEDIF(start,end,"ym"), d,  DATEDIF(start,end,"md"), y &" years "&m&" months "&d&" days"))`

				
			

### Setting up this LAMBDA getDuration() Function in your Excel

![](https://chandoo.org/wp/wp-content/uploads/2024/01/getDuration-LAMBDA-in-Excel.png)

To use this LAMBDA function in your Excel, 

1.  Go to Formula Ribbon > Name Manager
2.  Click on New Name
3.  Type the name as **getDuration**
4.  Type Refers to as the above LAMBDA function
5.  Click OK

  
Now, you will have a getDuration() function in your Excel!

To use it, just type=getDuration(start,end) in any cell.

Calculating Other Types of Durations in Excel
---------------------------------------------

Refer to below formulas to calculate other kinds of duration in Excel. All of these formulas assume you have start & end dates in cells D4 & D5.

### Duration in DAYS

				
					`=D5-D4`

				
			

### Duration in WORKING DAYS (Monday to Friday)

				
					`=NETWORKDAYS(D4,D5)`
				
			

### Duration in WORKING DAYS (Custom Weekend)

If you have a custom weekend type (for example, Friday, Saturday weekend), you can use the NETWORKDAYS.INTL function like this to calculate the duration in working days.

Both of these functions (NETWORKDAYS, NETWORKDAYS.INTL) also accept an optional list of holidays (such as Christmas, New Years day etc.) to handle arbitrary holidays.

![](https://chandoo.org/wp/wp-content/uploads/2024/01/networkdays-formula-to-calculate-duration-in-working-days.png)

				
					`=NETWORKDAYS.INTL(D4,D5, 4)  'calculates working days between D4 & D5 with Tuesday, Wednesday weekend policy!`
				
			

### Number of Months

				
					`=DATEDIF(D4, D5, "m")`
				
			

### Duration in Years

				
					`=(D5-d4)/365.25 'calculates the duration in years with leap year logic.`
				
			

Try these formulas yourself
---------------------------

[**Click here to download the SAMPLE FILE**](https://chandoo.org/wp/wp-content/uploads/2024/01/how-to-calculate-duration-in-excel.xlsx)
 with all these duration calculations. 

To use the LAMBDA function, you need Excel 365. 

More on Duration Calculation in Excel
-------------------------------------

Check out below articles to learn more about Date calculations like this.

*   [Add any number of days, months or years to a date with this formula](https://chandoo.org/wp/add-any-number-of-days-months-or-years-to-a-date-with-this-simple-trick/)
    
*   [Highlight due dates, over due items in Excel](https://chandoo.org/wp/highlight-due-dates-excel/)
    
*   [Calculating Duration in days, months & years – Excel Jet](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    
*   [DateDif documentation](https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c?ns=EXCEL&version=90)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [4 Comments](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/#respond)
    
*   Tagged under [date](https://chandoo.org/wp/tag/date/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel](https://chandoo.org/wp/tag/excel-2/)
    , [formulas](https://chandoo.org/wp/tag/formulas-2/)
    , [networkdays](https://chandoo.org/wp/tag/networkdays-2/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious35 shortcuts & tricks to make you an #AWESOME Data Analyst](https://chandoo.org/wp/35-tips-data-analysis-in-excel/)

[NextBeautiful Staff Roster Excel Template \[FREE Download\]Next](https://chandoo.org/wp/staff-roster-excel-template-free/)

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
    
    [Reply](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ