# Beyond If and Sum: 15 very useful microsoft excel formulas for everyone

**Source:** https://chandoo.org/wp/15-microsoft-excel-formulas

---

*   [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Beyond If and Sum, 15 really useful excel formulas for everyone
===============================================================

*   Last updated on May 30, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Excel formulas can always be very handy, especially when you are stuck with data and need to get something done fast. But how well do you know the spreadsheet formulas?

**Discover these 15 extremely powerful excel formulas and save a ton of time next time you open that spreadsheet.**

### 1\. Change the case of cell contents – to UPPER, lower, Proper

Boss wants a report of top 100 customers, thankfully you have the data, but the customer names are all in lower cases. Fret not, you can Proper Case cell contents with proper() formula.

> Example: Use `proper("pointy haired dilbert")` to get **Pointy Haired Dilbert**

Also try `lower()` and `upper()` as well to change excel cell value to lower and UPPER case

### 2\. Clean up textual data with trim, remove trailing spaces

Often when you copy data from other sources, you are bound to get lots of empty spaces next to each cell value. You can clean up cell contents with trim() spreadsheet function.

> Example: Use `trim(" copied data ")` to get **copied data**

### 3\. Extract characters from left, right or center of a given text

Need the first 5 letters of that SSN or area code from that phone number? You can command excel to do that with left() function.

> Example: Use `left("Hi Beautiful!",2)` to get **Hi**

Also try `right(text, no. of chars)` and `mid(text, start, no. of chars)` to get rightmost or middle characters. You can use `right(filename,3)` to get the extension of a file name 😉

### 4\. Find second, third, fourth element in a list without sorting

We all know that you can use min(), max() to find the smallest and largest numbers in a list. But what if you needed the second smallest number or 3rd largest number in the list? You are right, there is a spreadsheet function to exactly that.

> Example: Use `SMALL({10,9,12,14,26,13,4,6,8},3)` to get **8**

![small-excel-formula-find-nth-small-number-in-list](https://chandoo.org/wp/wp-content/uploads/2008/08/small-excel-formula-find-nth-small-number-in-list.png "small-excel-formula-find-nth-small-number-in-list")

Also try `large(list, n)` to get the nth largest number in a list.

### 5\. Find out current date, time with a snap

You have a list of customer orders and you want to findout which ones are due for shipping after today. The funny thing is you do this everyday. So instead of entering the date every single day you can use today()

> Example: Use `today()` to get **08/13/2008** or whatever is today’s date

Also try `now()` to get current time in date time format. Remember, you can always format these date and times to see them the way you like (for eg. Aug-13, August 13, 2008 instead of 08/13/2008)

### 6\. Convert those lengthy nested if functions to one simple formula with Choose()

Planning to create a gradebook or something using excel, you are bound to write some if() functions, but do you know that you can use choose() when you have more than 2 outcomes for a given condition? As you all know, `if(condition, fetch this, or this)` returns “fetch this” if the condition is TRUE or “or this” if the condition is FALSE. [Learn more about spreadsheet if functions like countif, sumif etc.](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)

Where as `choose(m, value1, value2, value3, value4 ...)` can return any of the value1,2.., based on the parameter m.

> Example: Use `CHOOSE(3,"when","in","doubt","just","choose")   `to get **doubt**

Remember, you can always write another formula for each of the n parameters of choose() so that based on input condition (in this case 3), another formula is evaluated.

### 7\. Repetitively print a character in a cell n number of times

You have the ZIP codes of all your customers in a list and planning to upload it to an address label generation tool. The sad part is for some reason, excel thinks zip codes are numbers, so it removed all the trailing zeros on the leftside of the zip code, thus making the 01001 as 1001. Worry not, you can use `rept()` the extra needed zeros. You can also [custom format cell contents to display zip codes, phone numbers, ssn etc](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/)
.

> Example: Use `zipcode & REPT("0",5-LEN(zipcode))` to convert zipcode 1001 to **01001**

You can use `REPT("|",n)` to generate micro bar charts in your sheet. [Learn more about incell charting](http://chandoo.org/wp/2008/07/15/incell-bar-charts-revisited/)
.

### 8\. Find out the data type of cell contents

![type-formula-arguments-spreadsheet](https://chandoo.org/wp/wp-content/uploads/2008/08/type-formula-arguments-spreadsheet.png "type-formula-arguments-spreadsheet")This can be handy when you are working off the data that someone else has created. For example you may want to capitalize if the contents are text, make it 5 characters if its a number and leave it as it is otherwise for certain cell value. Type() does just that, it tells what type of data a cell is containing.

> Example: Use `TYPE("Chandoo")` to get **2**

See the various type return values in the diagram shown right.

### 9\. Round a number to nearest even, odd number

When you are working with data that has fractions / decimals, often you may need to find the nearest integer, even or odd number to the given decimal number. Thankfully excel has the right function for this.

> Example: Use `ODD(63.4)` to get **65**

Also try even() to nearest even number and int() to round given fraction to integer just below it.

> Example: Use `EVEN(62.4)` to get **64**  
> Use `INT(62.99)` to get **62**

If you need to round off a given fraction to nearest integer you can use `round(62.65,0)` to get 63.

### 10\. Generate random number between any 2 given numbers

When you need a random number between any two numbers, try randbetween(), it is very useful in cases where you may need random numbers to simulate some behavior in your spreadsheets.

> Example: Use `RANDBETWEEN(10,100)` may return **47** if you keep trying 😉

### 11\. Convert pounds to KGs, meters to yards and tsps to table spoons

You need not ask Google if you need to convert 156 lbs to kilograms or find out how much 12 tea spoons of olive oil actually means. The hidden convert() function is really versatile and can convert many things to so many other things, except one currency to another, of course.

![convert-from-lbs-to-kgs-excel-function](https://chandoo.org/wp/wp-content/uploads/2008/08/convert-from-lbs-to-kgs-excel-function.png "convert-from-lbs-to-kgs-excel-function")

> Example: Use `CONVERT(150,"lbm","kg")` to convert 150 lbs to **68.03** kgs.  
> Use `CONVERT(12,"tsp","oz")` to findout that 12 tsps is actually **2** ounces.

### 12\. Instantly calculate loan installments using spreadsheet formula

You have your eyes on that beautiful car or beach property, but before visiting the seller / banker to findout of the monthly payment details, you would like to see how much your monthly / biweekly loan payments would be. Thankfully excel has the right formula to divide an amount to equal payment installments over given time period, the pmt() function.

![pmt-calculate-loan-payments](https://chandoo.org/wp/wp-content/uploads/2008/08/pmt-calculate-loan-payments.png "pmt-calculate-loan-payments")

> _If your loan amount is $125,000,  
> APR (interest rate per year) is 6%,  
> loan tenure is 5 years and  
> payments are made every month, then,_
> 
> Use `PMT(6%/12,5*12,-125000)` which tells us that monthly payment is **$ 2,416** if you keep trying 😉

Also, if you want to find out how much of each payment is going for principle and how much for the interest component, try using ppmt() and ipmt() functions. As you can guess, even though EMIs or loan installments remain constant, the amount contributed to principle and interest vary each month.

### 13\. What is this week’s number in the current year ?

Often you may need to find out if the current week is 25th week of this year. This is not so difficult to find as it may seem. Again, excel has the right function to do just that.

> Example: Use `WEEKNUM(TODAY())` will get **33**

### 14\. Find out what is the date after 30 working days from today ?

Finding out a future date after 30 days from today is easy, just change the month. But what if you need to know the date thirty working days from now. Don’t use your fingers to do that counting, save them for typing a comment here and use the workday() excel funtion instead. 🙂

> Example: Use `WORKDAY(TODAY(),30)` tells that **Sep 24, 2008** is 30 working days away from today.

If you want to find out number of working days between 2 dates you can use networkdays() function, [find out this and a 14 other fun things you can do with excel](http://chandoo.org/wp/2008/08/01/15-fun-things-with-excel/)
.

### 15\. With so many functions, how to handle errors

Once you get to the powerful domain of excel functions to simplify your work, you are bound to have incorrect data, missing cells etc. that can make your formulas go kaput. If only there is a way to find out when a formula throws up error, you can handle it. Well, you know what, there is a way to find out if a cell has an error or a proper value. iserror() MS Excel function tells you when a cell has error.

> Example: Use `ISERROR(43/0)` returns **TRUE** since 43 divided by zero throws divide by zero error.

Also try ISNA() to findout if a cell has NA error (Not applicable).

Give these functions a try, simplify your work and enjoy 🙂

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [132 Comments](https://chandoo.org/wp/15-microsoft-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/15-microsoft-excel-formulas/#respond)
    
*   Tagged under [ideas](https://chandoo.org/wp/tag/ideas/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [productivity](https://chandoo.org/wp/tag/productivity/)
    , [spreadsheet](https://chandoo.org/wp/tag/spreadsheet/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    
*   Category: [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousThe Olympic Medals by Country Chart – Improved now](https://chandoo.org/wp/olympic-medals-excel-chart-improved/)

[NextSimulating Dice throws – the correct way to do it in excelNext](https://chandoo.org/wp/simulate-dice-throws/)

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
    
    [Reply](https://chandoo.org/wp/15-microsoft-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/15-microsoft-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/15-microsoft-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ