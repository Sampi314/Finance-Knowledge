# Extract file name from full path using formulas » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    

Extract file name from full path using formulas
===============================================

*   Last updated on October 23, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Today lets tackle a very familiar problem. **You have a bunch of very long, complicated file names & paths. Your boss wants a list of files extracted from these paths**, like below:

![Extracting file names from full path using Excel formulas - how to?](https://img.chandoo.org/f/extract-files-names-from-path-excel-formulas.png "Extracting file names from full path using Excel formulas - how to?")

Of course nothing is impossible. You just need correct ingredients.

![What we need to extract file names from full path text - Excel formulas](https://img.chandoo.org/f/exract-files-names-from-path-what-you-need.png "What we need to extract file names from full path text - Excel formulas")

I cannot help you with a strong cup of coffee, so go and get it. I will wait…

Back already? well, lets start the formula magic then.

Extracting file name from a path
--------------------------------

If you observe the file paths carefully, to extract the file name, we need to know,

*   Position of last \\ in the full path text

Of course there are many methods find where the last \\ is. You can find a very excellent summary of these techniques in our [formula forensics #21 – finding the 4th slash](http://chandoo.org/wp/2012/05/17/formula-forensic-no-021/)
.

Today, let us see a new technique (well, sort of).

### Finding the position of last \\ using formulas

Before writing any formula, first let me clarify the only assumption:

*   File path is in cell B4

**Now, last \\ is nothing but first \\ when read from right.**

Read that line again.

Got it? Good, lets move on.

**How do we find the first \\ from right?**

If we can list down all individual characters from path right to left, then we just have to find the first \\ in that.

### Listing down individual characters from a given text

To get 5th character from text in B4, we can use MID formula like this:

\=MID(B4,5,1)

Suppose you want both 5th and 6th characters from B4, you can use:

\=MID(B4,{5,6},1)

This formula returns an array of 5th and 6th characters from the text in B4.

Cool, extending the logic, =MID(B4, {6,5},1) would give 6th & 5th characters in B4.

**Idea!**

If we can _replace {6,5} with decreasing numbers starting from length of text B4 all the way to 1_, then we can list all characters in B4, right to left.

But this leads us to next problem – **listing numbers from a specific value (length of B4) to 1 in descending order**.

### Listing numbers from _n_ to 1 in that order

We can use ROW() formula to generate sequence of numbers like this:

\=ROW(1:10) will give {1,2,3…,10}

_note: this returns an array, so you need to use it with Ctrl+Shift+Enter_

So if we can use =ROW(1:LEN(B4)) we could get numbers from 1 to length of text in B4 {1,2….LEN(B4)}

**Unfortunately** this will not work as 1:LEN(B4) is not a valid reference.

But we can fix that with INDIRECT, like this:

\=ROW(INDIRECT(“1:” & LEN(B4)))

**Tip:** INDIRECT formula lets you construct a reference by using values in other cells as shown above.

**Alternative:** You can also use OFFSET to get the same result like this: =ROW(OFFSET($A$1,,,LEN(B4))). [More on OFFSET here](http://chandoo.org/wp/2012/09/17/offset-formula-explained/ "OFFSET formula – Explained")
.

#### But wait…

So far, we have only generated numbers from 1 to _n._ **But we need numbers from n to 1.**

No sweat, we just subtract the numbers {1,2…n} from n+1 to get the list {n,n-1,n-2….2,1}

**Like this:**

\=LEN(B4)+1 – ROW(INDIRECT(“1:” & LEN(B4)))

### Using these numbers to list characters in file path in reverse order

Take a sip of that coffee, its getting cold!

Now, lets integrate our numbers in to MID like this:

\=MID(B4, LEN(B4)+1 – ROW(INDIRECT(“1:” & LEN(B4))), 1)

The blue portion gives you numbers {n…2,1}

The orange portion gives you letters from right to left.

### But we wanted the last \\

Oh right. We do not need these letters from right to left. We instead want to find the last \\ in our file path. So now we just ask Excel where the first \\ is in this reversed text.

\=MATCH(“\\”, MID(B4, LEN(B4)+1 – ROW(INDIRECT(“1:” & LEN(B4))), 1), 0)

Blue portion gives you letters in reverse order

Orange portion finds the first \\ in that.

Tip: [Learn more about MATCH formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)
.

### Extract the file name

Once you know where the last \\ is, finding the file name is easy.

use =MID(B4, position\_of\_last\_slash \+ 1, LEN(B4))

We need to +1 because we do not want the slash in our file name.

### Demo of the entire formula in action

Okay, lets see all these steps in action in one go.

![Extract file name from full path using Excel formulas - Demo](https://img.chandoo.org/f/extract-file-names-from-full-path-formula-demo.gif "Extract file name from full path using Excel formulas - Demo")

### How to find the extension?

Extension is few letters added at the end of file to indicate its type. For example, excel files usually have xls, xlsx, xlsm as extension.

_**So how to find this extension?**_

Extension & file name are separated by a dot .

But often file name itself can have a dot.

In other words, Extension is text in the file name followed by _**last dot**_.

Sounds like same problem as finding the last \\ and extracting file name. So I will skip the details.

**But assuming the file name is in D4, extension can be found with** =RIGHT(D4,MATCH(“.”,MID(D4,LEN(D4)-ROW(INDIRECT(“1:”&LEN(D4))),1),0))

### NOTE on both formulas

Both file name & extension formulas are array formulas. This means after typing them, you need to **press Ctrl+Shift+Enter to see correct result**.

### Bonus tip: Getting the file names & path from a folder

If you ever want to list down all files in a folder use this.

1.  Open command prompt (Start > Run > Cmd or Start > Cmd)
2.  Go to the folder using CD
3.  Type DIR /s/b >files.csv
4.  Close command prompt

Now you can see all the files in that folder in files.csv. Double click on it to open in Excel and run your magic 🙂

### Download Example workbook

[**Click here to download the example workbook**](https://img.chandoo.org/f/extract-file-name-from-path.xlsx)
. The file uses slightly different formulas. But works just the same. Examine it and learn more.

### How do you extract file names & as such?

Do you use formulas or do you rely on some other technique to extract portions of text like file names, mail addresses etc. _**Please share your tips & ideas using comments.**_

### Extract often? You will dig this.

Analysts life is filled with 3 Es – _extraction, exploration & explanation_. And like a good assistant, Excel helps you in all 3.

_**If you find yourself with a shovel, bucket and boat load of data often, you are going to enjoy these articles:**_

*   [Extract numbers from text using formulas](http://chandoo.org/wp/2012/06/19/extract-numbers-from-text-excel/)
     \[[and using macros](http://chandoo.org/wp/2012/06/26/extract-numbers-excel-vba/)\
    \]
*   [Extract dates from text](http://chandoo.org/wp/2012/08/17/extract-dates-from-text/)
    
*   [Extract user names from email addresses](http://chandoo.org/wp/2010/01/19/usernames-from-email-formulas/)
    
*   [Extract duplicates or unique values from a list](http://chandoo.org/wp/2008/11/06/unique-duplicate-missing-items-excel-help/)
    
*   [Extract data from multiple files & place in one sheet](http://chandoo.org/wp/2012/04/09/consolidate-data-from-different-excel-files-vba/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [53 Comments](https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [extract](https://chandoo.org/wp/tag/extract/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [len()](https://chandoo.org/wp/tag/len/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mid()](https://chandoo.org/wp/tag/mid/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    

[PrevPreviousPlease help me design our new product: Vitamin XL](https://chandoo.org/wp/vitamin-xl-survey/)

[NextEven faster ways to Extract file name from path \[quick tip\]Next](https://chandoo.org/wp/extract-file-name-from-path/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/extract-file-name-from-full-path-using-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ