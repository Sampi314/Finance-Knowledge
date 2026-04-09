# Histogram with FREQUENCY - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/histogram-with-frequency

---

[Skip to main content](https://exceljet.net/formulas/histogram-with-frequency#main-content)

[](https://exceljet.net/formulas/histogram-with-frequency#)

*   [Previous](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Next](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    

[Count](https://exceljet.net/formulas#Count)

Histogram with FREQUENCY
========================

by Dave Bruns · Updated 6 Nov 2020

Related functions 
------------------

[FREQUENCY](https://exceljet.net/functions/frequency-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6316/download?token=a0wvAvC8)
 (18.1 KB)

![Excel formula: Histogram with FREQUENCY](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Histogram%20with%20FREQUENCY.png "Excel formula: Histogram with FREQUENCY")

Summary
-------

One way to create a histogram is with the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
. In the example shown, the formula in cells G5:G8 is:

    {=FREQUENCY(data,bins)}
    

where **data** (C5:C16) and **bins** (F5:F8) are [named ranges](https://exceljet.net/glossary/named-range)
.

This formula is entered as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 in the range G5:G8.

Explanation 
------------

_Note: later versions of Excel include a [native histogram chart](https://exceljet.net/chart-types/histogram-chart)
, which is [easy to create](https://exceljet.net/videos/how-to-make-a-histogram-chart)
, but not as flexible to format. The example on this page shows one way to create your own histogram data with the FREQUENCY function and use a regular column chart to plot the results. Because FREQUENCY is a formula, the results and chart will dynamically update if data changes._

The [FREQUENCY function](https://exceljet.net/functions/frequency-function)
 returns a frequency distribution, which is a summary table that shows the count of each value in a range by "bin". FREQUENCY is a bit tricky to use, because must be entered as an [_array formula_](https://exceljet.net/glossary/array-formula)
. On the other hand, once you set up your bins correctly, FREQUENCY will give you all counts at once!

### Setup and formula

In the example shown, we have a list of 12 scores in the [named range](https://exceljet.net/glossary/named-range)
 "data" (C5:C16). The range F5:F8 is the named range "bins". FREQUENCY will treat each bin value as the _upper_ limit for that bin. In other words, each bin will include a count of scores up to and including the bin value. FREQUENCY will also return an "overflow count" – the count of values greater than the last bin.

To enter the FREQUENCY formula, follow these steps in the attached workbook.

1\. Delete existing formulas if needed (see note below).

2\. Select the range G5:G8 (all four cells).

3\. Paste or type this formula in the formula bar:

    =FREQUENCY(data,bins)
    

4\. Enter the formula as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter. Excel will automatically add curly braces {}. 

_Note: To edit existing formulas, you'll need to select all four cells first, then click Delete. You can select all cells at once with the [shortcut control + /](https://exceljet.net/shortcuts/select-current-array)
._

FREQUENCY will generate a count for each bin and return an [array](https://exceljet.net/glossary/array)
 of results like this:

    {2;4;5;1;0} // array returned by FREQUENCY
    

Excel will place the first 4 values in the range G5:G8. Notice the overflow count, zero, is also returned as the fifth element in the array, since there are no values greater than 100. This value is not shown in the worksheet, because we only entered the formula in four cells.

### Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, you can simply enter one formula in cell G5, and results will automatically [spill](https://exceljet.net/glossary/spill)
 onto the worksheet. There is no need to use control + shift + enter. However, if you use this approach, you will see the count for the overflow bin output as well. Entering the formula in 4 cells only (as above) suppresses this last value. If you don't mind the extra value, the single formula option is easier, and you can choose not to plot the value in a chart.

### Labels

The labels in E5:E8 are for readability and presentation only. These can be customized as you like. In the example shown, the formula in cell E5, copied down, is:

    =IF(F5=MIN(bins),"≤"&F5,F4+1&"-"&F5)
    

This formula simply builds a label for each bin using the bin values in column F.

### Histogram chart

To chart the output from FREQUENCY, follow these steps. First, hold down the control key and select two ranges: E4:E8, and G4:G8. Then insert a column chart (Insert > Charts > Clustered column):

![Inserting a clustered column chart](https://exceljet.net/sites/default/files/images/formulas/inline/Histogram%20with%20FREQUENCY%20insert%20column%20chart.png "Inserting a clustered column chart")

Next, right-click a bar, and format the data series to reduce the gap width to 5% (or as desired):

![Formatting data series to reduce gap](https://exceljet.net/sites/default/files/images/formulas/inline/Histogram%20with%20FREQUENCY%20format%20data%20series.png "Formatting data series to reduce gap")

Change the chart title as you like. In the example shown, we pick up the value in cell B2:

![Setting the chart title to cell B2](https://exceljet.net/sites/default/files/images/formulas/inline/Histogram%20with%20FREQUENCY%20set%20chart%20title.png "Setting the chart title to cell B2")

Final chart showing values plotted:

![Final chart with ranges visible](https://exceljet.net/sites/default/files/images/formulas/inline/Histogram%20with%20FREQUENCY%20final%20chart.png "Final chart with ranges visible")

### Histogram with Data Analysis ToolPak

Another way to create a histogram in Excel is to use the Data Analysis ToolPak add-in. This is a very simple method, and it works in older versions of Excel. However, one limitation is that the output is _static_, and won't update automatically if values in the data change. 

Related formulas
----------------

[![Excel formula: Basic in cell histogram](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20in%20cell%20histogram.png "Excel formula: Basic in cell histogram")](https://exceljet.net/formulas/basic-in-cell-histogram)

### [Basic in cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)

The REPT function simply repeats values. For example, this formula outputs 10 asterisks: =REPT("\*",10) // outputs \*\*\*\*\*\*\*\*\*\* You can use REPT to repeat any character(s) you like. In this example, we use the CHAR function to output a character with a code of 110. This character, when formatted with...

[![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")](https://exceljet.net/formulas/subtotal-by-color)

### [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below. Standard formula logic If color is being...

Related functions
-----------------

[![Excel FREQUENCY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20frequency%20function.png "Excel FREQUENCY function")](https://exceljet.net/functions/frequency-function)

### [FREQUENCY Function](https://exceljet.net/functions/frequency-function)

The Excel FREQUENCY function returns a frequency distribution, which is a list that shows the frequency of values at given intervals. FREQUENCY returns multiple values and must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control-shift-enter, except in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic in cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)
    
*   [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)
    

### Functions

*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    

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