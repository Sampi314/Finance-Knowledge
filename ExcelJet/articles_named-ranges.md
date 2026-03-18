# Named Ranges in Excel | Exceljet

**Source:** https://exceljet.net/articles/named-ranges

---

[Skip to main content](https://exceljet.net/articles/named-ranges#main-content)

[](https://exceljet.net/articles/named-ranges#)

*   [Previous](https://exceljet.net/articles/concat-textjoin)
    
*   [Next](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

Named Ranges in Excel
=====================

by Dave Bruns · Updated 24 Oct 2023

![How to create named ranges in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/creating%20a%20named%20range%20in%20excel1.png "How to create named ranges in Excel")

Summary
-------

Named ranges make formulas easier to read, faster to develop, and more portable. They're also useful for data validation, hyperlinks, and dynamic ranges. This article shows you how you can use named ranges to build better spreadsheets, and better formulas.

Named ranges are one of these crusty old features in Excel that few users understand. New users may find them weird and scary, and even old hands may avoid them because they seem pointless and complex.

But named ranges are actually a pretty cool feature. They can make formulas \*a lot\* easier to create, read, and maintain. And as a bonus, they make formulas easier to reuse (more portable).

In fact, I use named ranges all the time when testing and prototyping formulas. They help me get formulas working faster. I also use named ranges because I'm lazy, and don't like typing in complex references :)

The basics of named ranges in Excel
-----------------------------------

### What is a named range?

A named range is just a human-readable name for a range of cells in Excel. For example, if I name the range A1:A100 "data", I can use MAX to get the maximum value with a simple formula:

     =MAX(data) // max value
    

![Simple named range called "data"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/simple%20named%20range%20data.png?itok=db0tLj-G "Simple named range called "data"")

The beauty of named ranges is that you can use meaningful names in your formulas without thinking about cell references. Once you have a named range, just use it just like a cell reference. All of these formulas are valid with the named range "data":

    =MAX(data) // max value
    =MIN(data) // min value
    =COUNT(data) // total values
    =AVERAGE(data) // min value
    

Video: [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)

### Creating a named range is easy

Creating a named range is fast and easy. Just select a range of cells, and type a name into the name box. When you press return, the name is created:

![Create a named range fast with name box](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create%20a%20named%20range%20fast%20with%20name%20box.png?itok=g4f1P1mf "Create a named range fast with name box")

To quickly test the new range, choose the new name in the dropdown next to the name box. Excel will select the range on the worksheet.

### Excel can create names automatically (ctrl + shift + F3)

If you have well structured data with labels, you can have Excel create named ranges for you. Just select the data, along with the labels, and use the "Create from Selection" command on the Formulas tab of the ribbon:

![Create names from selection command on ribbon](https://exceljet.net/sites/default/files/images/articles/inline/ribbon%20create%20from%20selection.png "Create names from selection command on ribbon")

You can also use the keyboard shortcut control + shift + F3.

Using this feature, we can create named ranges for the population of 12 states in one step:

![Create names from selection with data and labels selected](https://exceljet.net/sites/default/files/images/articles/inline/create%20names%20create.png "Create names from selection with data and labels selected")

When you click OK, the names are created. You'll find all newly created names in the drop down menu next to the name box:

![New names also appear in the name box drop down menu](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create%20names%20dropdown.png?itok=ohQe_PLp "New names also appear in the name box drop down menu")

With names created, you can use them in formulas like this

    =SUM(MN,WI,MI)
    

### Update named ranges in the Name Manager (Control + F3)

Once you create a named range, use the [Name Manager](https://exceljet.net/glossary/name-manager)
 (Control + F3) to update as needed. Select the name you want to work with, then change the reference directly (i.e. edit "refers to"), or click the button at right and select a new range.

![Updated named ranges with the Name Manager](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/update%20named%20range%20with%20name%20manager.png?itok=8Vwgp6JX "Updated named ranges with the Name Manager")

There's no need to click the Edit button to update a reference. When you click Close, the range name will be updated.

_Note: if you select an entire named range on a worksheet, you can drag to a new location and the reference will be updated automatically. However, I don't know a way to adjust range references by clicking and dragging directly on the worksheet. If you know a way to do this, chime in below!_

### See all named ranges (control + F3)

To quickly see all named ranges in a workbook, use the dropdown menu next to the name box.

If you want to see more detail, open the Name Manager (Control + F3), which lists all names with references, and provides a filter as well:

![The name manager shows all newly created names](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create%20names%20with%20labels%20result.png?itok=u8eVSx8H "The name manager shows all newly created names")

_Note: in older versions of Excel on the Mac, there is no Name Manager, and you'll see the Define Name dialog instead._

### Copy and paste all named ranges (F3)

If you want a more persistent record of named ranges in a workbook, you can paste the full list of names anywhere you like. Go to Formulas > Use in Formula (or use the shortcut F3), then choose Paste names > Paste List:

![Paste names dialog box](https://exceljet.net/sites/default/files/images/articles/inline/paste%20names%20dialog%20box.png "Paste names dialog box")

When you click the Paste List button, you'll see the names and references pasted into the worksheet:

![After pasting named ranges into worksheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/paste%20names%20result.png?itok=2_FFIJwF "After pasting named ranges into worksheet")

### See names directly on the worksheet

If you set the zoom level to less than 40%, Excel will show range names directly on the worksheet:

![At zoom level <40%, Excel will show range names](https://exceljet.net/sites/default/files/images/articles/inline/zoom%20less%20than%2040%20shows%20range%20names.png "At zoom level <40%, Excel will show range names")

Thanks for this tip, Felipe!

### Names have rules

When creating named ranges, follow these rules:

1.  Names must begin with a letter, an underscore (\_), or a backslash (\\)
2.  Names can't contain spaces and most punctuation characters.
3.  Names can't conflict with cell references – you can't name a range "A1" or "Z100".
4.  Single letters are OK for names ("a", "b", "x", etc.), but the letters "r" and "c" are reserved.
5.  Names are not case-sensitive – "home", "HOME", and "HoMe" are all the same to Excel.

Named ranges in formulas
------------------------

### Named ranges are easy to use in formulas

For example, lets say you name a cell in your workbook "updated". The idea is you can put the current date in the cell (Ctrl + ;) and refer to the date elsewhere in the workbook.

![Using a named range inside a text formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/last%20update%20message%20with%20named%20range.png?itok=t3z8eOmx "Using a named range inside a text formula")

The formula in B8 looks like this:

    ="Updated: "& TEXT(updated, "ddd, mmmm d, yyyy")
    

You can paste this formula anywhere in the workbook and it will display correctly. Whenever you change the date in "updated", the message will update wherever the formula is used. See [this page](https://exceljet.net/formulas/last-updated-date-stamp)
 for more examples.

### Named ranges appear when typing a formula

Once you've created a named range, it will appear automatically in formulas when you type the first letter of the name. Press the tab key to enter the name when you have a match and want Excel to enter the name.

![Named ranges appear when entering formulas](https://exceljet.net/sites/default/files/images/articles/inline/named%20ranges%20when%20entering%20formula.png "Named ranges appear when entering formulas")

### Named ranges can work like constants

Because named ranges are created in a central location, you can use them like constants without a cell reference. For example, you can create names like "MPG" (miles per gallon) and "CPG" (cost per gallon) with and assign fixed values:

![Named ranges can work like constants, with no cell reference](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20as%20constants1.png?itok=hrl8-TQY "Named ranges can work like constants, with no cell reference")

Then you can use these names anywhere you like in formulas, and update their value in one central location.

![Using a named range like a constant in a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20as%20constants2.png?itok=48W5SX0t "Using a named range like a constant in a formula")

### Named ranges are absolute by default

By default, named ranges behave like absolute references. For example, in this worksheet, the formula to calculate fuel would be:

    =C5/$D$2
    

![Standard formula with absolute address](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20are%20absolute1.png?itok=7n9x4rLt "Standard formula with absolute address")

The reference to D2 is absolute (locked) so the formula can be copied down without D2 changing.

If we name D2 "MPG" the formula becomes:

    =C5/MPG
    

![Using a named range like a constant in a formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20are%20absolute3.png.png?itok=0wf6nL-L "Using a named range like a constant in a formula")

Since MPG is absolute by default, the formula can be copied down column D as-is.

### Named ranges can also be relative

Although named ranges are absolute by default, they can also be relative.  A relative named range refers to a range that is relative to the position of the active cell _at the time the range is created_. As a result, relative named ranges are useful building generic formulas that work wherever they are moved.

For example, you can create a generic "CellAbove" named range like this:

1.  Select cell A2
2.  Control + F3 to open Name Manager
3.  Tab into 'Refers to' section, then type: =A1

CellAbove will now retrieve the value from the cell above wherever it is it used.

_Important: make sure the active cell is at the correct location before creating the name._

### Apply named ranges to existing formulas

If you have existing formulas that don't use named ranges, you can ask Excel to apply the named ranges in the formulas for you. Start by selecting the cells that contain formulas you want to update. Then run Formulas > Define Names > Apply Names.

![The Apply Names dialog box](https://exceljet.net/sites/default/files/images/articles/inline/apply%20names%20dialog%20box.png "The Apply Names dialog box")

Excel will then replace references that have a corresponding named range with the name itself.

You can also apply names with find and replace:

![Applying names ranges with find and replace](https://exceljet.net/sites/default/files/images/articles/inline/apply%20names%20with%20find%20and%20replace.png "Applying names ranges with find and replace")

> Important: Save a backup of your worksheet, and select just the cells you want to change before using find and replace on formulas.

Key benefits of named ranges
----------------------------

### Named ranges make formulas easier to read

The biggest single benefit to named ranges is they make formulas easier to read and maintain. This is because they replace cryptic references with meaningful names. For example, consider this worksheet with data on planets in our solar system.  Without named ranges, a VLOOKUP formula to fetch "Position" from the table is quite cryptic:

    =VLOOKUP($H$4,$B$3:$E$11,2,0)
    

![Without named ranges formulas can be cryptic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20for%20readability1.png?itok=O861Q5cd "Without named ranges formulas can be cryptic")

However, with B3:E11 named "data", and H4 named "planet", we can write formulas like this:

    =VLOOKUP(planet,data,2,0) // position
    =VLOOKUP(planet,data,3,0) // diameter
    =VLOOKUP(planet,data,4,0) // satellites
    

![With named ranges, formulas can be simple](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20for%20readability2.png?itok=NGS-9fpo "With named ranges, formulas can be simple")

At a glance, you can see the only difference in these formulas in the column index.

### Named ranges make formulas portable and reusable

Named ranges can make it much easier to reuse a formula in a different worksheet. If you define names ahead of time in a worksheet, you can paste in a formula that uses these names and it will "just work". This is a great way to quickly get a formula working.

For example, this formula counts unique values in a range of numeric data:

    =SUM(--(FREQUENCY(data,data)>0))
    

To quickly "port" this formula to your own worksheet, name a range "data" and paste the formula into the worksheet. As long as "data" contains numeric values, the formula will work straightway.

_Tip: I recommend that you create the needed range names \*first\* in the destination workbook, then copy in the formula as text only (i.e. don't copy the cell that contains the formula in another worksheet, just copy the text of the formula). This stops Excel from creating names on-the-fly and l__ets you to fully control the name creation process. To copy only formula text, copy text from the formula bar, or copy via another application (i.e. browser, text editor, etc.)._

### Named ranges can be used for navigation

Named ranges are great for quick navigation. Just select the dropdown menu next to the name box, and choose a name. When you release the mouse, the range will be selected. When a named range exists on another sheet, you'll be taken to that sheet automatically.

![Named ranges allow for simple navigation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/navigation%20with%20named%20ranges.png?itok=4HQ2JrEl "Named ranges allow for simple navigation")

### Named ranges work well with hyperlinks

Named ranges make hyperlinks easy. For example, if you name A1 in Sheet1 "home", you can create a hyperlink somewhere else that takes you back there.

![Creating a hyperlink to a named range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/hyperlink%20to%20named%20range%20define.png?itok=fA_lB5ql "Creating a hyperlink to a named range")

![Example of named range hyperlink on the worksheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/hyperlink%20to%20named%20range%20example.png?itok=K-OKvVpC "Example of named range hyperlink on the worksheet")

To use a named range inside the [HYPERLINK function](https://exceljet.net/functions/hyperlink-function)
, add a hash (#) in front of the named range:

    =HYPERLINK("#home","take me home")
    

You can use this same syntax to create a hyperlink to a table:

    =HYPERLINK("#Table1","Go to Table1")

_Note: in older versions of Excel you can't link to a table like this. However, you can define a name equal to a table (i.e. =Table1) and hyperlink to that._

### Named ranges for data validation

Names ranges work well for data validation, since they let you use a logically named reference to validate input with a drop down menu. Below, the range G4:G8 is named "statuslist", then apply data validation with a List linked like this:

![Using a named range for data validation with list](https://exceljet.net/sites/default/files/images/articles/inline/named%20ranges%20for%20data%20validation%20setup.png "Using a named range for data validation with list")

The result is a dropdown menu in column E that only allows values in the named range:

![Data validation with named range example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/named%20ranges%20for%20data%20validation%20result.png?itok=7QzZVX3d "Data validation with named range example")

Dynamic Named Ranges
--------------------

Names ranges are extremely useful when they automatically adjust to new data in a worksheet. A range set up this way is referred to as a "dynamic named range". There are two ways to make a range dynamic: formulas and tables.

### Dynamic named range with a Table

A Table is the easiest way to create a dynamic named range. Select any cell in the data, then use the shortcut Control + T:

![Creating am Excel Table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dynamic%20range%20with%20table1.png?itok=_OwWZ109 "Creating am Excel Table")

When you create an Excel Table, a name is automatically created (e.g. Table1), but you can rename the table as you like. Once you have created a table, it will expand automatically when data is added.

![Tables will expand automatically and can be renamed](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dynamic%20range%20with%20table2.png?itok=lpQWLx-G "Tables will expand automatically and can be renamed")

### Dynamic named range with a formula

You can also create a dynamic named range with formulas, using functions like OFFSET and INDEX. Although these formulas are moderately complex, they provide a lightweight solution when you don't want to use a table. The links below provide examples with full explanations:

*   [Example of dynamic range formula with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)
    
*   [Example of dynamic range formula with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    

### Table names in data validation

Since Excel Tables provide an automatic dynamic range, they would seem to be a natural fit for data validation rules, where the goal is to validate against a list that may be always changing. However, one problem with tables is that you can't use structured references directly to create data validation or conditional formatting rules. In other words, you can't use a table name in conditional formatting or data validation input areas.

However, as a workaround, you can define named a named range that points to a table, and then use the named range for data validation or conditional formatting. The video below runs through this approach in detail.

Video: [How to use named ranges with tables](https://exceljet.net/videos/how-to-use-named-ranges-with-tables)

Deleting named ranges
---------------------

_Note: If you have formulas that refer to named ranges, you may want to update the formulas first before removing names. Otherwise, you'll see #NAME? errors in formulas that still refer to deleted names. Always save your worksheet before removing named ranges in case you have problems and need to revert to the original._

### Named ranges adjust when deleting and inserting cells 

When you delete \*part\* of a named range, or if  insert cells/rows/columns inside a named range, the range reference will adjust accordingly and remain valid. However, if you delete all of the cells that enclose a named range, the named range will lose the reference and display a #REF error. For example, if I name A1 "test", then delete column A, the name manager will show "refers to" as:

    =Sheet1!#REF!
    

### Delete names with Name Manager

To remove named ranges from a workbook manually, open the name manager, select a range, and click the Delete button. If you want to remove more than one name at the same time, you can Shift + Click or Ctrl + Click to select multiple names, then delete in one step.

### Delete names with errors

If you have a lot of names with reference errors, you can use the filter button in the name manager to filter on names with errors:

![Name Manager filter menu](https://exceljet.net/sites/default/files/images/articles/inline/name%20manager%20filter.png "Name Manager filter menu")

Then shift+click to select all names and delete.

Named ranges and Scope
----------------------

Named ranges in Excel have something called "scope", which determines whether a named range is local to a given worksheet, or global across the entire workbook. Global names have a scope of "workbook", and local names have a scope equal to the sheet name they exist on. For example, the scope for a local name might be "Sheet2". 

### The purpose of scope

Named ranges with a global scope are useful when you want all sheets in a workbook to have access to certain data, variables, or constants. For example, you might use a global named range a tax rate assumption used in several worksheets.

### Local scope

Local scope means a name is works only on the sheet it was created on. This means you can have multiple worksheets in the same workbook that all use the same name. For example, perhaps you have a workbook with monthly tracking sheets (one per month) that use named ranges with the same name, all scoped locally. This might allow you to reuse the same formulas in different sheets. The local scope allows the names in each sheet to work correctly without colliding with names in the other sheets.

To refer to a name with a local scope, you can prefix the sheet name to the range name:

    Sheet1!total_revenue
    Sheet2!total_revenue
    Sheet3!total_revenue
    

Range names created with the [name box](https://exceljet.net/glossary/name-box)
 automatically have global scope. To override this behavior, add the sheet name when defining the name:

    Sheet3!my_new_name
    

### Global scope

Global scope means a name will work anywhere in a workbook. For example, you could name a cell "last\_update", enter a date in the cell. Then you can use the formula below to display the date last updated in any worksheet.

    =last_update
    

Global names must be unique within a workbook.

### Local scope

Locally scoped named ranges make sense for worksheets that use named ranges for local assumptions only. For example, perhaps you have a workbook with monthly tracking sheets (one per month) that use named ranges with the same name, all scoped locally. The local scope allows the names in each sheet to work correctly without colliding with names in the other sheets.

### Managing named range scope

By default, new names created with the namebox are global, and you can't edit the scope of a named range after it's created. However, as a workaround, you can delete and recreate a name with the desired scope.

If you want to change several names at once from global to local, sometimes it makes sense to copy the sheet that contains the names. When you duplicate a worksheet that contains named ranges, Excel copies the named ranges to the second sheet, changing the scope to local at the same time. After you have the second sheet with locally scoped names, you can optionally delete the first sheet.

Jan Karel Pieterse and [Charles Williams](https://fastexcel.wordpress.com/)
 have developed a utility called the Name Manager that provides many useful operations for named ranges. You can [download the Name Manager utility here](http://www.jkp-ads.com/OfficeMarketPlaceNM-EN.asp)
.

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