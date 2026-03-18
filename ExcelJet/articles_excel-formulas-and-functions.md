# Excel formulas and functions | Exceljet

**Source:** https://exceljet.net/articles/excel-formulas-and-functions

---

[Skip to main content](https://exceljet.net/articles/excel-formulas-and-functions#main-content)

[](https://exceljet.net/articles/excel-formulas-and-functions#)

*   [Previous](https://exceljet.net/articles/how-to-lookup-first-and-last-match)
    
*   [Next](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    

Excel formulas and functions
============================

by Dave Bruns · Updated 19 Oct 2023

![Excel formulas and functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/fx.jpeg)

Summary
-------

Most people never receive proper Excel training and spend years frustrated by the simplest tasks, especially tasks that involve formulas. To use Excel with confidence, you must have a good understanding of formulas and functions. This article introduces the basic concepts you need to know to be proficient with formulas in Excel.

Formulas and functions are the bread and butter of Excel. They drive almost everything interesting and useful you will ever do in a spreadsheet. This article introduces the basic concepts you need to know to be proficient with formulas in Excel. [More examples here](https://exceljet.net/formulas)
.

### What is a formula?

A formula in Excel is an expression that returns a specific result. For example:

    =1+2 // returns 3
    

![Basic formula example - 1 + 3 = 3](https://exceljet.net/sites/default/files/images/articles/inline/basic%20formula%20example%201%20plus%202.png "Basic formula example - 1 + 3 = 3")

    =6/3 // returns 2
    

![Basic formula example - 6 / 3 = 2](https://exceljet.net/sites/default/files/images/articles/inline/basic%20formula%20example%206%20divided%20by%203.png "Basic formula example - 6 / 3 = 2")

Note: all formulas in Excel must begin with an equals sign (=).

### Cell references

In the examples above, values are "hardcoded". That means results won't change unless you edit the formula again and change a value manually. Generally, this is considered bad form, because it hides information and makes it harder to maintain a spreadsheet.

Instead, use [cell references](https://exceljet.net/videos/what-is-a-cell-reference)
 so values can be changed at any time. In the screen below, C1 contains the following formula:

    =A1+A2+A3 // returns 9
    

![Formula with cell references](https://exceljet.net/sites/default/files/images/articles/inline/formula%20with%20cell%20references.png "Formula with cell references")

Notice because we are using cell references for A1, A2, and A3, these values can be changed at any time and C1 will still show an accurate result.

### All formulas return a result

All formulas in Excel return a result, even when the result is an error. Below a formula is used to calculate percent change. The formula returns a correct result in D2 and D3, but returns a #DIV/0! error in D4, because B4 is empty:

![Formula result can be an error](https://exceljet.net/sites/default/files/images/articles/inline/formula%20result%20can%20be%20an%20error.png "Formula result can be an error")

There are different ways of handling errors. In this case, you could provide the missing value in B4, or "catch" the error with the [IFERROR function](https://exceljet.net/functions/iferror-function)
 and display a more friendly message (or nothing at all).

### Copy and paste formulas

The beauty of cell references is that they automatically update when a formula is copied to a new location. This means you don't need to enter the same basic formula again and again. In the screen below, the formula in E1 has been copied to the clipboard with Control + C:

![Formula in E1 copied to clipboard](https://exceljet.net/sites/default/files/images/articles/inline/cell%20references%201.png "Formula in E1 copied to clipboard")

Below: formula pasted to cell E2 with Control + V. Notice cell references have changed:

![Formula in E1 pasted to E2](https://exceljet.net/sites/default/files/images/articles/inline/cell%20references%202.png "Formula in E1 pasted to E2")

Below is the formula pasted to E3. Cell addresses are updated again:

![Formula in E1 pasted to E3](https://exceljet.net/sites/default/files/images/articles/inline/cell%20references%203.png "Formula in E1 pasted to E3")

### Relative and absolute references

The cell references above are called [_relative_](https://exceljet.net/glossary/relative-reference)
 references. This means the reference is relative to the cell it lives in.  The formula in E1 above is:

    =B1+C1+D1 // formula in E1
    

Literally, this means "cell 3 columns left "+ "cell 2 columns left" + "cell 1 column left". That's why, when the formula is copied down to cell E2, it continues to work in the same way.

Relative references are extremely useful, but there are times when you don't want a cell reference to change. A cell reference that won't change when copied is called an _[absolute reference](https://exceljet.net/glossary/absolute-reference)
._ To make a reference absolute, use the dollar symbol ($):

    =A1 // relative reference
    =$A$1 // absolute reference
    

For example, in the screen below, we want to multiply each value in column D by 10, which is entered in A1. By using an absolute reference for A1, we "lock" that reference so it won't change when the formula is copied to E2 and E3:

![Absolute reference example](https://exceljet.net/sites/default/files/images/articles/inline/absolute%20reference%20example.png "Absolute reference example")

Here are the final formulas in E1, E2, and E3:

    =D1*$A$1 // formula in E1
    =D2*$A$1 // formula in E2
    =D3*$A$1 // formula in E3
    

Notice the reference to D1 updates when the formula is copied, but the reference to A1 never changes. Now we can easily change the value in A1, and all three formulas recalculate. Below the value in A1 has changed from 10 to 12:

![Absolute reference example after value in A1 is changed](https://exceljet.net/sites/default/files/images/articles/inline/absolute%20reference%20example%202.png "Absolute reference example after value in A1 is changed")

This simple example also shows why it doesn't make sense to hardcode values into a formula. By storing the value in A1 in one place, and referring to A1 with an [absolute reference](https://exceljet.net/glossary/absolute-reference)
, the value can be changed at any time and all associated formulas will update instantly.

Tip: you can toggle between relative and absolute syntax with the [F4 key](https://exceljet.net/shortcuts/toggle-absolute-and-relative-references)
.

### How to enter a formula

To enter a formula:

1.  Select a cell
2.  Enter an equals sign (=)
3.  Type the formula, and press enter.

Instead of typing cell references, you can point and click, as seen below. Note references are color-coded:

![Entering a formula with point and click references](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Entering%20a%20formula%20with%20point%20and%20click.png?itok=qSTVC5xU "Entering a formula with point and click references")

All formulas in Excel must begin with an equals sign (=). No equals sign, no formula:

![Forgot to enter an equals sign means no formula, just text](https://exceljet.net/sites/default/files/images/articles/inline/Entering%20a%20formla%20forgot%20equal%20sign.png "Forgot to enter an equals sign means no formula, just text")

### How to change a formula

To edit a formula, you have 3 options:

1.  Select the cell, edit in the [formula bar](https://exceljet.net/glossary/formula-bar)
    
2.  Double-click the cell, edit directly
3.  Select the cell, [press F2](https://exceljet.net/shortcuts/edit-the-active-cell)
    , and edit directly

No matter which option you use, press Enter to confirm changes when done. If you want to cancel, and leave the formula unchanged, click the Escape key.

Video: [20 tips for entering formulas](https://exceljet.net/videos/23-excel-formula-tips)

### What is a function?

Working in Excel, you will hear the words "formula" and "function" used frequently, sometimes interchangeably. They are closely related, but not exactly the same. Technically, a formula is _any_ expression that begins with an equals sign (=).

A function, on the other hand, is a formula with a special name and purpose. In most cases, functions have names that reflect their intended use. For example, you probably know the [SUM function](https://exceljet.net/functions/sum-function)
 already, which returns the sum of given references:

    =SUM(1,2,3) // returns 6
    =SUM(A1:A3) // returns A1+A2+A3
    

The [AVERAGE function](https://exceljet.net/functions/average-function)
, as you would expect, returns the average of given references:

    =AVERAGE(1,2,3) // returns 2
    

The MIN and MAX functions return minimum and maximum values, respectively:

    =MIN(1,2,3) // returns 1
    =MAX(1,2,3) // returns 3
    

Excel contains [hundreds of specific functions](https://exceljet.net/functions)
. To get started, see [101 Key Excel functions](https://exceljet.net/articles/101-excel-functions)
.

### Function arguments

Most functions require inputs to return a result. These inputs are called "arguments". A function's arguments appear after the function name, inside parentheses, separated by commas.  All have a name, and an opening and closing parentheses (). The inputs inside the parentheses are called "arguments".The pattern looks like this:

    =NAME(argument1,argument2,argument3)
    

For example, the [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts cells that meet criteria, and takes two arguments, _range_ and _criteria_:

    =COUNTIF(range,criteria) // two arguments
    

In the screen below, _range_ is A1:A5 and _criteria_ is "red". The formula in C1 is:

    =COUNTIF(A1:A5,"red") // returns 2
    

 ![COUNTIF requires two arguments, range and criteria](https://exceljet.net/sites/default/files/images/articles/inline/function%20arguments%20example%20COUNTIF.png "COUNTIF requires two arguments, range and criteria")

Video: [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

Not all arguments are required. Arguments shown in square brackets \[ \] are optional. For example, the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 returns the fractional number of years between a start date and an end date and takes 3 arguments:

    =YEARFRAC(start_date,end_date,[basis])
    

_Start\_date_ and _end\_date_ are required arguments, _basis_ is an optional argument. See below for an example of how to use YEARFRAC to calculate current age based on birthdate.

### How to enter a function

If you know the name of the function, just start typing. Here are the steps:

1\. Enter an equals sign (=) and start typing. Excel will make a list of matching functions based as you type:

![As you type, Excel will show matching functions](https://exceljet.net/sites/default/files/images/articles/inline/enter%20function%201.png "As you type, Excel will show matching functions")

When you see the function you want in the list, use the arrow keys to select (or just keep typing).

2\. Type the Tab key to accept a function. Excel will complete the function:

![Press Tab to enter selected function](https://exceljet.net/sites/default/files/images/articles/inline/enter%20function%202.png "Press Tab to enter selected function")

3\. Fill in required arguments:

![Enter required arguments](https://exceljet.net/sites/default/files/images/articles/inline/enter%20function%203.png "Enter required arguments")

4\. Press Enter to confirm formula:

![Press Enter to confirm and enter the function](https://exceljet.net/sites/default/files/images/articles/inline/enter%20function%204.png "Press Enter to confirm and enter the function")

### Combining functions (nesting)

Many Excel formulas use more than one function, and functions can be "[nested](https://exceljet.net/glossary/nesting)
" inside each other. For example, below we have a birthdate in B1 and we want to calculate the current age in B2:

![Need a formula to calculate current age in B2](https://exceljet.net/sites/default/files/images/articles/inline/combine%20functions%201.png "Need a formula to calculate current age in B2")

The [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 will calculate years with a start date and end date:

![YEARFRAC will calculate years with a start date and end date](https://exceljet.net/sites/default/files/images/articles/inline/combine%20functions%202.png "YEARFRAC will calculate years with a start date and end date")

We can use B1 for the start date, and then use the [TODAY function](https://exceljet.net/functions/today-function)
 to supply the end date:

![B1 for start date, the TODAY function to supply end date](https://exceljet.net/sites/default/files/images/articles/inline/combine%20functions%203.png "B1 for start date, the TODAY function to supply end date")

When we press Enter to confirm, we get current age based on today's date:

    =YEARFRAC(B1,TODAY())
    

![YEARFRAC and TODAY functions to calculate current age](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/combine%20functions%204.png?itok=U8FNt5zL "YEARFRAC and TODAY functions to calculate current age")

Notice we are using the TODAY function to feed an end date to the YEARFRAC function. In other words, the TODAY function can be nested inside the YEARFRAC function to provide the end date argument. We can take the formula one step further and use the [INT function](https://exceljet.net/functions/int-function)
 to chop off the decimal value:

    =INT(YEARFRAC(B1,TODAY()))
    

![YEARFRAC and TODAY inside INT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/combine%20functions%205.png?itok=ET0PLQQS "YEARFRAC and TODAY inside INT")

Here, the original YEARFRAC formula returns 20.4 to the INT function, and the INT function returns a final result of 20.

Notes:

1.  The screens above were created on February 22, 2019.
2.  Nested [IF functions](https://exceljet.net/functions/if-function)
     are a classic example of [nesting functions](https://exceljet.net/articles/nested-ifs)
    . 
3.  The [TODAY function](https://exceljet.net/functions/today-function)
     is a rare Excel function with no required arguments.

_Key takeaway: The output of any formula or function can be fed directly into another formula or function._ 

### Math Operators

The table below shows the standard math operators available in Excel:

| Symbol | Operation | Example |
| --- | --- | --- |
| +   | Addition | \=2+3=5 |
| \-  | Subtraction | \=9-2=7 |
| \*  | Multiplication | \=6\*7=42 |
| /   | Division | \=9/3=3 |
| ^   | Exponentiation | \=4^2=16 |
| ()  | Parentheses | \=(2+4)/3=2 |

### Logical operators

Logical operators provide support for comparisons such as "greater than", "less than", etc. The logical operators available in Excel are shown in the table below:

| Operator | Meaning | Example |
| --- | --- | --- |
| \=  | Equal to | \=A1=10 |
| <>  | Not equal to | \=A1<>10 |
| \>  | Greater than | \=A1>100 |
| <   | Less than | \=A1<100 |
| \>= | Greater than or equal to | \=A1>=75 |
| <=  | Less than or equal to | \=A1<=0 |

Video: [How to build logical formulas](https://exceljet.net/plc/how-to-build-logical-formulas)

### Order of operations

When solving a formula, Excel follows a sequence called "order of operations". First, any expressions in parentheses are evaluated. Next Excel will solve for any exponents. After exponents, Excel will perform multiplication and division, then addition and subtraction. If the formula involves [concatenation](https://exceljet.net/glossary/concatenation)
, this will happen after standard math operations. Finally, Excel will evaluate [logical operators](https://exceljet.net/glossary/logical-operators)
, if present.

1.  Parentheses
2.  Exponents
3.  Multiplication and Division
4.  Addition and Subtraction
5.  Concatenation
6.  Logical operators

Tip: you can use the [Evaluate feature](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
 to watch Excel solve formulas step-by-step.

### Convert formulas to values

Sometimes you want to get rid of formulas and leave only values in their place. The easiest way to do this in Excel is to copy the formula, then paste, using Paste Special > Values. This overwrites the formulas with the values they return. You can use a [keyboard shortcut](https://exceljet.net/shortcuts/display-the-paste-special-dialog-box)
 for pasting values, or use the Paste menu on the Home tab on the ribbon.

Video: [Paste Special Shortcuts](https://exceljet.net/videos/shortcuts-for-paste-special)

### What's next?

Below are guides to help you learn more about Excel's formulas and functions. We also offer [online video training](https://exceljet.net/training)
.

*   [29 tips for working with formulas](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
     and functions ([video version here](https://exceljet.net/plc/excel-formulas-23-tips-to-save-you-time-today)
    )
*   [500 formula examples](https://exceljet.net/formulas)
     with full explanations
*   [101 important Excel functions](https://exceljet.net/articles/101-excel-functions)
    
*   [Guide to all Excel functions](https://exceljet.net/functions)
     (work in progress)
*   [Excel formula errors](https://exceljet.net/articles/excel-formula-errors)
     (examples and fixes)
*   [Formula criteria - 50 examples](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Formulas for conditional formatting](https://exceljet.net/conditional-formatting-formulas)
    
*   [How to use F9 to debug a formula](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
     (video)
*   [Excel formula errors and fixes](https://exceljet.net/videos/examples-of-flagged-errors-in-formulas)
     (video)

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