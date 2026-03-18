# Filter exclude blank values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-exclude-blank-values

---

[Skip to main content](https://exceljet.net/formulas/filter-exclude-blank-values#main-content)

[](https://exceljet.net/formulas/filter-exclude-blank-values#)

*   [Previous](https://exceljet.net/formulas/filter-every-nth-row)
    
*   [Next](https://exceljet.net/formulas/filter-horizontal-data)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter exclude blank values
===========================

by Dave Bruns · Updated 23 Aug 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Filter exclude blank values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20exclude%20blank%20values.png "Excel formula: Filter exclude blank values")

Summary
-------

To filter out rows with blank or empty cells, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with [boolean logic](https://exceljet.net/glossary/boolean-logic)
. In the example shown, the formula in F5 is:

    =FILTER(B5:D15,(B5:B15<>"")*(C5:C15<>"")*(D5:D15<>""))
    

The output contains only rows from the source data where all three columns have a value.

Generic formula
---------------

    =FILTER(data,(rng1<>"")*(rng2<>"")*(rng3<>""))

Explanation 
------------

The [FILTER function](https://exceljet.net/functions/filter-function)
 is designed to extract data that matches one or more criteria. In this case, we want to apply criteria that requires all three columns in the source data (Name, Group, and Room) to have data. In other words, if a row is missing any of these values, we want to exclude that row from output.

To do this, we use three [boolean](https://exceljet.net/glossary/boolean-logic)
 expressions operating on arrays. The first expression tests for blank names:

    B5:B15<>"" // check names
    

The not [operator](https://exceljet.net/glossary/math-operators)
 (<>) with an [empty string](https://exceljet.net/glossary/empty-string)
 ("") translates to "not empty". For each cell in the range B5:B15, the result will be either TRUE or FALSE, where TRUE means "not empty" and FALSE means "empty". Because there are 11 cells in the range, we get 11 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE}
    

The second expression tests for blank groups:

    C5:C15<>"" // check groups
    

Again, we are checking 11 cells, so we get 11 results:

    {TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE}
    

Finally, we check for blank room numbers:

    D5:D15<>"" // check groups
    

which produces:

    {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE}
    

When the arrays that result from the three expressions above are multiplied together, the math operation coerces the TRUE and FALSE values to 1s and 0s. We use multiplication in this case, because we want to enforce "AND" logic: expression1 AND expression2 AND expression3. In other words, all three expressions must return TRUE in a given row.

Following the rules of boolean logic, the final result is an array like this:

    {1;0;1;0;1;1;1;0;0;0;1}
    

This array is delivered directly to the FILTER function as the _include_ argument. FILTER only includes the 6 rows that correspond to 1s in the final output.

Related formulas
----------------

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Remove blank rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_blank_rows.png "Excel formula: Remove blank rows")](https://exceljet.net/formulas/remove-blank-rows)

### [Remove blank rows](https://exceljet.net/formulas/remove-blank-rows)

In this example, the goal is to remove empty rows from a range with a formula. One approach is to use the BYROW function to identify all non-empty rows in the range and pass this result into the FILTER function as the include argument. This is the approach used in the worksheet shown, where the...

[![Excel formula: Row is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/row_is_blank.png "Excel formula: Row is blank")](https://exceljet.net/formulas/row-is-blank)

### [Row is blank](https://exceljet.net/formulas/row-is-blank)

The goal is to use a formula to check if all cells in a row are blank or empty and return TRUE or FALSE. One way to solve this problem is with the SUMPRODUCT function, as seen in the worksheet above. Another approach is to use the newer BYROW function. Both methods are described below. SUMPRODUCT...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Remove blank rows](https://exceljet.net/formulas/remove-blank-rows)
    
*   [Row is blank](https://exceljet.net/formulas/row-is-blank)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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