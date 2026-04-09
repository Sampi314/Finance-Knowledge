# Basic attendance tracking formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-attendance-tracking-formula

---

[Skip to main content](https://exceljet.net/formulas/basic-attendance-tracking-formula#main-content)

[](https://exceljet.net/formulas/basic-attendance-tracking-formula#)

*   [Previous](https://exceljet.net/formulas/basic-array-formula-example)
    
*   [Next](https://exceljet.net/formulas/basic-error-trapping-example)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic attendance tracking formula
=================================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Basic attendance tracking formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20attendance%20tracking%20formula.png "Excel formula: Basic attendance tracking formula")

Summary
-------

One way to track attendance is with simple formulas based on the COUNTIF function. In the example shown, the formula in M5 is:

    =COUNTIF(C5:L5,"x")
    

Generic formula
---------------

    =COUNTIF(range,"x")

Explanation 
------------

This formula simply uses COUNTIF with a criteria of "x" (not quotation marks) to count x's in each row, where "x" represents "present" and an empty cell represents "absent":

    =COUNTIF(C5:L5,"x") // count present
    

The count absent days, the worksheet uses COUNTIF again, configured to count empty cells:

    =COUNTIF(C5:L5,"") // count absent
    

Related formulas
----------------

[![Excel formula: Count cells equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to.png "Excel formula: Count cells equal to")](https://exceljet.net/formulas/count-cells-equal-to)

### [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)

In this example, the goal is to count cells equal to a specific value. In this case, we want to count cells that contain "red" in the range D5:D16. This problem can be solved with the COUNTIF function and the SUMPRODUCT function, as explained below. COUNTIF function One way to solve this problem is...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells equal to](https://exceljet.net/formulas/count-cells-equal-to)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    

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