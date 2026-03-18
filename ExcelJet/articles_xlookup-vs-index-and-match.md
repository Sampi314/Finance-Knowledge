# XLOOKUP vs INDEX and MATCH | Exceljet

**Source:** https://exceljet.net/articles/xlookup-vs-index-and-match

---

[Skip to main content](https://exceljet.net/articles/xlookup-vs-index-and-match#main-content)

[](https://exceljet.net/articles/xlookup-vs-index-and-match#)

*   [Previous](https://exceljet.net/new-excel-functions)
    
*   [Next](https://exceljet.net/articles/xlookup-vs-vlookup)
    

XLOOKUP vs INDEX and MATCH
==========================

by Dave Bruns · Updated 5 Jul 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/7813/download?token=_ODiJXOb)
 (18.43 KB)

![XLOOKUP vs INDEX and MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/XLOOKUP_vs_INDEX_and_MATCH_0.jpeg "XLOOKUP vs INDEX and MATCH")

Summary
-------

For many years, [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 have been the go-to solution for difficult lookup problems in Excel. While more complicated to configure, the two-function combination of INDEX + MATCH is _flexible and powerful_. But now that [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 is more widely available, will INDEX and MATCH remain popular? Is there any reason to still use INDEX and MATCH? Read below for a detailed comparison.

> [See INDEX and MATCH Two-Column Lookup Example](https://exceljet.net/formulas/index-and-match-two-column-lookup)

### Introduction

For decades, [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 have been the go-to solution for handling complex lookup problems. Unlike [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, INDEX and MATCH are based on numeric positions: the [MATCH function](https://exceljet.net/functions/xmatch-function)
 locates the position of a value, and the [INDEX function](https://exceljet.net/functions/index-function)
 retrieves a value at that position. This approach makes INDEX and MATCH highly versatile, at the cost of more configuration.

However, with the introduction of [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 in 2019, Excel users have a powerful new lookup option available. XLOOKUP can do everything VLOOKUP can do, and much more (for a detailed comparison, [see this article](https://exceljet.net/articles/xlookup-vs-vlookup)
). But what about INDEX and MATCH? Can XLOOKUP do everything that INDEX and MATCH can do? Let's take a look at how these two options stack up against each other.

### INDEX AND MATCH: The Classic

The combination of INDEX and MATCH is a classic method for performing lookups in Excel. While it requires two separate functions, it provides a highly flexible and customizable solution for a wide range of lookup problems. The syntax for INDEX and MATCH looks like this:

    INDEX(return_array,MATCH(lookup_value,lookup_array,[match_type]))

In a nutshell, the MATCH function is used to locate the numeric position of a match in a set of data, and the INDEX function is used to retrieve a value at that position. The screen below shows an example of INDEX and MATCH configured to find an email address based on ID. The formula in cell H6 is:

    =INDEX(E6:E14,MATCH(G6,B6:B14,0))

Inside the MATCH function, the _lookup\_array_ is B6:B14, which contains IDs, and _match\_type_ is set to 0 to force an exact match. Inside the INDEX function, the (return) _array_ is given as E6:E14, which contains email addresses. MATCH returns the numeric position of ID 869 (7) to the INDEX function, and INDEX returns the value at that position as a final result.

![INDEX and MATCH exact match example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/INDEX_and_MATCH_exact_match_example.png "INDEX and MATCH exact match example")

For a full explanation of INDEX and MATCH step-by-step, see: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### MATCH vs XMATCH

Before we jump in and start comparing XLOOKUP to INDEX and MATCH, we need to talk about the [XMATCH function](https://exceljet.net/functions/xmatch-function)
. XMATCH is an upgraded replacement for the MATCH function, released at the same time as XLOOKUP. Like the MATCH function, XMATCH performs a lookup and returns a numeric position. Also like MATCH, XMATCH can perform lookups in vertical or horizontal ranges, supports approximate and exact matches, and allows wildcards (\* ?) for partial matches.

There are 5 key differences between XMATCH and MATCH:

1.  XMATCH _defaults to an exact match_, while MATCH defaults to an _approximate match_.
2.  XMATCH can find the next larger item _or_ the next smaller item.
3.  XMATCH can perform a reverse search (i.e. search from last to first).
4.  XMATCH does not require values to be sorted when performing an approximate match.
5.  XMATCH can perform a binary search, which is specifically optimized for speed.

In summary, XMATCH works like MATCH, but it is more flexible and powerful.

XMATCH was released at the same time as XLOOKUP. If you have XLOOKUP, you also have XMATCH. As a result, it doesn't make sense to compare XLOOKUP to INDEX and MATCH without including XMATCH. For the purpose of this article, you can assume that "INDEX and MATCH" can also mean "INDEX and XMATCH" as dictated by requirements.

### INDEX and MATCH Pros

**Compatibility:** The basic INDEX and MATCH combination will work in all versions of Excel and has long been a preferred option for difficult lookup problems. There are millions and millions of spreadsheets in the world that use this approach.

**Flexibility**: The combination of INDEX and MATCH is supremely flexible and can solve pretty much any lookup problem in Excel: lookups in vertical or horizontal ranges, approximate and exact match lookups, lookups with wildcards, and more.

**Numeric index:** MATCH returns a numeric position, and INDEX returns a value at that position. Because MATCH returns a numeric index, this value can be easily manipulated. For example, some advanced INDEX and MATCH formulas make simple on-the-fly adjustments to row or column index values based on other information in a worksheet ([example 1](https://exceljet.net/formulas/index-and-match-with-variable-columns)
, [example 2](https://exceljet.net/formulas/index-and-match-two-column-lookup)
, [example 3](https://exceljet.net/formulas/step-based-lookup-example)
).

**Vertical or horizontal:** INDEX and MATCH work equally well with vertical or horizontal ranges.

**Entire rows and columns**: INDEX can [return entire rows](https://exceljet.net/formulas/look-up-entire-row)
 by setting the column number to zero, and [entire columns](https://exceljet.net/formulas/look-up-entire-column)
 by setting the row number to zero.

**Two-way lookups**: INDEX and MATCH are well suited for two-way lookups (also called "matrix lookups" or "2D lookups") that target _both rows and columns_ because INDEX is designed to accept separate row and column numbers ([see example here](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
).

**Troubleshooting**: The two-step process used by INDEX and MATCH is a bit easier to troubleshoot because the operation is more transparent. You can test the result from MATCH ([with F9](https://exceljet.net/shortcuts/evaluate-part-of-a-formula)
) to see if you have a valid position. Alternatively, you can hardcode a row or column number into INDEX to simulate a result from MATCH.

**Multiple criteria**: The behavior of INDEX and MATCH makes it relatively straightforward to apply multiple criteria. The standard approach is to create a _lookup\_array_ with [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
, then set the _lookup\_value_ in MATCH to 1 ([See example](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
).

**Reverse search:** INDEX + XMATCH can easily perform a reverse search (last to first) because this feature is built into XMATCH.

**Binary search:** INDEX + XMATCH can be configured for a binary search (speed optimized) because this feature is built into XMATCH.

**Match flexibility:** INDEX + XMATCH can match the next smaller or the next larger value in unsorted data because this feature is provided by XMATCH.

### INDEX and MATCH Cons

While the INDEX and MATCH combo has many pros, it also has some cons.

**Dangerous default:** The default behavior for INDEX + MATCH is to return an _approximate match_, and the input that controls this behavior, _match\_type_, is _not_ required. This makes it easy to configure INDEX and MATCH in a way that returns a normal-looking, but incorrect, result. This is _not_ a problem with INDEX + XMATCH, since XMATCH returns an _exact match_ by default.

**Complexity:** The two-function structure of INDEX and MATCH can be more challenging to learn and apply because it uses a concept called [nesting](https://exceljet.net/glossary/nesting)
, in which an "inner" function (MATCH) returns a value directly to an "outer" function (INDEX).

**MATCH confusion:** While XMATCH allows INDEX and MATCH to compete directly with XLOOKUP on features, the choice of XMATCH over MATCH may cause confusion among users who are not clear on the differences. In addition, using XMATCH creates a dependency, since XMATCH will only work in a recent version of Excel.

**No built-in error handling**: Unlike XLOOKUP, the INDEX and MATCH combination does not have a built-in error-handling feature, so the formula will simply return #N/A when a lookup fails. To provide a more friendly or helpful message, another function like IFERROR or IFNA needs to be included (example).

### XLOOKUP - A Modern Alternative

[XLOOKUP](https://exceljet.net/functions/xlookup-function)
 is a modern replacement for the VLOOKUP function and was designed to address many of the limitations of VLOOKUP directly. It is a flexible and versatile function that can be used in a wide variety of situations. The syntax for XLOOKUP looks like this:

    XLOOKUP(lookup_value,lookup_array,return_array,[if_not_found],[match_mode],[search_mode])

The screen below shows how XLOOKUP would be configured to look up an email address based on ID. The formula in cell H6 is:

    =XLOOKUP(G6,B6:B14,E6:E14,"Not found")

Notice both _lookup\_array_ and _return\_array_ are provided as separate references, and the optional _if\_not\_found_ argument is set to display "Not found" in case there are no results. Also, note that XLOOKUP will perform an exact match by default, so there is no need to enable this behavior.

![XLOOKUP exact match example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/XLOOKUP_exact_match_example.png "XLOOKUP exact match example")

_For more XLOOKUP examples and videos,_ [_see this page_](https://exceljet.net/functions/xlookup-function)
_._

### XLOOKUP Pros

**Simplicity:** XLOOKUP is easier to configure than INDEX and MATCH because there is just one function to work with, and only three required arguments: _lookup\_value_, _lookup\_array_, and _return\_array_.

**Safe defaults:** unlike INDEX + MATCH, XLOOKUP _defaults to an exact match_. This is a much safer default because a user must explicitly enable approximate match behavior when needed. Note that INDEX + XMATCH _will_ default to an exact match because this is the default behavior for XMATCH.

**Vertical or horizontal:** Like INDEX and MATCH, XLOOKUP can use a vertical or horizontal lookup array.

**Entire rows and columns**: XLOOKUP can easily return [entire rows](https://exceljet.net/formulas/look-up-entire-row)
 or [entire columns](https://exceljet.net/formulas/look-up-entire-column)
.

**Reverse search:** XLOOKUP can search in a forward direction (first to last) or in reverse (last to first). This makes XLOOKUP useful for solving complicated problems like retrieving the latest price from data in chronological order. [See an example here](https://exceljet.net/formulas/xmatch-reverse-search)
. 

**Match flexibility:** XLOOKUP can be configured for an approximate match in two ways: (1) exact match or the _next smaller_ value (2) exact match or the _next larger_ value. In both cases, _data does not need to be sorted_. INDEX + XMATCH has the same capability, but INDEX + MATCH is limited to approximate matches in _sorted data only_. 

**Built-in error handling:** XLOOKUP offers a dedicated argument, _if\_not\_found_, to provide a custom value, a message, or even another formula to run if XLOOKUP does not find a match. [See an example here](https://exceljet.net/formulas/xlookup-without-na-error)
. With INDEX and MATCH, you must add another function like IFERROR or IFNA to handle errors.

**Multiple criteria**: The structure of XLOOKUP makes it relatively straightforward to apply multiple criteria. The standard approach is to create a _lookup\_array_ with [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
, then set the _lookup\_value_ to 1 ([basic example](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
, [advanced example](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
).

### XLOOKUP cons

**Limited availability:** XLOOKUP is only available in the latest versions of Excel. This means XLOOKUP will not work if a worksheet is opened in an older version of Excel. Before you use XLOOKUP, you must consider who will need to use a worksheet and what version of Excel they use.

**Two-way lookups are more complex:** Compared to INDEX and MATCH, a two-way lookup (i.e. looking up both a row and column in the same formula) with XLOOKUP is more complicated. This is because XLOOKUP does not use a numeric index to retrieve data, so you can't use the MATCH function like you can with INDEX and MATCH. [See an example here](https://exceljet.net/formulas/xlookup-two-way-exact-match)
.

### Feature comparison

The table below summarizes the key differences mentioned above.

| Feature | INDEX and MATCH | XLOOKUP |
| --- | --- | --- |
| Availability | All versions | Excel 2021+ |
| Learning curve | Moderate | Easier |
| Dangerous defaults | Yes/No\* | No  |
| Approximate match unsorted data | Yes\* | Yes |
| Horizontal lookup | Yes | Yes |
| Return entire rows or columns | Yes | Yes |
| Left lookup | Yes | Yes |
| Numeric indexing | Yes | No  |
| Built-in error handling | No  | Yes |
| Reverse search | Yes\* | Yes |
| Binary search | Yes\* | Yes |
| Two-way lookup | Yes | Yes with XLOOKUP + XLOOKUP |
| Multiple criteria | Yes with Boolean Logic | Yes with Boolean Logic |

\* Requires XMATCH, available in Excel 2021+.

### Summary

XLOOKUP and INDEX + MATCH are both flexible and powerful lookup solutions in Excel. For difficult lookup problems that require backward compatibility with older versions of Excel, INDEX + MATCH is the clear winner, since XLOOKUP is only available in Excel 2021 and later. If backward compatibility is not needed, XLOOKUP is better than regular INDEX and MATCH in several ways: XLOOKUP is simpler, has safe defaults, has built-in error handling, and is very flexible.

However, when we compare XLOOKUP to INDEX + XMATCH, the contest is much closer. Both options can run lookups on horizontal or vertical ranges, handle reverse lookups, use fast binary searches, and use approximate matching on unsorted data. XLOOKUP has an edge with built-in error handling and a friendly learning curve. But the numeric index used by INDEX + XMATCH is easier to test and troubleshoot because the two-step process is more transparent. In addition, many users will likely find an INDEX and MATCH formula more intuitive for two-way lookups.

With the above in mind, here are a few general recommendations and thoughts:

*   For new projects that don't require backward compatibility with older versions of Excel, XLOOKUP should be your default choice. It is a modern and powerful function that can handle almost any lookup problem.
*   INDEX + XMATCH is very close to XLOOKUP in terms of features and flexibility, and is arguably easier to use for two-way lookup problems. It also offers subtle benefits in [certain kinds of advanced lookups](https://exceljet.net/formulas/index-and-match-with-variable-columns)
    .
*   If backward compatibility is required, INDEX + MATCH is the most flexible and powerful lookup option available. However, for simple lookup problems, VLOOKUP will work just fine.
*   If you work in Excel frequently, it is worth your time to understand both XLOOKUP and INDEX and MATCH, since you will likely run into existing INDEX and MATCH formulas in older worksheets for many years to come.

### Learning Resources

*   [INDEX and MATCH overview](https://exceljet.net/articles/index-and-match)
    
*   [INDEX and MATCH training](https://exceljet.net/training/core-formula)
     
*   [XLOOKUP examples](https://exceljet.net/functions/xlookup-function)
    
*   [XLOOKUP training](https://exceljet.net/training/dynamic-array-formulas)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    

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