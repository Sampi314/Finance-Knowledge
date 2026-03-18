# Multiple Number Formatting

**Source:** https://sumproduct.com/thought/multiple-number-formatting/

---

[Home](https://sumproduct.com/)

\> Multiple Number Formatting

*   May 14, 2025

Multiple Number Formatting
==========================

How to circumvent the supposed Excel limit of number formats in one cell.

Multiple Number Formatting
==========================

This article extends the idea of number formatting. By Liam Bastick, Managing Director (and Excel MVP) with SumProduct Pty Ltd.

Query
-----

Is it possible to have many different number formats in one cell in Excel?

Advice
------

Imagine you wanted to format a cell so that the following values would appear as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/e86aba1eb797146569ecf65abe110130.jpg)

Multiple Number Formats Example Revisited

The plan here is to create the correct formatting without using VBA code or Excel formulae in ONE cell so that if any of the above values in the left hand column are entered into that cell they will appear as they are displayed in the right-hand column.

Number formatting has been discussed before (please see [Number Formatting](https://www.sumproduct.com/thought/number-formatting)
 for more details). A brief summary is provided below.

### Number Formatting Recap

Given that one of the primary purposes of a spreadsheet is to present numerical data, it is important how numerical data is presented. Cells may be individually formatted, using **CTRL + 1** or **ALT + O + E** in all versions of Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/image-01-format-cells-dialog-box1.gif)

Format Cells Dialog Box

Formatting only changes the appearance, not the underlying value, of a cell. For example, if cells **A1** and **B1** had the number ’1.4? typed in but were formatted to zero decimal places, then if cell **C1 = A1 + B1**, you would truly have 1 + 1 = 3 (well, 1.4 + 1.4 = 2.8 anyway).

Excel has many built-in number formats that are fairly easy to understand, e.g. Currency, Date, Percentage. Selecting the ‘Custom’ category activates the ‘Type’ input box and allows between 200 and 250 custom number formats in a particular workbook, depending upon the language version of Excel that has been installed.

The ‘Type’ input box allows up to four aspects of formatting to be specified in a cell. These aspects are referred to as sections and are separated by a semi-colon (;). To ascertain what is contained in each section depends on the total number of sections used, viz.

| Number of Sections | Section Details (Assuming No Conditions) |
| --- | --- |
| 1 (Min) | All numerical values |
| 2   | Non-negative numbers; negative numbers |
| 3   | Positive numbers; negative numbers; zero values |
| 4 (Max) | Positive numbers; negative numbers; zero values; text |

The following example has been explained in the aforementioned [Number Formatting](https://www.sumproduct.com/thought/number-formatting)
 article.

### Example 1

\[Blue\]$\* \_(#,##0.0,\_0\_);\[Red\]$\* (#,##0.00,);\[Color 7\]-\_.\_0\_0\_);\[Cyan\]@\*.”is text”

![](<Base64-Image-Removed>)

There is an alternative to the above four arguments:

| Number of Sections | Section Details (Assuming No Conditions) |
| --- | --- |
| 1 (Min) | All numerical values |
| 2   | Numbers meeting criterion; All other values |
| 3 (Max) | Numbers meeting first criterion; Numbers meeting second criterion which do not meet the first criterion; All other values |

This can be demonstrated as follows:

### Example 2 (‘Conditional Formatting’ in a Cell)

\[>=1000000\]#,##0,,”M”;\[>=1000\]#,##0,”K”;0

![](<Base64-Image-Removed>)

The conditions are included in square brackets such that if the condition is true, the following formatting will be applied.

In this example, there are only three sections, so text will be formatted ‘generally’. The first section, **\[>=1000000\]#,##0,,”M”**, will format all numbers greater than or equal to a million to the nearest million and add an “M” to the end of the number.

The second section will only be considered if the first condition is not true, so the order of the two ‘conditional formats’ needs to be thought through. Here, the second section, **\[>=1000\]#,##0,”K”**, will format all numbers greater than or equal to a thousand (but necessarily less than a million) to the nearest thousand and add a “K” to the end of the number.

The third and final section, **0**, will format all other numbers (every value less than 1,000) to the nearest integer without thousands separator(s).

This example is almost what we require; the problem is, we need to be able to cater for more conditions. So how do we do this?

### Conditional Formatting

In a previous article, I discussed [Conditional Formatting](https://www.sumproduct.com/thought/conditional-formatting)
, which was completely revamped and reinvented with the introduction of Excel 2007. Located in the Styles group of the Home tab, the conditional formatting feature allows you to consider multiple conditions:

![](<Base64-Image-Removed>)

Conditional Formatting: Drop Down Menu

For instance, inspecting ‘Highlight Cells Rules’ is akin to many of the “Cell Value Is” functionalities of its predecessor, e.g. Greater Than, Less Than, Between, Equal To. I can use this to exploit a loophole in the restrictive number of conditions custom number formatting appears to allow.

For example:

![](<Base64-Image-Removed>)

Conditional Formatting: Accessing Number Formatting

In this above illustration, I have selected conditional formatting to occur if the value in the cell is less than -1. Pressing the ‘Format…’ button then allows the user to select how the number formatting might appear.

Let me consider the problem again:

![](<Base64-Image-Removed>)

Multiple Number Formats Example Revisited

Using both functionalities, the requirement is fairly straightforward. My suggested solution would be:

*   Construct the underlying number formatting first. Personally, I would use custom number formatting so that all positive and negative numbers appeared as percentages, zero as a hyphen (“-”) and text as displayed above;
*   Next, I would apply conditional formatting number formatting where the cell value is greater than one so that numbers greater than a million could be displayed to the nearest 0.1m, numbers less than a million but greater than or equal to 1,000 could be displayed to the nearest 0.00k and numbers lower than 1,000 (but necessarily greater than one) could be displayed as integers; and
*   Finally, I would apply a second set of conditional formatting where the cell value is less than -1 as required.

I do not go through the required syntax here. My suggested solution can be found in the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-multiple-number-fomatting.xls)
 and the rationale / explanation can be understood by reading through the previous article on [Number Formatting](https://www.sumproduct.com/thought/number-formatting)
.

Since many, many conditional formats may be applied to one cell in Excel, you can soon apply significantly more than four formats to any cell(s) in Excel.

### Word to the Wise

Although I have explained you can circumvent the apparent limitations in number formatting using conditional formatting, applying too many unnecessary conditional formats can cause Excel to misbehave with cells not updating as intended and other cells (not formatted) changing as well.

These quirks suggest memory issues so limiting this methodology on a “as needs require” basis is thoroughly recommended.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/multiple-number-formatting/#0)
    
*   [Register](https://sumproduct.com/thought/multiple-number-formatting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/multiple-number-formatting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/multiple-number-formatting/#0)

[](https://sumproduct.com/thought/multiple-number-formatting/#0 "close")

top