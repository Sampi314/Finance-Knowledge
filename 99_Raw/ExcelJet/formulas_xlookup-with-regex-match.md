# XLOOKUP with regex match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-with-regex-match

---

[Skip to main content](https://exceljet.net/formulas/xlookup-with-regex-match#main-content)

[](https://exceljet.net/formulas/xlookup-with-regex-match#)

*   [Previous](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/xlookup-without-na-error)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP with regex match
========================

by Dave Bruns · Updated 4 Jan 2025

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8910/download?token=xYZChSFt)
 (18.3 KB)

![Excel formula: XLOOKUP with regex match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/xlookup_with_regex_match.png "Excel formula: XLOOKUP with regex match")

Summary
-------

To use a regex pattern in an XLOOKUP formula, you can enable "regex match" as the match mode and then provide a regex pattern in the lookup value. In the worksheet shown, the formula in F5 looks like this:

    =XLOOKUP("[A-Z]{3}"&F4&"[A-Z]{2}",B5:B16,C5:C16,,3)

This formula matches the number entered in cell F4 against the product codes in column B using a regex pattern. With the number 56 in cell F4, the result is $46.00, the correct price for product code PQR56DE.

> Regex support was added to XLOOKUP in December 2024, so this feature is only available in Excel 365 for now. For an overview of regex in Excel see see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> .

Generic formula
---------------

    =XLOOKUP(regex_pattern,lookup_array,return_array,,3)

Explanation 
------------

In this example, the goal is to look up the correct price of the product number entered in cell F4 using the product codes in column B. This problem is trickier than it looks. Each product code begins with 3 uppercase letters and ends with 2 or 3 uppercase letters. In the middle of the product code is a number between 2 and 4 digits. This is the number we want to use for a lookup value. Let's look at how to solve this problem with XLOOKUP and the newly released "regex match" feature. To provide some context on why you might need to use regex, let's start by looking at some XLOOKUP formulas that _don't work_. All formulas below refer to the worksheet shown above. Download the workbook above and follow along.

### Simple XLOOKUP formula

By default, XLOOKUP will perform an exact match. If we search for 56, XLOOKUP will simply return a #N/A error because 56 does not appear as a lookup value:

    =XLOOKUP("56",B5:B16,C5:C16) // returns #N/A

*   _lookup\_value_ - "56"
*   _lookup\_array_ - B5:B16 (the range containing the product codes)
*   _return\_array_ - C5:C16 (the range containing the prices)

Note that I've enclosed the "56" in double quotes because the product codes are text values, not numbers. But whether we look for the number 56 or the text "56", the result will be #N/A because XLOOKUP is performing an exact match, and those values do not exist by themselves as product codes.

### XLOOKUP with a wildcard match

If you know a little more about XLOOKUP, you might wonder if we can use a [wildcard](https://exceljet.net/glossary/wildcard)
 match. Indeed, you can enable a "wildcard character match" by providing the number 2 for _match\_mode_ argument like this:

    =XLOOKUP("56",B5:B16,C5:C16,,2) // enable wildcard match

The wildcard match doesn't do anything by itself without wildcards, so the formula above will also return #N/A. To actually use a wildcard match, we need to provide some wildcards. A typical approach involved adding some asterisks (\*) like this:

    =XLOOKUP("*56*",B5:B16,C5:C16,,2) // returns 78

*   _lookup\_value_ - "\*56\*"
*   _lookup\_array_ - B5:B16 (product codes)
*   _return\_array_ - C5:C16 (prices)
*   _if\_not\_found_ - omitted
*   _match\_mode_ - 2 (wildcard match)

The asterisks (\*) are wildcards that will match "zero or more characters". What we are doing here is looking for some number of characters, then "56," then some number of characters. This seems like it should work. However, the formula returns 78, which is not correct. Why? Well, if "56" only appeared once in the product codes, it _would_ work. However, "56" appears inside three product codes: KP563MN, QR56DE, and HJ3456TU. What's happening here is that XLOOKUP is matching the first product code that contains 56, KP563MN. Standard XLOOKUP behavior when there are multiple matches. Can we make XLOOKUP find the right code? Well, we could take the wildcard match idea a bit further by switching from "\*" to the "?" like this:

    =XLOOKUP("???56??",B5:B16,C5:C16,,2) // returns 46

The "?" wildcard means "one character of any kind". The literal meaning of this wildcard pattern is "3 characters, followed by 56, followed by 2 characters. In fact, the formula above _does return the correct price_ for PQR56DE, which is $46.00. However, there are some problems with this approach:

1.  Although PQR56DE has 2 letters ("DE") after the 56, _not all_ product codes follow this pattern. Some have two letters at the end, and some have three letters.
2.  We could have a product code like ABC5612XY, which will match the pattern above because the "?" will match any character, even numbers. The "?" wildcard makes no distinction between letters and digits.

In summary, with basic wildcards, we don't have a good way to create a pattern that will reliably match all product codes. It's time to roll out the big guns: Regular Expressions, called "regex" for short.

> What is regex? Regex, short for Regular Expressions, is a powerful tool for pattern matching in text data. Using a combination of metacharacters, literal characters, character classes, and quantifiers, you can define complex search patterns to extract, validate, or manipulate text data. Regular Expressions have been around for decades, but only recently arrived in Excel. The main benefit of regex in Excel is the ability to work with text very precisely without resorting to complicated formulas that are hard to create and maintain. If you are new to Regular Expressions, [see this overview](https://exceljet.net/articles/regular-expressions-in-excel)
> .

### XLOOKUP with a regex match

To enable a regex match in XLOOKUP, provide 3 for the fifth argument, called _match\_mode_. Going back to the original example above, once we enable regex, we have this formula:

    =XLOOKUP("56",B5:B16,C5:C16,,3) // regex enabled

Its interesting to note that this formula by itself returns $78.00. This is the price for KPX563MN, the first product code that contains "56". In other words, just by enabling regex, we get a working "contains" type match. This is cool because it means we can get XLOOKUP to do a "contains" type match by providing 3 for _match\_mode._ We don't need to use any wildcards or special symbols. However, the result above is _incorrect_ for the same reason we saw above: Three codes contain 56, and XLOOKUP matches the _first code that contains 56_.

> Actually, we don't even need to provide 56 as a text value like "56", because it will get evaluated as text _automatically_ inside in the regex engine. We'll get the same result if we use the _number_ 56 as the lookup value.

To get the formula working correctly, we need to beef up the regex pattern so that we aren't accidentally matching the wrong product code. The first step is to add a pattern to match the _beginning_ of the code. As noted above, the product codes always start with 3 uppercase characters. We can enforce this pattern in our lookup formula by adding "\[A-Z\]{3}" to the start:

    =XLOOKUP("[A-Z]{3}56",B5:B16,C5:C16,,3) // returns 78

The {3} is a _quantifier_ specifying 3 uppercase letters A-Z. This is already quite a bit more robust than our best wildcard formula above because XLOOKUP will now only match the 56 when it comes directly after 3 _uppercase letters_. Unfortunately, this formula also returns an incorrect result because KPX563MN is the first code to pass this test. To prevent this problem, we need to add a pattern to match the uppercase letters at the _end of the product code_. This is tricker. We know the code will end with uppercase letters, but there might be 2 characters, and there might be 3. This is where the power of regex patterns starts to really shine. To match 2-3 uppercase letters at the end, we can add "\[A-Z\]{2,3}" to the end of the pattern. The formula now looks like this:

    =XLOOKUP("[A-Z]{3}56[A-Z]{2,3}",B5:B16,C5:C16,,3) // returns 46

*   _lookup\_value_ - "\[A-Z\]{3}56\[A-Z\]{2,3}" (regex pattern)
*   _lookup\_array_ - B5:B16 (product codes)
*   _return\_array_ - C5:C16 (prices)
*   _if\_not\_found_ - omitted
*   _match\_mode_ - 3 (regex match)

The quantifier {2,3} means a minimum of 2 and a maximum of 3. The translation of the full pattern is "3 uppercase letters A-Z, followed by 56, followed by 2-3 uppercase letters A-Z". With this adjustment, the formula finally returns the correct result of 46. Better yet, we can use the same pattern to match any of these codes using only the number part as the lookup value. We now have a working solution, but of course, we don't want the number 56 hardcoded in the formula. The final step is to adjust the formula to get the lookup number from cell F4. We do this by [concatenating](https://exceljet.net/articles/how-to-concatenate-in-excel)
 a reference to F4 inside the regex pattern like this:

    =XLOOKUP("[A-Z]{3}"&F4&"[A-Z]{2,3}",B5:B16,C5:C16,,3)

This is the final working formula seen in the worksheet shown. When a user types a new valid number in cell F4, the formula will return a new result.

> To learn more about the symbols available for regex patterns, see the cheat sheet near the bottom of [this page](https://exceljet.net/articles/regular-expressions-in-excel)
> .

### Matching the entire cell

By default, regex will match any _substrings_ that match the pattern. For example, the pattern `cat` will match "cat", "catapult", "scatter", "concatenate", or "the top category" because "cat" appears as a substring in each text string. To match the text in a cell exactly, we need to use special anchors:

*   `^` (caret): Matches the start of the string. For example, `^abc` will match "abc123" but not "123abc".
*   `$` (dollar sign): Matches the end of the string. For example, `abc$` matches "123abc" but not "abc123".

To match the entire contents of a cell exactly, combine the `^` and the `$` in a pattern. For example, the pattern `^abc$` will match "abc" but not "123abc456" or "abcd". Moving back to the example above, if we want to restrict the pattern to match the entire contents of a cell, we can modify the formula like this:

    =XLOOKUP("^[A-Z]{3}"&F4&"[A-Z]{2,3}$",B5:B16,C5:C16,,3)

This new formula is more specific. It will continue to match a cell that contains "KPX563MN", but it will not match a cell that contains "KPX563MNXY" since the text ends with "MNXY" and the pattern only allows 3 or 3 uppercase letters a the end. The only change to this formula is the `^` at the start and the `$` at the end of the pattern.

Related formulas
----------------

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

[![Excel formula: XLOOKUP wildcard match example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20wildcard%20match%20example.png "Excel formula: XLOOKUP wildcard match example")](https://exceljet.net/formulas/xlookup-wildcard-match-example)

### [XLOOKUP wildcard match example](https://exceljet.net/formulas/xlookup-wildcard-match-example)

Working from the inside out, XLOOKUP is configured to find the value in H4 in the Last name column, and return all fields. In order to support wildcards , match\_mode is provided as 2: XLOOKUP(H4,D5:D15,B5:E15,2) // match Last, return all fields The lookup\_value comes from cell H4 The lookup\_array...

[![Excel formula: XLOOKUP wildcard contains substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_wildcard_contains_substring.png "Excel formula: XLOOKUP wildcard contains substring")](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)

### [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)

The goal is to look up the Title, Author, and Year in the list of books as shown using a formula based on a partial match and a wildcard. The text string to search for is entered in cell G4. All data is in an Excel Table named data in the range B5:D16. This problem can be easily solved with the...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    
*   [XLOOKUP wildcard match example](https://exceljet.net/formulas/xlookup-wildcard-match-example)
    
*   [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

### Articles

*   [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
    

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