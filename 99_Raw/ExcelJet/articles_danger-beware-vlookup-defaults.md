# Danger: beware VLOOKUP defaults | Exceljet

**Source:** https://exceljet.net/articles/danger-beware-vlookup-defaults

---

[Skip to main content](https://exceljet.net/articles/danger-beware-vlookup-defaults#main-content)

[](https://exceljet.net/articles/danger-beware-vlookup-defaults#)

*   [Previous](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [Next](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    

Danger: beware VLOOKUP defaults
===============================

by Dave Bruns · Updated 18 Oct 2023

![Danger: beware VLOOKUP defaults](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Beware%20VLOOKUP%20defaults.png "Danger: beware VLOOKUP defaults")

Summary
-------

Many users aren't aware of it, but VLOOKUP will use approximate match mode by default. This can be a disaster because VLOOKUP can return a totally incorrect result. Read below to learn how match modes work in VLOOKUP, and how to avoid this dangerous problem.

_By default, VLOOKUP will do an approximate match. This is a dangerous default because VLOOKUP may quietly return an incorrect result when it doesn't find your lookup value. Read below to see some examples of how VLOOKUP can cause trouble when you don't manage match behavior._

_Note: the [MATCH function](https://exceljet.net/functions/match-function)
 has this same behavior – match type is optional and defaults to approximate match._

When [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 is in approximate match mode, it assumes your table is sorted in ascending order, and does a binary search. As a result, when VLOOKUP finds a value that's _greater than the lookup value_, it will fall back, and match a previous value. In other words, it returns the last number that is _less than or equal to the lookup value_.

This is all fine and dandy when your data is sorted nicely, but it can be a disaster with unsorted data, because VLOOKUP might give you a totally incorrect result. Even worse, the result might look completely normal.

Video: Great video by Oz du Soleil on [how binary search really works in Excel](https://www.youtube.com/watch?v=GllJpJxOSvM)
.

To illustrate, here are two examples below, both of which show incorrect results with VLOOKUP in approximate match mode.

### Wrong match - example #1

In this example, there is no invoice 100235, but because VLOOKUP defaults to approximate match, it finds a result anyway.

![VLOOKUP approximate match wrong result 1 - missing value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20incorrect%20approximate%20match%20invoice.png?itok=f92p7jpS "VLOOKUP approximate match wrong result 1 - missing value")

### Wrong match - example #2

In the second example, VLOOKUP again is defaulting to an approximate match, since no 4th argument is supplied. VLOOKUP requires the table to be sorted when doing an approximate match, otherwise, results are unpredictable. In this case, the table isn't sorted and we simply get the wrong result (but note that there is no error):

![VLOOKUP approximate match wrong result 2  - not sorted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP%20incorrect%20approximate%20match%20email.png?itok=Qr1GJYwz "VLOOKUP approximate match wrong result 2  - not sorted")

### The fix

Both problems above can be fixed by forcing VLOOKUP to do an exact match. Just supply the 4th argument (_range\_lookup_) as FALSE or 0. In exact match mode, VLOOKUP will return the correct result if the lookup value is found and #N/A if not.

    =VLOOKUP(value,table,column) // danger, approximate match
    =VLOOKUP(value,table,column,0) // exact match
    

### Takeaway

Leaving VLOOKUP in its default mode can be dangerous. To avoid this problem, I recommend you always set the match mode explicitly as a reminder of what you expect. Also, when you do want to use approximate matching, _be sure your table is sorted_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    

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