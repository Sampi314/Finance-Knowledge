# Excel shows formula but not result | Exceljet

**Source:** https://exceljet.net/articles/excel-shows-formula-not-result

---

[Skip to main content](https://exceljet.net/articles/excel-shows-formula-not-result#main-content)

[](https://exceljet.net/articles/excel-shows-formula-not-result#)

*   [Previous](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Next](https://exceljet.net/articles/excel-tables)
    

Excel shows formula but not result
==================================

by Dave Bruns · Updated 16 Jan 2024

![Excel shows formula but not result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Excel_shows_formula_but_not_result_0.jpeg "What to do when Excel shows formulas but not results")

Summary
-------

Have you entered a formula, but Excel is not showing a result? This can be very confusing, and you might think you've somehow broken your spreadsheet. However, it's likely a simple problem. With a little troubleshooting, you can get things working again.

Every once in a while, you might find Excel behaving in a bizarre or unexpected way. One example is when you [accidentally trigger the scroll lock feature](https://exceljet.net/articles/how-to-disable-scroll-lock-in-excel)
. Another example is when one or more formulas suddenly stops working. Instead of a result, you see only a formula, as in the screen below:

![Broken formula - Excel shows formula but no result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/broken%20formula%20example2.png?itok=Zaci789D "Broken formula - Excel shows formula but no result")

_The VLOOKUP formula is correct, why no result?_

This can be very confusing, and you might think you've somehow broken your spreadsheet. However, it's likely a simple problem. With a little troubleshooting, you can get things working again. There are two main reasons you might see a formula instead of a result:

1.  You accidentally enabled Show Formulas
2.  Excel thinks your formula is text

I'll walk through each case with some examples.

Show Formulas is enabled
------------------------

Excel has a feature called Show Formulas that toggles the display of formula results and actual formulas. Show Formulas is meant to give you a quick way to see all formulas in a worksheet. However, if you accidentally trigger this mode, it can be quite disorienting. With Show Formulas enabled, columns are expanded, and every formula in a worksheet is displayed with no results anywhere in sight, as shown below.

![Show Formulas disabled](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/show%20formulas%20disabled.png?itok=yy-PjFlP "Show Formulas disabled")

_Show Formulas disabled (normal mode)_

![Show Formulas enabled](https://exceljet.net/sites/default/files/images/articles/inline/show%20formulas%20enabled.png "Show Formulas enabled")

_Show Formulas enabled_

To check if Show Formulas is turned on, visit the Formula tab in the ribbon and check the Show Formulas button:

![Show Formulas button on ribbon](https://exceljet.net/sites/default/files/images/articles/inline/show%20formulas%20button%20on%20ribbon.png "Show Formulas button on ribbon")

_Show Formulas enabled - just click to disable_

The reason Show Formulas can be accidentally enabled is because it has a [keyboard shortcut](https://exceljet.net/shortcuts/toggle-formulas-on-and-off)
 (Control +\`)  that a user might accidentally type. Try typing Control + \` in a worksheet to see how it works. You should see formulas toggled on and off each time you use the shortcut.

> [Watch a video with over 20 formula tips](https://exceljet.net/videos/23-excel-formula-tips)

Show Formulas toggles the display of _every_ formula in a worksheet. If you are having trouble with a _single_ formula, the problem isn't Show Formulas. Instead, Excel probably thinks the formula is text. Read on for more information.

Excel thinks your formula is text
---------------------------------

If Excel thinks a formula is just text and not an actual formula, it will simply display the text without trying to evaluate it as a formula. There are several situations that might cause this behavior.

### No equal sign

First, you may have forgotten the equal sign. All formulas in Excel must begin with an equal sign (=). If you leave this out, Excel will simply treat the formula as text:

![Broken formula - no equal sign](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/broken%20formula%20no%20equal%20sign2.png?itok=k6il3g8l "Broken formula - no equal sign")

_Broken formula example - no equal sign (=)_

### Space before the equal sign

A subtle variation of this problem can occur if there is one or more spaces before the equal sign. A single space can be hard to spot, but it breaks the rule that all formulas must start with an equal sign, so it will break the formula as shown below:

![Broken formula - space before equal sign](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/broken%20formula%20space%20before%20equal%20sign2.png?itok=mvQjECOG "Broken formula - space before equal sign")

### Formula wrapped in quotes

Finally, make sure the formula is not wrapped in quotes. Sometimes, when people mention a formula online, they will use quotes, like this:

    "=A1"
    

In Excel, quotes are used to signify a text value, so if you enter a formula like this, the formula _will not_ be evaluated. You can see an example of this in the screen below:

![Broken formula - formula wrapped in quotes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/broken%20formula%20formula%20in%20quotes2.png?itok=EcqZDEYt "Broken formula - formula wrapped in quotes")

_Note: you are free to use quotes inside formulas. In this case, the formula above requires quotes around criteria._ 

In all of the examples above, just edit the formula so it begins with an equal sign and all should be well:

![Broken formula fixed](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/broken%20formula%20fixed2.png?itok=XsSK1iVe "Broken formula fixed")

For reference, here is the working formula:

    =SUMIFS(D5:D9,E5:E9,">30")
    

### Cell format set to Text

Finally, every once in a while, you might see a formula that is well-formed in every way but somehow does not display a result. If you run into a formula like this, check to see if the cell format is set to Text.

![Ribbon - cell format is set to Text](https://exceljet.net/sites/default/files/images/articles/inline/ribbon%20cell%20format%20set%20to%20Text.png "Ribbon - cell format is set to Text")

If so, set the format to General (Control + ~), or another suitable number format. You may need to enter cell edit mode (click into the formula bar, or use F2, then enter) to get Excel to recognize the format change. Excel should then recognize the formula.

> After setting the format to General, you may need to enter the formula again to make Excel evaluate it properly.

### Tip - Save formula in progress as text

Although a broken formula is never fun, you can sometimes use the "formula as text problem" to your advantage, as a way to save work in progress on a tricky formula. Normally, if you try to enter a formula in an unfinished state, Excel will throw an error, stopping you from entering the formula. However, if you add a single quote before the equal sign Excel will treat the formula as text and let you enter it without complaint. The single quote reminds you that the formula has been intentionally converted to text:

![Save formula in progress](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/save%20formula%20in%20progress.png?itok=YCRm27_f "Save formula in progress")

Later, you can resume work on the formula again, starting where you left off. [See #17 in this list for more info](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
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

*   [The 54 Excel shortcuts you really should know](https://exceljet.net/articles/the-54-excel-shortcuts-you-really-should-know)
    

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