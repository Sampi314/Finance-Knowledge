# Excel Tutorial Using INDIRECT, MATCH, and SUMIFS

**Source:** https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews

---

Excel Practice Test for Interviews: Full Tutorial Using INDIRECT, MATCH, and SUMIFS \[Tutorial Video\] (14:55)
==============================================================================================================

In this tutorial, you’ll learn how to complete an Excel practice test by writing a flexible formula that lets you summarize quarterly or monthly data in an annual format using the INDIRECT, MATCH, and SUMIFS functions. This is a common task given in Excel tests and case studies, especially in industries such as real estate.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/#tab-signup)
    

Excel Practice Test for Interviews: Full Tutorial Using INDIRECT, MATCH, and SUMIFS

When it comes to **Excel practice tests** in interviews, the key is to have a solid knowledge of key Excel functions, such as SUMIFS, INDEX/MATCH, INDIRECT, and HLOOKUP/VLOOKUP, and then combine that knowledge with a lot of practice.

If you want to get an Excel practice test with simpler multiple choice questions, please see our [BIWS Certificates page](https://breakingintowallstreet.com/certificates/)
 and look at the PDFs under “Excel & VBA” there.

But if you want a much more challenging Excel practice test that requires you to write real formulas in Excel, keep reading.

**A Challenging Excel Practice Test**
-------------------------------------

Often, interviewers will ask you to write a single formula that accomplishes a task elegantly rather than having to modify a formula slightly each time you use it.

For example, In in many cases, you could write simple SUM formulas to sum up cells manually, but it’s far more robust to use the SUMIFS function so that you can check the dates and include only the matching quarterly or monthly data for the year you’re in.

But to make the function truly flexible so that you can copy and paste it down and around and use it to sum up data for different rows, you must use the MATCH and INDIRECT functions.

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

Here’s a real-life example submitted by one of our students:

**Excel Practice Test Prompt:** “Review the quarterly real estate data for this apartment complex with 4 units, and write a SINGLE formula to retrieve everything on an annual basis.”

Here’s a partial screenshot of the data from the blank Excel file above:

![Excel Practice Test - Monthly Setup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20737'%3E%3C/svg%3E "Excel Practice Test - Monthly Setup")

And here’s the annual summary page:

![Excel - Annual Summary](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20423'%3E%3C/svg%3E "Excel - Annual Summary")

The quarterly sheet is called “Quarters” and the annual sheet is called “Summary”.

So, how would you write a _single formula_ to accomplish this?

**Excel Practice Test: Recommended Approach**
---------------------------------------------

Instead of trying to write one formula all at once, **break it into smaller pieces** and build up to something more flexible by the end.

At each stage of the process, you want to have a _functional formula_ in Excel – that way, even if you don’t finish it perfectly, **you’ll still get credit for the work you did.**

In this case, let’s start with a SUMIFS formula so that we can capture the quarterly data by date:

\=SUMIFS(Quarters!$E$9:$T$9,Quarters!$E$2:$T$2,”<=”&Summary!E$2,Quarters!$E$2:$T$2,”>”&Summary!D$2)

Here’s what it looks like in Excel for the first row:

![Excel SUMIFS Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20390'%3E%3C/svg%3E "Excel SUMIFS Formula")

This is a good start, but the problem is that since Quarters!$E$9:$T$9 refers to the **summation range**, we’ll have to update that and make row 9 into row 16, row 23, and so on, as we move down:

![Manual Formula Changes for Rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20432'%3E%3C/svg%3E "Manual Formula Changes for Rows")

To make this part flexible, we need to _match the text on the left to the same text in the quarterly data_ and then move down that number of rows.

For example, in this first row, we could write this formula to do it:

\=MATCH($B4,Quarters!$B$1:$B$51,0)

![Excel MATCH Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20583'%3E%3C/svg%3E "Excel MATCH Function")

But it’s **not** as simple as just inserting this MATCH function into the SUMIFS formula above.

**The problem is that Excel only allows us to reference _fixed ranges_ of rows and columns in spreadsheets… such as B10:E19 or E9:T9.**

So, we can’t just “substitute in” one or several MATCH functions for the Quarters!$E$9:$T$9 range and be done with this Excel practice test.

But there is one exception: **we can use the INDIRECT function to create a _variable_ reference to another spreadsheet.**

The syntax here gets a bit tricky because we’ll need to join together several parts to create a new version of the formula above, but here’s the basic approach:

First note, that double quotes (” “) indicate _text_ within functions such as MATCH _inside_ the INDIRECT function, and the ampersand symbol (“&”) _joins_ text with functions.

So, in the original formula above:

\=SUMIFS(Quarters!$E$9:$T$9,Quarters!$E$2:$T$2,”<=”&Summary!E$2,Quarters!$E$2:$T$2,”>”&Summary!D$2)

We’ll replace the Quarters!$E$9:$T$9 part with the following:

INDIRECT(“Quarters!$E$”&MATCH($B4,Quarters!$B$1:$B$51,0)&”:$T$”&MATCH($B4,Quarters!$B$1:$B$51,0))

What does this do in the context of this Excel practice test?

The **first part** starts building the text for Quarters!$E$9:$T$9:

“Quarters!$E$”&MATCH($B4,Quarters!$B$1:$B$51,0) produces Quarters!$E$9.

This is because the first text here, “Quarters!$E$”, simply prints exactly as-is within the Excel function.

And then the MATCH($B4,Quarters!$B$1:$B$51,0) function finds the row position of the text we’re searching for in the “Quarters” spreadsheet, which is 9 in this case.

So, Excel sticks together these two parts: “Quarters!$E$” and 9 to form: Quarters!$E$9.

The next part here:

&”:$T$”&MATCH($B4,Quarters!$B$1:$B$51,0))

Simply finishes the Quarters!$E$9:$T$9 text. We use the & character to join the first part to this part, and then we print the “:$T$” text in Excel.

Then, to find the appropriate row number, we use the same match function and join it with the & operator:

MATCH($B4,Quarters!$B$1:$B$51,0)

As a result, this entire term:

&”:$T$”&MATCH($B4,Quarters!$B$1:$B$51,0)) turns into :$T$9 when Excel evaluates it.

Putting it altogether, here’s what happens with this entire formula:

INDIRECT(“Quarters!$E$”&MATCH($B4,Quarters!$B$1:$B$51,0)&”:$T$”&MATCH($B4,Quarters!$B$1:$B$51,0))

becomes:

Quarters!$E$9:$T$9

**And then as we copy this down, there’s no need to modify the formula manually because the MATCH functions keep finding the row number of the matching text on the Quarters spreadsheet:**

![Excel Practice Test - Solutions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20399'%3E%3C/svg%3E "Excel Practice Test - Solutions")

Here’s the entire annual summary for this Excel practice test:

![Annual Summary of Monthly Rental Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20434'%3E%3C/svg%3E "Annual Summary of Monthly Rental Data")

**How to Check Your Work**
--------------------------

It is tricky to get the syntax with the double quotes and ampersands exactly correct in these types of INDIRECT functions, so you should always check your work, time permitting.

The best way to do this is to sum up **manually** each quarter’s figures for each line item and see if they match the annual totals – if not, you have a problem.

Here’s an example for Gross Potential Rent:

![Excel Practice Test - Checking Your Work](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20532'%3E%3C/svg%3E "Excel Practice Test - Checking Your Work")

**Summary of Tests in Excel**
-----------------------------

In the Excel practice test – an actual exercise in Excel, not just a multiple choice test – the following topics are extremely common:

\-Lookup functions and INDEX/MATCH

\-Summation and summary functions such as SUMIFS

\-INDIRECT, which lets you create custom references and variable cell ranges that you can pass into other functions and formulas

You don’t necessarily need to get the formula above 100% correct to “pass” the test.

**The most important point is that you should make sure you have a working formula in each step of the process.**

That way, even if you mix up some of the syntax in the INDIRECT function, or your formula doesn’t work perfectly in all cases, you can show them some of your work and get credit for it.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel Tests in Interviews: INDIRECT, MATCH, SUMIFS, and More (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Test-INDIRECT-Match.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel Practice Test - Blank Version (XL)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Test-INDIRECT-Match-Blank.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel Practice Test - Solution (XL)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-Test-INDIRECT-Match-Complete.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&mini=true)
[Email](mailto:?subject=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[](https://www.linkedin.com/shareArticle?title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&mini=true)
[](mailto:?subject=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[](https://api.whatsapp.com/send?text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[Copy](https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/#)
[Email](mailto:?subject=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&t=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/)
[Pinterest](https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/#)
[Print](https://breakingintowallstreet.com/kb/excel/excel-practice-test-for-interviews/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[SMS](sms:?&body=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[X](https://x.com/intent/tweet?text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-practice-test-for-interviews%2F&title=Excel%20Practice%20Test%20for%20Interviews%3A%20Full%20Tutorial%20Using%20INDIRECT%2C%20MATCH%2C%20and%20SUMIFS%20%5BTutorial%20Video%5D%20%2814%3A55%29&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand