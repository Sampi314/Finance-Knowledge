# Using Excel's Random Functions to setup Dummy Data

**Source:** https://chandoo.org/wp/dummy-data-random-functions

---

*   [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Dummy Data – How to use the Random Functions
============================================

*   Last updated on May 5, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

**Dummy Data – How to use the Random Functions**

Using collected or known data is the best when developing Excel models, but from time to time this may not be available when you are developing your model.

This post will look at some options for setting up Dummy Data using Excels Random functions.

**Variability**
---------------

Real data displays a range of variability, but this variability is generally within ranges or distributions of ranges of results.

All fields type can contain variability

ie: Country, State Names and Zip/Postal Codes, Maybe large lists but are fixed

Peoples Names, Maybe a large lists but are fixed by local rules

Ages, generally less than 80, never less than 0

Dates: Rarely before 1990 or 1900 in rare cases

Lists: are fixed

Numbers: generally random or conforming to a fixed distribution or known trend

Numbers: may include integers, decimals, negatives, extremely large numbers or all combinations

In generating random lists you will need to choose if you want random data, random data within constraints or random with a distribution. The choice is really yours and should in part be based on what the data is being used for and how accurately it needs to reflect reality.

Techniques
----------

The techniques described below are all shown with a worked example in the attached [Examples File](https://chandoo.org/wp/wp-content/uploads/2011/05/Dummy-Data2.xlsx "Dummy Data 2007/10 Examples")
 or the [Excel 2003 Example](https://chandoo.org/wp/wp-content/uploads/2011/05/Dummy-Data2.xls "Example File 2003 Ver")

Each example is annotated below like (Example 4.). ie: Refer to Example 4 in the above example files.

### **Dates**

Setting up Random Dates is a simple process using the Date function.

_\=__Randbetween(StartDate,EndDate)_

Dates in a Range of Years

_\=__Randbetween(Date(2000,1,1),Date(2011,12,31))_

Will give a list of Random dates between 1 Jan 2000 and 31 Dec 2011 (Example 1.)

(_Thanx Mike W_)

Dates in a Month

_\=Date(2010, 6, Randbetween(1,30)_

Will give a list of Random dates between 1 June 2010 and 30 June 2010 (Example 2.)

Don’t worry that the above formula (Example 1) can actually produce a 31 Feb 2005, the Date function will happily convert that to 3 March 2005 (Example 3.)

Dates within a Date Distribution

_\=DATE(2011,7,NORMINV(RAND(), 0,60))_

Will give a list of Random dates between approximately 1 Jan 2010 and 31 Dec 2010, with a mean of July 1 and standard deviation of 2 Months (60days) (Example 4.)

Where NORMINV(RAND(), 0,60) will return values between -180 and +180, 99.7% of the time

### **Text Fields**

Dependant on how many items in the list you require there are 3 techniques available

Choose

For small lists of less than 6 to 10 items you can use a simple Choose function (Example 5.)

_\=Choose(Randbetween(1,6),”Item 1″, “Item 2”, “Item 3”, “Item 4”, “Item 5”, “Item 6”)_

VLookup

Using VLookup (Example 6.)

_\=Vlookup(Randbetween(1,List Length), List, 2)_

Index

Using Index (Example 7.)

_\=Index(List, Randbetween(1, Counta(List) ))_

### **Numbers**

Small Random List of Numbers

Random from a small list of numbers (Example 8.)

_\=Choose(Randbetween(1,6), Numb 1, Numb 2, Numb 3, Numb 4, Numb 5, Numb 6 )_

Note that the numbers:

*   Don’t have to be in any order,
*   Can be integers, negatives or contain decimals
*   Can be repeated

eg: _=Choose(Randbetween(1,6), 18, 21, -19, 36.4, 18, 24)_

Random Integers

Return Integers between Start and Finish (Example 9.)

_\=Randbetween(Start, Finish)_

_\=Randbetween(50, 100)_

Will return an Integer between 50 and 100

Random Numbers

_\=Rand()_

Will return a random number between 0 and 1

_\=Round(Rand()\*100, 2)_

Will Return Numbers between 0 and 100 with 2 Decimal places (Example 10.)

Random Numbers Based on a Distribution

_\=Norminv(Rand(), Mean, SD)_

Will return a random number between 0 and 1 based on a distribution of Average = Mean and Standard Deviation = SD

_\=Norminv(Rand(), 50, 17)_

Will return a random number between 0 and 100 based on a distribution of Average = 50 and Standard Deviation = 17, (Example 11.)

Random Numbers Fitting a Trend

If your distribution has to match a trend add a Random component to the Trends equation (Example 12.)

Y=mX+c

\= rand() \* X + rand()\*5

_\= rand() \* A2 + rand()\*5_

### **True/False**

Choose

Use Choose and Randbetween (Example 13.)

_\=Choose(Randbetween(1,2), True, False)_

If

Use If and Rand (Example 14.)

_\=If(Rand()<0.5, True, False)_

### **Combination Text and Numbers**

The above techniques can be combined to make lists of Alpha Numeric Data

Say your business has a fleet of vehicles (TR=Truck, VN=Van, CAR=Car)

_\=Choose(Randbetween(1,3),”TR”,”VN”,”CAR”) & Text(Randbetween(1,15),”0#”)_

Will randomly choose 1 of “_TR”,”VN”,”CAR” and add a random number between 1 and 15 to it format with a leading 0, eg: TR05,_ (Example 15.)

**Other Sources of Data**
-------------------------

### Random Data

There are a number of web sites where Random Data is available.

[http://www.fakenamegenerator.com/order.php](http://www.fakenamegenerator.com/order.php)

[http://www.generatedata.com/#generator](http://www.generatedata.com/#generator)

[http://www.melissadata.com/lookups/](http://www.melissadata.com/lookups/)

### Open Source Data

There are a number of web sites where Open Source Data is available.

[http://en.wikipedia.org/](http://en.wikipedia.org/)

[http://www.google.com/](http://www.google.com/)

[http://www.readwriteweb.com/archives/where\_to\_find\_open\_data\_on\_the.php](http://www.readwriteweb.com/archives/where_to_find_open_data_on_the.php)

**Function Used:**
------------------

**Rand**: Returns a random number between 0 and 1.

**Randbetween**: Returns a random Integer between lower and upper limits. Pre Excel 2007 Randbetween was only available through installation of the Analysis Toolpak (Thanx Luke).

**Norminv**: Returns the inverse of the normal cumulative distribution. That is it returns the X value from a Normal Distribution that has a know Mean and Standard Deviation where the a known cumulative percentage is supplied.

**Choose**: Choose an item from a list of up to 254 items.

**Vlookup**: Lookup the matching value from a list and return a data item from another column from the same location.

**Index**: Retrieve an items from a defined location within a range.

**Text**: Displays a number as Text with a defined format.

**Other Uses of Random Functions**
----------------------------------

Of course the techniques shown here don’t have to be used for setting up Dummy Data.

One area where Random numbers is used is in Monte Carlo Simulation. This has been discussed at [Chandoo.org](http://chandoo.org/wp/ "Chandoo.org")
 at [Data Tables and Monte-Carlo Simulations in Excel a Comprehensive Guide](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/ "Data Tables & MonteCarlo Simulations")

Techniques
----------

The techniques described above are all shown with a worked example in the attached [Examples File](https://chandoo.org/wp/wp-content/uploads/2011/04/Dummy-Data.xlsx "Dummy Data 2007/10 Examples")
 or the [Examples File 2003 ver](https://chandoo.org/wp/wp-content/uploads/2011/05/Dummy-Data.xls "Example Files 2003 Ver")

Limitations in Pre Excel 2007 versions
--------------------------------------

The Excel function, Randbetween, was only introduced in Excel 2007. As such the exaples above will only work in 2007/10.

However a simple alternative is available

Randbetween(Low, High) = Low + Int(Rand()\*(High-Low))+1

_Randbetween(90, 100) = 90 + Int(Rand()\*10)+1_

Examples using this approach are shown in the 2003 Version of the Examples files above.

**How have you made Dummy Data or used the Random Functions?**
--------------------------------------------------------------

How have you made Dummy Data or How have you used it ?

How have you used Random Numbers in your workbooks ?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [53 Comments](https://chandoo.org/wp/dummy-data-random-functions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/dummy-data-random-functions/#respond)
    
*   Tagged under [choose()](https://chandoo.org/wp/tag/choose/)
    , [Dummy Data](https://chandoo.org/wp/tag/dummy-data/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Norminv](https://chandoo.org/wp/tag/norminv/)
    , [rand()](https://chandoo.org/wp/tag/rand/)
    , [RANDBETWEEN()](https://chandoo.org/wp/tag/randbetween/)
    , [random](https://chandoo.org/wp/tag/random/)
    , [text()](https://chandoo.org/wp/tag/text/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [excel apps](https://chandoo.org/wp/category/excel-apps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPrevious80% Discount on PUP & PowerPivot Contest – Hurry up!](https://chandoo.org/wp/pup-discount-powerpivot-contest/)

[Next5 things you should know about VBA Classes + a Demo LessonNext](https://chandoo.org/wp/vba-classes-demo-and-faqs/)

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
    
    [Reply](https://chandoo.org/wp/dummy-data-random-functions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/dummy-data-random-functions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/dummy-data-random-functions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ