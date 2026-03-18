# Test conditional formatting with dummy formulas | Exceljet

**Source:** https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas

---

[Skip to main content](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas#main-content)

[](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas#)

*   [Previous](https://exceljet.net/articles/danger-beware-vlookup-defaults)
    
*   [Next](https://exceljet.net/articles/5-formulas-to-highlight-dates-by-month-and-year)
    

Test conditional formatting with dummy formulas
===============================================

by Dave Bruns · Updated 18 Jun 2024

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/2430/download?token=16cxho0M)
 (9.73 KB)

![How to test conditional formatting with dummy formulas](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Test_conditonal_formatting_with_dummy_formulas.png "How to test conditional formatting with dummy formulas")

Summary
-------

If you've ever tried to apply conditional formatting with a formula, you know the hardest part is making sure the formula actually works. Here's an easy way to test the formula, before you use it in a rule.

Quick Links
-----------

*   [Quick Start](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Examples](https://exceljet.net/conditional-formatting-formulas)
    
*   [Troubleshooting](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Training](https://exceljet.net/training/conditional-formatting)
    

If you've ever applied conditional formatting with your own formula, you know the hardest part is making sure the formula actually works.

The problem is that the formula area in a conditional formatting rule isn't very friendly. You don't get highlighted cell references, you don't get function autocomplete...heck....you don't even get screen tips.

As a result, it's hard to "see" if a formula is going to work until after you save the rule. If it doesn't, you have to use trial and error:

1.  Edit the rule
2.  Edit the formula using your "best guess"
3.  Save the rule to see what happens
4.  Repeat as needed

This isn't much fun, and it can be really frustrating when you run into a tricky problem.

Luckily, there's an easy fix: _dummy formulas._

### A better way - test with dummy formulas

With more complicated conditional formatting formulas, the key is to test the rule with "dummy" formulas first, before you create the rule. This may at first seem impossible — how can you test a conditional formatting formula without applying a conditional format?

The trick is understanding that you can think of conditional formatting as an "overlay" of invisible formulas that sit on top of the cells. When a formula in the overlay returns TRUE for a given cell, the formatting is applied.

So, to test a conditional formatting rule, you just need to build a set of "dummy" formulas on the worksheet that simulates the overlay.

I like to put the test formulas over to the side of the data, lined up with the rows. This makes it easy to set up and match references.

Then, simply write the first formula by referencing the upper left cell in the data. This will be the active cell when the conditional formatting rule is created.

> Video: [Test conditional formatting with dummy formulas](https://exceljet.net/videos/how-to-test-conditional-formatting-with-dummy-formula)

### Example 1 - Simple Formula

For example, say you have numbers in a table, and you want to highlight values over 100.

_Note: Excel contains a conditional formatting "preset" that will highlight values "greater than", so it's not necessary to use a formula to do this. We are just using a basic formula as an example._

![Problem - highlight values over 100 with a conditional formatting rule](https://exceljet.net/sites/default/files/images/articles/inline/CF_example1_start.png "Problem - highlight values over 100 with a conditional formatting rule")

We have plenty of space to the right, so we'll add our dummy formulas there. In cell H4, add the first formula. In this case, we want to use:

    =B4>100
    

Why B4? Because B4 corresponds to the active cell we'll have when we define the actual conditional formatting rule.

Now copy the formula across and down. You only need to copy down as many rows as you want to test. In this case, with a small set of data, we can easily test all rows.

![Copy formulas across and down](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example1_formula_copy.png?itok=pea3BIum "Copy formulas across and down")

Notice we get a TRUE or FALSE value in every cell. If we check a few references, you can see that each formula is evaluating a cell in the data, relative to B4. All references to B4 have changed, since B4 was entered as a relative address.

![Checking formula references](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example1_formula_ref_check.png?itok=8q84oNT8 "Checking formula references")

_Checking references - each formula refers to a cell relative to B4_

Now simply imagine these results transposed directly on top of the data. Wherever you see a TRUE value, the conditional formatting will be applied:

![Dummy formulas show TRUE where formatting will be applied](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example1_formula_overlay.png?itok=BSTRlPNw "Dummy formulas show TRUE where formatting will be applied")  
_Notice that TRUE values are correctly marking the values > 100 in the data (manually highlighted)_

The dummy formula looks good, so let's try it out in a conditional formatting rule.

First, copy the formula in the upper left cell of the dummy formulas – that's H4 in this case.

![Copy the first formula in the dummy set](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example1_formula_copy%20H4.png?itok=p45dsU7e "Copy the first formula in the dummy set")

Next, select the data and define a new conditional formatting rule.

![Select the data and start a new conditional formatting rule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example1_data_select.png?itok=vpLZIFhu "Select the data and start a new conditional formatting rule")

_Data selected - note the active cell is B4_

Paste the formula into the box, and set the format.

![Dummy formula pasted, rule ready to save](https://exceljet.net/sites/default/files/images/articles/inline/CF_example1_new_rule2.png "Dummy formula pasted, rule ready to save")

_Ready to save the new rule_

Success! All cells with values over 100 highlighted:

![Final conditional format, with dummy formulas removed](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example1_done.png?itok=whV_6FD4 "Final condtional format, with dummy formulas removed")

_Final conditional formatting applied with a formula, with dummy formulas removed._

### Example 2 - a more complicated formula

That was a simple example, so let's try the same approach with a more complicated formula.

Let's create a rule that highlights rows in a table based on the value in one column. In this case, we'll highlight tasks with a priority of "A".

![Problem - highlight tasks with a priority of "A"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example2_start.png?itok=QqFucNzj "Problem - highlight tasks with a priority of "A"")

_Need to highlight all rows with a priority of "A"_

This is a classic problem in conditional formatting. The formula will require a mixed reference, but mixed references can be hard to understand when you aren't able to see references on the worksheet. However, by using dummy formulas, we can easily test and perfect a rule.

As before, the first step is to figure out where to put the test formulas. We have plenty of room to the right, so we'll start in cell G5.

Since we want to highlight tasks with a priority of "A", we'll use this formula to start:

    =B5="A"
    

After I copy the formulas across and down, this is what we have:

![Dummy formulas - first try](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example2_dummy_first_try.png?itok=lDAjiAGj "Dummy formulas - first try")

_Not going to work - only values in column B will be highlighted (orange shading manually applied)_

Notice that we are getting a result of TRUE where the priority is "A", but only for values in column B. It's a good start, but it will only highlight cells in the first column.

We need to adjust the formula so that it returns TRUE for the entire row. To do this, we need to use a mixed reference in the formula to lock the column. The revised formula is:

    =$B5="A"
    

When I copy this new formula across our test range, we get what we need:

![Dummy formulas - second try - works!](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example2_dummy_second_try.png?itok=_FHqM6M9 "Dummy formulas - second try - works!")

_With the column locked, we get an entire row of TRUE's when the priority is "A" (orange shading manually applied)_

See how the dummy formulas will work? Imagine them as an overlay on the data itself.

Now let's created the conditional formatting rule. First, select the data:

![Data selected - note active cell is B5](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example2_data_selected.png?itok=zfzt1r0g "Data selected - note active cell is B5")

_Data selected, and ready to create new rule (note active cell is B5)_

Finally, let's create the rule, using the formula in the upper left:

![Formula pasted, new rule ready to save](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example2_new_rule.png?itok=m3fM_-y- "Formula pasted, new rule ready to save")

_Formula pasted from G5_

As you can see, the new rule works perfectly the first time.

![Final format - rows highlighted, dummy formulas removed](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/CF_example2_done.png?itok=cwfemayv "Final format - rows highlighted, dummy formulas removed")

_Conditional formatting working as expected (dummy formulas removed)_

### Conclusion

The next time you need to apply conditional formatting with a more complicated formula, set up dummy formulas next to the data, and fine tune the formula until you get TRUE values where you need them. By working directly on the worksheet, you have full access to all of Excel's formula tools, and you can easily troubleshoot and adjust the formula until it works perfectly.

> [See more conditional formatting formulas here](https://exceljet.net/conditional-formatting-formulas)

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    

### Training

*   [Conditional Formatting](https://exceljet.net/training/conditional-formatting)
    

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