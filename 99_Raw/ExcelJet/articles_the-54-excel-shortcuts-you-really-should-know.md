# The 54 Excel shortcuts you really should know | Exceljet

**Source:** https://exceljet.net/articles/the-54-excel-shortcuts-you-really-should-know

---

[Skip to main content](https://exceljet.net/articles/the-54-excel-shortcuts-you-really-should-know#main-content)

[](https://exceljet.net/articles/the-54-excel-shortcuts-you-really-should-know#)

*   [Previous](https://exceljet.net/articles/the-value-of-improving-a-skill-a-simple-model)
    
*   [Next](https://exceljet.net/articles/collapse-the-ribbon-when-you-dont-need-it)
    

The 54 Excel shortcuts you really should know
=============================================

by Dave Bruns · Updated 4 Dec 2025

![54 powerful Excel shortcuts](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/shortcut-article.png "54 powerful Excel shortcuts")

Summary
-------

A list and description of just over 50 important Excel shortcuts you should know if you spend a lot of time in Excel. This is a summarized version of the more than 200 shortcuts that are available in Excel for both Windows and Mac platforms.

_There are over 200 Excel shortcuts for both Mac and PC (_[_you can download a PDF here_](https://exceljet.net/shortcuts)
_). This article explains about 50 of the most useful.  – Dave_

### Next worksheet / Previous worksheet

Often, you'll need to switch back and forth between different worksheets in the same workbook. If you are working in a large workbook with many sheets, this can be annoying to do with your mouse, because some sheets may not be visible. However, with these shortcuts, you can quickly move forward and backward through sheets in a workbook using only the keyboard. To navigate sheets with your keyboard, use Control + PgDn (Mac: Option + Right arrow) to move to the _next worksheet_ to the right, and Control + PgUp (Mac: Option + Left arrow) to move to the _previous worksheet_ to the left.

| Shortcut | Win | Mac |
| --- | --- | --- |
| Move to the next worksheet | Ctrl PgDn | ⌥ → |
| Move to the previous worksheet | Ctrl PgUp | ⌥ ← |

### Next workbook / Previous workbook

To rotate to the next open workbook, use the keyboard shortcut Control + Tab (both platforms). To reverse direction, add the shift key: Control + Shift + Tab.

### Expand or collapse ribbon

This shortcut seems a bit frivolous until you realize that the ribbon is sitting there taking up 4 rows of space, even when you're not using it at all. Use Control + F1 (Mac: Command + Option + R) to collapse the ribbon when you don't need it, and bring it back when you do.

> Video: [30 popular Excel shortcuts in 12 minutes](https://exceljet.net/videos/30-excel-shortcuts-in-12-minutes)

### Display the Paste Special dialog box

This shortcut, Control + Alt + V (Mac: Control + Command + V) doesn't actually finish the paste; it just opens the Paste Special dialog box. At that point, you'll need to choose the type of paste you want to perform.

There are so many things you can do with paste special; it's a topic in itself.  At the very least, you probably already use paste special to strip out unwanted formatting and formulas (Paste Special > Values). But did you know that you can also paste formatting, paste column widths, multiply and add values in place, and even transpose tables? It's all there.

### Toggle autofilter

If you frequently filter lists or tables, this shortcut should be at the top of your list.  With the same shortcut, Control + Shift + L (Mac: Command + Shift + F) you can toggle filters on and off any list or data set. But the best part is toggling off the autofilter will clear any filters that have been set. So, if you have multiple filters active, you can "reset" all filters by using the shortcut twice in a row: once to remove the filters (which clears all filters), and once again to add a new autofilter. This is far faster than fiddling with each filter manually.

### Select all

Many people know the shortcut for "select all": Control + A. However, in Excel, this shortcut behaves differently in different contexts. If the cursor is in an empty cell, Control + A selects the entire worksheet. But if the cursor is in a group of _contiguous cells_, Control + A will select the entire group of cells instead.

The behavior changes again when the cursor is in an Excel Table. The first time you use Control + A, the table data is selected. The second time, both the table data + table header are selected. Finally, the third time you use Control + A, the entire worksheet is selected.

### Move to edge of data region

This shortcut sounds boring but it is vital if you routinely work with big lists or tables. Rather than scroll up, down, right and left, manually just put your cursor into the data and use Control + Arrow key to move in any direction to the edge of the data range (On a Mac you can use Command or Control). The cursor will travel to the first empty cell (or the edge of the spreadsheet, whichever comes first). If you start in an empty cell, the behavior is reversed - the cursor will move to the first cell with content and stop.

Move right = Control + Right arrow  
Move left = Control + Left arrow  
Move up = Control + Up arrow  
Move down = Control + Down arrow

Video: [How to move around big lists fast](https://exceljet.net/videos/how-to-move-around-big-lists-fast)

> How fast can the cursor move? Modern Excel has more than 1 million rows. If you put your cursor in A1 and press Control + down arrow, you'll be past the millionth row in less than a second. If we figure there are about 6 rows in an inch, then:
> 
> *   1,048,576 rows / 6 = 174,763 inches / 12 = 14,564 feet / 5280 = 2.76 miles
> *   2.76 miles in 1 second \* 60 = 165.6 miles per minute \* 60 = 9,936 miles per hour.
> 
> So, around 10,000 miles per hour. You're never going to beat it scrolling. Ever.

### Extend selection to the edge of data

Navigating at high speed through a large table is great fun, but what really makes this idea powerful is selecting huge swaths of cells at the same time. Because when you try to select large collections of cells manually (let's say 10,000 rows), you will be scrolling a long time. A _really_ long time.

To save your sanity and avoid all that scrolling, just add the Shift key to the Control + Arrow shortcut, and you will \*extend\* the current selection to include all the cells along the way. The best part about using Shift + Control + Arrow is that your selections are perfectly accurate. Even though the cursor is moving at great speed, it will stop on a dime at the edge of a data region.

Select right = Shift + Control + Right arrow  
Select left = Shift + Control + Left arrow  
Select up = Shift + Control + Up arrow  
Select down = Shift + Control + Down arrow

### Move to first cell in worksheet

Navigating larger worksheets can get really tedious. Sure, you can use the scroll bars to scroll the worksheet into position, but scroll bars require control and patience. If you just want to get back to the first screen in a worksheet, use the keyboard shortcut Control + Home (Mac: Fn + Control + left arrow). This will bring you straight back to cell A1, no matter how far you've wandered.

### Move to last cell in worksheet

In a similar way, you can jump to the "last cell" in a worksheet using Control + End (Mac: Fn + Control + Right arrow). What is the last cell? Good question. The last cell in a worksheet is at the intersection of the last row that contains data and the last column that contains data. Often, the last cell in a worksheet doesn't contain any data itself - it just defines the lower right edge of a rectangle that makes up the used portion of the worksheet.

One good use of this shortcut is to quickly see if there is any other data in the worksheet that you're not aware of. You can use this to make sure you don't accidentally print 16 blank pages because there's stray data in cell BF1345, for some unknown reason. It's also useful when you notice that a workbook is suddenly a lot bigger on disk than it should be. In this case, it's likely that there's extra data somewhere in the worksheet.

### Find next match

Rather basic, but worth knowing: once you've set up a find, and have found at least one match, you can keep finding "the next match" by using Shift F4 (Mac: Command + G). This is a nice way to step through matches in a worksheet methodically.

By the way: to activate Find, use Control + F (Mac: Command + F). On Windows and Mac, you can also use Control + H to activate Find and Replace. On Windows, this will open the find and replace dialog with Replace selected.

### Select row / select column

Both rows and columns can be selected with keyboard shortcuts. To select a row, use Shift + Space. To select a column, use Control + Space.

Once you have a row or column selected, you can hold down the shift key and extend your selection by using the appropriate arrow keys. For example, if the cursor is in row 10 and you press Shift + Space, row 10 will be selected. You can then hold the shift key down and use the Up or Down arrow keys to select additional rows above or below row 10.

Note that if you are working in an Excel table, these same shortcuts will select rows and columns within the table, not the entire worksheet.

Also note that once you have rows or columns selected, you can use other keyboard shortcuts to insert, delete, hide, and unhide.

### Add non-adjacent cells to selection

You'll often need to select cells that aren't next to one another. You might want to enter the same data to several cells (see Control + Enter) change formatting, or even use the status bar to get an on-the-fly SUM for a group of random cells. This is easily done using Control + Click (Mac: Command + Click). Just select the first cell (or cells) then hold down the control or command key and click other cells to add them to your selection.

### Show the active cell on worksheet

Sometimes you have a worksheet open and the cursor is nowhere in sight. You could press an arrow key to bring the cursor into view (and move to a new cell at the same time) or you could consult the namebox to get the address. But you can also just use Control + Backspace (Mac: Command + Delete) to automatically scroll the cursor into view, nicely centered in the window.

### Display 'Go To' dialog box

The Go To Special dialog is a bit like the Paste Special Dialog - within lies a treasure trove of utility hidden in an innocuous sounding control. Did you know you can use Go To Special to select only formulas? Only constants? Only blank cells? You can do all that and a lot more.

Unfortunately, the shortcut Control + G (both platforms) only gets you half way, to the Go To dialog box. From there, you need to click the Special button to get all the way to Go To Special. Control + G is still a worthy shortcut, however, because Go To Special is the gateway to many tricky and powerful features.

Chandoo has a good article that explains Go To Special in detail [here](http://chandoo.org/wp/2012/03/12/go-to-special/)
.

Video: [Go To Special to delete blank rows](https://exceljet.net/videos/shortcut-recipe-delete-blank-rows)

Video: [Go To Special to weed out rows that are missing values](https://exceljet.net/videos/shortcut-recipe-remove-specific-rows)

ENTERING DATA
-------------

### Start a new line in the same cell

This is not so much a shortcut as something you simply must know to enter multiple lines in a single cell. This is often a puzzle to Excel users (for obvious reasons) and I have no doubt that this puzzle has resulted in hundreds of thousands, if not millions, of Google searches. Here is the answer revealed: Alt + Enter (Mac: Control + Option + Return) will add a new line inside a cell.

### Enter the same value in multiple cells

This shortcut may not seem interesting, but you'll be surprised how often you use it once you understand how it works. Use Control + Enter when you want to enter the same value in multiple cells at once. This is a great way to save keystrokes when you want to enter the same value or formula in a group of cells. You can even use Control + Enter to enter data into non-contiguous cells. (See the previous shortcut for selecting non-adjacent cells.)

Control-enter also has another use: use it when you want to enter a value into a cell and stay in that same cell after hitting return.

### Insert current date / Insert current time

No Excel shortcut guide would be complete without mentioning these stalwarts for entering the current date and time.

To enter the current date, use Control + ;

To enter the current time, use Control + Shift + :

If you want to enter both the current date and time, type control +;, then enter a space, followed by Control + Shift + :

With either shortcut, excel will enter the current date or time using a valid Excel date in serial number format, with dates as integers and times as decimal values. You can then apply date or time formatting as you like.

### Fill down / Fill right

These handy shortcuts allow you to quickly copy data from the cell above or the cell to the left, without using the typical "copy, then paste" pattern. To copy a value from the cell above, use Control + D. To copy data from the cell to the left, use Control + R. You can use these same shortcuts to copy data to multiple cells too. The trick is to select both the source cells and target cells before you use the shortcut. (This isn't necessary if you're copying to cells that are directly adjacent to the source cells.)

For example, if you want to copy values from the row above into the next 6 rows in a table. Select the source row and the next 6 target rows. Then use control + D.

FORMATTING
----------

### Format (almost) anything

Now that the ribbon has taken over, this shortcut may seem unnecessary. After all, you can just click on all that bling-bling in the ribbon right? But pay attention grasshopper, this shortcut is the gateway to a lot of formatting options that don't appear in the ribbon. Better yet, you can use this shortcut to instantly access a full set of formatting options, _even when the ribbon is collapsed._

When regular cells are selected, Control + 1 (Mac: Command + 1) opens the Format Cells dialog. From there, you have quick access to number formats, alignment settings, fonts, borders, fills, and cell protection, with no need to hunt these things down in the ribbon.

When you're working with a chart, the same shortcut will open various formatting dialogs, depending on what you have selected. For example, if you have the chart area selected, Control + 1 (Mac: Command + 1) opens the Format Chart Area dialog. If you have data bars selected, the shortcut will open the Format Data Series dialog. And so on.

You can also use this shortcut when working with shapes and smart art.

The bottom line: give this shortcut before you head out to hunt down a formatting option in the ribbon.

_Note: thanks to Excel guru_ [_Jon Peltier_](https://peltiertech.com/)
 _for pointing out to me that Control + 1 is not just for formatting cells!_

### Bold, italic, underline

Basic, boring, yet essential:

Bold = Control + B (Mac: Command + B)  
Italic = Control + I (Mac: Command + I)  
Underline = Control + U (Mac: Command + U)

You should also know you can hold apply these formats to individual words and characters. Just double click the cell to enter edit mode, select the text you want to format, and apply one of these shortcuts.

### Number formats

These shortcuts are not critical, but it's worth knowing that you can apply seven number formats with keyboard shortcuts. Each shortcut follows the same pattern: Control + Shift + \[symbol\]. If you spend a few minutes trying them out, you'll get the idea quickly:

General = Control + Shift + ~  
Currency = Control + Shift + $  
Percentage = Control + Shift + %  
Scientific = Control + Shift + ^  
Date = Control + Shift + #  
Time = Control + Shift + @  
Number = Control + Shift +!

Conspicuously absent: the Accounting format.

FORMULAS
--------

### Edit the active cell

You can either double click a cell or use F2 (Mac: control + U) to enter "edit mode" for the active cell.

### Toggle absolute / relative reference

If you work regularly with formulas and cell addresses, this is one shortcut is essential, and will save you a lot of tedious editing cell references to add and remove the $ character. To use the shortcut, first enter edit mode, then position the cursor in or next to a cell reference you want to change. Then press F4 (Mac: Command + T). Each time you apply the shortcut, Excel will "rotate" one step through relative and absolute options. Starting with a relative reference, the rotation order works like this:  absolute, row locked, column locked, relative. So, for example for the reference A1, you'll see: $A$1, A$1, $A1, and, finally, A1 again.

_Note: on a laptop, you may need to use fn + F4 if function keys are used to control things like screen brightness, volume, etc._

> Video: [Speed run through 20+ formula tips](https://exceljet.net/videos/23-excel-formula-tips)

### Autosum selected cells

Autosum works on both rows and columns. Simply select an empty cell to the right or below the cells you want to sum, and type Alt + = (Mac: Command + Shift + T). Excel will guess the range you are trying to sum and insert the SUM function in one step. For more control, first select the range you intend to sum, including the cell where you'd like the SUM function to be. This prevents Excel from guessing wrong about the range in cases where there are blanks or text values in the sum range.

For even more satisfaction, you can have Excel insert multiple SUM functions at the same time. To sum multiple columns, select a range of empty cells below the columns. To sum multiple rows, select a range of empty cells in a column to the right of the rows.

For the ultimate in shortcut satisfaction, you can have Excel add sum formulas for an entire table in one step. Select a full table of numbers, including empty cells below the table and to the right of the table. Then use this shortcut. Excel will add a SUM function at the bottom of each column, at the right of each row, and, at the lower right corner of the range, giving you column totals, row totals, and a grand total all in one step. In the world of Excel shortcuts, it doesn't get much better than that.

### Toggle formulas on and off

It can often be handy to quickly see all the formulas in a worksheet, without clicking into each cell. By using Control + ', you can display all formulas in a worksheet at once. To dismiss the formulas and show the results of the formulas again, type Control + ' a second time.

This gives you a fast way to audit a worksheet. You can see where formulas are used and to check for consistency at the same time.

### Insert function arguments

This shortcut is a bit of a sleeper. You don't see it mentioned much, but it's pretty cool. What it does: when you're entering a function, after Excel has recognized the function name, typing Control + Shift + A (both platforms) will cause Excel to enter placeholders for all arguments. For example, if you type "=DATE(" and then use Control + Shift + A, Excel gives you "=DATE(year,month,day)". You can then double-click each argument and change it to the address or value you need.

### Paste name into formula

When you're editing a complex formula, that last thing you need is to have to leave edit mode to go find the name of a named range or constant. With this shortcut F3 (no Mac equivalent so far as I know, sorry!) you don't need to. Just press F3 and Excel will open the named range dialog box so that you can paste in the name you need.

### Accept function with autocomplete

When you're entering a function, Excel will try to guess the name of the function you want, and present an autocomplete list for you to select from. The question is, how do you accept one of the options displayed and yet still stay in edit mode? The trick is to use the tab key. When you press tab, Excel adds any parentheses as needed, then leaves the formula bar active so that you can fill in the arguments as needed. On a Mac, you need to use the down arrow key first to select the function you want, then Tab.

WORKING WITH THE GRID
---------------------

### Insert rows / columns

To insert a row or column with a keyboard shortcut, you need to first select an entire row or column, respectively.  The shortcut is the same whether you are inserting rows or columns:

*   With a laptop keyboard, use **Control Shift +**.
*   With a full keyboard, use **Control +**

In older versions of Mac Excel, the shortcut is Control + I.

With an entire row selected, this shortcut will insert a row _above_ the selected row. With an entire column selected, this shortcut will insert a column to the _right_ of the selected column.

You can also insert multiple rows and columns. Just select the number of rows or columns you want to insert before using the shortcut.

As already mentioned, you can use a keyboard shortcut to select entire rows or columns: Shift + space to select a row, Control + space to select a column.

### Delete rows / columns

Like inserting rows or columns, the key to deleting rows and columns is to first select an entire row or column. Once you have a row or column selected, the shortcut for deleting rows is the same as for deleting columns: Control + - (both platforms).

With this same shortcut, you can also delete multiple rows and columns. Just select the number of rows or columns you want to delete, then use Control + -.

Note: use the shortcuts we already mentioned to select rows and columns: Shift + space to select row(s), Control + space to select column(s).

Note 2: if you don't have an entire row or column selected when you use Control + -, Excel will present the Delete dialog box, which contains options for deleting rows and columns, and for shifting cells.

> **Working with entire rows and columns has benefits**.
> 
> *   Inserting rows and columns is a great way to organize data quickly and safely. By adding an entire row or column, there's no chance you'll accidentally push cells out of alignment somewhere else, because all cells are shifted the same amount.
> *   In a similar way, deleting columns and rows is a great way to clean up a worksheet quickly. In one fell swoop, you can slice out tons of junk that would be tedious to clean up manually.
> 
> Before you start tidying up rows or columns that contain nothing useful, ask yourself: _Can I just remove this stuff by deleting rows or columns?_ If so, then do it! Excel doesn't care how many rows or columns you delete. It will just silently replace deleted rows and columns with fresh copies.

### Hide and unhide columns

To hide one or more columns, use the shortcut Control + 0 (both platforms). Any columns that intersect the current selection will be hidden. If you prefer, you can also first select entire columns before using this shortcut.

Note that column letters on either side of hidden columns will appear in blue.

To unhide columns, you must first select cells that span either side of the hidden column, or select columns that span the hidden column(s). Then use the keyboard shortcut Control + Shift + 0.

Note that you are just adding Shift to the shortcut for hiding a column.

### Hide and unhide rows

To hide one or more rows, use the shortcut Control + 9 (both platforms). Any rows that intersect the current selection will be hidden. You can also first select one more entire row if you prefer.

Note that row numbers on either side of hidden rows will appear in blue.

To unhide rows, you must first select rows that span either side of the hidden row, or select entire rows that span the hidden row(s). Then use the keyboard shortcut Control + Shift + 9.

Note that you are just adding Shift to the shortcut for hiding a row.

CHARTS
------

### Create an embedded chart

To create an embedded chart, first select the data that makes up the chart, including any labels. Then use the keyboard shortcut Alt + F1 (Mac: Fn + Alt + F1). Excel will create a new chart on the same worksheet, using your current chart's default settings.

### Create chart in new worksheet

To create a chart on a new sheet, first select the data that makes up the chart. Then use the keyboard shortcut F11 (Mac: Fn + F11). Excel will create a chart in a new sheet based on your current chart default settings. This is a great way to sanity-check data in your worksheet.

> Resources to help you with Excel shortcuts:
> 
> *   [200 Excel shortcuts for Win and Mac](https://exceljet.net/shortcuts)
>      - online & updated frequently
> *   [Laminated quick reference cards](https://exceljet.net/training/excel-shortcuts-card-laminated)
>      - handy reference with no wifi needed
> *   [How to Use Mac Function Keys](https://exceljet.net/articles/how-to-use-mac-function-keys-with-excel)
>      - must read if you use Excel on a Mac
> *   [Video training](https://exceljet.net/training/excel-shortcuts)
>      - learn 200 Excel shortcuts with bite-sized videos

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Training

*   [Core Excel](https://exceljet.net/training/core-excel)
    

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