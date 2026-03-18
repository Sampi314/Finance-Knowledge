# Validate strong password - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/validate-strong-password

---

[Skip to main content](https://exceljet.net/formulas/validate-strong-password#main-content)

[](https://exceljet.net/formulas/validate-strong-password#)

*   [Previous](https://exceljet.net/formulas/trim-text-to-n-words)
    
*   [Next](https://exceljet.net/formulas/annual-compound-interest-schedule)
    

[Text](https://exceljet.net/formulas#Text)

Validate strong password
========================

by Dave Bruns · Updated 6 Sep 2024

Related functions 
------------------

[REGEXTEST](https://exceljet.net/functions/regextest-function)

[COUNT](https://exceljet.net/functions/count-function)

[FIND](https://exceljet.net/functions/find-function)

[LEN](https://exceljet.net/functions/len-function)

[UPPER](https://exceljet.net/functions/upper-function)

[ISERROR](https://exceljet.net/functions/iserror-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8463/download?token=UPyNToAi)
 (19.98 KB)

![Excel formula: Validate strong password](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/validate_strong_password.png "Excel formula: Validate strong password")

Summary
-------

To test for strong passwords, you can use a formula based on the [REGEXTEST function](https://exceljet.net/functions/regextest-function)
. In the worksheet shown, the formula in cell D5, copied down, is:

    =REGEXTEST(B5,"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s])[^\s]{8,15}$")

On each row, the formula returns TRUE or FALSE. To return TRUE, the password must meet the following criteria: It must be at least eight characters long and no longer than 15 characters. It must contain at least one uppercase (A-Z) and one lowercase (a-z) letter. It must contain at least one number (0-9), and at least one punctuation character. Finally, it must not contain any whitespace characters (spaces, tabs, etc.).

_Note: REGEXTEST is only available in the Excel 365 Beta channel. The article below also provides a traditional formula that will work in older versions of Excel._

Generic formula
---------------

    ​=REGEXTEST(A1,"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s])[^\s]{8,15}$")

Explanation 
------------

In this example, the goal is to check for "strong" passwords. What makes a password strong depends on the rules it must follow. In this case, a strong password must meet the following six conditions:

1.  At least 8 and not more than 15 characters long
2.  Contains at least one uppercase (A-Z) letter
3.  Contains at least one lowercase (a-z) letter
4.  Contains at least one number (0-9)
5.  Contains at least one punctuation character
6.  Does not contain whitespace

Traditionally, this has been a difficult problem in Excel because there is no simple way to implement the logic. Each rule must be checked with a combination of functions, resulting in a large and unwieldy formula. However, with the introduction of the REGEXTEST function, this problem can be solved in a straightforward fashion by implementing all rules in a single regular expression, or "regex" for short.

> The rules above should be adjusted as needed. The point of this example is to show how to test a text string in various ways with a formula, _not_ to define what a strong password is.

### REGEXTEST function

Excel's REGEXTEST function tests for the existence of text defined by a given _pattern_. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. The result from REGEXTEST is TRUE or FALSE. For example, the formulas below show how REGEXTEST can be used to test the text in A1 for a number or an uppercase character:

    =REGEXTEST(A1,"[0-9]") // test for a number
    =REGEXTEST(A1,"[A-Z]") // test for an uppercase character

You can read more about REGEXTEST [here](https://exceljet.net/functions/regextest-function)
.

### Strong password validation

The problem in this example is to test various passwords to determine if they are strong. Specifically, we want to check that each password passes the following six rules:

1.  Is at least 8 and not more than 15 characters long
2.  Contains at least one uppercase (A-Z) letter
3.  Contains at least one lowercase (a-z) letter
4.  Contains at least one number (0-9)
5.  Contains at least one punctuation character
6.  Does not contain any whitespace characters

To validate these rules using the REGEXTEST function, we need to supply an appropriate regex pattern. In the worksheet shown, the formula used to perform this test looks like this:

    =REGEXTEST(B5,"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s])[^\s]{8,15}$")

The first argument, _text_, comes from cell B5. The second argument, _pattern_, is the regular expression used to validate a strong password that follows the rules above. The REGEXTEST function is simple, but you can see that the regex pattern is not :) Here is how the pattern breaks down:

*   ^: Start of string.
*   (?=.\*\[A-Z\]): At least one uppercase letter.
*   (?=.\*\[a-z\]): At least one lowercase letter.
*   (?=.\*\\d): At least one digit.
*   (?=.\*\[^\\w\\s\]): At least one special character (not a word character or space).
*   \[^\\s\]{8,15}: At least 8 to 15 characters, none of which are whitespace.
*   $: End of string.

​The key to this pattern is the "positive lookahead" syntax: (?=...), a special way to check that a pattern exists in a string without including it in a match.

### Lookahead syntax

As mentioned above, a "lookahead" in regex is a way to assert that a certain pattern exists in a string without "consuming characters" (i.e., without including them in the match). Lookaheads are useful when you want to check for specific conditions within a string without actually capturing those conditions in the match result. Regex provides both positive and negative lookahead:

*   Positive Lookahead: (?=...) - The pattern inside (...) must exist ahead.
*   Negative Lookahead: (?!...) - The pattern inside (...) must not exist ahead.

For example, to check for the presence of at least one uppercase letter (A-Z) somewhere ahead in a string, you can use

    (?=.*[A-Z])

This lookahead ensures the condition is true, but it does not text in the match. Lookaheads do not move the cursor forward in the string or consume characters. They just check if the required pattern is present. Because lookaheads do not consume characters, they can be combined to enforce classic AND-style logic. The pattern used above includes four positive lookaheads:

*   (?=.\*\[A-Z\]): Ensures at least one uppercase letter somewhere in the string.
*   (?=.\*\[a-z\]): Ensures at least one lowercase letter somewhere in the string.
*   (?=.\*\\d): Ensures at least one digit somewhere in the string.
*   (?=.\*\[^\\w\\s\]): at least one punctuation character somewhere in the string.

If any condition is false, the pattern will fail, and REGEXTEST will return FALSE. Finally, after these lookaheads, the pattern \[^\\s\]{8,15} checks for a string length between 8 and 15 characters. This pattern allows any character except whitespace. However, because the lookaheads have already been verified, we know the password contains uppercase, lowercase, numbers, and punctuation.

_Note: When you use multiple lookaheads, they check for conditions without moving the cursor or consuming characters. Each lookahead runs independently, and the regex engine evaluates them all before proceeding, so the order doesn't matter. However, when we check the length with \[^\\s\]{8,15}, this pattern does consume characters and needs to occur at the end of the pattern._

### Formula for older versions of Excel

Can you perform validation like this with a formula in an older version of Excel? Yes, but it's more work. One way to do it is to enter the letters a-z (lowercase) in a range somewhere, then [name the range](https://exceljet.net/articles/named-ranges)
 "letters". Then, you can use a brute-force formula like this:

    =AND(
      LEN(B5)>=8,
      LEN(B5)<=15,
      COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))>=1,
      COUNT(FIND(letters,B5))>=1,
      COUNT(FIND(UPPER(letters),B5))>=1,
      COUNT(FIND({"!","@","#","$","%","^","&","*","(",")","_","+"},B5))>=1,
      ISERROR(FIND(" ",B5))
    )

> _Note: this is an array formula and must be entered with control + shift + enter in Excel 2019 and older._

At a high level, we are using the [AND function](https://exceljet.net/functions/and-function)
 to run multiple tests to validate the password in cell B5. If all tests return TRUE, the AND function will return TRUE. Otherwise, AND will return false. In all, we run seven tests. First, we check that the length of the password is at least 8 characters with the [LEN function](https://exceljet.net/functions/len-function)
:

    LEN(B5)>=8

Next, we check that the length is less than or equal to 15 characters:

    LEN(B5)<=15

If both tests return TRUE, we know the password is between 8-15 characters. Next, we use the [FIND function](https://exceljet.net/functions/find-function)
 with the [COUNT function](https://exceljet.net/functions/find-function)
 to test for at least one number:

    COUNT(FIND({0,1,2,3,4,5,6,7,8,9},B5))>=1

FIND is configured to look for the numbers 1-9 inside the text in cell B5. When FIND locates a number, it returns its numeric position. When a number is not found, FIND returns a #VALUE error. The COUNT function then returns a count of numeric positions. If the count is greater than or equal to 1, the expression returns TRUE. Otherwise, it returns FALSE. For a more detailed explanation, [see this page](https://exceljet.net/formulas/cell-contains-number)
.

The test for a lowercase letter is performed in the same way, with COUNT and FIND:

    COUNT(FIND(letters,B5))>=1,

Because the named range "letters" contains all letters, a-z, you can think of it like this:

    COUNT(FIND({"a","b","c"..."x","y","z",B5))>=1,

Essentially, we are asking FIND to find all 26 letters in the range. Since FIND is case-sensitive, it will only match lowercase letters. As before, when FIND locates a match, it returns its numeric position. When a match is not found, FIND returns a #VALUE error. The COUNT function returns a count, which we check with >=1. The test for an uppercase letter works the same way. The only difference is that we use the UPPER function to uppercase all letters before FIND begins its search:

    COUNT(FIND(UPPER(letters),B5))>=1

The punctuation test is the same, but this time, we hardcode the characters we to look for into the formula as an array constant:

    COUNT(FIND({"!","@","#","$","%","^","&","*","(",")","_","+"},B5))>=1

You can customize this list as desired. Another option is to create a named range "punctuation" that contains all special characters and use that instead of the array constant. Finally, we test for whitespace with this snippet:

    ISERROR(FIND(" ",B5))

If FIND locates a space, it will return its position, otherwise it will return #VALUE!. We want to see the error at this point because it confirms no space characters in the password. [ISERROR](https://exceljet.net/functions/iserror-function)
 converts the error into TRUE. If FIND does locate a space, it returns a numeric position and ISERROR returns FALSE.

_Again, this is an array formula and must be entered with control + shift + enter in Excel 2019 and older. You can avoid this requirement if you harcode the 26 lower and 26 uppercase characters into the formula instead of using the named range "letters"._

Related formulas
----------------

[![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")](https://exceljet.net/formulas/cell-contains-number)

### [Cell contains number](https://exceljet.net/formulas/cell-contains-number)

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value is a...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Range contains one of many substrings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20substrings.png "Excel formula: Range contains one of many substrings")](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

### [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

All the hard work is done by the COUNTIF function, which is configured to count the values in the named range "substrings" that appear the named range "rng" with like this: COUNTIF(rng,"\*"&substrings&"\*")) By wrapping substrings in the asterisks, Excel evaluates the formula like this: =...

Related functions
-----------------

[![Excel REGEXTEST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regextest_function.png "Excel REGEXTEST function")](https://exceljet.net/functions/regextest-function)

### [REGEXTEST Function](https://exceljet.net/functions/regextest-function)

The Excel REGEXTEST function tests for the existence of text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable pattern. The result from REGEXTEST is TRUE or FALSE....

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel UPPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")](https://exceljet.net/functions/upper-function)

### [UPPER Function](https://exceljet.net/functions/upper-function)

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains number](https://exceljet.net/formulas/cell-contains-number)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    

### Functions

*   [REGEXTEST Function](https://exceljet.net/functions/regextest-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [UPPER Function](https://exceljet.net/functions/upper-function)
    
*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    

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