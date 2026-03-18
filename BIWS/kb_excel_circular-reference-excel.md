# Circular Reference Excel - How to Find and Fix Them

**Source:** https://breakingintowallstreet.com/kb/excel/circular-reference-excel

---

Circular Reference Excel – How to Find and Fix Them \[Tutorial Video\] (10:47)
==============================================================================

You’ll learn about circular references in Excel formulas in this lesson, including why they come up, how to deal with them properly, and why you should generally avoid them in financial models.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/#tab-signup)
    

Circular Reference Excel - How to Find and Fix Them

**Circular Reference Excel: What Is It?**
-----------------------------------------

A **circular reference** in [Excel](https://www.microsoft.com/en-au/microsoft-365/excel)
 is a case where **the input of a cell depends on the output of that same cell.** Here’s a simple example:

![Circular Reference Excel - Example](https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/06/19075511/Circular-Reference-01.jpg "Circular Reference Excel - Example")

The contents of cell Q14 depend on the contents of cell R14 and… cell Q14.

The input of Q14 depends on its output – what’s already there – which creates a **circular reference.**

We know the circular reference is there because the bottom-left part of the screen now reads “Calculate”:

![Circular Reference Excel - Calculate Message](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20128'%3E%3C/svg%3E "Circular Reference Excel - Calculate Message")

If that does not appear correctly for you in Excel, or you just get a simple error message, go to the Options menu (Alt, T, O on PC or ⌘ + , on Mac), Formulas, and make sure your settings look like this:

![Circular Calculations in Options Menu](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20826%20678'%3E%3C/svg%3E "Circular Calculations in Options Menu")

When this happens – when the input of a cell depends on its output – Excel gets “confused” about what to do, and it has to start using approximations to make the calculations. For example, here’s what happens if we enter the number 2 into cell R14:

![Circular Calculation - Iterations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20364%2089'%3E%3C/svg%3E "Circular Calculation - Iterations")

Excel “loops” through this circular reference 100 times – per the settings in the screenshot above – to calculate the “answer,” which is 200 (since 100 \* 2 = 200).

A circular reference could be **direct** – as it is here, where the cell’s output directly flows into the cell’s input – or **indirect**.

For an example of an indirect circular reference, let’s say that Q14 = R14 + S14, and that S14 = Q14 + Q13:

![Indirect Circular Reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20175'%3E%3C/svg%3E "Indirect Circular Reference")

Cell S14 depends on what’s in Q14, but Q14 depends on what’s in S14.

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

In real life, circular references in financial models occur most frequently with **Interest Income** and **Interest Expense** – specifically, when you calculate those by using _average_ Cash or Debt balances rather than beginning-of-period balances.

A company’s Interest Income depends on its Cash balance, but its Cash balance changes over the year.

So, if you use the Average Cash balance (i.e., =AVERAGE(Beginning Cash, Ending Cash)), then the Interest Income is linked to both of those.

**BUT the Ending Cash balance also depends on the Interest Income!** More interest earned means the company’s Ending Cash Balance will be higher.

The same goes for Interest Expense and the Average Debt Balance during the year, but in the opposite direction (lower Interest Expense means more ability to repay Debt, which, in turn, means lower Interest Expense).

**Why You Should Avoid Them**
-----------------------------

You should **avoid circular references** whenever possible because they make models and spreadsheets unstable and difficult to modify.

If you try to edit a model where many rows or columns are linked to circular references, for example, deleting a single row or column could cause cascading #REF! errors because of the iterations required to complete a circular calculation.

However, you will encounter circular references “out in the wild” in other peoples’ models, so you need to know how to deal with them.

**How to Find Circular References**
-----------------------------------

If you go back to the Options menu, Formulas, and you _un-check_ “Use Iterative Calculations” Excel will display an error message and blue arrows that show all the circular references on your current sheet, along with the exact cells at the bottom of the screen:

![How to Find Circular References](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20514%20153'%3E%3C/svg%3E "How to Find Circular References")

You can then go into these cells and change the formulas to remove the circular references.

If your file or spreadsheet has _dozens_ or _hundreds_ of circular references, then it may be more difficult to do this because there will be blue arrows all over.

In that case, you will have to go line-by-line and cell-by-cell to fix these. There isn’t really a “more efficient” way to do it because deleting all the circular formulas manually will create even more problems.

Excel Circular Reference Workaround: How to Avoid Them
------------------------------------------------------

In financial models, the best way to **avoid** circular references is to build in a “switch” that lets the user toggle between Average Balances and Beginning Balances when calculating items like Interest Income and Interest Expense.

In practice, the added “accuracy” from using Average Balances is so small that it’s irrelevant in nearly all cases.

We recommend the following setup as a workaround to this problem:

![Circular References - Average Balance Switch](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20155'%3E%3C/svg%3E "Circular References - Average Balance Switch")

Then, whenever we calculate Interest Income or Interest Expense in the model, we use an IF statement to check the value in this named cell (1 or 0) and then use the Average Balances or Beginning Balance:

![Interest Income - Circular Switch](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20991%20777'%3E%3C/svg%3E "Interest Income - Circular Switch")

Setting this named cell to 0 will force all formulas to use the Beginning Cash or Debt Balances, meaning that there will be no circular references, and the model should remain stable.

We follow this practice in the examples and exercises in our [Excel & Financial Modeling Fundamentals course](https://breakingintowallstreet.com/excel-financial-modeling-fundamentals/)
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

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-14-Circular-References.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Circular References - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-14-Circular-References-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Circular References - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-14-Circular-References-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&mini=true)
[Email](mailto:?subject=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[](https://www.linkedin.com/shareArticle?title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&mini=true)
[](mailto:?subject=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[](https://api.whatsapp.com/send?text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[Copy](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/#)
[Email](mailto:?subject=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&t=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/06/04221341/circular-reference-excel.jpg&description=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[Print](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[SMS](sms:?&body=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[X](https://x.com/intent/tweet?text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fcircular-reference-excel%2F&title=Circular%20Reference%20Excel%20-%20How%20to%20Find%20and%20Fix%20Them%20%5BTutorial%20Video%5D%20%2810%3A47%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/06/04221341/circular-reference-excel.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand