# VLOOKUP with two client rates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-with-two-client-rates

---

[Skip to main content](https://exceljet.net/formulas/vlookup-with-two-client-rates#main-content)

[](https://exceljet.net/formulas/vlookup-with-two-client-rates#)

*   [Previous](https://exceljet.net/formulas/vlookup-with-numbers-and-text)
    
*   [Next](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP with two client rates
=============================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: VLOOKUP with two client rates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP%20with%20two%20client%20rates.png "Excel formula: VLOOKUP with two client rates")

Summary
-------

To lookup two different rates for the same client, and calculate a final charge, you can use a formula based on two VLOOKUP functions.

In the example shown, the formula in E5 is:

    =VLOOKUP(B5,rates,2,0)*C5+VLOOKUP(B5,rates,3,0)*D5
    

where "rates" is the named range G5:I8.

Generic formula
---------------

    =VLOOKUP(client,rates,col,0)*hrs+VLOOKUP(client,rates,col,0)*hrs

Explanation 
------------

This formula is composed of two lookups for the same client. The first lookup finds the onsite rate for the client in column B and multiplies the result by the number of hours in column C:

    =VLOOKUP(B5,rates,2,0)*C5
    

The second lookup finds the offsite rate for same client and multiplies the result by the number of hours in column D:

    VLOOKUP(B5,rates,3,0)*D5
    

In the final step the two results are added together:

    =(50*0)+(60*16)
    =960
    

Related formulas
----------------

[![Excel formula: VLOOKUP calculate shipping cost](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_shipping_cost.png "Excel formula: VLOOKUP calculate shipping cost")](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

### [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

This example shows how to use the VLOOKUP function to calculate the total shipping cost for an item in one formula, where the cost per kilogram (kg) varies according to weight. This requires an "approximate match" since in most cases the actual weight will not appear in the shipping cost table. For...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    

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