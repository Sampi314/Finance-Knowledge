# Formula to list weekends only | Exceljet

**Source:** https://exceljet.net/articles/formula-to-list-weekends-only

---

[Skip to main content](https://exceljet.net/articles/formula-to-list-weekends-only#main-content)

[](https://exceljet.net/articles/formula-to-list-weekends-only#)

*   [Previous](https://exceljet.net/articles/excel-data-validation-guide)
    
*   [Next](https://exceljet.net/articles/build-friendly-messages-with-concatenation)
    

Formula to list weekends only
=============================

by Dave Bruns · Updated 19 Oct 2023

![Generate weekend dates only with a simple formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/how_to_generate_a_list_of_weekends.jpeg)

Summary
-------

Sure, you can use a complicated WEEKDAY formula to generate a list of weekends. But with WORKDAY.INTL, you can do the same thing with a WAY simpler formula. The trick is to use a special 7-digit "mask" to filter out all dates except weekends.

_In a world where everyday is Saturday or Sunday...._

Here's a little puzzle for you...how can you use Excel to generate a list of dates that are weekends only? For example, a list of Saturday Sunday pairs like this:

![Example list of weekend dates only](https://exceljet.net/sites/default/files/images/articles/inline/list%20of%20weekend%20dates%20example1.png "Example list of weekend dates only")

A couple years ago, I found and [described a formula](https://exceljet.net/formulas/sequence-of-weekends)
 that will do it using the WEEKDAY function and some tricky date logic handled with IF:

    =IF(WEEKDAY(A1)=7,A1+1,A1+(7-WEEKDAY(A1)))
    

With a date in A1, you can enter the formula in A2 and drag down to get your list of weekend dates.

This formula works fine, but it's overly complicated. As a smart reader pointed out recently, you can do the same thing with the WORKDAY.INTL function and a much simpler formula:

    =WORKDAY.INTL(A1,1,"1111100")
    

This takes advantage of what I call the "mask" feature of WORKDAY.INTL, which allows you to designate \*any\* day of the week as a weekend. The logic may seem a little backwards, but basically 1 means "weekend" and 0 means "not weekend". So, "1111100" effectively filters out all days except Saturday and Sunday by telling WORKDAY.INTL that Mon-Fri are weekends.

![Using WORKDAY.INTL to generate weekend dates only](https://exceljet.net/sites/default/files/images/articles/inline/workday.intl%20function%20weekends%20only.png "Using WORKDAY.INTL to generate weekend dates only")

What I love about this example is how an initially complicated formula "collapses" into a simple solution.

Excel is full of hidden gems like this that can drastically simplify your work. The trick is of course is finding them :)

By the way, the [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
 function also supports same 7-digit mask feature.

### More formula info

1.  [More about WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
    
2.  [Calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
     (video)
3.  [More formula examples](https://exceljet.net/formulas)
    
4.  [Excel formula training](https://exceljet.net/training/core-formula)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

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