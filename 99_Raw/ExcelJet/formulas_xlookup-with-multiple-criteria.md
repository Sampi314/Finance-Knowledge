# XLOOKUP with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/xlookup-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/xlookup-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [Next](https://exceljet.net/formulas/xlookup-with-regex-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP with multiple criteria
==============================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7559/download?token=txa-faUA)
 (16.45 KB)

![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")

Summary
-------

The best way to use [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 with multiple criteria is to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to apply conditions. In the example shown, the formula in H8 is:

    =XLOOKUP(1,(B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7),E5:E15)
    

XLOOKUP returns $29.00, the price for a Medium Blue Hoodie. Note the _lookup\_value_ in XLOOKUP is 1 since the logical expressions in _lookup\_array_ create an [array](https://exceljet.net/glossary/array)
 of 1s and 0s. Read below for details.

_Note: in older versions of Excel, you can use the [same approach with INDEX and MATCH](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
._

Generic formula
---------------

    =XLOOKUP(1,(criteria1)*(criteria2)*(criteria3),data)

Explanation 
------------

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for _lookup\_value_ and _lookup\_array_. How can we configure XLOOKUP to consider values in _multiple_ columns? The trick is to _construct_ the lookup array we need using Boolean logic, then configure XLOOKUP to look for the number 1. This approach is explained below.

### Basic XLOOKUP

The most basic use of XLOOKUP involves just three arguments:

    =XLOOKUP(lookup_value,lookup_array,result_array)

_Lookup\_value_ is the value you are looking for, _lookup\_array_ is the range you are looking in, and _result\_array_ contains the value you want to return. There is no obvious way to supply multiple criteria.

### Boolean Logic

This formula works around this limitation by using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to create a temporary [array](https://exceljet.net/glossary/array)
 of ones and zeros to represent rows matching all 3 criteria, then asking XLOOKUP to find the first 1 in the array. The temporary array of ones and zeros is generated with this snippet:

    (B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7)
    

Here we compare the item entered in H5 against all items, the size in H6 against all sizes, and the color in H7 against all colors. The initial result is three arrays of TRUE/FALSE values like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE}*{FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;FALSE}*{FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

> Tip: [use F9 to see these results](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
> . Just select an expression in the formula bar, and press F9.

The math operation (multiplication) automatically converts the TRUE FALSE values to 1s and 0s:

    {0;0;0;0;1;1;1;0;0;0;0}*{0;1;0;0;0;1;0;1;1;0;0}*{0;1;0;1;0;1;0;0;0;0;0}
    

After multiplication is complete, we have a single array like this:

    {0;0;0;0;0;1;0;0;0;0;0}
    

This is the array returned to XLOOKUP as the _lookup\_array_. Notice, the sixth value in the array is 1. This corresponds to the sixth row in the data, which contains a Medium Blue Hoodie. Because our _lookup\_array_ contains only 1s and 0s, we set the _lookup\_value_ to 1. At this point, we can rewrite the formula like this:

    =XLOOKUP(1,{0;0;0;0;0;1;0;0;0;0;0},E5:E15) // returns 29

XLOOKUP locates the 1 in the sixth row of the lookup\_array and returns the sixth value in the _return\_array_ (E5:E15). This is $29.00, the price of a Medium Blue Hoodie.

### Array visualization

The [arrays](https://exceljet.net/glossary/array)
 explained above can be difficult to visualize. The image below shows the process. Columns B, C, and D correspond to the data in the example, after being compared to the values in H5, H6, and H7. Column F is created by multiplying the three columns together. This is the array delivered to XLOOKUP as the _lookup\_array_.

![XLOOKUP with multiple criteria - visualizing Boolean arrays](https://exceljet.net/sites/default/files/images/formulas/inline/XLOOKUP_with_multiple_criteria_array_visualization.png "XLOOKUP with multiple criteria - visualizing Boolean arrays")

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### Alternative with concatenation

In simple cases like this example, you will sometimes see an alternative approach that uses [concatenation](https://exceljet.net/glossary/concatenation)
 instead of Boolean logic. The formula looks like this:

    =XLOOKUP(H5&H6&H7,B5:B15&C5:C15&D5:D15,E5:E15)

The _lookup\_value_ is created by joining H5, H6, and H7 using [concatenation](https://exceljet.net/glossary/concatenation)
:

    =XLOOKUP(H5&H6&H7
    

This results in the string "HoodieMediumBlue". The _lookup\_array_ is created in a similar way, except we are now joining ranges:

    =XLOOKUP(H5&H6&H7,B5:B15&C5:C15&D5:D15
    

The _return\_array_ is supplied as a normal range, E5:E15:

    =XLOOKUP(H5&H6&H7,B5:B15&C5:C15&D5:D15,E5:E15)
    

In essence, we are gluing together the values we need for criteria in the _lookup\_array_, then looking for a value we _created_ by joining together the Item, Size, and Color that we want to find. In this configuration, XLOOKUP returns $29.00 as before.

This approach works in simple scenarios, but the Boolean Logic approach is far more flexible and powerful, so I recommend you use that method instead of concatenation. For an example of a problem that cannot be solved with concatenation, see [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
.

### INDEX and MATCH

XLOOKUP is only available in newer versions of Excel, but you can use the same technique with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, which will work in any version. The formula below uses INDEX and MATCH with Boolean logic to achieve the same result:

    =INDEX(E5:E15,MATCH(1,(B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7),0))

_Note: in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, this is an array formula and needs to be entered with Control + Shift + Enter. In newer versions of Excel that support [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, this formula will work seamlessly._

For more details and a sample workbook, see [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
.

Related formulas
----------------

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP with Boolean OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20boolean%20OR%20logic.png "Excel formula: XLOOKUP with Boolean OR logic")](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

### [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

In this example, the goal is to use XLOOKUP to find the first "red" or "pink" record in the data as shown. All data is in an Excel Table named data in the range B5:E14. This means the formulas below use structured references . As a result, the formulas will automatically include new data added to...

[![Excel formula: XLOOKUP with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20with%20complex%20multiple%20criteria.png "Excel formula: XLOOKUP with complex multiple criteria")](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)

### [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)

Normally, the XLOOKUP function is configured to look for a value in a lookup array that exists on the worksheet. However, when the criteria used to match a value becomes more complex, you can use Boolean logic to create a lookup array on the fly composed only of 1s and 0s, then look for the value 1...

[![Excel formula: XMATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XMATCH_with_multiple_criteria.png "Excel formula: XMATCH with multiple criteria")](https://exceljet.net/formulas/xmatch-with-multiple-criteria)

### [XMATCH with multiple criteria](https://exceljet.net/formulas/xmatch-with-multiple-criteria)

The goal is to match a row in a set of data based on a given Item, Size, and Color. At a glance, this seems like a difficult problem because XMATCH only has one value for lookup\_value and lookup\_array . How can we configure XMATCH to consider values from multiple columns? The trick is to generate...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/XLOOKUP%20with%20boolean%20logic-Play.png)](https://exceljet.net/videos/xlookup-with-boolean-logic)

### [XLOOKUP with boolean logic](https://exceljet.net/videos/xlookup-with-boolean-logic)

In this video we'll look at how to use the XLOOKUP function with Boolean logic. Boolean logic is an elegant way to apply multiple criteria. In this worksheet we have sample order data in a table called "data". Let's use the XLOOKUP function to find the first order in March where the color is red...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
    
*   [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
    
*   [XMATCH with multiple criteria](https://exceljet.net/formulas/xmatch-with-multiple-criteria)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    
*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [XLOOKUP with boolean logic](https://exceljet.net/videos/xlookup-with-boolean-logic)
    
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

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