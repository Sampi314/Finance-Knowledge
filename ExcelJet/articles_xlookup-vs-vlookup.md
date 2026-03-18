# XLOOKUP vs VLOOKUP | Exceljet

**Source:** https://exceljet.net/articles/xlookup-vs-vlookup

---

[Skip to main content](https://exceljet.net/articles/xlookup-vs-vlookup#main-content)

[](https://exceljet.net/articles/xlookup-vs-vlookup#)

*   [Previous](https://exceljet.net/articles/xlookup-vs-index-and-match)
    
*   [Next](https://exceljet.net/articles/why-sumproduct)
    

XLOOKUP vs VLOOKUP
==================

by Dave Bruns · Updated 26 Sep 2024

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/7795/download?token=PNa7VbIa)
 (18.44 KB)

![XLOOKUP vs VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/xlookup-vs-vlookup_0.jpeg "XLOOKUP vs VLOOKUP")

Summary
-------

For many years, [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 has reigned supreme as the most widely used lookup function in Excel. But now that [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 is more widely available, VLOOKUP's reign will likely come to an end. XLOOKUP is a modern replacement for the VLOOKUP function and is more capable in almost every way. Let's look at how these two functions stack up against each other.

### Introduction

Excel offers a [vast number of functions](https://exceljet.net/functions)
 that cater to different users and their unique requirements. Among these functions, VLOOKUP has long been the go-to choice for basic lookups in a table or range. In almost every industry, millions and millions of existing spreadsheets use VLOOKUP to do something useful.

However, with the introduction of XLOOKUP in 2019, Excel users have a powerful new lookup option available. XLOOKUP can do everything VLOOKUP can do, and much more. Should you stop using VLOOKUP altogether? Should you even learn VLOOKUP if you are new to Excel? Let's have a look at the pros and cons of XLOOKUP and VLOOKUP.

### VLOOKUP: The Old Standard

VLOOKUP is an Excel function that has been widely used for many years. As the name implies, VLOOKUP is designed to work with _vertical data_. Given a lookup value, VLOOKUP searches the first column of a table and returns a corresponding value from the same row in another specified column. In short, VLOOKUP looks up data in a table like a human would, and does so with minimal configuration. The syntax for VLOOKUP looks like this:

    VLOOKUP(lookup_value,table_array,col_index_num,range_lookup)

The screen below shows an example of VLOOKUP configured to find an email address based on ID. The formula in cell H6 is:

    =VLOOKUP(G6,B6:E14,4,FALSE)

Notice that _table\_array_ is a reference to the _entire table_, and the column to return is hardcoded as 4. Also note that VLOOKUP will perform an approximate match by default, so _range\_lookup_ is set to FALSE to force an exact match.

![Basic VLOOKUP example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/VLOOKUP_configuration_example.png "Basic VLOOKUP example")

_For more VLOOKUP examples and videos [see this page](https://exceljet.net/functions/vlookup-function)
._

### VLOOKUP Pros

**Intuitive operation:** VLOOKUP scans through the first column in the table. When it finds a match, it moves across the table to the specified column number and retrieves the value in the same row. With a small number of inputs, VLOOKUP is easy and intuitive.

**Widely used:** There are millions upon millions of spreadsheets in the world that depend on VLOOKUP to do useful work. You will find VLOOKUP everywhere, and being comfortable with VLOOKUP is a real advantage, even if you prefer XLOOKUP.

**Simple configuration:** If you have a data table with lookup values in the first column, you have pretty much everything you need to use VLOOKUP. All VLOOKUP needs is a lookup value, the table address, and a column number.

### VLOOKUP Cons

While VLOOKUP is popular and easy to use, it does have some real limitations.

**Dangerous default:** VLOOKUP's default behavior is to return an _approximate match_, and the argument that controls this behavior (_range\_lookup_) _is not required_. This is dangerous because it makes it easy for a new user to configure VLOOKUP in a way that returns a normal-looking result that is, in fact, _wrong_. [See an example here](https://exceljet.net/articles/danger-beware-vlookup-defaults)
.

**Vertical data only:** VLOOKUP can only search _vertically_, which means you have to use another formula like [HLOOKUP](https://exceljet.net/functions/hlookup-function)
 or [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 to perform a lookup in data that is organized horizontally.

**Lookup values in the first column only:** The lookup table given to VLOOKUP must have lookup values in the first column. This means VLOOKUP can't return data located in a column to the _left_ of the lookup column, [without a complicated workaround](https://exceljet.net/formulas/left-lookup-with-vlookup)
.

**Hardcoded column reference:** Because the column index number is hardcoded inside VLOOKUP, it won't respond to changes in the worksheet, which can potentially break a VLOOKUP formula. However, to be fair, you _can_ [combine VLOOKUP with the MATCH function](https://exceljet.net/formulas/vlookup-two-way-lookup)
 to perform a dynamic 2-way lookup.

**Approximate match:** VLOOKUP can be configured for an approximate match by setting _range\_lookup_ to TRUE, or by omitting the argument altogether. In this mode, VLOOKUP will match a value exactly or _match the next smallest value._ However, to work correctly, _data must be sorted in ascending order_.

**No built-in error trapping:** VLOOKUP does not offer a way to provide an alternate value when a lookup is unsuccessful. This means VLOOKUP will simply return a #N/A error when a lookup fails. To trap and handle this error, you must use another function like IFERROR or IFNA. [See an example here](https://exceljet.net/formulas/vlookup-without-na-error)
.

**No reverse search:** VLOOKUP will always start at the beginning of a table and return the first match in a lookup operation. There is no simple way to get VLOOKUP to perform a reverse search.

**No easy way to apply multiple criteria**: Because VLOOKUP requires an entire lookup table as an input, it is not easy to apply multiple criteria. The most basic workaround is to [add a helper column with concatenated values](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
. A more advanced approach involves [creating a new lookup table](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
 on the fly.

### XLOOKUP - A Robust Alternative

[XLOOKUP](https://exceljet.net/functions/xlookup-function)
 is a modern replacement for the VLOOKUP function and was designed to address many of the limitations of VLOOKUP directly. It is a flexible and versatile function that can be used in a wide variety of situations. The syntax for the XLOOKUP function looks like this:

    XLOOKUP(lookup_value,lookup_array,return_array,[if_not_found],[match_mode],[search_mode])

The screen below shows how XLOOKUP would be configured to look up an email address based on ID. The formula in cell H6 is:

    =XLOOKUP(G6,B6:B14,E6:E14,"Not found")

Notice both _lookup\_array_ and _return\_array_ are provided as regular references and the optional _if\_not\_found_ argument is set to display "Not found" in case there are no results. Also note that XLOOKUP will perform an exact match by default, so there is no need to enable this behavior.

![Basic XLOOKUP example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/XLOOKUP_configuration_example.png "Basic XLOOKUP example")

_For more XLOOKUP examples and videos [see this page](https://exceljet.net/functions/xlookup-function)
._

### XLOOKUP Pros

**Sensible defaults:** Unlike VLOOKUP, XLOOKUP _defaults to an exact match_. This is a much safer default because a user must explicitly enable approximate match behavior when needed. VLOOKUP's approximate match default is dangerous because it can create incorrect (but normal-looking) results. [See an example here](https://exceljet.net/articles/danger-beware-vlookup-defaults)
.

**Two-way search:** Unlike VLOOKUP, XLOOKUP can search both _vertically_ and _horizontally_, which means there is no need to use other functions when data is not in a vertical orientation. [See an example here](https://exceljet.net/formulas/xlookup-horizontal-lookup)
.

**Reverse search:** XLOOKUP can search in a forward direction (first to last) or in reverse (last to first). This means XLOOKUP can easily solve complicated problems like retrieving the latest price from data in chronological order. [See an example here](https://exceljet.net/formulas/xmatch-reverse-search)
.

**Normal column reference:** XLOOKUP uses a normal cell reference for the _return\_array_. This means XLOOKUP is less fragile than VLOOKUP because ordinary changes to the table structure (i.e. inserting or deleting columns) will not break the formula.

**Approximate match:** XLOOKUP can be set for an approximate match in two ways: (1) exact match or the _next smaller_ value (2) exact match or the _next larger_ value. In both cases, data _does not_ need to be sorted. See a [basic example here](https://exceljet.net/formulas/xlookup-basic-approximate-match)
. See a more advanced [closest-match example here](https://exceljet.net/formulas/find-closest-match)
.

**Built-in error handling:** XLOOKUP offers a dedicated argument, _if\_not\_found_, to provide a custom value, a message, or even another formula to run if XLOOKUP does not find a match. There is no need to use another function like [IFERROR](https://exceljet.net/functions/iferror-function)
. [See an example here](https://exceljet.net/formulas/xlookup-without-na-error)
.

**Easy to apply multiple criteria**: The structure of XLOOKUP makes it straightforward to apply multiple criteria. The trick is to create a _lookup\_array_ with [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
, then set the _lookup\_value_ to 1 ([basic example](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
, [advanced example](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
).

### XLOOKUP cons

**Limited availability:** XLOOKUP is only available in the latest versions of Excel. This means XLOOKUP will not work if a worksheet is opened in an older version of Excel. Before you use XLOOKUP, you must consider who will need to use a worksheet and what version of Excel they use.

**Learning curve:** XLOOKUP is more complex to configure than VLOOKUP and takes some time to get the hang of. This is mostly because XLOOKUP provides many more features than VLOOKUP.

**Two-way lookups are more complex:** Compared to VLOOKUP and INDEX and MATCH, a two-way lookup (i.e. looking up both a row and column in the same formula) with XLOOKUP is more complicated. This is because XLOOKUP does not use a numeric index to retrieve data, so you can't just add the MATCH function like we can with VLOOKUP. [See an example here](https://exceljet.net/formulas/xlookup-two-way-exact-match)
.

### Feature comparison

The table below summarizes the key differences mentioned above.

| Feature | VLOOKUP | XLOOKUP |
| --- | --- | --- |
| Availability | All versions | Excel 2021+ |
| Simple configuration | Yes | More options |
| Dangerous defaults | Yes | No  |
| Approximate matching | Yes, with sorted data | Yes, data can be unsorted |
| Horizontal lookup | No  | Yes |
| Left lookup | No  | Yes |
| Numeric column reference | Yes | No  |
| Built-in error handling | No  | Yes |
| Reverse search | No  | Yes |
| Multiple criteria | Complicated | Easier |
| Two-way lookup | Yes with MATCH | Yes with XLOOKUP + XLOOKUP |

### Summary

While VLOOKUP has been widely used in Excel for many decades, it has real limitations. The XLOOKUP function has been designed to address these limitations head-on. In almost every respect, XLOOKUP is a better and more powerful lookup function. That said, there are millions of spreadsheets in the world that use VLOOKUP successfully to solve many ordinary lookup problems. There is no burning need to replace existing VLOOKUP solutions with XLOOKUP unless the existing configuration is unnecessarily complex. In other words, VLOOKUP is not broken; it is simply limited. In addition, before you replace VLOOKUP with XLOOKUP, you need to consider the Excel version used by others who will use the worksheet. XLOOKUP is only available in Excel 2021 and later.

With the above in mind, I recommend that you start using XLOOKUP for your lookup problems. XLOOKUP takes a little more practice because it has more features and options. However, even if you use XLOOKUP almost exclusively for your own work, you will likely continue to run into existing VLOOKUP solutions for many years to come. If you work in Excel frequently, it is worth your time to be proficient with both VLOOKUP and XLOOKUP. 

### Learning Resources

*   [VLOOKUP examples](https://exceljet.net/functions/vlookup-function)
    
*   [VLOOKUP video training](https://exceljet.net/training/core-formula)
     
*   [XLOOKUP examples](https://exceljet.net/functions/xlookup-function)
    
*   [XLOOKUP video training](https://exceljet.net/training/dynamic-array-formulas)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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