# Excel XNPV function | Exceljet

**Source:** https://exceljet.net/functions/xnpv-function

---

[Skip to main content](https://exceljet.net/functions/xnpv-function#main-content)

[](https://exceljet.net/functions/xnpv-function#)

*   [Previous](https://exceljet.net/functions/xirr-function)
    
*   [Next](https://exceljet.net/functions/yield-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

XNPV Function
=============

by Dave Bruns · Updated 7 Nov 2021

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[IRR](https://exceljet.net/functions/irr-function)

[XIRR](https://exceljet.net/functions/xirr-function)

![Excel XNPV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_xnpv.png "Excel XNPV function")

Summary
-------

The Excel XNPV function is a financial function that calculates the net present value (NPV) of an investment using a discount rate and a series of cash flows that occur at irregular intervals.

Purpose 
--------

Calculate net present value for irregular cash flows

Return value 
-------------

Net present value

Syntax
------

    =XNPV(rate,values,dates)

*   _rate_ - Discount rate to apply to the cash flows.
*   _values_ - Values representing cash flows.
*   _dates_ - Dates that correspond to cash flows, in any order.

Using the XNPV function 
------------------------

The XNPV function returns the net present value (NPV) of an investment based on a discount _rate_ and a series of cash flows that occur at irregular intervals. _Values_ represent cash flows and be correspond to _dates_. Negative values represent cash paid out; positive values represent cash received. The first date indicates the beginning of the schedule of payments and must be the earliest date. Subsequent dates may occur in any order.

The XNPV function takes three [arguments](https://exceljet.net/glossary/function-argument)
: _rate_, _values_, and _dates_. _Rate_ represents the discount rate to apply to the cash flows. Enter _rate_ as a percentage like 6% or the decimal value 0.06.

_Values_ represent a series of cash flows that correspond to _dates_. The first value is optional and corresponds to a cost at the beginning of the investment. If the first value is a cost or payment, it must be a entered as a negative number. All subsequent payments are discounted based on a 365-day year. _Values_ must include at least one positive and one negative value, or XNPV will return a #NUM! error.

The _dates_ argument represents a schedule of dates that correspond to _values_. The values supplied for _dates_ must be valid [Excel dates](https://exceljet.net/glossary/excel-date)
. The first payment date indicates the beginning of the schedule of payments and must be the earliest date. Other dates must be later than this date, but _do not_ need to be in chronological order. Typically, _dates_ is supplied as a [range](https://exceljet.net/glossary/range)
. 

XNPV does not discount the initial cash flow. Subsequent payments are discounted based on a 365-day year. To discount to a particular valuation date, you can set up XNPV so that the first cashflow is zero, associated with the valuation date.

### Example

In the example shown, the formula in F6 is:

    =XNPV(F4,B5:B10,C5:C10) // returns 177.6532
    

The result is 177.6532, displayed as 177.65 when [formatted as a number](https://exceljet.net/shortcuts/apply-number-format)
 with two decimal places.

### Notes

*   _Rate_ is provided as a percentage (.12 for 12%).
*   _Dates_ do not need to be in chronological order, but the first payment date must be the earliest date.
*   _Dates_ must be valid [Excel dates](https://exceljet.net/glossary/excel-date)
    .
*   XNPV doesn’t discount the initial cash flow.

Related functions
-----------------

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel IRR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_irr.png "Excel IRR function")](https://exceljet.net/functions/irr-function)

### [IRR Function](https://exceljet.net/functions/irr-function)

The Excel IRR function is a financial function that returns the internal rate of return (IRR) for a series of cash flows that occur at regular intervals.

[![Excel XIRR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20xirr%20function.png "Excel XIRR function")](https://exceljet.net/functions/xirr-function)

### [XIRR Function](https://exceljet.net/functions/xirr-function)

The Excel XIRR function is a financial function that returns the internal rate of return (IRR) for a series of cash flows that occur at irregular intervals. The XIRR function uses iteration to arrive at a result.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [IRR Function](https://exceljet.net/functions/irr-function)
    
*   [XIRR Function](https://exceljet.net/functions/xirr-function)
    

### Links

*   [Microsoft XNPV function documentation](https://support.office.com/en-us/article/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7)
    

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