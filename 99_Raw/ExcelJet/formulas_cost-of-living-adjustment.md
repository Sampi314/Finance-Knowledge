# Cost of living adjustment - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cost-of-living-adjustment

---

[Skip to main content](https://exceljet.net/formulas/cost-of-living-adjustment#main-content)

[](https://exceljet.net/formulas/cost-of-living-adjustment#)

*   [Previous](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    
*   [Next](https://exceljet.net/formulas/count-consecutive-monthly-orders)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Cost of living adjustment
=========================

by Dave Bruns · Updated 22 Jun 2022

![Excel formula: Cost of living adjustment](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cost%20of%20living%20adjustment.png "Excel formula: Cost of living adjustment")

Summary
-------

To calculate a cost of living (COLA) adjustment in Excel, you can use a simple formula that multiplies the base times the adjustment percentage, then adds the result to the base. In the example shown, the formula in C6, copied down, is:

    =C5+(C5*cola)
    

where **cola** is the [named range](https://exceljet.net/glossary/named-range)
 F6, and contains the adjustment as a percentage.

Generic formula
---------------

    =base+(base*cola)

Explanation 
------------

The goal in this example is to calculate a cost of living (COLA) adjustment for each of the eleven years shown, starting on the second year. The actual adjustment percentage is entered in cell F6, which is the named range **cola**. Each year, the adjustment should be applied to the previous base amount in column C, starting with the base amount in cell C5.

The formula in cell C6, copied down is:

    =C5+(C5*cola)
    

With 30,000 in C5 as shown, the formula is solved like this:

    =C5+(C5*cola)
    =30000+(30000*0.03)
    =30000+900
    =30900
    

As the formula is copied down the table, the [relative reference](https://exceljet.net/glossary/relative-reference)
 C5 changes at each row, while the [named range](https://exceljet.net/glossary/named-range)
 **cola** (F6) behaves like an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 and does not change. The result on each new row is the previous year's base plus the adjustment.

### Total adjustments

To calculate the total of all adjustments, the formula in F7 is:

    =SUM(C5:C15-C5)
    

This is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered with control+shift+enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
. The result is the total of all adjustments made since year 1.

### Alternative layout

The screen below shows an alternative layout that breaks out the adjustment amount separately, and allows a different rate of adjustment for each year.

![COLA calculation alternative layout](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/cost%20of%20living%20adjustment%20alternative.png?itok=3DoxhXLt "COLA calculation alternative layout")

The formula in N5, copied down, calculates the adjustment:

    =M5*L5
    

The formula in M6, copied down, calculates a new base for year:

    =M5+N5
    

Related formulas
----------------

[![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")](https://exceljet.net/formulas/increase-by-percentage)

### [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1+...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    

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