# 20 Advanced Excel Functions and Formulas (for Excel Pros)

**Source:** https://trumpexcel.com/advanced-excel-functions-formulas

---

[Skip to content](https://trumpexcel.com/advanced-excel-functions-formulas/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/advanced-excel-functions-formulas/#below-title)

Excel has 450+ functions that can do a range of awesome things. If you’ve used Excel even for a few days, I am sure you have heard of functions like VLOOKUP, SUMIF, COUNTIF, and so on.

And what is more awesome is that one Excel function – a formula that consists of two, three, or more functions.

With a combination of functions, you can create some advanced Excel formulas that can do some incredibly advanced things with a press of a key.

So if you’re an Excel aficionado like me, I am sure you’re going to love this article. In this article, I will cover the 20 advanced Excel functions you should know.

I will also share examples of some advanced formulas you can create with these advanced functions.

A quick note about advanced functions/formulas: By advanced, I mean functions that would need some know-how and are not usually used by basic Excel users (such as SUM or COUNT).

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/advanced-excel-functions-formulas/#)

XLOOKUP Function
----------------

[XLOOKUP](https://trumpexcel.com/xlookup-function/)
 is the king of advanced functions (Microsoft hasn’t given this title to any function, but I am sure no one deserves it more than this function).

It is a new function that is available in Excel 2021 and Excel for Microsoft 365. This means people using the earlier versions of Excel won’t be able to use it.

XLOOKUP is a refined version of VLOOKUP, that addresses some of the drawbacks that VLOOKUP has.

You can use this function in situations where you need to scan a list of values in rows or columns and find out if the list contains the value you’re looking for (called the lookup value).

It also allows you to find the value, and then return any other value from the same row or column.

If you’re still confused about what this function does, consider this – you go to a newly opened café close to your house and you want to eat something. so you get their menu and start scanning the menu from top to bottom.

When you identify an item you would want to order, you look to the right to check the prices.

And that’s what XLOOKUP does for you. It can scan the list, find out the position of the lookup value, and return the value from any corresponding column in the same row.

There are many amazing things you can do with XLOOKUP, and I have covered some in the video below:

**Note**: If you use XLOOKUP and share the file with someone who is using an older version of Excel, the formulas won’t work in their workbooks. So if that’s the case, it’s best not to use XLOOKUP

Also read: [Excel Skills (Basic, Intermediate, and Advanced)](https://trumpexcel.com/excel-skills/)

VLOOKUP Function
----------------

VLOOKUP had been the undisputed king of Excel functions, till the XLOOKUP function arrived. Since many people are still not using Excel 2021 or Excel for Microsoft 365, they don’t have access to XLOOKUP.

So, for them, VLOOKUP is the function they must know. For advanced formula users, a complete understanding of using VLOOKUP can really make a difference in their work.

Just like XLOOKUP, VLOOKUP also scans a list in a column and can return the matching lookup value or any value from any column in the same row.

If you want to learn how to best use the VLOOKUP function, check out this detailed tutorial on this advanced formula: [10 VLOOKUP Examples For Beginner & Advanced Users](https://trumpexcel.com/excel-vlookup-function/)

Here are some advanced formula examples of using VLOOKUP:

*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    
*   [Use VLookup to Get the Last Number in a List in Excel](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/)
    
*   [Avoid Nested IF Function in Excel…VLOOKUP to Rescue](https://trumpexcel.com/avoid-nested-if-function-vlookup/)
    
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    

Also read: [How to Describe Excel Skills in a Resume?](https://trumpexcel.com/excel-skills/resume/)

INDEX / MATCH Function
----------------------

The combination of INDEX and MATCH functions can do wonders. So if you desire to learn about advanced formulas in Excel, you must learn how this magical combination works.

Till the time XLOOKUP arrived, many advanced Excel users preferred using INDEX/MATCH over VLOOKUP (and this combination can take care of some of VLOOKUP’s drawbacks). There used to be a hot debate on which formula is better [VLOOKUP vs INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
.

Even with XLOOKUP, I highly recommend you learn using INDEX/MATCH.

While individually these functions aren’t that useful, when you combine them, it’s a powerful tool for advanced Excel formula users.

You can read the following guide where I cover some basic and advanced usage of the INDEX/MATCH formula – [INDEX & MATCH Functions Combo in Excel (10 Easy Examples)](https://trumpexcel.com/index-match/)

Also read: [Formulas Not Working In Excel](https://trumpexcel.com/excel-formulas-not-working/)

SUMPRODUCT Function
-------------------

Outside the realm of lookup and reference formulas (i.e., XLOOKUP, VLOOKUP, and INDEX/MATCH), SUMPRODUCT is one of those functions that advanced Excel users love.

Its name may fool you into thinking that it’s a math or stat formula that can add multiple numbers, but it’s way more than that.

Initially, the Excel team wanted this function to do calculations where it can give you the sum of the product in two columns.

While this is a decent use case, Excel users got crafty and found out that it can be a lot more than this.

Advanced Excel users often use the SUMPRODUCT formula for conditional sums or conditional calculations.

Suppose you have a dataset of salespeople, their region, and their sales numbers. Then you can use SUMPRODUCT to:

*   Only add sales value for a specific region (or more than one region)
*   Only add sales values above a specific value
*   Add sales values above or below a specific value (OR condition)

You can check the video below where I show SUMPRODUCT examples:

Note: The SUMPRODUCT function is quite popular among Excel users who [create dashboards](https://trumpexcel.com/creating-excel-dashboard/)
 and reports. Excel has introduced a new SUMIFS function that can do some of what the SUMPRODUCT function does, but not everything. So if you want to learn advanced Excel formulas, I would suggest you learn this one too.

SUMIF/COUNTIF & SUMIFS/COUNTIFS Functions
-----------------------------------------

I have clubbed these four functions together as they have the same modus-operandi.

You can use this to conditionally sum or count from your dataset.

For example, if you have a list of names, and you want to quickly count how many times a specific name appears in the list, you can use the COUNTIF formula.

And similarly, if you have a data set where you have the Sales Rep names and their sales values, and you want to get the sum of all the sales done by a specific sales Rep, you can use the SUMIF function.

And in case you need to check for multiple conditions, you can use the COUNTIFS or SUMIFS formulas.

For example, if I have a data set with a Date column, a Sales Rep name column, and their Sales values, I can use the SUMIFS formula to get the sum of all the sales done by a specific sales Rep in a specific month.

Since there are two conditions to check (the sales Rep name and the date),  you need to use the SUMIFS formula. Similarly, if you have multiple conditions to check when getting the count in a dataset, use the COUNTIFS formula.

FILTER Function
---------------

[FILTER](https://trumpexcel.com/filter-function/)
 is a new function in Excel 2021 and Excel for Microsoft 365, and it’s amazing.

As the name suggests, you can use it to filter a dataset in Excel and extract the results.

This was one of the most requested functions in Excel, as the workaround without the FILTER function is quite long and complex.

To give you a simple example to showcase the FILTER function utility, suppose you have a dataset with Sales Rep names, their regions/countries, and their sales values.

With the FILTER function, you can quickly filter all the records for any specific country. And to make it even more powerful, instead of hard-coding the name of the country in the formula, you can put it in a cell and refer to that cell in the formula.

This way, you can simply change the name of the country in the cell, and the formula would instantly give you all the records for that country.

Below is a video I made showing some advanced examples of the FILTER function.

SORT & SORTBY Function
----------------------

Again, two new functions in Excel 2021 and Excel for Microsoft 365.

Just like the FILTER function, these were much needed as there was no easy way to sort the data dynamically with a formula.

Before the introduction of this formula, most of this data sorting was done using the sort feature in Excel which gives you a static result.

This means that in case you change your original data set, the resulting sorted data wouldn’t update and you’ll have to sort it again.

But not anymore.

Using the SORT function, you can quickly sort any data set based on the specified row or column. It also gives you the flexibility to choose the sort order (i.e., ascending or descending).

So if you have a data set and you want to sort this data based on one specific column, you can use the SORT function.

The SORTBY function provides a little more functionality while sorting the data using a formula. With this function, you can sort based on multiple columns.

For example, if you have 2 columns, where the first column has the name of the region (such as East, West, North, South), and the other column has the sales values, then you can use the SORTBY function to first sort this based on the region name and then based on the sales values.

Also read: [How to Sort By Color in Excel (in less than 10 seconds)](https://trumpexcel.com/sort-by-color/)

UNIQUE Function
---------------

UNIQUE Is again a new function that is available only to the users of Microsoft 365.

Just like the SORT and the SORTBY function, this one was also desperately needed.

As the name suggests, the UNIQUE function will give you a list of unique names or items in a dataset.

Before this function, the way to do this was by using the [remove duplicate functionality](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
, or the [advanced filter functionality](https://trumpexcel.com/excel-advanced-filter/)
.

But even with these inbuilt functionalities, with large data sets and more conditions, it used to become complicated.

And of course, the result used to be static, which meant that in case the original data changes, the resulting data would not update and you will have to repeat the process again.

TEXTJOIN Function
-----------------

TEXTJOIN is a relatively new function that was introduced in Excel 2019, edit solves a major problem.

TEXTJOIN allows you to quickly combine the content of a selected range of cells without creating along concatenate formula or using the & sign a gazillion times.

So if you have multiple items in different cells in a row or column, and you want to quickly combine them, you can do that using one single formula.

It also allows you to specify a delimiter such as a space character or a comma, so that all the combined cells would have that delimiter between the content of the cells.

To be honest, this is a very simple formula that even the most basic Excel user can use, but if you are an advanced excel user, it is unforgivable for you to use concatenate and & combine cells (you ought to know better)

Also read: [How to Combine First and Last Name in Excel](https://trumpexcel.com/combine-first-and-last-name-excel/)

IFS Function
------------

IFS is another function that was introduced in Excel 2019 (way too late if you ask me).

I love the IF function and it has done a lot of heavy lifting for me over the years. But the dude has limitations.

To begin with, you can only check for two conditions, so if you need to check for three or more, you end up with a long [nested if formula](https://trumpexcel.com/avoid-nested-if-function-vlookup/)
.

And God forbid if you have to check for 5, 10, or 15 conditions, I can imagine what horror your formulas would look like.

To ease the pressure on the overworked IF formula, Microsoft introduced the IFS function which can check for multiple conditions.

So if you’re a teacher grading students or a manager who needs to decide how much Commission your sales reps get based on their sales value, you don’t need to create long convoluted IF formulas, instead, you can use the IFS function.

Also read: [Test Multiple Conditions Using Excel IFS Function](https://trumpexcel.com/excel-ifs-function/)

IFERROR Function
----------------

You can’t call yourself an advanced Excel formula user if you’re Excel sheet is full of errors such as #N/A or #REF! or #DIV/0!.

While getting these errors may be out of your control sometimes, IFERROR allows you to handle these errors by replacing them with something more meaningful.

For example, if you’re using the VLOOKUP formula and it cannot find the lookup value, it is going to return the NA error. with the [IFERROR formula](https://trumpexcel.com/excel-iferror-function/)
, you can replace this NA error with something more meaningful such as “Look-up value not found” or “Data not available”.

Also read: [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)

OFFSET Function
---------------

OFFSET function can be used in very specific situations, and most advanced Excel users would rarely need to use it.

OFFSET function allows you to offset the reference by this specified number of rows or columns.

For example, I can use the OFFSET function to offset the reference A1 by two rows and two columns so that it gives me C3 (which is the reference of a cell that is two rows below and two columns to the right)

If you’re interested in learning how the OFFSET function works, I have a detailed tutorial where I cover some examples of [how to use the OFFSET formula](https://trumpexcel.com/excel-offset-function/)
.

One important thing you need to know about the OFFSET function is that it is [volatile](https://trumpexcel.com/excel-volatile-formulas/)
, which means that anytime there is a change in your worksheet the function would be re-calculated.

While you won’t notice any changes if you are using the OFFSET function in a couple of cells, if you’re using it inner bigger data set or an entire row or column, then it could [slow down your Excel file](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
.

FIND / SEARCH Function (With Wildcard Characters)
-------------------------------------------------

[FIND](https://trumpexcel.com/excel-find-function/)
 and [SEARCH](https://trumpexcel.com/excel-search-function/)
 are two similar functions that allow you to search for a given text in a cell and return the starting position of the string that you searched for.

You cannot claim to be an advanced Excel formula user if you do not know how to use the full power of FIND/SEARCH functions.

While these functions won’t be of much help on their own, when you combine these with other text functions LEFT/RIGHT/MID, you can do some serious text manipulation.

For example, if you have a column full of e-mail addresses, and you want to get the user ID and not get everything after the @ symbol, you can do that using the FIND or the SEARCH function.

To do this, we’d first have to use one of these functions to find the position of the add the rate in the cell, and once you have this position you can use this value within the left function to extract everything which is to the left of the @ symbol.

_Note that you cannot use [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
 in the FIND formula however you can use them in the SEARCH formula_

RIGHT / LEFT / MID Function
---------------------------

Working with text data is a regular part of many advanced Excel users’ day-to-day work.

While there are many text manipulation options available in Excel (such as [Text to Columns](https://trumpexcel.com/excel-text-to-columns-examples/)
 or Power Query), many advanced Excel users still prefer going the formula way.

[RIGHT](https://trumpexcel.com/excel-right-function/)
, [LEFT](https://trumpexcel.com/excel-left-function/)
, and [MID](https://trumpexcel.com/excel-mid-function/)
 functions allow you to extract a part of the text string.

For example, if you have an e-mail ID such as AverageJoe@email.com, you can use the LEFT function to extract only the username from this e-mail ID, or you can use the RIGHT function to extract the domain name (which would be email.com).

With the MID function, you can extract text from the middle of the text string. For example, if I want to extract the domain name between @ and the . (dot), I can easily do this using the MID function.

These text functions are not quite useful on their own, but when you combine them with other formulas such as LEN or FIND, you can do some incredibly advanced stuff with them.

Here are some advanced formula examples of using RIGHT/LEFT/MID functions:

*   [Remove Characters From Left in Excel (Easy Formulas)](https://trumpexcel.com/remove-characters-from-left-excel/)
    
*   [Extract Last Name in Excel (5 Easy Ways)](https://trumpexcel.com/extract-last-name-excel/)
    
*   [How to Extract the First Word from a Text String in Excel (3 Easy Ways)](https://trumpexcel.com/extract-first-word-excel/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    

REPLACE / SUBSTITUTE Function
-----------------------------

[REPLACE](https://trumpexcel.com/excel-replace-function/)
 and [SUBSTITUTE](https://trumpexcel.com/excel-substitute-function/)
, as the name clearly suggests, allows you to find some text in a text free, and replace or substitute it with what you want.

With the REPLACE function, you can specify the starting position and the total number of characters that you want to replace with the specified text string.

On the other hand, with the SUBSTITUTE function, you can specify the text string that you want to replace with another text string. For example, if you have a data set where you want to replace the word ‘Private’ with ‘Pvt’, you can easily do that using the SUBSTITUTE function.

While these functions are quite useful on their own themselves, they’re often used with other text functions such as LEN, TRIM, or RIGHT/LEFT/MID

IMAGE Function
--------------

IMAGE is a brand new function in Microsoft 365 (at least at the time of writing this article).

For a long time, I wished Excel had a function that would allow me to use a URL and insert an image from that URL into a cell in Excel.

And finally, my wish has been granted.

With the IMAGE function, you can use a URL of an image within the cell, and it would insert the image into the cell itself.

Earlier, to place an [image inside a cell](https://trumpexcel.com/insert-picture-into-excel-cell/)
, you had to manually add the image to the worksheet and then position it so that it fits in the cell.

While I don’t expect this function to be used by many average Excel users, some advanced Excel users can use these while creating dashboards.

For example, you can create a template, where the function fetches the image of the product or the logo of the company based on the URL.

At the risk of sounding disloyal to Excel, we need to thank Google Sheets for this. IMAGE function has been a part of Google Sheets for many years, and many Excel users (such as myself) I’ve been asking for it to be added to Excel well. So in the interest of humanity, Excel copied this function from Google Sheets (and yayy that they did)

SMALL / LARGE Function
----------------------

[SMALL](https://trumpexcel.com/excel-small-function/)
 and [LARGE](https://trumpexcel.com/excel-large-function/)
 are two simple formulas that do one simple thing – give you the Kth smallest or largest value from a data set.

For example, I can use the SMALL function to give me the second smallest or the third smallest value from a range of cells.

And why include these two formulas as part of my best-advanced formula tutorial – because I have used them in situations where no other function could do what these could do.

For example, I have used these to manage outliers in my data set, use them with formulas that return an array (such as the INDEX function), and get the top three or top five values from it.

I agree that these two formulas have limited usage in advanced Excel formulas, but I would still urge you to keep them in your back pocket in case you need them.

Also read: [How to Find Outliers in Excel (and how to handle these)](https://trumpexcel.com/find-outliers-excel/)

SEQUENCE Function
-----------------

SEQUENCE is also a new function that’s available in Excel 2021 and Excel with Microsoft 365.

[SEQUENCE function](https://trumpexcel.com/excel-functions/sequence/)
 would fill a range of cells with a sequence of numbers. you can specify how many rows and columns you want to fill, the starting number, and the step between each number.

For example, if I enter the below formula in cell A1, it is going to fill cells A1 to A10 with a sequence of numbers starting from 1 to 10.

\=SEQUENCE(10,1,1,1)

While there were other methods to do this earlier in Excel (such as manually entering the data and then using the fill handle, or using the fill series method), having a formula do it makes it not only more convenient But necessary in some situations.

One advanced use case where this function could be useful is when you’re creating a calendar where you want to fill a grid of cells with a sequence of numbers.

You can check out the [Excel calendar template](https://trumpexcel.com/interactive-calendar-excel/)
 I created using this function.

But more importantly, I’ve often come across situations where I needed a sequence of numbers as a part of my formula. Earlier, I had to rely on tricks such as using the ROWS or COLUMNS formulas, now I can easily do that using the SEQUENCE function.

Also read: [7 Quick & Easy Ways to Number Rows in Excel](https://trumpexcel.com/number-rows-in-excel/)

WORKDAY / NETWORKDAYS Function
------------------------------

[WORKDAY](https://trumpexcel.com/excel-workday-function/)
 and [NETWORKDAYS](https://trumpexcel.com/excel-networkdays-function/)
 functions are amazing. When I started using Excel and I was learning these formulas, I thought of them as just another formula that could be useful in some situations.

But the more I have learned about these functions, the more I believe you need to know how to use them well to be called an advanced formula user.

At the outset, these formulas do simple stuff:

*   WORKDAY – It calculates the date after the specified number of working days
*   NETWORKDAYS – It total number of working days between two given dates

And since we have working days and non-working days in a week (as well as holidays), these functions automatically account for weekend days and you can also specify the holidays that would be ignored.

And since this was not enough, as many people had different weekend days than Saturday and Sunday, Excel released two add-on functions, [WORKDAY.INTL](https://trumpexcel.com/excel-workdayintl-function/)
 and [NETWORKD](https://trumpexcel.com/excel-networkdays-intl-function/)
[A](https://trumpexcel.com/excel-networkdays-intl-function/)
[YS.INTL](https://trumpexcel.com/excel-networkdays-intl-function/)
.

These international functions allowed users to choose the days that would be considered weekends.

But wait, there is more.

What if you were working in a part-time job and you want to calculate data after a specific number of work days or the total number of work days between two given dates?

You can do that as well.

The international versions of these functions allow you to specify all the working days and not working days and then it will do the calculation based on it.

For example, you can specify that only Mondays and Thursdays are working for you and all the other days are non-working days.

Also read: [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)

TEXTAFTER / TEXTBEFORE Function
-------------------------------

While Excel already had some really amazing text functions, they added TEXTBEFORE and TEXTAFTER in the Microsoft 365 version of Excel to make things even easier.

Earlier if you had to extract the first name from the full name, you had to use a combination of the LEFT function with the FIND function. But with the TEXTBEFORE function, you can easily extract all the text before a given specific delimiter.

Similarly, with TEXTAFTER, you can extract all the text after a given delimiter instead of using a combination of formulas.

I have recently started using these two functions and I can tell you that these are a great improvement over the existing text functions and simplifies things to a great extent.

In this tutorial, I have covered the **top 20 Advanced Excel functions** based on my understanding and years of experience in working with Excel.

While this list could be slightly different for you based on the kind of work you do, in general, if you master these 20 advanced Excel functions and how to use them in advanced formulas, you’ll be way ahead of the curve.

I hope this article has been useful to you.

**Other Excel tutorials you may also find useful:**

*   [FREE Online Excel Training (12+ Hours) | Learn Excel (Basic/Advanced)](https://trumpexcel.com/learn-excel/)
    
*   [10 Advanced Excel Charts that You Can Use In Your Day-to-day Work](https://trumpexcel.com/advanced-charts/)
    
*   [VLOOKUP vs XLOOKUP Function – What’s the Difference?](https://trumpexcel.com/excel-functions/vlookup-vs-xlookup/)
    
*   [Excel LAMBDA Function](https://trumpexcel.com/excel-functions/lambda/)
    
*   [REGEX Functions in Excel](https://trumpexcel.com/excel-functions/regex-excel/)
    
*   [Excel Advanced Filter – A Complete Guide with Examples](https://trumpexcel.com/excel-advanced-filter/)
    
*   [How to Hide or Show Formula Bar in Excel?](https://trumpexcel.com/show-hide-formula-bar-excel/)
    
*   [Remove Characters From Left in Excel](https://trumpexcel.com/remove-characters-from-left-excel/)
    
*   [Formula vs Function in Excel – What’s the Difference?](https://trumpexcel.com/formula-vs-function-excel/)
    
*   [TAKE Function in Excel](https://trumpexcel.com/excel-functions/take-function/)
    
*   [Excel REDUCE Function](https://trumpexcel.com/excel-functions/reduce-function/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/advanced-excel-functions-formulas/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK