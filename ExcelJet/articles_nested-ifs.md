# 19 tips for nested IF formulas | Exceljet

**Source:** https://exceljet.net/articles/nested-ifs

---

[Skip to main content](https://exceljet.net/articles/nested-ifs#main-content)

[](https://exceljet.net/articles/nested-ifs#)

*   [Previous](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Next](https://exceljet.net/articles/how-to-use-the-mod-function-to-repeat-values)
    

19 tips for nested IF formulas
==============================

by Dave Bruns · Updated 24 Oct 2023

![All about nested IFs](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/blog%20nested%20colors%20large.png "All about nested IFs")

Summary
-------

Are nested IFs evil? Are they necessary? Are there alternatives? The answer is Yes! This in-depth article explores nested IF formulas in detail, with lots of tips, and several alternatives.

The [IF function](https://exceljet.net/functions/if-function)
 is one of the most heavily used functions in Excel. IF is a simple function, and people love IF because it gives them the power to make Excel _respond_ as information is entered in a spreadsheet. With IF, you can bring your spreadsheet to life.

But one IF often leads to another, and once you combine more than a couple IFs, your formulas can start to look like little Frankensteins :)

Are nested IFs evil? Are they sometimes necessary? What are the alternatives?

Read on to learn the answers to these questions and more...

### 1\. Basic IF

Before we talk about nested IF, let's quickly review the basic IF structure:

    =IF(test,[true],[false])
    

The IF function runs a test and performs different actions depending on whether the result is true or false.

Note the square brackets...these mean the arguments are optional. However, you must supply _either_ a value for true, or a value for false.

To illustrate, here we use IF to check scores and calculate "Pass" for scores of at least 65:

![Basic IF function - return "Pass" for scores of at least 65](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/basic%20IF%201.png?itok=0S6at5nh "Basic IF function - return "Pass" for scores of at least 65")

Cell D3 in the example contains this formula:

    =IF(C3>=65,"Pass")
    

Translation: if the score in C3 is at least 65, return "Pass".

Note however that if the score is _less than_ 65, IF returns FALSE, since we didn't supply a value if false. To display "Fail" for non-passing scores, we can add "Fail" as the false argument like so:

    =IF(C3>=65,"Pass","Fail")
    

![Basic IF function - with a value added for false](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/basic%20IF%202.png?itok=yPAiwx8B "Basic IF function - with a value added for false")

Video: [How to build logical formulas](https://exceljet.net/plc/how-to-build-logical-formulas)
.

### 2\. What nesting means

Nesting simply means to combine formulas, one inside the other, so that one formula handles the result of another. For example, here's a formula where the TODAY function is nested inside the MONTH function:

    =MONTH(TODAY())
    

The TODAY function returns the current date inside of the MONTH function. The MONTH function takes that date and returns the current month. Even moderately complex formulas use nesting frequently, so you'll see nesting everywhere in more complex formulas. 

### 3\. A simple nested IF

A nested IF is just two more IF statements in a formula, where one IF statement appears inside the other.

To illustrate, below I've extended the original pass/fail formula above to handle "incomplete" results by adding an IF function, and nesting one IF inside the other:

![A basic nested IF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/basic%20nested%20IF.png?itok=iF27sfde "A basic nested IF")

    =IF(C3="","Incomplete",IF(C3>=65,"Pass","Fail"))
    

The outer IF runs first and tests to see if C3 is blank. If so, outer IF returns "Incomplete", and the inner IF never runs.

If the score is _not blank_, the outer IF returns FALSE, and the original IF function is run.

> Learn nested IFs with [clear, concise video training](https://exceljet.net/training/core-formula)
> .

### 4\. A nested IF for scales

You'll often see nested IFs set up to handle "scales"...for example, to assign grades, shipping costs, tax rates, or other values that vary on a scale with a numerical input. As long as there aren't too many levels in the scale, nested IFs work fine here, but you must keep the formula organized, or it becomes difficult to read.

The trick is to decide a direction (high to low, or low to high), then structure the conditions accordingly. For example, to assign grades in a "low to high" order, we can represent the solution needed in the following table. Note there is no condition for "A", because once we've run through all the other conditions, we know the score must be greater than 95, and therefore an "A".

|     |     |     |
| --- | --- | --- |
| Score | Grade | Condition |
| 0-63 | F   | <64 |
| 64-72 | D   | <73 |
| 73-84 | C   | <85 |
| 85-94 | B   | <95 |
| 95-100 | A   |     |

With the conditions clearly understood, we can enter the first IF statement:

    =IF(C5<64,"F")
    

This takes care of "F". Now, to handle "D", we need to add another condition:

    =IF(C5<64,"F",IF(C5<73,"D"))
    

Note that I simply dropped another IF into the first IF for the "false" result. To extend the formula to handle "C", we repeat the process:

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C")))
    

We continue on this way until we reach the last grade. Then, instead of adding another IF, just add the final grade for false.

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C",IF(C5<95,"B","A"))))
    

Here is the final nested IF formula in action:

![Completed nested IF example for calculating grades](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/nested%20IF%20grades.png?itok=Ep4_uCPs "Completed nested IF example for calculating grades")

Video: [How to make a nested IF to assign grades](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

### 5\. Nested IFs have a logical flow

Many formulas are solved from the inside out, because "inner" functions or expressions must be solved first for the rest of the formula to continue.  

Nested IFs have their own logical flow, where the "outer" IFs act like a gateway to "inner" IFs. This means that results from outer IFs determine whether inner IFs even run. The diagram below visualizes the logical flow of the grade formula above.

![The logical flow of a nested IF](https://exceljet.net/sites/default/files/images/articles/inline/nested%20if%20logical%20flow.png "The logical flow of a nested IF")

### 6\. Use Evaluate to watch the logical flow

On Windows, you can use the [Evaluate feature](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
 to watch Excel solve your formulas, step-by-step. This is a great way to "see" the logical flow of more complex formulas and to troubleshoot when things aren't working as you expect. The screen below shows the Evaluate window open and ready to go. Each time you click the Evaluate button, the "next step" in the formula is solved.  You can find Evaluate on the Formulas tab of the ribbon (Alt M, V).

![Using Evaluate to step through a nested IF that assigns grades](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/evaluate%20window%20grades.png?itok=Y-Ezksoo "Using Evaluate to step through a nested IF that assigns grades")

Unfortunately, the Mac version of Excel doesn't contain the Evaluate feature, but you can still use the F9 trick below.

### 7\. Use F9 to spot-check results

When you select an expression in the formula bar and press the F9 key, Excel solves just the part selected. This is a powerful way to confirm what a formula is really doing. In the screen below, I am using the screen tip windows to select different parts of the formula, then clicking F9 to see that part solved:

![Using F9 check a nested IF that assigns grades](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/F9%20in%20progress.png?itok=C2GkxJHL "Using F9 check a nested IF that assigns grades")

Use Control + Z (Command + Z) on a Mac to undo F9. You can also press Esc to exit the formula editor without any changes.

Video: [How to debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### 8\. Know your limits

Excel has limits on how deeply you can nest IF functions. Up to Excel 2007, Excel allowed up to 7 levels of nested IFs. In Excel 2007+, Excel allows up to 64 levels.

However, just because you _can_ nest a lot of IFs, it doesn't mean you _should_. Every additional level you add makes the formula more difficult to understand and troubleshoot. If you find yourself working with a nested IF more than a few levels deep, you should probably take a different approach — see the below for alternatives.

### 9\. Match parentheses like a pro

One of the challenges with nested IFs is matching or "balancing" parentheses. When parentheses aren't matched correctly, your formula is broken. Luckily, Excel provides a couple of tools to help you make sure parentheses are "balanced" while editing formulas.

First, once you have more than one set of parentheses, the parentheses are color-coded so that opening parentheses match closing parentheses. These colors are pretty darn hard to see, but they are there if you look closely:

![Formula parentheses are color-matched but hard to see](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/parentheses%20matching%20text.png?itok=ICEHJwp4 "Formula parentheses are color-matched but hard to see")

Second (and better) when you close parentheses, Excel will briefly bold the matching pair. You can also click into the formula and use the arrow key to move through parentheses, and Excel will briefly bold both parentheses when there is a matching pair. If there is no match, you'll see no bolding.

Unfortunately, the bolding is a Windows-only feature. If you're using Excel on a Mac to edit complex formulas, it sometimes makes sense to copy and paste the formula into a good text editor ([Text Wrangler](http://www.barebones.com/products/textwrangler/)
 is free and excellent) to get better parentheses-matching tools. Text Wrangler will flash when parentheses are matched, and you can use Command + B to select all text contained by parentheses. You can paste the formula back into Excel after you've straightened things out.

### 10\. Use the screen tip window to navigate and select

When it comes to navigating and editing nested IFs, the function screen tip is your best friend. With it, you can navigate and precisely select all arguments in a nested IF:

![Navigate and select formula arguments with the screen tip](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/screen%20tip%20window%20text.png?itok=O9NuFAd0 "Navigate and select formula arguments with the screen tip")

You can see me use the screen tip window a lot in this video: [How to build a nested IF](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)
.

### 11\. Take care with text and numbers

Just as a quick reminder, when working with the IF function, take care that you a properly handling numbers and text. For example, I often see formulas like this:

    =IF(A1="100","Pass","Fail")
    

Is the test score in A1 _really_ text and not a number? No? Then don't use quotes around the number. Otherwise, the logical test will _never_ return FALSE even when the value is a passing score, because "100" is not the same as 100. If the test score is numeric, use this:

    =IF(A1=100,"Pass","Fail")
    

### 12\. Add line breaks to make nested IFs easy to read

When you're working with a formula that contains many levels of nested IFs, it can be tricky to keep things straight. Because Excel doesn't care about "white space" in formulas (i.e. extra spaces or line breaks), you can greatly improve the readability of nested ifs by adding line breaks.

For example, the screen below shows a nested IF that calculates a commission rate based on a sales number. Here you can see the typical nested IF structure, which is hard to decipher:

![Nested IFs without line breaks are difficult to read](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/line%20breaks%20and%20nested%20IFs%201.png?itok=dBwbnqJJ "Nested IFs without line breaks are difficult to read")

However, if I add line breaks before each "value if false", the logic of the formula jumps out clearly. Plus, the formula is easier to edit:

![Line breaks make nested IFs easier to read](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/line%20breaks%20and%20nested%20IFs%202%20text.png?itok=wVFPLk01 "Line breaks make nested IFs easier to read")

You can add line breaks on Windows with Alt + Enter, on a Mac, use Control + Option + Return.

Video: [How to make a nested IF easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
.

### 13\. Limit IFs with AND and OR

Nested IFs are powerful, but they become complicated quickly as you add more levels. One way to avoid more levels is to use IF in combination with the AND and OR functions. These functions return a simple TRUE/FALSE result that works perfectly inside IF, so you can use them to extend the logic of a single IF.

For example, in the problem below, we want to put an "x" in column D to mark rows where the color is "red" and the size is "small".

![IF with the AND function is simpler than two nested IFs](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/If%20this%20and%20that.png?itok=PfgNKW3n "IF with the AND function is simpler than two nested IFs")

We could write the formula with two nested IFs like this:

    =IF(B6="red",IF(C6="small","x",""),"")
    

However, by replacing the test with the AND function, we can simplify the formula:

    =IF(AND(B6="red",C6="small"),"x","")
    

In the same way, we can easily extend this formula with the OR function to check for red OR blue AND small:

    =IF(AND(OR(B4="red",B4="blue"),C4="small"),"x","")
    

All of this _could_ be done with nested IFs, but the formula would rapidly become more complex.

Video: [IF this OR that](https://exceljet.net/videos/if-this-or-that)

### 14\. Replace Nested IFs with VLOOKUP

When a nested IF is simply assigning values based on a single input,  it can be easily replaced with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. For example, this nested IF assigns numbers to five different colors:

    =IF(E3="red",100,IF(E3="blue",200,IF(E3="green",300,IF(E3="orange",400,500))))
    

We can easily replace it with this (much simpler) VLOOKUP:

    =VLOOKUP(E3,B3:C7,2,0)
    

![Nested IF vs VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/vlookup%20vs%20nested%20IF.png?itok=P-6k1S19 "Nested IF vs VLOOKUP")

As a bonus, VLOOKUP keeps values on the worksheet (where they can be easily changed) instead of embedding them in the formula.

Although the formula above uses exact matching, you can easily use [VLOOKUP for grades](https://exceljet.net/formulas/vlookup-calculate-grades)
 as well.

See also: [23 things to know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)

Video: [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

Video: [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### 15\. Choose CHOOSE

The CHOOSE function can provide an elegant solution when you need to map simple, consecutive numbers (1,2,3, etc.) to arbitrary values.

In the example below, CHOOSE is used to create custom weekday abbreviations:

![Nested IF vs the CHOOSE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/choose%20vs%20nestedifs.png?itok=kIqMp3T- "Nested IF vs the CHOOSE function")

Sure, you _could_ use a long and complicated nested IF to do the same thing, but please don't :)

### 16\. Use IFS instead of nested IFs

In more recent versions of Excel there is a new function you can use instead of nested IFs: the [IFS function](https://exceljet.net/functions/ifs-function)
. The IFS function provides a special structure for evaluating multiple conditions _without_ nesting:

![The IFS function - multiple conditions without nesting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/ifs%20function%20example.png?itok=fNJ4KaMk "The IFS function - multiple conditions without nesting")

The formula used above looks like this:

    =IFS(D5<60,"F",D5<70,"D",D5<80,"C",D5<90,"B",D5>=90,"A")
    

Note we have just a single pair of parentheses since all conditions are handled as separate arguments the IFS function.

### 17\. Max out

Sometimes, you can use MAX or MIN in a very clever way that avoids an IF statement. For example, suppose you have a calculation that needs to result in a positive number, or zero. In other words, if the calculation returns a negative number, you just want to show zero.

The MAX function gives you a clever way to do this without an IF anywhere in sight:

    =MAX(calculation,0)
    

This technique returns the result of the calculation if positive, and zero otherwise.

I love this construction because its _just so simple_. [See this article for a full write-up](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
.

### 18\. Trap errors with IFERROR

A classic use of IF is to trap errors and supply another result when an error is thrown, like this:

    =IF(ISERROR(formula),error_result,formula)
    

This is ugly and redundant, since same formula goes in twice, and Excel has to calculate the same result twice when there is no error.

In Excel 2007, the IFERROR function was introduced, which lets you trap errors much more elegantly:

    =IFERROR(formula,error_result)
    

Now when the formula throws an error, IFERROR simply returns the value you provide.

### 19\. Use boolean logic

You can also sometimes avoid nested IFs by using what's called "boolean logic". The word boolean refers to TRUE/FALSE values. Although Excel displays the words TRUE and FALSE in cells, internally, Excel treats TRUE as 1 and FALSE as zero. You can use this fact to write clever, and very fast formulas. For example, in the VLOOKUP example above, we have a nested IF formula that looks like this:

    =IF(E3="red",100,IF(E3="blue",200,IF(E3="green",300,IF(E3="orange",400,500))))
    

Using boolean logic, you can rewrite the formula like this:

    =(E3="red")*100+(E3="blue")*200+(E3="green")*300+(E3="orange")*400+(E3="purple")*500
    

Each expression performs a test, and then multiples the outcome of the test by the "value if true". Since tests return either TRUE or FALSE (1 or 0), the FALSE results effectively cancel themselves out of the formula.

For numeric results, boolean logic is simple and extremely fast, since there is no branching. On the downside, boolean logic can be confusing to people who aren't used to seeing it. Still, it's a great technique to know about.

Video: [How to use boolean logic in Excel formulas](https://exceljet.net/videos/intro-to-boolean-logic)

### When do you need a nested IF?

With all these options for avoiding nested IFs, you might wonder when it makes sense to use a nested IF?

I think nested IFs make sense when you need to evaluate _several different inputs_ to make a decision.

For example, suppose you want to calculate an invoice status of "Paid", "Open", "Overdue", etc. This requires that you look at the invoice age _and_ outstanding balance:

![Calculating invoice status with a nested IF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/invoice%20status%20with%20nested%20if.png?itok=rPWR_dKB "Calculating invoice status with a nested IF")

In this case, a nested IF is a perfectly fine solution.

### Your thoughts?

What about you? Are you an IF-ster? Do you avoid nested IFs? Are nested IFs evil? Share your thoughts below.

> Learn Excel formulas quickly with [concise video training](https://exceljet.net/training/core-formula)
> .

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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