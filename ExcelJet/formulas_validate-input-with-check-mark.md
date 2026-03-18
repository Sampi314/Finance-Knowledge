# Validate input with check mark - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/validate-input-with-check-mark

---

[Skip to main content](https://exceljet.net/formulas/validate-input-with-check-mark#main-content)

[](https://exceljet.net/formulas/validate-input-with-check-mark#)

*   [Previous](https://exceljet.net/formulas/unwrap-column-into-fields)
    
*   [Next](https://exceljet.net/formulas/value-exists-in-a-range)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Validate input with check mark
==============================

by Dave Bruns · Updated 30 Nov 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6416/download?token=qaMIhAw4)
 (16.3 KB)

![Excel formula: Validate input with check mark](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/validate_input_with_check_mark.png "Excel formula: Validate input with check mark")

Summary
-------

To display a check mark if a value is valid based on an existing list of allowed values, you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
 together with the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in C5 is:

    =IF(COUNTIF(list,B5),"✓","")
    

where **list** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E9. As the formula is copied down, it returns a checkmark when the value in column B exists in the range E5:E9, and an empty string ("") otherwise.

Generic formula
---------------

    =IF(logical_test,"✓","")

Explanation 
------------

This formula is a good example of [nesting](https://exceljet.net/glossary/nesting)
 one function inside another. At the core, this formula uses the [IF function](https://exceljet.net/functions/if-function)
 to return a check mark (✓) when a logical test returns TRUE:

    =IF(logical_test,"✓","")
    

If the test returns FALSE, the formula returns an [empty string](https://exceljet.net/glossary/empty-string)
 (""). For the logical test, we are using the [COUNTIF function](https://exceljet.net/functions/countif-function)
 like this:

    =COUNTIF(list,B5)
    

COUNTIF returns a count of how many times the value in B5 occurs in the [named range](https://exceljet.net/glossary/named-range)
 **list** (E5:E9). If the value in B5 exists in the range E5:E9, COUNTIF will return 1. If not, COUNTIF will return zero. Excel's standard behavior is to evaluate _any_ non-zero number as TRUE, and zero as FALSE. So, If the value in B5 exists in E5:E9, COUNTIF returns 1 and IF returns a check mark (✓). If the value in B5 is not found in the allowed list, COUNTIF returns zero and IF returns an empty string (""), which displays nothing.

### With hardcoded values

The example above shows allowed values in a range of cells, but allowed values can also be hardcoded into a slightly more complex version of the formula as an [array constant](https://exceljet.net/glossary/array-constant)
 like this:

    =IF(SUM(COUNTIF(B5,{"red","blue","green"})),"✓","")
    

Notice that we need to provide the array constant as the _criteria_, and B5 as the _range_. This is because COUNTIF will not accept an array constant as the range argument. Because of this change, COUNTIF will return 3 counts (one for each value in the array constant) and we also need to wrap the SUM function around COUNTIF to catch the results from COUNTIF and return a final count. 

_Note: The fact that COUNTIF won't accept an array for the range argument is not widely understood. To read more about COUNTIF quirkiness, see [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
._

### Check mark character (✓)

Inserting a checkmark character in Excel can be surprisingly challenging and you will find many articles on the internet explaining various approaches. The easiest way to get the check mark character (✓) used in this formula into Excel is simply to copy and paste it. If you are copying from this web page, paste it directly into the [formula bar](https://exceljet.net/glossary/formula-bar)
 to avoid bringing in unwanted formatting. You can also copy and paste directly from the attached worksheet.

If you have trouble with copy and paste, try using the  [UNICHAR function](https://exceljet.net/functions/unichar-function)
 to insert a checkmark like this:

    =UNICHAR(10003) // returns "✓"
    

UNICHAR (10003) returns a Unicode version of the checkmark:  [Unicode 2713 (U+2713)](https://wumbo.net/symbols/checkmark/)
. The original formula can be written like this:

    =IF(COUNTIF(list,B5),UNICHAR(10003),"")
    

_Note: the UNICHAR function was introduced in Excel 2013._

### Extending the formula

The basic idea in this formula can be extended in many clever ways. For example, the screenshot below shows a formula that returns a check mark only when all test scores are at least 65:

![Check mark if all values are at least 65](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/checkmark%20if%20all%20values%20at%20least%2065.png?itok=ulmBE774 "Check mark if all values are at least 65")

The formula in G5 is:

    =IF(NOT(COUNTIF(B5:F5,"<65")),"✓","")
    

The [NOT function](https://exceljet.net/functions/not-function)
 reverses the result from COUNTIF. If you find this confusing, you can alternately restructure the IF formula like this:

    =IF(COUNTIF(B5:F5,"<65"),"","✓")
    

In the version of the formula, the logic is more similar to the original formula above. However, we have moved the check mark to the _value\_if\_false_ argument, so the check mark will appear only if the count from COUNTIF is zero. In other words, the check mark will appear only when no values less than 65 are found.

_Note: you can also use [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
 to highlight valid or invalid input, and [data validation](https://exceljet.net/data-validation-formulas)
 to restrict input to allow only valid data._

Related formulas
----------------

[![Excel formula: All values in a range are at least](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/All%20values%20in%20a%20range%20are%20at%20least.png "Excel formula: All values in a range are at least")](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

### [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

At the core, this formula uses the COUNTIF function to count any cells that fall below a given value, which is hardcoded as 65 in the formula: COUNTIF(B5:F5,"<65") In this part of the formula, COUNTIF will return a positive number if any cell in the range is less than 65, and zero if not. In the...

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: If cell begins with x, y, or z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_begins_with_x_y_or_z_0.png "Excel formula: If cell begins with x, y, or z")](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

### [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

The goal is to take a specific action when a value begins with "x", "y", or "z". As is often the case in Excel, there are multiple ways to approach this problem. The simplest way is to use the OR function with the LEFT function to create the required logical test. Another option is to use the...

[![Excel formula: All cells in range are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all_cells_in_range_are_blank.png "Excel formula: All cells in range are blank")](https://exceljet.net/formulas/all-cells-in-range-are-blank)

### [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)

When working with Excel, there are times when you need to determine if a range of cells is empty. This can be useful in various scenarios, such as data validation, error checking, or report preparation. In this article, we'll explore a couple of formulas that can help you check if all cells in a...

[![Excel formula: Data validation must not exist in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20must%20not%20exist%20in%20list.png "Excel formula: Data validation must not exist in list")](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)

### [Data validation must not exist in list](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)

Data validation rules are triggered when a user adds or changes a cell value. In this case, the COUNTIF function is part of an expression that returns TRUE when a value does not exist in a defined list. The COUNTIF function simply counts occurrences of the value in the list. As long as the count is...

[![Excel formula: If complete show checkmark](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_complete_show_checkmark.png "Excel formula: If complete show checkmark")](https://exceljet.net/formulas/if-complete-show-checkmark)

### [If complete show checkmark](https://exceljet.net/formulas/if-complete-show-checkmark)

The goal is to display a checkmark (also called a "tick mark" in British English) when a task is marked complete. The easiest way to do this is with the IF function and the mark you would like to display. The article below explains several options. IF with a plain checkmark The simplest approach,...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    
*   [All cells in range are blank](https://exceljet.net/formulas/all-cells-in-range-are-blank)
    
*   [Data validation must not exist in list](https://exceljet.net/formulas/data-validation-must-not-exist-in-list)
    
*   [If complete show checkmark](https://exceljet.net/formulas/if-complete-show-checkmark)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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