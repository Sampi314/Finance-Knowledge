# Extract Time from Strings using Text Format?

**Source:** https://chandoo.org/wp/formula-forensic-no-019

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensic No 019. Converting uneven Text Strings to Time
===============================================================

*   Last updated on April 19, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Last week over at the Chandoo.org Forums, Birko asked a question about [How to Import some Numbers as Times](http://chandoo.org/forums/topic/convert-a-number-to-hours-minutes-and-seconds "FF019")
.

“I have imported some data that comes in as a number that I need to convert to h:mm. The data string will be either 1,3,4,5,6 integers long and looks like this…eg

Imported         Need to equal this  
Number           h:mm  
0                      0:00  
100                  0:01  
1000                0:10  
10900              1:09  
235900            23:59

Can someone please provide a smart formula to convert this (assume data is in cell A1).”

Today in Formula Forensics we will look at how this problem was solved, and the solution which may surprise you.

Importing Numbers as Times.
---------------------------

When I first saw this data I start by looking at patterns.

Working backwards through the list

I can see that 235900 is 23 Hrs, 59 Min and 0 second

I can see that 10900 is 1 Hr, 9 Min and 0 second

I can see that 1000 is 0 Hrs, 10 Min and 0 second

I can see that 100 is 0 Hr, 1 Min and 0 second

I can see that 0 is 0 Hr, 0 Min and 0 second

I then start to think about how to extract the Hours, Minutes and seconds independently from the Text using a series of Left, Right and Mid functions, and quickly realised that due to the varying lengths of the strings, That they will end up being complex formulas as I will need to allow for each string length.

What if I pad the strings with leading 0’s and then extract them.

That is possible, but as a single formula it will be long and cumbersome as the padding has to occur a number of times for each Hour, Minute and Second as part of the Time() function.

So padding may work but is cumbersome, then a bright light moment

What about I use the Text function to do the padding.

And I quickly posted the following formula:

    =(LEFT(TEXT(A1,"000000"),2)/24)+(MID(TEXT(A1,"000000"),3,2)/1440)+(RIGHT(TEXT(A1,"000000"),2)/(24*3600))

As Time is just a number between 0 = midnight and 0.999999 = 11:59:59 pm, I can extract the Hours, Minutes and seconds separately and then simply add them together to get the actual time

I Can use the Text function to display the Strings in a consistent format that allows me to use the Left, Mid and Right functions to retrieve the Hours minutes and Seconds from the appropriate places.

Lets work through this formula section by section and see what is going on.

### Hours

`The Hours component of the formula is`

`=``(LEFT(TEXT(A1,"000000"),2)/24)``+(MID(TEXT(A1,"000000"),3,2)/1440)+(RIGHT(TEXT(A1,"000000"),2)/(24*3600))`

`=(LEFT(TEXT(A1,"000000"),2)/24)`

Working from the middle out, this formula takes the value in A1 and displays it as a Number with the format “000000”

So using our data

235900 will convert to 235900

10900 will convert to 010900

1000 will convert to 001000

We can now use a Left() function to extract the hours from the first 2 characters of the converted string

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF19_1.png "FF19_1")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF19_1.png)

Using our examples:

Left(235900,2) = 23

Left(010900,2) = 01

Left(001000,2) = 00

To convert hours to a Time we simply divide by 24

### Minutes

`The Minutes component of the formula is`

`=(LEFT(TEXT(A1,"000000"),2)/24)+(``MID(TEXT(A1,"000000"),3,2)/1440``)+(RIGHT(TEXT(A1,"000000"),2)/(24*3600))`

`=MID(TEXT(A1,"000000"),3,2)/1440`

Once again, Working from the middle out, this formula takes the value in A1 and displays it as a Number with the format “000000”

So using our data

235900 will convert to 235900

10900 will convert to 010900

1000 will convert to 001000

We can now use a Mid() function to extract the minutes from the middle 2 characters of the converted string

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF19_2.png "FF19_2")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF19_2.png)

Mid(235900,3,2) = 59

Mid(010900,2) = 09

Mid(001000,2) = 10

To convert Minutes to a Time we simply divide by 1440 (1440 is how many minutes are in a day = 24 \* 60)

### Seconds

`The Seconds component of the formula is`

    =(LEFT(TEXT(A1,"000000"),2)/24)+(MID(TEXT(A1,"000000"),3,2)/1440)+(

`=RIGHT(TEXT(A1,"000000"),2)/(24*3600)``)`

Once again, Working from the middle out, this formula takes the value in A1 and displays it as a Number with the format “000000”

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF19_3.png "FF19_3")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF19_3.png)

So using our data

235900 will convert to 235900

10900 will convert to 010900

1000 will convert to 001000

We can now use a Right() function to extract the minutes from the middle 2 characters of the converted string

Right(235900,3,2) = 00

Right(010900,2) = 00

Right(001000,2) = 00

To convert Seconds to a Time we simply divide by 86400 (86,400 is how many seconds are in a day = 24 \* 60 \* 60)

### Total Time

To get the total Time we simply add the Hour, Minutes and Seconds together

`=``(LEFT(TEXT(A1,"000000"),2)/24)``+``(MID(TEXT(A1,"000000"),3,2)/1440)``+``(RIGHT(TEXT(A1,"000000"),2)/(24*3600)``)`

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/04/TextToTime.xls "Text to Time")
.

Formula Forensics “The Series”
------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "FF The Series")

Formula Forensics Needs Your Help
---------------------------------

I urgently need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained but don’t want to write a post also send it to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [22 Comments](https://chandoo.org/wp/formula-forensic-no-019/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensic-no-019/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [left()](https://chandoo.org/wp/tag/left/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mid()](https://chandoo.org/wp/tag/mid/)
    , [right()](https://chandoo.org/wp/tag/right/)
    , [text()](https://chandoo.org/wp/tag/text/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousCreating Customer Service Dashboard in Excel \[Part 3 of 4\]](https://chandoo.org/wp/creating-customer-service-dashboard-in-excel/)

[NextSend mails using Excel VBA and OutlookNext](https://chandoo.org/wp/send-mails-using-excel-vba-and-outlook/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-019/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensic-no-019/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensic-no-019/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ