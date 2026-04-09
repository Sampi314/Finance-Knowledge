# Index Match Function Excel: Full Tutorial and Examples

**Source:** https://breakingintowallstreet.com/kb/excel/index-match-function-excel

---

Index Match Function Excel \[Tutorial Video\] (16:32)
=====================================================

In this lesson, you’ll learn the basic syntax for INDEX and MATCH, two of the most powerful functions in Excel, and you’ll learn how to use them to create improved versions of the HLOOKUP and VLOOKUP functions.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/index-match-function-excel/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/index-match-function-excel/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/index-match-function-excel/#tab-signup)
    

Index Match Function Excel

  
The **Index Match function** combination in [Excel](https://www.microsoft.com/en-au/microsoft-365/excel)
 is the best way to **retrieve data from ranges of cells in Excel**.

The Index Match combo gets around the limitations of functions like VLOOKUP and HLOOKUP, and it’s faster and far more flexible than either of these.

It’s arguably even better than the newer XLOOKUP function because you can write a single INDEX function to search an entire range rather than having to write “double” XLOOKUP functions, with one inside the other.

You use the Index Match Function Excel combination to retrieve specific items in data analyses and to set up scenarios and lists of comparable public companies and precedent transactions in financial models.

Let’s start by looking at a few simple examples of how it works:

Index Match Function Excel: Starting with INDEX
-----------------------------------------------

Let’s say that we have a list of sales representatives (sales reps) for a company in a spreadsheet called “Sales\_Reps”.

We could use the INDEX function to retrieve information from a specific row and column number, using this syntax:

\=INDEX(Array, Row Number, Column Number)

![Simple INDEX Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20255'%3E%3C/svg%3E "Simple INDEX Function")

Since the 3rd row is for “Cletus Richie” and the 7th column is for “Hire Date” this function retrieves Cletus Richie’s Hire Date:

![INDEX Function Results](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20260'%3E%3C/svg%3E "INDEX Function Results")

Since we have to specify the exact row number and column number in this range, though, this function is _worse_ than VLOOKUP and HLOOKUP – at least those functions find the item in a range of data!

If the range of cells you’re indexing has only 1 column, the “Column Number” part of the INDEX function is optional:

![INDEX with Optional Column Number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20269'%3E%3C/svg%3E "INDEX with Optional Column Number")

But if the range has more than 1 column, leaving out the Column Number will generate a #REF! error.

By itself, INDEX is not very useful because of the need to specify the exact row and column numbers.

**Combining INDEX with MATCH – usually two MATCH functions – though, makes it an _incredibly useful_ function combination in Excel.**

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

The MATCH Function in Excel
---------------------------

The MATCH function finds the row or column number of an item in a range of cells, and then it passes those row and column numbers into INDEX.

Here’s an example of how MATCH works by itself, using the following syntax:

\=MATCH(Lookup Value, Lookup Array, Match Type)

You normally set “Match Type” to 0 for an Exact Match:

![MATCH with Exact Match](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20275'%3E%3C/svg%3E "MATCH with Exact Match")

This MATCH function returns 4 since “State” is in the 4th position of this row at the top.

This 4 is the _relative position_ of “State” in the row – **not** its absolute position, which is column #5 (column E)!

We can also use MATCH to find items in a column:

![MATCH Function for a Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20271'%3E%3C/svg%3E "MATCH Function for a Column")

This function returns 10 since the Sales Rep with a base salary of $89,00 is in the _10th row of this specific column_.

Index Match Function Excel: Combining INDEX and MATCH
-----------------------------------------------------

When you combine INDEX and MATCH, **the size of the range in the INDEX function must match the sizes of the ranges in the MATCH functions.**

Here’s an example where we search for the name of Sales Rep #6:

![Index Match Function Excel: Combined](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20255'%3E%3C/svg%3E "Index Match Function Excel: Combined")

This produces “Sylvia Marin” because that is the name of the Sales Rep with ID 6. The function here is:

\=INDEX(B2:K11,MATCH(6,G2:G11,0),MATCH(“Name”,B2:K2,0))

Here is what happens internally:

First, Excel looks in the G2:G11 column for the number 6. It needs an exact match because of the 0 in this function: MATCH(6,G2:G11,0).

It finds this number 6 in row 7 of this range.

Then, Excel looks in row B2:K2 for “Name” and it once again needs an exact match because of the 0 in this function: MATCH(“Name”,B2:K2,0).

It finds “Name” in column 1 of this range.

Then, Excel replaces these MATCH functions with the numbers 7 and 1 instead:

![Index Match Function Excel: How Excel Processes It](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20256'%3E%3C/svg%3E "Index Match Function Excel: How Excel Processes It")

And this produces the “answer” of Sylvia Marin:

![Result of the INDEX and MATCH Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20261'%3E%3C/svg%3E "Result of the INDEX and MATCH Function")

Unlike VLOOKUP and HLOOKUP, this Index Match Function Excel combination can search in _any row or column in the range of cells_ – not just the leftmost column or topmost row.

It also works even if the range of cells changes (i.e., rows or columns are added or deleted) because it always _searches_ for specific items in the reference row or column:

![INDEX and MATCH Flexibility Over Ranges](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20239'%3E%3C/svg%3E "INDEX and MATCH Flexibility Over Ranges")

The only disadvantage is that the INDEX/MATCH/MATCH combination takes a bit more time to set up than VLOOKUP or HLOOKUP, but it’s so much more flexible that the additional time requirement doesn’t even matter.

Also, you must be _very careful_ with the ranges used in the INDEX function and the two inner MATCH functions, or this combination will not work properly:

![Misaligned Range in INDEX and MATCH](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20345'%3E%3C/svg%3E "Misaligned Range in INDEX and MATCH")

Rewriting a VLOOKUP Function with the INDEX and MATCH Functions
---------------------------------------------------------------

We can now use INDEX and MATCH to rewrite previous VLOOKUP and HLOOKUP functions and make them more flexible.

For example, we previously used VLOOKUP to calculate the Commissions owed to each sales rep for each sale in a table of customer orders.

But we can now rewrite it using the INDEX/MATCH/MATCH combination:

![Rewriting a VLOOKUP Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20403'%3E%3C/svg%3E "Rewriting a VLOOKUP Function")

What’s the advantage?

Now, if we ever change the position of the “Commission Rate” column in the Sales\_Reps spreadsheet, or we insert or delete columns, this function will still work:

![Index Match Function Excel - Flexibility](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20563'%3E%3C/svg%3E "Index Match Function Excel - Flexibility")

This may seem like a minor point, but spreadsheets change _all the time_ as you go through different versions and processes.

The other big advantage is that with VLOOKUP, we _must_ start in column G of the Sales\_Reps spreadsheet since that’s the one that contains the Sales Rep IDs.

But with INDEX/MATCH, there are no such requirements, so we can INDEX the entire range and then decide which row and column to search later on.

This point is a bigger advantage because there are many, many cases in which you need to find an item and then move to the left, or find an item and move up – or move in some other directions.

With VLOOKUP and HLOOKUP, you can’t do that at all – but it’s easy with INDEX and MATCH.

Other Uses of INDEX and MATCH in Excel
--------------------------------------

Outside of data analysis, we also use the INDEX/MATCH combination all the time in financial models. Here are a few examples:

First, we often use this function combo to set up **scenarios** in models and select the appropriate number based on the selected scenario:

![Index Match Function Excel - Scenarios in a Financial Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20504'%3E%3C/svg%3E "Index Match Function Excel - Scenarios in a Financial Model")

Notice here that the range used in the MATCH function does not have to be “inside” the indexed area – it just needs to be _the same height as the indexed area_, i.e., it must have the same number of rows.

This is what the concept of “alignment” means – you don’t necessarily need an exact match, **but the number of rows and number of columns in the inner MATCH functions must match the number of rows and columns in the indexed range**.

We also use INDEX and MATCH for retrieving data from “calculations” sheets, such as those for [comparable company analysis (CCA)](https://breakingintowallstreet.com/kb/valuation/comparable-company-analysis-cca/)
:

![INDEX and MATCH for Calculations in Comparable Company Analysis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20982%20468'%3E%3C/svg%3E "INDEX and MATCH for Calculations in Comparable Company Analysis")

In this case, we typically index a _huge_ range that has data and calculations for each company in this set, such as the area shown below:

![Calculations Sheet in Comparable Company Analysis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20768'%3E%3C/svg%3E "Calculations Sheet in Comparable Company Analysis")

Once again, the key advantage is **flexibility.**

By setting it up this way, if something ever changes, the same INDEX and MATCH functions will work.

If we used HLOOKUP or VLOOKUP instead, we would have to change the row and column numbers, the starting and ending points of the range, and so on.

Finally, the INDEX/MATCH combo is great because they are both **non-volatile functions**, meaning that they are not recalculated when something in the spreadsheet changes… unless that change directly affects those functions.

By contrast, Excel will do a forced recalculate of HLOOKUP and VLOOKUP whenever something changes – even if it’s small and unrelated to them.

**The Bottom Line:** The Index Match Function Excel combination is one of the most powerful tools in your spreadsheet toolbox.

Use it often and use it well, and you’ll save hours and hours in spreadsheets.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-07-INDEX-MATCH-Part-1.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) INDEX and MATCH Functions - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-07-INDEX-MATCH-Part-1-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) INDEX and MATCH Functions - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-07-INDEX-MATCH-Part-1-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&mini=true)
[Email](mailto:?subject=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[](https://www.linkedin.com/shareArticle?title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&mini=true)
[](mailto:?subject=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[](https://api.whatsapp.com/send?text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[Copy](https://breakingintowallstreet.com/kb/excel/index-match-function-excel/#)
[Email](mailto:?subject=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&t=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04225028/index-match-function-excel-1.jpg&description=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[Print](https://breakingintowallstreet.com/kb/excel/index-match-function-excel/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[SMS](sms:?&body=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[X](https://x.com/intent/tweet?text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Findex-match-function-excel%2F&title=Index%20Match%20Function%20Excel%20%5BTutorial%20Video%5D%20%2816%3A32%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04225028/index-match-function-excel-1.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand