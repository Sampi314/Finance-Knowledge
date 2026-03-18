# Extract date from text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-date-from-text-string

---

[Skip to main content](https://exceljet.net/formulas/extract-date-from-text-string#main-content)

[](https://exceljet.net/formulas/extract-date-from-text-string#)

*   [Previous](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Next](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Extract date from text string
=============================

by Dave Bruns · Updated 13 Sep 2024

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

[SEARCH](https://exceljet.net/functions/search-function)

[REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8475/download?token=9hEIWQLn)
 (18.3 KB)

![Excel formula: Extract date from text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract_date_from_text_string.png "Excel formula: Extract date from text string")

Summary
-------

To extract a date in a format like mm/dd/yy from a text string, you can use a formula based on the [SEARCH function](https://exceljet.net/functions/search-function)
 and the [MID function](https://exceljet.net/functions/mid-function)
. In the worksheet shown, the formula in cell D5 is:

    =MID(B5,SEARCH("??/??/??",B5),8)+0

As the formula is copied down, it extracts dates in mm/dd/yy format from the text in column B. The resulting value is then formatted as date.

_Note: the new [REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
 (currently in the beta channel of Excel 365) is a better way to solve this problem. See below for details._

Generic formula
---------------

    =MID(A1,SEARCH("??/??/??",A1),8)+0

Explanation 
------------

In this example, the goal is to extract a date in a format like mm/dd/yy from a text string with a formula. The position of the date is not known, so the date must be located as a first step. This article explains two ways to solve this challenge:

*   A "classic" formula based on the SEARCH function and the MID function that will work in any version of Excel.
*   A modern formula based on the REGEXEXTRACT function, which is only available in the Beta channel of Excel 365.

### Classic formula

In the worksheet shown, we are using a "classic" formula to extract dates from the text strings in column B. The formula in cell D5 looks like this:

    =MID(B5,SEARCH("??/??/??",B5),8)+0

At a high level, this formula uses the [SEARCH function](https://exceljet.net/functions/search-function)
 to locate the date and the [MID function](https://exceljet.net/functions/mid-function)
 to extract the date. MID is designed to extract a given number of characters from the middle of a text string. SEARCH will return the position of a matching value as a number. Working from the inside out, SEARCH is configured like this:

    SEARCH("??/??/??",B5)

Here, the find\_text is given as "??/??/??", and the within\_text is provided as B5. The SEARCH supports wildcards, and the "?" character means _any single character_. The pattern "??/??/??" means: _any two characters followed by a forward slash "/", followed by any two characters followed by a forward slash "/", followed by any two characters_.

The text in cell B5 is 57 characters long, and the date begins at character 37. The SEARCH function finds the date pattern and returns 37 as a result. This result lands inside the MID function as the _start\_num_. Simplifying, we now have:

    =MID(B5,37,8)+0

Inside the MID function, the text comes from cell B5, the _start\_num_ is 37, and _num\_chars_ is set to 8. We use 8 because a date in the format "mm/dd/yy" is eight characters. With this configuration, MID extracts 8 characters beginning at character 37, and we now have the date isolated, still in text format:

    ="06/15/24"+0

As a final step, we add zero. This is a simple hack to get a valid date from a text string. The math operation forces Excel's formula engine to try and convert the text "06/15/24" into a number. In this case, Excel recognizes that "06/15/24" as a date and performs the conversion. It then returns the serial number 45458, which is June 15, 2024, in [Excel's date system](https://exceljet.net/glossary/excel-date)
:

    =45458+0

Adding zero has no effect on the number, so the final result is 45458. The last step is to format the result using the date format "d-mmm-yyyy" which causes Excel to display the dates in column D as they appear. We can apply this formatting because we have converted text value into a valid Excel date. This format can be adjusted to display dates as desired. 

> Why add zero? When extracting a date from a text string using a formula, the result is initially returned as text. By adding zero (+0), we force Excel to interpret the text as a number, which automatically converts the text string into a valid Excel date. This step is important because Excel stores dates as serial numbers. Once converted, the date can be formatted and used in calculations like any other date value. Without this step, Excel would not recognize the text as a date.

Although this formula is fairly simple, it is not especially robust. For example, it will match the non-date "AA/BB/CC" and even "AAAA/BB/CCCC". It will also fail on dates in "mm/dd/yyyy" format since only the first two year digits of the year will be used, resulting in an incorrect year. If all dates use a 4-digit year, you can use the modified formula below:

    =MID(B5,SEARCH("??/??/????",B5),10)+0

See below for a more robust formula based on regex.

_Notes: (1) If you only want a text value (not an actual date), omit adding a zero._ _(2) This formula works because the [SEARCH function](https://exceljet.net/functions/search-function)
 supports wildcards, unlike the [FIND function](https://exceljet.net/functions/find-function)
._

### A modern formula based on regex

In the latest version of Excel, which offers the [REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
, we can build a more robust formula because regex patterns are much more specific than Excel's primitive wildcards. In the worksheet below, we are using REGEXEXTRACT to extract dates with a formula like this:

    =REGEXEXTRACT(B5,"\b\d{1,2}/\d{1,2}/\d{2,4}\b")+0

Inside REGEXEXTRACT, the _text_ is given as B5. The regex _pattern_ looks like this:

    "\b\d{1,2}/\d{1,2}/\d{2,4}\b"

Regular expressions (regex) are a language used to match and extract text patterns. Briefly, this is how the pattern works:

*   \\b: Matches a word boundary
*   \\d{1,2}: Matches one or two digits for the month
*   /: Matches the forward slash separator
*   \\d{1,2}: Matches one or two digits for the day
*   /: Matches the second forward slash separator
*   \\d{2,4}: Matches 2-4 digits for the year
*   \\b: Matches another word boundary

You can see how the formula works in the worksheet below:

![Using REGEXEXTRACT to extract dates from text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/extract_date_from_text_string_with_regex.png "Using REGEXEXTRACT to extract dates from text")

Notice we are now matching 4-digit years on rows 7 and 12, in addition to the other 2-digit years. Compared to the MID + SEARCH formula above, this formula does a better job of matching dates. It is more flexible in some ways but more restrictive in others. For example, it will match dates like "1/1/23", "01/01/23", and "5/25/2023", but it won't match a text string like "AA/BB/CC" or "1234/12/1234". However, note that the pattern _does not check_ that the month is between 1-12 or that the day is valid for the given month. It also doesn't validate the year in any way. It would, for example, allow a 3-digit year, which Excel won't interpret correctly. Since this is regex, we can easily make the pattern more specific. The revised formula below will only allow a 2-digit year OR a 4-digit year:

    =REGEXEXTRACT(B5,"\b\d{1,2}/\d{1,2}/(\d{2}|\d{4})\b")+0

In regex, there is always a way to tighten up edge cases at the cost of more complexity. However, even the initial regex formula above is much better than the traditional SEARCH + MID at preventing false matches. REGEXEXTRACT is a _huge upgrade_ to Excel's tools for matching and extracting text.

Related formulas
----------------

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

[![Excel formula: Join date and text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_date_and_text.png "Excel formula: Join date and text")](https://exceljet.net/formulas/join-date-and-text)

### [Join date and text](https://exceljet.net/formulas/join-date-and-text)

In this example, the goal is to join a text string to a formatted date. The challenge is that numbers lose their formatting in Excel when they are concatenated in a formula. For example, if we have the date 31-Dec-1999 in cell B5, and we join B5 to a text string and don't control the date format...

Related functions
-----------------

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel REGEXEXTRACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexextract_function.png "Excel REGEXEXTRACT function")](https://exceljet.net/functions/regexextract-function)

### [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)

The Excel REGEXEXTRACT function extracts matching text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXEXTRACT will return the first match, but...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    
*   [Join date and text](https://exceljet.net/formulas/join-date-and-text)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)
    

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