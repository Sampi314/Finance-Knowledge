# Cool things you can do with conditional formatting | Exceljet

**Source:** https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting

---

[Skip to main content](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting#main-content)

[](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting#)

*   [Previous](https://exceljet.net/articles/5-formulas-to-highlight-dates-by-month-and-year)
    
*   [Next](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before)
    

Cool things you can do with conditional formatting
==================================================

by Dave Bruns · Updated 18 Oct 2023

![Excel conditional formatting tips](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/cool_cf_things_400.png "Excel conditional formatting tips")

Summary
-------

In this article, we look at some cool ways that you can use Excel's conditional formatting feature to quickly visualize important data.

You've heard of data visualization, right? It's the art and science of presenting data in a way so that people can "see" important information _at a glance_. Data visualization makes complex data more accessible and useful. In a world overflowing with data, it's more valuable than ever.

Excel has a great tool for visualizing data called Conditional Formatting. If you work with data in Excel (and who doesn't these days?) you'll find it incredibly useful. By creating simple rules that highlight _just the data you are interested in_, you can spot key information very quickly.

To help get you started, and to give you some inspiration, here are some cool ways that you can use Excel conditional formatting to help you understand data faster.

### Highlight duplicate or unique values

One of the handy ways you can use conditional formatting is to highlight duplicate or unique values quickly. Excel contains built-in rules to make both of these tasks easy.

For example, suppose you have this table of zip codes, and you want to highlight duplicate zip codes? With over 160 zip codes in the list, it's almost impossible for the human eye to spot duplicate codes.

![165 zip codes with some duplicates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/zips1.png?itok=fuvsiSnO "165 zip codes with some duplicates")

But using Conditional Formatting, you can just select the table and tell Excel to highlight duplicates using a built-in conditional formatting rule for duplicates:

![Built-in conditional formatting rule for flagging duplicates](https://exceljet.net/sites/default/files/images/articles/inline/zips2.png "Built-in conditional formatting rule for flagging duplicates")

With just a few clicks, here is the result:

![165 zip codes with duplicates clearly highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/zips3.png?itok=GVvAEupz "165 zip codes with duplicates clearly highlighted")

Alternately, suppose you have this table of names and you need to find only unique values (values that appear once)?

![Lots of names...which ones appear just once?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/names1.png?itok=mRSb6FrU "Lots of names...which ones appear just once?")

Good luck finding names that appear only once with just your eyes! However, using a built-in conditional formatting rule, you can find all unique names in less than 10 seconds:

![Built-in conditional formatting rule for flagging unique values](https://exceljet.net/sites/default/files/images/articles/inline/names2.png "Built-in conditional formatting rule for flagging unique values")

![Unique names clearly highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/names3.png?itok=gJeJ9FGK "Unique names clearly highlighted")

Flipping the problem yet again, what if you wanted to find all names that appear at least 5 times? By creating a rule based on a formula:

![CF formula to count duplicates that appear at least 5 times](https://exceljet.net/sites/default/files/images/articles/inline/names4.png "CF formula to count duplicates that appear at least 5 times")

You can easily highlight names that appear at least 5 times:

![Names that appear at least 5 times clearly highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/names5.png?itok=d7Y60iP8 "Names that appear at least 5 times clearly highlighted")

The formula I'm using, with a named range "names" for all names, is this:

    =COUNTIF(names,B2)>4
    

###   
Highlight top or bottom values

Suppose you have the following report, which shows monthly sales totals for the salespeople in your company:

![Sales data by month and salesperson](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/sales1.png?itok=Q3oaFYyM "Sales data by month and salesperson")

It's nice to have all the information in one place, but you'd like to quickly see the 5 top and 5 bottom sales numbers, so you know where to focus your attention.

By using two built-in conditional formatting rules:

![Top 5 and bottom 5 CF rules](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/sales2.png?itok=CNsW7g0q "Top 5 and bottom 5 CF rules")

You can flag the top 5 values in green, and the bottom 5 values in red:

![Top 5 values in green, bottom 5 values in red](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/sales3.png?itok=l0-WC1rv "Top 5 values in green, bottom 5 values in red")

> Want to learn more? See our [video course on conditional formatting](https://exceljet.net/training/conditional-formatting)
> .

### Highlighting values based on a variable input

Although Excel contains a large number of Conditional Formatting presets, the real power of Conditional Formatting comes from using formulas. Formulas allow you to create more powerful and flexible rules.

For example, suppose you want to explore a data set and highlight values above a certain value, in this case, 800?

![Ready to highlight values greater than the input cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/variable1.png?itok=3cvTw6z1 "Ready to highlight values greater than the input cell")

By creating an input cell and referring to that input cell in a formula, you can make the threshold a variable.

![CF formula compares values to named range "input"](https://exceljet.net/sites/default/files/images/articles/inline/variable2.png "CF formula compares values to named range "input"")

Here the rule highlights all values greater than 800:

![All values greater than the input (800) highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/variable3.png?itok=B-86ca5R "All values greater than the input (800) highlighted")

Here we've changed the input to 900, highlighting fewer values:

![Only values greater than 900 highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/variable4.png?itok=_lh5VN0w "Only values greater than 900 highlighted")

By making the rule variable, you create a model that lets you _interactively_ explore the data. This is a great way to add some professional polish to a worksheet, because people _love_ things that respond instantly to their actions.

### Highlight entire rows based on values in a column

There are many situations where you may want to highlight an entire row based on a value that appears in one column. To do this with conditional formatting, you'll need to use a formula and then lock the column reference as needed.

For example, let's say you want to highlight orders in this set of data that are over $100:

![Order data...which orders are over 00?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/orders1.png?itok=aHtFWSmE "Order data...which orders are over $100?")

The formula locks the column reference to test only values in column E:

![CF formula to test only values in column E](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/orders2.png?itok=8P-zCohZ "CF formula to test only values in column E")

The result:

![Rows with orders over 00 in value are highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/orders3.png?itok=ne4ji0Qb "Rows with orders over $100 in value are highlighted")

### Highlight rows based on an input cell

Building on the previous examples, here we are highlighting rows based on the value in an input cell named "owner".

![CF rule to highlight rows based on owner](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/tasks2.png?itok=nVeW3Usl "CF rule to highlight rows based on owner")

![Tasks owned by Sue are highlighted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/tasks3.png?itok=0lsInyMc "Tasks owned by Sue are highlighted")

### Build a search box

Using the same basic idea in the last example, you can actually build a search box using conditional formatting that searches multiple columns at the same time. This is a nice alternative to filtering because no data is hidden.

Video: [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

### Training

*   [Conditional Formatting](https://exceljet.net/training/conditional-formatting)
    
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