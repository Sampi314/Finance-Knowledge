# Formula-Forensics-No. 036: Calculating Costs that Vary By Year

**Source:** https://chandoo.org/wp/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Posts by Sajan](https://chandoo.org/wp/category/posts-by-sajan/)
    

Formula Forensics-No. 036: Calculating Costs that Vary by Year and Age
======================================================================

*   Last updated on November 26, 2013

![Picture of Sajan Thomas](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=300&d=mm&r=g)

#### Sajan Thomas

Share

Facebook

Twitter

LinkedIn

Van Gysel asked in a [recent post at Chandoo.org](http://chandoo.org/forum/threads/multiply-two-matrix.13309/ "Question at Chandoo.org")
 for a way to calculate the costs of running a plantation.  The twist is that the costs vary by year, and based on the age of the trees.

The following is a slightly simplified version of the solution I offered:

\=SUM(IFERROR(LOOKUP(“Year”&MMULT(N($B$3:B$7>0),TRANSPOSE(COLUMN($B$3:B$7)^0)), $B$11:$I$11, $B12:$I12),0)\*B$3:B$7)      Ctrl+Shift+Enter

Today I am going to try and explain how the formula works.

As always at Formula Forensics, you can follow along with a sample file: [Download Here](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Calculating-Plantation-Costs.xlsx "Sample File")

The Problem
-----------

In a plantation, the costs for planting and maintaining trees vary based on the age of the trees and by year.  The table below shows the acres of trees planted per year and the yield and costs per year that vary based on the age of the trees.

![FF36-02](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-02.jpg)

Let us look at the calculations needed for each year.

#### Year 2013

*   300 acres of trees were planted in 2013.  Calculations for 2013 are as follows.  (Only Yield calculation is shown, but the process is similar for Nursery costs, Fertilizers, etc.)
*   The trees do not yield any fruits in the first year.  As such, Yield for year1=300\*0=0

That was easy!

####  Year 2014

*   700 additional acres of trees will be planted in 2014.  Calculations for 2014 are as follows.  (Again, only Yield calculation is shown, but others are calculated similarly.)

[![FF36-Year2Calc](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Year2Calc.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Year2Calc.jpg)

*   300 acres of trees are 2 years old.  700 acres are 1 year old.
*   The 300 acres from 2013 now yield fruit since it is year2.  However, the new trees (700 acres) do not yield any fruits yet.  So total yield for 2014=300\*Year2Yield+700\*Year1Yield=300\*5+700\*0

#### Year 2015

*   1000 additional acres are to be planted in 2015.  Calculations for 2015 are as follows:

[![FF36-Year3Calc](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Year3Calc.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Year3Calc.jpg)

*   300 acres are from 2013 (3 years old); 700 acres are from 2014 (2 years old); 1000 acres are from 2015 (1 year old).
*   Yield for 2015=300\*Year3Yield + 700\*Year2Yield + 1000\*Year1Yield = 300\*10 + 700\*5 + 1000\*0

####  Year 2016

*   1000 additional acres are to be planted in 2016.  Calculations for 2016 are as follows:

[![FF36-Year4Calc](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Year4Calc.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Year4Calc.jpg)

*   Yield for 2016=300\*15+700\*10+1000\*5+1000\*0

How do we simulate the above calculation in an Excel formula?

A Solution
----------

Let us first look at how we performed the calculations above manually, using the 2016 Yield as an example.

1.  We took each acreage value in 2016, and determined its age by counting how many years it has been since that acreage was planted.  You might have observed that the age can be counted by the number of times a value has been repeated up to that point.  (In other words, if I planted 300 acres in 2013, I should see that same amount in 2014, 2015 and 2016.) As such, 300 acres is repeated 4 times.  700 acres is repeated 3 times.  1000 acres is repeated 2 times. And the latest planting of 1000 acres exists only once.
2.  Once we determine the age for a given acreage, we looked up the yield for that age in the second table
3.  We then multiplied the acreage with the corresponding yield value.

Calculation #1 can be expressed as follows:

*   Age for acreage 1 (first planted in 2013)=count of B3:E3 where value is greater than zero.  i.e. COUNTIF(B3:E3,”>0”)
*   Age for acreage 2 (planted in 2014)=count of B4:E4 where value is greater than zero.  i.e. COUNTIF(B4:E4,”>0”)
*   Age for acreage 3 (planted in 2015)=count of B5:E5 where value is greater than zero.  i.e. COUNTIF(B5:E5,”>0”)
*   Age for acreage 4 (planted in 2016)=count of B6:E6 where value is greater than zero.  i.e. COUNTIF(B6:E6,”>0”)
*   Age for acreage 5 is zero since nothing has been planted for 2017 yet in 2016

The above approach would work if we were calculating the age one row at a time.  However, that can become tedious really fast.  We need to perform the calculation for the full range (B3:E7) together, but return the counts for each row individually.

Excel’s **MMULT** function comes to the rescue!

MMULT (which stands for **M**atrix **Mult**iply) multiplies two matrices and returns a third matrix based on rules for matrix multiplication.  I am planning to devote a whole article to explain the MMULT function.  As such, for this article, we will summarize the utility of the function as “take a 2-dimensional array, add each column’s value for each row, and return a 1-column array”.

MMULT requires that its arguments be numeric.

So to obtain the counts for the year 2016, we can use the following:

MMULT(N($B$3:E$7>0),TRANSPOSE(COLUMN($B$3:E$7)^0))

As you can see from the picture below, MMULT’s results are the addition of each column for each row.

[![FF36-TRUE FALSE to1s 0s](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-TRUE-FALSE-to1s-0s.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-TRUE-FALSE-to1s-0s.jpg)

In the above formula, you may have noticed that the range uses absolute and relative referencing (signified by the $ sign or lack thereof).  This is to ensure that the range grows or shrinks as needed.  The upper left address is held constant ($B$3).  However, the lower right address for the range has columns that vary but row that is fixed on row #7.  This ensures that the formula would work if we copy to the left, right, etc. in the final results.

Now that we have the age for each acreage value, we can look up the corresponding yield value using (what else?) LOOKUP function.

But before we can use LOOKUP, we will need to convert the numeric values returned from MMULT into the strings Year1, Year2, etc. found in the Costs table.  Of course, you know how to do that… concatenate the string “Year” to the result from MMULT

“Year”&MMULT(N($B$3:E$7>0),TRANSPOSE(COLUMN($B$3:E$7)^0))

For the 2016 example, we get {“Year4″;”Year3″;”Year2″;”Year1″;”Year0”}

We can now use LOOKUP as follows:

LOOKUP(“Year”&MMULT(N($B$3:E$7>0),TRANSPOSE(COLUMN($B$3:E$7)^0)), $B$11:$I$11, $B12:$I12)

[![FF36-2016 calc](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-2016-calc.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-2016-calc.jpg)

You may recall that LOOKUP looks up a value in the array indicated by the second argument, and returns the corresponding value from the third array argument.  In this case, instead of looking up a single value, we look up an array of values (supplied in the first argument) to the function.

The above formula translates to the following:

LOOKUP({“Year4″;”Year3″;”Year2″;”Year1″;”Year0”}, {“Year1″,”Year2″,”Year3″,”Year4″,”Year5″,”Year6″,”Year7″,”Year8”}, {0,5,10,15,20,25,30,35})

The result from LOOKUP is {15;10;5;0;#N/A}

(The last value is #N/A because there is no acreage value for 2017 yet (as of 2016 column).  The concatenation resulted in Year0 which does not exist in the “Age of The Trees” range (B11:I11) above.)

By using IFERROR(LOOKUP(…),0) we get {15;10;5;0;0}

We can now multiply the above result with the acreage values for 2016 to get {4500;7000;5000;0;0}

Finally, we SUM the values to get 16500

[![FF36-Final Calc](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Final-Calc.jpg)](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Final-Calc.jpg)

Putting it all together, we get the following formula (shown for Production for year 2016)

**\=SUM(IFERROR(LOOKUP(“Year”&MMULT(N($B$3:E$7>0),TRANSPOSE(COLUMN($B$3:E$7)^0)), $B$11:$I$11, $B12:$I12),0)\*E$3:E$7)**

One of the benefits of the above formula is that you can copy the same formula to calculate values for additional years, as well as other plantation costs.

Download
--------

You can download a copy of the above file and follow along: [Download sample file](https://chandoo.org/wp/wp-content/uploads/2013/11/FF36-Calculating-Plantation-Costs.xlsx "Sample File")
.

Let me know (using the comments below) what you think of the above approach and solution, as well as any other approaches you have utilized to solve a similar problem.  In the meantime, I wish you continued _Excel_lence!

\-Sajan.

 Other Posts in this Series
---------------------------

The Formula Forensics Series contains a wealth of useful solutions and information.

Visit the [Formula Forensics Home Page](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")
 to read other articles in this series.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [10 Comments](https://chandoo.org/wp/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [Costs that vary by year](https://chandoo.org/wp/tag/costs-that-vary-by-year/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [lookup](https://chandoo.org/wp/tag/lookup/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MMult()](https://chandoo.org/wp/tag/mmult/)
    , [Variable Costs Calculation](https://chandoo.org/wp/tag/variable-costs-calculation/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Posts by Sajan](https://chandoo.org/wp/category/posts-by-sajan/)
    

[PrevPreviousFind last day of any month with this simple trick \[formulas\]](https://chandoo.org/wp/last-day-of-month-formula/)

[NextAsk me anythingNext](https://chandoo.org/wp/ask-me-anything/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-036-calculating-costs-that-vary-by-year-and-age/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ