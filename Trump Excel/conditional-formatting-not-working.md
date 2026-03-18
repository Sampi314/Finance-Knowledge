# Conditional Formatting Not Working in Excel - Easy Fix!

**Source:** https://trumpexcel.com/conditional-formatting-not-working

---

[Skip to content](https://trumpexcel.com/conditional-formatting-not-working/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/conditional-formatting-not-working/#below-title)

Conditional Formatting allows you to add a visual layer to your dataset and make it easier to understand.

You can use it to quickly highlight cells that satisfy the specified conditions (such as highlighting cells with the top 3 values or highlighting all cells that contain the word ‘Excel’, etc.)

But sometimes Conditional Formatting may not work as expected. In most cases, a handful of reasons are the culprit, and you can easily get it sorted.

In this article, I will cover the most common reasons why Conditional Formatting may not work in your Excel and how to fix these issues.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/conditional-formatting-not-working/#)

Using Incorrect Range in Conditional Formatting
-----------------------------------------------

Let’s start with the most basic but a big one.

**Conditional formatting is applied on an incorrect range.**

When you [start with conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
, you need to select a range of cells that would be analyzed, and then formatting would be applied if the cell satisfies the criteria.

If you have used the wrong range, conditional formatting rules are being checked for the wrong set of cells, and hence it doesn’t work as expected.

**How to Fix?**

This one is very easy to fix.

Select the cells/ranges where your conditional formatting is glitching, then click the ‘Home’ tab, then click on the Conditional Formatting icon, and then click on ‘Manage Rules’.

![Click on Manage Rules in Excel conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20492'%3E%3C/svg%3E)

This will open the ‘Conditional Formatting Rules Manager’ dialog box, which will list all the rules that have been applied to that range.

![Change the range in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20248'%3E%3C/svg%3E)

Check if the rules are applied to the correct range or not. If not, correct the range in the ‘Applies’ To field.

Also read: [How to Remove Conditional Formatting in Excel](https://trumpexcel.com/remove-conditional-formatting-excel/)

Formula in Conditional Formatting Does Not Return TRUE or FALSE
---------------------------------------------------------------

Apart from the already built-in Conditional Formatting rules, you can also create your own formulas to determine which cells to format.

When you use a formula in Conditional Formatting, it needs to return a TRUE or a FALSE.

When the formula returns TRUE for a cell, that cell gets the specified format applied to it, and when it returns FALSE, the formatting is not applied.

A common issue when Conditional Formatting is not working is when the formula does not return a TRUE or FALSE value.

![Conditional formatting formula should return true or false](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

So, if you’re using a formula, double-check to ensure it works as expected.

**Pro Tip**: You can first create the formula in a cell in a worksheet, and when you’re satisfied that it works as expected, you can copy it to the Conditional Formatting dialog box.

Also read: [Highlight Blank Cells in Excel](https://trumpexcel.com/highlight-blank-cells-in-excel/)

Used Incorrect Cell Reference (Absolute/Relative)
-------------------------------------------------

When you use formulas in Conditional Formatting, you need to use the right [type of cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 (absolute, relative, or mixed).

If you’re not using the right reference, the formula doesn’t work as expected, and that impacts the conditions formatting as well.

Below, I have an example where I have created a formula to highlight all the rows in range A2:C100, where the values in cells in column B are more than the value in cell D1.

![check the references in conditional formatting formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

For this to work, I need to lock D1 and make it $D$1, so that when cells in column B are being analyzed, each cell is compared to D1.

If I don’t use an absolute reference here (which is $D$1), my conditional formatting won’t work as expected.

Similarly, I need to use a mixed reference $B2. This way, for each cell in a row, only the value in cell B2 is considered, as I’ve locked the column.

For example, when it comes to the 10th row, it would only look at the value in cell B10, and if its value is more than that in cell D1, the entire row would get highlighted.

Also read: [Copy Conditional Formatting to Another Cell in Excel](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)

Overlapping Rules Are Not in the Right Order (Conflict in Rules)
----------------------------------------------------------------

When you apply multiple Conditional Formatting rules on a range of cells, you need to ensure they are in the right order.

In the list of rules hierarchy, the first rule is applied and gets preference over the second one, and the second rule gets preference over the third one, and so on.

So, if you have multiple rules applied to the same range of cells, you can check the rules to ensure that they are in the right order.

To get the list of all the rules, follow the below steps:

1.  Select the range of cells on which we have applied the conditional formatting rules.
2.  Click the Home tab.
3.  Click on the ‘Conditional Formatting’ option in the ribbon.
4.  From the drop-down, click on the ‘Manage Rules’ option. This will open the _Conditional Formatting Rules Manager_ dialog box.

![Click on Manage Rules in Excel conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20492'%3E%3C/svg%3E)

5.  Check and confirm that all the rules have the correct order.

![Check the order of conditional formatting rules if not working](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20248'%3E%3C/svg%3E)

Pro Tip: You can use the arrow icons in the dialog box to move a rule above or below the other rules

Numbers are Formatted as Text
-----------------------------

If you’re applying condition formatting to a range that contains numbers, one reason why conditional formatting may not be working is because the numbers are formatted as text.

For example, below, I have a data set where I’ve student names in column A and their scores in column B, and I have applied conditional formatting to highlight all those scores that are less than 40.

![Conditional formatting not working in the selected range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20388'%3E%3C/svg%3E)

You don’t see the cells highlighted in any specific format because the conditional formatting did not work.

This is because there is an apostrophe before the number, which [converts these numbers to text](https://trumpexcel.com/convert-numbers-to-text-excel/)
.

![Numbers are formatted as text with apostrophe in the beginning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20436'%3E%3C/svg%3E)

So now, when I try to apply conditional formatting, since it cannot find any number in column B, it is unable to highlight cells with values less than 40.

To fix this, you need to [convert these text values back into numbers](https://trumpexcel.com/convert-text-to-numbers-excel/)
 so that they can be used with conditional formatting.

Using Functions Not Available in Your Excel
-------------------------------------------

Since there are many different versions of Excel, with Microsoft 365 being the latest one, there are many functions that are available in the new versions but not in the older versions.

Some examples of these functions would be [XLOOKUP](https://trumpexcel.com/xlookup-function/)
, [FILTER](https://trumpexcel.com/filter-function/)
, SORTBY, IFS, etc.

If you’re using any of these newer functions in a formula in Conditional Formatting and it is opened in an older version of Excel, Conditional Formatting will not work.

A good way to quickly check for this is to try and use the function in a cell in Excel and see if you can get a TRUE or a FALSE result from that formula.

Also read: [Excel Conditional Formatting Based on Another Cell](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/)

Conflicts with Add-in
---------------------

If you have checked for all the above possible reasons and your condition formatting is still not working then one reason could be a conflicting add-in your Excel.

If you’re using any 3rd party add-ins, try to [disable these add-ins](https://spreadsheetplanet.com/remove-add-ins-excel/)
 and see if Conditional Formatting works. If the issue was because of a conflict with the add-in, this would solve it.

In this article, I covered some possible reasons why your condition formatting may not be working and how to fix it. Note that everything that I have covered in this article is also true for Google Sheets.

I hope you found this Excel article helpful. Please let me know your thoughts in the comments section below.

**Other Excel articles you may also like:**

*   [Excel Formulas Not Working (Not Calculating)](https://trumpexcel.com/excel-formulas-not-working/)
    
*   [Arrow Keys Not Working in Excel (Not Moving Cells)](https://trumpexcel.com/arrow-keys-not-working-excel/)
    
*   [Apply Conditional Formatting Based on Another Column](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    
*   [Copy Conditional Formatting to Another Cell](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)
    
*   [Highlight Rows Based on a Cell Value in Excel](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [Create 100% Stacked Bar Chart in Excel](https://trumpexcel.com/stacked-bar-chart-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/conditional-formatting-not-working/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK