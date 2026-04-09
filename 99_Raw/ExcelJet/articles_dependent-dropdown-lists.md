# How to make dependent dropdown lists in Excel | Exceljet

**Source:** https://exceljet.net/articles/dependent-dropdown-lists

---

[Skip to main content](https://exceljet.net/articles/dependent-dropdown-lists#main-content)

[](https://exceljet.net/articles/dependent-dropdown-lists#)

*   [Previous](https://exceljet.net/articles/custom-number-formats)
    
*   [Next](https://exceljet.net/articles/excel-data-validation-guide)
    

How to make dependent dropdown lists in Excel
=============================================

by Dave Bruns · Updated 22 Nov 2022

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/3991/download?token=AkkyTJp1)
 (9.37 KB)

![How to make dependent dropdown lists](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/dependent_dropdown_list_example.png "How to make dependent dropdown lists")

Summary
-------

One of the most useful features of data validation is the ability to create a dropdown list that let users select a value from a predefined list. But how can you make one dropdown dynamically respond to another? In other words, how can you make the values in a dropdown list depend on another value in the worksheet? Read on to see how to create dependent dropdown lists in Excel.

Quick Links
-----------

*   [Overview](https://exceljet.net/articles/excel-data-validation-guide)
    
*   [Validation Formulas](https://exceljet.net/data-validation-formulas)
    
*   [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)
    

### What is a dropdown list?

Dropdown lists allow users to select a value from a predefined list. This makes it easy for users to enter only data that meets requirements. Dropdown lists are implemented as a special kind of data validation. The screen below shows a simple example. In column E, the choices are Complete, Pending, or Cancelled, and these values are pulled automatically from the range G5:G7:

![Example dropdown list created with data validation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Example%20dropdown%20list%20created%20with%20data%20validation.png?itok=bIiFOvvc "Example dropdown list created with data validation")

Dropdown lists are easy to create and use. But once you start to use dropdown menus in your spreadsheets, you'll inevitably run into a challenge: how can you make the values in one dropdown list depend on the values in another? In other words, how can you make a dropdown list dynamic?

Here are some examples:

*   a list of cities that depends on the selected country
*   a list of flavors that depends on type of ice cream
*   a list of models that depends on manufacturer
*   a list of foods that depends on category

These kind of lists are called _dependent dropdowns_, since the list depends on another value. They are created with data validation, using a custom formula based on the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 and [named ranges](https://exceljet.net/glossary/named-range)
. This may sound complicated, but it is actually very simple, and a great example of how INDIRECT can be used.

Read on to see how to create dependent dropdown lists in Excel.

### Dependent dropdown example

In the example shown below, column B provides a dropdown menu for food Category, and column C provides options in the chosen category. If the user selects "Fruit", they see a list of fruits, if they select "Nut", they see a list of nuts, and if they select "Vegetable", they see a list of vegetables.

![regular dropdown list with horizontal range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/regular%20dropdown%20list%20with%20horizontal%20range.png?itok=ACbAALoO "regular dropdown list with horizontal range")

![dependent dropdown list with custom formula and INDIRECT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dependent%20dropdown%20list%20with%20custom%20formula%20and%20INDIRECT.png?itok=8NavVSJw "dependent dropdown list with custom formula and INDIRECT")

The data validation in column B uses this custom formula:

    =category
    

And the data validation in column C uses this custom formula:

    =INDIRECT(B5)
    

Where the worksheet contains the following named ranges:

_category = E4:G4  
vegetable = F5:F10  
nut = G5:G9  
fruit = E5:E11_

### How this works

The key to this technique is [named ranges](https://exceljet.net/glossary/named-range)
 + the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. INDIRECT accepts text values and tries to evaluate them as cell references. For example, INDIRECT will take the text "A1" and turn it into an actual reference:

    =INDIRECT("A1")
    =A1
    

Similarly, INDIRECT will convert the text "A1:A10" into the range A1:A10 inside another function:

    =SUM(INDIRECT("A1:A10")
    =SUM(A1:A10)
    

At first glance, you might find this construction annoying, or even pointless. Why complicate a nice simple formula with INDIRECT?

Rest assured, there is a method to the madness :)

The beauty of INDIRECT is that it lets you use text _exactly like a cell reference_. This provides two key benefits:

1.  You can assemble a text reference inside a formula, which is handy for [certain kinds of dynamic references](https://exceljet.net/formulas/dynamic-worksheet-reference)
    .
2.  You can pick up text values on a worksheet, and use them like a cell reference in a formula.

In the example on this page, we're combining the latter idea with named ranges to build dependent dropdown lists. INDIRECT maps text to a named range, which is then resolved to a valid reference. So, in this example, we're picking up the text values in column B, and using INDIRECT to convert them to cell references by matching existing named ranges, like this:

    =INDIRECT(B6)
    =INDIRECT("nut")
    =G5:G9
    

B6 resolves to the text "nut" which resolves to the range G5:G9.

### How to set up dependent dropdown lists

This section describes how to set up the dependent dropdown lists shown in the example.

1\. Create the lists you need. In the example, create a list of fruits, nuts, and vegetables in a worksheet.

![create the lists needed for data validation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create%20the%20lists%20needed%20for%20data%20validation.png?itok=FbKXw4Oe "create the lists needed for data validation")

2. Create [named ranges](https://exceljet.net/glossary/named-range)
 for each list: category = E4:G4, vegetable = F5:F10, nut = G5:G9, and fruit = E5:E11.

![create the named ranges needed for data validation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/create%20the%20named%20ranges%20needed%20for%20data%20validation.png?itok=1f-v7Rwt "create the named ranges needed for data validation")

> _Important: the column headings in E4, F4, and G4 must match the last three named ranges above ("vegetable", "nut", and "fruit"). In other words, you must make sure that the [named ranges](https://exceljet.net/glossary/named-range)
>  you created match the values in the Category dropdown list._

3\. Create and test a data validation rule to provide a dropdown list for Category using the following custom formula:

    =category
    

![data validation rule for category](https://exceljet.net/sites/default/files/images/articles/inline/data%20validation%20rule%20for%20category.png "data validation rule for category")

_Note: just to be clear, the named range "category" is used for readability and convenience only – using a named range here is not required. Also note data validation with a list works fine with both horizontal and vertical ranges – both will be presented as a vertical dropdown menu._

4\. Create a data validation rule for the dependent dropdown list with a custom formula based on the INDIRECT function:

    =INDIRECT(B5)
    

![data validation rule for food dropdown](https://exceljet.net/sites/default/files/images/articles/inline/data%20validation%20rule%20for%20food.png "data validation rule for food dropdown")

In this formula, INDIRECT simply evaluates values in column B as references, which links them to the named ranges previously defined.

5\. Test the dropdown lists to make sure they dynamically respond to values in column B.

![testing data validation for food list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/testing%20data%20validation%20for%20food%20list.png?itok=1Wst2Fat "testing data validation for food list")

_Note: the approach we are taking here is not case-sensitive. The named range is called "nut" and the value in B6 is "Nut" but the INDIRECT function correctly resolves to the named range, even though case differs._

### Dealing with spaces

Named ranges don't allow spaces, so the usual convention is to use underscore characters instead. So, for example, if you want to create a named range for _ice cream_, you would use _ice\_cream._ This works fine, but dependent dropdown lists will break if they try to map "ice cream" to "ice\_cream". To fix this problem you can use a more robust custom formula for data validation:

     =INDIRECT(SUBSTITUTE(A1," ","_"))
    

This formula still uses INDIRECT to link the text value in A1 to a named range, but before INDIRECT runs, the SUBSTITUTE function replaces all spaces with underscores. If the text contains no spaces, SUBSTITUTE has no effect.

### Practice file

The example file is attached below – check it out to see how it works. If you want to learn the technique yourself, I'd recommend you build a file of your own. The best way to learn is by doing.

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