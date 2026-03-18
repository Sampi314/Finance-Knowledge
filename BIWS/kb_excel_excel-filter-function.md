# Excel FILTER Function: Full Tutorial and XL Examples

**Source:** https://breakingintowallstreet.com/kb/excel/excel-filter-function

---

Excel FILTER Function: Data, Financial Models, and the Multiverse
=================================================================

The FILTER function in Excel, added in the 365 version and Excel 2021 and beyond, lets you extract multiple matching rows from a set of data based on one or more conditions; it updates the results dynamically as the data changes and creates a spill range you can reference in other formulas.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/excel-filter-function/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/excel-filter-function/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/excel-filter-function/#tab-signup)
    

Excel FILTER Function: Data, Financial Models, and the Multiverse

> **Excel FILTER Function Definition:** The FILTER function in Excel, added in the 365 version and Excel 2021 and beyond, lets you extract multiple matching rows from a set of data based on one or more conditions; it updates the results dynamically as the data changes and creates a **spill range** you can reference in other formulas.

Microsoft has added dozens of features, functions, and formulas to Excel since ~2020, but the **FILTER** function is one of the top 5 most useful new additions.

Other functions, such as [XLOOKUP](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
 and [INDEX/MATCH](https://breakingintowallstreet.com/kb/excel/index-match-function-excel/)
, exist mostly to find **single values** in ranges of data.

But **FILTER** is about finding **multiple matching records** without modifying the original data.

If XLOOKUP and INDEX/MATCH are like Spider-Man, you can think of FILTER as the “multiverse” version:

![FILTER vs. XLOOKUP](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20747'%3E%3C/svg%3E "FILTER vs. XLOOKUP")

The basic parameters are as follows:

\=FILTER(Array, Include, \[If Empty\])

You reference the “array” or range of data you want to filter, you specify the criteria to filter it, and then you state what will appear if nothing matches your criteria.

For example, we could “filter” a list of customer order data for Orders above $1,000 with this function:

![Basic FILTER Functionality](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20163'%3E%3C/svg%3E "Basic FILTER Functionality")

The B6:J104 part refers to the entire range of customer order data, which is to the left of this smaller area.

This gives us a list of orders that dynamically updates as new data is added; we can reference this **spill range** with the “#” notation and use it in other operations, and it will keep resizing as the data changes:

![FILTER and Spill Ranges](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20204'%3E%3C/svg%3E "FILTER and Spill Ranges")

FILTER is incredibly useful for data analysis, but it’s also useful in [financial models](https://mergersandinquisitions.com/financial-modeling/)
 – especially when you are building **asset-level forecasts**, such as for private equity portfolio companies, properties in [real estate](https://breakingintowallstreet.com/kb/real-estate-modeling/)
, or solar/wind farms in [project finance](https://breakingintowallstreet.com/kb/project-finance/)
.

### **Files & Resources:**

*   [Excel FILTER Function (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Excel/Excel-Filter-Function.xlsx)
    
*   [Excel FILTER Function – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Excel/Excel-Filter-Function-Slides.pdf)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **4:24:** Part 1: FILTER with Multiple Criteria
*   **7:28:** Part 2: FILTER for PE Fund Modeling
*   **12:31:** Part 3: FILTER with the XIRR and IRR Functions
*   **15:31:** Part 4: How to Make This More Dynamic
*   **19:27:** Recap and Summary

**Excel FILTER Function with Multiple Criteria**
------------------------------------------------

To use FILTER with multiple criteria, one method is to “multiply together” the separate fields.

For example, let’s say that we want to capture all orders by “Mars University” for “Product G” in this sales data.

To do this, we’d enter the **entire range** to filter and then use (Column1=Target1) \* (Column2=Target2) in the “Include” part:

![FILTER with Multiple Criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20161'%3E%3C/svg%3E "FILTER with Multiple Criteria")

To make this even more robust, we can turn these inputs into **dropdown menus** using Data Validation (Alt, D, L in PC Excel) and the SORT and UNIQUE functions:

![Dropdown Menus via Data Validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20620'%3E%3C/svg%3E "Dropdown Menus via Data Validation")

We directly reference these ranges in the Data Validation menu after selecting “List” under “Allow” and going to the “Source” area.

The FILTER function then updates the area on the right in real time as we keep changing the school/organization name and product name:

![FILTER Updating the Range Dynamically](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20358'%3E%3C/svg%3E "FILTER Updating the Range Dynamically")

If the underlying data changes because of new additions or deletions, FILTER automatically updates its output as well.

We can also use NOT conditions, dates, and many other inputs with FILTER; this just scratches the surface.

**How to Use the FILTER Function in Excel for Financial Models**
----------------------------------------------------------------

In financial models, FILTER is useful for creating **roll-ups**, **summaries**, and **aggregate tables**, especially in asset-level models.

For example, when modeling an [oil & gas company](https://breakingintowallstreet.com/kb/oil-gas-modeling/)
, you might want to summarize the production and reserves in each oil field, and in real estate, you might want to summarize the rent, net operating income (NOI), and [Cap Rates](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
 for different properties.

In this example, we’ll look at a set of cash flows from a **private equity fund** that has invested in technology and services companies.

The goal is to create a **summary table** that has the [Gross Multiple of Invested Capital (MOIC) and Gross Internal Rate of Return (IRR)](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-on-cash-return-vs-irr/)
 for each company.

These formulas are straightforward _if_ we already have the investment and exit dates, invested capital, realizations, and unrealized values for all the companies.

The **starting point** is retrieving the portfolio company names from this set of cash flows:

![Portfolio Company Names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20713'%3E%3C/svg%3E "Portfolio Company Names")

The “old way” of doing this was to copy and paste the list as values, go to Data –> Remove Duplicates, and then delete the “N/A” from the list and copy/paste this new set of names over to the summary area:

![Remove Duplicates Demonstration](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20641'%3E%3C/svg%3E "Remove Duplicates Demonstration")

This method works, but **it’s not dynamic**.

If the company names or cash flows ever change, the summary table will not update properly.

We can improve it by using the FILTER and UNIQUE functions to create a **dynamic list** of company names that updates as the cash flow data changes:

![FILTER and UNIQUE for Company Names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20378'%3E%3C/svg%3E "FILTER and UNIQUE for Company Names")

UNIQUE removes all the duplicate company names, and the FILTER, with the <>“N/A” part, removes all the “N/A” labels from the set of company names.

With the investment and exit dates, we can use a similar “multiplication trick” with XLOOKUP to find the dates based on criteria in **2 columns in this range:**

![XLOOKUP Multiplication Trick](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20349'%3E%3C/svg%3E "XLOOKUP Multiplication Trick")

Functions like this normally work by searching the top row and leftmost column in a range for matches and then returning the value at the intersection of those matches.

However, XLOOKUP can also find a matching value based on the criteria over 2 columns.

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

**Combining FILTER with IRR or XIRR**
-------------------------------------

We can also combine FILTER with traditional financial functions such as IRR and XIRR to calculate fund-level stats.

For example, what is the **Gross IRR** for this private equity fund?

The investment dates are **irregular** (see the list above), so the standard IRR function, which assumes annual intervals, does not work.

Also, we want to **exclude** Management Fees and Carried Interest (the performance fees the PE fund charges).

This is a perfect use case for XIRR (to deal with the irregular dates) combined with FILTER (to exclude certain entries in the set of cash flows).

The formula looks like this:

![XIRR with FILTER](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20732'%3E%3C/svg%3E "XIRR with FILTER")

**How to Make This PE Fund Summary More Dynamic with FILTER and XLOOKUP**
-------------------------------------------------------------------------

One issue here is that since we’re mixing traditional formulas with dynamic array functions, the “traditional formulas” section does not expand when we add new companies to this set.

For example, if we add “Company X” to this set of Investments, we get a #SPILL! error because of the “Total” row at the bottom that blocks the spill range:

![SPILL Error with Additional Entries](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20352'%3E%3C/svg%3E "SPILL Error with Additional Entries")

We can fix some of this by deleting the “Total” row at the bottom, but it still doesn’t solve the issue of the _other_ formulas not spilling down as this new company name is added to the list:

![Creating Space for the Company Name Spill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20578'%3E%3C/svg%3E "Creating Space for the Company Name Spill")

To make this model more robust, we can change the XLOOKUP formulas to return **spill ranges** that change dynamically as the company list changes.

And we can use the FILTER function to limit the lookup range to just the companies in the “Investment:” area and to limit the return range to dates that are within this area:

\=XLOOKUP($I13#, FILTER(Fund\_Companies, (Fund\_Items=K$10), “N/A”), FILTER(Fund\_Dates, (Fund\_Items=K$10), “N/A”), “N/A”)

![Making XLOOKUP Work with a Dynamic Array and Create a Spill Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20600'%3E%3C/svg%3E "Making XLOOKUP Work with a Dynamic Array and Create a Spill Range")

We could apply a similar setup to the rest of the formulas here to make all of them dynamic as well.

The key point is that instead of referencing just a **single cell**, such as I13, we should use the I13# notation to reference the **spill range** created by the FILTER and UNIQUE function combination for the company names on the left.

All of this is arguably **overkill** for a quick/simple analysis, but these features make Excel more flexible and powerful, especially in cases where a model needs to be updated continuously over long periods.

[Sign Up for Excel & VBA](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel FILTER Function - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Excel/Excel-Filter-Function-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel FILTER Function (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/Excel/Excel-Filter-Function.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&mini=true)
[Email](mailto:?subject=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[](https://www.linkedin.com/shareArticle?title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&mini=true)
[](mailto:?subject=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[](https://api.whatsapp.com/send?text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[Copy](https://breakingintowallstreet.com/kb/excel/excel-filter-function/#)
[Email](mailto:?subject=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&t=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-filter-function/)
[Pinterest](https://breakingintowallstreet.com/kb/excel/excel-filter-function/#)
[Print](https://breakingintowallstreet.com/kb/excel/excel-filter-function/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[SMS](sms:?&body=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[X](https://x.com/intent/tweet?text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-filter-function%2F&title=Excel%20FILTER%20Function%3A%20Data%2C%20Financial%20Models%2C%20and%20the%20Multiverse&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand