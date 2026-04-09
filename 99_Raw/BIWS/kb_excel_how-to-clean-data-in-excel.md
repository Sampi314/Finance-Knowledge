# How to Clean Data in Excel: Tutorial, Screenshots, and Excel Examples

**Source:** https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel

---

How to Clean Data in Excel (PC/Windows Version) \[Tutorial Video\] (10:20)
==========================================================================

In this tutorial on how to clean data in Excel, you’ll complete a practice exercise to clean up and separate address data into separate columns and fix problems with the capitalization and punctuation using the text and formatting functions.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/#tab-signup)
    

How to Clean Data in Excel (PC/Windows Version)

**NOTE:** This tutorial on how to clean data in [Excel](https://www.microsoft.com/en-au/microsoft-365/excel)
 uses the PC/Windows version shortcuts. We do cover Mac Excel shortcuts in our full [Excel & Financial Modeling Fundamental course,](https://breakingintowallstreet.com/excel-financial-modeling-fundamentals/)
 but they’re presented in completely separate sets of lessons.

Below, we will list the key PC/Windows shortcuts as well as Mac alternatives.

How to Clean Data in Excel, Part 1: Typical Tasks, Functions, and Shortcuts
---------------------------------------------------------------------------

Our task here is simple: we have customer order data, but the addresses are not presented in an ideal format.

We want to separate the entire “Address” for each order into Street Address, City, State, and ZIP Code fields:

![Customer Order Data in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20489'%3E%3C/svg%3E "Customer Order Data in Excel") To do that, we will use the following functions and shortcuts:

### **Navigation, Selection, and Row/Column Shortcuts:**

**Ctrl + Spacebar:** Select Column (same in Mac Excel)

**Shift + Spacebar:** Select Row (same in Mac Excel)

**Shift + Ctrl + Arrow Keys:** Select to Boundary (same in Mac Excel)

**Shift + Arrow Keys:** Select Multiple Cells (same in Mac Excel)

**Alt, I, C:** Insert Column (Ctrl + Shift + + in Mac Excel)

**Alt, O, C, W:** Change Column Width (No equivalent in Mac Excel)

**Alt, O, C, A:** Auto-Fit Column Width (No equivalent in Mac Excel)

**F2:** Edit Cell (same in Modern Mac Excel; may need Ctrl + U in older versions)

**Alt, E, D:** Delete Cells/Rows/Columns (Ctrl + – in Mac Excel)

### **Copy/Paste/Formatting Shortcuts:**

**Ctrl + 1:** Format Dialog Box (⌘ + 1 in Mac Excel)

**Ctrl + H:** Replace (same in Mac Excel)

**Alt, E, S, F:** Paste Formulas (Ctrl + ⌘ + V, F in Mac Excel)

**Alt, E, S, V:** Paste Values (Ctrl + ⌘ + V, V in Mac Excel)

### **Useful Functions for Cleaning Data in Excel:**

**Alt, A, E:** Text to Columns function (No equivalent in Mac Excel)

**\=PROPER:** Makes first letter in each word uppercase (same in Mac Excel)

**\=TRIM:** Removes extra spaces (same in Mac Excel)

**\=UPPER:** Makes text all uppercase (same in Mac Excel)

**\=SUBSTITUTE:** Replace text within text based on search (same in Mac Excel)

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

**How to Clean Data in Excel, Part 2: Adding Columns and Text to Columns**
--------------------------------------------------------------------------

We start this process by inserting a few extra columns to the right of the Address, City, State, and ZIP column, and then using the Text to Columns function (Alt, A, E) to separate the data based on the commas:

![Text to Columns Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20591'%3E%3C/svg%3E "Text to Columns Function")

![Text to Columns Function, Part 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20413'%3E%3C/svg%3E "Text to Columns Function, Part 2")

We select cell F3, right next to the original data, for the destination cell, and then click “Finish”:

![Text to Columns Function, Part 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20898%20652'%3E%3C/svg%3E "Text to Columns Function, Part 3")

We can now delete the original data column, select all the new data, and then cut and paste it into the original column (E):

![How to Clean Data in Excel - Cutting Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20776%20435'%3E%3C/svg%3E "How to Clean Data in Excel - Cutting Data")

At this point, we can also change the title of each column to something more appropriate, such as Address, City, State, and ZIP.

**How to Clean Data in Excel, Part 3: Fixing Each Column**
----------------------------------------------------------

We can fix the ZIP Code formatting by selecting the whole column with Shift + Ctrl + Down, pressing Ctrl + 1, and then going to Number, Special, and Zip Code:

![How to Clean Data in Excel - ZIP Codes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20623'%3E%3C/svg%3E "How to Clean Data in Excel - ZIP Codes")

The City and State columns have extra spaces at the beginning and end, as well as improper capitalization. To fix these issues, we can use the PROPER and TRIM functions for the City and UPPER and TRIM for the State:

![PROPER and TRIM Functions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20102'%3E%3C/svg%3E "PROPER and TRIM Functions")

![UPPER and TRIM Functions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%2094'%3E%3C/svg%3E "UPPER and TRIM Functions")

We can then copy both these formulas, select to the bottom with Shift + Ctrl and the arrow keys, and then use Alt, E, S, F to paste these as formulas:

![How to Clean Data in Excel - Pasting Formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20466'%3E%3C/svg%3E "How to Clean Data in Excel - Pasting Formulas")

Now, we want to **copy and paste these as** **values (Ctrl + C and then Alt, E, S, V)** – this is because we want to delete the old data.

When we delete that old data, these formulas will stop working, so we need to paste everything as values first so that our spreadsheet saves these new, correct values.

Then, we can cut and paste these over the original, poorly formatted data with Ctrl + X and Ctrl + V:

![Cutting and Pasting Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20331'%3E%3C/svg%3E "Cutting and Pasting Data")

Next, we can select these three columns with Shift + Ctrl + arrow keys and then use the Alt, O, C, A shortcut to auto-fit the column widths based on the widest item in each column:

![Auto-Fit Column Width](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20367'%3E%3C/svg%3E "Auto-Fit Column Width")

Finally, to fix the Street Address column, we can use the PROPER function to capitalize each word correctly. We do not need TRIM because these names do not have extra spaces.

Once again, we enter PROPER, copy and paste the formula down with Ctrl + C and Alt, E, S, F, and then copy and paste values with Alt, E, S, V:

![Fixing Address Data with PROPER](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20252'%3E%3C/svg%3E "Fixing Address Data with PROPER")

Once we’ve pasted these as values, we can then press Ctrl + X to cut this entire column and paste it over the original, incorrectly formatted data:

![How to Clean Data in Excel - Pasting Remaining Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20916%20463'%3E%3C/svg%3E "How to Clean Data in Excel - Pasting Remaining Data")

**How to Clean Data in Excel, Part 4: Fixing Annoying, Remaining Problems**
---------------------------------------------------------------------------

If you take a close look at this data, you’ll find a few small problems – for example:

![How to Clean Data in Excel - Direction Abbreviations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20594'%3E%3C/svg%3E "How to Clean Data in Excel - Direction Abbreviations")

We could try to use the SUBSTITUTE function to fix these issues, but it’s easiest to do a simple Find and Replace with Ctrl + H, where we search for ” Sw ” or ” Se ” and replace them with ” SW ” and ” SE ” respectively (and do something similar for Nw and Ne):

![How to Clean Data in Excel - Direction Abbreviations, Part 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20687%20749'%3E%3C/svg%3E "How to Clean Data in Excel - Direction Abbreviations, Part 2")

With that done, we can then auto-fit the Street Address column with Alt, O, C, A and then delete the blank columns on the right-hand side.

Cleaning up data in Excel is not that complicated if you know the appropriate shortcuts and functions – it’s just a matter of practice and becoming very efficient with the keyboard shortcut.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-02-PC-05-Cleaning-Up-Data.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) How to Clean Data in Excel - Before](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-02-PC-05-Cleaning-Up-Data-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) How to Clean Data in Excel - After](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-02-PC-05-Cleaning-Up-Data-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&mini=true)
[Email](mailto:?subject=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[](https://www.linkedin.com/shareArticle?title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&mini=true)
[](mailto:?subject=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[](https://api.whatsapp.com/send?text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[Copy](https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/#)
[Email](mailto:?subject=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&t=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04221453/how-to-clean-data-in-excel.jpg&description=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[Print](https://breakingintowallstreet.com/kb/excel/how-to-clean-data-in-excel/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[SMS](sms:?&body=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[X](https://x.com/intent/tweet?text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[WhatsApp](https://api.whatsapp.com/send?text=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fhow-to-clean-data-in-excel%2F&title=How%20to%20Clean%20Data%20in%20Excel%20%28PC%2FWindows%20Version%29%20%5BTutorial%20Video%5D%20%2810%3A20%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04221453/how-to-clean-data-in-excel.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand