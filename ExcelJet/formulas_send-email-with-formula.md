# Send email with formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/send-email-with-formula

---

[Skip to main content](https://exceljet.net/formulas/send-email-with-formula#main-content)

[](https://exceljet.net/formulas/send-email-with-formula#)

*   [Previous](https://exceljet.net/formulas/search-multiple-worksheets-for-value)
    
*   [Next](https://exceljet.net/formulas/show-formula-text-with-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Send email with formula
=======================

by Dave Bruns · Updated 2 Nov 2023

Related functions 
------------------

[HYPERLINK](https://exceljet.net/functions/hyperlink-function)

![Excel formula: Send email with formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/send%20email%20with%20formula2.png "Excel formula: Send email with formula")

Summary
-------

To send an email with a formula, you can build a "mailto:" link with the [HYPERLINK function](https://exceljet.net/functions/hyperlink-function)
. In the example shown, the formula in G5 is:

    =HYPERLINK("mailto:"&C5&"?"
    &"cc="&D5
    &"&subject="&E5
    &"&body="&F5,
    "link")
    

When the link is clicked in Excel, the default email client will create a new email with the information supplied. The link text ("link") can be customized as desired.

Generic formula
---------------

    =HYPERLINK("mailto:"&email&"?"
    &"cc="&cc
    &"&subject="&subject
    &"&body="&body,
    "link text")

Explanation 
------------

In this example, the goal is to create a clickable link that will result in a ready-to-send email.

### The mailto link protocol

The [mailto link protocol](https://en.wikipedia.org/wiki/Mailto)
 allows five variables as shown in the table below:

| Variable | Purpose |
| --- | --- |
| mailto: | The primary recipient(s) |
| &cc= | The CC recipient(s) |
| &bcc= | The BCC recipient(s) |
| &subject= | The email subject text |
| &body= | The email body text |

_Notes: (1) separate multiple email addresses with commas. (2) Not all variables are required._

The variables are presented as "query string parameters", delimited with the ampersand (?) character. For example, a fully formed mailto: link in an HTML document might appear like this:

![Example mailto link](https://exceljet.net/sites/default/files/images/formulas/inline/example%20mailto%20link.png "Example mailto link")

When a user clicks the link text, a new email will open in the default email application with the variables filled in.

### Creating the link

In Excel, the [HYPERLINK function](https://exceljet.net/functions/hyperlink-function)
 can be used to create links. The basic syntax is:

    =HYPERLINK("link","link text")
    

The link itself is a text string that represents a valid link. The link text (called "friendly name" in Excel) is the text displayed to a user.

Ultimately, the goal for the formula in G5 is to build a string like this:

    mailto:aya@aa.com?cc=bb@bb.com&subject=subject&body=body
    

Because the mailto link uses several pieces of information, it must be assembled with [concatenation](https://exceljet.net/glossary/concatenation)
.

The formula is a bit tricky. While the ampersand is the [operator](https://exceljet.net/glossary/math-operators)
 for concatenation in Excel, it is also used to delimit the mailto link parameters (cc, bcc, subject, etc.). This means that some ampersands (&) are used to join text in the formula, and some are _embedded in the final result_. In the code below, the ampersands in yellow are used for concatenation in Excel. The white ampersands are embedded in the final result:

    =HYPERLINK("mailto:"&C5&"?"
        &"cc="&D5
        &"&subject="&E5
        &"&body="&F5,
        "link")
    

_Note: the formula above is [entered with line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 for better readability._

### Empty mailto parameters

For the sake of simplicity, the formula above does not try to exclude empty parameters from the final result. In quick testing with Gmail and Outlook, missing parameters seem to be ignored gracefully. The behavior in other email applications may vary.

Related functions
-----------------

[![Excel HYPERLINK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hyperlink%20function.png "Excel HYPERLINK function")](https://exceljet.net/functions/hyperlink-function)

### [HYPERLINK Function](https://exceljet.net/functions/hyperlink-function)

The Excel HYPERLINK function returns a hyperlink to a given destination. You can use HYPERLINK to create a clickable hyperlink with a formula. The HYPERLINK function can build links to workbook locations, pages on the internet, or files on network servers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [HYPERLINK Function](https://exceljet.net/functions/hyperlink-function)
    

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