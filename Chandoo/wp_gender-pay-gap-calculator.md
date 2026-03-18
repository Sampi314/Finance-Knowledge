# Gender Pay Gap Calculator - FREE Excel Template

**Source:** https://chandoo.org/wp/gender-pay-gap-calculator

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

How to calculate the Gender Pay Gap using Excel Formulas? (Free Calculator Template)
====================================================================================

*   Last updated on March 19, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**_Gender Pay Gap_** is the difference in pay for groups of men & women and usually based on the average or median salaries. We can use Microsoft Excel to quickly calculate the GPG (Gender Pay Gap) from your data. In this article, let me explain the process, Excel formulas and offer you a ready to use GPG calculator.

What is Gender Pay Gap?
-----------------------

![What is Gender Pay Gap?](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0047.png)

_According to NZ Government,_

> Gender pay gaps are differences in pay for groups of women and men, usually based on the median or mean pay that men and women receive.
> 
> Source: [Statistics New Zealand](https://www.stats.govt.nz/methods/organisational-gender-pay-gaps-measurement-and-analysis-guidelines)

How to calculate Gender Pay Gap in Excel?
-----------------------------------------

![Gender Pay Gap Excel formulas](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0048.png)

Assuming you have average salary of men & women in two cells C3 & C4, we can calculate Gender Pay Gap using the below formulas:

**Gender Pay Gap in $s:**

    =C3 - C4Generalized formula = average of male salary - average of female salary

**Percentage Gender Pay Gap:**

    =(C3-C4)/C3Generalized formula = (average of male salary - average of female salary) / average of male salary

Gender Pay Gap from raw data:
-----------------------------

![example staff data table](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0049.png)

Excel is a great option for identifying and reporting gender pay gap issues when you have full employee data. Let’s say you have the staff data in an [Excel table](https://chandoo.org/wp/data-tables/)
 as shown above.

In this case, we can use below formulas to calculate the Gender Pay Gap:

### Step 1: Set up your data in as a table

Create a 3-column table in Excel with the staff ID, gender & annualized full-time salary. (Related: [Learn how to create a table in Excel](https://chandoo.org/wp/data-tables/)
)

Name your table as “staff” using the Table Design ribbon in Excel.

### Step 2: Calculate male & female average salaries:

You can use AVERAGEIFS function in Excel to calculate the male & female specific average salary.

The formula for male average looks like this:

    =AVERAGEIFS(staff[Annualized Full-time Salary],staff[Gender], "Male")

And the formula for female average looks similar.

### Step 3: Calculate the Gender Pay Gap in $s and %:

The formulas for this are explained above. They are:

GPG in $s: =Average Male Salary – Average Female Salary

GPG in %: =(Average Male Salary – Average Female Salary) / Average Male Salary

### Step 4: Format everything

Format the GPG $ and Salary calculations in your currency formatting (Ctrl Shift 4)

Format the GPG % in Percentage formatting using Excel format cells option (CTRL Shift 5)

Please refer to below illustration for formula set up and help.

![Formulas to calculate "average" GPG from raw data](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0051.png)

Average vs. Median Gender Pay Gaps
----------------------------------

![Average vs. median gpg](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0052.png)

It is a good idea to calculate both average and median GPG values from your data. We all know that an odd high value can impact the average calculation. May be your CEO is a female and her high $$$ salary thus she bumps up the average female pay significantly.

### To calculate the Median Gender Pay Gap values in Excel:

Firstly, calculate the median pay for both male & female groups. _Unfortunately, Excel doesn’t have a MEDIANIFS function._ So, use the below formula instead:

    =MEDIAN(IF(staff[Gender]="Male",staff[Annualized Full-time Salary]))

**Caution: Array formula**

After typing the formulas, press **CTRL+Shift+Enter** to get the correct result.

Change the gender value to Female for the respective median salary.

Once both medians are calculated, you can easily calculate the gender pay gap (both in dollars and percentage) using the same formulas as above.

Download FREE Gender Pay Gap Calculator – Excel File
----------------------------------------------------

[![download pay gap calculator excel workbook](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0055.png)](https://chandoo.org/wp/wp-content/uploads/2024/03/gpg-calculator.xlsx)

Click here to download my [**Gender Pay Gap calculator template**](https://chandoo.org/wp/wp-content/uploads/2024/03/gpg-calculator.xlsx)
. Copy and paste your data and the file calculates the GPG automatically.

How to get the Hourly Pay Gap values?
-------------------------------------

![how to calculate hourly pay gap](https://chandoo.org/wp/wp-content/uploads/2024/03/SNAG-0053.png)

Once you have calculated the Gender Pay Gap in dollars, just divide the number with total annual hours of work. In most countries, this would be 2080 hours (ie 52 weeks times 40 hours per week).

So, for example, if you have a pay gap of $3,117, then the hourly pay gap is $1.50

This means, female staff are earning $1.50 less than their male counterparts _every hour._

Our GPG is negative, what does it mean?
---------------------------------------

A negative GPG value indicates that your female staff are paid more (on average or median basis) compared to the male staff.

Limitations & Problems with Gender Pay Gap statistics:
------------------------------------------------------

While Gender Pay Gap offers a great insight into the compensation of men vs women employees, it has a few limitations.

*   **GPG doesn’t explain any hierarchical distribution issues.** If you have a lopsided distribution of staff in your organization (may be more female staff at lower-level positions and more male staff in senior positions), GPG doesn’t expose this issue. I recommend visualizing the male vs. female distribution by salary bands or seniority for a better insight in to these issues.
*   **A low or zero Gender Pay Gap is not enough.** If you want an equitable and fair organization, aiming for a zero gender pay gap at aggregate level is not enough. You need to examine GPG by:
    *   department level GPG
    *   city / location level GPG
    *   manager vs. non-manager GPG
    *   new hires vs. existing staff GPG
*   **GPG is meaningless for small organizations**. If your total headcount is less than 30, GPG calculations can be meaningless or less insightful.

In conclusion,
--------------

Gender Pay Gap is a key metric (KPI) in HR data analysis. Calculating, measuring and tracking GPG is helpful to understand any underlying pay issues in your organization. But don’t forget to explore the staff distribution, hiring patterns and historical trends to fully understand your data.

For more on HR data analysis, check out below articles:

*   [9 Box Grid & talent mapping analysis with Excel](https://chandoo.org/wp/9-box-talent-map-template/)
    
*   [Understanding Employee Churn using Excel](https://chandoo.org/wp/figuring-out-employee-churn-with-power-query-hr-analytics/)
    
*   [Employee training tracker with Excel](https://chandoo.org/wp/training-tracker/)
    
*   [HR Dashboard using Excel – Video](https://youtu.be/ui657YnwLV8)
    
*   [HR Dashboard using Power BI](https://youtu.be/5KaIU-9EF-0)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/gender-pay-gap-calculator/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/gender-pay-gap-calculator/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Excel for HR](https://chandoo.org/wp/tag/excel-for-hr/)
    , [gender pay gap](https://chandoo.org/wp/tag/gender-pay-gap/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

[PrevPreviousWeighted Average in Excel \[Formulas\]](https://chandoo.org/wp/weighted-average-excel/)

[NextHow to convert test scores to letter grades in Excel?Next](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/gender-pay-gap-calculator/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/gender-pay-gap-calculator/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/gender-pay-gap-calculator/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ