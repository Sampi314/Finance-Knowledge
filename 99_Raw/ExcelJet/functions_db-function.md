# Excel DB function | Exceljet

**Source:** https://exceljet.net/functions/db-function

---

[Skip to main content](https://exceljet.net/functions/db-function#main-content)

[](https://exceljet.net/functions/db-function#)

*   [Previous](https://exceljet.net/functions/cumprinc-function)
    
*   [Next](https://exceljet.net/functions/ddb-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

DB Function
===========

by Dave Bruns · Updated 26 Aug 2021

Related functions 
------------------

[SLN](https://exceljet.net/functions/sln-function)

[DB](https://exceljet.net/functions/db-function)

[DDB](https://exceljet.net/functions/ddb-function)

[SYD](https://exceljet.net/functions/syd-function)

[VDB](https://exceljet.net/functions/vdb-function)

![Excel DB function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_db_function.png "Excel DB function")

Summary
-------

The Excel DB function returns the depreciation of an asset for a specified period using the fixed-declining balance method. The calculation is based on initial asset cost, salvage value, the number of periods over which the asset is depreciated and, optionally, the number of months in the first year.

Purpose 
--------

Depreciation - fixed-declining balance

Return value 
-------------

Depreciation in given period

Syntax
------

    =DB(cost,salvage,life,period,[month])

*   _cost_ - Initial cost of asset.
*   _salvage_ - Asset value at the end of the depreciation.
*   _life_ - Periods over which asset is depreciated.
*   _period_ - Period to calculation depreciation for.
*   _month_ - \[optional\] Number of months in the first year. Defaults to 12.

Using the DB function 
----------------------

The Excel DB function returns the depreciation of an asset for a specified period using the fixed-declining balance method. The calculated depreciation is based on initial asset cost, salvage value, the number of periods over which the asset is depreciated and, optionally, the number of months in the first year.

In the example shown, the formula in C6, copied down, is:

    =DB(cost,salvage,life,B6)
    

where [named ranges](https://exceljet.net/glossary/named-range)
 are "cost" = G4, "salvage" = G5, and  "life" = G6.

### Fixed-declining balance calculation

To get a rate to use to calculate depreciation based on fixed-declining balance, Excel uses the following formula:

    rate=1-((salvage/cost)^(1/life))
    

To calculate depreciation in each year, Excel uses a formula like this:

    =(cost-prior depreciation)*rate
    

However, depreciation for the first and last year is calculated differently to account for the _month_ argument. The table below shows the calculation used to depreciate an asset over 5 years. If 3 is supplied for _month_, depreciation the first year is based on 3 months only, and depreciation the last year is based on 9 months.

| Year | Depreciation Calculation |
| --- | --- |
| 1   | \=_cost_ \* _rate_ \* _month_ / 12 |
| 2   | \=(_cost_ - prior depreciation) _\* rate_ |
| 3   | \=(_cost_ - prior depreciation) _\* rate_ |
| 4   | \=(_cost_ - prior depreciation) \* _rate_ |
| 5   | \=((_cost_ - prior depreciation) \* _rate_ \* (12 - _month_)) / 12 |

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

*   [Microsoft DB function documentation](https://support.office.com/en-us/article/db-function-354e7d28-5f93-4ff1-8a52-eb4ee549d9d7)
    

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