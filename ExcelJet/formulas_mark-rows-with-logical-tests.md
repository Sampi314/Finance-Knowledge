# Mark rows with logical tests - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/mark-rows-with-logical-tests

---

[Skip to main content](https://exceljet.net/formulas/mark-rows-with-logical-tests#main-content)

[](https://exceljet.net/formulas/mark-rows-with-logical-tests#)

*   [Previous](https://exceljet.net/formulas/lookup-last-file-revision)
    
*   [Next](https://exceljet.net/formulas/most-frequently-occurring-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Mark rows with logical tests
============================

by Dave Bruns · Updated 20 Jun 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6893/download?token=94pGZXgq)
 (14.23 KB)

![Excel formula: Mark rows with logical tests](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Mark%20rows%20with%20logical%20tests.png "Excel formula: Mark rows with logical tests")

Summary
-------

To mark or flag data records directly based on logical tests, you can use a formula based on the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 and the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in cell E5 is:

    =IF(COUNTIFS(name,B5,drink,"coffee"),"Y","N")
    

where **name** (B5:B16) and **drink** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =IF(COUNTIFS(range1,criteria1,range2,criteria2),"Y","N")
    

Explanation 
------------

In this example, the goal is to mark or flag certain records in a data set based on one or more [logical conditions](https://exceljet.net/glossary/logical-test)
. In each case, the result should be "Y" for "Yes" or "N" for "No". The data represents drinks purchased by five people on different days. Note that most people appear more than once in the data. For each name, we are checking for three separate conditions:

1.  Have they purchased tea?
2.  Have they purchased coffee?
3.  Have they purchased both coffee and tea?

Note these conditions apply to all the data available for each person. To make the formulas easier to set up, we have two [named ranges](https://exceljet.net/glossary/named-range)
 to work with: **name** (B5:B16) and **drink** (D5:D16). Also, note that we are using names as a unique identifier for convenience only. Normally, data like this will include some sort of unique ID for each person.

### Coffee

To check if a person has ever purchased coffee, we need to look for a specific name in the same row as "coffee". Essentially, we want to count rows where a given name appears with "coffee". We can do this with the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 configured with two conditions like this:

    COUNTIFS(name,B5,drink,"coffee") // returns 3
    

We are checking for the name in B5 ("Juan") in **names** (B5:B16), and "coffee" in **drinks** (D5:D16). COUNTIFS joins these conditions with AND logic, so the result is a count of all records where the name is "Juan" and the drink is "coffee" (3). To get a result of "Y" for "Yes" or "N" for "No", we [nest](https://exceljet.net/glossary/nesting)
 the COUNTIFS function inside the [IF function](https://exceljet.net/videos/the-if-function)
 like this:

    =IF(COUNTIFS(name,B5,drink,"coffee"),"Y","N")
    

Note we are using the COUNTIFS formula as the logical test inside the IF function. COUNTIFS won't return TRUE and FALSE, but rather a number that represents a count. When supplied conditions are met, the result will be a non-zero number. If no records meet supplied conditions, COUNTIFS will return zero. [Excel will evaluate any non-zero number as TRUE and zero as FALSE](https://exceljet.net/videos/introduction-to-booleans)
. In cell E5, the formula is solved like this:

    =IF(COUNTIFS(name,B5,drink,"coffee"),"Y","N")
    =IF(3,"Y","N")
    ="Y"
    

Note the result for "Juan" and "Coffee", "Y", will be the same in all rows where the name is "Juan". This is a global test applied with all data considered.

### Tea

To check if a person has ever purchased tea, we use the same approach. In this case, however, we want to check for rows where a given name appears with "tea". The formula in cell F5 is:

    =IF(COUNTIFS(name,B5,drink,"tea"),"Y","N")
    

Note the structure is the same as the formula in cell E5: [COUNTIFS](https://exceljet.net/functions/countifs-function)
 is used to count records that meet two conditions and delivers a numeric count to the [IF function](https://exceljet.net/functions/if-function)
, which returns a final result. In cell F5, the formula is solved like this:

    =IF(COUNTIFS(name,B5,drink,"tea"),"Y","N")
    =IF(0,"Y","N")
    ="N"
    

Note in this case the count from COUNTIFS is zero, since Juan never purchased tea, and IF evaluates zero as FALSE and returns "N".

### Coffee and Tea

To check if a person has purchased _both_ coffee and tea, we can use the [AND function](https://exceljet.net/functions/and-function)
 for the logical test. The formula in G5 is:

    =IF(AND(E5="Y",F5="Y"),"Y","N")
    

Here, we are using the AND function to check the already calculated results in columns E and F for convenience and efficiency. For a standalone version of this formula, we could use the COUNTIFS function twice in one formula like this:

    =IF(AND(COUNTIFS(name,B5,drink,"coffee"),COUNTIFS(name,B5,drink,"tea")),"Y","N")
    

As before, the AND function will evaluate any non-zero number as TRUE and zero as FALSE. In cell G5, the formula is evaluated like this:

    =IF(AND(COUNTIFS(name,B5,drink,"coffee"),COUNTIFS(name,B5,drink,"tea")),"Y","N")
    =IF(AND(3,0),"Y","N")
    =IF(FALSE,"Y","N")
    ="N"
    

The result is "N" because although Juan has purchased coffee 3 times, he has never purchased tea.

Related formulas
----------------

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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