# Excel COUNTA function | Exceljet

**Source:** https://exceljet.net/functions/counta-function

---

[Skip to main content](https://exceljet.net/functions/counta-function#main-content)

[](https://exceljet.net/functions/counta-function#)

*   [Previous](https://exceljet.net/functions/count-function)
    
*   [Next](https://exceljet.net/functions/countblank-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

COUNTA Function
===============

by Dave Bruns · Updated 25 Oct 2022

Related functions 
------------------

[COUNT](https://exceljet.net/functions/count-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[COUNTBLANK](https://exceljet.net/functions/countblank-function)

![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")

Summary
-------

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Purpose 
--------

Count the number of non-blank cells

Return value 
-------------

A number representing non-blank cells.

Syntax
------

    =COUNTA(value1,[value2],...)

*   _value1_ - An item, cell reference, or range.
*   _value2_ - \[optional\] An item, cell reference, or range.

Using the COUNTA function 
--------------------------

The COUNTA function counts cells that contain values, including numbers, text, logicals, errors, and empty text (""). COUNTA does not count empty cells.

The COUNTA function returns the count of values in the list of supplied [arguments](https://exceljet.net/glossary/function-argument)
. COUNTA takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _value1_, _value2_, _value3_, etc. Arguments can be individual hardcoded values, cell references, or ranges up to a total of 255 arguments. All values are counted, including text, numbers, percentages, errors, dates, times, fractions, and formulas that return [empty strings](https://exceljet.net/glossary/empty-string)
 (""). Empty cells are ignored.

### Examples

In the example shown, COUNTA is set up to values in the range B5:B15:

    =COUNTA(B5:B15) // returns 9
    

COUNTA returns 9, since there are 9 non-empty cells in the range B5:B15. 

The COUNTA function counts numbers and text:

    =COUNTA(1,2,3) // returns 3
    =COUNTA(1,"a","b") // returns 3
    =COUNTA(1,2,3,"a",5%) // returns 5
    

To count non-empty cells in the range A1:A10:

    =COUNTA(A1:A10) // count non-empty cells in A1:A10
    

To count non-empty cells in the range A1:A10 and the range C1:H2:

    =COUNTA(A1:A10,C1:H2) // two ranges
    

### Empty strings

Note that COUNTA includes [empty strings](https://exceljet.net/glossary/empty-string)
 ("") in the count, which can be returned by formulas. For example, the formula below will return "OK" when the value in A1 is at least 10, and an empty string ("") when the value is less than 10:

    =IF(A1>=10,"OK","")
    

The COUNTA function will count both results as non-empty. To ignore empty strings, [this example provides a workaround](https://exceljet.net/formulas/count-cells-that-are-not-blank)
.

### Invisible characters

Be aware that COUNTA will also count cells that look empty, but actually contain invisible characters or an empty string ("") returned by a formula. You can check which cells are blank using Go To > Special > Blanks:

1.  Select a range
2.  Open Go To dialog (Control + G)
3.  Press "Special"
4.  Select "Blanks"

### Functions for counting

*   To count numbers only, use the [COUNT function](https://exceljet.net/functions/count-function)
    .
*   To count numbers and text, use the [COUNTA function](https://exceljet.net/functions/counta-function)
    .
*   To count with one condition, use the [COUNTIF function](https://exceljet.net/functions/countif-function)
    
*   To count with multiple conditions, use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
    .
*   To count empty cells, use the [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
    .

### Notes

*   COUNTA will count cells that contain numbers, text, logical values, error values, and empty text ("").
*   To count numeric values only, use the [COUNT function](https://exceljet.net/functions/count-function)
    .

COUNTA function examples
------------------------

[![Excel formula: Dynamic named range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20index1.png "Excel formula: Dynamic named range with INDEX")](https://exceljet.net/formulas/dynamic-named-range-with-index)

### [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)

This page shows an example of a dynamic named range created with the INDEX function together with the COUNTA function. Dynamic named ranges automatically expand and contract when data is added or removed. They are an alternative to using an Excel Table , which also resizes as data is added or...

[![Excel formula: Score quiz answers with key](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/score%20quiz%20answers%20with%20key.png "Excel formula: Score quiz answers with key")](https://exceljet.net/formulas/score-quiz-answers-with-key)

### [Score quiz answers with key](https://exceljet.net/formulas/score-quiz-answers-with-key)

This formula uses the named range key (C4:G4) for convenience only. Without the named range, you'll want to use an absolute reference so the formula can be copied. In cell I7, we have this formula: =SUM(--(C7:G7=key)) working from the inside-out, this expression is evaluated first: C7:G7=key //...

[![Excel formula: Add row numbers and skip blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20row%20numbers%20and%20skip%20blanks.png "Excel formula: Add row numbers and skip blanks")](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

### [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

In the example shown, the goal is to add row numbers in column B only when there is a value in column C. The formula in B5 is: =IF(ISBLANK(C5),"",COUNTA($C$5:C5)) The IF function first checks if cell C5 has a value with the ISBLANK function : ISBLANK(C5) // TRUE if empty, FALSE if not If C5 is...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Multiple cells have same value case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Multiple%20cells%20have%20same%20value%20case%20sensitive.png "Excel formula: Multiple cells have same value case sensitive")](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

### [Multiple cells have same value case sensitive](https://exceljet.net/formulas/multiple-cells-have-same-value-case-sensitive)

This formula uses the EXACT formula to compare a range of cells to a single value: =EXACT(B5:F5,B5) Because we give EXACT a range of values in the first argument, we get back an array result containing TRUE FALSE values: {TRUE,FALSE,TRUE,TRUE,TRUE} This array goes into the AND function, which...

[![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")](https://exceljet.net/formulas/dynamic-named-range-with-offset)

### [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a video demo of this approach here . This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width...

[![Excel formula: Count sold and remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20sold%20and%20remaining.png "Excel formula: Count sold and remaining")](https://exceljet.net/formulas/count-sold-and-remaining)

### [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)

In this example, the goal is to count the number of items sold and remaining, based on the data visible in columns B and C. The ID column holds unique ids, and the Sold column is used to record a sale. An "x" in the Sold column indicates the item has been sold. As is typical in Excel, there are...

[![Excel formula: Count unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20criteria.png "Excel formula: Count unique values with criteria")](https://exceljet.net/formulas/count-unique-values-with-criteria)

### [Count unique values with criteria](https://exceljet.net/formulas/count-unique-values-with-criteria)

In this example, the goal is to count unique values that meet one or more specific conditions. In the example shown, the formula used in cell H7 is: =SUM(--(LEN(UNIQUE(FILTER(B6:B15,C6:C15=H6,"")))>0)) At the core, this formula uses the FILTER function to apply criteria, and the UNIQUE function...

[![Excel formula: Count cells that are not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20not%20blank.png "Excel formula: Count cells that are not blank")](https://exceljet.net/formulas/count-cells-that-are-not-blank)

### [Count cells that are not blank](https://exceljet.net/formulas/count-cells-that-are-not-blank)

In this example, the goal is to count cells in a range that are not blank (i.e. not empty). There are several ways to go about this task, depending on your needs. The article below explains different approaches. COUNTA function While the COUNT function only counts numbers, the COUNTA function...

[![Excel formula: Count cells that are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20blank_0.png "Excel formula: Count cells that are blank")](https://exceljet.net/formulas/count-cells-that-are-blank)

### [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)

In this example, the goal is to count cells in a range that are blank. Counting blank cells in Excel can be tricky because cells can look blank even when they are not actually empty. The article below explains three different approaches. COUNTBLANK function The simplest way to count empty cells in...

[![Excel formula: Basic outline numbering](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20outline%20numbering.png "Excel formula: Basic outline numbering")](https://exceljet.net/formulas/basic-outline-numbering)

### [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)

At the core, this formula builds a level 1 and level 2 number and concatenates the two numbers together with a period (".") as a separator. The result is a value like "1.1". The "level 1" number is generated with COUNTA like this: =COUNTA($B$5:B5) Note the range is an expanding reference , so it...

[![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")](https://exceljet.net/formulas/project-complete-percentage)

### [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is: =COUNTA(C5:C11)/COUNTA(B5:B11) At the core, this formula...

[![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")](https://exceljet.net/formulas/count-cells-in-range)

### [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is...

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

COUNTA function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20text%20values-Play.png)](https://exceljet.net/videos/how-to-generate-random-text-values)

### [How to generate random text values](https://exceljet.net/videos/how-to-generate-random-text-values)

In this video, we'll look at how to create a list of random text values. As we've already seen, the RANDARRAY function can be used to generate random dates and times, which are numeric values. How can we generate random values that aren't numeric? One way is to use this is to use the RANDARRAY...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20unique%20values-Play_0.png)](https://exceljet.net/videos/how-to-count-unique-values)

### [How to count unique values](https://exceljet.net/videos/how-to-count-unique-values)

In this video, we'll look at how to count the unique values returned by the UNIQUE function . Before dynamic array formulas, counting unique values in Excel involved complex array formulas, especially if you needed to count values based on one or more conditions. Now that dynamic array formulas,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)

### [How to create a dynamic named range with INDEX](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)

In this video we'll look at how to create a dynamic named range with the INDEX function . Unlike INDIRECT and OFFSET , INDEX is a non-volatile function. This means that INDEX will not recalculate whenever a change is made to a worksheet. This makes INDEX ideal for professional models and for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20OFFSET-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)

### [How to create a dynamic named range with OFFSET](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)

In this video we're going to look at how to create a dynamic named range using the OFFSET function . To create a dynamic named range that refers to this data using the OFFSET function, first identify the first cell of the data in the upper left. In this case, that's cell B6. To create a named range...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Spilling%20and%20the%20spill%20range-Play.png)](https://exceljet.net/videos/spilling-and-the-spill-range)

### [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)

In this video, we’ll look at a core idea in dynamic array behavior, the spill range . When a dynamic array formula outputs multiple values, it is said to “spill” these values onto the worksheet. For example, if I use the UNIQUE function on this list of colors, UNIQUE spills 3 values - red, blue,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20see%20arrays%20in%20formulas-Play.png)](https://exceljet.net/videos/how-to-see-arrays-in-formulas)

### [How to see arrays in formulas](https://exceljet.net/videos/how-to-see-arrays-in-formulas)

In this video, we'll look at a few ways that you can see or visualize arrays in a formula. One of the best things about the new dynamic array formula engine in Excel is that it's much easier to see and visualize arrays. Let's take a look at a few examples. The first way to see arrays is to enter...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20perform%20a%20random%20sort-Play_0.png)](https://exceljet.net/videos/how-to-perform-a-random-sort)

### [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)

In this video, we’ll look at how to perform a random sort with the SORTBY function , with help from the RANDARRAY function . In this worksheet, we have the first 10 letters in the alphabet in the range B5:B14. How can we sort this data in random order? One way to do this is to add a helper column...

Related functions
-----------------

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")](https://exceljet.net/functions/countblank-function)

### [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)
    
*   [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)
    
*   [Last row in mixed data with no blanks](https://exceljet.net/formulas/last-row-in-mixed-data-with-no-blanks)
    
*   [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)
    
*   [Running count group by n size](https://exceljet.net/formulas/running-count-group-by-n-size)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Score quiz answers with key](https://exceljet.net/formulas/score-quiz-answers-with-key)
    
*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)
    

### Videos

*   [How to create a dynamic named range with OFFSET](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)
    
*   [How to create a dynamic named range with INDEX](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)
    
*   [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)
    
*   [How to count unique values](https://exceljet.net/videos/how-to-count-unique-values)
    
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
    
*   [How to see arrays in formulas](https://exceljet.net/videos/how-to-see-arrays-in-formulas)
    
*   [How to generate random text values](https://exceljet.net/videos/how-to-generate-random-text-values)
    

### Functions

*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [COUNTBLANK Function](https://exceljet.net/functions/countblank-function)
    

### Links

*   [Microsoft COUNTA function documentation](https://support.office.com/en-us/article/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509)
    

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