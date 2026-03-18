# Multiplying and other arithmetic with Feet & Inches in Excel - How to?

**Source:** https://chandoo.org/wp/feet-inches-arithmetic-in-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Multiplying 24ft 9inches with 6ft 3inches using Excel
=====================================================

*   Last updated on April 14, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Imagine you are a carpenter and you are tasked with laying wooden floor at Gill Bates’ house_. Now Gill B has a very big house and he wants to make sure you do a good job. So instead of asking you to lay the floor for entire house, he asks you to finish flooring in the guest bedroom first. Here are the dimensions of that guest bedroom.

*   Width: 6ft 3inches
*   Length: 24ft 9inches
*   Size of individual wooden floor board: 2ft x 4inches

**And here is the big question you are facing.**

_What?!? the guest bedroom width is only 6ft 3inches?_

But over the years of chiseling and polishing you have learned to keep quiet and do your work.

So the real question you have is, **How many wooden floor boards should you buy?**

Of course, you want to find the answer using Excel. Why else would a carpenter read this blog?

Multiplying Feet & Inches using Excel
-------------------------------------

If the metric system became an universal standard for measuring things, we all can stop worrying and go to that wooden tile store to place order now. Alas, we still have to deal with feet, inches, miles, pounds, ounces and gallons (not to mention irrational numbers like pi, e and _eleventeen_).

Fortunately, Excel has 2 powerful features to support calculations like this.

### Method 1: Using CONVERT()

CONVERT() as the name suggests is an Excel function that can convert values from one base to another, like feet to inches, square meters to square feet, centigrade to fahrenheit,  grape juice to wine. Well, not the last one, but it shines in all other scenarios.

So we can use CONVERT() to first convert all the numbers to a common base like meters or inches or feet. Then perform the arithmetic. Once done, convert back to Feet & Inches.

Pretty simple eh?

See this model:

![Multiplying & Other arithmetic on feet & inches using Excel - how to?](https://img.chandoo.org/f/multiplying-and-other-arithmetic-feet-inches-excel-trick-1.png)

**The process is simple:**

1.  First we convert all feet & inch values to meters
2.  This is done with =CONVERT( feet value + inch value / 12, “ft”, “m”)
3.  Once we have values in meters, we perform the arithmetic by simple multiplication & division.

### Method 2: Using Fraction Cell Format

If you don’t feel so hot for the CONVERT(), then this method works for you. You can use **fraction cell formatting** to enter fractions like 6 3/12 and 24 9/12 in to cells and let Excel treat them as regular numbers when multiplying, adding or dividing.

See this model:

![Multiplying & other arithmetic with Feet & Inches in Excel - How to?](https://img.chandoo.org/f/multiplying-and-other-arithmetic-feet-inches-excel-trick-2.png)

**How to set it up?**

1.  Select all the cells where you need values to be shown in feet inches fraction format
2.  Press CTRL + 1 (or right click and format cells)
3.  Select Custom and enter the formatting code as
4.  **\# ??/12**
5.  This ensures that when you type a fraction like 6 3/12, Excel treats that as number (6.25)
6.  Rest of the arithmetic is simple.

Related: [Custom Cell Formatting in Excel – Tips](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/)
, [more tips](http://chandoo.org/wp/2012/01/31/custom-number-formats-multiply-divide-by-any-power-of-10/)
, [even more tips](http://chandoo.org/wp/2011/11/02/a-technique-to-quickly-develop-custom-number-formats/)

Bonus Tricks
------------

Here are few more scenarios where you can use either CONVERT() or fraction formatting.

*   If varnishing 1 square feet takes 2 minutes 30 seconds, how much times does it take to finish a 20 ft 6 in x 12 ft 9 in room?
*   If average customer call lasts 3 minutes 10 seconds and Cynthia took 400 calls in last week, how many hours did she work?
*   If Mr. Gill Bates earns $1000 per every 1 minute 4 seconds, how many days does it take for him to earn $10 million?
*   How many teaspoons of honey per gallon?

Download example workbook:
--------------------------

[**Click here to download example workbook**](https://img.chandoo.org/f/feet-inches-arithmetic.xlsx)
. It shows 3 methods for solving this problem. Examine the formulas and format settings to learn more.

### Do you use Excel for these kind of problems?

I am not much of a carpenter. Few years ago, I decided to add a door to my office desk so that my kids (they learned how to crawl around that time) wouldn’t poke the reset button of my CPU. After buying necessary material (a wooden plank, nails, hinges, magnetic door locks) and wasting a day hammering nails in to my fingers, bending one of the hinges, almost breaking the wooden plank in to two, I gave up and closed the shelf-space completely instead ([here is a pic of my carpentering disaster](https://img.chandoo.org/f/my-carpentry-disaster.jpg)
). So it suffices to say I do not use Excel for modeling my carpentry jobs.

But I am sure many of our readers are better carpenters, masons, plumbers, knitters or cooks than me. **So tell me.** Do you use Excel for modeling these kind of problems? What formulas, techniques and tips do you use? Please share using comments.

Now if you excuse me, I have to go look at the leaky faucet my wife is complaining about. I am sure I can ruin it with a pipe wrench.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [41 Comments](https://chandoo.org/wp/feet-inches-arithmetic-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/feet-inches-arithmetic-in-excel/#respond)
    
*   Tagged under [Convert](https://chandoo.org/wp/tag/convert/)
    , [custom cell formatting](https://chandoo.org/wp/tag/custom-cell-formatting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [roundup](https://chandoo.org/wp/tag/roundup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousExcel for iPad – Demo & Introduction](https://chandoo.org/wp/excel-for-ipad-intro/)

[NextCP005: Introduction to Form Controls – an interview with Debra DalgleishNext](https://chandoo.org/wp/cp005-form-controls/)

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
    
    [Reply](https://chandoo.org/wp/feet-inches-arithmetic-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/feet-inches-arithmetic-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/feet-inches-arithmetic-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ