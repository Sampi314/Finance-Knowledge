# What is an array formula? | Exceljet

**Source:** https://exceljet.net/articles/what-is-an-array-formula

---

[Skip to main content](https://exceljet.net/articles/what-is-an-array-formula#main-content)

[](https://exceljet.net/articles/what-is-an-array-formula#)

*   [Previous](https://exceljet.net/articles/how-to-concatenate-in-excel)
    
*   [Next](https://exceljet.net/articles/excels-racon-functions)
    

What is an array formula?
=========================

by Dave Bruns · Updated 15 May 2024

![What is an array formula?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/what_is_an_array_formula_0.jpeg)

Summary
-------

In the world of Excel formulas, the term "array formula" is probably responsible for more confusion than just about any other concept. This is because the definition of an array formula has become mixed up with the requirement to enter some array formulas in a special way, with control + shift + enter.

### Introduction

What is an array formula anyway?

In simple terms, an _array formula_ is a formula that works with an [_array_](https://exceljet.net/glossary/array)
 of values, rather than a _single_ value. Array formulas can return a single result or multiple results.

That sounds simple enough, and indeed many array formulas are _not_ complex. However, because _some_ array formulas need to be entered in a special way, and some _don't_, array formulas live mostly in the geeky realm of super users.

In fact, in the world of Excel formulas, the term "array formula" may be responsible for more confusion than just about any other concept.

With the introduction of [Dynamic Arrays in Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, array formulas are going to become a lot more common, because they are now much easier to use and understand:

1.  No need for control + shift + enter
2.  Formulas that return multiple results will [spill](https://exceljet.net/glossary/spill)
    

### Related videos

We've been working on a new course, [Dynamic Array formulas](https://exceljet.net/training/dynamic-array-formulas)
, and these videos help explain the topics discussed below:

*   [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)
    
*   [3 basic array formula examples](https://exceljet.net/videos/3-basic-array-formulas)
    

### Basic array formula example

In the example below, we want to find the maximum change in temperature over seven days:

![Basic array formula example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/basic%20array%20formula%20example.png?itok=RXxS8-l4 "Basic array formula example")

The formula in F5 is:

    =MAX(C5:C11-D5:D11)
    

This is an array formula that returns a single result.

Working from the inside out, we first subtract the low temps from high temps:

    C5:C11-D5:D11 // array operation
    

Each range contains 7 values, which we can expand into arrays like this:

    {86;84;89;87;82;85;88}-{69;65;57;62;70;59;59}
    

This is called an [array operation](https://exceljet.net/glossary/array-operation)
. We are working with multiple values, and the result after subtraction is a _new array_ with 7 values, where each value represents the change in temperature on the given day:

    {17;19;32;25;12;26;29} // new array
    

The new array is returned directly to the MAX function which returns the largest value:

    =MAX({17;19;32;25;12;26;29}) // returns 32
    

You can see that this array formula is actually quite simple!

### Traditional Excel - complication and danger

The problem arises when we enter the formula. In "Traditional Excel" (currently, every version of Excel except Office 365), this formula must be entered with [control + shift + enter](https://exceljet.net/glossary/cse)
. When entered this way, Excel will display curly braces in the formula bar like this:

    {=MAX(C5:C11-D5:D11)}
    

These curly braces tell you that Excel is handling the formula as an array formula. In other words, Excel is "letting you" work with multiple values.

To most users, that's pretty strange and confusing. But it gets worse. 

If you (or someone else) forget to enter the formula with control + shift + enter, the _same exact formula_ may return an incorrect result.

For example, the formula above _without_ control + shift + enter will return 17, the change in temperature on Monday. This will be a "silent failure" – no warning will occur. The formula will simply stop working correctly.

Obviously, formulas that return incorrect results are bad news :)

### Dynamic Excel - simplicity and clarity

The great thing about the [Dynamic Array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, is that array formulas _just work_. You don't have to use control + shift + enter with _any_ array formula.

Even better, a formula that returns multiple values will [spill](https://exceljet.net/glossary/spill)
 these values onto the worksheet. This makes array formulas much easier to understand because it's obvious when a formula is returning more than one value.

In contrast, the same formulas in previous versions of Excel will display only one result in a single cell, no matter how many values are actually returned. 

The bottom line is that working with array formulas in Excel is now easier and more intuitive than ever. You can now use array formulas whenever you like, without worrying about fancy syntax requirements.

### Videos

[What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)
  
[3 basic array formulas](https://exceljet.net/videos/3-basic-array-formulas)

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

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