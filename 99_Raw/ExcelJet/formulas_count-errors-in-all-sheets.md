# Count errors in all sheets - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-errors-in-all-sheets

---

[Skip to main content](https://exceljet.net/formulas/count-errors-in-all-sheets#main-content)

[](https://exceljet.net/formulas/count-errors-in-all-sheets#)

*   [Previous](https://exceljet.net/formulas/volume-of-a-sphere)
    
*   [Next](https://exceljet.net/formulas/dynamic-workbook-reference)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Count errors in all sheets
==========================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[HYPERLINK](https://exceljet.net/functions/hyperlink-function)

[ISREF](https://exceljet.net/functions/isref-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8250/download?token=v2o6pX9N)
 (63.36 KB)

![Excel formula: Count errors in all sheets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_errors_in_all_sheets.png "Excel formula: Count errors in all sheets")

Summary
-------

To count errors by sheet a workbook you can use a formula based on the [ISERROR function](https://exceljet.net/functions/iserror-function)
, with help from [INDIRECT](https://exceljet.net/functions/indirect-function)
 and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
. In the worksheet shown, the formula in cell C5 is:

    =SUMPRODUCT(--(ISERROR(INDIRECT("'"&B5&"'!A1:F101"))))

As the formula is copied down, it returns a count of errors on each worksheet listed in column B. See below for options to generate a list of sheet names automatically.

Generic formula
---------------

    =SUMPRODUCT(--(ISERROR(INDIRECT("'"&A1&"'!range"))))

Explanation 
------------

In this example, the goal is to count errors in a workbook by sheet, where the sheet names have been previously entered in a column as shown. This is a tricky problem in Excel for a couple of reasons. First, there is no direct way to generate a list of sheets in a workbook with a formula. Second, once we have a list of sheet names, we need to run the text through the INDIRECT function to get a valid reference. Nevertheless, this is an interesting problem that provides a useful way to audit sheets in a workbook for errors. The article below explains the steps needed to create the report, and options for generating a list of sheet names.

> Note: INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
>  that can cause performance problems in large or complex workbooks. 

### Step 1: Create a new sheet to track errors

The first step is to create a new sheet where you can enter the formulas needed to count errors. Create a new sheet using the "Plus" icon at the right of the existing sheets, then name the sheet "Errors". I recommend you place this sheet at the end of the workbook. In the example above, the Errors sheet is the last. You'll then want to format a column to hold the sheet names and error counts as seen in the example. Next, we need to create a list of sheet names.

### Step 2: Create the list of sheet names

The next step is to create a list of sheet names. As mentioned above, there is no direct way to create a list of sheet names with a formula in Excel. The four main options are as follows:

1.  Enter the sheet names manually.
2.  Use a defined name + a formula (see below).
3.  Use Power Query (see below).
4.  Use VBA (not discussed in this article).

> Before you try options #2 or #3 above, I recommend you enter a few sheet names manually and try out the formula to count errors on each sheet. It's a good idea to make sure the solution will be useful to you before investing more time.

**Manual option**

In a basic workbook, is it easy to manually create a list of sheet names with copy and paste:

1.  Double-click a sheet to select the name
2.  Copy the name to the clipboard (Control + C)
3.  Paste the name into a cell on the Errors sheet.

Repeat this process for each sheet in the workbook you want to track. Note that the names you enter must match the sheet names exactly. If you rename or add a new sheet, you will need to update the list of sheet names to match. If you are working with a large workbook with many sheets, this process can become tedious, and you may want to try a more automated solution to list sheet names. Here are two options:

**Excel formula + defined name**

One option is to create a defined name that refers to an Excel 4.0 macro, and then refer to the name in a regular formula. This option works pretty well and has the advantage of automatically updating the list of sheet names when there are changes. One disadvantage of this approach is that you will need to save the file as a macro-enabled workbook (.xlsm) if you want the sheet names to remain dynamic. For step-by-step instructions for listing sheet names with a formula, [see this article](https://exceljet.net/formulas/list-sheet-names-with-formula)
.

**Power Query**

Another option to automatically generate sheet names in a workbook is to use Power Query. This is a more modern approach, and it works well, but the list of sheets won't automatically update when there are changes. Instead, you must right-click the list and click "Refresh". On the plus side, there is no need to save the file in a special format. See step-by-step [instructions here](https://exceljet.net/formulas/list-sheet-names-with-formula#power_query_option)
.

### Step 3: Enter a formula to count errors by sheet

Finally, we arrive at the point where we can count errors on each sheet. In the worksheet shown, the formula used to do this looks like this:

    =SUMPRODUCT(--(ISERROR(INDIRECT("'"&B5&"'!A1:F200"))))

_Note: we are hardcoding the range as A1:F200 which is big enough for the workbook in this example. You will need to adjust this range to suit your workbook. The range should be big enough to include the cells you care about on each sheet, but not so large as to cause performance problems in larger workbooks with many sheets. INDIRECT will trigger a recalculation with each change to the workbook!_

Working from the inside out, the first step is to create a valid reference to a range on a sheet. This is done with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
, which is designed to convert a text string into a valid reference. For example:

    =INDIRECT("A1") // returns a reference to A1
    =INDIRECT("C5") // returns a reference to C5
    =INDIRECT("Sheet1!A1:A10") // returns a reference to A1:A10 on Sheet1
    

The main thing to understand is each reference above begins as plain text. INDIRECT evaluates the text and converts it to a valid cell reference that can be used in a formula. In this example, INDIRECT is configured like this:

    INDIRECT("'"&B5&"'!A1:F200")

The sheet name ("January") comes from cell B5. Inside INDIRECT, we are [concatenating](https://exceljet.net/articles/how-to-concatenate-in-excel)
 separate values into a single text string that can be interpreted as a range on the given sheet. Note we are carefully adding single quotes (') around the sheet name. These are required when a sheet name contains space or punctuation. We also need to add an exclamation point (!) before the range. After the individual values are joined into a single text string, the result looks like this:

    INDIRECT("'January'!A1:F200")

INDIRECT then converts this text value into a valid reference and we now have a standard reference:

    =SUMPRODUCT(--(ISERROR('January'!A1:F200)))

The next step is to count errors. First, we run the [ISERROR function](https://exceljet.net/functions/iserror-function)
 on all cells in the range A1:F200 on the January sheet:

    ISERROR('January'!A1:F200)

ISERROR returns TRUE when a cell contains an error, and FALSE if not. Because there are 1200 cells in the range A1:F200, ISERROR returns an array that contains 1200 TRUE or FALSE results. Most of these values will be FALSE, since most cells in the range do not contain errors. Next, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) on the result from ISERROR:

    --(ISERROR('January'!A1:F200))

The only purpose of this operation is to convert the 1200 TRUE and FALSE values into 1s and 0s. After this step, the vast majority of the values will be zeros.

> This is why we don't want to use an unnecessarily large range - we are asking Excel to perform a lot of calculations for each sheet, and because INDIRECT is a volatile calculation, these calculations will occur _every time_ the worksheet is changed.

Finally, we are ready to add things up with the SUMPRODUCT function. SUMPRODUCT sums the values in the array (again, the majority of the values are zeros) and returns a total sum. This sum represents the count of errors on the sheet. As the formula is copied down, the same process is repeated for each sheet in the list.

_Note: in Excel 2021 and later, you can replace the SUMPRODUCT function with the SUM function in this formula without special handling. In older versions, SUM must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter. See [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
 for more info._

### Step 4: Add a link to each sheet (optional)

It is also possible to add a link to each worksheet with the [HYPERLINK function](https://exceljet.net/functions/hyperlink-function)
. The formula in cell D5, copied down, is:

    =HYPERLINK("#'"&B5&"'!B5","Link")

HYPERLINK takes two arguments: _link\_location_ and _friendly\_name_. Link\_location is the destination or path the link should follow, entered as a text value. _Friendly\_name_ is the anchor text that will be displayed with the link. One interesting feature of HYPERLINK is that it is programmed to evaluate text as a reference, so we don't need to use the INDIRECT in this formula. As before we are concatenating values together to assemble a reference to a particular sheet. the only difference is that we add a hash character (#) at the start, which is required by HYPERLINK when linking to a sheet. After concatenation, we have the following:

    =HYPERLINK("#'January'!B5","Link")

The result is a clickable link to cell B5 on the "January" sheet. As the formula is copied down, it returns a link to each sheet in the list. You can customize the destination cell and the anchor text as desired.

_Tip: On a sheet with errors, you can select all errors with [Go To](https://exceljet.net/shortcuts/display-go-to-dialog-box)
 (Control + G) > Formulas > Errors_

### Step 5: Trap errors (optional)

If a sheet name is not valid, INDIRECT will return a #REF error. Normally, we might see this error on the worksheet, but because we are nesting INDIRECT inside ISERROR, ISERROR will see the #REF error and return TRUE, causing the formula to return a count of 1. This is misleading because the error is not on the target sheet but instead a problem with the reference itself. One way to trap this error is to check the reference returned by INDIRECT first like this:

    =IF(ISREF(INDIRECT("'"&B5&"'!A1:F200")),SUMPRODUCT(--(ISERROR(INDIRECT("'"&B5&"'!A1:F200")))),"Invalid reference")

_Translation: If the reference returned by INDIRECT is valid, run the original formula. Otherwise, return "Invalid reference"._

The [ISREF function](https://exceljet.net/functions/isref-function)
 is used to test the reference returned by INDIRECT and the [IF function](https://exceljet.net/functions/if-function)
 is used to control the flow. In a newer version of Excel you can clean things up a bit by adding the [LET function](https://exceljet.net/functions/let-function)
 and running INDIRECT just once like this:

    =LET(
    ref,INDIRECT("'"&B5&"'!A1:F200"),
    IF(ISREF(ref),SUMPRODUCT(--ISERROR(ref)),"Invalid reference")
    )

Related formulas
----------------

[![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")](https://exceljet.net/formulas/list-sheet-names-with-formula)

### [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach: Define a name called "sheetnames" with an old macro command and the...

[![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

### [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel HYPERLINK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hyperlink%20function.png "Excel HYPERLINK function")](https://exceljet.net/functions/hyperlink-function)

### [HYPERLINK Function](https://exceljet.net/functions/hyperlink-function)

The Excel HYPERLINK function returns a hyperlink to a given destination. You can use HYPERLINK to create a clickable hyperlink with a formula. The HYPERLINK function can build links to workbook locations, pages on the internet, or files on network servers....

[![Excel ISREF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isref%20function.png "Excel ISREF function")](https://exceljet.net/functions/isref-function)

### [ISREF Function](https://exceljet.net/functions/isref-function)

The Excel ISREF returns TRUE when a cell contains a reference and FALSE if not. You can use the ISREF function to check for a reference in a formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)
    
*   [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [HYPERLINK Function](https://exceljet.net/functions/hyperlink-function)
    
*   [ISREF Function](https://exceljet.net/functions/isref-function)
    

### Articles

*   [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
    

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