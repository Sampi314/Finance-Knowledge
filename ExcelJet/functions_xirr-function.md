# Excel XIRR function | Exceljet

**Source:** https://exceljet.net/functions/xirr-function

---

[Skip to main content](https://exceljet.net/functions/xirr-function#main-content)

[](https://exceljet.net/functions/xirr-function#)

*   [Previous](https://exceljet.net/functions/vdb-function)
    
*   [Next](https://exceljet.net/functions/xnpv-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

XIRR Function
=============

by Dave Bruns · Updated 8 Nov 2021

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[NPV](https://exceljet.net/functions/npv-function)

[IRR](https://exceljet.net/functions/irr-function)

[MIRR](https://exceljet.net/functions/mirr-function)

[XNPV](https://exceljet.net/functions/xnpv-function)

![Excel XIRR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20xirr%20function.png "Excel XIRR function")

Summary
-------

The Excel XIRR function is a financial function that returns the internal rate of return (IRR) for a series of cash flows that occur at irregular intervals. The XIRR function uses iteration to arrive at a result.

Purpose 
--------

Calculate internal rate of return for irregular cash flows

Return value 
-------------

Calculated internal rate of return

Syntax
------

    =XIRR(values,dates,[guess])

*   _values_ - Array or reference to cells that contain cash flows.
*   _dates_ - Dates that correspond to cash flows, in any order.
*   _guess_ - \[optional\] An estimate for expected IRR. Default is 0.1 (10%).

Using the XIRR function 
------------------------

The XIRR function calculates the internal rate of return for a series of cash flows that occur at irregular intervals. Payments are expressed as negative values and income as positive values.  If the first value is a cost or payment, it must be a negative value. Subsequent payments are discounted based on a 365-day year. To calculate the internal rate of return for a series of regular, periodic cash flows, use the [IRR function](https://exceljet.net/functions/irr-function)
.

XIRR is related to the [XNPV function](https://exceljet.net/functions/xnpv-function)
. The rate returned by XIRR is the interest rate when XNPV = 0. The XIRR function uses iteration to arrive at a result. Starting with guess (which defaults to 0.1 if not provided) XIRR iterates through a calculation until the result is accurate to 0.000001 percent. If no result is found after 100 tries, XIRR returns the #NUM! error.

The XIRR function takes three [arguments](https://exceljet.net/glossary/function-argument)
: _values_, _dates_, and _guess_. _Values_ represent a series of cash flows. The first value is optional and corresponds to a cost at the beginning of the investment. If the first value is a cost or payment, it must be a entered as a negative number. _Values_ must include at least one positive and one negative value, or XIRR will return a #NUM! error. If _values_ contains any non-numeric values, XIRR returns a #VALUE! error.

The _dates_ argument represents a schedule of dates that correspond to _values_. The values supplied for _dates_ must be valid [Excel dates](https://exceljet.net/glossary/excel-date)
. Dates _do not_ need to be entered in chronological order. Typically, _dates_ is supplied as a [range](https://exceljet.net/glossary/range)
. If any date is not recognized as a date, XIRR returns a #VALUE! error.

The _guess_ argument is optional and represents the seed value to start with for the iterative calculation used by XIRR. If not provided, _guess_ defaults to 10% (0.10). Typically, you can safely omit _guess_. If XIRR returns #NUM!, and _values_ contains at least one positive and one negative value, try different percentages for _guess_ between 0 and 1.

### Example

In the example shown, dates are in the values are in the range B5:B10, and dates are in the range C5:C10. The formula in cell F4 is:

    =XIRR(B5:B10,C5:C10)  // returns .0788
    

The result returned by XIRR is .0788, displayed as 8% when the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 is applied.

### Notes

*   The _values_ array must contain at least one positive value and one negative value.
*   _Dates_ must be valid [Excel dates](https://exceljet.net/glossary/excel-date)
     that correspond to _values_
*   _Dates_ do not need to be in chronological order.
*   XIRR is related to the [XNPV function](https://exceljet.net/functions/xnpv-function)
    .

Related functions
-----------------

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel NPV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_npv.png "Excel NPV function")](https://exceljet.net/functions/npv-function)

### [NPV Function](https://exceljet.net/functions/npv-function)

The Excel NPV function is a financial function that calculates the net present value (NPV) of an investment using a discount rate and a series of future cash flows.

[![Excel IRR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_irr.png "Excel IRR function")](https://exceljet.net/functions/irr-function)

### [IRR Function](https://exceljet.net/functions/irr-function)

The Excel IRR function is a financial function that returns the internal rate of return (IRR) for a series of cash flows that occur at regular intervals.

[![Excel MIRR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mirr.png "Excel MIRR function")](https://exceljet.net/functions/mirr-function)

### [MIRR Function](https://exceljet.net/functions/mirr-function)

The Excel MIRR function is a financial function that returns the modified internal rate of return (MIRR) for a series of cash flows, taking into account both discount rate and reinvestment rate for future cash flows.

[![Excel XNPV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xnpv.png "Excel XNPV function")](https://exceljet.net/functions/xnpv-function)

### [XNPV Function](https://exceljet.net/functions/xnpv-function)

The Excel XNPV function is a financial function that calculates the net present value (NPV) of an investment using a discount rate and a series of cash flows that occur at irregular intervals.

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
    
*   [NPV Function](https://exceljet.net/functions/npv-function)
    
*   [IRR Function](https://exceljet.net/functions/irr-function)
    
*   [MIRR Function](https://exceljet.net/functions/mirr-function)
    
*   [XNPV Function](https://exceljet.net/functions/xnpv-function)
    

### Links

*   [Microsoft XIRR function documentation](https://support.office.com/en-us/article/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d)
    

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