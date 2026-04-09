# Excel NPV function | Exceljet

**Source:** https://exceljet.net/functions/npv-function

---

[Skip to main content](https://exceljet.net/functions/npv-function#main-content)

[](https://exceljet.net/functions/npv-function#)

*   [Previous](https://exceljet.net/functions/nper-function)
    
*   [Next](https://exceljet.net/functions/oddfprice-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

NPV Function
============

by Dave Bruns · Updated 30 Aug 2021

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[IRR](https://exceljet.net/functions/irr-function)

![Excel NPV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_npv.png "Excel NPV function")

Summary
-------

The Excel NPV function is a financial function that calculates the net present value (NPV) of an investment using a discount rate and a series of future cash flows.

Purpose 
--------

Calculate net present value

Return value 
-------------

Net present value

Syntax
------

    =NPV(rate,value1,[value2],...)

*   _rate_ - Discount rate over one period.
*   _value1_ - First value(s) representing cash flows.
*   _value2_ - \[optional\] Second value(s) representing cash flows.

Using the NPV function 
-----------------------

NPV calculates the net present value (NPV) of an investment using a discount rate and a series of future cash flows. The discount rate is the rate for one period, assumed to be annual. NPV in Excel is a bit tricky, because of how the function is implemented. Although NPV carries the idea of "net", as in the present value of future cash flows less initial cost, NPV is really just the present value of uneven cash flows.

As Timothy R. Mayes, author of [Financial Analysis with Microsoft Excel](https://www.amazon.com/Financial-Analysis-Microsoft-Excel-Timothy/dp/1285432274)
, says on his website [TVMCalcs.com](http://www.tvmcalcs.com/blog/comments/the_npv_function_doesnt_calculate_net_present_value/)
:

_Net present value is defined as the present value of the expected future cash flows less the initial cost of the investment...the NPV function in spreadsheets doesn't really calculate NPV. Instead, despite the word "net," the NPV function is really just a present value of an uneven cash flow function._

One simple approach is to exclude the initial investment from the _values_ argument and instead subtract the amount outside the NPV function. 

In the example shown, the formula in F6 is:

    =NPV(F4,C6:C10)+C5
    

Note the initial investment in C5 is not included as a value, and is instead added to the result of NPV (since the number is negative).

### Notes

*   _values_ must be equally spaced in time and occur at the end of each period.
*   _values_ must be in chronological order.

NPV function examples
---------------------

[![Excel formula: NPV formula for net present value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/NPV%20formula%20for%20net%20present%20value.png "Excel formula: NPV formula for net present value")](https://exceljet.net/formulas/npv-formula-for-net-present-value)

### [NPV formula for net present value](https://exceljet.net/formulas/npv-formula-for-net-present-value)

Net Present Value (NPV) is the present value of expected future cash flows minus the initial cost of investment. The NPV function in Excel only calculates the present value of uneven cashflows, so the initial cost must be handled explicitly. One way to calculate Net Present Value in Excel is to use...

Related functions
-----------------

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

[![Excel IRR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_irr.png "Excel IRR function")](https://exceljet.net/functions/irr-function)

### [IRR Function](https://exceljet.net/functions/irr-function)

The Excel IRR function is a financial function that returns the internal rate of return (IRR) for a series of cash flows that occur at regular intervals.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [NPV formula for net present value](https://exceljet.net/formulas/npv-formula-for-net-present-value)
    

### Functions

*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [IRR Function](https://exceljet.net/functions/irr-function)
    

### Links

*   [Microsoft NPV function documentation](https://support.office.com/en-us/article/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568)
    

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