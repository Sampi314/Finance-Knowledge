# Split full name into parts - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-full-name-into-parts

---

[Skip to main content](https://exceljet.net/formulas/split-full-name-into-parts#main-content)

[](https://exceljet.net/formulas/split-full-name-into-parts#)

*   [Previous](https://exceljet.net/formulas/put-names-into-proper-case)
    
*   [Next](https://exceljet.net/formulas/calculate-percent-variance)
    

[Names](https://exceljet.net/formulas#Names)

Split full name into parts
==========================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[LET](https://exceljet.net/functions/let-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[INDEX](https://exceljet.net/functions/index-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[DROP](https://exceljet.net/functions/drop-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8099/download?token=bvYQuld7)
 (17.9 KB)

![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")

Summary
-------

To split full names in the form "First, Middle, Last" into separate columns with a single formula, you can use a formula based on the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
. In the worksheet shown, the formula in cell D5 is:

    =LET(
      parts,TEXTSPLIT(B5," "),
      count,COUNTA(parts),
      first,INDEX(parts,1),
      last,INDEX(parts,count),
      IFS(
        count=1,HSTACK(first,"",""),
        count=2,HSTACK(first,"",last),
        count>2,HSTACK(first,TEXTJOIN(" ",1,DROP(DROP(parts,,1),,-1)),last)
       )
    )

As the formula is copied down, it returns the first, middle, and last names into separate columns. Note that empty middle names are ignored, and cases where there are two middle names are handled properly.

> _Note: this formula requires functions that are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
> ._

Explanation 
------------

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names.

### The challenge

The main challenge is that a middle name is not always present and in some cases, there is more than one middle name. As a result, when TEXTSPLIT (or Excel's older [Text to Columns](https://exceljet.net/glossary/text-to-columns)
 feature) is used to split the names, the various parts of each name do not always fall into the right column, as you can see in the worksheet below:

![The TEXTSPLIT function by itself](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/split_full_name_into_parts_textsplit_by_itself.png "The TEXTSPLIT function by itself")

The output is only correct when a name has exactly three parts.

### Separate formulas

One way to approach this challenge is to parse each part of the name in three separate formulas:

*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Get middle name from name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    

See the links above for details. However, it is also possible to create an all-in-one formula to parse each name in one step with the LET function. This is the approach explained below. 

### All-in-one formula

The solution below shows how the [LET function](https://exceljet.net/functions/let-function)
 can help organize what would otherwise be a complex formula. The formula in cell D5, copied down, looks like this:

    =LET(
      parts,TEXTSPLIT(B5," "),
      count,COUNTA(parts),
      first,INDEX(parts,1),
      last,INDEX(parts,count),
      IFS(
        count=1,HSTACK(first,"",""),
        count=2,HSTACK(first,"",last),
        count>2,HSTACK(first,TEXTJOIN(" ",1,DROP(DROP(parts,,1),,-1)),last)
       )
    )

> Note: you can toggle the formula bar open/closed with the [keyboard shortcut](https://exceljet.net/shortcuts)
>  Control + Shift + U

At the top level, the LET function is used to define four variables: **parts**, **count**, **first**, and **last**. The variable **parts** is assigned a value by the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
:

    =TEXTSPLIT(B5, " ") // split name into separate parts

The delimiter given to TEXTSPLIT is a single space (" "), so the result is an array that contains all parts (i.e. words) that appear in the full name. Next, the [COUNTA function](https://exceljet.net/functions/counta-function)
 is used to assign a value to **count**:

    =COUNTA(parts) // count parts

Next, we use the [INDEX function](https://exceljet.net/functions/index-function)
 to assign values to **first** and **last**. To get a value for **first**, we ask for the _first_ value in **parts**. To get a value for **last**, we ask for the _last_ value in parts, by using the **count**. The code looks like this:

    INDEX(parts,1) // first
    INDEX(parts,count) // last

_Note: the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 would also work instead of INDEX, but INDEX is simple and brief, so we use it here._

At this point, we have what we need to create the final output for each name. What we want in the end is an array that contains three values for each name: first, middle, and last. This requires some conditional logic, which we implement with the [IFS function](https://exceljet.net/functions/ifs-function)
:

    IFS(
      count=1,HSTACK(first,"",""),
      count=2,HSTACK(first,"",last),
      count>2,HSTACK(first,TEXTJOIN(" ",1,DROP(DROP(parts,,1),,-1)),last)
    )

If the count is 1, we use the [HSTACK function](https://exceljet.net/functions/hstack-function)
 to assemble a horizontal [array](https://exceljet.net/glossary/array)
 that contains only the first name (**first**):

    HSTACK(first,"","")

This allows the formula to handle a case where there is only a single name (e.g. Bono, Prince, Madonna, Adele, Beyoncé, etc.). Note that we provide an empty string ("") for the middle name and the last name so that we are always returning an array with three items on each row.

Next, if the count is 2, we use HSTACK to return the first name and the last name, and provide an empty string for the middle name:

    HSTACK(first,"",last)

Finally, if the count is greater than 2, we use HSTACK again like this:

    HSTACK(first,TEXTJOIN(" ",1,DROP(DROP(parts,,1),,-1)),last)

This is the trickiest part of this formula. Note that we supply the first name and the last name in a normal fashion. For the middle name, however, we use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 and the [DROP function](https://exceljet.net/functions/drop-function)
 like this:

    TEXTJOIN(" ",1,DROP(DROP(parts,,1),,-1))

Our goal here is to keep all middle names together and return just a single value. We don't want to output additional cells for names that have more than one middle name. We start by using the DROP function twice:

    DROP(DROP(parts,,1),,-1)

The inner drop function removes the first name from **parts** (i.e. the first value in the **parts** array). The outer DROP function removes the last name from **parts**. The TEXTJOIN function then [concatenates](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the remaining values in **parts**, each value separated by a single space. The result is returned to HSTACK as the middle name. The practical effect of this fancy code is that the formula can handle any number of middle names: all names that appear between the first name and the last name are simply joined together.

_Note: the approach in this formula works fine for the data as shown, but you might need to adjust the logic in the formula to suit your data._

### Conclusion

Splitting full names into separate parts (first, last, and middle) is challenging because names have a variable number of parts. You can use the TEXTSPLIT function to easily split names into separate parts, but the names might not land in the correct column. The same problem occurs if you use Excel's Text-To-Columns feature. One way to solve this problem is to create a formula that handles each name differently depending on how many parts it contains. The LET function is ideal for this purpose because it can be used to define variables that are then processed with conditional logic in a single formula.

Related formulas
----------------

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

Related functions
-----------------

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    

### Functions

*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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