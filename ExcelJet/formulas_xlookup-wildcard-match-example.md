# XLOOKUP wildcard match example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-wildcard-match-example

---

[Skip to main content](https://exceljet.net/formulas/xlookup-wildcard-match-example#main-content)

[](https://exceljet.net/formulas/xlookup-wildcard-match-example#)

*   [Previous](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
    
*   [Next](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP wildcard match example
==============================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

![Excel formula: XLOOKUP wildcard match example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/xlookup%20wildcard%20match%20example.png "Excel formula: XLOOKUP wildcard match example")

Summary
-------

To perform a partial match with XLOOKUP, supply 2 for the match mode argument to allow wildcards. In the example shown, the formula in H7 is:

    =TRANSPOSE((XLOOKUP(H4,D5:D15,B5:E15,"Not found",2)))
    

which performs a wildcard match with the value in H4 and returns all 4 fields as the result. The TRANSPOSE function is optional and used here only to convert the result from XLOOKUP to a vertical array.

Generic formula
---------------

    =XLOOKUP(value,lookup,return,"not found",2)

Explanation 
------------

Working from the inside out, XLOOKUP is configured to find the value in H4 in the Last name column, and return all fields. In order to support [wildcards](https://exceljet.net/glossary/wildcard)
, _match\_mode_ is provided as 2:

    XLOOKUP(H4,D5:D15,B5:E15,2) // match Last, return all fields
    

*   The _lookup\_value_ comes from cell H4
*   The _lookup\_array_ is the range D5:D15, which contains Last names
*   The _return\_array_ is B5:E15, which contains all fields
*   The _not\_found_ argument is set to "Not found"
*   The _match\_mode_ is 2, to allow wildcards
*   The _search\_mode_ is not provided and defaults to 1 (first to last)

Since H4 contains "corr\*", XLOOKUP finds the first Last name beginning with "corr" and returns all four fields in a horizontal [array](https://exceljet.net/glossary/array)
:

    {648,"Sharyn","Corriveau","Support"}
    

This result is returned directly to the TRANSPOSE function:

    =TRANSPOSE({648,"Sharyn","Corriveau","Support"})
    

The [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 changes the array from horizontal to vertical:

    {648;"Sharyn";"Corriveau";"Support"} // vertical array
    

and the array values [spill](https://exceljet.net/glossary/spill)
 into the range H7:H10.

### With implicit wildcard

In the example above, the asterisk wildcard (\*) is entered explicitly into the lookup value. To pass in the wildcard implicitly, you can adjust the formula like this:

    =TRANSPOSE((XLOOKUP(H4&"*",D5:D15,B5:E15,"Not found",2)))
    

Above, we [concatenate](https://exceljet.net/glossary/concatenation)
 the asterisk [wildcard](https://exceljet.net/glossary/wildcard)
 (\*) to the value in H4 in the formula itself. This will append the asterisk to any value entered in H4, and XLOOKUP will perform a wildcard lookup.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP lookup left](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20lookup%20left.png "Excel formula: XLOOKUP lookup left")](https://exceljet.net/formulas/xlookup-lookup-left)

### [XLOOKUP lookup left](https://exceljet.net/formulas/xlookup-lookup-left)

Whereas VLOOKUP is limited to lookups to the right of the lookup column, XLOOKUP can lookup values to the left natively. This means XLOOKUP can be used instead of INDEX and MATCH to find values to the left in a table or range. In the example shown, we are looking for the weight associated with...

[![Excel formula: XLOOKUP wildcard contains substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_wildcard_contains_substring.png "Excel formula: XLOOKUP wildcard contains substring")](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)

### [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)

The goal is to look up the Title, Author, and Year in the list of books as shown using a formula based on a partial match and a wildcard. The text string to search for is entered in cell G4. All data is in an Excel Table named data in the range B5:D16. This problem can be easily solved with the...

[![Excel formula: XLOOKUP match text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20match%20text%20contains.png "Excel formula: XLOOKUP match text contains")](https://exceljet.net/formulas/xlookup-match-text-contains)

### [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)

The XLOOKUP function contains built-in support for wildcards, but this feature must be enabled explicitly by setting match mode to the number 2. In the example shown, XLOOKUP is configured to match the value entered in cell E5, which may appear anywhere in the lookup values in B5:B15. The formula...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP lookup left](https://exceljet.net/formulas/xlookup-lookup-left)
    
*   [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
    
*   [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

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