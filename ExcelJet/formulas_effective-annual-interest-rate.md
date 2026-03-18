# Effective annual interest rate - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/effective-annual-interest-rate

---

[Skip to main content](https://exceljet.net/formulas/effective-annual-interest-rate#main-content)

[](https://exceljet.net/formulas/effective-annual-interest-rate#)

*   [Previous](https://exceljet.net/formulas/currency-exchange-rate-example)
    
*   [Next](https://exceljet.net/formulas/estimate-mortgage-payment)
    

[Financial](https://exceljet.net/formulas#Financial)

Effective annual interest rate
==============================

by Dave Bruns · Updated 27 Jan 2021

Related functions 
------------------

[EFFECT](https://exceljet.net/functions/effect-function)

[RRI](https://exceljet.net/functions/rri-function)

![Excel formula: Effective annual interest rate](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/effective%20annual%20interest%20rate.png "Excel formula: Effective annual interest rate")

Summary
-------

To calculate the effective annual interest rate, when the nominal rate and compounding periods are given, you can use the EFFECT function. In the example shown, the formula in D5, copied down, is:

    =EFFECT(rate,C5)
    

where "rate" is the [named range](https://exceljet.net/glossary/named-range)
 H4.

Generic formula
---------------

    =EFFECT(rate,periods)

Explanation 
------------

The Effective Annual Rate (EAR) is the interest rate after factoring in compounding. In other words, the EAR is the rate actually earned due to the effect of [compounding more frequently than once a year](https://exceljet.net/formulas/compare-effect-of-compounding-periods)
 (annually).

The [EFFECT function](https://exceljet.net/functions/effect-function)
 calculates the effective annual interest rate based on the nominal annual interest rate, and the number of compounding periods per year.

To demonstrate how this works, the table shown in the example is set up with various compounding periods in column C. The nominal interest rate is provided in cell H4, which is the [named range](https://exceljet.net/glossary/named-range)
 "rate".

The formula in D5 is:

    =EFFECT(rate,C5)
    

Because named ranges behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
, this formula can simply be copied down the table. The EFFECT function returns the calculated EAR for each of the given periods.

### Manual check

The generic formula for calculating EAR (in Excel formula syntax) is:

    =(1+i/n)^n–1
    

where **n** stands for periods, and _i_ is the stated interest rate. This formula is used to check the results from EFFECT. In E5, the formula is:

    =(1+rate/C5)^C5-1
    

When this formula is copied down the table, the results in columns D and E match:

![Effective annual interest rate - manual check](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/effective%20annual%20interest%20rate%20manual%20check.png?itok=N0JrXrFP "Effective annual interest rate - manual check")

Related formulas
----------------

[![Excel formula: Calculate compound interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20compound%20interest.png "Excel formula: Calculate compound interest")](https://exceljet.net/formulas/calculate-compound-interest)

### [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)

Compound interest is a financial concept that describes how an initial investment grows over time, taking into account not only the interest earned on the initial amount but also the interest earned on the interest itself. Compound interest allows your money to grow exponentially, which makes it a...

[![Excel formula: Calculate simple interest](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20%20simple%20interest.png "Excel formula: Calculate simple interest")](https://exceljet.net/formulas/calculate-simple-interest)

### [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)

The general formula for simple interest is: interest=principal\*rate\*term So, using cell references, we have: =C5\*C7\*C6 =1000\*10\*0.05 =500

[![Excel formula: Annual compound interest schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/annual%20compound%20interest%20schedule.png "Excel formula: Annual compound interest schedule")](https://exceljet.net/formulas/annual-compound-interest-schedule)

### [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)

If you have an annual interest rate, and a starting balance you can calculate interest with: =balance \* rate and the ending balance with: =balance+(balance\*rate) So, for each period in the example, we use this formula copied down the table: =C5+(C5\*rate) With the FV function The FV function can...

[![Excel formula: Compare effect of compounding periods](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/compare%20compounding%20periods.png "Excel formula: Compare effect of compounding periods")](https://exceljet.net/formulas/compare-effect-of-compounding-periods)

### [Compare effect of compounding periods](https://exceljet.net/formulas/compare-effect-of-compounding-periods)

The FV function calculates compound interest and returns the future value of an investment over a specified term. To configure the function, we need to provide a rate, the number of periods, the periodic payment, and the present value: Present value ( pv ) is the named range G4 Rate is provided as...

Related functions
-----------------

[![Excel EFFECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_effect_function.png "Excel EFFECT function")](https://exceljet.net/functions/effect-function)

### [EFFECT Function](https://exceljet.net/functions/effect-function)

The Excel EFFECT function returns the effective annual interest rate, given a nominal interest rate and the number of compounding periods per year. Effective annual interest rate is the interest rate actually earned due to compounding. 

[![Excel RRI function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_rri_function.png "Excel RRI function")](https://exceljet.net/functions/rri-function)

### [RRI Function](https://exceljet.net/functions/rri-function)

The Excel RRI function returns an equivalent interest rate for the growth of an investment. You can use RRI to calculate Compound Annual Growth Rate (CAGR) in Excel.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate compound interest](https://exceljet.net/formulas/calculate-compound-interest)
    
*   [Calculate simple interest](https://exceljet.net/formulas/calculate-simple-interest)
    
*   [Annual compound interest schedule](https://exceljet.net/formulas/annual-compound-interest-schedule)
    
*   [Compare effect of compounding periods](https://exceljet.net/formulas/compare-effect-of-compounding-periods)
    

### Functions

*   [EFFECT Function](https://exceljet.net/functions/effect-function)
    
*   [RRI Function](https://exceljet.net/functions/rri-function)
    

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