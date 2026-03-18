# Excel SYD function | Exceljet

**Source:** https://exceljet.net/functions/syd-function

---

[Skip to main content](https://exceljet.net/functions/syd-function#main-content)

[](https://exceljet.net/functions/syd-function#)

*   [Previous](https://exceljet.net/functions/sln-function)
    
*   [Next](https://exceljet.net/functions/tbilleq-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

SYD Function
============

by Dave Bruns · Updated 2 Nov 2018

Related functions 
------------------

[SLN](https://exceljet.net/functions/sln-function)

[DB](https://exceljet.net/functions/db-function)

[DDB](https://exceljet.net/functions/ddb-function)

[SYD](https://exceljet.net/functions/syd-function)

[VDB](https://exceljet.net/functions/vdb-function)

![Excel SYD function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_syd_function.png "Excel SYD function")

Summary
-------

The Excel SYD function returns the "sum-of-years" depreciation for an asset in a given period. The calculated depreciation is based on initial asset cost, salvage value, and the number of periods over which the asset is depreciated.

Purpose 
--------

Depreciation - sum-of-years

Return value 
-------------

Depreciation in given period

Syntax
------

    =SYD(cost,salvage,life,period)

*   _cost_ - Initial cost of asset.
*   _salvage_ - Asset value at the end of the depreciation.
*   _life_ - Periods over which asset is depreciated.
*   _period_ - Period to calculation depreciation for.

Using the SYD function 
-----------------------

The Excel SYD function returns the "sum-of-years" depreciation for an asset in a given period. The calculated depreciation is based on initial asset cost, salvage value, and the number of periods over which the asset is depreciated.

For example, for an asset with an initial cost of $10,000, a useful life of 5 years, and a salvage value of $2,000, depreciation in year 1 can be calculated with SYD as follows:

    =SYD(10000,2000,5,1) // returns $2,667 
    

In the worksheet as shown, the formula in C7, copied down, is:

    =SYD(cost,salvage,life,B7)
    

### Sum of years calculation

In the example, the asset has a useful life of 5 years. Excel sums the years like this:

    =1+2+3+4+5=15
    

This sum is then used in the calculation as follows: The asset loses 8000 in value over a 5 year period, so depreciation in period 1 = 5/15 \* 8000 = $2,667, depreciation in period 2= 4/15 \* 8000 = $2,133 , and so on. The table below summarizes the calculation in all periods.

| Year | Depreciation Calculation |
| --- | --- |
| 1   | \=(5/15) \* 8000 |
| 2   | \=(4/15) \* 8000 |
| 3   | \=(3/15) \* 8000 |
| 4   | \=(2/15) \* 8000 |
| 5   | \=(1/15) \* 8000 |

Related functions
-----------------

[![Excel SLN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_sln_function.png "Excel SLN function")](https://exceljet.net/functions/sln-function)

### [SLN Function](https://exceljet.net/functions/sln-function)

The Excel SLN function returns the depreciation of an asset for one period, calculated with a straight-line method. The calculated depreciation is based on initial asset cost, salvage value, and the number of periods over which the asset is depreciated.

[![Excel DB function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_db_function.png "Excel DB function")](https://exceljet.net/functions/db-function)

### [DB Function](https://exceljet.net/functions/db-function)

The Excel DB function returns the depreciation of an asset for a specified period using the fixed-declining balance method. The calculation is based on initial asset cost, salvage value, the number of periods over which the asset is depreciated and, optionally, the number of months in the first...

[![Excel DDB function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_ddb_function.png "Excel DDB function")](https://exceljet.net/functions/ddb-function)

### [DDB Function](https://exceljet.net/functions/ddb-function)

The Excel DDB function returns the depreciation of an asset for a given period using the double-declining balance method or another method you specify by changing the _factor_ argument.

[![Excel SYD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_syd_function.png "Excel SYD function")](https://exceljet.net/functions/syd-function)

### [SYD Function](https://exceljet.net/functions/syd-function)

The Excel SYD function returns the "sum-of-years" depreciation for an asset in a given period. The calculated depreciation is based on initial asset cost, salvage value, and the number of periods over which the asset is depreciated.

[![Excel VDB function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_vdb_function.png "Excel VDB function")](https://exceljet.net/functions/vdb-function)

### [VDB Function](https://exceljet.net/functions/vdb-function)

The Excel VDB function returns the depreciation of an asset for given period, using the double-declining balance method or another method specified by changing the **factor** argument. By default, the VDB function will switch to straight line calculation. VDB stands for variable...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SLN Function](https://exceljet.net/functions/sln-function)
    
*   [DB Function](https://exceljet.net/functions/db-function)
    
*   [DDB Function](https://exceljet.net/functions/ddb-function)
    
*   [SYD Function](https://exceljet.net/functions/syd-function)
    
*   [VDB Function](https://exceljet.net/functions/vdb-function)
    

### Links

*   [Microsoft SYD function documentation](https://support.office.com/en-us/article/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27)
    

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