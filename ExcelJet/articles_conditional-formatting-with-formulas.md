# Conditional formatting with formulas | Exceljet

**Source:** https://exceljet.net/articles/conditional-formatting-with-formulas

---

[Skip to main content](https://exceljet.net/articles/conditional-formatting-with-formulas#main-content)

[](https://exceljet.net/articles/conditional-formatting-with-formulas#)

*   [Previous](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    
*   [Next](https://exceljet.net/articles/nested-ifs)
    

Conditional formatting with formulas
====================================

by Dave Bruns · Updated 11 May 2024

![Conditional formatting with formulas](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/gantt%20chart%20weekends.png "Conditional formatting with formulas")

Summary
-------

Although Excel ships with many conditional formatting "presets", these are limited. A more powerful way to apply conditional formatting is with formulas, because formulas allow you to apply rules that use more sophisticated logic. This article shows 10 examples, including how to highlight rows, column differences, missing values, and how to build Gantt charts and search boxes with conditional formatting.

Quick Links
-----------

*   [Quick Start](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Examples](https://exceljet.net/conditional-formatting-formulas)
    
*   [Troubleshooting](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Training](https://exceljet.net/training/conditional-formatting)
    

Conditional formatting is a fantastic way to quickly visualize data in a spreadsheet. With conditional formatting, you can do things like highlight dates in the next 30 days, flag data entry problems, highlight rows that contain top customers, show duplicates, and more.

Excel ships with a large number of "presets" that make it easy to create new rules without formulas. However, you can also create rules with your own custom formulas. By using your own formula, you take over the condition that triggers a rule and can apply exactly the logic you need. Formulas give you maximum power and flexibility.

For example, using the "Equal to" preset, it's easy to highlight cells equal to "apple".

But what if you want to highlight cells equal to "apple" or "kiwi" or "lime"? Sure, you can create a rule for each value, but that's a lot of trouble. Instead, you can simply use one rule based on a formula with the [OR function](https://exceljet.net/functions/or-function)
:

![A rule to highlight x, y, or z](https://exceljet.net/sites/default/files/images/articles/inline/highlight%20z%20or%20y%20or%20z%20rule%20short.png "A rule to highlight x, y, or z")

Here's the result of the rule applied to the range B4:F8 in this spreadsheet:

![Conditional formatting with the OR function](https://exceljet.net/sites/default/files/images/articles/inline/highlight%20z%20or%20y%20or%20z.png "Conditional formatting with the OR function")

Here's the exact formula used:

    =OR(B4="apple",B4="kiwi",B4="lime")
    

Quick start
-----------

You can create a formula-based conditional formatting rule in four easy steps:

1\. Select the cells you want to format.

![Select the cells to format](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20odd%20numbers%20select.png "Select the cells to format")

2\. Create a conditional formatting rule, and select the Formula option

![Select the formula option](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20odd%20numbers%20new%20rule%20formula.png "Select the formula option")

3\. Enter a formula that returns TRUE or FALSE.

![Enter the formula relative to the active cell](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20odd%20numbers%20new%20add%20formula.png "Enter the formula relative to the active cell")

4\. Set formatting options and save the rule.

![Set formatting options](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20odd%20numbers%20new%20set%20format.png "Set formatting options")

The [ISODD function](https://exceljet.net/functions/isodd-function)
 only returns TRUE for odd numbers, triggering the rule:

![The ISODD function returns TRUE for odd numbers, triggering the rule](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20odd%20numbers%20new%20rule%20done.png "The ISODD function returns TRUE for odd numbers, triggering the rule")

Video: [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

> We also offer [video training on conditional formatting](https://exceljet.net/training)
> .

Formula logic
-------------

Formulas that apply conditional formatting must return TRUE or FALSE, or numeric equivalents. Here are some examples:

    =ISODD(A1)
    =ISNUMBER(A1)
    =A1>100
    =AND(A1>100,B1<50)
    =OR(F1="MN",F1="WI")
    

The above formulas all return TRUE or FALSE, so they work perfectly as a trigger for conditional formatting.

When conditional formatting is applied to a range of cells, enter cell references with respect to the upper-left cell. The trick to understanding how conditional formatting formulas work is to visualize the same formula being applied to _each cell in the selection_, with cell references updated as usual. Imagine that you entered the formula in the upper-left cell of the selection, and then copied the formula across the entire selection. If you struggle with this, see the section on [Dummy Formulas](https://exceljet.net/articles/conditional-formatting-with-formulas#dummyformulas)
 below.

Formula Examples
----------------

Below are examples of custom formulas you can use to apply conditional formatting. Some of these examples can be created using Excel's built-in presets for highlighting cells, but custom formulas can go far beyond presets, as you can see below.

> Also see: [More than 30 Conditional Formatting Formulas](https://exceljet.net/conditional-formatting-formulas)

### Highlight orders from Texas

To highlight rows that represent orders from Texas (abbreviated TX), use a formula that locks the reference to column F:

    =$F5="TX"
    

![Use a formula to highlight rows where state = "TX"](https://exceljet.net/sites/default/files/images/articles/inline/highlight%20orders%20from%20texas.png "Use a formula to highlight rows where state = "TX"")

For more details, see this article: [Highlight rows with conditional formatting](https://exceljet.net/formulas/highlight-entire-rows)
.

Video: [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### Highlight dates in the next 30 days 

To highlight dates occurring in the next 30 days, we need a formula that (1) makes sure dates are in the future and (2) makes sure dates are 30 days or less from today. One way to do this is to use the [AND function](https://exceljet.net/functions/and-function)
 together with the [NOW function](https://exceljet.net/functions/now-function)
 like this:

    =AND(B4>NOW(),B4<=(NOW()+30))
    

With a current date of August 18, 2016, the conditional formatting highlights dates as follows:

![Conditional formatting to highlight dates in the next 30 days](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20dates%20in%20the%20next%2030%20days.png "Conditional formatting to highlight dates in the next 30 days")

The [NOW function](https://exceljet.net/functions/now-function)
 returns the current date and time. For details about how this formula, works, see this article: [Highlight dates in the next N days](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)
.

### Highlight column differences 

Given two columns that contain similar information, you can use conditional formatting to spot subtle differences. The formula used to trigger the formatting below is:

    =$B4<>$C4
    

![Conditional formatting to compare columns](https://exceljet.net/sites/default/files/images/articles/inline/Compare%20columns%20and%20highlight%20differences.png "Conditional formatting to compare columns")

See also: [a version of this formula that uses the EXACT function to do a case-sensitive comparison](https://exceljet.net/formulas/highlight-column-differences)
.

### Highlight missing values

To highlight values in one list that are missing from another, you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
:

    =COUNTIF(list,B5)=0
    

![Highlight missing values with conditional formatting](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20missing%20values.png "Highlight missing values with conditional formatting")

This formula simply checks each value in **List A** against values in the named range "list" (D5:D10). When the count is zero, the formula returns TRUE and triggers the rule, which highlights values in **List A** that are missing from **List B**.

Video: [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

### Highlight properties with 3+ bedrooms under $350k

To find properties in this list that have at least 3 bedrooms but are less than $300,000, you can use a formula based on the AND function:

    =AND($C5<350000,$D5>=3)
    

The dollar signs ($) lock the reference to columns C and D, and the [AND function](https://exceljet.net/functions/and-function)
 is used to make sure both conditions are TRUE. In rows where the AND function returns TRUE, the conditional formatting is applied:

![Conditional formatting to highlight property listings](https://exceljet.net/sites/default/files/images/articles/inline/Highlight%20properties.png "Conditional formatting to highlight property listings")

### Highlight top values (dynamic example)

Although Excel has presets for "top values", this example shows how to do the same thing with a formula, and how formulas can be more flexible. By using a formula, we can make the worksheet interactive — when the value in F2 is updated, the rule instantly responds and highlights new values.

![Dynamic conditional formatting for top values](https://exceljet.net/sites/default/files/images/articles/inline/highlight%20top%20values.png "Dynamic conditional formatting for top values")

The formula used for this rule is:

    =B4>=LARGE(data,input)
    

Where "data" is the named range  B4:G11, and "input" is the named range F2. This page has [details and a full explanation](https://exceljet.net/formulas/highlight-top-values)
.

### Gantt charts

Believe it or not, you can even use formulas to create simple Gantt charts with conditional formatting like this:

![Using conditional formatting to create a Gantt chart](https://exceljet.net/sites/default/files/images/articles/inline/gantt%20chart%20weekends.png "Using conditional formatting to create a Gantt chart")

This worksheet uses two rules, one for the bars, and one for the weekend shading:

    =AND(D$4>=$B5,D$4<=$C5) // bars
    =WEEKDAY(D$4,2)>5 // weekends
    

[This article explains the formula for bars](https://exceljet.net/formulas/gantt-chart)
, and [this article explains the formula for weekend shading](https://exceljet.net/formulas/gantt-chart-with-weekends)
.

### Simple search box

One cool trick you can do with conditional formatting is to build a simple search box. In this example, a rule highlights cells in column B that contain text typed in cell F2:

![Conditional formatting search box](https://exceljet.net/sites/default/files/images/articles/inline/cells%20that%20contain%20specific%20text.png "Conditional formatting search box")

The formula used is:

    =ISNUMBER(SEARCH($F$2,B2))
    

For more details and a full explanation, see:

*   Article: [How to highlight cells that contain specific text](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   Article: [How to highlight rows that contain specific text](https://exceljet.net/formulas/highlight-rows-that-contain)
    
*   Video: [How to build a search box to highlight data](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

Troubleshooting
---------------

If you can't get your conditional formatting rules to fire correctly, there's most likely a problem with your formula. First, make sure you started the formula with an equals sign (=). If you forget this step, Excel will silently convert your entire formula to text, rendering it useless. To fix, just remove the double quotes Excel added at either side and make sure the formula begins with equals (=).

If your formula is entered correctly but is not triggering the rule, you may have to dig a little deeper. Normally, you can use the F9 key to check results in a formula or use the Evaluate feature to step through a formula. Unfortunately, you can't use these tools with conditional formatting formulas, but you can use a technique called "dummy formulas".

### Dummy Formulas

Dummy formulas are a way to test your conditional formatting formulas directly on the worksheet, so you can see what they're actually doing. This can be a big time-saver when you're struggling to get cell references working correctly.

In a nutshell, you enter the same formula across a range of cells that matches the shape of your data. This lets you see the values returned by each formula, and it's a great way to visualize and understand how formula-based conditional formatting works. For a detailed explanation, [see this article](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
.

[![Use dummy formulas to check conditional formatting formulas](https://exceljet.net/sites/default/files/images/articles/inline/conditional%20formatting%20dummy%20formulas.png "Use dummy formulas to check conditional formatting formulas")](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)

Video: [Test conditional formatting with dummy formulas](https://exceljet.net/videos/how-to-test-conditional-formatting-with-dummy-formula)

Limitations
-----------

There are some limitations that come with formula-based conditional formatting:

1.  You can't apply icons, color scales, or data bars with a custom formula. You are limited to standard cell formatting, including number formats, font, fill color, and border options.
2.  You can't use certain formula constructs like unions, intersections, or array constants for conditional formatting criteria.
3.  You can't reference other workbooks in a conditional formatting formula.

You can sometimes work around #2 and #3. You may be able to move the logic of the formula into a cell in the worksheet, and then refer to that cell in the formula instead. If you are trying to use an array constant, try creating a named range instead.

More CF formula resources
-------------------------

*   [More than 30 conditional formatting formulas examples](https://exceljet.net/conditional-formatting-formulas)
    
*   [Video training with practice worksheets](https://exceljet.net/training)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    

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