# Excel's RACON functions | Exceljet

**Source:** https://exceljet.net/articles/excels-racon-functions

---

[Skip to main content](https://exceljet.net/articles/excels-racon-functions#main-content)

[](https://exceljet.net/articles/excels-racon-functions#)

*   [Previous](https://exceljet.net/articles/what-is-an-array-formula)
    
*   [Next](https://exceljet.net/articles/download-coronavirus-data-to-excel)
    

Excel's RACON functions
=======================

by Dave Bruns · Updated 12 Oct 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/6020/download?token=aCdpY35R)
 (22.42 KB)

![Excel's RACON functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/RACON.jpeg)

Summary
-------

There are eight widely used functions in Excel that use a syntax different from other functions in Excel. This syntax can make these functions more challenging to use, because it is not intuitive.  Read on for important information about COUNTIF, COUNTIFS, SUMIF, SUMIFS,  AVERAGEIF, AVERAGEIFS, MINIFS, and MAXIFS.

There are eight functions in Excel that work differently than you might realize. I call these "range-based conditional functions" or RACON (Ray-con) functions for short, because these functions apply criteria to a range and return a _single_ result based on supplied criteria. In other words, these functions perform _range-based_, _conditional aggregation._ Here is the list of RACON functions:

| Function | Purpose |
| --- | --- |
| [AVERAGEIF](https://exceljet.net/functions/averageif-function) | Conditional average with one condition |
| [AVERAGEIFS](https://exceljet.net/functions/averageifs-function) | Conditional average with one or more conditions |
| [COUNTIF](https://exceljet.net/functions/countif-function) | Conditional count with one condition |
| [COUNTIFS](https://exceljet.net/functions/countifs-function) | Conditional count with one or more conditions |
| [MINIFS](https://exceljet.net/functions/minifs-function) | Conditional minimum with one or more conditions |
| [MAXIFS](https://exceljet.net/functions/maxifs-function) | Conditional maximum with one or more conditions |
| [SUMIF](https://exceljet.net/functions/sumif-function) | Conditional sum with one condition |
| [SUMIFS](https://exceljet.net/functions/sumifs-function) | Conditional sum with one or more conditions |

Click any function above for details and _many_ examples.

> Other Excel MVPs I know refer to this same group of functions as the \*IFS functions.

### What's different?

Although these functions are widely used, they operate differently in three key ways you may not have noticed:

1.  [Logical expressions are split](https://exceljet.net/articles/excels-racon-functions#logical_expressions_split)
     into two parts
2.  [Ranges are _required_](https://exceljet.net/articles/excels-racon-functions#range_required)
    , you can't substitute arrays
3.  [Other miscellaneous quirks](https://exceljet.net/articles/excels-racon-functions#other_quirks)
    

In the article below, I explain these differences in some detail.

Once you understand how these functions work, you can more easily get them to do what you want. In addition, you'll have a better idea about when you should explore alternatives.

_Note: although the examples below deal exclusively with the COUNTIFS function, the same differences apply to all functions in the table above._

### Logical expressions are split

A key difference in these functions versus others is that they apply criteria in a special way, by separating the logical expressions into two parts: range and criteria. For example, the basic syntax for COUNTIFS looks like this:

    =COUNTIFS(range,criteria,range,criteria,etc)
    

I assume this was done for ease and convenience, to somehow make it "easier" to enter formula criteria without really understanding how to enter criteria as an expression, but it has consequences. For example, let's say you want to test the value in A1 and return TRUE when the value is greater than 5. With the [IF function](https://exceljet.net/functions/if-function)
 the syntax is simple:

    =IF(A1>5,TRUE)
    

Nothing special, right? The logical expression, A1>5, makes perfect sense, and we can copy it down the column to test all values:

![IF example - is A1 greater than 5](https://exceljet.net/sites/default/files/images/articles/inline/IF%20function%20-%20is%20A1%20greater%20than%205.png "IF example - is A1 greater than 5")

> Note: I am embedding the expression A1>5 in the IF function only to illustrate how a logical expression would typically appear _inside_ another function. The expression by itself (i.e. =A1>5), will create exactly the same TRUE/FALSE result.

Now, let's say you want to _count_ values in A1:A10 greater than 5 with the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. This requires the following formula:

    =COUNTIFS(A1:A10,">5")
    

Notice anything strange about this formula? What's that text (">5") doing in there?

Isn't 5 a _numeric_ value? Yes, indeed.

This happens because the logical expression A1:A10>5 has been _split_ into two parts. The range A1:A10 is perfectly valid, so it remains unquoted, but `>5` is a partial and invalid expression. As a result, it must appear in quotes like ">5".

![COUNTIF example - count greater than 5](https://exceljet.net/sites/default/files/images/articles/inline/COUNTIF%20example%20-%20count%20greater%20than%205.png "COUNTIF example - count greater than 5")

Somewhere behind the scenes, the Excel formula engine reassembles the text into a valid expression again:

    A1:A10>5 // reassembled expression
    

Things get even weirder when we involve another cell in the criteria. For example, let's say we want to check values greater than B1. With the IF function, this is straightforward:

    =IF(A1>B1,TRUE) // simple
    

But let's say we want to _count_ values in A1:A10 that are greater than B1. Now we need to write:

    =COUNTIFS(A1:A10,">"&B1) // what the ??
    

We are counting _numeric_ values, but we need to use both [concatenation](https://exceljet.net/glossary/concatenation)
 _and_ quoted text? Yes.

But note the cell reference itself is _not_ quoted :)

![COUNTIF example - count greater than 5 with cell reference](https://exceljet.net/sites/default/files/images/articles/inline/COUNTIF%20example%20-%20count%20greater%20than%205%20cell%20reference.png "COUNTIF example - count greater than 5 with cell reference")

What about text values? Suppose we want to check if a cell equals "apple". With IF, the logic is simple:

    =IF(A1="apple",TRUE)
    

![IF example - if A1 equals "apple"](https://exceljet.net/sites/default/files/images/articles/inline/IF%20example%20-%20A1%20equals%20apple.png "IF example - if A1 equals "apple"")

Now, what if we want to _count_ cells equal to "apple"?

Both of these formulas will work:

    =COUNTIFS(A1:A10,"=apple")
    =COUNTIFS(A1:A10,"apple")
    

Basically, the "equals to" (=) operator is implied, so it's not required.

![COUNTIFS example - count cells equal to "apple"](https://exceljet.net/sites/default/files/images/articles/inline/COUNTIFS%20example%20-%20count%20cells%20equal%20to%20apple.png "COUNTIFS example - count cells equal to "apple"")

So, the logic is simpler, but quirky. In a similar way, you can count values equal _to_ 5, with either:

    =COUNTIFS(A1:A10,5) // no text
    =COUNTIFS(A1:A10,"=5") // text
    

As above, both will work.

To summarize, because RACON functions split logical expressions into two parts, they require a unique syntax:

1.  Criteria that include logical operators  must be enclosed in double quotes ("")
2.  The equals to (=)  operator can be omitted (or not)
3.  Criteria based on another cell must use [concatenation](https://exceljet.net/glossary/concatenation)
    

Let's look next at the second key difference, ranges.

### Ranges are required

A second key difference with RACON functions is range arguments.  When a RACON function asks for a range, you _must_ provide a range — you can't provide an in-memory array\*.

This may not seem like a big deal at first. After all, the data is on the worksheet, right? So why not supply a range? However, in real-life situations, this requirement has consequences.

One example is dates. Let's say you want to check dates in A1:A10 to see which ones are in June?

With the IF function, you can simply use the [MONTH function](https://exceljet.net/functions/month-function)
 like this:

    =IF(MONTH(A1)=6,TRUE) // month is 6?
    

The logic is simple: extract the month number with the MONTH function and compare the result to 6. If I put the formula in B1 and copy it down to B10, we'll get TRUE for dates in the month of June, and FALSE for all other dates:

![IF example - check month is june](https://exceljet.net/sites/default/files/images/articles/inline/IF%20example%20-%20check%20month%20is%20june.png "IF example - check month is june")

By the way, this is an example of [nesting](https://exceljet.net/glossary/nesting)
 one formula inside another.

Now, how can we _count_ the dates in A1:A10 that are in June? You might think we could use the MONTH function like we did with IF:

    =COUNTIFS(MONTH(A1:A10),6) // nope
    

Nope. While this looks perfectly reasonable, it isn't going to work. Excel won't even let you _enter_ the formula. Instead, it will throw a generic "There's a problem with this formula" error. In fact, the "problem" is that you must supply a _range_ as the first argument to COUNTIFS.

Even though the MONTH function will happily give you all 10 month numbers in an array, an array won't cut it. You _must_ supply a range.

Okay, so how can you get COUNTIFS to count dates in June? It's not pretty:

    =COUNTIFS(A1:A10,">="&DATE(2020,6,1),A1:A10,"<="&DATE(2020,6,30))
    

![COUNTIFS example - count dates in june](https://exceljet.net/sites/default/files/images/articles/inline/COUNTIFS%20example%20-%20count%20dates%20in%20june.png "COUNTIFS example - count dates in june")

We are basically using the [DATE function](https://exceljet.net/functions/date-function)
 to hardcode start and end dates into the formula and using multiple criteria. The first condition tests for dates greater than or equal to June 1, the second condition tests for dates less than or equal to June 30.

If we put the date "1-June-2020" into another cell, B1, we can make things slightly less painful by using the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 to calculate the last day in June:

    =COUNTIFS(A1:A10,">="&B1,A1:A10,"<="&EOMONTH(B1,0))
    

![COUNTIFS example - count dates in june with cell reference](https://exceljet.net/sites/default/files/images/articles/inline/COUNTIFS%20example%20-%20count%20dates%20in%20june%20cell%20ref.png "COUNTIFS example - count dates in june with cell reference")

But we still can't avoid the monkey business of concatenation. And, I should note, both of the COUNTIFS examples above are testing for dates in _June 2020_, not just June.

The problem in a nutshell is that because COUNTIFS requires a range, we lose the power to manipulate values in that range directly.

_\* To be clear,_ [_spill ranges_](https://exceljet.net/glossary/spill-range)
 _work fine in RACON functions, since they are ranges on the worksheet._

### Other quirks

RACON functions also have some other quirks, including:

1.  [They strip leading zeros](https://exceljet.net/formulas/count-numbers-with-leading-zeros)
     in text-based numbers
2.  They evaluate [certain logical expressions](https://exceljet.net/formulas/text-is-greater-than-number)
     differently
3.  They evaluate [very long numbers differently](https://exceljet.net/formulas/count-long-numbers)
    
4.  [3D references](https://exceljet.net/videos/how-to-create-3d-references)
     are not allowed for _range_ arguments

### Alternatives

Now, how can we count dates in June with a function that doesn't have these limitations? Well, before the [Dynamic Array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 arrived, [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 would be the most streamlined solution:

    =SUMPRODUCT(--(MONTH(A1:A10)=6))
    

This is an [array formula](https://exceljet.net/glossary/array-formula)
, but it does not require control + shift + enter.

In the Dynamic Array version of Excel, we can use the [SUM function](https://exceljet.net/functions/sum-function)
 in the same way:

    =SUM(--(MONTH(A1:A10)=6))
    

This _does_ require control + shift + enter in earlier versions of Excel, but in Dynamic Excel, it will just work.

Both formulas use the [double-negative trick](https://exceljet.net/glossary/double-unary)
 to change TRUE FALSE values to 1's and 0's, so they can be counted.

We can also use the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    =COUNT(FILTER(A1:A10,MONTH(A1:A10)=6))
    

This involves one more function, but notice the logic used inside FILTER to test for month is _exactly the same_.

### Consistency and the future

The beauty of the [new functions in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 is that they all use logical expressions in the _same consistent way_. Even better, dynamic arrays let you build simple array formulas with the same clean and simple syntax, no fancy keystrokes required.

Although the RACON functions are still useful and, in some slightly twisted way, "easier", many future Excel formulas will be simpler, more consistent, and easier to learn. 

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