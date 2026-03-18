# Loan Amortization Schedule in Excel - FREE Template » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/loan-amortization-schedule-in-excel

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Loan Amortization Schedule in Excel – FREE Template
===================================================

*   Last updated on February 20, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you want to calculate _**loan amortization schedule in Excel****?**_ We can use PMT & SEQUENCE functions to quickly and efficiently generate the full loan amortization table for any number of years.

[![Loan Amortization Schedule in Excel](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3178.png)](https://chandoo.org/wp/loan-amortization-schedule-in-excel/#download-template)

Set up input section for loan amortization table
------------------------------------------------

First, you need to set up the parameters for calculating loan schedule. We need below information.

![Inputs for loan amortization schedule in Excel](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3179.png)

*   Interest Rate (annualized)
*   Loan duration (in years)
*   Payments per year (for ex: 12 for monthly, 52 for weekly and 26 for fortnightly)
*   Loan amount

For the sake of the example on this page, I am using 5.35% annual interest rate (cell D3), 30 years loan duration (cell D4), 12 payments per year (cell D5) and $100,000 loan amount (cell D6).

Write formulas to calculate the amortization schedule
-----------------------------------------------------

Then, we need to calculate the amortization schedule or table. For this we can use the [PMT](https://chandoo.org/excel-formulas/pmt.shtml)
, IPMT, PPMT functions along with [**_SEQUENCE dynamic array_** **_function_**](https://chandoo.org/wp/dynamic-array-functions/#elementor-toc__heading-anchor-7)
**_._**

### Setting up the amortization schedule in Excel Grid

First create a range of cells like below to do all the calculations.

![amortization table structure](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3183.png)

### Formula for generating all payment periods

To generate all payment periods, we can use the SEQUENCE function below.

For example, if you have 12 payments per year for 30 years, then the sequence function below generates numbers 1 thru 360.

				
					`=SEQUENCE(D5*D4)`
				
			

![Using SEQUENCE function to generate all payment periods for amortization schedule](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3184.png)

### Calculating the equal payments for each period

We can use PMT function to calculate the equated payment or installment amounts.

The syntax for PMT function is

    =PMT(rate_of_interest, 

    amount_borrowed)

In our case, as we have **_12 payments per year,_** we need to divide the interest rate by 12 and multiply the number of years with 12. Finally, we want the same amount for all the periods. So our PMT formula will be:

				
					`=IF(C10#>0,     PMT($D$3/D5,D4*D5,D6))`
				
			

![PMT formula to calculate the equal payment for each period](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3185.png)

### Calculating the Principal portion  
of each payment in the amortization schedule

We can use **PPMT function** to calculate the principal paid at each point of time. The syntax for this is…

    =PPMT(
      rate_of_interest, 
      payment_number
      total_number_of_payments,
      amount_borrowed)

As we need to calculate this value for all the periods, we can use the SPILL RANGE in C10# as the **_payment\_number._**

Our PPMT formula looks like this:

				
					`=PPMT(D3/D5,C10#,D4*D5,D6)`

				
			

![Using PPMT function to calculate principal portion in amortization schedule](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3182.png)

### Formula for Interest portion for each payment in amortization schedule

We can **use IPMT function** to calculate the interest portion in our schedule. The syntax and logic are same as PPMT.

Here is the IPMT formula to use:

				
					`=IPMT(D3/D5,C10#,D4*D5,D6)`
				
			

    

### Formula for Balance at the end of each period

The final formula in our amortization schedule is balance. For this, we can use a variety of Excel formulas. **_I particularly like using SCAN function for this_** as this is simple and automatically scales up or down depending on how many payments we make.

Know more about SCAN function in Excel

SCAN is a new Excel 365 function that scans a list or array and runs a calculations on it. Then it returns the results the values for each step of the calculation.

**Example of SCAN:**

\=SCAN(0, A1:A10, SUM)

**Result:**  
Returns the running total of the values in A1:A10

**Explanation:**

*   SCAN starts the calculation with 0.
*   Then it reads the values of A1:A10, one at a time.
*   It then adds the values to 0 (because the third argument is SUM) and returns the intermediate results.
*   So, the results will become:
    *   First value: 0+A1
    *   Second value: first value + A2
    *   Third value: second value + A3…

Learn more about **[SCAN function here](https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29?ns=excel&version=90&ui=en-us&rs=en-us&ad=us)
**.

We can use below SCAN function to get the balance at the end of each payment in our amortization table.

				
					`=SCAN(D6,E10#,SUM)`
				
			

This function will start the calculations with D6 (amount borrowed) and scans thru the principal paid column (E10#) and calculates the running total of balance by using the SUM function.

![Using SCAN function to calculate dynamic running total of the loan balance](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3181.png)

Calculating SUMMARY of Amortization Table
-----------------------------------------

Often, you may want to calculate the summary from an amortization table like below:

![Summary calculations are helpful to understand the totals in amortization schedule and impact of various terms and interest rates.](https://chandoo.org/wp/wp-content/uploads/2024/02/SNAG-3186.png)

We can use simple arithmetic formulas like SUM or division (/) to calculate such values.

As you can see, with a 30 year payment of $100,000 loan at 5.35% interest rate, more than half of the payments (50.26%) go towards interest.

Limitations of Amortization Schedules
-------------------------------------

While amortization schedules are great to understand and model cashflows (or plan for future payments), they are quite rigid and do not reflect real-world scenarios. Here are a few limitations of this approach.

*   Amortization tables assume interest rates stay same for the entire duration.
*   They do not cater for excess payment. If you want to prepare an amortization or **[loan schedule with excess payments, use this template](https://chandoo.org/wp/mortgage-calculator-with-extra-payments-excel-download/)
    **.
*   The calculation does not consider any fixed or recurring fees or charges (such as loan administration charge once a year).

Download Loan Amortization Schedule Excel Template
--------------------------------------------------

**[Please download my loan amortization schedule template](https://chandoo.org/wp/wp-content/uploads/2024/02/amortization-schedule-template-v1.xlsx)
** and use it to see the schedule for your data.

If you have an older version of Excel (other than 365), use the “non-365” worksheet to run the calculations.

Other Loan Calculators & Schedules
----------------------------------

[![impact of excess payments on mortgage - with amortization schedule](https://chandoo.org/wp/wp-content/uploads/2022/09/mortgage-calculator-with-extra-payments-demo.gif)](https://chandoo.org/wp/mortgage-calculator-with-extra-payments-excel-download/)

*   If you want to test impact of excess payments on the amortization, try my [loan schedule with excess payments calculator](https://chandoo.org/wp/mortgage-calculator-with-extra-payments-excel-download/)
    .
*   Not sure how much you can borrow? See my [Interactive Mortgage Calculator with Excel](https://chandoo.org/wp/mortgage-payment-calculator/)
     form-controls.

[![Using form controls in Excel to see the impact on monthly payment for various rates, terms and amounts borrowed.](https://chandoo.org/img/c/mortgage-payment-calculator.gif)](https://chandoo.org/wp/mortgage-payment-calculator/)

Have a question about Amortization Schedule Template?
-----------------------------------------------------

Leave a comment with your question so I can help you.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/loan-amortization-schedule-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/loan-amortization-schedule-in-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic array formulas](https://chandoo.org/wp/tag/dynamic-array-formulas/)
    , [excel](https://chandoo.org/wp/tag/excel-2/)
    , [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)
    , [ipmt](https://chandoo.org/wp/tag/ipmt-2/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [pmt](https://chandoo.org/wp/tag/pmt-2/)
    , [ppmt](https://chandoo.org/wp/tag/ppmt-2/)
    , [scan](https://chandoo.org/wp/tag/scan/)
    , [sequence](https://chandoo.org/wp/tag/sequence/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHow-to create Dependent Drop Downs in Excel \[Dynamic & Multiple\]](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/)

[NextHow to fix SPILL Error in Excel Tables (3 easy solutions)Next](https://chandoo.org/wp/how-to-fix-spill-error-in-excel-tables/)

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
    
    [Reply](https://chandoo.org/wp/loan-amortization-schedule-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/loan-amortization-schedule-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/loan-amortization-schedule-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ