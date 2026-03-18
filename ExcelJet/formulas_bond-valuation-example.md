# Bond valuation example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/bond-valuation-example

---

[Skip to main content](https://exceljet.net/formulas/bond-valuation-example#main-content)

[](https://exceljet.net/formulas/bond-valuation-example#)

*   [Previous](https://exceljet.net/formulas/annuity-solve-for-interest-rate)
    
*   [Next](https://exceljet.net/formulas/cagr-formula-examples)
    

[Financial](https://exceljet.net/formulas#Financial)

Bond valuation example
======================

by Dave Bruns · Updated 5 Feb 2019

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[FV](https://exceljet.net/functions/fv-function)

[PRICE](https://exceljet.net/functions/price-function)

![Excel formula: Bond valuation example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Bond%20valuation%20example.png "Excel formula: Bond valuation example")

Summary
-------

To calculate the value of a bond on the issue date, you can use the PV function. In the example shown, the formula in C10 is:

    =-PV(C6/C8,C7*C8,C5/C8*C4,C4)
    

_Note: This example assumes that today is the issue date, so the next payment will occur in exactly six months. See note below on finding the value of a bond on any date._

Explanation 
------------

In the example shown, we have a 3-year bond with a face value of $1,000. The coupon rate is 7% so the bond will pay 7% of the $1,000 face value in interest every year, or $70. However, because interest is paid semiannually in two equal payments, there will be 6 coupon payments of $35 each. The $1,000 will be returned at maturity. Finally, the required rate of return (discount rate) is assumed to be 8%.

The value of an asset is the present value of its cash flows. In this example we use the PV function to calculate the present value of the 6 equal payments plus the $1000 repayment that occurs when the bond reaches maturity. The PV function is configured as follows:

    =-PV(C6/C8,C7*C8,C5/C8*C4,C4)
    

The arguments provided to PV are as follows:

**rate** - C6/C8 = 8%/2 = 4%

**nper** - C7\*C8 = 3\*2 = 6

**pmt** - C5/C8\*C4 = 7%/2\*1000 = 35

**fv** - 1000

The PV function returns -973.79. To get positive dollars, we use a negative sign before the PV function to get final result of $973.79

### Between coupon payment dates

In the example above, it is relatively straightforward to find the value of a bond on a coupon payment date with the PV function. Finding the value of a bond between coupon payment dates is more complex because interest does not compound between payments. The [PRICE function](https://exceljet.net/functions/price-function)
 can be used to calculate the "clean price" of a bond on any date.

### More detail

For a more detailed explanation of bond valuation, [see this article](http://www.tvmcalcs.com/calculators/apps/excel_bond_valuation)
 on [tvmcalcs.com](http://www.tvmcalcs.com/)
.

Related formulas
----------------

[![Excel formula: Present value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/present%20value%20of%20annuity.png "Excel formula: Present value of annuity")](https://exceljet.net/formulas/present-value-of-annuity)

### [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)

The PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate. An annuity is a series of equal cash flows,...

[![Excel formula: Future value of annuity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20of%20annuity.png "Excel formula: Future value of annuity")](https://exceljet.net/formulas/future-value-of-annuity)

### [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)

The FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate. An annuity is a series of equal cash flows, spaced equally in time. In...

[![Excel formula: Future value vs. Present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/future%20value%20vs%20present%20value%20arrows.png "Excel formula: Future value vs. Present value")](https://exceljet.net/formulas/future-value-vs.-present-value)

### [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)

The FV function is a financial function that returns the future value of an investment, given periodic, constant payments with a constant interest rate. The PV function returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future...

Related functions
-----------------

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel FV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fv.png "Excel FV function")](https://exceljet.net/functions/fv-function)

### [FV Function](https://exceljet.net/functions/fv-function)

The Excel FV function is a financial function that returns the future value of an investment. You can use the FV function to get the future value of an investment assuming periodic, constant payments with a constant interest rate.

[![Excel PRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_price_function.png "Excel PRICE function")](https://exceljet.net/functions/price-function)

### [PRICE Function](https://exceljet.net/functions/price-function)

The Excel PRICE function returns the price per $100 face value of a security that pays periodic interest.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Present value of annuity](https://exceljet.net/formulas/present-value-of-annuity)
    
*   [Future value of annuity](https://exceljet.net/formulas/future-value-of-annuity)
    
*   [Future value vs. Present value](https://exceljet.net/formulas/future-value-vs.-present-value)
    

### Functions

*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [FV Function](https://exceljet.net/functions/fv-function)
    
*   [PRICE Function](https://exceljet.net/functions/price-function)
    

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