# XLOOKUP and XMATCH: Two New X-Men for Excel

**Source:** https://sumproduct.com/news/xlookup-and-xmatch-two-new-x-men-for-excel/

---

[Home](https://sumproduct.com/)

\> XLOOKUP and XMATCH: Two New X-Men for Excel

*   August 29, 2019

XLOOKUP and XMATCH: Two New X-Men for Excel
===========================================

The newly added functions in late August 2019.

XLOOKUP and XMATCH: Two New X-Men for Excel
===========================================

29 August 2019

Late August 2019 and Microsoft has added two new functions, **XLOOKUP** and **XMATCH**. For reasons that will become clear, here I will mainly consider the former function – because once you understand **XLOOKUP**, **XMATCH** becomes obvious (nothing personal, **XMATCH**).

Therefore, let’s take a look at the new addition to the **[LOOKUP](https://www.sumproduct.com/thought/looking-up-to-lookup)** family. I so wanted it to be called **FLOOKUP** but it was not to be…

Ask anyone and they will tell you two “truths”:

1.  They are a better than average driver and everyone else is an idiot on the roads
2.  They are a better than average Excel user because they know how to use **VLOOKUP**.

It’s well known I hate **[VLOOKUP](https://www.sumproduct.com/thought/lookout-for-vlookup-and-hlookup)** with a passion and if anything can come along and hurry its demise, well, I shall welcome it with open arms. Ladies and gentlemen, may I present the future of looking up for the masses – **XLOOKUP**. Hopefully, it will make an “ex” of **VLOOKUP**!

**Why I Loathe VLOOKUP**

Just as a recap, let me just summarise the resident incumbent:

**VLOOKUP(lookup\_value, table\_array, column\_index\_number, \[range\_lookup\])**

has the following syntax:

*   **lookup\_value:** what value do you want to look up?
*   **table\_array:** where is the lookup table?
*   **column\_index\_number:** which column has the value you want returned?
*   **\[range\_lookup\]:** do you want an exact or an approximate match? This is optional and to begin with, I am going to ignore this argument exists.

**HLOOKUP** is similar, but works on a row, rather than a column, basis.

To show my disdain, I am going to use **VLOOKUP** throughout to keep things simple. **VLOOKUP** always looks for the **lookup\_value** in the first column of a table (the **table\_array**) and then returns a corresponding value so many columns to the right, determined by the **column\_index\_number**.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-55.jpg)

In this above example, the formula in cell **G25** seeks the value 2 in the first column of the table **F13:M18** and returns the corresponding value from the eighth column of the table (returning 47).

Pretty easy to understand; so far so good. So what goes wrong? Well, what happens if you add or remove a column from the table range?

Adding (inserting) a column gives us the wrong value:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-47.jpg)

With a column inserted, the formula contain hard code (8) and therefore, the eighth column (**M**) is still referenced, giving rise to the wrong value. Deleting a column instead is even worse:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-38.jpg)

Now there are only seven columns so the formula returns _#REF!_ Oops.

It is possible to make the column index number dynamic using the **COLUMNS** function:

![](<Base64-Image-Removed>)

**COLUMNS(reference)** counts the number of columns in the **reference**. Using the range **F13:M13**, this formula will now keep track of how many columns there are between the lookup column (**F**) and the result column (**M**). This will prevent the problems illustrated above.

But there’s more issues. Consider duplicate values in the lookup column. With one duplicate, the following happens:

![](<Base64-Image-Removed>)

Here, the second value is returned, which might not be what is wanted. With two duplicates:

![](<Base64-Image-Removed>)

Ah, it looks like it might take the last occurrence. Testing this hypothesis with three duplicates:

![](<Base64-Image-Removed>)

Yes, there seems to be a pattern: **VLOOKUP** takes the last occurrence. Better make sure:

![](<Base64-Image-Removed>)

Rats. In this example, the value returned is the fourth of five. The problem is, there’s no consistent logic and the formula and its result cannot be relied upon. It gets worse if we exclude duplicates but mix up the lookup column a little:

![](<Base64-Image-Removed>)

In this instance, **VLOOKUP** cannot even find the value 2!

So what’s going on? The problem – and common modelling mistake – is that the fourth argument has been ignored:

**VLOOKUP(lookup\_value, table\_array, column\_index\_number, \[range\_lookup\])**

**\[range\_lookup\]** appears in square brackets, which means it is optional. It has two values:

*   **TRUE**: this is the _default_ setting if the argument is not specified. Here, **VLOOKUP** will seek an approximate match, looking for the largest value less than or equal to the value sought. There is a price to be paid though: the values in the first column (or row for **HLOOKUP**) must be in _strict ascending_ order – this means that each value must be larger than the value before, so no duplicates.
    
    This is useful when looking up postage rates for example where prices are given in categories of pounds and you have 2.7lb to post (say). It’s worth noting though that this isn’t the most common lookup when modelling.
    

*   **FALSE**: this has to be specified. In this case, data can be any which way – including duplicates – and the result will be based upon the _first_ occurrence of the value sought. If an exact match cannot be found, **VLOOKUP** will return the value _#N/A_.

And this is the problem highlighted by the above examples. The final argument was never specified so the lookup column data has to be in _strict_ ascending order – and this premiss was continually breached.

The robust formula needs both **COLUMNS** and a fourth argument of **FALSE** to work as expected:

![](<Base64-Image-Removed>)

This is a very common mistake in modelling. Using a fourth argument of **FALSE**, **VLOOKUP** will return the corresponding result for the first occurrence of the **lookup\_value**, regardless of number of duplicates, errors or series order. If an approximate match is required, the data must be in strict ascending order.

**VLOOKUP** (and consequently **[HLOOKUP](https://www.sumproduct.com/thought/lookout-for-vlookup-and-hlookup)
**) are not the simple, easy to use functions people think they are. In fact, they can never be used to return data for columns to the left (**VLOOKUP**) or rows above (**HLOOKUP**). So what should modellers use instead..?

**_Introducing XLOOKUP_**

There’s a new boss in town, but it’s only in selected towns presently. This function has been released in what Microsoft refers to as “Preview” mode, _i.e._ it’s not yet “Generally Available” but it is something you can try and hunt out. Presently, just like [dynamic arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
, you need to be part of what is called the “Office Insider” programme which is an Office 365 fast track. You can register in **File -> Account -> Office Insider** in Excel’s backstage area.

![](<Base64-Image-Removed>)

Even then, you’re not guaranteed a ticket to the ball as only some will receive the new function as Microsoft slowly roll out these features and functions. Please don’t let that put you off. This feature _will_ be with all Office 365 subscribers soon.

**XLOOKUP** has the following syntax:

**XLOOKUP(lookup\_value, lookup\_vector, results\_array, \[match\_mode\], \[search\_mode\])**

On first glance, it looks like it has too many arguments, but often you will only use the first three:

*   **lookup\_value:** this is required and defineswhat value you want to look up
*   **lookup\_vector:** this reference is required and is the row or column of data you are referencing to look up **lookup\_value**
*   **results\_array:** this is where the corresponding item is you wish to return and is also required (even if it is the same as **lookup\_vector**). This does _not_ have to be a vector (_i.e._ one row or one column of cells): it may be an array (with at least two rows and at least two columns of cells). The only stipulation is that the number of rows / columns must equal the number of rows / columns in the column / row vector – but more on that later
*   **match\_mode:** this argument is optional. There are four choices:
    
    *   **0:** exact match (default)
    *   **\-1:** exact match or else the largest value less than or equal to **lookup\_value**
    *   **1:** exact match or else smallest value greater than or equal to **lookup\_value**
    *   **2:** wildcard match. You should use the special character **?** to match any character and **\*** to match any run of characters.
    
    What’s impressive, though, is that for certain selections of the final argument (**search\_mode**), you _don’t_ need to put your data in alphanumerical order! As far as I am aware, this is a first for Excel
    
*   **search\_mode:** this argument is also optional. There are again four choices:
    *   **1:** search first to last (default)
    *   **\-1:** search last to first
    *   **2:** what is known as a binary search, first to last (requires **lookup\_vector** to be sorted). Just so you know, a binary search is a search algorithm that finds the position of a target value within a sorted array. A binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found
    *   **\-2:** another binary search, this time last to first (and again, this requires **lookup\_vector** to be sorted).

**_XLOOKUP compares favourably with VLOOKUP_**

While **VLOOKUP** is the third most used function in Excel (behind **SUM** and **AVERAGE**), it has several well-known limitations which **XLOOKUP** overcomes:

*   **it defaults to an “approximate” match:** most often, users want an exact match, but this is not **VLOOKUP**’s default behaviour. To perform an exact match, you need to set the final argument to FALSE (as explained earlier). If you forget (which is easy to do), you’ll probably get the wrong answer
*   **it does not support column insertions / deletions:** **VLOOKUP**’s third argument is the column number you’d like returned. Since this is a hard-coded number, if you insert or delete a column you need to increment or decrement the column number inside the **VLOOKUP** – hence the need for the **COLUMNS** function (and the corresponding **ROWS** function for **HLOOKUP**)
*   **it cannot look to the left:** **VLOOKUP** always searches the first column, then returns a column to the right. There is no way to return values from a column to the left, forcing users to rearrange their data
*   **it cannot search from the bottom:** If you want to find the last occurrence, you need to reverse the order of your data
*   **it cannot search for next larger item:** when performing an “approximate” match, only the item less than or equal to the searched item can be returned and only if correctly sorted
*   **references more cells than necessary: VLOOKUP**’s second argument, **table\_array**, needs to stretch from the lookup column to the results column. As a result, it typically references more cells than it truly depends on. This could result in unnecessary calculations, reducing the performance of your spreadsheets.

Let’s have a look at **XLOOKUP** versus **VLOOKUP**:

![](<Base64-Image-Removed>)

You can clearly see the **XLOOKUP** function is shorter:

**\=XLOOKUP(H52,F41:F47,G41:G47)**

Only the first three arguments are needed, whereas **VLOOKUP** requires both a fourth argument, and, for full flexibility, the **COLUMNS** function as well. **XLOOKUP** will automatically update if rows / columns are inserted or deleted. It’s just _simpler_.

**HLOOKUP** has similar issues:

![](<Base64-Image-Removed>)

Here, this highlights what happens if I try to deduce the student name from the Student ID. **HLOOKUP** cannot refer to earlier rows, just as **VLOOKUP** cannot consider columns to the left. Given any unused elements of the table are ignored also, it’s just good news all round. Goodbye limitations, hello **XLOOKUP**.

Indeed, things get even more interesting when you start considering **XLOOKUP**’s final two arguments, namely **match\_mode** and **search\_mode**, _viz_.

![](<Base64-Image-Removed>)

Notice that I am searching the ‘Value’ column, which is neither sorted nor contains unique items. However, I can look for approximate matches – impossible with **VLOOKUP** and / or **HLOOKUP**.

Do you see how the results vary depending upon **match\_mode** and **search\_mode**?

![](<Base64-Image-Removed>)

The **match\_mode** zero (0) returns _#N/A_because there is no exact match.

When **match\_mode** is -1, **XLOOKUP** seeks an exact match or else the largest value less than or equal to **lookup\_value** (6.5). That would be 4 – but this occurs more than once (B and D both have a value of 4). **XLOOKUP** chooses depending upon whether it is searching top down (**search\_mode** 1, where B will be identified first) or bottom up (**search\_mode** \-1, where D will be identified first). Note that with binary searches (with a **search\_mode** of 2 or -2), the data needs to be sorted. It isn’t – hence we have garbage answers that cannot be relied upon.

With **match\_mode** 1, the result is clearer cut. Only one value is the smallest value greater than or equal to 6.5. That is 7, and is related to A. Again, binary search results should be ignored.

The **match\_mode** 2 results are spurious. This is seeking wildcard matches, but there are no matches, hence _N/A_ for the only **search\_modes** that may be seen as creditable (1 and -1).

Clearly binary searches are higher maintenance. In the past, it was worth investing in them as they did return results more quickly. However, according to Microsoft, this is no longer the case: apparently, there is “…no significant benefit to using _(sic)_ the binary search options…”. If this is indeed the case, then I would strongly recommend not using them going forward with **XLOOKUP**.

To show how simple it now is to search from the end, consider the following:

![](<Base64-Image-Removed>)

This used to be an awkward calculation – but not anymore! The formula is easy:

**\=XLOOKUP($G$130,$G$113:$G$125,H$113:H$125,,-1)**

It’s a “standard” **XLOOKUP** formula, with a “bottom up” search coerced by using the final value of -1 (forcing the **search\_mode** to go into “reverse”).

**_Comparisons with LOOKUP_**

Whilst **XLOOKUP** wins hands down against **HLOOKUP** and **VLOOKUP**, the same cannot necessarily be said for **LOOKUP**. You may recall **[LOOKUP](https://www.sumproduct.com/thought/looking-up-to-lookup)
** has two forms: an array form and a vector form. As a reminder:

*   an **array** is a collection of cells consisting of at least two rows and at least two columns
*   a **vector** is a collection of cells across just one row (row vector) or down just one column (column vector).

The diagram should be self-explanatory:

![](<Base64-Image-Removed>)

The array form of **LOOKUP** looks in the first row or column of an array for the specified value and returns a value from the same position in the last row or column of the same array:

**LOOKUP(lookup\_value, array)**

where:

*   **lookup\_value** is the value that **LOOKUP** searches for in an array. The **lookup\_value** argument can be a number, text, a logical value, or a name or reference that refers to a value
*   **array** is the range of cells that contains text, numbers, or logical values that you want to compare with **lookup\_value**.

The array form of **LOOKUP** is very similar to the **HLOOKUP** and **VLOOKUP** functions. The difference is that **HLOOKUP** searches for the value of **lookup\_value** in the first row, **VLOOKUP** searches in the first column, and **LOOKUP** searches according to the dimensions of array.

If **array** covers an area that is wider than it is tall (_i.e._ it has more columns than rows), **LOOKUP** searches for the value of **lookup\_value** in the first row and returns the result from the last row. Otherwise, **LOOKUP** searches for the value of **lookup\_value** in the first column and returns the result from the last column instead.

The alternative form is the vector form:

**LOOKUP(lookup\_value, lookup\_vector, \[result\_vector\])**

The **LOOKUP** function vector form syntax has the following arguments:

*   **lookup\_value** is the value that **LOOKUP** searches for in the first vector
*   **lookup\_vector** is the range that contains only one row or one column
*   **\[result\_vector\]** is optional – if ignored, **lookup\_vector** is used – this is the where the result will come from and must contain the same number of cells as the **lookup\_vector**.

Like the default versions of **HLOOKUP** and **VLOOKUP**, **lookup\_value** must be located in a range of ascending values.

Let me demonstrate with an example:

![](<Base64-Image-Removed>)

**LOOKUP** is a great function to use with time series analysis / forecasting. Dates are in ascending order and the **LOOKUP** syntax is remarkably simple. As a modeller, I use it regularly when I am modelling many more forecast periods than I want assumption periods.

Here, you can see I carry assumptions only for 2020 until 2024 (the final value is 2024, just with a “+” in number formatting). The formula

**\=LOOKUP(G$74,$G$67:$K$68)**

returns the corresponding value for the period that is either an exact match or else the largest value less than or equal to the **lookup\_value**. **LOOKUP** uses the top row of the table for looking up its data and the final row for returning the corresponding value. Simple. As for **XLOOKUP**:

**\=XLOOKUP(G$82,$G$67:$K$67,$G$68:$K$68,-1)**

This formula is longer and requires two additional arguments (**match\_mode** \-1 is required to mirror the behaviour of **LOOKUP**). Indeed, given that an **IF** statement is required to ensure no errors for earlier periods, _e.g._

**\=IF(G$90<$G$67,$G$68,LOOKUP(G$90,$G$67:$K$68))**

it may be argued that **LOOKUP** is a simpler function to use here than its counterpart.

This isn’t the only time **LOOKUP** outperforms **XLOOKUP**:

![](<Base64-Image-Removed>)

Here, we do see a limitation of **XLOOKUP**. Whilst the third argument of **XLOOKUP**, **results\_array**, does not need to be a vector, it cannot be the transposition of the **lookup\_vector**. You would have to transpose it using the **[TRANSPOSE](https://www.sumproduct.com/thought/transpose-i-suppose)** function, for example. This makes **LOOKUP** much easier to use – compare:

**\=LOOKUP(H112,F105:F109,G102:K102)**

with

**\=XLOOKUP(H112,F105:F109,TRANSPOSE(G102:K102))**

In this instance, **LOOKUP** wins.

**_Useful Features of XLOOKUP_**

**XLOOKUP** can be used to perform a two-way match, similar to **[INDEX MATCH MATCH](https://www.sumproduct.com/thought/index-match)
**:

![](<Base64-Image-Removed>)

Many advanced users might use the formula

**\=INDEX(H40:N46,MATCH(G53,G40:G46,0),MATCH(G51,H39:N39,0))**

where:

*   **INDEX(array, row\_number, \[column\_number\])** returns a value or the reference to a value from within a table or range (list) citing the row\_number and the column\_number
*   **MATCH(lookup\_value, lookup\_vector, \[match\_type\])** returns the relative position of an item in an array that (approximately) matches a specified value. It’s most commonly used with match\_type zero (0), which requires an exact match.

Therefore, this formula finds the position in the row for the student and the position in the column of the subject. The intersection of these two provides the required result.

**XLOOKUP** does it differently:

**\=XLOOKUP(G53,G40:G46,XLOOKUP(G51,H39:N39,H40:N46))**

Welcome to the wonderful world of the _nested_ **XLOOKUP** function! Here, the internal formula

**\=XLOOKUP(G51,H39:N39,H40:N46)**

demonstrates a key difference between this and your typical lookup function – the first argument is a cell, the second argument is a column vector and the third is an array – with, most importantly, the same number of rows as the **lookup\_vector**. This means it returns a column vector of data, not a single value. This is great news in the brave new world of dynamic arrays.

In essence, this means the formula resolves to

**\=XLOOKUP(G53,G40:G46,J40:J46)**

as **J40:J46** is the resultant vector of **\=XLOOKUP(G51,H39:N39,H40:N46)**. This is a really powerful – and virtually new – concept to get your head around, that admittedly **[SUMPRODUCT](https://www.sumproduct.com/thought/sumproduct-squared)
** exploits too. Once you understand this, it’s clear how this formula works and opens your eyes to the power of nested **XLOOKUP** functions.

I can’t believe I am talking about the virtues of nested functions here! Let me change the subject quickly…

To show you how dynamic arrays can make the most of being able to create resultant vectors, consider the following example:

![](<Base64-Image-Removed>)

The formula

**\=XLOOKUP(G77,I65:L65,I66:L72)**

again resolves to a vector – but this time is allowed to spill as a dynamic array. Obviously, this will only work in Office 365, but it’s a very useful tool that might just make you think it’s time to drop that perpetual licence.

Once you start playing with the dynamic range side, you can start to get imaginative. For example:

![](<Base64-Image-Removed>)

In this illustration, I want to calculate the sales between two periods:

![](<Base64-Image-Removed>)

This might seem like a simple drop-down list using data validation (**ALT + D + L**), but **XLOOKUP** has been used in determining the list to be used for the end months.

Let me explain. I have hidden the range of relevant dates in cell H101 spilled across

![](<Base64-Image-Removed>)

**XLOOKUP** can return a reference, so the formula

**\=XLOOKUP(G100,H94:S94,H94:s94):S94**

evaluates to the row vector **N94:S94** (since the start month is July). This spilled dynamic array formula is then referenced in the data validation:

![](<Base64-Image-Removed>)

(You may recall **$H$101#** means the spilled range starting in cell **H101**.) It should be noted that the formula **\=XLOOKUP(G100,H94:S94,H94:s94):S94** may not be used directly in the ‘Data Validation’ dialog, but this is a neat trick to ensure you cannot select an end month before the start month (assuming you are a rational human being that selects the start before the end!).

The formula to sum the sales then is

**\=SUM(XLOOKUP(G100,H94:S94,H95:S95):XLOOKUP(G101,H94:S94,H95:S95))**

Again, this uses the fact **XLOOKUP** can return a reference, so this formula equates to

**\=SUM(N95:Q95)**

Easy! Now I am combining two **XLOOKUP** formulae with a colon (:) to form a range. This joins other illustrious functions used this way such as **[CHOOSE](https://www.sumproduct.com/thought/do-you-choose-to-use-choose)**, **[IF](https://www.sumproduct.com/thought/spreadsheet-skills-flagging-if)
**, **[IFS](https://www.sumproduct.com/thought/excel-2016-functions-and-features)**, **[INDEX](https://www.sumproduct.com/thought/index-match)**, **[INDIRECT](https://www.sumproduct.com/thought/being-direct-about-indirect)
**, **[OFFSET](https://www.sumproduct.com/thought/onset-of-offset)
, [SINGLE (@)](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
**, **[SWITCH](https://www.sumproduct.com/thought/excel-2016-functions-and-features)** and **[TEXT](https://www.sumproduct.com/thought/concatenation)
**. First nesting, now joining – what’s next?

**_Partial and Exact Matching_**

Seeking partial matches (sounds like an unfussy dating agency!) suddenly became a lot easier too. You can use wildcards if you want to – just set the **match\_mode** to 2:

![](<Base64-Image-Removed>)

Here, I am searching for **J?n\*n\*** – which is fine as long as you know what the wildcard characters mean:

*   **?** means “any character”, but just one character.  If you wanted to make space for two and only two characters you would use **??**
*   **\*** means “any number of characters’ – including zero.

For example, **M?n\*m\*** would identify “Manmade”, “minimum” and “Manikum” but would not accept “millennium”.  Here, our formulae

**\=XLOOKUP(G184,H174:H179,I174:I179,2)**

**\=XLOOKUP(G184,H174:H179,I174:I179,2,-1)**

would locate the first and last items that satisfied the condition **J?n\*n\*** (_i.e._ “Jonathan” and “Jonny” respectively).

But what if you wanted an exact match with case sensitivity?  You just have to think a little but outside of the proverbial box:

![](<Base64-Image-Removed>)

Here, we use another feature of **XLOOKUP** – its ability to search a virtual vector, _i.e._ one that has been constructed in memory, rather than physically within the spreadsheet cells.  Consider the formula

**\=XLOOKUP(TRUE,EXACT(H145:H154,G159),I145:I154)**

Here, the interim calculation **\=EXACT(H145:H154,G159)**, looks at the range **H145:H154** and deduces whether the cells are an exact match for the selection ‘Sum Product’ in cell **G159**.  The **[EXACT](https://old.sumproduct.com/thought/finding-an-exact-match)
** function would evaluate as

**{FALSE; TRUE; FALSE; FALSE; FALSE; FALSE; FALSE; FALSE; TRUE; FALSE}**

Therefore, the formula coerces to

**\=XLOOKUP(TRUE,{FALSE; TRUE; FALSE; FALSE; FALSE; FALSE; FALSE; FALSE; TRUE; FALSE},I145:I154)**

and then the formula becomes simple to understand.

No doubt there are many more great things you can do with **XLOOKUP**, but hey, it’s just arrived and we are only getting started!

**_XMATCH_**

As I said at the beginning, **XLOOKUP** did not land in isolation.  In addition to **XLOOKUP**, **XMATCH** has arrived with a similar signature to **XLOOKUP**, but instead it returns the index (position) of the matching item.  **XMATCH** is both easier to use and more capable than its predecessor **MATCH**.

![](<Base64-Image-Removed>)

**XMATCH** has the following syntax:

**XMATCH(lookup\_value, lookup\_vector, \[match\_mode\], \[search\_mode\])**

where:

*   **lookup\_value:** this is required and defines what value you want to look up
*   **lookup\_vector:** this reference is required and is the row or column of data you are referencing to look up **lookup\_value**
*   **match\_mode:** this argument is optional.  There are four choices:
    
    *   **0:** exact match (default)
    *   **\-1:** exact match or else the largest value less than or equal to **lookup\_value**
    *   **1:** exact match or else smallest value greater than or equal to **lookup\_value**
    *   **2:** wildcard match.  You should use the special character **?** to match any character and **\*** to match any run of characters.
    
    Again, for certain selections of the final argument (**search\_mode**), you don’t need to put your data in alphanumerical order
*   **search\_mode:** this argument is also optional.  There are again four choices:
    *   **1:** search first to last (default)
    *   **\-1:** search last to first
    *   **2:** this is a binary search, first to last (requires **lookup\_vector** to be sorted)
    *   **\-2:** another binary search, this time last to first (and again, this requires **lookup\_vector** to be sorted).

As you can see, it’s a fairly straightforward addition to the **MATCH** family.  It acts similarly to **MATCH** – just with heaps more functionality.

**_Word to the Wise_**

**XLOOKUP** and **XMATCH** open up new avenues for Excel to explore, but it must be remembered they are still in Preview and may only be accessed by a lucky few on the Insider track.  Feel free to download and play with the [attached Excel file](https://sumproduct.com/assets/news-graphics/xlookup-and-xmatch/sp-xlookup-and-xmatch-functions.xlsx)
, but don’t be too perturbed if your version of Excel does not recognise these functions yet.

*   [Log in](https://sumproduct.com/news/xlookup-and-xmatch-two-new-x-men-for-excel/#0)
    
*   [Register](https://sumproduct.com/news/xlookup-and-xmatch-two-new-x-men-for-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/xlookup-and-xmatch-two-new-x-men-for-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/xlookup-and-xmatch-two-new-x-men-for-excel/#0)

[](https://sumproduct.com/news/xlookup-and-xmatch-two-new-x-men-for-excel/#0 "close")

top