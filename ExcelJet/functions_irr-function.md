# Excel IRR function | Exceljet

**Source:** https://exceljet.net/functions/irr-function

---

[Skip to main content](https://exceljet.net/functions/irr-function#main-content)

[](https://exceljet.net/functions/irr-function#)

*   [Previous](https://exceljet.net/functions/ipmt-function)
    
*   [Next](https://exceljet.net/functions/ispmt-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

IRR Function
============

by Dave Bruns · Updated 27 Aug 2021

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[NPV](https://exceljet.net/functions/npv-function)

![Excel IRR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_irr.png "Excel IRR function")

Summary
-------

The Excel IRR function is a financial function that returns the internal rate of return (IRR) for a series of cash flows that occur at regular intervals.

Purpose 
--------

Calculate internal rate of return

Return value 
-------------

Calculated return as percentage

Syntax
------

    =IRR(values,[guess])

*   _values_ - Array or reference to cells that contain values.
*   _guess_ - \[optional\] An estimate for expected IRR. Default is .1 (10%).

Using the IRR function 
-----------------------

The internal rate of return (IRR) is the interest rate received for an investment with payments and income occurring at regular intervals (i.e. monthly, annual). Payments are expressed as negative values and income as positive values. Amounts can vary, but intervals need to be the same. The first value is negative, since it represents an outflow.

Excel uses iteration to arrive at a result, starting with the guess (if provided) or with .1 (10%) if not. If an accurate IRR can't be calculated after a fixed number of iterations, the #NUM error is returned. A better guess will prevent this error.

### Notes

*   The _values_ array must contain at least one positive value and one negative value.
*   Values should be in chronological order.
*   If IRR returns the #NUM! or an unexpected result, adjust _guess_.

Related functions
-----------------

[![Excel PV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pv%20function.png "Excel PV function")](https://exceljet.net/functions/pv-function)

### [PV Function](https://exceljet.net/functions/pv-function)

The Excel PV function is a financial function that returns the present value of an investment. You can use the PV function to get the value in today's dollars of a series of future payments, assuming periodic, constant payments and a constant interest rate.

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

*   [PV Function](https://exceljet.net/functions/pv-function)
    
*   [NPV Function](https://exceljet.net/functions/npv-function)
    

### Links

*   [Microsoft IRR function documentation](https://support.office.com/en-us/article/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc)
    

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