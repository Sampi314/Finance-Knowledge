# How to speed up your models: Part 3

**Source:** https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3

---

How to speed up your models: Part 3
-----------------------------------

[Forvis Mazars Financial Modelling](https://financialmodelling.forvismazars.com/)
[Financial Modelling](https://financialmodelling.forvismazars.com/online-resources/blog-types/financial-modelling-blog-types/)

How to speed up your models: Part 3

[](http://twitter.com/share?text=How+to+speed+up+your+models%3A+Part+3&url=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
[](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
[](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
[](mailto:?subject=How%20to%20speed%20up%20your%20models:%20Part%203&body=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)

How to speed up your models: Part 3
===================================

By [Matthias Prosser](https://financialmodelling.forvismazars.com/author/matthias-prosser/ "Posts by Matthias Prosser")

Tuesday 6th April 2021

This article is Part 3 in the series “_How to speed up your models_”; [Part 1](https://financialmode1.wpengine.com/how-to-speed-up-your-models-part-1-2/)
 and [Part 2](https://financialmode1.wpengine.com/how-to-speed-up-your-models-part-2/)
 are available on the Forvis Mazars Financial Modelling website. This final part will focus on some commonly used Excel functionality which can slow down financial models and practical tips to minimise the impact on calculation speed while still including the desired functionality. In terms of calculation speed, sometimes what you don’t include in a model can matter just as much as what you do!

External links
--------------

In Microsoft’s own words…

> “Avoid inter-workbook links when it is possible; they can be slow, easily broken, and not always easy to find and fix.”

There’s not much more to say about external links other than to avoid using them whenever possible. If there are inputs to the model which should come from another Excel file, then these inputs should be brought in via pasting values into the model and updating when needed. This will also prevent inputs accidentally being updated via the source file and will ease the process of sharing the model between different teams and organisations who may not have access to the source file.

Note there are numerous ways an external link can unintentionally be created within a file, of which we have listed the most common types in the table below. To check if you have any external links in your workbook you can go to Data > Queries & Connections > Edit Links. If this option is greyed out the file does not have any external links.

|     |     |     |
| --- | --- | --- |
| **Type** | **Cause** | **Solution** |
| **Links in formulae** | Pasting links instead of pasting values | _Search within the entire workbook for “.x”_ |
| **Links in named ranges** | Copying in sheet(s) from other workbooks | _Open the name manager and sort the “Refers to” column to find names referring to other workbooks_ |
| **Links in chart data** | Copying in chart(s) from other workbooks | _Go to “Select data” for each chart and check if any data is being sourced from an external file_ |

Because Excel attempts to automatically update external links and notifies the user via a pop-up whenever the Excel file is opened, these unintentional links should be removed to improve both performance and the user experience.

Data tables
-----------

Data tables are a powerful way to compare outputs across scenarios or test sensitivities, but they can slow calculation speed. In modelling, they are often used to show outputs for multiple scenarios at once. However, this requires the model to recalculate every scenario each time, which impacts performance and should be avoided if speed is an issue.

If a model must use a data table, performance can be improved by setting calculation to “Automatic except for data tables.” This prevents non-active scenarios from recalculating unless triggered manually. However, this method is not always accurate, as explained below.

In models with optimisation macros (e.g. debt sizing), data tables cannot run the macro for each scenario and instead apply live case results to all scenarios, leading to incorrect outputs. Combined with performance issues, this makes data tables a poor choice for scenario output tables in project finance models. A better approach is to use a VBA macro to run each scenario, execute the optimisation, and paste the results into the output table. This produces the same result without the performance or accuracy risks.

Charts
------

You can do a lot using Excel charts however this blessing can also sometimes be a curse from a performance perspective. Sometimes modellers go over the top including too much data, excessive formatting or simply including far more charts than necessary. We provide recommendations in each of these areas below, however the key idea is to just keep it simple when it comes to charts.

### Including too much data:

If a chart has five or more data series, it’s likely too busy, combine series or remove irrelevant data. Also check data frequency: annual data often gives the same insight as monthly or quarterly but with far fewer points.

### Excessive formatting:

Fancy formatting like 3D charts or gradients slows performance and often makes charts harder to read. Keep formatting simple and avoid excess features, colours, or fonts so charts run faster and are easier to understand.

### Including too many charts:

Think carefully about your audience and what information they really need. Do not include extra charts just for the sake of it; the goal should be to make the summary page as short as possible (i.e. usually one to two A4 pages, depending on your audience). You may also want to consider replacing some charts with sparklines, which are much more economical from both a calculation and space perspective, and much faster to create.

Conditional formatting and data validation
------------------------------------------

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/04/image.png)

Conditional formatting and data validation are very useful features of Excel which we should all be utilising as appropriate, however using them a lot will significantly slow down calculation speed. Note also that conditional formatting rules which use formulae are always volatile and therefore are particularly slow. For this reason, the use of these features should be limited, especially in large models. In slow models, conditional formatting should be one of the first features to reduce. It is mainly for presentation and does not affect calculations.

Note some applications of conditional formatting can be achieved through the non-volatile number formatting functionality instead, if you understand the custom formatting notation Excel uses.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/04/imag1.png)

As a simple example, if you want to display positive numbers in green, negatives in red and zero in black you can use the following code:

_\[Green\]0; \[Red\]0; \[Black\]0_

By default, Excel defines four different types of data for formatting purposes, separated by semicolons in custom number formats. These are:

_positive values; negative vales; zero; text_

As a simple example, if you want to display positive numbers in green, negatives in red and zero in black you can use the following code:

_\[Green\]0; \[Red\]0; \[Black\]0_

By default, Excel defines four different types of data for formatting purposes, separated by semicolons in custom number formats. These are:

_positive values; negative vales; zero; text_

You can define different groupings using the custom number formats. A simple example with groupings of <100 and >=100 is shown below. Note this flexibility will allow custom number formats to replace conditional formatting in some instances.

_\[Red\]\[<100\]0; \[Blue\]\[>=100\]0_

For more on conditional formatting and custom number formats, see the further reading section below for useful resources.

Other potential issues
----------------------

Other common modelling issues can also accidentally affect performance. A number of these are explained below including recommendations on how to avoid or fix them.

### End cells:

Modellers often extend the used range far beyond what is needed, for example by formatting the far-right column or bottom row. This makes Excel save every column or row, greatly increasing file size. While it may not slow calculations, it can make opening and saving much slower and may even cause crashes.

_You can check the used range on each sheet by going to the end cell (CTRL + END). It is also advisable to check the file size periodically to see if there is an unexplained jump which might mean the used range has been expanded._

### Excessive range names:

Having excessive amounts of named ranges will slow down calculation speed because names are recalculated each time they are referenced by a formula that is recalculated. Note also that although dynamic named ranges can be very useful (created using OFFSET and COUNTA), they are volatile and therefore will impact calculation speed as well.

_Periodically check named ranges look ok and there aren’t too many of them in the name manager, (CTRL + F3)._

### Excessive cell styles:

Cell styles help maintain consistent formatting, but too many can slow your model. This often happens when copying data or sheets from other workbooks, so use them carefully.

_We recommend copying only formulae or only values for the ranges of cells needed as this won’t bring in the cell styles or formatting associated with those cells. You should also periodically cull excess cell styles from your workbook._

### Event-based VBA code and add-ins:

Excessive event-based VBA code, personal macros, or multiple add-ins can all significantly impact performance.

_You can check whether VBA is causing calculation impacts by re-opening the file and holding down SHIFT. This disables any macros in the workbook. If you notice a performance improvement you can test which macro or add-in is causing issues through a process of elimination by individually enabling/disabling each until you find the culprit(s). It is also good practice to periodically assess whether you have add-ins which you no longer use and therefore should be removed._

### Excessive grouping:

Again, we are big advocates of using grouping to present different levels of information and avoid hiding cells, however using grouping excessively may impact model performance.

_Consider how many levels of grouping are really required for your model. Typically, one to two levels will be sufficient for most cases._

Wrapping up
-----------

This concludes our series on _How to speed up your models._ If you are interested in learning more about financial modelling we have a wide range of resources on our website including [tutorials](https://financialmodelling.forvismazars.com/online-resources/tutorials/)
, [webinars](https://financialmodelling.forvismazars.com/online-resources/webinars/)
 and [blogs](https://financialmodelling.forvismazars.com/financial-modelling-resources/blogs/)
. We have also included a selection of further reading on the topics covered in this post below.

Further reading:
----------------

### External links:

*   See the “Remove Phantom Workbook Links” section of this article on [Reducing Workbook and Worksheet Frustration](https://www.oreilly.com/library/view/excel-hacks-2nd/9780596528348/ch01.html)
    
*   Data tables:
*   For an overview of how scenarios and sensitivities are used in PF models, please see our webinar on [Creating Sensitivity Tables for Infrastructure Project Analysis](https://financialmodelling.forvismazars.com/resources/sensitivity-tables-webinar/)
    . The use of a data table for scenario analysis is shown from minute 34 of the video.

### Conditional formatting:

*   [Excel: Replacing volatile conditional formatting](https://sfmagazine.com/post-entry/april-2016-excel-replacing-volatile-conditional-formatting/)
    
*   [Excel custom number formats](https://exceljet.net/custom-number-formats)
     (comprehensive explanation of Excel’s custom number formats)
*   [Custom formats builder/tester](https://customformats.com/)
    

### Charts:

*   [Speeding up & optimizing Excel – Tips for Charting & Formatting](https://chandoo.org/wp/excel-optimization-charting-formatting-tips/)
    

### Other:

*   [Excel calculation bottlenecks](http://www.decisionmodels.com/optspeedd.htm)
    

Request Prices and Discounts
----------------------------

Related posts

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2020/03/shutterstock_1403062694-1024x684.jpg)](https://financialmodelling.forvismazars.com/welcome-to-our-digital-classrooms/)

#### Digital Classrooms

Forvis Mazars – welcome to our Digital Classrooms! We are opening our Digital Classrooms to individual registrations, making our world-leading...

[Read more](https://financialmodelling.forvismazars.com/welcome-to-our-digital-classrooms/)

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2026/02/WhatsApp-Image-2026-02-12-at-10.18.58-1024x681.jpeg)](https://financialmodelling.forvismazars.com/ai-in-project-finance-blog/)

#### AI in Project Finance: New Course and Webinar

To help practitioners understand and apply AI in a practical disciplined way Forvis Mazars APAC Energy has launched two complementary...

[Read more](https://financialmodelling.forvismazars.com/ai-in-project-finance-blog/)

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-12-at-10.20.46_ff6ffcaf.jpg)](https://financialmodelling.forvismazars.com/top-5-financial-modelling-tutorials/)

#### Our Top 5 Most-Downloaded Financial Modelling Tutorials

Explore our Top 5 financial modelling tutorials — clear, practical walkthroughs of key project finance concepts like CFADS, DSCR, LLCR...

[Read more](https://financialmodelling.forvismazars.com/top-5-financial-modelling-tutorials/)

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2025/08/GettyImages-1309760275-1024x683.jpg)](https://financialmodelling.forvismazars.com/excel-copilot-function-ai-formulas/)

#### How to Use the Excel Copilot Function: AI-Powered Formulas for Smarter Data Analysis

What Is the Excel Copilot Function? The Excel Copilot function is a new AI-powered formula available in Microsoft 365. It...

[Read more](https://financialmodelling.forvismazars.com/excel-copilot-function-ai-formulas/)

*   [](mailto:?subject=How%20to%20speed%20up%20your%20models:%20Part%203&body=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
    
*   [](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
    
*   [](http://twitter.com/share?text=How+to+speed+up+your+models%3A+Part+3&url=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
    
*   [](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/)
    

*   [Legal and privacy](https://www.forvismazars.com/uk/en/contact-us/legal-and-privacy)
    

Copyright 2026 - Forvis Mazars

This website uses cookies.

Some of these cookies are necessary, while others help us analyse our traffic, serve advertising and deliver customised experiences for you. For more information on the cookies we use, please refer to our [Privacy Policy](https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-3/#)
.

Customise Settings I Accept

*    Compulsory Cookies
    
    This website cannot function properly without these cookies.
    
*    Analytical Cookies
    
    Analytical cookies help us enhance our website by collecting information on its usage.
    
*    Marketing Cookies
    
    We use marketing cookies to increase the relevancy of our advertising campaigns.
    

### Follow us

Forvis Mazars is dedicated to exceptional financial modelling. As part of our commitment to raising the bar in financial modelling, we want to ensure the financial modelling community is kept up to date with the latest events, tips, techniques and training.

By registering for email updates from Forvis Mazars you will be kept up to date about:

*   Financial modelling events
*   New tutorials
*   The latest blog posts
*   Upcoming training courses