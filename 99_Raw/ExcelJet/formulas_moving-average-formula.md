# Moving average formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/moving-average-formula

---

[Skip to main content](https://exceljet.net/formulas/moving-average-formula#main-content)

[](https://exceljet.net/formulas/moving-average-formula#)

*   [Previous](https://exceljet.net/formulas/basic-average-example)
    
*   [Next](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)
    

[Average](https://exceljet.net/formulas#Average)

Moving average formula
======================

by Dave Bruns · Updated 17 Jul 2023

Related functions 
------------------

[OFFSET](https://exceljet.net/functions/offset-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[MIN](https://exceljet.net/functions/min-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6226/download?token=VlMShRuC)
 (32.42 KB)

![Excel formula: Moving average formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/moving%20average%20formula.png "Excel formula: Moving average formula")

Summary
-------

To calculate a moving or rolling average, you can use a simple formula based on the [AVERAGE function](https://exceljet.net/functions/average-function)
 with relative references. In the example shown, the formula in E7 is:

    =AVERAGE(C5:C7)
    

As the formula is copied down, it calculates a 3-day moving average based on the sales value for the current day and the two previous days.

[Below is a more flexible](https://exceljet.net/formulas/moving-average-formula#offset_example)
 option based on the [OFFSET function](https://exceljet.net/functions/offset-function)
 which handles variable periods.

### About moving averages

A moving average (also called a rolling average) is an average based on subsets of data at given intervals. Calculating an average at specific intervals smooths out the data by reducing the impact of random fluctuations. This makes it easier to see overall trends, especially in a chart. The larger the interval used to calculate a moving average, the more smoothing that occurs, since more data points are included in each calculated average.

Explanation 
------------

The formulas shown in the example all use the AVERAGE function with a relative reference set up for each specific interval. The 3-day moving average in E7 is calculated by feeding AVERAGE a range that includes the current day and the two previous days like this:

    =AVERAGE(C5:C7) // 3-day average
    

The 5-day and 7-day averages are calculated in the same way. In each case, the range provided to AVERAGE is enlarged to include the required number of days:

    =AVERAGE(C5:C9) // 5-day average
    =AVERAGE(C5:C11) // 7-day average
    

All formulas use a [relative reference](https://exceljet.net/glossary/relative-reference)
 for the range supplied to the AVERAGE function. As the formulas are copied down the column, the range changes at each row to include the values needed for each average.

When the values are plotted in a line chart, the smoothing effect is clear:

![Moving average chart example](https://exceljet.net/sites/default/files/images/formulas/inline/moving%20average%20chart.png "Moving average chart example")

### Insufficient data

If you start the formulas in the _first_ row of the table, the first few formulas won't have enough data to calculate a complete average, because the range will extend _above_ the first row of data:

![Moving average range problem](https://exceljet.net/sites/default/files/images/formulas/inline/moving%20average%20range%20problem.png "Moving average range problem")

This may or may not be an issue, depending on the structure of the worksheet, and whether it's important that all averages are based on the same number of values. The AVERAGE function will automatically ignore text values and empty cells, so it will continue to calculate an average with fewer values. This is why it "works" in E5 and E6.

One way to clearly indicate insufficient data is to check the current row number and abort with #NA when there are less than n values. For example, for the 3-day average, you could use:

    =IF(ROW()-ROW($C$5)+1<3,NA(),AVERAGE(C3:C5))
    

The first part of the formula simply generates a "normalized" row number, starting with 1:

    ROW()-ROW($C$5)+1  // relative row number
    

In row 5, the result is 1, in row 6 the result is 2, and so on.

When the current row number is less than 3, the formula returns #N/A. Otherwise, the formula returns a moving average as before. This mimics the behavior of the Analysis Toolpak version of Moving Average, which outputs #N/A until the first complete period is reached.

![Moving average with #n/a for insufficient data](https://exceljet.net/sites/default/files/images/formulas/inline/moving%20average%20with%20na%20for%20insufficient%20data.png "Moving average with #n/a for insufficient data")

However, as the number of periods increases, you will eventually run out of rows above the data and won't be able to enter the required range inside AVERAGE. For example, you can't set up a moving 7-day average with the worksheet as shown, since you can't enter a range that extends 6 rows above C5.

### Variable periods with OFFSET

A more flexible way to calculate a moving average is with the OFFSET function. OFFSET can create a dynamic range, which means we can set up a formula where the number of periods is variable. The general form is:

    =AVERAGE(OFFSET(A1,0,0,-n,1))
    

where n is the number of periods to include in each average. As above, OFFSET returns a range that is passed into the AVERAGE function. Below you can see this formula in action, where **n** is the [named range](https://exceljet.net/glossary/named-range)
 E2. Starting at cell C5, OFFSET constructs a range that extends back to previous rows. This is accomplished by using a height equal to negative **n**. When E5 is changed to another number, the moving average recalculates on all rows:

![Moving average with OFFSET function](https://exceljet.net/sites/default/files/images/formulas/inline/moving%20average%20with%20offset%20function.png "Moving average with OFFSET function")

The formula in E5, copied down, is:

    =AVERAGE(OFFSET(C5,0,0,-n,1))
    

Like the original formula above, the version with OFFSET will also have the problem of insufficient data in the first few rows, depending on how many periods are given in E5.

In the example shown, the averages calculate successfully because the AVERAGE function _automatically ignores text values and blank cells_, and there are no other numeric values above C5. So, while the range passed into AVERAGE in E5 is C1:C5, there is only one value to average, 100. However, as periods increase, OFFSET will continue to create a range that extends _above the start of the data_, eventually running into the top of the worksheet and returning a #REF error.

One solution is to "cap" the size of the range to the number of data points available. This can be done by using the MIN function to restrict the number used for height as seen below:

![Moving average with OFFSET function and capped range](https://exceljet.net/sites/default/files/images/formulas/inline/moving%20average%20with%20offset%20function%20and%20capped%20range.png "Moving average with OFFSET function and capped range")

    =AVERAGE(OFFSET(C5,0,0,-(MIN(ROW()-ROW($C$5)+1,n)),1))
    

This looks pretty scary but is actually quite simple. We are limiting the height passed into OFFSET with the [MIN function](https://exceljet.net/functions/min-function)
:

    MIN(ROW()-ROW($C$5)+1,n)
    

Inside MIN, the first value is a [relative row number](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
, calculated with:

    ROW()-ROW($C$5)+1 // relative row number..1,2,3, etc.
    

The second value given to MIN is the number of periods, n. When the relative row number is less than n, MIN returns the current row number to OFFSET for height. When the row number is greater than n, MIN returns n. In other words, MIN simply returns the smaller of the two values.

A nice feature of the OFFSET option is that n can be easily changed. If we change n to 7 and plot the results, we get a chart like this:

![Moving average chart with OFFSET function](https://exceljet.net/sites/default/files/images/formulas/inline/moving%20average%20chart%20with%20offset%20function.png "Moving average chart with OFFSET function")

_Note: A quirk with the OFFSET formulas above is that they won't work in Google Sheets, because the OFFSET function in Sheets won't allow a negative value for height or width. The attached spreadsheet has workaround formulas for Google Sheets._

Related formulas
----------------

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

### [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

In this example, the goal is to sum the largest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

Related functions
-----------------

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    

### Functions

*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

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