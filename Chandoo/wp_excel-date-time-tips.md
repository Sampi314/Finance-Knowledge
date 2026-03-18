# Excel Date & Time tips - How to calculate tomorrows date, last weeks date, next months date etc...

**Source:** https://chandoo.org/wp/excel-date-time-tips

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

42 tips for Excel time travelers
================================

*   Last updated on October 17, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**![Excel Date & Time tips](https://img.chandoo.org/q/excel-date-and-time-tips.png)Today, let’s travel in time**.  Pack your photon ray guns, extra underwear, buckle your seat belts and open Excel!

Of course, we are not going to travel in time. (Come to think of it, we are going to travel in time. By the time you finish reading this, you would have traveled a few minutes)

We are going to learn how to travel in time when using Excel. **In simple terms, you are going to learn how to move forward or backward in time using Excel formulas.**

So are you ready to hit the warp speed? Let’s beam up our Excel time machine.

### Tip 0 – Date & Time are an illusion

Most important tip for Excel time travelers is to understand that _**Excel dates & times are just numbers**_. So when you see a date like 17-October-2013 in a cell, you can safely assume that it is a number disguised to look like 17th of October, 2013. To see the number behind this, just select the cell and format it as number (from Home ribbon).

![Date & Time values are numbers in Excel](https://img.chandoo.org/q/dates-are-numbers-in-excel.gif)

Now that you understood this concept, let’s jump in to the 42 tips. All these tips assume a date or time value is in the cell A1.

### Staying at present:

1.  To have latest star date in a cell, just press CTRL+; (of course, in Excel world, star date is nothing but whatever date your computer shows)
2.  To have current time in a cell, just press CTRL+:
3.  Of course, we time travelers are lazy. So pressing CTRL+; every day or CTRL+: every second is not cool. That is why you can use =TODAY() in a cell to get today’s date. It will automatically change when you re-open the file tomorrow.
4.  Likewise, use =NOW() to get current date & time in a cell. Remember, although time changes every second, you will not see the cell updated unless the formula is somehow re-calculated. This is done by,
    *   Pressing F9
    *   Saving / re-opening the file
    *   Making any changes to any cell (like typing a value, changing a value)
    *   Editing the formula cell and pressing Enter
5.  To check if today is after or before the date in cell A1, you can use =TODAY() > A1. This will be TRUE if A1 has a past date and FALSE if A1 has a future date.
6.  To know how many days are there between TODAY and the date in A1, use =TODAY() – A1. This will be a negative number if A1 is a future date. To see just the number of days (without negative sign), you can use =ABS(TODAY()-A1)
7.  To know how many hours are left between the time in A1 and current time, use =(NOW()-A1)\*24.
8.  While the above formula works, it shows hours and fraction. To just see hours and minutes left, you can use =TEXT((NOW()-A1), “\[hh\]:mm”). Note: This formula works only when A1 < NOW().
9.  To know how many weeks are left between TODAY() date and a future date in A1, use =(TODAY() –  
    A1)/7
10.  To know how many months are left between TODAY() and date in A1, use = DATEDIF(TODAY(), A1, “m”).  
    Related: [How to use DATEDIF function](http://chandoo.org/wp/2011/05/16/lost-excel-functions/)
    .
11.  To know which month is running, use =MONTH(TODAY())
12.  To see the month name instead of number, use =TEXT(TODAY(), “MMMM”). This shows the month’s name in your Excel language.
13.  To know which year is running, use =YEAR(TODAY())
14.  To see the last 2 digits of the year, you can use =RIGHT(YEAR(TODAY()), 2)
15.  To find the day of week for TODAY, use =WEEKDAY(TODAY()). This will give a number (1 to 7, 1 for Sunday, 7 for Saturday).
16.  To see the weekday name instead of number, use =TEXT(TODAY(), “DDDD”).
17.  To see today’s date alone, use =DAY(TODAY())
18.  [To know if the present year is a leap year or not, see this](http://chandoo.org/wp/2012/02/29/check-leap-year-using-excel/)
    .

### Going back in time

19.  To go back by 6 days from the date in A1, use =A1-6
20.  To go back to last Friday use =A1-WEEKDAY(A1, 16). This works in Excel 2010, 2013. If your time machine is old (ie you have Excel 2003 or earlier versions), you can use =A1-CHOOSE(WEEKDAY(A1), 2,3,4,5,6,7,1)
21.  To go back by 5 weeks, use =A1-5\*7
22.  To go back to start of the month, use =DATE(YEAR(A1), MONTH(A1),1)
23.  To go back to end of previous month, use = DATE(YEAR(A1), MONTH(A1),1) – 1
24.  Or use =EOMONTH(A1,-1)
25.  To go back by 2 months, use =EDATE(A1, -2)
26.  To go back by 27 working days, use =WORKDAY(A1, -27). This assumes, Monday to Friday as working days.
27.  To go back by 27 working days, assuming you follow Monday to Friday work week and a set of extra holidays, use =WORKDAY(A1, -27, LIST\_OF\_HOLIDAYS)
28.  To go back by 7 quarters, use =EDATE(A1, -7 \* 3)
29.  To go back to the start of the year, =DATE(YEAR(A1), 1,1)
30.  To go back to same date last year, = DATE(YEAR(A1)-1, MONTH(A1), DAY(A1))
31.  To go back a decade, =DATE(YEAR(A1)-10, MONTH(A1), DAY(A1))

### Going forward in time

_We, time travelers are smart people_. Once you know that turning the knob backwards takes you to past, you know how to go to future. So I am giving very few examples for going forward in time.

32.  To go to the 17th working day from date A1, assuming you use Sunday to Thursday workweek, use =WORKDAY.INTL(A1,17,7). This formula works in Excel 2010 or above.
33.  To go to next hour, use=A1+1/24
34.  To go to next day morning 9AM, use =INT(A1+1) + 9/24
35.  To go to 18th of next month, use =DATE(YEAR(A1), MONTH(A1)+1, 18)
36.  To go to end of the current quarter for date in A1, use =DATE(YEAR(A1), CHOOSE(MONTH(A1), 4,4,4,7,7,7,10,10,10,13,13,13),1)-1
37.  To go to a future date that is 4 years, 6 months, 7 days away from A1, use =DATE(YEAR(A1)+4, MONTH(A1)+6, DAY(A1)+7)

### Finding the amount of time traveled

38.  To know how many days are between 2 dates (in A1 & A2), use =A1-A2
39.  To know how many working days are between 2 dates, use =NETWORKDAYS(A1, A2) (remember: A1 should be less than A2).

### Fixes for common time travel hiccups

40.  If you see ###### instead of a date in a cell, try making the column wider. If you still see ######, that means the date value is not understandable by Excel (negative numbers, dates prior to 1st of January 1900 etc.)
41.  Often when pasting date values in to Excel, you notice that they are not treated as dates. [Use these techniques to fix](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    .
42.  If you pass in-correct values or use wrong parameters, your date formulas show an error like #NUM or #VALUE. Read this to [understand how to fix such errors](http://chandoo.org/wp/2009/04/20/excel-formula-errors/)
    .

### Quiz time for time travelers

I see that you safely made it here. I hope you had a good journey. Let me see how good your time traveling is. Answer these questions:

*   Write a formula to take date in A1 to next month’s first Monday.
*   Given a date in A1, find out the closest Christmas date to it.

### Building your own time machine? Check out these tips too

If you work with date & time values often, then learning about them certainly pays off. Read below articles to one up your time travel awesomeness.

*   [Using Date & Time in Excel](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)
    
*   [How to calculate common holiday dates in Excel?](http://chandoo.org/wp/2009/12/24/public-holidays-excel-dates/)
    
*   [How to calculate payroll dates?](http://chandoo.org/wp/2008/09/17/payroll-period-calculation-using-excel-formulas/)
    
*   [How to sort a bunch of birth dates by _birthday_?](http://chandoo.org/wp/2013/08/26/sort-by-birthday-quick-tip/)
    
*   [Check if two dates are in same month](http://chandoo.org/wp/2012/11/02/two-dates-in-month-check/)
    

Good luck time traveling. I will see you again in future 🙂

PS: _Make sure you attempt the challenges and post your answers in comments_.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [73 Comments](https://chandoo.org/wp/excel-date-time-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-date-time-tips/#respond)
    
*   Tagged under [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [edate()](https://chandoo.org/wp/tag/edate/)
    , [eomonth](https://chandoo.org/wp/tag/eomonth/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [networkdays()](https://chandoo.org/wp/tag/networkdays/)
    , [Networkdays.intl()](https://chandoo.org/wp/tag/networkdays-intl/)
    , [now()](https://chandoo.org/wp/tag/now/)
    , [today()](https://chandoo.org/wp/tag/today/)
    , [workday](https://chandoo.org/wp/tag/workday/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousChandoo.org produces it’s Second MVP.](https://chandoo.org/wp/chandoo-org-produces-its-second-mvp/)

[NextI am writing a book \[and its coming soon\]Next](https://chandoo.org/wp/the-vlookup-book-coming-soon/)

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
    
    [Reply](https://chandoo.org/wp/excel-date-time-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-date-time-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-date-time-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ