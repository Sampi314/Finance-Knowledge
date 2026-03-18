# Sensitivity Analysis Excel: Tutorial, Video, and Template

**Source:** https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel

---

Sensitivity Analysis Excel: How to Set It Up \[Tutorial Video\] (17:58)
=======================================================================

In this lesson, you’ll learn how to set up sensitivity tables in financial models, including the key requirements for inputs and outputs and the required steps, and you’ll get practice creating these tables in the Walmart valuation.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/#tab-signup)
    

Sensitivity analysis in Excel

  
**Sensitivity analysis in Excel** lets you vary the assumptions in a model and look at the output under a range of different outcomes.

All investing is **probabilistic** because you can’t predict exactly what will happen 5, 10, or 15 years into the future – but you can come up with a reasonable set of potential scenarios.

For example, if a company you’re analyzing exceeds growth expectations and grows at 15% per year rather than 5-10%, that might be one scenario.

If it grows in-line with expectations, that could be another scenario. And if it _declines_ or grows at a negative rate, that could be a third scenario.

You can use sensitivity analysis to look at how this company’s _valuation_ changes as you move from one scenario to the next.

Sensitivity Analysis Excel: Data Tables and How to Build Them
-------------------------------------------------------------

Internally in Excel, sensitivity analyses are known as “data tables,” and you can access them in the ribbon menu under the Data tab and “What-If Analysis”:

![Sensitivity Analysis Excel - Data Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20268'%3E%3C/svg%3E "Sensitivity Analysis Excel - Data Table")

In PC/Windows Excel, the shortcut is Alt, D, T or Alt, A, W, T (there is no shortcut in Mac Excel):

A properly set-up and formatted sensitivity table looks like this (taken from the Walmart DCF, where we vary the Discount Rate and Terminal Growth Rate to assess the company’s implied value):

![Sensitivity Analysis Excel - Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20205'%3E%3C/svg%3E "Sensitivity Analysis Excel - Example")

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

To create this table, use the following steps:

### Sensitivity Tables, Part 1: Building an Appropriate Financial Model

Before you do anything else, you must have a financial model or other analysis where **several key inputs or assumptions _directly_ affect the output.**

For example, in our setup for this Walmart DCF, it’s easy to see that assumptions such as the Discount Rate and the Terminal Multiple affect the company’s implied share price.

The Terminal Multiple affects its Terminal Value, and then the Discount Rate affects the Present Value (PV) of the Terminal Value and the PV of the Free Cash Flows in the projection period, and those flow into the Implied Enterprise Value and then the Implied Equity Value and Share Price:

![Flow of Inputs in Sensitivity Analysis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20583'%3E%3C/svg%3E "Flow of Inputs in Sensitivity Analysis")

If you do not have a setup like this, where a few key cells _affect the output_ of your model, sensitivity analyses will not work.

### Sensitivity Tables, Part 2: Formatting

Next, start by formatting the cells the way you want. We usually pick blue colors for the background/fill of the outer cells, with white font color on top, and then a standard white background with black font color for the middle area:

![Sensitivity Table Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20203'%3E%3C/svg%3E "Sensitivity Table Formatting")

This is just formatting, so you should look at our tutorial on [how to color code in Excel](https://breakingintowallstreet.com/kb/excel/how-to-color-code-in-excel/)
 for more.

### Sensitivity Tables, Part 3: Enter the Row and Column Numbers You Want to Sensitize

This step is very important: when you enter the numbers in the row and column of the table that you want to sensitize, **you cannot link them directly to anything in the model!**

So, you must hard-code all these numbers in Excel, or you must start the row and column with a hard-coded number and then add or subtract in each column or row after that.

Here they are for Walmart:

![Sensitivity Analysis Excel - Row and Column Figures](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20454'%3E%3C/svg%3E "Sensitivity Analysis Excel - Row and Column Figures")

### Sensitivity Tables, Part 4: Link to the Output Variable in the Top-Left Corner

Next, go to the top-left corner of the table – cell D102 here – and enter a direct link to the output variable that you want to display in the table.

In this case, it’s the company’s Implied Share Price under the Perpetuity Growth Rate method of calculating Terminal Value:

![Sensitivity Analysis Excel - Output Variable](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20190'%3E%3C/svg%3E "Sensitivity Analysis Excel - Output Variable")

![Sensitivity Analysis Excel - Output Variable in Model](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20774'%3E%3C/svg%3E "Sensitivity Analysis Excel - Output Variable")

This is the only part of the sensitivity table that should be linked to something in the model.

### Sensitivity Tables, Part 5: Select the Entire Range and Create the Table

Now, select the entire range and go to Alt, D, T or Data, What-If Analysis, and Data Table, and enter the row and column input cells (the Terminal Growth Rate and Discount Rate here):

![Creating the Sensitivity Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20229'%3E%3C/svg%3E "Creating the Sensitivity Table")

![Entering the Row and Column Input Cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20210'%3E%3C/svg%3E "Entering the Row and Column Input Cells")

If the table does not refresh right away, press F9 to force a spreadsheet update and see the results.

### Sensitivity Tables, Part 6: Check Your Work

The results should look like this:

![How to Check a Sensitivity Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20203'%3E%3C/svg%3E "How to Check a Sensitivity Table")

You should check your work by reviewing the table and looking at the following points:

\-Do the numbers **change** in each cell? If not, you’re doing something wrong. You should not see rows or columns where the output is the same.

\-In valuation tables, does the company’s implied value _increase_ as its revenue, revenue growth, or margins increase? Higher numbers should mean a higher valuation.

\-As the Discount Rate increases, the company’s implied value should _decrease_.

The list goes on: make sure you understand how each assumption should affect the output and then see if it works that way in your table.

**Sensitivity Analysis Excel: Key Requirements to Set Up the Tables**
---------------------------------------------------------------------

To recap and summarize this article, here are the key requirements for Excel-based sensitivity analysis:

**1) The input variables and output must be on the same spreadsheet as the table**. You cannot use assumptions or drivers from other sheets, such as the 3-statement model, in this table.

**2) The numbers in the input row and column cannot be linked to or from anything that’s in the model.** Start each input row or column with a hard-coded number and then hard-code the rest or make them change by simple percentages or numbers.

**3) The row and column inputs and the output must be related in some way.** If the inputs do not affect the output, the table will show no changes as you vary the numbers.

**4) Set “Workbook Calculation” in Options or Preferences to “Automatic except for data tables”** or your spreadsheet will slow down, especially with many tables. You can then press F9 to refresh or update the tables.

**5) Enter a direct link to the output you want to sensitize in the top-left-hand corner of the table**. And then, select everything and go through the steps shown above. “Row Input Cell” should be a direct link for the input in the top row, and “Column Input Cell” should be a direct link for the input in the left column.

**6) You cannot modify individual cells in the table once it has been created.** If you want to change something or select different inputs or outputs, you must delete and re-enter the entire table.

You will see sensitivity tables in almost every financial model of intermediate complexity and beyond, so you _must_ know how to use them.

They aren’t that difficult, but many students make mistakes with the points above.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-17-Sensitivity-Tables.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Sensitivity Analyses - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-17-Sensitivity-Tables-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Sensitivity Analyses - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-03-17-Sensitivity-Tables-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&mini=true)
[Email](mailto:?subject=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[](https://www.linkedin.com/shareArticle?title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&mini=true)
[](mailto:?subject=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[](https://api.whatsapp.com/send?text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[Copy](https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/#)
[Email](mailto:?subject=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&t=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/04221539/sensitivity-analysis-excel.jpg&description=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[Print](https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[SMS](sms:?&body=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[X](https://x.com/intent/tweet?text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fsensitivity-analysis-excel%2F&title=Sensitivity%20Analysis%20Excel%3A%20How%20to%20Set%20It%20Up%20%5BTutorial%20Video%5D%20%2817%3A58%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/04221539/sensitivity-analysis-excel.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand