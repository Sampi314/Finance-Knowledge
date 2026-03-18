# Articles | Exceljet

**Source:** https://exceljet.net/articles

---

[Skip to main content](https://exceljet.net/articles#main-content)

[](https://exceljet.net/articles#)

Articles
========

Filter by

Select topicChartsConditional FormattingExcel TablesFormulasModelingPivot TablesPower QueryProductivityShortcuts

[Formulas](https://exceljet.net/articles?tag=26)

[How to replace Excel's DATEDIF function](https://exceljet.net/articles/how-to-replace-excels-datedif-function)

----------------------------------------------------------------------------------------------------------------

Excel's DATEDIF function is widely used for calculating the difference between two dates in years, months, or days, but it will silently return buggy results in specific cases. DATEDIF2 is a custom LAMBDA function that replaces DATEDIF with reliable date arithmetic. This article explains the problems with DATEDIF, walks through the DATEDIF2 formula step by step, and shows where the two functions differ.

[Seeded Random Number Generator in Excel](https://exceljet.net/articles/seeded-random-number-generator-in-excel)

-----------------------------------------------------------------------------------------------------------------

How to keep random numbers from changing in Excel? Excel's random functions like RAND and RANDARRAY recalculate every time you edit your worksheet, making it impossible to maintain stable random results. This article shows you how to build a seeded random number generator using Excel's LAMBDA function, allowing you to generate reproducible random numbers that only change when you want them to. Perfect for scenarios like randomly assigning students to groups or any situation where you need consistent, repeatable random results.

[Formulas](https://exceljet.net/articles?tag=26)

[Modeling the 4 Percent Retirement Rule in Excel](https://exceljet.net/articles/modeling-the-4-percent-retirement-rule-in-excel)

---------------------------------------------------------------------------------------------------------------------------------

The 4% retirement rule suggests you can safely withdraw 4% of your portfolio in year one of retirement, then adjust that amount for inflation each year for 30 years without running out of money. But how does this actually play out year by year? This article builds a complete Excel model to find out, exploring three different approaches, from classic row-by-row formulas to modern dynamic arrays to a single formula that generates the entire 30-year schedule. These models are fully functional, so you can play with the inputs and see how things work yourself.

[Formulas](https://exceljet.net/articles?tag=26)

[Native checkboxes in Excel](https://exceljet.net/articles/native-checkboxes-in-excel)

---------------------------------------------------------------------------------------

If you've ever tried to create a to-do list, survey, or any kind of checklist in Excel, you've probably wished for a simple checkbox feature. Well, your wish has finally come true. Microsoft has finally introduced a native checkbox feature in Excel. It's easy to use and a great way to make your spreadsheets more interactive.

[Formulas](https://exceljet.net/articles?tag=26)

[Why some Excel functions won't spill](https://exceljet.net/articles/why-some-excel-functions-wont-spill)

----------------------------------------------------------------------------------------------------------

Ever wonder why some Excel functions stubbornly refuse to spill results into multiple cells, even when you give them a range of data? For example, if you give some functions like EOMONTH or EDATE a range of dates, you'll get back a #VALUE! error. This quirky behavior affects dozens of Excel functions, mostly legacy functions from the old Analysis ToolPak, that were developed decades before dynamic array formulas were introduced. The good news? There's an incredibly simple fix that most Excel users don't know about: just add a plus sign (+) before your range reference. That's it!  Read below for a full explanation, examples of how to fix the problem, and a list of functions that are affected.

[Formula challenge - list names by teams](https://exceljet.net/challenges/formula-challenge-list-names-by-teams)

-----------------------------------------------------------------------------------------------------------------

In the worksheet shown, the goal is to list the names associated with each team, based on the data in columns B and C. The result should be a list of team members separated by commas. The solution should be dynamic. If the data changes, the result should update accordingly. This challenge assumes you are using Excel 2021 or later. 

[Formulas](https://exceljet.net/articles?tag=26)

[Floating Point Errors in Excel](https://exceljet.net/articles/floating-point-errors-in-excel)

-----------------------------------------------------------------------------------------------

Have you ever had Excel tell you two numbers are different when they look the same? This can be quite unsettling. You keep checking and re-checking numbers that look identical, and yet Excel insists they are different. Is Excel broken? Do you need glasses? Don't worry, it's not your fault. You may have run into a floating-point error. There are reasons why this can happen, and simple ways to fix the problem. 

[Formulas](https://exceljet.net/articles?tag=26)

[Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)

-------------------------------------------------------------------------------------------

After decades of waiting, Excel finally supports Regular Expressions, aka regex! Learn how three powerful new functions - REGEXTEST, REGEXREPLACE, and REGEXEXTRACT - can transform complex text operations into elegant, maintainable formulas. Whether you're cleaning data, validating inputs, or extracting patterns, these new tools will change how you write advanced formulas in Excel.

[Formulas](https://exceljet.net/articles?tag=26)

[Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)

-----------------------------------------------------------------------------------

Excel has supported the complex number system for years. Engineers use it to solve problems related to electronics, fluid dynamics, and signal processing. The way Excel's formula engine implements complex numbers is an example of functional programming, a paradigm that Microsoft has invested heavily in recently with the latest updates and functions.

[Formulas](https://exceljet.net/articles?tag=26)

[New Excel Functions](https://exceljet.net/new-excel-functions)

----------------------------------------------------------------

Nearly 50 new functions have been added to Excel! This is not your Dad's Excel anymore – a lot has changed. This article takes a quick tour of the new functions, with links to more detailed information.

[Formulas](https://exceljet.net/articles?tag=26)

[XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)

---------------------------------------------------------------------------------------

For many years, INDEX and MATCH have been the go-to solution for difficult lookup problems in Excel. While more complicated to configure, the two-function combination of INDEX + MATCH is flexible and powerful. But now that XLOOKUP is more widely available, will INDEX and MATCH remain popular? Is there any reason to still use INDEX and MATCH? Read below for a detailed comparison. See INDEX and MATCH Two-Column Lookup Example

[Formulas](https://exceljet.net/articles?tag=26)

[XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)

-----------------------------------------------------------------------

For many years, VLOOKUP has reigned supreme as the most widely used lookup function in Excel. But now that XLOOKUP is more widely available, VLOOKUP's reign will likely come to an end. XLOOKUP is a modern replacement for the VLOOKUP function and is more capable in almost every way. Let's look at how these two functions stack up against each other.

[Formulas](https://exceljet.net/articles?tag=26)

[Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

----------------------------------------------------------------

In this article, I attempt to explain why you see SUMPRODUCT so often in formulas, and when you can use the SUM function instead. The short version: SUMPRODUCT supports array operations natively, which makes it very useful for solving seemingly unrelated Excel problems. In the current version of Excel, you can use the SUM function instead, but SUMPRODUCT is better for backwards compatibility.

[Formulas](https://exceljet.net/articles?tag=26)

[How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)

-----------------------------------------------------------------------------------------

This article explains how to concatenate manually with the ampersand operator (&) and with the three Excel functions designed for concatenation: CONCATENATE, CONCAT, and TEXTJOIN.

[Formulas](https://exceljet.net/articles?tag=26)

[What is an array formula?](https://exceljet.net/articles/what-is-an-array-formula)

------------------------------------------------------------------------------------

In the world of Excel formulas, the term "array formula" is probably responsible for more confusion than just about any other concept. This is because the definition of an array formula has become mixed up with the requirement to enter some array formulas in a special way, with control + shift + enter.

[Formulas](https://exceljet.net/articles?tag=26)

[Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)

--------------------------------------------------------------------------------

There are eight widely used functions in Excel that use a syntax different from other functions in Excel. This syntax can make these functions more challenging to use, because it is not intuitive.  Read on for important information about COUNTIF, COUNTIFS, SUMIF, SUMIFS,  AVERAGEIF, AVERAGEIFS, MINIFS, and MAXIFS.

[Power Query](https://exceljet.net/articles?tag=111)

[Download Coronavirus data to Excel](https://exceljet.net/articles/download-coronavirus-data-to-excel)

-------------------------------------------------------------------------------------------------------

This article provides examples of public Coronavirus data you can download to Excel with Power Query. Each example has a link, a screenshot to show what the data looks like in Excel after being imported, and an Excel workbook.

[Power Query](https://exceljet.net/articles?tag=111)

[Tracking COVID-19 with Excel](https://exceljet.net/articles/tracking-covid-19-with-excel)

-------------------------------------------------------------------------------------------

A quick example of how to track testing for COVID-19 using Excel and publicly available data. In this project, the data is fetched and "shaped" with Power Query, then dropped back into Excel, where it can be refreshed with a single click.

[Formulas](https://exceljet.net/articles?tag=26)

[Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)

-----------------------------------------------------------------------------------------------------------------

Dynamic Excel offers 6 brand new functions that solve hard problems in Excel like sorting, filtering, and working with unique values. For those not using Office 365, this page provides some alternative formulas that work in older versions of Excel.

[Formulas](https://exceljet.net/articles?tag=26)

[Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)

-------------------------------------------------------------------------------------------------

Dynamic Arrays are the biggest change to Excel formulas in years. Maybe the biggest change ever. This is because Dynamic Arrays let you easily work with multiple values at the same time in a formula. This article provides an overview with many links and examples.

Pages
-----

*   1
*   [2](https://exceljet.net/articles?page=1 "Go to page 2")
    
*   [3](https://exceljet.net/articles?page=2 "Go to page 3")
    
*   [4](https://exceljet.net/articles?page=3 "Go to page 4")
    
*   [next ›](https://exceljet.net/articles?page=1 "Go to next page")
    
*   [last »](https://exceljet.net/articles?page=3 "Go to last page")
    

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