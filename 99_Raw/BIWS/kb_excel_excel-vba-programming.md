# Excel VBA Programming: How to Record a Macro in Excel

**Source:** https://breakingintowallstreet.com/kb/excel/excel-vba-programming

---

Excel VBA Programming: How to Record a Macro in Excel \[Tutorial Video\] (19:16)
================================================================================

In this tutorial, you’ll learn Excel VBA programming, including how to record a macro in Excel, and you’ll see how you can quickly automate your work and get results without doing anything complicated. This sample lesson is part of our Excel & Fundamentals course and the VBA coverage there.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/#tab-signup)
    

Excel VBA Programming: How to Record a Macro in Excel

  
We get a lot of questions about Excel VBA programming, macros, and other programming languages such as R and Python for investment banking and corporate finance roles.

The short answer is that **yes**, it helps to be familiar with VBA and macros in Excel because they’ll save you significant time on the job, but you don’t need to know them for interviews.

Other programming languages like R and Python are more useful for roles like trading, portfolio management, or quant research or quant funds where you do real statistical work over huge data sets.

It’s worth spending **10-20%** of your total Excel training time to learn some VBA basics.

The best method is to learn how to record a macro in Excel, review and edit the code in the VBA Editor, and then tweak and optimize it.

Most Excel constructs, like IF statements, AND, OR, and NOT, and INDEX and MATCH, also carry over to VBA, but the syntax is sometimes different.

You can also do a lot more in VBA, such as looping through a range of cells and performing operations on each one automatically based on its contents or formatting.

**Excel VBA Programming: Your First VBA Macro**
-----------------------------------------------

One great use case for VBA in investment banking is to create a macro for an “Input Box” in Excel – it’s simple, and it doesn’t require much logic or error-checking.

An “input box” is used for assumptions in financial models, such as the highlighted areas below:

![Input Box Examples](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20193'%3E%3C/svg%3E)

Without a macro, it’s quite cumbersome to do because you have to change the borders, alignment, fill color, and font color, and each one is a separate keystroke or mouse click.

Using Copy and Paste Formats doesn’t work, either, because we don’t want to copy the Number Formats – just _specific elements_ of the formatting in each cell.

The Format Painter does not work because it incorrectly copies the Number Formats, and it can’t detect the difference between filled cells and empty cells.

And finally, the Styles feature in Excel is not the best solution because then you’ll have to select all the cells manually and apply the Style first.

Updates or changes are easier to handle with Styles, but we rarely change the formatting of Input Boxes anyway, so this point does not make a big difference here.

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

How to Record a Macro in Excel: Part 1
--------------------------------------

To record this macro, we can start by making sure the Developer Toolbar is available within Excel.

To do this in PC/Windows Excel, go to Alt, T, O for Options, then Customize Ribbon, and make sure Developer Toolbar is checked:

![Developer Toolbar in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20824%20646'%3E%3C/svg%3E)

In Mac Excel, you can press ⌘ + , to access the same Options or Preferences menu.

Then, go to the Developer tab in the ribbon menu and click “Record Macro”:

![Record Macro Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20857%20163'%3E%3C/svg%3E)

You can call this macro something like “Color\_Code” and you can assign the shortcut key Ctrl + Shift + I to it:

![Excel VBA Programming - Macro Shortcut Key Assignment](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%20288'%3E%3C/svg%3E)

Once you’ve done this, go to any cell that might be considered an “Input Box” and do the following:

1) Press Ctrl + 1 or ⌘ + 1 on the Mac, move to the Alignment tab, and select “Center” for Horizontal.

2) Go to the Font tab and change the Color to Blue (optional – we don’t change this in the video).

3) Go to the Border tab and select a Dark Grey color and “Outline” for the Border Style under Presets.

4) Go to the Fill tab and select a light yellow color.

5) Now, exit out of the Ctrl + 1 or ⌘ + 1 dialog, go back to the Developer Toolbar in the ribbon menu, and press “Stop Recording.”

When you’re done recording, go back to the Visual Basic Editor with Alt, L, V or Alt + F11 on the PC (no shortcut in Mac Excel, so go to the Developer Toolbar and navigate to Visual Basic manually).

You’ll see that it has automatically generated code that looks something like this:

![Excel VBA Programming - Autogenerated Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20907'%3E%3C/svg%3E)

Excel VBA Programming: How to Optimize It
-----------------------------------------

While this code “works,” there are some issues with it:

**Issue #1:** There’s way too much code because there are separate “With” statements for the individual borders, interior, and other parts, and we can group these all together.

![Redundant Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20907'%3E%3C/svg%3E)

**Issue #2:** It’s not very readable because there are too many useless commands, and it’s hard to tell what the colors are.

**Issue #3:** We should skip empty cells to make it more efficient, and ideally, we should treat cells with formulas and constants differently so we can apply blue or black font colors to them.

The third issue is more difficult to fix and requires additional training in Excel VBA programming, but we can fix the first two points with simple code reorganization and RGB values for the colors.

A “fixed” version might look like this:

![Excel VBA Programming - Optimized Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20831%20328'%3E%3C/svg%3E)

More Advanced Tips and Tricks
-----------------------------

To skip empty cells and format the input boxes differently based on whether each cell contains a formula or constant, we can use “Intersect” commands in VBA along with the “Special Cells” property to select the formulas and constants and skip the empty cells.

We can then set the font colors for the formulas and constants separately, and set the “nonEmptyRange” to all the cells containing a formula or constant in the range of cells the user has selected.

Finally, we apply the border, fill, and alignment formatting at the end, assuming that there’s at least one non-blank cell in this range.

We cover these more advanced commands in our [Excel & Fundamentals course](https://breakingintowallstreet.com/excel-financial-modeling-fundamentals/)
, but here’s a quick summary:

![Excel VBA Programming - Optimized Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20584'%3E%3C/svg%3E)

Or, you can [learn more about financial modeling here](https://mergersandinquisitions.com/financial-modeling/)
.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) VBA Macro - Explanation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Investment-Banking-VBA-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel - Finished VBA Macro in Real Estate File (XL)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Investment-Banking-VBA.xlsm)
    

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

[X](https://x.com/intent/tweet?text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&mini=true)
[Email](mailto:?subject=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[](https://www.linkedin.com/shareArticle?title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&mini=true)
[](mailto:?subject=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[](https://api.whatsapp.com/send?text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[Copy](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/#)
[Email](mailto:?subject=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&t=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/02/04224043/Excel-VBA-Programming_-How-to-Record-a-Macro-in-Excel.jpg&description=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[Print](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[SMS](sms:?&body=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[X](https://x.com/intent/tweet?text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-vba-programming%2F&title=Excel%20VBA%20Programming%3A%20How%20to%20Record%20a%20Macro%20in%20Excel%20%5BTutorial%20Video%5D%20%2819%3A16%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/02/04224043/Excel-VBA-Programming_-How-to-Record-a-Macro-in-Excel.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand