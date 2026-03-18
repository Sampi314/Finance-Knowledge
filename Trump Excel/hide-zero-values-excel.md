# Hide Zero Values in Excel | Make Cells Blank If the Value is 0

**Source:** https://trumpexcel.com/hide-zero-values-excel

---

[Skip to content](https://trumpexcel.com/hide-zero-values-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/hide-zero-values-excel/#below-title)

**Watch Video – How to Hide Zero Values in Excel + How to Remove Zero Values**

In case you prefer reading over watching a video, below is the complete written tutorial.

Sometimes in Excel, you may want to **hide zero values** in your dataset and show these cells as blanks.

Suppose you have a dataset as shown below and you want to hide the value 0 in all these cells (or want to replace it with something such as a dash or the text ‘Not Available’).

![Data set that has zeroes in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20335'%3E%3C/svg%3E)

While you can do this manually with a small dataset, you’ll need better ways when working with large datasets.

In this tutorial, I will show you multiple ways to hide zero values in Excel and one method to select and remove all the zero values from the dataset.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/hide-zero-values-excel/#)

**Important Note**: When you hide a 0 in a cell using the methods shown in this tutorial, it will only hide the 0 and not remove it. While the cells may look empty, those cells still contain the 0s. And in case you use these cells (that have hidden zeroes) in any formula, these will be used in the formula.

Let’s get started and dive into each of these methods!

Automatically Hide Zero Value in Cells
--------------------------------------

Excel has an inbuilt functionality that allows you to automatically hide all the zero values for the entire worksheet.

All you have to do is uncheck a box in Excel options, and the change will be applied to the entire worksheet.

Suppose you have the sales dataset as shown below and you want to hide all the zero values and show a blank cells instead.

![Data set that has zeroes in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20335'%3E%3C/svg%3E)

Below are the steps to hide zeros from all the cells in a workbook in Excel:

1.  Open the workbook in which you want to hide all the zeros
2.  Click the File tab![Click the File option in the ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20396%20196'%3E%3C/svg%3E)
3.  Click on Options![Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20240%20461'%3E%3C/svg%3E)
4.  In the Excel Options dialog box that opens, click on the ‘Advanced’ option in the left pane![Click the Advanced option in the Left pane in Excel Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20510%20376'%3E%3C/svg%3E)
5.  Scroll down to the section that says ‘Display option for this worksheet’, and select the worksheet in which you want to hide the zeros.![Select the worksheet in which you want to hide zeroes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20385'%3E%3C/svg%3E)
6.  Uncheck the ‘Show a zero in cells that have zero value’ option![Uncheck the option - Show a zero in cells that have zero value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20657%20512'%3E%3C/svg%3E)
7.  Click Ok

The above steps would instantly hide zeros in all the cells in the selected worksheet.

This change is also applied to cells where zero is a result of a formula.

Remember that this method only hides the 0 value in the cells and doesn’t remove these. The 0 is still there, it’s just hidden.

This is the best and fastest method to hide zero values in Excel. But this is useful only if you want to hide zero values in the entire worksheet. In case you only want this to hide zero values in a specific range of cells, it’s better to use other methods covered next in this tutorial.

Hide Zero Value in Cells using Conditional Formatting
-----------------------------------------------------

While the above method is the most convenient one, it doesn’t allow you to hide zeros only in a specific range (rather it hides zero values in the entire worksheet).

In case you only want to hide zeros for a specific dataset (or multiple datasets), you can use conditional formatting.

With conditional formatting, you can apply a specific format based on the value in the cells. So, if the value in some cells is 0, you can simply program conditional formatting to hide it (or even highlight it if you want).

Suppose you have a dataset as shown below and you want to hide zeros in the cells.

![Data set that has zeroes in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20335'%3E%3C/svg%3E)

Below are the steps to hide zeros in Excel using conditional formatting:

1.  Select the dataset
2.  Click the ‘Home’ tab![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20198'%3E%3C/svg%3E)
3.  In the ‘Styles’ group, click on ‘Conditional Formatting’.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20157'%3E%3C/svg%3E)
4.  Place the cursor over the ‘Highlight Cells Rules’ options and in the options that show up, click on the ‘Equal to’ option.![Click on the Equal to option in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20508'%3E%3C/svg%3E)
5.  In the ‘Equal To’ dialog box, enter ‘0’ in the left field.![Enter 0 in the Equal to field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20159'%3E%3C/svg%3E)
6.  Select the Format drop-down and click on ‘Custom Format’.![Click on Custom Formatting in the formatting options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20227'%3E%3C/svg%3E)
7.  In the ‘Format Cells’ dialog box, select the ‘Font’ tab.
8.  From the Color drop-down, choose the white color.![Select the white font color to hide the zeroes using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20575'%3E%3C/svg%3E)
9.  Click OK.
10.  Click OK.

The above steps change the font color of the cells that have the zeros to white, which make these cells look blank.

This workaround works only when you have a white background in your worksheet. In case there is any other background-color in the cells, the white color may still keep the zeros visible.

In case you want to truly hide the zeros in the cells, where the cells look blank no matter what background color is given to the cells, you can use the steps below.

1.  Select the dataset
2.  Click the ‘Home’ tab![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20198'%3E%3C/svg%3E)
3.  In the ‘Styles’ group, click on ‘Conditional Formatting’.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20157'%3E%3C/svg%3E)
4.  Place the cursor over the ‘Highlight Cells Rules’ options and in the options that show up, click on the ‘Equal to’ option.
5.  In the ‘Equal To’ dialog box, enter 0 in the left field.![Enter 0 in the Equal to field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20159'%3E%3C/svg%3E)
6.  Select the Format drop-down and click on Custom Format.![Click on Custom Formatting in the formatting options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20227'%3E%3C/svg%3E)
7.  In the ‘Format Cells’ dialog box, select the ‘Number’ tab and click on the ‘Custom’ option in the left pane.
8.  In the Custom format option, enter the following in the Type field: **;;;** (three semi-colons without space)![Custom format to hide zeroes using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20575'%3E%3C/svg%3E)
9.  Click OK.
10.  Click OK.

The above steps change the custom formatting of cells that have the value 0.

When you use three semi-colons as the format, it hides everything in the cell (be it numeric or text). And since this format is applied only to those cells which have the value 0 in it, it only hides the zeros and not the rest of the dataset.

You can also use this method to highlight these cells in a different color (such as red or yellow). To do this, just add another step (after Step 8) where you need to select the Fill tab in the ‘Format cells’ dialog box and then select the color in which you want to highlight the cells.

Both the methods covered above also work when 0 is a result of a formula in a cell.

Note: Both the method covered in this section only hide the zero values. It doesn’t remove these zeros. This means that in case you use these cells in calculations, all the zeros will be used as well.

Hide Zero Value using Custom Formatting
---------------------------------------

Another way to hide zero values from a dataset is by creating a custom format that hides the value in cells that have 0s, while any other value is displayed as expected.

Below are the steps to use a custom format to hide zeros in cells:

1.  Select the entire dataset for which you want to apply this format. If you want this for the entire worksheet, select all the cells
2.  With the cells selected, click the Home tab![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20198'%3E%3C/svg%3E)
3.  In the Cells group, click the Format option![Click the Format option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20156'%3E%3C/svg%3E)
4.  From the drop-down option, click on Format Cells. This will open the Format cells dialog box![Click on Format Cells option in the drop-down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20225%20582'%3E%3C/svg%3E)
5.  In the Format Cells dialog box, select the Number tab![Select the Number tab in the Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20535'%3E%3C/svg%3E)
6.  In the option on the left pane, click on the Custom option.![Click the Custom option in the Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20535'%3E%3C/svg%3E)
7.  In the options on the right, enter the following format in the Type field: **0;-0;;@![Enter the custom format to hide zeroes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20535'%3E%3C/svg%3E)**
8.  Click OK

The above steps would apply a custom format to the selected cells where only those cells which have the value 0 are formatted to hide the value, while the rest of the cells display the data as expected.

**How does this custom format work?**

In Excel, there are four types of data formats that you specify:

1.  Positive numbers
2.  Negative numbers
3.  Zeros
4.  Text

And for each of these data types, you can specify a format.

In most cases, there is a default format – General, which keeps all these data types visible. But you have the flexibility of creating a specific format for each of these data types.

Below is the custom format structure you need to follow in case you are applying a custom format to each of these data types:

**_<Positive Numbers>;<Negative Numbers>;<Zeros>;<Text>_**

In the method covered above, I have specified the format to:

**0;-0;;@**

The above format does the following:

1.  Positive numbers are shown as is
2.  Negative numbers are shown with a negative sign
3.  Zeros are hidden (as no format is specified)
4.  Text is shown as is

**Pro Tip**: If you want [negative numbers to show up as red](https://trumpexcel.com/negative-numbers-red-excel/)
 in your dataset, use the following custom format: **0;\[Red\]0;0;@**

Replace Zeros with Dash or Some Specific Text
---------------------------------------------

In some cases, you may want to not just hide the zeros in the cells, but replace these with something more meaning.

For example, you may want to remove the zeros and replace it with a dash or a text such as “Not Available” or “Data Yet to Come”

This is again made possible [using custom number formatting](https://trumpexcel.com/excel-custom-number-formatting/)
, where you can specify what a cell should display instead of a zero.

Below are the steps to convert a 0 to a dash in Excel:

1.  Select the entire dataset for which you want to apply this format. If you want this for the entire worksheet, select all the cells
2.  With the cells selected, click the Home tab![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20198'%3E%3C/svg%3E)
3.  In the Cells group, click the Format option![Click the Format option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20156'%3E%3C/svg%3E)
4.  From the drop-down option, click on Format Cells. This will open the Format cells dialog box![Click on Format Cells option in the drop-down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20225%20582'%3E%3C/svg%3E)
5.  In the Format Cells dialog box, select the Number tab![Select the Number tab in the Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20535'%3E%3C/svg%3E)
6.  In the option on the left pane, click on the Custom option.
7.  In the options on the right, enter the following format in the Type field: **0;-0;–;@![Enter the format to replace zero with dash](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20603'%3E%3C/svg%3E)**
8.  Click OK

The above steps would keep all the other cells as is and change the cells with the value 0 to show a dash (–).

**Note**: In this example, I have chosen to replace the zero with a dash, but you can use any text as well. For example, if you want to show the NA in the cells, you can use the following format: **0;-0;”NA”;@**

**Pro Tip**: You can also specify a few text colors in custom number formatting. For example, if you want the cells with zeros to show the text NA in red color, you can use the following format: **0;-0;\[Red\]”NA”;@**

Hide Zero Values in Pivot Tables
--------------------------------

There can be two scenarios where a Pivot Table shows the value as 0:

1.  The source data cells that are summarized in the Pivot Table has 0 values
2.  The source data cells that are summarized in the Pivot Table are blanks and the Pivot table has been formatted to show the empty cells as zero

Let’s see how to hide the zeros in the Pivot table in each scenario:

### When Source Data cells have 0s

Below is a sample dataset that I have used to create a Pivot table. Note that the Quantity/Revenue/Profit numbers for all the records for ‘West’ are 0.

![Pivot Table Data which has 0 in the records](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20259'%3E%3C/svg%3E)

The Pivot table created using this data set looks as shown below:

![Pivot Table that has 0](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20201'%3E%3C/svg%3E)

Since there were 0s in the dataset for all the records for West region, you see a 0 in the Pivot table for west here.

If you want to hide zero in this Pivot Table, you can use conditional formatting to do this.

However, conditional formatting in the Pivot Table in Excel works a little different than regular data.

Here are the steps to apply conditional formatting to Pivot Table to hide zeros:

1.  Select any cell in the column that has 0s in the Pivot Table summary (Do not select all the cells, but only one cell)
2.  Click the Home tab
3.  In the ‘Styles’ group, click on ‘Conditional Formatting’.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20157'%3E%3C/svg%3E)
4.  Place the cursor over the ‘Highlight Cells Rules’ options and in the options that show up, click on the ‘Equal to’ option.![Click on the Equal to option in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20508'%3E%3C/svg%3E)
5.  In the ‘Equal To’ dialog box, enter 0 in the left field.![Enter 0 in the Equal to field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20159'%3E%3C/svg%3E)
6.  Select the Format drop-down and click on Custom Format.![Click on Custom Formatting in the formatting options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20227'%3E%3C/svg%3E)
7.  In the ‘Format Cells’ dialog box, select the Number tab and click on the ‘Custom’ option in the left pane.
8.  In the Custom format option, enter the following in the Type field: **;;;** (three semi-colons without space)![Custom format to hide zeroes using conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20575'%3E%3C/svg%3E)
9.  Click OK. You will see small Formatting Options icon at the right of the selected cell.
10.  Click on this ‘Formatting Options’ icon![Formatting Option icon when conditional formatting is applied to Pivot Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20195'%3E%3C/svg%3E)
11.  In the options that become available, choose – All cells showing “Sum of Revenue” values for “Region”.![Select All cells showing Sum of Revenue values for Region option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20682%20203'%3E%3C/svg%3E)

The above steps hide the zero in the Pivot Table in such a way that if you change the Pivot Table structure (by adding more rows/columns headers to it, the zeros will continue to be hidden).

If you want to learn more about how this works, here is a detailed tutorial on the right way to **[apply conditional formatting to Pivot Tables](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
**.

### When Source Data cells have empty cells

Below is an example where I have a dataset that has empty cells for all the records for West.

![Pivot Table where there are blank cells in source data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20299'%3E%3C/svg%3E)

If I create a Pivot Table using this data, I will get the result as shown below.

![Pivot table when there are blank cells in source data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20343%20192'%3E%3C/svg%3E)

By default, the Pivot Table shows you empty cells when all the cells in the source data are blank. But in case you still see a 0 in this case, follow the below steps to hide the zero and show blank cells:

1.  Right-click on any of the cells in the Pivot Table
2.  Click on ‘Pivot Table Options’![Right click on any cell in Pivot Table and then click on Pivot Table options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20512'%3E%3C/svg%3E)
3.  In the ‘PivotTable Options’ dialog box, click on the ‘Layout & Format’ tab
4.  In the Format options, check the options and ‘For empty cells show:’ and leave it blank.![Check the option for empty cells show and keep it blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20488'%3E%3C/svg%3E)
5.  Click OK.

The above steps would hide the zeros in the Pivot Table and show a blank cell instead.

In case you want the Pivot Table to show something instead of the 0, you can specify that in step 4. For example, if you want to show the text – ‘Data not Available’, instead of the 0, type this text in the field (as shown below).

![Show Data Not Available in Pivot Table instead of 0](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20490'%3E%3C/svg%3E)

Find and Remove Zeros in Excel
------------------------------

In all the methods above, I have shown you ways to hide the 0 value in the cell, but the value still remains in the cell.

In case you want to remove the zero values from the dataset (which would leave you with blank cells), use the below steps:

1.  Select the dataset (or the entire worksheet)
2.  Click the Home tab
3.  In the ‘Editing’ group, click on ‘Find & Select’
4.  In the options that are shown in the drop-down, click on ‘Replace’![Click on Replace in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20229%20435'%3E%3C/svg%3E)
5.  In the ‘Find and Replace’ dialog box, make the following changes:
    *   In the ‘Find what’ field, enter 0
    *   In the ‘Replace with’ field, enter nothing (leave it empty)
    *   Click on Options button and check the ‘Match entire cell contents’ option![Find and Replace options to replace 0 with blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)
6.  Click on Replace All

The above steps would instantly replace all the cells that had zero value with a blank.

In case you don’t want to remove the zeros right away and first select the cells, use the following steps:

1.  Select the dataset (or the entire worksheet)
2.  Click the Home tab
3.  In the ‘Editing’ group, click on ‘Find & Select’
4.  In the options that are shown in the drop-down, click on ‘Replace’
5.  In the ‘Find and Replace’ dialog box, make the following changes:
    *   In the ‘Find what’ field, enter 0
    *   In the ‘Replace with’ field, enter nothing (leave it empty)
    *   Click on Options button and check the ‘Match entire cell contents’ option![Find and Replace options to replace 0 with blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)
6.  Click on the ‘Find All’ button. This will give you a list of all the cells that have 0 in it![Click on Find All to find all cells with 0 in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)
7.  Press Control-A (hold the control key and press A). This will select all the cells that have 0 in it.![Find and Select all cells with 0 in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20560'%3E%3C/svg%3E)

Now, that you have all the cells with 0 selected, you can delete these, replace these with something else, or change the color and highlight these.

Hiding the Zeros Vs. Removing The Zeros
---------------------------------------

When treating the cells with 0s in it, you need to know the difference between hiding these and removing these.

When you hide the zero value in a cell, it is not visible to you, but it still remains in the cell. This means that if you have a dataset and you use it for calculation, that 0 value will also be used in the calculation.

On the contrary, when you have a blank cell, using it in formulas may mean that Excel automatically ignores these cells (depending on which formula you’re using).

For example, below is what I get when I use the AVERAGE formula to get the average for two columns (the result is in row 14). Column A has cells where the 0 value has been hidden (but is still there in the cell) and Column B has cells where the 0 value has been removed.

![Difference between hiding zero values and removing zero values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20360'%3E%3C/svg%3E)

You can see the difference in the result despite the fact that the dataset for both datasets looks the same.

This happens as the [AVERAGE formula](https://trumpexcel.com/excel-average-function/)
 ignores blank cells in column B, but it uses the ones in Column A (as the ones in column A still has the value 0 in it).

**You may also like the following Excel tutorials:**

*   [How to Hide a Worksheet in Excel](https://trumpexcel.com/hide-worksheet/)
    
*   [Delete Rows Based on a Cell Value](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    
*   [Delete Blank Rows in Excel](https://trumpexcel.com/delete-blank-rows-excel/)
    
*   [How to Delete Every Other Row in Excel (or Every Nth Row)](https://trumpexcel.com/delete-every-other-row-excel/)
    
*   [Show Formulas in Excel Instead of the Values](https://trumpexcel.com/show-formulas-in-excel/)
    
*   [Change Negative Number to Positive in Excel](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Remove Leading Zeros in Excel](https://trumpexcel.com/remove-leading-zeros-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “Hide Zero Values in Excel | Make Cells Blank If the Value is 0”
------------------------------------------------------------------------------

1.  This helps big-time, using Custom Format cells to provide my BLANK WHEN ZERO solution. Many thanks from Auckland, NZ.
    
    [Reply](https://trumpexcel.com/hide-zero-values-excel/#comment-31333)
    
2.  Thank you very much
    
    [Reply](https://trumpexcel.com/hide-zero-values-excel/#comment-14899)
    
3.  You are absolutely amazing! I love every video from you!
    
    [Reply](https://trumpexcel.com/hide-zero-values-excel/#comment-12592)
    
4.  As usual, a fantastic article, very well written. Keep up good work. Greetings from Romania.
    
    [Reply](https://trumpexcel.com/hide-zero-values-excel/#comment-12360)
    
    *   Glad you found it useful!
        
        [Reply](https://trumpexcel.com/hide-zero-values-excel/#comment-12368)
        
        *   Summit you’re still great! Cheers from Miami FL USA
            
            [Reply](https://trumpexcel.com/hide-zero-values-excel/#comment-12373)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/hide-zero-values-excel/#respond)

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