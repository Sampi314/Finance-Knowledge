# How to Color Code in Excel - Shortcuts for Formulas, Constants & Inputs

**Source:** https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel

---

How to Color Code in Excel for Financial Models (PC/Windows Version) \[Tutorial Video\] (32:42)
===============================================================================================

In this lesson, you’ll learn how to apply color coding and formatting to financial models and fix problems with decimals, currency signs, indentation, alignment, links vs. formulas vs. constants, and more – and you’ll practice by fixing the formatting on the Summary spreadsheet.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/#tab-signup)
    

How to Color Code in Excel for Financial Models (PC/Windows Version)

This sample lesson from our Excel/VBA course covers **how to color code in Excel** and some of the key principles for **formatting financial models.**

**Table of Contents:**

**1:06:** Formatting Principles

**11:02:** Demonstration of Walmart Model Fixes

**19:59:** Exercise – Summary Spreadsheet Fixes

**30:34:** Recap and Summary

We have some general guidelines for model formatting, but these are not like the laws of physics (gravity, momentum, speed of light, etc.) – they’re “rules of thumb” rather than “laws of nature.”

**How to Color Code in Excel: Key PC and Mac Shortcuts**
--------------------------------------------------------

We use the following colors for different types of cells:

![How to Color Code in Excel - Standards](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201021%20131'%3E%3C/svg%3E "How to Color Code in Excel - Standards")

To find and select these cells, you can use the following **PC/Windows shortcuts**:

**F5:** Jump to Cell

**F5, Alt + S, O, X:** Select Constants (Drop the X if you want to highlight text constants)

**F5, Alt + S, F, X:** Select Formulas (Drop the X to highlight textual formulas)

**Ctrl + 1:** Format Dialog Box

**Ctrl + F:** Find

For example, if you press F5, Alt + S, O, X, that will highlight all constants on the spreadsheet. You can then press Ctrl + 1 to change their font color to blue, or you can access the font color commands from the “Home” tab in the ribbon menu.

To find direct links to other spreadsheets in the file, you can press Ctrl + F and search for the “!” character, which always indicates links to other sheets.

To find links to other files, search for “.xls” using Ctrl + F, and change the font color to red for each instance.

In the **Mac version of Excel**, you can use these shortcuts instead:

**F5 or Ctrl + G:** Jump to Cell

**F5 or Ctrl + G, Special, Constants:** Select Constants (Drop the X if you want to highlight text constants)

**F5 or Ctrl + G, Special, Formulas:** Select Formulas (Drop the X to highlight textual formulas)

**⌘ + 1:** Format Dialog Box

**⌘ + F:** Find

![Excel & VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Learn Excel Shortcuts, Formulas, Graphs, Data, and VBA for Automation

*   #### Become a shortcut, formula & formatting machine
    
    Excel will be your “native language” after you finish this course
    
*   #### Learn the skills with dozens of practice exercises
    
    Learn by doing and check your work against the solutions
    
*   #### Shave hours off your workday with VBA and macros
    
    Automate repetitive tasks, format spreadsheets quickly, and more
    

[Full Details](https://breakingintowallstreet.com/excel-vba/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Excel-VBA-Course-Outline.pdf)

**How to Color Code in Excel: What Financial Models Should Look Like**
----------------------------------------------------------------------

If you follow these standards for color coding, your financial models should look like the examples below.

Here’s the normal color-coding scheme:

![How to Color Code in Excel: Green, Black, and Blue](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20255'%3E%3C/svg%3E "How to Color Code in Excel: Green, Black, and Blue")

We use a yellow background and grey border for “input cells” that are assumptions or drivers in the model, while we use a white background with no borders for historical financial data:

![How to Color Code in Excel: Assumptions and Historical Financial Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20878%20475'%3E%3C/svg%3E "How to Color Code in Excel: Assumptions and Historical Financial Data")

Here are a few other examples of cell colors based on their categories and contents:

![Color Coding by Cell Category](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20813%20275'%3E%3C/svg%3E "Color Coding by Cell Category")

**Other Principles of Financial Model Formatting**
--------------------------------------------------

In addition to the points above about color-coding, we follow these guidelines with other types of formatting:

**Centering:** We use the “Accounting” format and variations of the “Percentage” format for most numbers, so centering is not an issue there. For the input boxes, we prefer to center percentages, dates, text, and normal numbers, but we do not apply it to anything in the “Accounting” format.

**Dollar or Other Currency Signs:** Only display these in the top row and bottom row of schedules. Sometimes it’s a bit ambiguous what a “schedule” is – often, we’ll display these in the top and bottom rows of each major segment.

**“Units”:** We like to use an extra column to display the units, especially in schedules that mix $ per Sq Ft and Sq Ft and other figures with actual $, to remove ambiguity.

**Indentation:** We indent the individual rows within each category, and we use multiple indents for sub-categories. We also indent percentages used for informational purposes such as the margin formulas.

**Signs:** On the IS and CFS, we often use (+) and (-) when it is meaningful to do so – for example, if everything in a row is going to be positive or negative, and it’s easy to specify which is which.

**Italics:** We usually italicize _percentages used for informational purposes_ – so, the overall margins and revenue growth rates, but not the assumptions used to calculate them in the first place. Those are in the yellow input boxes!

**Decimals:** It doesn’t matter what you do as long as you’re consistent. Use 1 decimal, 0 decimals, or 2 decimal places for all the financial figures in your model… exceptions apply for the Share Price and EPS figures, which almost always use 2 decimal places because of how share prices are displayed.

We also usually use at least 1 decimal place, sometimes up to 2-3, to display the company’s share count. Usually 1 decimal place for valuation multiples and percentages as well – even if the financial figures in the model have 0 decimal places, as is the case here.

**Headers:** We use a blue background color, white text, and the “FY” format for the top header with the Historical and Projected years. We then use a grey background color for the other headers in a schedule – sometimes display the years on top depending on the spacing.

You can view examples of these standards in action below:

![Header and Unit Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20503'%3E%3C/svg%3E "Header and Unit Formatting")

![Income Statement Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20448'%3E%3C/svg%3E "Income Statement Formatting")

![Financial Model Formatting - Indentations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20507'%3E%3C/svg%3E "Financial Model Formatting - Indentations")

**How to Automate the Color-Coding Process in Excel**
-----------------------------------------------------

It’s difficult to automate “all” this formatting, but you can automate much of the color-coding process if you feel comfortable using VBA, which we cover in the final module of this course.

In short, you can use the .SpecialCells, Union, and Intersect commands to find the appropriate cells, loop through them, and change the colors appropriately.

You can get the full Excel file (.xlsm) or just the .xlam file for the VBA code itself below:

[Full Excel File with Color-Code Macro](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Color-Code-Macro-Excel-File.xlsm)

[Color-Code Macro VBA Code](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Color-Code-Macro.xlam)

**Note:** You must know Excel fairly well to use macros. If not, you could do serious damage to your spreadsheets. If you have little experience in Excel, then you should not mess around with this macro.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://xl3-breakingintowallstreet-com.s3.amazonaws.com/XL-02-PC-07-Formatting-Financial-Models.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Formatting Financial Models - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-02-PC-07-Formatting-Financial-Models-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Formatting Financial Models - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-02-PC-07-Formatting-Financial-Models-After.xlsxv)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Excel & VBA](https://breakingintowallstreet.com/excel-vba/)

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[Learn More](https://breakingintowallstreet.com/excel-vba/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[BIWS Premium](https://breakingintowallstreet.com/biws-premium/)
: Get the Excel & VBA, Core Financial Modeling, and PowerPoint Pro courses together and learn everything from Excel shortcuts up through financial modeling, valuation, M&A and LBO deals, and the key PowerPoint shortcuts and commands. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/biws-premium/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&mini=true)
[Email](mailto:?subject=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[](https://www.linkedin.com/shareArticle?title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&mini=true)
[](mailto:?subject=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[](https://api.whatsapp.com/send?text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[Copy](https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/#)
[Email](mailto:?subject=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&t=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/06/04221508/how-to-color-code-in-excel.jpg&description=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[Print](https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[SMS](sms:?&body=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[X](https://x.com/intent/tweet?text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[WhatsApp](https://api.whatsapp.com/send?text=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-color-code-in-excel%2F&title=How%20to%20Color%20Code%20in%20Excel%20for%20Financial%20Models%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2832%3A42%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/06/04221508/how-to-color-code-in-excel.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand