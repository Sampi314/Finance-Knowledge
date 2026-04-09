# XLOOKUP in Excel: How to Use It, and Whether Or Not It’s a Game-Changer (14:38)

**Source:** https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer

---

XLOOKUP in Excel: How to Use It, and Whether Or Not It’s a Game-Changer (14:38)
===============================================================================

In this tutorial, you’ll learn how to use the XLOOKUP function in Excel 365, how it improves upon VLOOKUP, HLOOKUP, and INDEX/MATCH, and whether or not XLOOKUP will start appearing in spreadsheets everywhere.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/#tab-signup)
    

XLOOKUP in Excel: How to Use It, and Whether Or Not It’s a Game-Changer

  
XLOOKUP is intended to be an improved version of functions like VLOOKUP, HLOOKUP, and even the INDEX/MATCH combination – so, how well does it serve that role?

The short version is that it’s a clear improvement over VLOOKUP and HLOOKUP, as it’s more powerful and easier to use than those.

It lets you specify a search value, a “lookup array,” and a “return array,” and search in any direction of a range of cells without having to give a row or column number.

It also lets you change the match type (exact vs. approximate vs. others), the search order, and the behavior if no value is found.

Nested XLOOKUP functions are a bit shorter and faster to write than the INDEX/MATCH/MATCH combination, but it’s not \*as big\* an improvement here.

The main problem is that XLOOKUP doesn’t work in older versions of Excel, and companies tend to upgrade VERY slowly.

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

How XLOOKUP Fixes and Improves VLOOKUP
--------------------------------------

Although the VLOOKUP function is very common in spreadsheets, it has a number of problems, which is why we almost always recommend INDEX/MATCH instead (and XLOOKUP is now even better):

First, VLOOKUP can only search from left to right in a table of data, and the item you’re looking up must be in the leftmost column of that table.

Second, you need to specify a column number for the results you want VLOOKUP to return. This may not seem like a big deal, but if the data range or setup ever changes, the function will not be valid anymore.

Third, VLOOKUP has no built-in support for errors such as the data not being found or for different “search modes” such as going from first-to-last or last-to-first.

Finally, VLOOKUP and HLOOKUP are both slow functions that are possibly “volatile,” meaning that small changes elsewhere on the spreadsheet could cause these functions to recalculate, even if the recalculation is not necessary.

If you compare equivalent VLOOKUP and XLOOKUP formulas for calculating the Discounted Price after a School or Organization receives a discount on a product purchase in this data, you can see the difference:

\=H3 \* (1 – VLOOKUP(E3, Schools!$C$3:$E$17, COLUMNS(Schools!$C$2:$E$17), FALSE))

\=H3 \* (1 – XLOOKUP(E3, Schools!$C$3:$C$17, Schools!$E$3:$E$17, 0, 0))

The XLOOKUP version is faster and easier to write, it handles the case where there’s no match by returning a “0,” and it doesn’t require a column number or the COLUMNS function. Instead, you directly enter the “answer” or “results” column.

XLOOKUP vs. INDEX/MATCH/MATCH
-----------------------------

The INDEX/MATCH/MATCH combo is most useful when you have to perform a 2-way lookup in a table by the row number and column number.

For example, in the “Schools” tab here, maybe we want to write a function that outputs \*any\* parameter for \*any\* School or Organization based on the Promo Code and the Parameter Name.

With error-checking included, the INDEX/MATCH/MATCH version looks like this:

\=IFERROR(INDEX($B$2:$E$17, MATCH(C20,$C$2:$C$17, 0), MATCH(B21,$B$2:$E$2, 0)), “N/A”)

The MATCH functions find the positions of the Parameter and the School/Organization, and then the INDEX function returns the value at the intersection of this row and column in the table.

The IFERROR around the entire formula makes it return “N/A” if the Promo Code or Parameter Name are not found.

The XLOOKUP version uses a nested XLOOKUP and is a bit shorter to write:

\=XLOOKUP(B21, $B$2:$E$2, XLOOKUP(C20,$C$2:$C$17, $B$2:$E$17, “N/A”))

First, it finds the position of the Parameter Name in the row at the top.

Then, the second XLOOKUP function finds the position of the Promo Code in the Promo Code column and returns the entire matching row.

Then, the first XLOOKUP combines the position of the Parameter Name with this single row result to return the parameter value, such as the commission rate or group discount rate for this specific School or Organization.

### Video Transcript

Hello, and welcome to another tutorial video. We’re going to be looking at the newly introduced XLOOKUP function in Excel in this lesson, see how to use it, determine when it’s useful, and not so useful, and then see whether or not it really is a game changer in Excel like some people claim. The first thing I have to point out here is that this function, XLOOKUP, was introduced in the 365 version of Excel. As I record this in 2020, it does not work in any other versions of Excel. It doesn’t work in Excel 2019, 2016, everything before that. Now, it may eventually be introduced and come to those standalone desktop versions, but as of right now, you need to be using the 365 version of Excel to access this new function. XLOOKUP is an improved version or replacement of functions like VLOOKUP and HLOOKUP as well as LOOKUP and even INDEX and MATCH.

We’re going to look at it here, go through a few examples, and then answer the question of whether or not it really improves upon these functions and by how much and whether you should start using it everywhere. The short answer on XLOOKUP is that it is a clear improvement over VLOOKUP in HLOOKUP. It is more powerful and easier to use than those functions. It lets you specify a LOOKUP array and a return array, and then whatever you’re searching for, and then it lets you search in any direction without having to specify a column number or a row number, and it lets you modify many options. Let’s go into Excel and see how this works. I have here a list of sales with first name, last name, promo code, order date, product name, and normal price. Then, we have a list of schools over here.

The idea is that we’re selling our products to these schools and then when students purchase an item from one of these schools, they enter a promo code. Then, they receive a discount based on that promo code, and we want to fill in the school or organization as well as the discounted price and the commissions owed based on the promo code that they’ve entered and the school they’re associated with. To fill in the school organization, I can type =XLOOKUP. LOOKUP value will just be the promo code right here. Then, XLOOKUP array, I’ll go over to schools right here and we will enter the promo code array. I’ll anchor this with F4, so it doesn’t shift around.

Then, the return array will just be the school organization column here. I’ll anchor this with F4. Then, I can also enter this option for what happens if this is not found. For example, I could type something like N/A here for not available or for now, I could just leave this blank just to show you how the basic function works. We have that. Let’s now copy this down to the bottom. Now, we have the school or organization name based on the promo code for each one of these individual sales. Now, if you compare XLOOKUP to the INDEX/MATCH/MATCH combination, it is a bit faster and shorter to write a nested XLOOKUP function, but it’s not quite as big of an improvement. You’ll see that when we get to the second main example here.

The biggest issue with XLOOKUP is that it doesn’t work in older versions of Excel. Companies tend to upgrade very slowly. Even now in 2020, you will still find people who are using versions of Excel from 10 or 15 years ago, or maybe even further back than that. To show how it improves on VLOOKUP, let’s look at a couple of the problems with VLOOKUP first. Now, the first major issue is that if you use a function like VLOOKUP, you can only move from left to right in a table of data. The item you’re looking up must be in the leftmost column.

If we look at this example for the school and organization names, we couldn’t even do it with VLOOKUP because the school organization name is to the left of the promo code. If I were to type something like =VLOOKUP here and then our promo code as the value, and then the table array, we can just enter the promo code and the commission rate and group discount rate here, you see the problem. This promo code needs to be in the left most column of this table array, but the school organization is what we actually want to find. That’s actually to the left of this entire table. We can’t really do this very easily with VLOOKUP, which is one of the major limitations. You can get around it by using INDEX and MATCH, but then you get into separate functions.

The second problem is that you need to specify the column number for the results that you want VLOOKUP to return. Now, this may not seem like a big deal. For example, maybe we just want to look up something like the discount or the commission rate for one of these schools. We go in and we enter our promo code. Then, for the table array, we go over here and select this whole area, anchor this with F4, and then we need to enter our column index number. We can enter two to get the commission rate, for example, or we can enter three to get the group discount rate. That may not seem like a big deal, but the problem is that what happens if we ever insert a new column right here? If that’s the case, then our formula here stops working, or at least it doesn’t work as we want it to, because now it’s referencing a different area with a different set of columns.

Now, there are some ways around this. For example, we could use the columns function in Excel to fix part of that, but it’s still somewhat awkward to have to enter these column or row numbers. There’s also no built-in support for errors or different search modes, such as searching from first to last or last to first. VLOOKUP and HLOOKUP are both slow functions that are possibly volatile, which means that if something ever changes in your spreadsheet, all these functions will recalculate and it will really slow down everything. These are some of the issues with VLOOKUP as well as HLOOKUP. HLOOKUP is just a bit different because it goes from top to bottom instead of left to right.

Let’s look at another example of VLOOKUP versus XLOOKUP for finding data. For this one, we want to look at the formula for finding the discounted price after the group discount, the school or organization receives. Let’s go over here and for the discounted price, it’ll be equal to the normal price. Then, we need to multiply it by one minus the discount the school receives. I’m going to say one minus, and then I’ll say VLOOKUP. We’ll enter the promo code right here. Then, for the table array, we’ll go over here and get this whole table, press F4 to ink everything. Then, for the column index number, we could just enter three here. I’ll enter false to get an exact match.

I forgot an extra parenthesis at the end, but Excel fix that by itself so we can have this. Then, we can just go down and enter this, alt ESF to paste formulas. We have our discounted prices for these tools and that’s how we do it with VLOOKUP. You can see it right there. Now, one slight improvement here is instead of typing three as I did, we could just use the columns function. Columns will get us the number of columns and arrange. I can just enter all these columns here, press F4 to anchor them and then close it out like that. This is a slightly better, slightly more flexible version because now if this area ever changes, we’ll still get to the correct column number. If, for example, we delete or insert columns somewhere in here as long as the basic area stays the same.

But then, if we try to write this function using XLOOKUP, take a look at how it works. Most of the first parts stays the same. We’re still going to be taking the normal price and multiplying by one minus the group discount, except now we can use XLOOKUP and we can type in the promo code. Then, for the LOOKUP array, it will just be the promo code column right here. Then, for the return array, it’ll just be the group discount column right here. If we do not find something, then I can type zero.

This makes sense because if the promo code doesn’t correspond to anything, then whoever entered this doesn’t get a discount. It’s just going to be one minus zero, which is just one, meaning no discount. Then, for the match mode, we have a couple different options, exact match, wild card match, exact or next smaller item, exact or next larger item. But for something simple like this, we’re just going to zero for exact match. Even if we didn’t enter that, XLOOKUP, by default assumes an exact match. We don’t even need to enter that last parameter. Let’s take this and copy this down, alt ESF, and so we have that.

Here’s our XLOOKUP version. It’s faster and easier to write. It handles the case where there is no match, whereas VLOOKUP simply doesn’t handle that and we’d get an error with this formula. Also, no column number is necessary, so we don’t need to bother with entering the column number manually or with this columns function right here. That’s how XLOOKUP improves upon VLOOKUP in this case. Let’s now go to XLOOKUP versus the INDEX/MATCH/MATCH combination. The INDEX/MATCH/MATCH combo is most useful when you have to perform a two-way LOOKUP by row number and column number.

An example is maybe you have to enter a formula to output any parameter for a school organization based on its promo code. Let’s go over to the school’s tab and see how this works. Down here, I have this area where there’s the promo code, and then there’s the school organization. I’ve used data validation, alt DL, and I’ve said it so that we have to select one of these parameters from the top of the table right here in source. Now, to write this with INDEX and MATCH, we can type index, and then we can index this whole area. I’ll just anchor this with F4, even though we don’t really have to here because this formula just stays in place.

For the row number, we will type a MATCH function. Then, we want to use this value, the promo code value right here. For the XLOOKUP array, we will enter the promo code column right here, including the top title. Then, for the MATCH type, we’ll say zero for exact match. Then, for the column number, we’ll enter another match function. For the LOOKUP value, we’ll link to our school/organization there, the text for it. For the LOOKUP array, we’ll just enter the row at the top, F4 to anchor that, and then zero for match. That’s our INDEX and MATCH function.

Of course, we could change this. We change it to something like COW for College of Winterhold. We could change the parameter we’re trying to find to commission rate, for example, or we could change it to group discount, or we could just change it to something else like Red Coast University right here and get different parameters like that. That is the INDEX and MATCH function. We’d say, “That’s fine.” If we want to improve it even more like I did here, we could write an if error around this. The advantage is that if we don’t actually get anything, so we can’t find a match for whatever we’re looking up, then we just get an N/A out of this function rather than getting an error message. We just get N/A text instead. If I enter something like SDF and a bunch of extra letters after that, we just get an N/A right there.

If we try to rewrite this with XLOOKUP, it is better, but arguably not dramatically better. I’ll just show you what it looks like right now. I will enter XLOOKUP and for the LOOKUP value, with this one, we’re going to start with the parameter on the left, the commission rate. Then, for the LOOKUP array, we will just go up to the top and enter that. Then, for the return array, I am going to write a nested XLOOKUP function here. I am going to type for the return array, another XLOOKUP function. We will go to promo code right here, and then we’ll go up. Then, for the LOOKUP array, we want this promo code column, the whole thing. Then, for the return array, I’m going to select this whole area, which is equivalent to the area that we are indexing with the INDEX/MATCH/MATCH version of this.

I will anchor that whole thing. If it’s not found, I’ll just say N/A, and then for the match mode, again, we want to do an exact match here, and then let’s close out all these parentheses. There, we can see what it looks like if we write this with a nested XLOOKUP function instead. One thing I would point out here is that although it is slightly shorter and faster to write, if we enter some type of nonsensical value like A, B, C, D, we do get a value error. The interesting part is even if we say N/A for not found and zero for exact match here, this error still stays in place because of the way we’ve written the function. I would argue this is actually a bit of a limitation or drawback that yes, XLOOKUP does have this mode for what to display if there’s an error or it’s not found, but it doesn’t always work perfectly.

Especially when you have a nested function like this, it may or may not work the way you want it to. This is why we think that although XLOOKUP is better than INDEX/MATCH/MATCH, in some ways, it’s not 100% improvement across all criteria. It’s less of a difference than replacing VLOOKUP and HLOOKUP with XLOOKUP instead. Now, a few other points before I wrap this up. There is an older function in Excel called just LOOKUP, which is similar, but it’s limited to an approximate match. That can be problematic if you are working with missing or unsorted data. We could just enter LOOKUP, and then the promo code, went through this for the LOOKUP vector. Then, for the result vector, we can enter the school organization name here, and so we get it like this,

This works pretty well for simple cases like this. But again, the problem is that it only works with approximate matches. Again, it doesn’t let you search in different directions. There’s nothing by default to show if it doesn’t find it in the data, so there are some issues with it. XLOOKUP can also do a lot more than what we showed you here. It can return entire ranges, use wild cards, search and reverse order depending on how your data is set up, so it does a whole lot more than the older HLOOKUP and VLOOKUP functions. The biggest downside is that it’s not backwards compatible and it’s not going to work in all these older versions of Excel, so we don’t think it’s going to suddenly replace these types of functions that you see all the time in spreadsheets, unless IT departments start suddenly upgrading everyone’s office installation very, very quickly.

We’re at the end, so let’s do a recap and summary. XLOOKUP is an improved version of the LOOKUP, HLOOKUP and VLOOKUP functions that is more powerful, faster and shorter to write. It also improves upon INDEX/MATCH/MATCH functions. We’d say there are some benefits, like the fact that you can specify the not found condition, but it’s not quite as big of a change as you might think. We don’t think it really adds as much over the INDEX/MATCH/MATCH combo as it does over the HLOOKUP and VLOOKUP functions. You can specify the not found condition with XLOOKUP, the match mode, the search mode, and you can also return entire ranges and operate on it.

If someone is not using a 365 version of Excel, they’re not going to be able to use this function at all, so don’t expect huge uptake right away. This is something that you’ll start to see appearing more and more often over, say the next five or even 10 years, but not something you’re going to see right away today or tomorrow or in the very near future. That’s about it. I hope you now know a bit more about this new function that Microsoft has introduced and how you can use it effectively in Excel.

[Premium Course Signup](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) XLOOKUP in Excel: How to Use It, and Whether Or Not It’s a Game-Changer - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-XLOOKUP-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Excel XLOOKUP Examples](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/Excel-XLOOKUP-Examples.xlsx)
    

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

[X](https://x.com/intent/tweet?text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&mini=true)
[Email](mailto:?subject=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[](https://www.linkedin.com/shareArticle?title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&mini=true)
[](mailto:?subject=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[](https://api.whatsapp.com/send?text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[Copy](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/#)
[Email](mailto:?subject=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&t=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/)
[Pinterest](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/#)
[Print](https://breakingintowallstreet.com/kb/excel/xlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[SMS](sms:?&body=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[X](https://x.com/intent/tweet?text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[WhatsApp](https://api.whatsapp.com/send?text=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fxlookup-in-excel-how-to-use-it-and-whether-or-not-its-a-game-changer%2F&title=XLOOKUP%20in%20Excel%3A%20How%20to%20Use%20It%2C%20and%20Whether%20Or%20Not%20It%E2%80%99s%20a%20Game-Changer%20%2814%3A38%29&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand