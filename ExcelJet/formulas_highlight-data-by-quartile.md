# Highlight data by quartile - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-data-by-quartile

---

[Skip to main content](https://exceljet.net/formulas/highlight-data-by-quartile#main-content)

[](https://exceljet.net/formulas/highlight-data-by-quartile#)

*   [Previous](https://exceljet.net/formulas/highlight-column-differences)
    
*   [Next](https://exceljet.net/formulas/highlight-dates-between)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight data by quartile
==========================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[QUARTILE](https://exceljet.net/functions/quartile-function)

![Excel formula: Highlight data by quartile](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20quartiles.png "Excel formula: Highlight data by quartile")

Summary
-------

To highlight cells by quartile, you can apply conditional formatting with a formula that uses the QUARTILE function.

In the example shown, we are using 4 different conditional formatting rules. Each rule highlights a quartile in the range B4:F11 using the QUARTILE function. The formulas look like this:

    =B4>QUARTILE(B4:F11,3)
    =B4>=QUARTILE(B4:F11,2)
    =B4>=QUARTILE(B4:F11,1)
    =B4>=QUARTILE(B4:F11,0)
    

Note that we are highlighting quartiles in a specific order, starting with quartile 4 and ending with quartile 1.

It's important that the formula be entered relative to the upper left most cell in the data, in this case cell B4.

Generic formula
---------------

    =A1>=QUARTILE(data,quart)

Explanation 
------------

The QUARTILE function is automatic, and will calculate the 1st quartile with an input of 1, the 2nd quartile with an input of 2, and the 3rd quartile with an input of 3. With an input of 0, quartile returns the minimum value in the data.

The trick in this case is to arrange the conditional formatting rules so that they run in the same direction. The first rule highlights values greater than the 3rd quartile. The second rule highlights values greater than the 2nd quartile, the 3rd rule highlights data greater than the 1st quartile, and the last rule highlights data greater than the minimum value.

Related functions
-----------------

[![Excel QUARTILE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_quartile.png "Excel QUARTILE function")](https://exceljet.net/functions/quartile-function)

### [QUARTILE Function](https://exceljet.net/functions/quartile-function)

The Excel QUARTILE function returns the quartile (each of four equal groups) for a given set of data. QUARTILE can return minimum value, first quartile, second quartile, third quartile, and max value.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

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

### Functions

*   [QUARTILE Function](https://exceljet.net/functions/quartile-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

### Articles

*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Conditional Formatting](https://exceljet.net/training/conditional-formatting)
    

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