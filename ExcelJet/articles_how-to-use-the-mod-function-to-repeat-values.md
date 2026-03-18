# How to use the MOD function to repeat values | Exceljet

**Source:** https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values

---

[Skip to main content](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values#main-content)

[](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values#)

*   [Previous](https://exceljet.net/articles/nested-ifs)
    
*   [Next](https://exceljet.net/articles/how-to-set-a-default-template-in-excel)
    

How to use the MOD function to repeat values
============================================

by Dave Bruns · Updated 24 Oct 2023

![Like a clock, the MOD function repeats](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Mod-2.png "Like a clock, the MOD function repeats")

Summary
-------

MOD is nerdy, but cool. If you've ever struggled to create a more complex formula in Excel, you'll like this one. It shows you how to build a more complex formula step-by-step, without going crazy.

Ever use Excel's [MOD function](https://exceljet.net/functions/mod-function)
?

The MOD function performs the _modulo operation_. It takes a number and a divisor, does the division, and gives you back the remainder.

Unless you're a programmer, this might seem way too nerdy. Modulo? Seriously? What can the average person do with that?

As it turns out — a lot!

_Note: MOD turns up in many compact, elegant formulas in Excel. In fact, if you use MOD in one of your formulas, people will automatically assume you're an Excel pro, so take care :)_

To illustrate how MOD is useful, let me pose a simple problem:

Let's say you maintain a budget with some monthly expenses, and you'd like to enter an expense that occurs every 3 months, and zero for months in between. You want something like this:

![Using the MOD function to generate a repeating value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20done.png?itok=gWYLBbg5 "Using the MOD function to generate a repeating value")

Simple, right? But how to begin...what kind of formula does something every 3 months?

Believe it or not, the MOD function is the key.

Earlier, I mentioned the remainder. The trick in this case is not the remainder itself, but rather what it means when you _don't_ get a remainder. In other words, when MOD returns _zero_.

Think about it — when the remainder is zero, it means the divisor goes into the number evenly.

Hmmm...we can use that!

Note: if you want more background on why MOD works well for repeating things, [Khan Academy has a nice explanation of modular arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
.

We want to do something every 3 months. So, if we run the month number through MOD with a divisor of 3, and get zero as the result, it's time to add the expense.

Let's do it.

First, let's add month numbers above our table so we have something to work with right away.

![Month numbers hardcoded for rapid prototyping](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20add%20month%20numbers.png?itok=4gVnHf9O "Month numbers hardcoded for rapid prototyping")

_Tip: When you're building a more complex formula, don't be afraid to hard-code values that will help you validate your ideas quickly. Think of this as rapid prototyping. Once you know your approach will work, you can come back and figure out how to remove the hard-coded values. Don't optimize prematurely!_

Now, with the month numbers in place, we'll enter a simple MOD formula.

    =MOD(B5,3)
    

This gives us the remainder in each cell, and every 3 months, we get a remainder of zero.

![The MOD function gives us zero every 3 months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20basic%20mod.png?itok=4zqeHxNR "The MOD function gives us zero every 3 months")

Next, let's get our value in there when the remainder is zero, and get rid of the other numbers. We can do this by adding an IF statement to test for a zero remainder: if the remainder is zero, return 60, otherwise return 0.

    =IF(MOD(B5,3)=0,60,0)
    

Now we have 60 at every 3rd month and a zero in between. Cool.

![Using IF with MOD to filter non-zero results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20mod%20with%20IF.png?itok=Op0zy3lA "Using IF with MOD to filter non-zero results")

Next, we'll replace the hardcoded 60 with a reference to B4 so we can easily change it later. Obviously, if the value will never change, there's no need to do this, but it's a good practice to expose inputs on the worksheet, especially when they appear in more than one place, and might change later.

We use an absolute reference for B4 so we can copy the formula across without it changing.

    =IF(MOD(B5,3)=0,$B$4,0)
    

![The formula now contains a variable input](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20with%20B4%20ref.png?itok=6TCazZbp "The formula now contains a variable input")

This is just what we need, but it's time to get rid of those unsightly numbers we added above the months.

How can we do it?

There are two ways we can deal with this. One method uses the COLUMN function, and one uses the MONTH function. (See how knowing [more Excel functions](https://exceljet.net/functions)
 can be useful?)

We'll look at COLUMN first...

### With the COLUMN function

The COLUMN function returns the column number of a given reference. When you don't give COLUMN a reference, it returns the column number of the _current cell_. This is easier to show than explain, so let's add the COLUMN function to the cells that currently contain month numbers:

![Replacing hardcoded month numbers with the COLUMN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20with%20COLUMN%20function.png?itok=3g3tCk-g "Replacing hardcoded month numbers with the COLUMN function")

This is nice, but notice that it's not quite what we need. The first number starts with 2, not 1, because the first formula sits in the second column. So this throws off our repeating values.

Easily solved. We just need to subtract 1 from the column number:

    COLUMN()-1
    

Note: think of 1 as an "offset" that you adjust as needed for your situation.

![Correcting the COLUMN function with an offset](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20with%20COLUMN%20function%202.png?itok=PwBNAJ7p "Correcting the COLUMN function with an offset")

Now COLUMN generates the month numbers we need, and we can update our formula. We simply nest the COLUMN function where we had a reference to the month numbers:

    =IF(MOD(COLUMN()-1,3)=0,$B$4,0)
    

Then we can delete the numbers:

![MOD formula updated with the COLUMN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20with%20COLUMN%20function%203.png?itok=pr1BMwBG "MOD formula updated with the COLUMN function")

### With the MONTH function

While the COLUMN function works fine, it's a little awkward, because we have to hardcode an offset value to get a correct month number. We only have 12 months — isn't there some way to use the month numbers directly? Yes, in fact, there is.

With a little tweak, we can build a more logical formula by using actual dates.  To do this, we need to replace the month abbreviations ("Jan", "Feb", "Mar", etc.) with full dates like 1/1/2016, 2/1/2016, 3/1/2016, etc.

Tip: Enter the first two dates then select them both, and [use the fill handle](https://exceljet.net/videos/how-to-enter-custom-patterns-with-the-fill-handle-in-excel)
 to have Excel fill in the rest. 

![Text labels replaced with dates in month headers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20dates%20in%20headers%201.png?itok=4vt8olOH "Text labels replaced with dates in month headers")

At first, this looks silly — people don't want to see actual dates for months.

No problem. All we need to do is apply the custom number format "mmm" to the dates, and we've got abbreviated month names again:

![Back to month names again with a custom number format](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20dates%20with%20custom%20number%20format%20.png?itok=IRJ1vdsJ "Back to month names again with a custom number format")  
_Same dates with the custom date format "ddd"._

The beauty of this approach is that the column headers now contain regular dates, so we can use normal date functions on them.

And now we can simply use the MONTH function to get the number, and ditch COLUMN:

    =IF(MOD(MONTH(B6),3)=0,$B$4,0)
    

![MOD formula updated to use the MONTH function instead of COLUMN](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/repeat%20value%20with%20MOD%20dates%20with%20MONTH.png?itok=OUD6awFX "MOD formula updated to use the MONTH function instead of COLUMN")

This eliminates that offset value, and the formula will work wherever the budget table appears in the worksheet.

### More MOD formulas

As I mentioned, the MOD function is a versatile function and can be used in many ways, so you'll see it in a variety of formulas. It's particularly useful for "every nth" type formulas, but it's handy for other things to. Here's a list of examples you can use for inspiration.

[Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
  
[Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
  
[Count cells that contain odd numbers](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers)
  
[Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)
  
[Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)
  
[Fixed value every N months](https://exceljet.net/formulas/repeat-fixed-value-every-3-months)
  
[Highlight every other row](https://exceljet.net/formulas/highlight-every-other-row)
  
[Calculate elapsed work time](https://exceljet.net/formulas/calculate-number-of-hours-between-two-times)

### More Excel formulas and functions

If you want to master more Excel formulas and functions, we have some good resources for you:

1.  [Excel functions for the minimalist](https://exceljet.net/functions)
    
2.  [500 Excel formula examples](https://exceljet.net/formulas)
    
3.  [Excel formula training with practice worksheets](https://exceljet.net/training/core-formula)
    

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Top 10 reasons to learn Excel formulas](https://exceljet.net/articles/top-10-reasons-to-learn-excel-formulas)
    

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