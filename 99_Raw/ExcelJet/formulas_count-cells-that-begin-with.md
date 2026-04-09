# Count cells that begin with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-begin-with

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-begin-with#main-content)

[](https://exceljet.net/formulas/count-cells-that-begin-with#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-are-not-blank)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that begin with
===========================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[LEFT](https://exceljet.net/functions/left-function)

[LEN](https://exceljet.net/functions/len-function)

[EXACT](https://exceljet.net/functions/exact-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7301/download?token=4bWVMfTM)
 (17.76 KB)

![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")

Summary
-------

To count the number of cells that begin with specific text, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with a wildcard. In the example shown, the formula in cell E5 is:

    =COUNTIF(data,D5)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. COUNTIF returns 3, since there are three cells that begin with "apx". Note that COUNTIF is _not_ case-sensitive. See below for a case-sensitive formula.

Generic formula
---------------

    =COUNTIF(range,"text*")

Explanation 
------------

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named **data**. 

### COUNTIF function

The simplest way to solve this problem is with the COUNTIF function and a wildcard. [COUNTIF supports three wildcards](https://exceljet.net/functions/countifs-function)
 that can be used in the _criteria_ [argument](https://exceljet.net/glossary/function-argument)
: question mark (?), asterisk(\*), or tilde (~). A question mark (?) matches any one character and an asterisk (\*) matches zero or more characters of any kind. The tilde (~) is an escape character to match _literal_ wildcards that may appear in **data**. In this example, we only need to use an asterisk (\*). 

To count cells in a range that contain "apple" anywhere, you can use a formula like this:

    =COUNTIF(range,"*apple*") // contain "apple" anywhere
    

To count cells in a range that begin with "apple" you can use a formula like this:

    =COUNTIF(range,"apple*") // begin with "apple"
    

In the worksheet shown, we use the criteria in column D directly like this:

    =COUNTIF(data,D5)
    

As the formula is copied down, COUNTIF returns the count of cells in **data** (B5:B16) that begin with the text seen in D5:D8, which already includes a wildcard. Notice that COUNTIF is _not_ case-sensitive. The text in D5:D8 is all lowercase, yet COUNTIFS happily matches the uppercase text in B5:B16.

### SUMPRODUCT function

Another way to solve this problem is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT(--(LEFT(data,LEN(D5))=D5))
    

![Count cells that begin with SUMPRODUCT and LEFT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20cells%20that%20begin%20with%20SUMPRODUCT%20and%20LEFT.png?itok=CrJxDOjS "Count cells that begin with SUMPRODUCT and LEFT")

Working from the inside out, the [LEFT](https://exceljet.net/functions/left-function)
 and [LEN](https://exceljet.net/functions/len-function)
 functions are used to extract the first few characters of each value in **data**:

    LEFT(data,LEN(D5))
    

Since the text in D5 is "apx", LEN returns 3, and LEFT returns the first 3 letters of all values in **data** in an [array](https://exceljet.net/glossary/array)
 like this:

    {"APX";"APX";"APX";"XKR";"XKR";"XKR";"XKR";"XED";"XED";"XED";"XED";"XED"}
    

Next, the result from LEFT is compared to the original value in D5. Since Excel is not case-sensitive by default, the result is an array of 12 TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Notice the TRUE values correspond to cells in **data** that begin with "apx".

Next, the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) converts the TRUE and FALSE values to 1s and 0s, and SUMPRODUCT sums the array and returns the result:

    =SUMPRODUCT({1;1;1;0;0;0;0;0;0;0;0;0}) // returns 3
    

The final result is 3, since there are three values in B5:B16 that begin with "apx".

### Case-sensitive option

Although the SUMPRODUCT formula is more complicated than the COUNTIF formula, the nice thing about using SUMPRODUCT is that we can easily include other functions if needed. For example, to make the formula case-sensitive, we can add the [EXACT function](https://exceljet.net/functions/exact-function)
. EXACT compares values like this:

    =EXACT("apple","apple") // returns TRUE
    =EXACT("apple","Apple") // returns FALSE
    

EXACT only returns TRUE when the two text strings have exactly the same case. We can use EXACT in the formula like this:

    =SUMPRODUCT(--EXACT(LEFT(data,LEN(D5)),D5))
    

This version of the formula uses the LEFT and LEN functions in the same way as the original formula above. The difference is that the EXACT function compares extracted text with the text in column D. Since EXACT _is_ case-sensitive, the entire formula becomes case-sensitive:

![Count cells that begin with SUMPRODUCT and EXACT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20cells%20that%20begin%20with%20SUMPRODUCT%20and%20EXACT.png?itok=4zlh2bfF "Count cells that begin with SUMPRODUCT and EXACT")

Notice the value in D6 remains lowercase, and the formula in E6 returns 0 as a result.

### SUMPRODUCT with FIND

In Excel, there is _always_ another way to skin the cat :) Here is another case-sensitive formula based on the FIND function:

    =SUMPRODUCT(--(IFERROR(FIND(D5,data,1),0)=1))
    

![Count cells that begin with SUMPRODUCT and FIND](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20cells%20that%20begin%20with%20SUMPRODUCT%20and%20FIND.png?itok=OUjyXER2 "Count cells that begin with SUMPRODUCT and FIND")

This is arguably the most elegant option, since we don't need the LEN function, the LEFT function, or the EXACT function at all. Because the [FIND function](https://exceljet.net/functions/find-function)
 is case-sensitive, we can configure FIND to look for the text in column D, and check if the result is 1, since 1 means the text was found starting at the first character.

However, one quirk of the FIND function is that it will return a #VALUE! error if the search text is not found, and this error will bubble up to the top and ruin our formula if we don't trap it. As a consequence, we have to involve the [IFERROR function](https://exceljet.net/functions/iferror-function)
, just to catch the error and return 0 when it occurs. This makes the formula a bit more cryptic. Still, I do like this formula.

Related formulas
----------------

[![Excel formula: Count cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20end%20with.png "Excel formula: Count cells that end with")](https://exceljet.net/formulas/count-cells-that-end-with)

### [Count cells that end with](https://exceljet.net/formulas/count-cells-that-end-with)

In this example, the goal is to count cells in the range B5:B16 that end with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Count cells equal to case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20case%20sensitive.png "Excel formula: Count cells equal to case sensitive")](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

### [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

In this example, the goal is to count codes in a case-sensitive way. The COUNTIF function and the COUNTIFS function are both good options for counting text values, but neither is case-sensitive, so they can't be used to solve this problem. The solution is to use the EXACT function to compare codes...

[![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

### [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions COUNTIF and COUNTIFS are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the FIND...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that end with](https://exceljet.net/formulas/count-cells-that-end-with)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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