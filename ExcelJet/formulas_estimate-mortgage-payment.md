# Estimate mortgage payment - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/estimate-mortgage-payment

---

[Skip to main content](https://exceljet.net/formulas/estimate-mortgage-payment#main-content)

[](https://exceljet.net/formulas/estimate-mortgage-payment#)

*   [Previous](https://exceljet.net/formulas/effective-annual-interest-rate)
    
*   [Next](https://exceljet.net/formulas/future-value-of-annuity)
    

[Financial](https://exceljet.net/formulas#Financial)

Estimate mortgage payment
=========================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[PMT](https://exceljet.net/functions/pmt-function)

[PV](https://exceljet.net/functions/pv-function)

[FV](https://exceljet.net/functions/fv-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8044/download?token=YeZX3GL5)
 (13.43 KB)

![Excel formula: Estimate mortgage payment](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/estimate_mortgage_payment.png "Excel formula: Estimate mortgage payment")

Summary
-------

To calculate an estimated mortgage payment in Excel with a formula, you can use the [PMT function](https://exceljet.net/functions/pmt-function)
. In the example shown, the formula in C11 is:

    =PMT(C5/12,C6*12,-C9)
    

With the inputs in the worksheet as shown, the PMT function determines a monthly payment of 2,994. This is the calculated monthly payment for a 30-year mortgage with an interest rate of 7% and a loan amount of $450,000. If any of the assumptions in column C are changed, the payment will recalculate automatically.

_Note: also see this [formula to calculate a mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)
._

Generic formula
---------------

    =PMT(rate/12,term*12,-principal)

Explanation 
------------

In this example, the goal is to calculate a monthly mortgage payment based on three inputs:

1.  The loan amount
2.  The annual interest rate
3.  The loan term in years

The worksheet shown also takes into account the down payment, which is calculated using a simple formula in C8 (see below) and then subtracted from the cost in cell C4. The mortgage payment is then calculated based on the loan amount in cell C9. 

> This simplified example ignores property taxes, homeowner's insurance, mortgage insurance, and other fees.

### Mortgages and interest calculations

A mortgage is a type of loan specifically used to purchase real estate. In a mortgage agreement, the buyer borrows money from a lender to buy a home and repays the loan over a long period of time. Here are the main components:

*   **Principal** _-_ The total loan amount, after any down payment.
*   **Interest** - The cost of borrowing money. The lender charges a percentage of the principal amount as interest. This interest is usually compounded on a monthly basis for mortgages over the entire term.
*   **Term** -  This is the number of years you have to pay back the loan. Common terms for mortgages are 15, 20, or 30 years.

The monthly mortgage payment is made up of both the principal and the interest. Over time, a larger portion of the monthly payment goes toward reducing the loan balance (or principal), and a smaller portion goes toward paying interest.

### The PMT function in Excel

The [PMT function](https://exceljet.net/functions/pmt-function)
 in Excel calculates the monthly payment for a loan, given the loan amount, interest rate, and repayment time. The PMT function assumes fixed periodic payments and a constant interest rate. The full generic syntax for PMT looks like this

    =PMT(rate,nper,pv,[fv],[type])

Each argument has the following meaning:

*   _rate_: The interest rate for the loan.
*   _nper_: The total number of payment periods for the loan.
*   _pv_: The principal amount of the loan.
*   _fv_ (optional): The cash balance desired after the last payment is made. Defaults to 0.
*   _type_ (optional): When payments are due (0 = end of period, 1 = beginning of period). Defaults to 0.

Although the PMT function takes five arguments total, we only need the first three arguments (_rate_, _nper_, and _pv_) to estimate the mortgage payment in this example.

### Example

You can use the PMT function to calculate the payment for a mortgage by providing the interest rate, the term, and the loan amount. In the example shown, the formula in cell C11 is:

    =PMT(C5/12,C6*12,-C9)

The arguments are provided to PMT as follows:

*   _rate_ = C5/12 (7%/12)
*   _nper_ = C6\*12 (30\*12)
*   _pv_ = -C9 (-450000)

Because mortgage rates are annual, and terms are stated in years, the arguments for the rate and periods are carefully set up to normalize inputs to monthly periods. To get the _rate_ (which is the period rate), we divide the annual rate (7%) by the compounding periods per year (12). To get the number of periods (_nper_), we multiply the term in years (30) by the periods per term (12). To get a value for _pv_ (the present value), we use -C9, which converts the loan amount to -450,000. We use a minus operator to make this value negative, since a loan represents money owed, and is a cash outflow. Putting it all together, Excel evaluates the formula like this:

    =PMT(C5/12,C6*12,-C9)
    =PMT(0.07/12,30*12,-450000)
    =PMT(0.005833,360,-450000)
    =2994

The PMT function returns 2,994. This is the calculated monthly payment for a 30-year mortgage with an interest rate of 7% and a loan amount of $450,000.

> _Note: When using PMT, always be consistent with the units provided for rate and periods. For a mortgage, you typically need to divide the annual interest rate by 12 to get a period rate and multiply the term by 12 to get the total number of periods._

### Other worksheet formulas

The worksheet shown contains two other formulas. In the first formula, the down payment amount in C8 is calculated like this:

    =C4*C7
    

This formula multiples the cost in C4 by the down payment percentage in C7. With $500,000 in cell C4 and 10% in cell C7, the down payment is calculated to be $50,000. In the second formula, the loan amount in C9 is calculated like this:

    =C4-C8
    

This formula subtracts the down payment in C8 from the cost in C4 to determine a loan amount. With $500,000 in cell C4 and $50,000 in C8, the result in C9 is $450,000.

> Note: the interest rate in C5 and the down payment percentage in C7 are decimal values formatted with Excel's [percentage number format](https://exceljet.net/glossary/percentage-number-format)
> .

Related formulas
----------------

[![Excel formula: Mortgage payment schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/mortgage_schedule_with_extra_payment.png "Excel formula: Mortgage payment schedule")](https://exceljet.net/formulas/mortgage-payment-schedule)

### [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)

The goal of this example is to show how to create a mortgage payment schedule using Excel formulas. A mortgage payment schedule is a detailed breakdown of every payment over the life of a loan. Each payment represents one period , typically a month. For each period, the schedule shows how much of...

[![Excel formula: Payment for annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annuity%20payment%20amount.png "Excel formula: Payment for annuity")](https://exceljet.net/formulas/payment-for-annuity)

### [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)

The PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate. An annuity is a series of equal cash flows, spaced equally in time. The goal in this...

[![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")](https://exceljet.net/formulas/future-value-of-annuity)

### [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)

The FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time. In...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

[![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")](https://exceljet.net/formulas/present-value-of-annuity)

### [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)

The PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows,...

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

Related functions
-----------------

[![Excel PMT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pmt.png "Excel PMT function")](https://exceljet.net/functions/pmt-function)

### [PMT Function](https://exceljet.net/functions/pmt-function)

The Excel PMT function is a financial function that returns the periodic payment for a loan. You can use the PMT function to figure out payments for a loan, given the loan amount, number of periods, and interest rate.

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel FV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fv.png "Excel FV function")](https://exceljet.net/functions/fv-function)

### [FV Function](https://exceljet.net/functions/fv-function)

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)
    
*   [Payment for annuity](https://exceljet.net/formulas/payment-for-annuity)
    
*   [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)
    
*   [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)
    
*   [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    

### Functions

*   [PMT Function](https://exceljet.net/functions/pmt-function)
    
*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [FV Function](https://exceljet.net/functions/fv-function)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)