# Create date range from two dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/create-date-range-from-two-dates

---

[Skip to main content](https://exceljet.net/formulas/create-date-range-from-two-dates#main-content)

[](https://exceljet.net/formulas/create-date-range-from-two-dates#)

*   [Previous](https://exceljet.net/formulas/count-times-in-a-specific-range)
    
*   [Next](https://exceljet.net/formulas/custom-weekday-abbreviation)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Create date range from two dates
================================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Create date range from two dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/create%20date%20range%20from%20two%20dates.png "Excel formula: Create date range from two dates")

Summary
-------

To display a date range in one cell based on dates in different cells, you can use a formula based on the TEXT function.

In the example shown, the formula in cell E5 is:

    =TEXT(B5,"mmm d")&" - "&TEXT(C5,"mmm d")
    

Generic formula
---------------

    =TEXT(date1,"format")&" - "&TEXT(date2,"format")

Explanation 
------------

The TEXT function takes numeric values and converts them to text values using the format you specify. In this example, we are using the format "mmm d" for both TEXT functions in E5. The results are joined with a hyphen using simple concatenation.

_Note: the other examples in column E all use different text formats._

### End date missing

If the end date is missing, the formula won't work correctly because the hyphen will still be appended to the start date (e.g."March 1 - ").

To handle this case, you can wrap the concatenation and second TEXT function inside IF like so:

    =TEXT(date1,"mmm d")&IF(date2<>""," - "&TEXT(date2,"mmm d"),"")
    

This creates the full date range when both dates are present, but outputs only the start date when the end date is missing.

### Start date missing

To handle a case where both dates are missing, you could nest another IF like this:

    =IF(date1<>"",TEXT(date1,"mmmm d")&IF(date2<>""," - "&TEXT(date2,"mmm d"),""),"")
    

This formula simply returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("") when date1 is not available.

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20formula%20with%20nested%20IFs-thumb.png)](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

### [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

In this video I'll show you how to create a formula that uses multiple, nested IF statements. This is a common technique to handle multiple conditions. Let's take a look. This worksheet shows a class of students with five test scores in columns D through H, and an average in column I. In column J...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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