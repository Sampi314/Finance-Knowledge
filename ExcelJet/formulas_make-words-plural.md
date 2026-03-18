# Make words plural - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/make-words-plural

---

[Skip to main content](https://exceljet.net/formulas/make-words-plural#main-content)

[](https://exceljet.net/formulas/make-words-plural#)

*   [Previous](https://exceljet.net/formulas/mac-address-format)
    
*   [Next](https://exceljet.net/formulas/most-frequent-text-with-criteria)
    

[Text](https://exceljet.net/formulas#Text)

Make words plural
=================

by Dave Bruns · Updated 25 Sep 2022

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[IFNA](https://exceljet.net/functions/ifna-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6891/download?token=_Y3VGwbY)
 (14.4 KB)

![Excel formula: Make words plural](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/make%20words%20plural.png "Excel formula: Make words plural")

Summary
-------

To make a singular noun plural based on a given number of items, you can use a formula based on [concatenation](https://exceljet.net/glossary/concatenation)
 and the [IFNA](https://exceljet.net/functions/ifna-function)
, [VLOOKUP,](https://exceljet.net/functions/vlookup-function)
 and [IF](https://exceljet.net/videos/the-if-function)
 functions. In the example shown, the formula in D5 copied down is:

    =B5&" "&IF(B5>1,IFNA(VLOOKUP(C5,wordtable,2,0),C5&"s"),C5)
    

where **wordtable** is the [named range](https://exceljet.net/glossary/named-range)
 F5:G11. If the number in column B is greater than 1, the result is a "pluralized" noun. If the number is one, the result is the original (singular) word.

Generic formula
---------------

    IF(n>1,IFNA(VLOOKUP(A1,wordtable,2,0),A1&"s"),A1)

Explanation 
------------

In this example, the goal is to make a noun plural when the number of items is greater than one. In many cases, a noun can be made plural by adding an "s". However, many nouns have an irregular plural form, and the main challenge is to handle these exceptions.

### Ingredients

In the example shown, the formula uses these ingredients:

*   [IF function](https://exceljet.net/functions/if-function)
     – to check the number of items
*   [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
     – to lookup irregular plural forms
*   [IFNA function](https://exceljet.net/functions/ifna-function)
     – to take action when there is no irregular form
*   [Concatenation](https://exceljet.net/glossary/concatenation)
     – to glue text together

_Note: There are many ways to solve a problem like this in Excel, and this is just one approach._

### Adding an "s"

In the simplest case, the only task is to add an "s" to the end of a word using [concatenation](https://exceljet.net/glossary/concatenation)
. This can be done with a formula like this:

    =C5&"s" // simple concatenation
    

The [ampersand operator](https://exceljet.net/glossary/math-operators)
 (&) is used to join an "s" to the word in column C.

However, we don't want to add an "s" unless the number in column B is greater than 1. For this, we can use the [IF function](https://exceljet.net/functions/if-function)
 to check the number in column B:

    =IF(B5>1,C5&"s"),C5)
    

In this version of the formula, we only add an "s" when the number in B5 is greater than 1. At this point, the formula handles the base case without trouble, but it won't handle words with irregular plural forms.

### Handling irregular forms

To handle words with an irregular plural form, we need to perform a lookup. In the example shown, we do this with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
:

    =VLOOKUP(C5,wordtable,2,0)
    

where **wordtable** is the [named range](https://exceljet.net/glossary/named-range)
 F5:G11. Here, we use VLOOKUP to locate a word in a table and return the irregular plural from the second column. Obviously, this only works when the table contains an entry for a given word. If a word _does not_ exist in the table, VLOOKUP will return a #N/A error, and we can use this error to take some other action. The trick is to [nest](https://exceljet.net/glossary/nesting)
 VLOOKUP inside the [IFNA function](https://exceljet.net/functions/ifna-function)
 to trap the error like this:

    =IFNA(VLOOKUP(C5,wordtable,2,0),other)
    

where "other" represents a different action. The idea is that words with an irregular plural form need to have an entry in the table. At this point in the formula, we know the word should be plural. If we check the table and can't find the word, we can assume the word does not have an irregular plural form and we can simply add an "s".

### Putting it all together

We now have all the pieces we need for a single formula:

1.  Make plural only when number > 1
2.  Handle a regular plural form
3.  Handle an irregular plural form

We now need to assemble these pieces together in a logical flow like this:

_If number is greater than one, make the word plural, otherwise, return the original word. When making a word plural, check a custom table first to see if there is an irregular form. If there is an irregular form, use it. If an entry is not found, simply add an "s"._

The formula that implements this logic looks like this:

    IF(B5>1,IFNA(VLOOKUP(C5,wordtable,2,0),C5&"s"),C5)
    

The formula that appears in the example performs one additional step: it [concatenates](https://exceljet.net/glossary/concatenation)
 the number from column B to the result from the formula above so that the number appears together with the plural form of the noun:

    =B5&" "&IF(B5>1,IFNA(VLOOKUP(C5,wordtable,2,0),C5&"s"),C5)
    

This results in a [text string](https://exceljet.net/glossary/text-value)
 like "3 apples" and it makes it easier to quickly check results.

_Note: if a noun has an irregular form but is not listed in the custom table, this formula will incorrectly add an "s". Therefore, all words with an irregular plural form that you want to handle must exist in the custom table. This is a limitation of the formula._

Related formulas
----------------

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

[![Excel formula: Join date and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_date_and_text.png "Excel formula: Join date and text")](https://exceljet.net/formulas/join-date-and-text)

### [Join date and text](https://exceljet.net/formulas/join-date-and-text)

In this example, the goal is to join a text string to a formatted date. The challenge is that numbers lose their formatting in Excel when they are concatenated in a formula. For example, if we have the date 31-Dec-1999 in cell B5, and we join B5 to a text string and don't control the date format...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Join date and text](https://exceljet.net/formulas/join-date-and-text)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

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