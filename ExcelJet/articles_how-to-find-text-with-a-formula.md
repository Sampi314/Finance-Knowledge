# How to find text with a formula | Exceljet

**Source:** https://exceljet.net/articles/how-to-find-text-with-a-formula

---

[Skip to main content](https://exceljet.net/articles/how-to-find-text-with-a-formula#main-content)

[](https://exceljet.net/articles/how-to-find-text-with-a-formula#)

*   [Previous](https://exceljet.net/articles/how-to-set-a-default-template-in-excel)
    
*   [Next](https://exceljet.net/articles/excel-shortcuts-on-the-mac)
    

How to find text with a formula
===============================

by Dave Bruns · Updated 22 Oct 2023

![Formulas for finding text in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/find%20text%20formula2.png "Formulas for finding text in Excel")

Summary
-------

Does cell A1 contain "apple"? This is a surprisingly tricky problem in Excel. In this article, we look at several options, based on the functions FIND, SEARCH, ISNUMBER, and COUNTIF.

Question: What formula tells you if A1 _contains_ the text "apple"?

This is a surprisingly tricky problem in Excel. The "obvious" answer is to use the [FIND function](https://exceljet.net/functions/find-function)
 to "look" for the text, like this:

    =FIND("apple",A1)
    

Then, if you want a TRUE/FALSE result, add the [IF function](https://exceljet.net/functions/if-function)
:

    =IF(FIND("apple",A1),TRUE)
    

This works great if "apple" is found – FIND returns a number to indicate the position, and IF calls it good and returns TRUE.

But FIND has an annoying quirk – if it _doesn't_ find "apple", it returns the #VALUE error.  This means that the formula above doesn't return FALSE when text isn't found, it returns #VALUE:

![Finding text with the FIND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20text%20with%20find.png?itok=M5cjQiU1 "Finding text with the FIND function")  
_FIND returns the position of the text (if found), but #VALUE if not found._

![Finding text with the FIND function with IF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20text%20with%20find2.png?itok=_ugmjoPs "Finding text with the FIND function with IF function")  
_Unfortunately, this error appears even if we wrap the FIND function in the IF function._

Grrrr. Nobody likes to see errors in their spreadsheets.

(There may be some good reason for this, but returning zero would be much nicer.)

What about the [SEARCH function](https://exceljet.net/functions/search-function)
, which also locates the position of text? Unlike FIND, SEARCH supports wildcards, and is not case-sensitive. Maybe SEARCH returns FALSE or zero if the text isn't found?  
  
Nope. SEARCH also returns #VALUE when the text isn't found.

So, what to do? Well, in a classic, counter-intuitive Excel move, you can trap the #VALUE error with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, like this:

    =ISNUMBER(FIND("apple",A1))
    

Now ISNUMBER returns TRUE when FIND yields a number, and FALSE when FIND throws the error.

![Trapping the #VALUE error with the ISNUMBER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20text%20with%20find%20and%20isnumber.png?itok=JMIWW3CX "Trapping the #VALUE error with the ISNUMBER function")

### Another way with COUNTIF

If all that seems a little crazy, you can also the [COUNTIF function](https://exceljet.net/functions/isnumber-function)
 to find text:

    =COUNTIF(A1,"*apple*")
    

It might seem strange to use COUNTIF like this, since we're just counting one cell. But COUNTIF does the job well – if "apple" is found, it returns 1, if not, it returns zero.

![Finding text with COUNTIF and wildcards](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20text%20with%20countif.png?itok=suQDNzQ6 "Finding text with COUNTIF and wildcards")

For many situations (e.g. conditional formatting) a 1 or 0 result will be just fine. But if you want to force a TRUE/FALSE result, just wrap with IF:

    =IF(COUNTIF(A1,"*apple*"),TRUE)
    

Now we get TRUE if "apple" is found, FALSE if not:

![Finding text with COUNTIF plus IF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20text%20with%20countif%20with%20If.png?itok=y_RAu3ww "Finding text with COUNTIF plus IF")

Note that COUNTIF supports wildcards – in fact, you _must_ use wildcards to get the "contains" behavior, by adding an asterisk to either side of the text you're looking for. On the downside, COUNTIF isn't case-sensitive, so you'll need to use FIND if case is important.

### Other examples

So what can you do with these kind of formulas? A lot!

Here are a few examples (with full explanations) to inspire you:

*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Sum cells that contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Test a cell to see if contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Highlight cells that contain specific text](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Build a search box to highlight data](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
     (video)

### Logical confusion?

If you need to brush up on how logical formulas work, [see this video](https://exceljet.net/plc/how-to-build-logical-formulas)
. It's kind of boring, but it runs through a lot of examples.

### Other formulas

If you like formulas (who doesn't?!), [we maintain a big list of examples](https://exceljet.net/formulas)
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