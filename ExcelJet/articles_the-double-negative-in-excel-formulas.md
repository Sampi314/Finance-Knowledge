# The double negative in Excel formulas | Exceljet

**Source:** https://exceljet.net/articles/the-double-negative-in-excel-formulas

---

[Skip to main content](https://exceljet.net/articles/the-double-negative-in-excel-formulas#main-content)

[](https://exceljet.net/articles/the-double-negative-in-excel-formulas#)

*   [Previous](https://exceljet.net/articles/excel-formulas-and-functions)
    
*   [Next](https://exceljet.net/articles/101-excel-functions)
    

The double negative in Excel formulas
=====================================

by Dave Bruns · Updated 29 Oct 2023

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/4996/download?token=KxBaAQMM)
 (9.16 KB)

![The double negative in Excel formulas](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/double_negative_0.jpeg)

Summary
-------

The double negative coerces TRUE or FALSE values to their numeric equivalents, 1 and 0. This is a useful technique in many advanced formulas that work with cell ranges.

> Note: the discussion on this page is about converting TRUE and FALSE values to 1s and 0s. However, the techniques discussed on this page are more general and will also work to convert any number that is text to a numeric value. 

In more advanced Excel formulas, you might run into the double negative operation (--):

![Double negative in action](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/double%20negative%20formula%20example3.png?itok=p0wZmM-Q "Double negative in action")

What the heck is that, and what is it doing?

The double negative (sometimes called the even more nerdy "double unary") coerces TRUE or FALSE values to their numeric equivalents, 1 and 0. It's used in formulas where numbers are needed for a particular math operation. That might sound pretty vague, so I'll illustrate with the example above. Let's say you have a list of words in a range, and you want to count how many contain more than 5 characters.

![How to count cells with more than 5 characters?](https://exceljet.net/sites/default/files/images/articles/inline/How%20to%20count%20cells%20with%20more%20than%205%20chars.png "How to count cells with more than 5 characters?")

You can build a simple formula to do this with the [LEN function](https://exceljet.net/functions/len-function)
 and this expression:

    LEN(B5:B9)>5
    

For each of the five cells in the range, LEN will return a character count, which will be checked with >5. The result will be an array of 5 TRUE or FALSE values like this:

    {FALSE;TRUE;TRUE;FALSE;TRUE}
    

Notice there are 3 TRUE values, one each for each text value with more than 5 characters: "banana", "pineapple", and "grapefruit". The 2 FALSE values are for "Apple" and "Pear". Now, if we drop that expression into SUMPRODUCT to count the TRUE results, what do we get?

    =SUMPRODUCT(LEN(B5:B9)>5)
    

We get zero. Why?

Because TRUE and FALSE are logicals, not numbers.

![Zero result without coercion](https://exceljet.net/sites/default/files/images/articles/inline/zero%20result%20without%20coercion.png "Zero result without coercion")

    =SUMPRODUCT({FALSE;TRUE;TRUE;FALSE;TRUE}) // returns zero
    

Excel won't treat logicals as numbers without a little nudge. Fortunately, it doesn't take much. Any math operation will get Excel to convert TRUE to 1 and FALSE to zero. As it turns out, the double negative is a simple and clear way to do this. The first negative will convert TRUE to -1, and the second negative will convert -1 to 1. In the case of FALSE values, the first negative will result in zero, and the second negative will also result in zero.

To use the double negative in this formula, we wrap the original expression in parentheses, put a double negative out front.

![Correct result after coercion with double negative](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/correct%20result%20after%20coercion.png?itok=MM4whQ6v "Correct result after coercion with double negative")

    =SUMPRODUCT(--(LEN(B5:B9)>5)) // coerce with --
    =SUMPRODUCT({0;1;1;0;1}) // returns 3
    

By the way, I'm using the SUMPRODUCT function here instead of SUM so that we don't need to enter as an [array formula](https://exceljet.net/glossary/array-formula)
, with control + shift + enter. But SUM entered with control + shift + enter will yield the same result.

### Debugging with F9

Whenever you're working with things like double negatives, you must know how to use F9 to debug a formula. The F9 key is like an x-ray to reveal what Excel is really doing "under the hood". For example, if I select the original expression in the formula and press F9, I see an array of TRUE and FALSE values.

![Step 1: carefully select entire expression](https://exceljet.net/sites/default/files/images/articles/inline/step%201%20carefully%20select%20entire%20expression.png "Step 1: carefully select entire expression")![Step 2: press F9 key to debug](https://exceljet.net/sites/default/files/images/articles/inline/step%202%20press%20F9%20key%20to%20debug.png "Step 2: press F9 key to debug")

If I select the _revised formula_, including the double negative, and press F9:

![Step 1 - select expression](https://exceljet.net/sites/default/files/images/articles/inline/Step%201%20select.png "Step 1 - select expression")

Excel will show 1's and 0's.

![Step 2 - press F9](https://exceljet.net/sites/default/files/images/articles/inline/step%202%20press%20F9%20key.png "Step 2 - press F9")

Video: [How to debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

Video: [23 tips to save time with formulas](https://exceljet.net/videos/23-excel-formula-tips)

### Other ways to coerce

A double negative is not the only way to get ones and zeros from logicals. You can also add or subtract zero, multiply by one, or use the inscrutably named [N function](https://exceljet.net/functions/n-function)
. All of the formulas below will return the same result:

    =SUMPRODUCT(--(LEN(range)>5))
    =SUMPRODUCT((LEN(range)>5)+0)
    =SUMPRODUCT((LEN(range)>5)*1)
    =SUMPRODUCT(N(LEN(range)>5))
    

Which option should you use?

Personally, I use the double negative option most often, because it's simple and clearly indicates the purpose. But I like the [N function](https://exceljet.net/functions/n-function)
 as well.

### Other examples

Coercing TRUE and FALSE values to 1's and 0's is incredibly useful in all kinds of formulas, but it takes a little getting used to. Here are some other formulas that use this technique:

*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    
*   [Count cells that contain text case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Count cells by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-equals-one-of-many-things)
    
*   [Count matches between columns](https://exceljet.net/formulas/count-matches-between-two-columns)
    
*   [SUMPRODUCT function (see example)](https://exceljet.net/functions/sumproduct-function)
    

You can find [many other examples here](https://exceljet.net/formulas)
.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [101 Excel Functions you should know](https://exceljet.net/articles/101-excel-functions)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [29 ways to save time with Excel formulas](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
    

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