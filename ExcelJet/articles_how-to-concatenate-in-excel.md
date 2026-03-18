# How to concatenate in Excel | Exceljet

**Source:** https://exceljet.net/articles/how-to-concatenate-in-excel

---

[Skip to main content](https://exceljet.net/articles/how-to-concatenate-in-excel#main-content)

[](https://exceljet.net/articles/how-to-concatenate-in-excel#)

*   [Previous](https://exceljet.net/articles/why-sumproduct)
    
*   [Next](https://exceljet.net/articles/what-is-an-array-formula)
    

How to concatenate in Excel
===========================

by Dave Bruns · Updated 1 Nov 2023

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/7274/download?token=vzzcwFtp)
 (26.93 KB)

![How to concatenate in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/How_to_concatenate_in_Excel.jpg)

Summary
-------

This article explains how to concatenate manually with the ampersand operator (&) and with the three Excel functions designed for concatenation: CONCATENATE, CONCAT, and TEXTJOIN.

One of the most important operations in Excel formulas is concatenation. In Excel formulas, concatenation is the process of joining one value to another to form a [text string](https://exceljet.net/glossary/text-value)
. The values being joined can be hardcoded text, cell references, or results from other formulas.

There are two primary ways to concatenate in Excel:

1.  Manually with the [ampersand operator (&)](https://exceljet.net/glossary/math-operators)
    
2.  Automatically with a function like [CONCAT](https://exceljet.net/functions/concat-function)
     or [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
    

In the article below, I'll focus first on manual concatenation with the ampersand operator (&), since this should be your go-to solution for basic concatenation problems. Then I'll introduce the three Excel functions dedicated to concatenation: CONCATENATE, CONCAT, and TEXTJOIN. These functions can make sense when you need to concatenate many values at the same time. As with so many things in Excel, the most important thing is to understand the basics first. 

### What is concatenation?

Concatenation is the operation of joining values together to form text. For example, to join "A" and "B" together with concatenation, you can use a formula like this:

    ="A"&"B" // returns "AB"
    

The ampersand (&) is Excel's concatenation [operator](https://exceljet.net/glossary/math-operators)
. Unless you are using one of Excel's concatenation functions, you will always see the ampersand in a formula that performs concatenation. It's important to understand that the result from concatenation is always text, even when concatenation involves numbers. For example:

    ="A"&100 // returns "A100"
    =100&200 // returns "100200"
    

Both of the formulas above return text values, even though some of the values being joined are numeric. In fact, you can transform a number to text by concatenating an [empty string](https://exceljet.net/glossary/empty-string)
 ("") to the number like this:

    =100&"" // returns "100"
    

You will sometimes see this technique in a [lookup formula that involves numbers and text](https://exceljet.net/formulas/vlookup-with-numbers-and-text)
. Notice in all examples above, text values appear in double quotes (""), while numeric values are not quoted. For example, while 100 is a numeric value, "100" is a text value.

### Basic concatenation formula

To explain how concatenation works in a formula in a worksheet, let's start with a simple example that shows how to concatenate a text string to a value in a cell. With the value 10 in cell B5, this formula will return "Cell B5 contains 10":

![Basic concatenation example in an Excel formula](https://exceljet.net/sites/default/files/images/articles/inline/Basic%20concatenation%20example.png "Basic concatenation example in an Excel formula")

    ="Cell B5 contains "&B5
    

There are three things to note in the formula above:

1.  The text is enclosed in double quotes ("")
2.  The ampersand joins the text and cell B5
3.  The cell reference (B5) is _not_ enclosed in quotes

In brief, hardcoded text values are enclosed in double quotes, while cell references, math operators, and function names are _not_ enclosed in quotes.

Now let's extend the text message above to add a period (.) at the end. In the screen below, the formula in D5 is:

![Basic concatenation example extended](https://exceljet.net/sites/default/files/images/articles/inline/Basic%20concatenation%20example%20extended.png "Basic concatenation example extended")

    ="Cell B5 contains "&B5&"."
    

In the new formula above, notice two things:

1.  We need another ampersand (&) to add the period
2.  The period is text and needs to be enclosed in quotes ("")

Naturally, this is a regular Excel formula that will recalculate automatically. If we change the value in B5 to 15, the new result is "Cell B5 contains 15.".

![Basic concatenation example with new cell value](https://exceljet.net/sites/default/files/images/articles/inline/Basic%20concatenation%20example%20with%20cell%20value%20changed.png "Basic concatenation example with new cell value")

This example shows the basics of concatenation in Excel with the ampersand (&) operator. Now let's look at an example of concatenation with some basic formula logic to customize a message.

### Concatenation with conditional logic

There's nothing special about concatenation, so you can mix in conditional formula logic as needed. In the formula below, we're using the same basic structure as the example above, with a different message:

![Another basic concatenation formula](https://exceljet.net/sites/default/files/images/articles/inline/Another%20basic%20concatenation%20formula.png "Another basic concatenation formula")

    ="Your score is "&B5&"."
    

We start the message, concatenate the value from B5, and concatenate the period. Now let's extend the formula with some conditional logic. Suppose we want to add the text "Nice work!" to the end of the message when the score is 85 or greater. To do this, we can add the [IF function](https://exceljet.net/videos/the-if-function)
 like this:

    ="Your score is "&B5&"."&IF(B5>=85," Nice work!","")
    

This looks complicated, so let's break it into parts. Part 1 is the same as before:

    ="Your score is "&B5&"." // part 1
    

Part 2 adds conditional logic based on the IF function:

    IF(B5>=85," Nice work!","") // part 2
    

If the score in cell B5 is 85 or higher, IF returns " Nice work!". Otherwise, IF returns an empty string (""). The final formula simply concatenates part 1 to part 2:

    ="Your score is "&B5&"."&IF(B5>=85," Nice work!","")
    

Notice we need another ampersand (&) to join part 1 and part 2, since IF is a function name. Also notice that we have included a space (" ") at the start of " Nice work!" so that this text doesn't run into the period\*. The screen below shows how the two formulas compare:

![Concatenation with formula logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Concatenation%20with%20formula%20logic.png?itok=UNzqcMhm "Concatenation with formula logic")

_\*Note: in more complex formulas that involve concatenation, you will find you frequently need to adjust space or punctuation to keep the message legible._

### Concatenation with number formatting

One tricky aspect of concatenation in Excel is [number formatting](https://exceljet.net/glossary/number-format)
. Number formats in Excel are a powerful way to control the display of numeric values, but they are not part of the number. This means that number formatting will be lost when you concatenate a formatted number. For example, in the worksheet below, B5 contains 99 formatted with the Currency number format. However, when B5 is concatenated in the formula in D5:

    ="The price is "&B5
    

the Currency formatting is lost:

![Concatenation with number formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Concatenation%20with%20number%20formatting.png?itok=AarFe0tk "Concatenation with number formatting")

You can add number formatting during concatenation by using the [TEXT function](https://exceljet.net/functions/text-function)
 in your formula. The formula in D6 is:

    ="The price is "&TEXT(B5,"$#,##0.00")
    

In this formula, we place the number in B5 inside the TEXT function and provide a basic Currency number format. As a result, the number 99 is displayed as $99.00 in the result.

### Date formatting

Dates are also numbers in Excel and their display is controlled by Date number formatting:

![Concatenation with date formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Concatenation%20with%20date%20formatting.png?itok=MVI2ae54 "Concatenation with date formatting")

In the worksheet below, the formula in D5 is:

    ="The report is due on "&B5
    

Notice the date appears as a [raw numeric value](https://exceljet.net/glossary/excel-date)
. The formula in D5 uses the TEXT function to apply a date format during concatenation:

    ="The report is due on "&TEXT(B5,"mmmm d")
    

Excel provides a large number of number formats you can use with the TEXT function. For more details, see [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
.

### Functions for concatenation

Up to now, we've focused on manual concatenation with the ampersand (&) operator. In this section, we'll look at the functions Excel provides to help with concatenation: [CONCATENATE](https://exceljet.net/functions/concatenate-function)
, [CONCAT](https://exceljet.net/functions/concat-function)
, and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
. In general, CONCATENATE and CONCAT are alternatives to manual concatenation with the ampersand (&) operator, while TEXTJOIN provides more advanced options for working with multiple values. I personally use the ampersand (&) operator as a default approach, and only use the functions below when needed.

### CONCATENATE function

The [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 is an older function now replaced by the CONCAT function. CONCATENATE allows you to perform simple concatenation only. The values to concatenate and any delimiters are supplied as separate [arguments](https://exceljet.net/glossary/function-argument)
, as seen in the example below:

![CONCATENATE function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CONCATENATE%20function%20example.png?itok=I-vch23E "CONCATENATE function example")

The main benefit of the CONCATENATE function is that values are supplied as separate arguments, with no need for an ampersand (&). The formulas in F5:F8 are:

    =CONCATENATE(B5,C5,D5)
    =CONCATENATE(B6,C6,D6)
    =CONCATENATE(B7,"-",C7,"-",D7)
    =CONCATENATE(B8,", ",C8,", ",D8)
    

Note that hardcoded text values must still be enclosed in double quotes (""), just like manual concatenation with the & operator.

### CONCAT function

The [CONCAT function](https://exceljet.net/functions/concat-function)
 replaces the CONCATENATE function in newer versions of Excel. The big difference between the two functions is that CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of values:

![CONCAT function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CONCAT%20function%20example.png?itok=U-anWYgP "CONCAT function example")

The formulas in F5:F8 are:

    =CONCAT(B5:D5)
    =CONCAT(B6:D6)
    =CONCAT(B7,"-",C7,"-",D7)
    =CONCAT(B8,", ",C8,", ",D8)
    

Notice the first two formulas supply a range directly to CONCAT as a single argument. The ability to provide a range is the primary advantage of CONCAT over CONCATENATE. The next two formulas supply individual values because they are joining values with a delimiter – a hyphen ("-) in the first formula and a comma with a space (", ") in the second formula. Although CONCAT can handle a range, there is no way to provide a delimiter as a separate argument. For this, we need to use the TEXTJOIN function.

### TEXTJOIN function

Finally, there is the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. Like the CONCAT function, TEXTJOIN is able to accept a [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
 of values to concatenate. However, TEXTJOIN provides two additional features that make it especially useful:

1.  Ability to accept custom delimiter
2.  Ability to ignore empty values

The syntax for TEXTJOIN is:

    =TEXTJOIN (delimiter, ignore_empty, text1, [text2], ...)
    

The first argument, _delimiter_, is the delimiter to use when joining values. The second argument, _ignore\_empty_, is a Boolean that indicates whether TEXTJOIN should ignore or process empty values. The remaining arguments, _text1_, _text2_, etc. represent the values to be joined. The worksheet below shows TEXTJOIN in action:

![TEXTJOIN function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/TEXTJOIN%20function%20example.png?itok=RskvJR23 "TEXTJOIN function example")

The formulas in F5:F10 are:

    =TEXTJOIN("",FALSE,B5:D5)
    =TEXTJOIN("",FALSE,B6:D6)
    =TEXTJOIN("-",FALSE,B7:D7)
    =TEXTJOIN(", ",FALSE,B8:D8)
    =TEXTJOIN(", ",FALSE,B9:D9)
    =TEXTJOIN(", ",TRUE,B10:D10)
    

Notice the first two formulas supply an empty string ("") for _delimiter_, which causes TEXTJOIN to join values directly. The next four formulas all supply one or more characters for _delimiter_. In cell F9, you can see how the delimiter is repeated when a range contains empty values and _ignore\_empty_ is set to FALSE. In F10, _ignore\_empty_ has been set to TRUE, and TEXTJOIN ignores the empty value in cell C10.

### More examples

Below are more examples that show how concatenation can be used in Excel formulas:

*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)
    
*   [Count cells greater than](https://exceljet.net/formulas/count-cells-greater-than)
    
*   [Make words plural](https://exceljet.net/formulas/make-words-plural)
    
*   [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    

### Videos

Here are some videos from our [online training](https://exceljet.net/training)
 that feature concatenation:

*   [How to join values with the ampersand](https://exceljet.net/videos/how-to-join-values-with-the-ampersand)
    
*   [How to use concatenation to clarify assumptions](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)
    
*   [Build friendly messages with concatenation](https://exceljet.net/articles/build-friendly-messages-with-concatenation)
    

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