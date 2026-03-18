# Build friendly messages with concatenation | Exceljet

**Source:** https://exceljet.net/articles/build-friendly-messages-with-concatenation

---

[Skip to main content](https://exceljet.net/articles/build-friendly-messages-with-concatenation#main-content)

[](https://exceljet.net/articles/build-friendly-messages-with-concatenation#)

*   [Previous](https://exceljet.net/articles/formula-to-list-weekends-only)
    
*   [Next](https://exceljet.net/articles/the-eomonth-function-formula-friday)
    

Build friendly messages with concatenation
==========================================

by Dave Bruns · Updated 11 May 2024

![Friendly, dynamic messages with concatenation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/concatenation_message_artwork_0.jpeg "Friendly, dynamic messages with concatenation")

Summary
-------

In this article, we explain how to use concatenation to display friendly and useful messages in your spreadsheets. The messages are dynamic and respond instantly to changes, so the effect is polished and professional.

One of the many cool things about Excel is that you can use formulas to display useful, dynamic messages directly on the worksheet. Dynamic messages give your spreadsheets a nice polish. Because they respond instantly to user input, the effect is friendly and professional:

![Example of concatenation to show dynamic message](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dynamic%20message%20with%20concatenation.png?itok=2lmvCxFH "Example of concatenation to show dynamic message")

A key tool in building friendly messages is [concatenation](https://exceljet.net/glossary/concatenation)
. Concatenation sounds complicated, but it's a really simple and useful formula technique you can learn in a few minutes. You'll find many opportunities to use concatenation in your spreadsheets.

_Caution: When people see messages like this in a worksheet you built, they'll assume you're some kind of Excel genius, so be warned :)_

### A basic example

You can assemble messages with nothing more than a simple formula and a technique called "concatenation". Don't be alarmed by this fancy-sounding word. Concatenation simply means "join together". In Excel, this generally means joining text with a value from a cell, or with the result of a function. For example, with the number 10 in cell B4, you can write a formula like this:

    =B4&" apples"
    

Which displays this message: _10 apples_

![Basic concatenation example](https://exceljet.net/sites/default/files/images/articles/inline/basic%20concatenation%20example1.png "Basic concatenation example")

_Note: text is fully enclosed in double quotes, and must include required spaces._

Here, the ampersand character (&) is used to join a text string with the value in cell A1. The ampersand is the "concatenation operator" in Excel, just like the asterisk (\*) is the multiplication operator, the plus symbol (+) is the addition operator, and so on.

If a user updates cell B4 to contain 25, the message updates instantly:

![Concatenation formula updates automatically](https://exceljet.net/sites/default/files/images/articles/inline/basic%20concatenation%20example%20instant%20update.png "Concatenation formula updates automatically")

### Embedding a value in the middle

You don't have to concatenate only at the beginning or end of a text string, you can use multiple ampersands to embed values anywhere you like in a string. Taking the example above another step, you can use two ampersands to create a full sentence with a value in the middle:

    ="There are "&B4&" apples."
    

Which returns: _There are 25 apples._

![Concatenation to embed number between two text strings](https://exceljet.net/sites/default/files/images/articles/inline/basic%20concatenation%20example%20between%20text.png "Concatenation to embed number between two text strings")

_Again note: all text must be enclosed in double quotes. If you forget to do this, Excel won't let you enter the formula._

### Concatenation with other functions

Once you get the basic idea of concatenation, you'll quickly see how you can use the results of other formulas or functions in your messages. For example, perhaps you maintain data in a filtered table. You often use one or more filters to narrow down data in the table, and you'd like to know how many records you're viewing at any given time, and how many records are in the table total.

Building on the examples above, you can use concatenation, together with the row and subtotal functions to build a message like this: "Displaying x of y records". Here,  x represents the total record count, and y is the number of records currently visible, as seen below:

![Using concatenation to show number of visible items in filtered table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/concatenation%20X%20of%20y%20displayed%20message.png?itok=K1LFFU5W "Using concatenation to show number of visible items in filtered table")

The formula used is:

    ="Showing "&SUBTOTAL(103,Table1[Issue])&" of "&ROWS(Table1)&" issues"
    

Video: [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

### Concatenation with number formatting

Once you get comfortable with concatenation, you'll start to notice many opportunities to concatenate values into more meaningful messages. Then, one of the first problems you'll likely run into is losing the formatting of numeric values you include in a message.

For example, let's say you have a due date in cell C4, and you want to display a message like "The project is due August 15, 2017".

So, you start off with this formula:

    ="The project is due on "&C2
    

However, when you hit enter you see: The project is due on 42962

![Concatenation with unformatted date](https://exceljet.net/sites/default/files/images/articles/inline/concatenate%20date%20message1.png "Concatenation with unformatted date")

It's kind of cool to see the underlying value, but most people don't know that August 15, 2017 is the 42962-th day in Excel's date numbering system, so not especially useful :)

To fix this problem, use the TEXT function to apply the formatting of your choice:

![Concatenation with formatted date](https://exceljet.net/sites/default/files/images/articles/inline/concatenate%20date%20message2.png "Concatenation with formatted date")

The improved version uses this formula:

    ="The project is due on "&TEXT(C2,"ddd, mmm d, yyyy")
    

The TEXT function is a handy function you can use whenever you want to apply formatting to a numeric value and up with text. You can use it for all number formatting, including percentage, currency, dates, times, and custom formats.

The video below shows how to use the TEXT function to increment a padded number (i.e. 0001, 00123, etc.)

Video: [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

### Clarify assumptions with concatenation

Another cool use of concatenation is to make assumptions clear in a model that requires specific user inputs or variables.

This video below shows how concatenation can be used to "expose" several assumptions directly on the worksheet by concatenating variable inputs directly to calculation labels.

Video: [How to clarify assumptions with concatenation](https://exceljet.net/videos/how-to-use-concatenation-to-clarify-assumptions)

### Excel concatenation functions

Excel contains three functions you can also use for concatenation: the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
, the [CONCAT function](https://exceljet.net/functions/concat-function)
, and the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. CONCAT and TEXTJOIN are new functions available in Office 365 and Excel 2019.

I'm not a fan of CONCATENATE, since it doesn't do anything you can't do with the [regular old ampersand](https://exceljet.net/glossary/concatenation)
 (&), which is much shorter, and more flexible to boot.

But CONCAT will let you join ranges, which is a new feature, and TEXTJOIN goes one step further and lets you join ranges with a delimiter of your choice. They are worth a look if you are using a newer version of Excel. This article discusses both functions in more detail: [CONCAT and TEXTJOIN](https://exceljet.net/articles/concat-textjoin)
.

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