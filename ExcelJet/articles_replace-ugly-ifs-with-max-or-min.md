# Replace ugly IFs with MAX or MIN | Exceljet

**Source:** https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min

---

[Skip to main content](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min#main-content)

[](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min#)

*   [Previous](https://exceljet.net/articles/named-ranges)
    
*   [Next](https://exceljet.net/articles/conditional-formatting-with-formulas)
    

Replace ugly IFs with MAX or MIN
================================

by Dave Bruns · Updated 4 Oct 2023

![Replace IF with MAX or MIN](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/replace%20if%20with%20max%20or%20min.png "Replace IF with MAX or MIN")

Summary
-------

In this article, we show you how to replace a complicated IF statement with a clever and compact formula based on MIN or MAX. This is a great tip any time you need to choose the smaller or greater of two values inside a formula.

In this article, I want to show you how you can sometimes replace a more complicated IF formula with a more elegant MIN or MAX formula. This is a very simple tip that really demonstrates how you can leverage Excel's formulas to create clever and compact solutions to everyday problems. To illustrate, let's look at two examples.

### A free lunch with MAX

Let's say you have a $50 credit at a restaurant. It's a one-time use credit that expires tomorrow, so you take your friend to dinner today. You split a salad, a pizza, and a couple of beers. When it comes time to apply the credit to the bill, you might calculate the balance like this:

    balance= total-credit
    

Simple formula. But what happens when the credit is greater than the total?

If that happens, you'll see a negative balance:

![Balance is negative when credit > total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/calculate%20discount%20negative%20balance.png?itok=qLvWs5_J "Balance is negative when credit > total")

A negative balance doesn't make sense in this case, so you reach for the handy IF function:

    balance=IF(total-credit>0,total-credit,0)
    

![Typical IF formula to trap a negative balance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/calculate%20balance%20with%20IF.png?itok=ZwdAd-xA "Typical IF formula to trap a negative balance")

Problem solved. The IF function now catches negative results and returns zero instead.

This works, but the approach is ugly and redundant. The IF function is only there to trap negative results, and it forces you to repeat the main operation twice. There must be a more direct approach?

Yes, indeed, with the MAX function.

### MAX instead of IF

You might not think of the MAX function in a situation like this, because it seems geared toward large sets of data. That's true, but MAX works equally well with small, even tiny, sets of data. 

Consider that you want the formula to return the greater of two things: the calculated balance, or zero. That means you can write a formula like this:

    =MAX(total-credit, 0)
    

![MAX returns a positive balance, or zero](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/calculate%20balance%20with%20MAX.png?itok=ZIrvUkrC "MAX returns a positive balance, or zero")

Now MAX simply returns the greater of the two options — a positive balance or zero. Negative values are banished and never make it to the final result.

Pretty cool, huh?

### A capped fee with MIN

You can use the MIN function in the same way. For example, assume you need to calculate an association fee of 1.5%, up to a maximum of $3,000.  In other words, use 1.5% to calculate the fee, but cap the result at $3,000.

You could of course use IF like this:

    =IF(1.5%*amount>3000,3000,1.5%*amount)
    

![Using the IF function to calculate a capped fee](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/calculate%20capped%20fee%20with%20IF_0.png?itok=FOLgpkCf "Using the IF function to calculate a capped fee")

However, with the MIN function, you can write a compact formula that fully captures the requirement:

    =MIN(1.5%*amount,3000)
    

![Using the MIN function to calculate a capped fee](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/calculate%20capped%20fee%20with%20MIN.png?itok=GY6BAxm5 "Using the MIN function to calculate a capped fee")

Now any fee under $3000 is returned as calculated, but the total fee is never greater than $3000.

### More examples

Here are a couple more examples of using MAX or MIN to replace IF:

*   [Force negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)
    
*   [Cap percentage at a specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    

### More formulas

Like so many things in Excel, the trick to learning more formulas is more exposure. To help you out, we maintain a [large collection of sample formulas](https://exceljet.net/formulas)
 you can browse and study. This is a great way to find specific solutions to many problems you're likely to encounter in Excel. We also have a [good library of video courses](https://exceljet.net/training)
 to help you learn quickly in a more structured environment.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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