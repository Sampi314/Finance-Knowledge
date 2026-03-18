# Top 10 ways to fix an unbalanced balance sheet

**Source:** https://financialmodelling.forvismazars.com/how-to-speed-up-your-models-part-1-2

---

Top 10 ways to fix an unbalanced balance sheet
----------------------------------------------

[Forvis Mazars Financial Modelling](https://financialmodelling.forvismazars.com/)
[Financial Modelling](https://financialmodelling.forvismazars.com/online-resources/blog-types/financial-modelling-blog-types/)

Top 10 ways to fix an unbalanced balance sheet

[](http://twitter.com/share?text=Top+10+ways+to+fix+an+unbalanced+balance+sheet&url=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
[](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
[](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
[](mailto:?subject=Top%2010%20ways%20to%20fix%20an%20unbalanced%20balance%20sheet&body=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)

Top 10 ways to fix an unbalanced balance sheet
==============================================

By [Shaun Comley](https://financialmodelling.forvismazars.com/author/shauncomley/ "Posts by Shaun Comley")

Tuesday 22nd June 2021

Financial statements are a series of double entries. When we are setting up our Financial Statements, we must make sure we bring in both sides of the double entries to ensure our balance sheet balances. As Isaac Newton’s Third Law states ‘For every action there is an equal and opposite reaction’; to become a balance sheet king you must remember, ‘For every Debit, there is an equal and opposite Credit’

A balance sheet that doesn’t balance is the nemesis of many a modeller. There is nothing more infuriating than needing to deliver a model and just not being able to track down a balance sheet error, especially as the clock ticks away late into the night.

Don’t worry, I have felt the pain. The below are 10 practical steps that have been finely tuned after sleepless nights and 15 accounting exams. This article will hopefully speed up the process of debugging what is causing the imbalance and help avoid this issue reoccurring during your modelling career.

### 1\. Make sure your Balance Sheet check is correct and clearly visible

Making the correct Balance Sheet check may seem obvious however, there are a few things we must ensure:

**a) Net assets equals total equity**

Starting from the most basic item, we must make sure that we have correctly linked our formula and that we are checking that net assets less total equity is equal to zero.

**b) Appropriate rounding**

Excel isn’t perfect, despite what we all may think, Excel only stores up to 15 significant figures. When we are building complex financial models, we will use all 15 significant figures. This can cause really small differences in our net asset and equity. However, when decision making, we may only care to the nearest dollar or cent. Using the ROUND function will ensure that our check has the level of tolerance that is material.

**c) Check the absolute difference**

Rather than checking each period we should create a global check of each period’s deltas. The most efficient way to do this is by summing all the deltas however, we could have an equal and opposite delta. If this occurred the global check would provide a false result. To avoid this error, always calculate the absolute difference.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/BS-1.png)

**d) Clearly visible throughout the model**

Once we achieve a balance sheet that does balance, we need to make this check visible throughout the model. This should sit on the top ribbon of our spreadsheet, above any freeze panes you have on your calculation sheet. This will ensure that when we make any updates to model, if we cause an imbalance, we can diagnose it straight away. 

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/BS-2.png)

There are alternative methods to Balance Sheet checks. Many modellers will use a logic check to ensure that the delta between equity and net assets is below a certain tolerance number. This works effectively as a check; however, this method won’t help identify what is causing the imbalance.

### 2\. Check that the correct signs are applied

Once we have created our check, our next step is to make sure income and assets are positive and costs and liabilities are negative. An extremely common mistake is missing a negative sign when incorporating items into financial statements. It is so easy to miss and can be hard to pick up. However, a run through of each line item on your Cashflow, Profit and Loss and Balance Sheet will help you identify these errors and is a super easy win.

### 3\. Ensuring we have linked to the right time period

Two of Mazars’ guiding themes are “Keep it simple” and “Get it right”, this is extremely relevant when setting up financial statements.

To “[Keep it simple](https://financialmode1.wpengine.com/mazars-financial-modelling/guiding-themes/mazars-keep-it-simple/)
”, Financial Statements should just be links to calculations within the workbook, we should not be performing calculations within them, otherwise there is a high potential for us to exclude this from another section of the statements.

To “[Get it right](https://financialmode1.wpengine.com/mazars-financial-modelling/guiding-themes/mazars-get-it-right/)
”, we should ensure that we have consistent timing across all our sheets in the model. This will mean when we are linking on our financial statements, we are linking to the same column on our calculation sheet.

For example, if our calculation timeline starts in Column J, we are linking to Column J on our calculation sheets. By doing this we will avoid any misalignment error.

We can then do a simple check that we avoided any misalignment error for each of the first columns. A quick keyboard shortcut to help this is “Ctrl + \`”, which will show formulas (“Ctrl + \`” will switch it back to normal)

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/bs-3.png)

### 4\. Check the consistency in formulae

A key pillar of almost every modelling best practice is consistency in formulae across the row. If we don’t have that consistency, it’s highly likely that your balance sheet doesn’t balance. A way to check formulae consistency is using Go to Special > Row differences. To do this highlight your financial statements formulae and use the shortcut “Ctrl + \\”. This shortcut will highlight the cells in that range that have row inconsistencies. We then suggest colouring those cells in a bright colour to pick them out easily.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/BS-4.png)

From here you then need to identify what is the correct formula to use. Don’t simply copy the formula on the left across, you may have corrected the formula midway across the sheet accidently (I’ve made this mistake before).

### 5\. Check all sums

One of the most common errors when building financial models is missing rows within your summed range. When we insert a row above a sum, the range doesn’t update to include that new row.

![](https://financialmode1.wpengine.com/wp-content/uploads/2021/06/BS-5.png)

A quick run through each of the Balance Sheet’s closing balances and your Financial Statement calculations to make sure you haven’t made this mistake. Check a couple throughout the row as another common error is to update the sum for the first column and not copying it across the row. This can also be done through checking the consistency in formulae as suggested in point 4.

It is also important to check the lines within your Cashflow and Profit and Loss to ensure that these are flowing down to your net cashflow and net profit after tax respectively. It’s very common to miss out a line reference in your Cashflow available for debt service (CFADS) or EBIT.

### 6\. The delta in Balance Sheet checks

The above were the easy wins and hopefully you’ve been able to find your Balance Sheet differences. However, it becomes a little trickier from this point on, as its highly likely that you excluded something within your financial statements. So how do we find something that isn’t there?

This is where we create a second check, commonly known as “Balance sheet check 2”, which calculates the delta between two balance sheet checks.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/BS-6.png)

This will allow us to see patterns in how our Balance Sheet imbalance changes,

which can be more informative than the value of the total imbalance. How then do we diagnose these:

Firstly, check to see if you have an exact match for difference within your financial statements. If you can find an exact match of the difference with one of the line items in your financial statements, it would suggest that you have only incorporated one side of the double entry

**a) Look for an exact match**

**b) Consistently the same difference**

This is highly likely to be a constant expense or revenue which is not escalated. An example of what is missing is straight line depreciation.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/bs-7.png)

**c) Slowly increasing/decreasing difference**

When this is the case, we will need to look at things that are affected by inflation or interest rates. An increasing difference would suggest an item affected by inflation such as the revenue or expense, as these values would increase over time. A decreasing difference would suggest an item affected by interest rates, this is as over time the balance will decrease and thus the associated interest and payments. This is not necessarily always the case but should hopefully generate ideas of where to focus your efforts.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/bs-8.png)

**d) Jumps in the difference**

This is a due to recurring items that don’t happen every period. Examples of this would be debt repayments or capex spend.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/bs-9.png)

**e) Unbalanced for a set period**

Look at the time horizon that the balance sheet is imbalanced for, was a certain facility active during this period and no other period, this could be the cause of the difference.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/bs-10.png)

Although this check won’t necessarily give you the exact reason for your balance sheet not balancing this will isolate your search. In addition, hopefully when you see the second check, you’ll start to recognise the numbers that you may be missing. You’ll be surprised how familiar numbers become from across the model. The more balance sheets you debug the more familiar you’ll become with this balance sheet check two.

### 7\. Double and half the Balance Sheet check

This is a classic accounting trick; I was taught this while doing my accounting exams and financial audit. Within point 7 we have talked about identifying the difference using patterns, if we haven’t seen a pattern or a number, we are familiar with, by doubling or halving the difference this may allow us to find it. This will often help find items where we have put the incorrect sign and in which case have done two debits for example.

### 8\. Work from right to left

While trying to debug what’s causing your imbalance, work from right to left. We need to identify the area where your Balance Sheet isn’t balancing and thus towards the end of your forecast there are likely to be less items active, for example debt facilities. This will allow us to refine our search, we can then work back to the start of the forecast, hopefully the items that aren’t active all the way to the end could be the causes of the imbalance.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2021/06/bs-11.png)

### 9\. Opening balance testing

When reforecasting of an existing Balance Sheet, it’s very easy to make mistakes and not properly incorporate all items. A way to check where these numbers are properly incorporated is changing the numbers and see what happens to your balance sheet check. When changing numbers in your opening Balance Sheet, the retained earnings should be the balancing number (net assets less share capital).

If you change an item on your opening Balance Sheet and your Balance Sheet delta changes, we know that there is an issue with this item. If there is no movement, it means that the appropriate debits and credits have been incorporated and we can move to the next Balance Sheet item.

### 10\. Check changes period to period of Balance Sheet items

The last chance of resolving your issue, is to go through each item on the balance sheet from period to period (remember working right to left) and checking that the balance sheet movements are reflected in the profit and loss and or the cashflow. This can be quite a time-consuming activity but is a systematic way of ensuring all debits and credits have been correctly incorporated in the financial statements and should lead to you finding the imbalance.

### Before your model is good to go

A test you should do before you’re finished is to run through all scenarios. Often in our base case financial model, certain functionality won’t be active for example, a Debt Service Reserve Account (DSRA). In our base case we might not expect to use the DSRA, but it may be required in some downside cases. An easy way to do this would be to include your checks within your scenario table to ensure you can detect balance sheet imbalances in non-active scenarios.

If your balance sheet still doesn’t balance after all these steps, you may benefit from attending one of our training courses. Our full course portfolio can be found [here](https://financialmode1.wpengine.com/the-academy-financial-modelling-courses/course-portfolio/)
.

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

*   [](mailto:?subject=Top%2010%20ways%20to%20fix%20an%20unbalanced%20balance%20sheet&body=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
    
*   [](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
    
*   [](http://twitter.com/share?text=Top+10+ways+to+fix+an+unbalanced+balance+sheet&url=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
    
*   [](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/)
    

*   [Legal and privacy](https://www.forvismazars.com/uk/en/contact-us/legal-and-privacy)
    

Copyright 2026 - Forvis Mazars

This website uses cookies.

Some of these cookies are necessary, while others help us analyse our traffic, serve advertising and deliver customised experiences for you. For more information on the cookies we use, please refer to our [Privacy Policy](https://financialmodelling.forvismazars.com/top-10-ways-to-fix-an-unbalanced-balance-sheet/#)
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