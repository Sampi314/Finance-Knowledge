# Compound Interest Formula in Excel with Examples

**Source:** https://chandoo.org/wp/compound-interest-formula-in-excel

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Compound Interest Formula in Excel
==================================

*   Last updated on April 2, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Compound interest is defined as “the interest on savings calculated on both the initial principal and the accumulated interest from previous periods.” Classically, known as “interest on interest”, this is the most common type interest used in every day finance situations. 

To calculate compound interest

*   on principal amount **P**
*   at the rate of interest **R**
*   for the number of years **N**
*   and compounded **T** times per year
*   we can use the formula = P\*(1+R/T)^(N\*T)

In this article, let me explain the necessary Excel formulas to calculate compound interest using your data.

![Compound Interest Excel Formula](https://chandoo.org/wp/wp-content/uploads/2024/01/SNAG-3140.png)

#### In this Article

Compound Interest Excel Formula
-------------------------------

Let’s say you borrow $5,000 at 5% interest rate for 10 years. The compounded value at the end of 10 years can be calculated with below Excel formula.

*   Cell D4 has principal value: $5000
*   Cell D5 has interest rate: 5%
*   Cell D6 has years: 10

![compound interest excel formula](https://chandoo.org/wp/wp-content/uploads/2024/01/compound-interest-excel-formula.png)

				
					`=D4*(1+D5)^D6`
				
			

We can also calculate just the interest portion with this formula:

				
					`=D4*(1+D5)^D6 - D4`
				
			

Compounding Once per Month  
or 'T' Times per Year
--------------------------------------------------

It is common for compounding to be done more than once per year. In such cases, you can use below Excel formula logic to calculate the compound interest.

Below example shows compounding 4 times per year (ie, once every quarter).

![compounding every quarter - excel formula](https://chandoo.org/wp/wp-content/uploads/2024/01/compounding-every-quarter-excel-formula.png)

				
					`' D20 has Principal Amount ' D21 has Rate of Interest ' D23 has number of years ' D24 has compounding terms per years  =D20*(1+D21/D23)^(D22*D23)`
				
			

Compounding Every 'x' Months
----------------------------

If you want to calculate the effect of compounding every ‘x’ months, you can just below logic.

![compound interest formul with compounding every n months](https://chandoo.org/wp/wp-content/uploads/2024/01/compound-interest-formul-with-compounding-every-n-months.png)

				
					`' D34 has Principal Amount ' D35 has Rate of Interest ' D36 has number of years ' D37 has number of months per compounding  =D34*(1+D35*D37/12)^(D36*12/D37)`
				
			

Calculating Compound Interest with FV Function
----------------------------------------------

Instead of using the P\*(1+R/T)^(N\*T) formula, you can use the FV () function (Future Value) to calculate the compounded value over time.

Here are a few examples:

### $5000, 5%, 10 years, compounding once per year

				
					`'FV Syntax: FV(Interest Rate per term, Number of terms, , Principal Amount)  =FV(5%, 10,, -5000)  Output: $8144.47`
				
			

### $5000, 5%, 10 years, compounding 4 times per year

				
					`=FV(5%/4, 10*4,, -5000)  Output: $8218.10`
				
			

### $5000, 5%, 10 years, compounding x times per year

				
					`'Cell A1 has the Compounding Terms x  =FV(5%/A1, 10*A1,, -5000)`

				
			

Compound vs. Simple Interest
----------------------------

Simple interest is defined as Principal x Interest Rate. It doesn’t change over time.

On the other hand, Compound Interest changes over time, as we calculate _interest ON interest too._

Here is a quick demo of how Simple & Compound Interests compare over 20 years time, for $5,000 borrowed at 5% rate of interest.

				
					`'SIMPLE INTEREST FORMULA  =Principal * Rate_of_INTEREST  'COMPOUND INTEREST FORMULA  =Principal * (1 + Rate_of_INTEREST)^number_of_YEARS`
				
			

![simple vs. compound interest comparison](https://chandoo.org/wp/wp-content/uploads/2024/01/simple-vs.-compound-interest-comparison.png)

Compounding Effect
------------------

![Massive effect of compounding!!!](https://chandoo.org/wp/wp-content/uploads/2024/01/SNAG-3150.png)

**“Compounding Effect”** or that rapid growth of money over time often surprises people.

Imagine investing $5,000 at 5%, compounded annually  for 20 years. Below table shows the effect of compounding on your money.

![effect of compounding over time](https://chandoo.org/wp/wp-content/uploads/2024/01/effect-of-compounding-over-time.png)

To calculate compounded value for various years, we can use below formulas.

				
					`'LIST OF 20 YEARS  =SEQUENCE(20)  'COMPOUNDED VALUE AT THE END OF EACH YEAR 'Amount is $5000, Rate of interest is 5%  =5000 * (1+5%)^SEQUENCE(20)`
				
			

The compounding effect is starkly visible in the below graph.

![compounding effect in Excel Chart](https://chandoo.org/wp/wp-content/uploads/2024/01/compounding-effect-visualized.png)

Effect of Frequency on Compounding
----------------------------------

You might think how often we compound would have an impact on the final value. But it does little. 

For example, if we compare the outputs of  $5,000 compounded at 5% at various frequencies, at the end of 20 years, the values would be:

*   Once a year compounding: $13,266.49
*   Twice a year: $13,452.32
*   4 Times a year: 13,507.42
*   6 Times a year: $13,535.21
*   Every month (12 times): $13,563.20
*   Every week (52 times): $13,584.88
*   Every day (365 times): $13,590.48

The value hardly changes.

Below table shows how this looks over various time periods.

![compounding vs. number of terms](https://chandoo.org/wp/wp-content/uploads/2024/01/compounding-vs.-number-of-terms.png)

Interest Rate vs. Compounding
-----------------------------

Interest rate on the other hand has a dramatic effect on the result of compounding. 

For example, $5000 invested at 8% will be almost $11 million in a century!

> Compounding is CRAZY!!!  
> $5,000 invested today at 1% interest would be worth $13,500 in 100 years.  
> Same money, but invested at 8% would be a whopping $10.9 million!
> 
> [Tweet](https://twitter.com/intent/tweet?text=Compounding+is+CRAZY%21%21%21%3Cbr%2F%3E%0A%245%2C000+invested+today+at+1%25+interest+would+be+worth+%2413%2C500+in+100+years.%3Cbr%2F%3E%0ASame+money%2C+but+invested+at+8%25+would+be+a+whopping+%2410.9+million%21&url=https%3A%2F%2Fchandoo.org%2Fwp%2Fwp%2Fcompound-interest-formula-in-excel%2F&via=r1c1)

We can see the dramatic impact of rising interest rates on the compounded value with this table.

![compounding at various rates of interest](https://chandoo.org/wp/wp-content/uploads/2024/01/compouding-at-various-rates-of-interest.png)

				
					`'Compounded value at various interest rates  'List of interest rates upto 20% =SEQUENCE(20)/100  'COMPOUNDED VALUE AT VARIOUS RATES 'Amount is $5000, Duration is 20 years 'Compounded once per year  =5000 * (1+SEQUENCE(20)/100) ^ 20`
				
			

### Interest Rate vs. Compounding Graph

![Compounding vs. Rate of interest illustration](https://chandoo.org/wp/wp-content/uploads/2024/01/Compounding-vs.-Rate-of-interest-illustration.png)

Effect of Compounding with Regular Payments
-------------------------------------------

We can use Excel to figure out the compounded value with regular payments easily.

For example, if you invest

*   $500 every month
*   at 8%
*   for 20 years

the final amount will be $294,510.21

To calculate this you can use the FV function, as shown below:

				
					`'FV Function Syntax  =FV(INTEREST_RATE, NUMBER_OF_PAYMENTS, PAYMENT_AMOUNT)  'Example with $500 monthly payment for 20 years at 8%  =FV(8%/12, 20 * 12, 500)  'OUTPUT  =$294,510.21`
				
			

Here you can see the calculations and yearly balances for such regular (monthly) investments.

![compounding value of regular payments](https://chandoo.org/wp/wp-content/uploads/2024/01/compounding-value-of-regular-payments.png)

Rule of 72: Time to Double
--------------------------

A common thumb rule used in compounding is **rule of 72.** 

> **RULE OF 72**  
> To find out how long it takes for your money to double, divide 72 with rate of interest.  
> For example, at 8% interest rate, your money will double in 72/8 = 9 years.
> 
> [Tweet](https://twitter.com/intent/tweet?text=%3CSTRONG%3ERULE+OF+72%3C%2FSTRONG%3E%3CBR%2F%3E%0ATo+find+out+how+long+it+takes+for+your+money+to+double%2C+divide+72+with+rate+of+interest.+%3Cbr%2F%3EFor+example%2C+at+8%25+interest+rate%2C+your+money+will+double+in+72%2F8+%3D+9+years.&url=https%3A%2F%2Fchandoo.org%2Fwp%2Fwp%2Fcompound-interest-formula-in-excel%2F&via=r1c1)

You can use this when you don’t have the luxury of Excel or a calculator nearby to quickly calculate how long it takes for your money to double.

### But what if I want to calculate the EXACT time it takes?

In such cases, you can use the formula =LOG(2) / LOG(1+Rate of Interest).

				
					`'Time to Double 'Exact formula  =LOG(2) / LOG(1+Rate_of_Interest)  'Approximate formula  =72/(Rate_of_Interest*100)   'Example at 8%  =LOG(2) / LOG(1+8%) =9.01  =72 / (8% *100) =9`

				
			

In below example, you can see the rapid decrease in time it takes to double as the interest rate (rate of return) goes up.

![time to double your money](https://chandoo.org/wp/wp-content/uploads/2024/01/time-to-double-your-money.png)

Reverse of Compounding - The PV Function
----------------------------------------

We can use the PV (Present Value) function in Excel to calculate the principal value, given a compounded value.

For example, you want to save $100,000 for your daughter’s wedding, which you expect to be in 20 years. You expect the rate of interest to be 5%.

You want to know how much to save now to get $100k after 20 years.

Using the PV function as below, we can get that result.

				
					`'Reverse of Compounding 'Using PV Function to calculat the initial amount  'FUTURE AMOUNT = $100,000 'INTEREST RATE = 5% 'DURATION = 20 YEARS 'COMPOUNDING ANNUALLY  =PV(5%, 20,,-100,000)  =$37,688.95`
				
			

![Using PV function to calculate the reverse of Compounding](https://chandoo.org/wp/wp-content/uploads/2024/01/SNAG-3151-1.png)

Reverse of Regular Compounding - PMT Function
---------------------------------------------

And we can use the PMT function to calculate reverse of the regular compounding.

Going back to the “saving for daughter’s wedding” case, you want to save up $100k for your daughter’s wedding in 20 years. You expect the interest rate to be 5%.

How much should you save every year?

or every month?

We can use the PMT function to figure out the regular amounts.

![Regular payments needed to reach a compounded value at the end](https://chandoo.org/wp/wp-content/uploads/2024/01/SNAG-3153.png)

				
					`'Reverse of Compounding with Regular Payments 'Using PMT Function to calculat the regular payments from end value  'FUTURE AMOUNT = $100,000 'INTEREST RATE = 5% 'DURATION = 20 YEARS 'COMPOUNDING ANNUALLY  =PMT(5%, 20,,, -100000)  =$3,024.26`
				
			

Compound Interest in Excel - VIDEO
----------------------------------

Need to understand these formulas better? 

Check out my quick and to-the-point [video on Calculating Compound Interest in Excel](https://youtu.be/HnkT-Ol1FWY)
. 

Example Workbook with Compound Interest Calculations
----------------------------------------------------

I made an Excel file with over 20 examples (and more than 100 formulas). [**Click here to download the file**](https://chandoo.org/wp/wp-content/uploads/2024/01/compound-interest-formula-excel-demo.xlsx)
 and learn the concepts better.

Learn More Finance & Accounting Concepts
----------------------------------------

Check out below articles to learn more useful Accounting & Finance concepts with related Excel formulas.

[](https://chandoo.org/wp/top-10-accounting-kpis-excel/)

![top-10-accounting-kpis and how to calculate them with Excel](https://chandoo.org/wp/wp-content/uploads/2023/08/top-10-accounting-kpis.jpg)

We can calculate any Finance & Accounting KPI values using...

[Read More](https://chandoo.org/wp/top-10-accounting-kpis-excel/)

[](https://chandoo.org/wp/mortgage-calculator-with-extra-payments-excel-download/)

![Impact of Extra payments on mortgage](https://chandoo.org/wp/wp-content/uploads/2022/09/SNAG-2284.png)

Recently, we got a new mortgage. And I wanted to...

[Read More](https://chandoo.org/wp/mortgage-calculator-with-extra-payments-excel-download/)

Lets talk about how we can use Excel to calculate...

[Read More](https://chandoo.org/wp/calculate-cagr-using-excel/)

Offset() function to Calculate IRR for Dynamic Range When you...

[Read More](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/)

Today, let us learn how to use NPV() function in...

[Read More](https://chandoo.org/wp/using-npv-in-excel/)

Load More

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/compound-interest-formula-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/compound-interest-formula-in-excel/#respond)
    
*   Tagged under [compound interest](https://chandoo.org/wp/tag/compound-interest/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [finance](https://chandoo.org/wp/tag/finance/)
    , [FV](https://chandoo.org/wp/tag/fv/)
    , [goal seek](https://chandoo.org/wp/tag/goal-seek/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pmt](https://chandoo.org/wp/tag/pmt-2/)
    , [pv](https://chandoo.org/wp/tag/pv/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow to convert test scores to letter grades in Excel?](https://chandoo.org/wp/how-to-convert-test-scores-to-letter-grades-in-excel/)

[NextAnnouncing Power BI Dashboard Contest (win $500 prizes!)Next](https://chandoo.org/wp/announcing-power-bi-dashboard-contest/)

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
    
    [Reply](https://chandoo.org/wp/compound-interest-formula-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/compound-interest-formula-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/compound-interest-formula-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ