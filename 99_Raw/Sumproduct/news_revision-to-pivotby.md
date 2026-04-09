# Revision to PIVOTBY

**Source:** https://sumproduct.com/news/revision-to-pivotby/

---

[Home](https://sumproduct.com/)

\> Revision to PIVOTBY

*   May 16, 2024

Revision to PIVOTBY
===================

Revision to PIVOTBY
===================

16 May 2024

Back in November last year, Microsoft announced several new functions, including **PIVOTBY**, andeta lambdas such as **PERCENTOF**. On the quiet, they have added a new argument which makes **PIVOTBY** just that little bit more powerful.

At the time of writing, they are rolling out to users enrolled in the beta channel for Windows Excel and Mac Excel. Don’t be upset if you don’t get this new update straight away. But first, let’s have a little refresher…

**_eta Lambdas_**

These “eta reduced lambda” functions may sound scary, but they make the world of dynamic arrays more accessible to the inexperienced. They help make the other three functions simpler to use. Dynamic array calculations using basic aggregation functions often require syntax such as

**LAMBDA(x, SUM(x))**

**LAMBDA(y, AVERAGE(y))**

_etc._

However, given **x** and **y** _(above)_ are merely dummy variables, an “eta lambda” function simply replaces the need for this structure with the so-easy-anyone-can-understand-it syntax of

**SUM**

**AVERAGE**

_etc._

Even I can do it. For example, consider the following formula in cell **G17** below:

![](<Base64-Image-Removed>)

**\=BYCOL(G13:J16,LAMBDA(x,SUM(x)))**

This sums the range **G13:J16** by column using that **LAMBDA(x, SUM(x))** trick. But there is no need for this anymore, _viz._

![](<Base64-Image-Removed>)

**\=BYCOL(G21:J24,SUM)**

That’s much simpler and many one argument functions may now be turned into eta lambdas (and one or two other functions too).

**_PERCENTOF_**

This function can be used in conjunction with **PIVOTBY**_(below)_ or on its own. This is used to return the percentage that a subset makes up of a given dataset. It is logically equivalent to

**SUM(subset) /  
SUM(everything)**

It sums the values in the subset of the dataset and divides it by the sum of all the values. It has the following syntax:

**\=PERCENTOF(data\_subset,  
data\_all)**

The arguments are as follows;

*   **data\_subset:** this is required, and represents the values that are in the data subset
*   **data\_all:** this too is required and denotes the values that make up the entire set.

You can use it, for example, with **GROUPBY**:

**\=GROUPBY(tbl\[Category\],tbl\[Sales\],PERCENTOF)**

![](<Base64-Image-Removed>)

Alternatively, it may be used on its own:

![](<Base64-Image-Removed>)

**_PIVOTBY_**

The reason for this article is that **PIVOTBY** has changed. It has added a new, final argument: **relative\_to** – but let’s back up first.

The **PIVOTBY** function allows you to create a summary of your data via a formula too, akin to a formulaic PivotTable. It supports grouping along two axes and aggregating the associated values. For instance, if you had a table of sales data, you might generate a summary of sales by state and year.

It should be noted that **PIVOTBY** is a function that returns an array of values that can spill to the grid. Furthermore, at this stage, not all features of a PivotTable appear to be replicable by this function.

The syntax of the **PIVOTBY** function is:

**PIVOTBY(row\_fields,  
col\_fields, values, function, \[field\_headers\], \[row\_total\_depth\], \[row\_sort\_order\],  
\[col\_total\_depth\], \[col\_sort\_order\], \[filter\_array****\], \[relative\_to\])**

It has the following arguments:

*   **row\_fields:** this is required, and represents a column-oriented array or range that contains the values which are used to group rows and generate row headers. The array or range may contain multiple columns. If so, the output will have multiple row group levels
*   **col\_fields:** also required, and represents a column-oriented array or range that contains the values which are used to group columns and generate column headers. The array or range may contain multiple columns. If so, the output will have multiple column group levels

*   **values:** this is also required, and denotes a column-oriented array or range of the data to aggregate. The array or range may contain multiple columns. If so, the output will have multiple aggregations

*   **function:** also required, this is an explicit or eta reduced lambda (_e.g._ **SUM**, **PERCENTOF**, **AVERAGE**,**COUNT**) that is used to aggregate **values**. A vector of lambdas may be provided. If so, the output will have multiple aggregations. The orientation of the vector will determine whether they are laid out row- or column-wise
*   **field\_headers:** this and the remaining arguments are all optional. This represents a number that specifies whether the **row\_fields**, **col\_fields** and **values** have headers and whether field headers should be returned in the results. The possible values are:

*   **Missing:** Automatic
*   **0:** No
*   **1:** Yes and don’t show
*   **2:** No but generate
*   **3:** Yes and show

It should be noted that “Automatic” assumes the data contains headers based upon the **values** argument. If the first value is text and the second value is a number, then the data is assumed to have headers. Fields headers are shown if there are multiple row or column group levels

*   **row\_total\_depth:** this optional argument determines whether the row headers should contain totals. The possible values are:

*   **Missing**: Automatic, with grand totals and, where possible, subtotals
*   **0:** No Totals
*   **1:** Grand Totals
*   **2:** Grand and Subtotals
*   **\-1:** Grand Totals at Top
*   **\-2:** Grand and Subtotals at Top

It should be noted that for subtotals, **row\_fields** must have at least two \[2\] columns. Numbers greater than two \[2\] are supported provided **row\_field** has sufficient columns

*   **row\_sort\_order:** again optional, this argument denotes a number indicating how rows should be sorted. Numbers correspond with the columns in **row\_fields** followed by the columns in **values**. If the number is negative, the rows are sorted in descending / reverse order. A vector of numbers may be provided when sorting based upon only **row\_fields  
    **

*   **col\_total\_depth:** this optional argument determines whether the column headers should contain totals. The possible values are:

*   **Missing**: Automatic, with grand totals and, where possible, subtotals
*   **0:** No Totals
*   **1:** Grand Totals
*   **2:** Grand and Subtotals
*   **\-1:** Grand Totals at Top
*   **\-2:** Grand and Subtotals at Top

It should be noted that for subtotals, **col\_fields** must have at least two \[2\] columns. Numbers greater than two \[2\] are supported provided **col\_field** has sufficient columns

*   **col\_sort\_order:** again optional, this argument denotes a number indicating how they should be sorted. Numbers correspond with the columns in **col\_fields** followed by the columns in **values**. If the number is negative, these are sorted in descending / reverse order. A vector of numbers may be provided when sorting based upon only **col\_fields  
    **

*   **filter\_array:** this is now the penultimate optional argument, it represents a column-oriented one-dimensional array of Boolean values \[1, 0\] that indicate whether the corresponding row of data should be considered. It should be noted that the length of the array must match the length of **row\_fields** and **col\_fields**

*   **relative\_to:** this new, final argument allows you to summarise functions relative to row and column totals or the grand total. Five alternatives are possible:
    *   **0:** Column Totals (default) _(Screentip: Calculation performed relative to all values in column)_
    *   **1:** Row Totals _(Calculation performed relative to all values in row)_
    *   **2:** Grand Total _(Calculation performed relative to all values)_
    *   **3:** Parent Column Total _(Calculation performed relative to all values in column parent)_
    *   **4:** Parent Row Total _(Calculation performed relative to all values in row parent)_.

Let’s look at **PIVOTBY** using **PERCENTOF**, highlighting this new **relative\_to** final argument. You can follow along with the [attached Excel file](https://www.sumproduct.com/assets/news_graphics/revision-to-pivotby/sp-pivotby-new-argument.xlsx)
.

Consider the following Table (**CTRL + T**) called **Data**_(truncated)_:

![](<Base64-Image-Removed>)

Here, we have two parent / child relationships:

*   **Year** and **Quarter**
*   **Category** and **Item**.

From our previous article on **[PIVOTBY](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-pivotby-function)
**, we can create a formulaic alternative to a PivotTable (with crafty formatting) using the following formula:

**\=PIVOTBY(Data\[\[Category\]:\[Item\]\],Data\[\[Year\]:\[Quarter\]\],Data\[Sales\],PERCENTOF)**

![](<Base64-Image-Removed>)

Note that each column of sales is represented as a percentage of that column (including the Total column). Whilst it was a great start, Microsoft received feedback that end users wanted to see percentages summarised in alternative ways – and that is what has been addressed here.

This newly introduced final argument, **relative\_to**, behaves the same in scenario **0**: Column Totals. This is the default view:

**\=PIVOTBY(Data\[\[Category\]:\[Item\]\],Data\[\[Year\]:\[Quarter\]\],Data\[Sales\],PERCENTOF,,,,,,,0)**

![](<Base64-Image-Removed>)

It is clear to see this is identical to the first output. But let’s see what happens when we start playing with the final argument. Let’s change this value to **1:** Row Totals.

**\=PIVOTBY(Data\[\[Category\]:\[Item\]\],Data\[\[Year\]:\[Quarter\]\],Data\[Sales\],PERCENTOF,,,,,,,1)**

Now, each row of sales is represented as a percentage of that row (including the Total row), _viz._

![](<Base64-Image-Removed>)

If you wish, you can show the sales as a percentage of the Grand Total, using **2:** Grand Total:

**\=PIVOTBY(Data\[\[Category\]:\[Item\]\],Data\[\[Year\]:\[Quarter\]\],Data\[Sales\],PERCENTOF,,,,,,,2)**

![](<Base64-Image-Removed>)

There are still two further scenarios – and this is why our example contained two parent / child relationships. The first is **3:** Parent Column Total:

**\=PIVOTBY(Data\[\[Category\]:\[Item\]\],Data\[\[Year\]:\[Quarter\]\],Data\[Sales\],PERCENTOF,,,,,,,3)**

![](<Base64-Image-Removed>)

Here, the Total column is 100% throughout. It is a little confusing as, if anything, it looks a little like Scenario **1:** Row Totals. This is because the column here refers to the headings in each column, _i.e._ **Year** and **Quarter**. You can see that for any row the sum of the four quarters for any given year totals 100% (including the Total row).

Finally, Scenario **4:** Parent Row Total considers the other parent / child relationship:

**\=PIVOTBY(Data\[\[Category\]:\[Item\]\],Data\[\[Year\]:\[Quarter\]\],Data\[Sales\],PERCENTOF,,,,,,,4)**

![](<Base64-Image-Removed>)

In this final illustration, the Total row is 100% throughout. This looks similar to the default Scenario **0:** Column Totals. This is because the row here refers to the headings in each row, _i.e._ **Category** and **Item**. You can see that for any row the sum of any category for any given **Quarter** and **Year** totals 100% (including the Total column).

**_Word to the Wise_**

Starting with **RANDARRAY**, Microsoft continues to venture into new territory by tinkering with new functions and features whilst they remain in beta. Previously, revising a function’s signature / syntax was unheard of. Here at SumProduct, we’re not complaining. The software giant has been collating formula usage and explicit feedback to determine what is missing / needs revising – and then done something about it.

If only they had done that with **MATCH** many years ago!!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/revision-to-pivotby/#0)
    
*   [Register](https://sumproduct.com/news/revision-to-pivotby/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/revision-to-pivotby/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/revision-to-pivotby/#0)

[](https://sumproduct.com/news/revision-to-pivotby/#0 "close")

top