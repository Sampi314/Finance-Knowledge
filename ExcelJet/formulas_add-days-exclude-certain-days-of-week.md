# Add days exclude certain days of week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-days-exclude-certain-days-of-week

---

[Skip to main content](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week#main-content)

[](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week#)

*   [Previous](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Next](https://exceljet.net/formulas/add-days-to-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add days exclude certain days of week
=====================================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

![Excel formula: Add days exclude certain days of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Add%20days%20exclude%20certain%20days%20of%20week.png "Excel formula: Add days exclude certain days of week")

Summary
-------

To add days to a date while excluding specific days (i.e. exclude Tuesdays and Thursdays, Wednesdays only, etc.) you can use the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 with a special pattern code. In the example shown, the formula in C7 is:

    =WORKDAY.INTL(B7,7,"0101000")
    

This formula adds 7 days to the date in B7, excluding Tuesdays and Thursdays.

Generic formula
---------------

    =WORKDAY.INTL(date,days,"pattern")
    

Explanation 
------------

The [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 is based on the [WORKDAY function](https://exceljet.net/functions/workday-function)
, which is designed to add work days to a date. WORKDAY automatically excludes Saturday and Sunday, and optionally can exclude a list of custom holidays. The WORKDAY.INTL does the same thing, but makes it possible to exclude any days of the week, in addition to holidays.

To exclude specific days of the week you can either use a pre-configured code (see [this page](https://exceljet.net/functions/workday.intl-function)
 for a full list of presets) or provide your own "pattern code". The pattern code must be 7 digits long and have either a zero for each day of the week, starting on Monday and ending on Sunday. Values equal to 1 are _excluded,_ and days with zero values are treated normally.

So, assuming you want to add 7 days to a date in cell A1, you can write formulas like this:

    =WORKDAY.INTL(A1,7,"0000011") // exclude Sat, Sun
    =WORKDAY.INTL(A1,7,"0010011") // exclude Sat, Sun, Wed
    =WORKDAY.INTL(A1,7,"0101011") // exclude Sat, Sun, Tue, Thu
    

Related formulas
----------------

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

Related functions
-----------------

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    

### Functions

*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    

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