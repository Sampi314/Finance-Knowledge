# Required recovery rate - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/required-recovery-rate

---

[Skip to main content](https://exceljet.net/formulas/required-recovery-rate#main-content)

[](https://exceljet.net/formulas/required-recovery-rate#)

*   [Previous](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Next](https://exceljet.net/formulas/simple-investing-worksheet)
    

[Financial](https://exceljet.net/formulas#Financial)

Required recovery rate
======================

by Dave Bruns · Updated 12 May 2024

![Excel formula: Required recovery rate](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/required_recovery_rate.png "Excel formula: Required recovery rate")

Summary
-------

To calculate the required recovery rate or breakeven rate for an investment loss, you can use a simple formula and format the result as a percentage. In the worksheet shown, the formula in cell F5 is:

    =1/(1+C5)-1

Where C5 is the loss in column C is expressed as a negative percentage. The result is the gain needed to recover the initial investment as a percentage. As the formula is copied down, it calculates the required recovery rate for each loss in the table. Notice that larger losses require _much higher_ recovery rates.

Generic formula
---------------

    =1/(1-%loss)-1

Explanation 
------------

In this example, the goal is to calculate the required recovery rate (or gain) to complete offset a loss expressed as a negative percentage. This is not a difficult problem, but you must pay attention to the sign of the loss and be sure to format the result with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

### Background

One of the most important aspects of investing is the math of gains and losses. A 50% loss does not require a 50% gain to recover the loss, it actually requires a _100% gain_. Put simply, as a loss gets larger (as a percentage), the recovery rate (or gain), required to offset the loss _increases at an increasing rate_:

*   A loss of 10% requires a gain of 11.1%
*   A loss of 20% requires a gain of 25%
*   A loss of 50% requires a gain of 100%
*   A loss of 80% requires a gain of 400%

### Formula

With a loss expressed as a percentage, you can calculate the required gain or recovery rate with a formula like this:

    =1/(1-%loss)-1

The formula above assumes the loss is given as a _positive_ percentage. If the loss is given as a _negative_ percentage (as in the worksheet shown), use the modified formula below:

    =1/(1+%loss)-1

In the worksheet shown, the loss percentages are in column C. The formula in F5, copied down, is:

    =1/(1+C5)-1

This formula evaluates like this:

    =1/(1+-0.05)-1
    =1/(0.95)-1
    =1.0526-1
    =0.0526
    =5.3%

The result is a decimal value that should be formatted with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

### Formula check

To check the calculated recovery rate for each loss, the formula in G5, copied down, is:

    =D5*(1+F5)

This formula simply multiples the result in column D by 1 plus the recovery rate. In all cases, it should return the initial value in column B,  proving that the recovery rate will completely offset the loss.

Related formulas
----------------

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

[![Excel formula: Get stock price last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20days.png "Excel formula: Get stock price last n days")](https://exceljet.net/formulas/get-stock-price-last-n-days)

### [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)

In this example, the goal is to retrieve historical stock price information for a given stock, provided as a ticker symbol like "MSFT", "AAPL", "MMM", etc. over the past n days, where n is a variable that can be changed as desired. In addition, the data should be sorted in reverse chronological...

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Estimate mortgage payment](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/estimate_mortgage_payment.png "Excel formula: Estimate mortgage payment")](https://exceljet.net/formulas/estimate-mortgage-payment)

### [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)

In this example, the goal is to calculate a monthly mortgage payment based on three inputs: The loan amount The annual interest rate The loan term in years The worksheet shown also takes into account the down payment, which is calculated using a simple formula in C8 (see below) and then subtracted...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_percentage_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)

### [How to use percentage formatting in Excel](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)

In this lesson we'll look at the Percentage format. The Percentage format is made to display fractional values as percentages. For instance, the value .05, formatted as a percent, will display as 5%. Let's take a look. In column B of our table we have a set of numbers in General format. Let's first...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)
    
*   [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)
    
*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    
*   [Estimate mortgage payment](https://exceljet.net/formulas/estimate-mortgage-payment)
    

### Videos

*   [How to use percentage formatting in Excel](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)
    

### Links

*   [Percentage gain and loss (www.bogleheads.org)](https://www.bogleheads.org/wiki/Percentage_gain_and_loss)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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