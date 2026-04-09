# Excel Showing Formula Instead of Result - Quick Fix!

**Source:** https://trumpexcel.com/excel-showing-formula-instead-of-result

---

[Skip to content](https://trumpexcel.com/excel-showing-formula-instead-of-result/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-showing-formula-instead-of-result/#below-title)

Sometimes, it happens that instead of showing the result of a formula in Excel, you see the formula itself.

Below, I have an example where I have a formula in column C, and instead of showing the result of the formula, Excel shows the formula itself.

![Data set where It shows formula instead of the result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20283'%3E%3C/svg%3E)

This is a pretty common occurrence with Excel users, and you can easily fix it.

In this article, I will cover possible reasons why Excel is showing the formula instead of the result and how to fix it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-showing-formula-instead-of-result/#)

Reason 1: Show Formulas Option is Enabled
-----------------------------------------

Excel has an inbuilt ‘Show Formulas’ option that displays all the formulas in the cells instead of showing you the result of those formulas,

The most common reason that your Excel file is showing formulas instead of values is that this option may be enabled.

**How to fix this?**

Here are the steps to disable the show formulas option in Excel:

1.  Click the _Formulas_ tab in the ribbon
2.  Click on the _Show Formulas_ option in the Formula Auditing group.

![Click the show formulas button in the formulas tab in the ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20689%20132'%3E%3C/svg%3E)

If this issue were because the _Show Formulas_ option was enabled, the above steps would disable it, and you would now see the results of the formulas instead of the formulas themselves.

_Note: When the show formulas option is enabled, you will see that option in the ribbon in a slightly darker shade of gray (indicating that it is currently active). It works as a toggle where when you click on it, it gets enabled, and when you click on it again, it gets disabled._

**Pro Tip**: You can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 **Control + ~** to enable or disable the show formulas option. To use this, hold the central key and then press the ~ key.

When the _Show Formula_ option is enabled, it is applied to the entire worksheet. So, all the formulas in the worksheet would be shown as formulas instead of the results when it is enabled.

If this doesn’t solve your problem, let’s try the other methods.

Also read: [Show Formulas in Excel Instead of the Values](https://trumpexcel.com/show-formulas-in-excel/)

Reason 2: Cells with Formulas are Formatted as Text
---------------------------------------------------

The cells in a worksheet in Excel can be formatted in different ways to show the value in the cell differently.

For example, you can format the cells to show the numbers, dates, text values, currency, accounting numbers, etc.

When the cells are formatted as text, and then you enter a formula in that cell, Excel shows you the formula itself instead of showing you the result of the formula.

This is because the back end of that cell expects to receive a text value and not a formula.

Below is an example where I have some formulas in column D, and you can see that it shows the formula in the cell as the format of the cell is set to _Text_.

![Cell formatting is set to text - Excel showing formula instead of result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20373'%3E%3C/svg%3E)

**How to fix this?**

I’m sure you’ve already guessed it – you need to change the cell format so that it can start showing the formula results.

Here are the steps to do this:

1.  Select the cells for which you want to change the cell format.
2.  Click the Home tab in the ribbon.

![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20223'%3E%3C/svg%3E)

3.  In the Number group, click on the Formatting drop-down.

![Click on the formatting drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20563%20223'%3E%3C/svg%3E)

4.  Select the _General_ Option

![Select the general formatting option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20535'%3E%3C/svg%3E)

The above steps would change the format of the selected cells to General, which means that now if you enter a formula in these cells, it will show you the result of the formula.

_But what about those cells that already had formulas before we made the change of cell formatting to General?_

In those cells, you would continue to see the formula instead of the formula result.

To correct this, you need to select the cell that is showing the formula, press the F2 key (to get into the edit mode), and then press the Enter key. Doing this forces the cell to recalculate the formula and show you the result.

Alternatively, you can select all the cells that have the formula that is showing as text, then press the F2 key to get into the edit mode, and then hold the Control key and press the Enter key to convert all the formulas into their result in one go.

Also read: [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)

Reason 3: Formula Equal-To Sign is Missing
------------------------------------------

Another common issue could be a missing equal-to sign (=) at the beginning of the formula.

Every formula in Excel needs to start with an equal-to sign. This sign tells Excel to interpret anything following it as a formula.

And if a formula does not start with an equal-to sign, Excel would treat it as regular text.

![Formula being shown as text as the equal to sign is missing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20283'%3E%3C/svg%3E)

This is why, if the equal-to sign is missing, Excel will simply display the formula as is without performing any calculations.

**How to fix this?**

The fix is simple – add the equal-to sign before the formula:

*   Select the cell where the formula is being displayed as text.
*   Click into the [formula bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
     or double-click directly on the cell to edit it.
*   Add an equal-to sign (=) at the beginning of the formula. Ensure there are no spaces or other characters before the = sign.
*   After adding the equal-to sign, press Enter. Excel should recognize the formula and display the calculated result instead of the formula text.

Also read: [How to Hide Formulas in Excel (and Only Display the Value)](https://trumpexcel.com/hide-formulas-excel/)

Reason 4: Apostrophe or Space Character Before the Formula
----------------------------------------------------------

In Excel, when you add an apostrophe (‘) or a leading space at the beginning of a cell’s content, it tells Excel to treat the cell content as text.

This is useful when you want to display numbers or formulas as literals (for example, to show a phone number without formatting or a formula for instructional purposes).

However, if you unintentionally put an apostrophe or a space character before a formula, Excel will not recognize it as a formula and instead treat it as a text string.

Instead, it will display the formula text as-is.

Below is an example where I have a proper formula in cell A1, a formula with a leading apostrophe in cell A2, and a formula with a leading space character in cell A3.

![Formula being shown as there is an apostrophe before the formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20326'%3E%3C/svg%3E)

Note that while there is an apostrophe in cell D2, you don’t see that in the cell itself. However, when you look at the formula bar, you will notice the apostrophe before the equal to sign.

**How to fix this?**

Here are the steps to fix this:

*   Select the cell where the formula is being displayed as text.
*   Click into the formula bar or double-click directly on the [cell to edit](https://trumpexcel.com/edit-cells-excel/)
     it.
*   Delete any apostrophe (‘) or space that is before the equal-to sign (=). Make sure the formula begins exactly with the equal-to sign.
*   Press the Enter key after making the changes. Excel should now show you the formula result instead of showing the formula text.

Also read: [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)

Reason 5: Formula is Wrapped in Quotes (or Double Quotes)
---------------------------------------------------------

Just like having an apostrophe before the formula, when a formula in Excel is wrapped in quotes (or double quotes), it causes the formula to be treated as a text string.

While sometimes this may be done intentionally (when you want to display the formula text for instructional or documentation purposes), it could also happen when you get your Excel files from the web or from databases.

![Showing formula instead of result as there are double quotes around the formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20283'%3E%3C/svg%3E)

Unlike an apostrophe, this is easier to spot as you can see the extra quotes in the cell itself.

**How to fix this?**

This can be fixed by simply removing the quotes or double quotes around the formula and making the formula recalculate.

Here are the steps to do this:

*   Select the cell in which the formula is being displayed as text.
*   Click into the formula bar or double-click on the cell to edit it.
*   Remove the quotes (”) or double quotes (“”) surrounding the formula. Ensure that the formula starts with an equal-to sign (=) and has no text characters before it.
*   Press the Enter key after making the changes.

Also read: [Highlight Cells With Formulas in Excel](https://trumpexcel.com/highlight-cells-with-formulas-excel/)

Reason 6: FORMULATEXT is Being Used
-----------------------------------

The FORMULATEXT function in Excel is designed to display the formula used in a referenced cell as a text string. This function is particularly useful for auditing or documenting the formulas in your spreadsheet.

When you use FORMULATEXT, Excel will show the exact formula contained in the referenced cell, not the result of that formula.

For example:

*   If cell A1 contains the formula =SUM(B1:B20)
*   Using =FORMULATEXT(A1) in another cell will display =SUM(B1:B20) as text.

![FORMULATEXT showing formula in the cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20253'%3E%3C/svg%3E)

**How to fix this?**

If you want to display the result of a formula instead of the formula itself, you should not use FORMULATEXT.

Instead, you can directly reference the cell containing the formula.

**Other Excel articles you may also like:**

*   [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)
    
*   [Identify Errors Using Excel Formula Debugging](https://trumpexcel.com/excel-formula-debugging/)
    
*   [Return Cell Address Instead of Value in Excel](https://trumpexcel.com/return-cell-address-instead-of-value-excel/)
    
*   [Excel Formulas Not Working](https://trumpexcel.com/excel-formulas-not-working/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-showing-formula-instead-of-result/#respond)

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