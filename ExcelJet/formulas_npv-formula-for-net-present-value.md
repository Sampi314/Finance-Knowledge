# NPV formula for net present value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/npv-formula-for-net-present-value

---

[Skip to main content](https://exceljet.net/formulas/npv-formula-for-net-present-value#main-content)

[](https://exceljet.net/formulas/npv-formula-for-net-present-value#)

*   [Previous](https://exceljet.net/formulas/mortgage-payment-schedule)
    
*   [Next](https://exceljet.net/formulas/payment-for-annuity)
    

[Financial](https://exceljet.net/formulas#Financial)

NPV formula for net present value
=================================

by Dave Bruns · Updated 6 Nov 2018

Related functions 
------------------

[NPV](https://exceljet.net/functions/npv-function)

![Excel formula: NPV formula for net present value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/NPV%20formula%20for%20net%20present%20value.png "Excel formula: NPV formula for net present value")

Summary
-------

To calculate Net Present Value (NPV) you can use the NPV function. In the example shown, the formula in F6 is:

    =NPV(F4,C6:C10)+C5
    

Generic formula
---------------

    =NPV(rate,cashflows)-initialcost

Explanation 
------------

Net Present Value (NPV) is the present value of expected future cash flows minus the initial cost of investment. The NPV function in Excel only calculates the present value of uneven cashflows, so the initial cost must be handled explicitly.

One way to calculate Net Present Value in Excel is to use NPV to get the present value of all expected cash flows, then subtract the initial investment. This is the approach taken in the example shown, where the formula in F6 is:

    =NPV(F4,C6:C10)+C5
    

The NPV function returns 50962.91. The initial investment (-50,000, recorded as a negative value because it is an outflow) is then added, and the final result is 962.91.

Related functions
-----------------

[![Excel NPV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_npv.png "Excel NPV function")](https://exceljet.net/functions/npv-function)

### [NPV Function](https://exceljet.net/functions/npv-function)

The Excel NPV function is a financial function that calculates the net present value (NPV) of an investment using a discount rate and a series of future cash flows.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [NPV Function](https://exceljet.net/functions/npv-function)
    

### Links

*   [The NPV Function Doesn’t Calculate Net Present Value](http://www.tvmcalcs.com/blog/comments/the_npv_function_doesnt_calculate_net_present_value)
    

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