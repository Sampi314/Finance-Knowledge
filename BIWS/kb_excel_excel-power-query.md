# Excel Power Query: Tutorial, Examples, and Uses in Corporate Finance

**Source:** https://breakingintowallstreet.com/kb/excel/excel-power-query

---

Excel Power Query: Full Explanation and Examples \[Tutorial Video\] (11:03)
===========================================================================

In this tutorial, you’ll learn how to use Power Query in Excel to retrieve data from online sources without having to copy and paste text and clean it up manually – and you’ll see how it might be useful when creating presentations and other documents.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/excel-power-query/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/excel-power-query/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/excel-power-query/#tab-signup)
    

Excel Power Query: Full Explanation and Examples

  
One common question we get is: “I see you now cover Excel features like Power Pivot, **Power Query**, VBA, and the Internal Data Model in Excel. Do I need to know these features?”

“Will I be tested on them in interviews? How could they possibly be useful for deal-based roles like IB or PE?”

**The Short Answer About More Advanced Excel Features**
-------------------------------------------------------

The **short answer** is that you don’t “need” to know these features for interviews, but they can make your life on the job much easier.

Even with basic knowledge gained from a few minutes spent using these tools, you can save yourself hours and hours of time.

Yes, you usually work with financial models and valuations in investment banking, private equity, and related fields, but you also have to **analyze data** and present it effectively.

**Power Query** is hugely helpful here because it can automatically parse websites, extract data, and put it in tabular format, so that you do not have to copy and paste anything manually or clean the data manually.

Also, if the website or source data ever changes, Power Query lets you refresh it automatically and make the changes flow through your model.

**Excel Power Query Demonstration**
-----------------------------------

The other day, I had to look up and classify a company’s sales transactions by state.

I had the abbreviations for each state or territory, but I needed to find their full names… and they were inconsistent.

Also, there were some non-standard/less-common ones, such as “MP” for the Northern Mariana Islands, “AP” for U.S. Armed Forces – Pacific, etc:

![Excel - State Abbreviations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20917%20473'%3E%3C/svg%3E)

I could have Googled it and copied and pasted and tweaked the data, but instead I used **Power Query** to do this.

**One warning:** Power Query won’t work in Mac Excel. You need a fairly modern version of PC/Windows Excel (2016, 2019, or Office 365) to follow this example; otherwise, you can download Power Query as an add-in for older versions (Google “Power Query” and your version of Excel).

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

**Step 1:** Go to Data, Get Data, From Other Sources, and From Web in Excel and enter the URL you want to use. In this case, we want to use this list of state and territory abbreviations from Wikipedia:

[https://en.wikipedia.org/wiki/List\_of\_U.S.\_state\_abbreviations](https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations)

![Excel Power Query - Step 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20629'%3E%3C/svg%3E)

![Data URL in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20913%20344'%3E%3C/svg%3E)

**Step 2:** Click “OK” and then “Connect” and select the Table that you want to use:

![Excel Power Query - Step 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20878%20698'%3E%3C/svg%3E)

**Step 3:** Go to “Transform Data” and delete the columns that you do not need (here, it’s based on the best matches for abbreviations and the only column that listed all the possible abbreviations).

![Excel Power Query - Step 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20581'%3E%3C/svg%3E)

**Step 4:** Now, press “Close & Load” to import this data into a table on a new spreadsheet in your Excel file. At this point, you can also rename the table under Properties and “Name” on the right-hand side under “Query Settings”:

![Excel Power Query - Step 6](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20579'%3E%3C/svg%3E)

![Imported Data from Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20879'%3E%3C/svg%3E)

**Step 5:** Now, you can write an INDEX/MATCH formula to retrieve the state/territory name from the appropriate column. We use this one in the example:

\=INDEX(State\_Table,MATCH(Txns\_by\_State!D5,State\_Table\[USPS\],0),1)

![INDEX/MATCH with Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20922%20405'%3E%3C/svg%3E)

**Step 6:** Copy and paste this formula down using the Ctrl + C and Alt, E, S, F shortcuts:

![Finished List of Transactions by State](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20928%20627'%3E%3C/svg%3E)

If the data is really messy, we could have also rearranged the table so that each row contained the state’s full name and one possible abbreviation for it, then the next row contained the next possible abbreviation for it, and so on.

And if something ever changes, we could easily refresh this data automatically and keep the transformations in place now.

**Excel Power Query: Other Use Cases**
--------------------------------------

You could use this same feature to update data sheets for items such as:

\-Employees by location.

\-Buildings by location.

\-Employees by product line or geography.

\-Revenue or Net Income by product or geography.

These are all common items in management presentations, memos, the [Confidential Information Memorandum (CIM)](https://www.mergersandinquisitions.com/confidential-information-memorandum/)
, and other documents that you use or create all the time in investment banking and private equity.

All you have to do is enter the Investor Relations section of the company’s website, find the right URL, and let Power Query parse all the text on the page and turn it into usable tables.

This feature is arguably even more useful in corporate finance / budgeting roles where you may need to retrieve data from online sources and link it to Excel, and you don’t want to bother with manual copy-and-paste commands.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Power Query Tutorial and Explanation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Power-Query-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel Power Query Example - Sales Transactions by State (XL)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Power-Query-Transactions-by-State.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&mini=true)
[Email](mailto:?subject=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[](https://www.linkedin.com/shareArticle?title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&mini=true)
[](mailto:?subject=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[](https://api.whatsapp.com/send?text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[Copy](https://breakingintowallstreet.com/kb/excel/excel-power-query/#)
[Email](mailto:?subject=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&t=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-power-query/)
[Pinterest](https://breakingintowallstreet.com/kb/excel/excel-power-query/#)
[Print](https://breakingintowallstreet.com/kb/excel/excel-power-query/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[SMS](sms:?&body=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[X](https://x.com/intent/tweet?text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-power-query%2F&title=Excel%20Power%20Query%3A%20Full%20Explanation%20and%20Examples%20%5BTutorial%20Video%5D%20%2811%3A03%29&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand