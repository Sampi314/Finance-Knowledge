# Excel MIRR function | Exceljet

**Source:** https://exceljet.net/functions/mirr-function

---

[Skip to main content](https://exceljet.net/functions/mirr-function#main-content)

[](https://exceljet.net/functions/mirr-function#)

*   [Previous](https://exceljet.net/functions/mduration-function)
    
*   [Next](https://exceljet.net/functions/nominal-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

MIRR Function
=============

by Dave Bruns · Updated 29 Aug 2021

Related functions 
------------------

[PV](https://exceljet.net/functions/pv-function)

[NPV](https://exceljet.net/functions/npv-function)

[IRR](https://exceljet.net/functions/irr-function)

![Excel MIRR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_mirr.png "Excel MIRR function")

Summary
-------

The Excel MIRR function is a financial function that returns the modified internal rate of return (MIRR) for a series of cash flows, taking into account both discount rate and reinvestment rate for future cash flows.

Purpose 
--------

Calculate modified internal rate of return

Return value 
-------------

Calculated return as percentage

Syntax
------

    =MIRR(values,finance_rate,reinvest_rate)

*   _values_ - Array or reference to cells that contain cash flows.
*   _finance\_rate_ - Required rate of return (discount rate) as percentage.
*   _reinvest\_rate_ - Interest rate received on cash flows reinvested as percentage.

Using the MIRR function 
------------------------

The standard Internal rate of return function (IRR) assumes all cash flows are reinvested at the same rate as the IRR. The modified internal rate of return function (MIRR) accepts both the cost of investment (discount rate) and a reinvestment rate for cash flows received.

In the example shown, the formula in F6 is:

    =MIRR(B5:B11,F4,F4)
    

In this example, we assume that the reinvestment rate is the same as the cost of capital, so we set both the _finance\_rate_ and _reinvest\_rate_ to the value in F4, which is 10%.

### Notes

*   The _values_ array must contain at least one positive value and one negative value.
*   _Values_ should be in chronological order.
*   MIRR assumes cash flows at regular periods.

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
    

### Links

*   [Microsoft MIRR function documentation](https://support.office.com/en-us/article/mirr-function-b020f038-7492-4fb4-93c1-35c345b53524)
    

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