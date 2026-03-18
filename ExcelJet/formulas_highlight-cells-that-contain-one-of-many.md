# Highlight cells that contain one of many - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many

---

[Skip to main content](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many#main-content)

[](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many#)

*   [Previous](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Next](https://exceljet.net/formulas/highlight-cells-that-end-with)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight cells that contain one of many
========================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Highlight cells that contain one of many](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20cells%20that%20contain%20one%20of%20many.png "Excel formula: Highlight cells that contain one of many")

Summary
-------

To highlight cells that contain one of many text strings, you can use a formula based on the functions ISNUMBER and SEARCH, together with the SUMPRODUCT function. In the example shown, the conditional formatting applied to B4:B11 is based on this formula:

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,B4)))>0
    

Generic formula
---------------

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,A1)))>0

Explanation 
------------

Working from the inside out, this part of the formula searches each cell in B4:B11 for all values in the named range "things":

    --ISNUMBER(SEARCH(things,B4)
    

The SEARCH function returns the position of the value if found, and the #VALUE error if not found. For B4, the results come back in an array like this:

    {8;#VALUE!;#VALUE!}
    

The ISNUMBER function changes all results to TRUE or FALSE:

    {TRUE;FALSE;FALSE}
    

The double negative in front of ISNUMBER forces TRUE/FALSE to 1/0:

    {1;0;0}
    

The SUMPRODUCT function then adds up the results, which is then tested against zero:

    =SUMPRODUCT({1;0;0})>0
    

Any non-zero result means at least one value was found, so the formula returns TRUE, triggering the rule.

### Ignore empty things

To ignore empty cells in the named range "things", you can try a modified formula like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH(IF(things<>"",things),B4)))>0
    

This works as long as the text values you are testing don't contain the string "FALSE". If they do, you can extend the IF function to include a value if false known not to occur in the text (i.e. "zzzz", "####", etc.)

### Case-sensitive option

SEARCH is not case-sensitive. To check case as well, replace SEARCH with FIND like so:

    =SUMPRODUCT(--ISNUMBER(FIND(things,A1)))>0
    

### Preventing false matches

One problem with this approach is you may see false matches caused by substrings that appear inside longer words. For example, if you try to match "dr" you may also find "Andrea", "drink", "dry", etc. since "dr" appears inside these words. This happens because SEARCH automatically performs a "contains" match.

For a partial fix, you can add space around the search words (i.e. " dr ", or "dr ") to avoid catching "dr" in another word. But this will fail if "dr" appears first or last in a cell, or appears next to punctuation. This can be partially addressed by adding space also around the original text. To add space to the start and end of both at the same time, you can try a formula like this:

    =SUMPRODUCT(--ISNUMBER(FIND(" "&things&" "," "&B4&" ")))>0
    

However, this won't fix problems caused by punctuation.

If you need a more complete solution, one option is to [normalize the text](https://exceljet.net/formulas/normalize-text)
 first in a [helper column](https://exceljet.net/glossary/helper-column)
, taking care to also add a leading and trailing space. Then you can search for whole words surrounded by spaces.

Related formulas
----------------

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

### Articles

*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    

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