# Native checkboxes in Excel | Exceljet

**Source:** https://exceljet.net/articles/native-checkboxes-in-excel

---

[Skip to main content](https://exceljet.net/articles/native-checkboxes-in-excel#main-content)

[](https://exceljet.net/articles/native-checkboxes-in-excel#)

*   [Previous](https://exceljet.net/articles/modeling-the-4-percent-retirement-rule-in-excel)
    
*   [Next](https://exceljet.net/articles/why-some-excel-functions-wont-spill)
    

Native checkboxes in Excel
==========================

by Dave Bruns · Updated 20 Jul 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/9294/download?token=FLHDdnjV)
 (31.98 KB)

![Native Checkboxes in Excel artwork](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/native-checkboxes-in-excel-artwork.jpg "Native Checkboxes in Excel artwork")

Summary
-------

If you've ever tried to create a to-do list, survey, or any kind of checklist in Excel, you've probably wished for a simple checkbox feature. Well, your wish has finally come true. Microsoft has finally introduced a native checkbox feature in Excel. It's easy to use and a great way to make your spreadsheets more interactive.

One of the big changes to Excel in the last year was the introduction of a native checkbox in Excel. Checkboxes might seem like a small thing, but they're very useful for organizing information, tracking progress, and creating interactive spreadsheets. There's something uniquely satisfying about ticking a box to finish off a task!

Unlike the clunky solutions of the past, this new checkbox sits happily in a cell and is very easy to set up. Because the checkbox lives in the grid, it will move around naturally as columns and rows are adjusted. Because it returns TRUE or FALSE, you can use the output directly in formulas or to apply conditional formatting. The possibilities are endless.

This article introduces the new native checkbox feature in Excel and walks through a number of practical examples. The examples are in the attached workbook, so download the workbook, follow along, and try the checkboxes out yourself.

> For now, native checkboxes are only available in Excel 365. This guide only covers the new native checkbox feature. In older versions of Excel, the process for adding a checkbox is different and more complicated.

### Table of contents

*   [The old days: before native checkboxes](https://exceljet.net/articles/native-checkboxes-in-excel#the-old-days-before-native-checkboxes)
    
*   [Key features of native checkboxes in Excel](https://exceljet.net/articles/native-checkboxes-in-excel#key-features-of-native-checkboxes-in-excel)
    
*   [How to add a checkbox](https://exceljet.net/articles/native-checkboxes-in-excel#how-to-add-a-checkbox)
    
*   [How to remove a checkbox](https://exceljet.net/articles/native-checkboxes-in-excel#how-to-remove-a-checkbox)
    
*   [Checking and unchecking a checkbox](https://exceljet.net/articles/native-checkboxes-in-excel#checking-and-unchecking-a-checkbox)
    
*   [Example 1: Simple Checklist](https://exceljet.net/articles/native-checkboxes-in-excel#example-1-simple-checklist)
    
*   [Example 2: Highlight rows with a checkbox](https://exceljet.net/articles/native-checkboxes-in-excel#example-2-highlight-rows-with-a-checkbox)
    
*   [Example 3: Count and sum checkboxes](https://exceljet.net/articles/native-checkboxes-in-excel#example-3-count-and-sum-checkboxes)
    
*   [Example 4: Change formula output with a checkbox](https://exceljet.net/articles/native-checkboxes-in-excel#example-4-change-formula-output-with-a-checkbox)
    
*   [Example 5: Filter a list with a checkbox](https://exceljet.net/articles/native-checkboxes-in-excel#example-5-filter-a-list-with-a-checkbox)
    
*   [Other important information](https://exceljet.net/articles/native-checkboxes-in-excel#other-important-information)
    

### The old days: Before native checkboxes

Until Microsoft added the native, in-cell checkbox in 2024, every "checkbox" in Excel was actually a small shape that floated above the grid. To create a checkbox, you first had to show the Developer tab (hidden by default), choose either a Form-control checkbox or an ActiveX checkbox, drop it onto the sheet, and then link it to a cell so formulas could pick up its TRUE/FALSE value. The boxes didn't automatically resize or move if you changed row heights or column widths, and they were easy to misalign or delete.

As a result, most people didn't use checkboxes but instead worked around the problem, using "x" to mark items, showing green ticks with conditional formatting, or creating dropdown lists with "Yes" and "No" options. These solutions work, but they aren't elegant or intuitive.

The new checkbox lives inside the cell itself, fills down like ordinary data, survives sorting and filtering, and works the same on Windows, Mac, and Excel online. In short, it works like you would expect it to. It's a real upgrade in usability and a great addition to Excel.

### Key features of native checkboxes in Excel

The new native checkbox feature is a useful new addition to your day-to-day work in Excel. It's easy to use, with a number of useful features:

*   A simple way to mark a task as completed.
*   One-step process: Ribbon > Insert > Checkbox.
*   User-friendly. No need for form controls or developer tools.
*   Native in the Excel grid (no floating objects).
*   Compatible with Excel formulas and conditional formatting.
*   A nice way to make spreadsheets more interactive and intuitive.
*   Cross-platform compatibility. Works on Windows, Mac, and Excel online.

### How to add a checkbox

Adding a native checkbox in Excel is easy. First, select the cell(s) you want to add the checkbox to:

![Adding a checkbox step 1: select the cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/adding-a-checkbox-1.png "Adding a checkbox step 1: select the cells")

Next, click the Checkbox button on the Insert tab of the ribbon:

![Adding a checkbox step 2: click the Checkbox button](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/adding-a-checkbox-2.png "Adding a checkbox step 2: click the Checkbox button")

That's it! You've added an interactive checkbox to your cell. You can now click the checkbox to toggle between checked and unchecked as you like:

![Adding a checkbox step 3: use your checkboxes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/adding-a-checkbox-3.png "Adding a checkbox step 3: use your checkboxes")

Notice the checkbox will show TRUE (checked) or FALSE (unchecked) in the formula bar as you interact with it.

### How to remove a checkbox

The process to remove a checkbox is also very easy. First, select the cells you want to remove the checkbox from:

![Removing a checkbox step 1: select the cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/removing-a-checkbox-1.png "Removing a checkbox step 1: select the cells")

Next, click the Delete key on your keyboard. If a checkbox was checked, it will now be unchecked:

![Removing a checkbox step 2: Press Delete](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/removing-a-checkbox-2.png "Removing a checkbox step 2: Press Delete")

Click the Delete key a second time to completely remove the checkbox:

![Removing a checkbox step 3: Press Delete again if needed](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/removing-a-checkbox-3.png "Removing a checkbox step 3: Press Delete again if needed")

### Checking and unchecking a checkbox

An Excel checkbox is a control that toggles between checked and unchecked. Click once to check it, and click again to uncheck it. If you have more than one checkbox selected, only the first checkbox will be affected.

Another way to check and uncheck checkboxes is to use the Spacebar. Press the Spacebar once to check the checkbox, and press it again to uncheck it. A big advantage of the spacebar is that you can use it to check and uncheck all checkboxes in a selection.

First, select the range of checkboxes you want to check or uncheck, then press the Spacebar to check all the checkboxes at once:

![Using the Spacebar to check multiple checkboxes at once](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/spacebar-check-multiple-checkboxes.png "Using the Spacebar to check multiple checkboxes at once")

If you press the Spacebar again, all the checkboxes will be unchecked:

![Using the Spacebar to uncheck multiple checkboxes at once](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/spacebar-uncheck-multiple-checkboxes.png "Using the Spacebar to uncheck multiple checkboxes at once")

> The Spacebar behavior changes if any checkboxes are already checked. If checkboxes in the selection are checked, pressing the Spacebar will uncheck them. Press the Spacebar again to check all checkboxes in the selection.

### Example 1: Simple Checklist

A classic use of checkboxes is to create a checklist, useful for tracking the completion of tasks or steps. To create a checklist like this, follow the steps explained above:

1.  Select the cell(s) you want to add the checkbox to.
2.  Click the checkbox button on the Insert tab of the ribbon.
3.  Click the checkbox to toggle between checked and unchecked.

![Creating a simple checklist step 1: Add the checkboxes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/simple-checklist-example.png "Creating a simple checklist step 1: Add the checkboxes")

To add a strikethrough effect to the text when the checkbox is checked, use Conditional Formatting. Here are the steps:

1.  Select the cells you want to format, C5:C14 in this example.
2.  Navigate to Home > Conditional Formatting > New Rule.
3.  Select "Use a formula to determine which cells to format" option.
4.  Enter the formula `=$B5` in the formula bar.
5.  Click the Format button and check the "Strikethrough" option.
6.  Click OK to save and apply the strikethrough effect.

The screenshot below shows how the rule is configured after adding the formula and setting the strikethrough formatting:

![Creating a simple checklist step 2: Create a conditional formatting rule for the strikethrough effect.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/simple-checklist-example-strikethrough-rule.png "Creating a simple checklist step 2: Create a conditional formatting rule for the strikethrough effect.")

> Note: Because checkboxes return TRUE and FALSE, the formula in the conditional formatting rule is simply `=$B5`. If you prefer, you can use `=$B5=TRUE` instead. Also, it's not strictly necessary to lock the column reference, but it's useful when you want to copy the rule to other columns.

> If you are new to the concept of applying a conditional formatting rule with a formula, watch this short video: [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
> .

### Example 2: Highlight rows with a checkbox

Another useful way to use checkboxes is to highlight rows of interest, as seen in the worksheet below:

![Example of highlighting rows with a checklist](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/highlighting-rows-with-a-checkbox.png "Example of highlighting rows with a checklist")

Like the previous example, the formatting is applied using Conditional Formatting. Here are the steps:

1.  Select the cells you want to format, B5:G15 in this example.
2.  Navigate to Home > Conditional Formatting > New Rule.
3.  Select "Use a formula to determine which cells to format" option.
4.  Enter the formula `=$B5` in the formula bar.
5.  Click the Format button and set a Fill color
6.  Click OK to save and apply the highlight effect.

The screenshot below shows how the rule is configured after adding the formula and setting the fill color:

![Highlighting rows with a checklist: conditional formatting rule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/highlighting-rows-with-a-checkbox-rule.png "Highlighting rows with a checklist: conditional formatting rule")

> Note: This is a case where we need the mixed reference `=$B5` to lock the column and so that it does not change as it is evaluated across all six columns

### Example 3: Count and sum checkboxes

Once you are using checkboxes in a worksheet, you may want to count or sum the number of checkboxes that are checked, or sum the values associated with checked or unchecked checkboxes. You can easily do this with the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 and [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 as shown in the worksheet below:

![Counting and summing with checkboxes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/counting-and-summing-checkboxes.png "Counting and summing with checkboxes")

The formulas in column G are set up to count the number of checkboxes that are checked or unchecked D5:D14 using COUNTIFS. The formulas in column H are set up to sum the values in C5:C14 for the checkboxes that are checked or unchecked in D5:D14 using SUMIFS.

    G5: =COUNTIFS(D5:D14,TRUE)
    G6: =COUNTIFS(D5:D14,FALSE)
    H5: =SUMIFS(C5:C14,D5:D14,TRUE)
    H6: =SUMIFS(C5:C14,D5:D14,FALSE)
    

Note that for criteria, we simply use TRUE or FALSE, which is the result of the checkbox.

### Example 4: Change formula output with a checkbox

Because checkboxes return TRUE or FALSE, you can use them to change the output of a formula. For example, you can use the result from a checkbox with the [IF function](https://exceljet.net/functions/if-function)
 to apply a discount or penalty to a value based on whether the checkbox is checked or unchecked. You can see an example of this in the worksheet below, where a checkbox in column D is used to [apply a 20% discount](https://exceljet.net/formulas/decrease-by-percentage)
 to the Price in column C:

![Changing formula output with a checklist (applying a discount)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/changing-formula-output-with-a-checkbox.png "Changing formula output with a checklist (applying a discount)")

The formula in column E looks like this:

    =IF(D5,C5*(1-20%),C5)
    

Inside the [IF function](https://exceljet.net/functions/if-function)
, the logical test is `D5`, which is the result of the checkbox. If the checkbox is checked, the formula returns `C5*(1-20%)`, which is the price minus 20%. If the checkbox is unchecked, the formula returns `C5`, which is the original price.

> Note: Applying a discount is just one example of how you can use checkboxes to change the output of a formula. Because checkboxes return TRUE or FALSE, you can use them to change the output of almost any formula.

### Example 5: Filter a list with a checkbox

Another useful way to use checkboxes is to filter a list based on the checkbox status. You can see an example of this in the worksheet below, where a checkbox in column B (RSVP) is used to filter names in column C with the [FILTER function](https://exceljet.net/functions/filter-function)
:

![Filtering a list with a checkbox](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/filtering-a-list-with-a-checkbox.png "Filtering a list with a checkbox")

The idea is to create a list of names that have RSVP'd "Yes" to an event. The formula in cell E5 looks like this:

    =FILTER(C5:C14,B5:B14)
    

Inside the [FILTER function](https://exceljet.net/functions/filter-function)
, the array is given as `C5:C14`, which is the range of names to filter. The include argument is `B5:B14`, which is the range of checkboxes to filter by. Because checkboxes return TRUE or FALSE, the result from FILTER is a list of names in column C where RSVP is TRUE (checked).

### Other important information

Here are a few other things you should know about using new native checkboxes in Excel:

*   Checkboxes are a little like [number formatting](https://exceljet.net/articles/custom-number-formats)
     in that you can copy and paste checkbox formatting using [Paste Special](https://exceljet.net/shortcuts/display-the-paste-special-dialog-box)
     > Formats on top of TRUE and FALSE values, and the checkboxes will display correctly. However, if you select a checkbox and examine the Checkbox button on the Insert tab of the ribbon, there is no indication that checkbox formatting has been "applied".
*   One difference between checkboxes and number formatting is that inserting checkboxes adds actual values to cells in the worksheet. By default, all checkboxes are unchecked, and the value is FALSE. As you tick off checkboxes, the values change to TRUE. If you remove the checkboxes from cells, the TRUE and FALSE values are also removed.
*   If you want to turn off the display of checkboxes but keep the TRUE and FALSE values intact, first select the checkboxes, then navigate to Home > Clear > Clear Formats. You can also put a zero in another cell, copy the zero, then select the checkboxes and use Paste Special > Add to convert the checkboxes to TRUE and FALSE values.
*   If you have existing formulas that return TRUE and FALSE, and you insert checkboxes on top of these formulas, the checkboxes will appear correctly. However, checkboxes applied to formulas are read-only; you can't change the state by clicking. The formula underneath the checkbox is the only mechanism that will check and uncheck the box. 

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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