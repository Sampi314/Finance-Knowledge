# Excel ISOMITTED function | Exceljet

**Source:** https://exceljet.net/functions/isomitted-function

---

[Skip to main content](https://exceljet.net/functions/isomitted-function#main-content)

[](https://exceljet.net/functions/isomitted-function#)

*   [Previous](https://exceljet.net/functions/image-function)
    
*   [Next](https://exceljet.net/functions/lambda-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

ISOMITTED Function
==================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

![Excel ISOMITTED function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_isomitted_function.png "Excel ISOMITTED function")

Summary
-------

The Excel ISOMITTED function is a helper function for LAMBDA functions to allow optional arguments. Inside a LAMBDA function, ISOMITTED will return TRUE when an argument has not been provided.

Purpose 
--------

Check for optional arguments in LAMBDAs

Return value 
-------------

TRUE or FALSE

Syntax
------

    =ISOMITTED(argument)

*   _argument_ - The argument to test for.

Using the ISOMITTED function 
-----------------------------

The Excel ISOMITTED function is a helper function for [LAMBDA functions](https://exceljet.net/functions/lambda-function)
 to allow optional [arguments](https://exceljet.net/glossary/function-argument)
. Inside a LAMBDA function, ISOMITTED will return TRUE when an argument has not been provided. ISOMITTED takes just one argument, _argument_, which should be the name of an argument defined in the parent LAMBDA function. 

### Step-by-step example

To illustrate how ISOMITTED works, imagine a simple LAMBDA formula that adds 10 any given value. With the value 100 in cell A1, this formula will return 110:

    =LAMBDA(a,a+10)(A1) // returns 110

Next, we alter the formula to make both a and _b_ variables:

    =LAMBDA(a,b,a+b)(A1,10) // returns 110
    =LAMBDA(a,b,a+b)(A1,20) // returns 120

With 100 in A1, if we supply 10 for b, the formula returns 110. If we supply 20 for b, the formula returns 120. So far so good.

Now let's say we want to make _b_ optional, and we want _b_ to _default_ to 10 if not provided. To accomplish this, we can use ISOMITTED to check for _b._ We perform this check inside the [IF function](https://exceljet.net/functions/if-function)
, then we run one calculation if _b_ is provided and a _another_ calculation if _b_ is _not_ provided:

    IF(ISOMITTED(b),a+10,a+b) // test for b

Finally, we place the snippet above into the LAMBDA function as before. We also enclose _b_ in square brackets \[b\] to follow the convention of optional arguments in Excel:

    =LAMBDA(a,[b],IF(ISOMITTED(b),a+10,a+b))(A1) // returns 110
    =LAMBDA(a,[b],IF(ISOMITTED(b),a+10,a+b))(A1,20) // returns 120
    

Now if we don't provide a value for _b_, the formula returns _a_ + 10. If we do provider a value for _b_, the formula returns _a_ + _b_.

_Note: the formulas above are using the special syntax for LAMBDA functions, where argument values are provided after the function in parentheses. [Read more about the LAMBDA function here](https://exceljet.net/functions/lambda-function)
._

### Worksheet Example

In the worksheet shown above, we are using the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to check password length. The LAMBDA takes two arguments, _a_ and _b_. _A_ is the password to check, and _b_ is the required length. _B_ is an optional argument and defaults to 8 when not provided. The formula in D5, copied down, is:

    =LAMBDA(a,[b],IF(ISOMITTED(b),LEN(a)>=8,LEN(a)>=b))(B5)

Since _b_ is _not_ supplied, the passwords in column B are checked for a minimum length of 8 characters. The formula returns TRUE if a password is at least 8 characters long and FALSE if not. To check for a minimum length of 10 characters, simply provide a value for _b_:

    =LAMBDA(a,[b],IF(ISOMITTED(b),LEN(a)>=8,LEN(a)>=b))(B5,10)

In this version, _b_ has been provided as 10. The formula returns TRUE if a password is at least 10 characters long and FALSE if not. The screen below shows how the formula works after we have created a named LAMBDA function called "PasswordCheck" with the formula above:

![ ISOMITTED example to check password length](https://exceljet.net/sites/default/files/images/functions/inline/ISOMITTED_example_to_check_password_length.png " ISOMITTED example to check password length")

The formula in D5 checks for a length of 8 characters by default. The formula in F5 checks for a length of 10 characters:

    =PasswordCheck(B5)
    =PasswordCheck(B5,10)

ISOMITTED function examples
---------------------------

[![Excel formula: Number to words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/number_to_words.png "Excel formula: Number to words")](https://exceljet.net/formulas/number-to-words)

### [Number to words](https://exceljet.net/formulas/number-to-words)

In this example, the goal is to build a custom function that will convert a number like 123 into "One hundred twenty three" or "One hundred twenty three dollars" when currency is specified as USD. In addition, the formula should support multiple currencies and handle decimals. Traditionally, "...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Number to words](https://exceljet.net/formulas/number-to-words)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

### Links

*   [Microsoft ISOMITTED function documentation](https://support.microsoft.com/en-us/office/isomitted-function-831d6fbc-0f07-40c4-9c5b-9c73fd1d60c1)
    

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