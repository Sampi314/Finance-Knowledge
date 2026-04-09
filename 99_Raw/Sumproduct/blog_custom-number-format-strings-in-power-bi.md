# Power BI Blog: Custom Number Format Strings in Power BI

**Source:** https://sumproduct.com/blog/custom-number-format-strings-in-power-bi/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Custom Number Format Strings in Power BI

*   February 5, 2026

Power BI Blog: Custom Number Format Strings in Power BI
=======================================================

___Welcome back to this week’s edition of the Power BI blog series.  This week, we look at custom number formatting.___

Custom number formatting is a simple and impactful tool for improving the aesthetic of any data laden Power BI dashboard.  Common formatting syntax for Power BI includes the following:

| Number Code | Description |
| --- | --- |
| **General** | General number format |
| **0** | Digit placeholder (0 for ‘padding’) |
| **#** | Digit placeholder (extra zeroes not displayed) |
| **. (decimal point)** | Decimal placeholder. In some locales, a comma is used as the decimal separator |
| **%** | Percentage placeholder |
| **, (comma)** | Thousands separator |
| **E+, E-, e-, e+** | Scientific notation |

| **Text Code** | **Description** |
| --- | --- |
| **$ – + ()** | These characters are displayed in the number |
| **\\** | Display the next character |
| **`"text"`** | To display other characters, enclose in quotation marks |

| **Date Code** | **Description** |
| --- | --- |
| **/** | Date separator |
| **M** | Month as a number without leading zeroes (1 to 12) |
| **MM** | Month as a number with leading zeroes (01 to 12) |
| **MMM** | Month as an abbreviation (Jan – Dec) |
| **MMMM** | Full month name (January – December) |
| **d** | Day without leading zeroes (1 to 31) |
| **dd** | Day with leading zeroes (01 to 31) |
| **ddd** | Day as an abbreviation (Sun – Sat) |
| **dddd** | Unabbreviated day (Sunday – Saturday) |
| **y or yy** | Year as a two-digit number (e.g. 09 ,97) |
| **yyyy** | Year as a four-digit number (e.g. 2009,1997) |

| **Time code** | **Description** |
| --- | --- |
| **:** | Time separator |
| **h** | Hours as a number without the leading zero (0 to 23) |
| **hh** | Hours as a number with leading zeroes (00 to 23) |
| **n** | Minutes as a number without leading zero (0 to 59) |
| **nn** | Minutes as a number with leading zeroes (00 to 59) |
| **m** | Minutes as a number without leading zero (0 to 59). Only if preceded by h or hh or used in format code of Visual level |
| **mm** | Minutes as a number with leading zeroes (00 to 59). Only if preceded by h or hh or used in format code of Visual level |
| **s** | Seconds as a number without leading zero (0 to 59) |
| **ss** | Seconds as a number with leading zeroes (00 to 59) |
| **tt** | Use 12-hour clock and display AM / PM |

| **Date Preset** | **Description** |
| --- | --- |
| **General** | Display the date and time |
| **Long Date** | Display the date your operating system is set to use in long date format |
| **Short Date** | Display the date your operating system is set to use in short date format |
| **Long Time** | Display the time your operating system is set to use in long time format. Includes hours, minutes and seconds |
| **Short Time** | Display the time using military time (e.g. 15:35) |

| **Number Preset** | **Description** |
| --- | --- |
| **General** | Display the number without formatting |
| **Currency** | Display number with a thousand separator and a dollar sign |
| **Fixed** | Display at least one \[1\] before and two \[2\] digits after the decimal point |
| **Standard** | Display at least one \[1\] before and two \[2\] digits after the decimal point, and a thousand separator |
| **Percent** | Display number multiplied by 100 percent and two \[2\] digits after the decimal point |
| **Scientific** | Use standard scientific notation |

When using this syntax, Power BI follows a **Positive;Negative;Zero** order where a semicolon is placed to distinguish between each element and its unique formatting parameters, for example:

**`"#,##0;(#,##0);-"`**

This creates a thousand separator for each non-zero value, and places brackets around negative values only. For zeroes, it replaces them with a dash:

![](<Base64-Image-Removed>)

**_Limitations of Power BI Compared to Excel_**

If you have used number format codes in Excel, you may expect a similar experience in Power BI and, for the most part, because Power BI uses a similar syntax, it is.  However, there are some key differences:

*   **Only three \[3\] elements in syntax order**: Power BI has no fourth element within its syntax order for text-based data.  You cannot set a format string for fields that are text or Boolean
*   **Colour:** Power BI currently does not support colour in its format codes, instead it uses an independent conditional formatting feature
*   **Formatting Alignment and Spacing:** using syntax that alters the visual position of text or values, such as an underscore, will reproduce the syntax as part of the string rather than creating the desired realignment. Here is a working example of successful realignment achieved in Excel:

**#,##0\_);(#,##0)**

![](<Base64-Image-Removed>)

   Here is the same code used in Power BI which produces the underscore and bracket literally:

**`"#,##0_);(#,##0)"`**

![](<Base64-Image-Removed>)

*   **Other unintegrated syntax**: Syntax like **@**, **?**, and **mmmmm** are integrated into Excel, however, these are not available in Power BI.

Despite having these limitations, using format codes is a quick and simple way to visually transform your data.

**_How to use Format Codes_**

Here are some common formatting string examples for you to use:

| **Description** | **Format string** |
| --- | --- |
| **Thousand separators** | #,0 |
| **Decimal places** | #,0.00 |
| **Percentage** | #,0% |
| **Currency** | $#,0 |
| **Scientific notation** | 0.00E+00 |
| **Brackets if negative value** | #,0;(#,0) |
| **Number in thousand with 1 decimal place** | #,0,.0K |
| **Number in million with 2 decimal places** | #,0,,.00M |
| **Up/down icon** | ▲ #,0;▼ #,0 |

There are three \[3\] main methods in applying format codes, the most common method being directly through a measure.  To perform this first method, click on the target field, then ‘Measure tools’ and type the format string directly in the Format box or in the Format box dropdown choose Dynamic:

![](<Base64-Image-Removed>)

The Format formula bar will appear in place of the typical Measure formula bar.  Enter in the desired formatting code in speech commas (**`""`**), for example:

**`"$#,##0 AUD"`**

![](<Base64-Image-Removed>)

This format code will produce a currency symbol at the beginning and “AUD” as text at the end.  It will also generate separators:

![](<Base64-Image-Removed>)

For the second method, you can change the format at the visual level.  First, select the visual containing the value and then click **Format your visual ->** **General** **\-> Data format**:

![](<Base64-Image-Removed>)

Then, open the Format options tab, switch the format to Custom and enter the desired format code into the Format code bar:

**`"$#,##0 AUD"`**

![](<Base64-Image-Removed>)

The third method is for formatting a table of values.  First, click ‘Model view’ and select the field intended for the desired change:

![](<Base64-Image-Removed>)

Then, in the Properties pane, under **Formatting**, click **Format -> Custom**, and under ‘Custom format’ enter the code into the second box:

![](<Base64-Image-Removed>)

The format code used here generates brackets around negative numbers and adds separators:

`**"#,##0;(#,##0)"**`

![](<Base64-Image-Removed>)

Simple.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/public-courses/)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

*   [Log in](https://sumproduct.com/blog/custom-number-format-strings-in-power-bi/#0)
    
*   [Register](https://sumproduct.com/blog/custom-number-format-strings-in-power-bi/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/custom-number-format-strings-in-power-bi/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/custom-number-format-strings-in-power-bi/#0)

[](https://sumproduct.com/blog/custom-number-format-strings-in-power-bi/#0 "close")

top