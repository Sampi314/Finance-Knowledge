# Dynamic Range Names

**Source:** https://sumproduct.com/thought/dynamic-range-names/

---

[Home](https://sumproduct.com/)

\> Dynamic Range Names

*   May 14, 2025

Dynamic Range Names
===================

How to create dynamic range names.

Dynamic Range Names
===================

_Liam Bastick_ _highlights some of the common issues and scenarios in financial modelling / Excel spreadsheeting. This time we look at what are known in the trade as dynamic range names._

**_Dynamic Range Names_**

Just to warn you, I’ve written a novel this time out and there’s lots of past referencing for this article! But it’s worth it for an important modelling topic: dynamic range names, _i.e._ creating a selection that _varies_ depending upon criteria specified or certain circumstances arising.

Before I start though, allow me to perform a brief recap on how range names are created…

### Recap: Creating Range Names

Range names are created using the ‘Name Manager’ in Excel 2007 and later. The Name Box (circled, below),

![](<Base64-Image-Removed>)

drop down menus and / or Ribbon may be used, or keyboard shortcuts such as **ALT + I + N + D + N** or **ALT + M + N**. I would suggest using none of these methods. Simply use the keyboard shortcut **CTRL + F3** in all versions of Excel, and then click on the ‘New’ button in the ‘Name Manager’ dialog box), _viz._

![](<Base64-Image-Removed>)

After clicking on ‘New’ (above), the following dialog box appears:

![](<Base64-Image-Removed>)

### Methods of Creating Dynamic Range Names

There are several ways to create a range name that will vary based on conditions cited or other circumstances. Here, I am going to look at the following approaches:

*   Using structured references (Excel Tables)
*   **OFFSET** method
*   **INDIRECT** method
*   **IF** method
*   **CHOOSE** method
*   Relative referencing.

This isn’t intended to be an exhaustive list, but it’s a good start! Let me go through each one in turn – and as always there’s an attached [Excel file](https://sumproduct.com/assets/thought-files/dynamic-range-names/sp-dynamic-range-names.xlsx)
 to play with too.

**_Using Structured References (Excel Tables)_**

Consider you had some financial data similar to the following:

![](<Base64-Image-Removed>)

Highlighting the data (here, cells **B2:C9**) and using the keyboard shortcut **ALT + F1** produces a quick and dirty chart, _viz._

![](<Base64-Image-Removed>)

The problem is, when you add the next period’s data _nothing_ happens:

![](<Base64-Image-Removed>)

Most of us have been there and bought that t-shirt. Therefore, with a heavy heart, you right-click on the chart and choose ‘Select data…’

![](<Base64-Image-Removed>)

and from the resulting dialog box you update the date and sales references:

![](<Base64-Image-Removed>)

Surely there is a better way? Oh yes – it’s dynamic range name time with a _Table_.

Let’s start again. After entering the data and before creating the chart, convert the data range to a Table (**CTRL + T**, or from the ‘Insert’ tab on the Ribbon, choose ‘Table’ from the ‘Tables’ section):

![](<Base64-Image-Removed>)

Ensure the ‘My table has headers’ check box is ticked in the ensuing dialog box:

![](<Base64-Image-Removed>)

Now add a chart as before, but this time, when additional data is added the chart automatically updates:

![](<Base64-Image-Removed>)

How good a trick is that? Therefore, I have a rule with chart data: **always put it in a Table before creating the chart**. It just makes life easier.

Tables can be used to make lists of variable length too. Consider creating the following Table:

![](<Base64-Image-Removed>)

In this example, I will call this Table **Table\_List** (I am nothing if not imaginative). Selecting the range excluding the heading (‘Data’) is denoted **Table\_List\[Data\]**. If I add further entries (_e.g._ “Devon” and “Hate” anyone?), the range **Table\_List\[Data\]** will expand accordingly _automatically_.

I can create an in-cell list using _data validation_. To do this, I go to the Ribbon and select ‘Data Validation’ from the ‘Data Tools’ group in the ‘Data’ tab of the Ribbon (keyboard shortcuts, either **ALT + A + V + V** or **ALT + D + L**):

![](<Base64-Image-Removed>)

The problem is if you make this the source of the data validated list,

![](<Base64-Image-Removed>)

Excel doesn’t like it:

![](<Base64-Image-Removed>)

The type of formula used – structured referencing – is not compatible with source creation in data validated lists. However, there is a simple workaround: just name this range, _viz._

![](<Base64-Image-Removed>)

Here, I have named the range **LU\_Simple\_Dynamic\_List** (**LU** simply stands for Look Up). Now, if I use this as my source,

![](<Base64-Image-Removed>)

it works! It’s a simple trick, but really useful and makes Tables one of your first ports of call should you require dynamic range names, _e.g._

![](<Base64-Image-Removed>)

### OFFSET Method

Sometimes, using the Tables approach is not appropriate. Tables increase in depth when data is added, but what if the list should extend or contract based on a formulaic constraint? Putting formulae in cells will automatically extend the Table, regardless if the outputs are seemingly blank (_e.g._**“”**).

This method is older than the Table approach, as Tables only appeared as recently as Excel 2007. The problem has been around for 20 years before that! Hence, enter the **OFFSET** function.

The syntax for **OFFSET** is as follows:

**OFFSET(Reference,Rows,Columns,\[Height\],\[Width\])**

The arguments in square brackets (**Height** and **Width**) may be omitted from the formula (they both have a default value of 1 which is explained further below).

In its most basic form, **OFFSET(Ref,x,y)** will select a reference **x** rows down (**\-x** would be **x** rows up) and **y** columns to the right (**\-y** would be **y** columns to the left) of the reference **Ref**. For example, consider the following grid:

![](<Base64-Image-Removed>)

**OFFSET(A1,2,3)** would take us two rows down and three columns across to cell **D3**. Therefore, **OFFSET(A1,2,3)** equals 16, _viz._

![](<Base64-Image-Removed>)

That’s how most people know – and use – **OFFSET**. However, it is the **Height** and **Width** optional arguments that are the useful ones when it comes to dynamic range names. If we consider the extended formula **OFFSET(D4,-1,-2,-2,3)**, it would take us first to cell **B3** but then we would select a range based on the **Height** and **Width** parameters. The **Height** would be two rows going up the sheet, with row 14 as the base (_i.e._ rows 13 and 14), and the **Width** would be three columns going from left to right, with column **B** as the base (_i.e._ columns **B**, **C** and **D**).

Hence, **OFFSET(D4,-1,-2,-2,3)** would select the range **B2:D3**, _viz._

![](<Base64-Image-Removed>)

Note that **OFFSET(D4,-1,-2,-2,3)** equates to _#VALUE!_ since Excel cannot display a matrix in one cell, but it does recognise it. However, if after typing in **OFFSET(D4,-1,-2,-2,3)** we press **CTRL + SHIFT + ENTER**, we turn the formula into an array formula: **{OFFSET(D4,-1,-2,-2,3)}** (do not type the braces in, they will appear automatically as part of the Excel syntax). This gives a value of 8, which is the value in the top left-hand corner of the matrix, _but Excel is storing more than that_. This can be seen as follows:

**SUM(OFFSET(D4,-1,-2,-2,3))** = 72 (_i.e._

**SUM(B2:D3)**)

**AVERAGE(OFFSET(D4,-1,-2,-2,3))** = 12 (_i.e._

**AVERAGE(B2:D3)**).

Indeed, we can construct a simple depreciation calculation, transpose references or even build a dynamic chart (one that displays more / less categories of information as required) using **OFFSET**’s **Height** and **Width** characteristics. Let me demonstrate with a couple of examples (again, these are available for perusal in the [attached Excel file](https://sumproduct.com/assets/thought-files/dynamic-range-names/sp-dynamic-range-names.xlsx)
).

In the first example, consider the following ‘messy’ list:

![](<Base64-Image-Removed>)

The number of items, given the range name **No\_of\_Items**, can be surmised simply using **\=COUNTA(Range)**, where **Range** is the data list (_i.e._ the cells in yellow). **COUNTA** simply counts the number of non-empty cells in the **Range**.

Simple manipulation can create an interim list removing the spaces:

![](<Base64-Image-Removed>)

The aim is to make a list that does not include the five blank rows. Assuming the first cell (_i.e._ where “Alpha” is situated) is cell **F29** on the worksheet **Sheet Name**, we can define the list as

**\=OFFSET(‘Sheet Name’!$F$29,,,No\_of\_Items,)**

Note that the sheet name must be included in this formula for it to work. No displacement occurs, but the depth is defined as five (**No\_of\_Items**) rows:

![](<Base64-Image-Removed>)

For the second example, just to change things up, I’ll use **Width** rather than **Height**. Here, let’s consider chart data as follows:

![](<Base64-Image-Removed>)

Check boxes have been used to include / exclude columns of data – in the example illustrated _(above)_, only every other column is included (again, the Table methodology would not work directly here). Simple manipulation gets the chart data table _(highlighted in the blue box, above)_.

A standard chart would include five categories, two with blank names and null values, but very simply, I can produce the following chart instead:

![](<Base64-Image-Removed>)

If I had four categories, the chart would update automatically to

![](<Base64-Image-Removed>)

All we need to do is define the range for the amounts and data using **OFFSET** once more. Assuming the chart data for titles starts in cell **H25** of the **SheetName** worksheet, the formulae for the dynamic range names will be as follows:

**LU\_Dynamic\_Amount:**

\=**OFFSET(SheetName!$H$26,,,,MAX(SheetName!$H$24:$L$24))**

**LU\_Dynamic\_Title:**

**\=****OFFSET(SheetName!$H$25,,,,MAX(SheetName!$H$24:$L$24))**

The width of these ranges will be **MAX(SheetName!$H$24:$L$24)**, _i.e._ three in this instance. This means the number of columns will total three! This is why an error check is required here: if all cells are unchecked, there will be no chart to render.

To get the range names into the chart data, there is one more twist: the range names referenced must include the name of the workbook, _e.g._

![](<Base64-Image-Removed>)

### INDIRECT Method

Excel’s **INDIRECT** function allows the creation of a formula by referring to the contents of a cell, rather than the cell reference itself.

The **INDIRECT(ref\_text,\[a1\])** function syntax has two arguments:

1.  **ref\_text** This is a required reference to a cell that contains an A1-style reference, an R1C1-style reference, a name defined as a reference, or a reference to a cell as a text string. If **ref\_text** is not a valid cell reference, **INDIRECT** returns the _#REF!_ error value. If **ref\_text** refers to another workbook (an external reference), the other workbook must be open. If the source workbook is not open, **INDIRECT** again returns the _#REF!_ error value
2.  **\[a1\]** This is optional (hence the square brackets) and represents a logical value that specifies what type of reference is contained in the cell **ref\_text**. If **a1** is TRUE or omitted, **ref\_text** is interpreted as an A1-style reference. If **a1** is **FALSE**, **ref\_text** is interpreted as an R1C1-style reference. Most modellers seldom consider this alternative referencing approach.

Essentially, **INDIRECT** works as follows:

![](<Base64-Image-Removed>)

In the above example, the formula in cell **H18** (the yellow cell) is

**\=INDIRECT(H11)**.

With only one argument in this function, **INDIRECT** assumes the A1 cell notation (_e.g._ the cell in the third row fourth column is cell **D3**). Note that the value in cell **H11** is **H13**, this formula returns the value / contents of cell **H13**, _i.e._ 187.

This idea can be extended to consider data validated lists (again, this example can be found in the [attached Excel file](https://sumproduct.com/assets/thought-files/dynamic-range-names/sp-dynamic-range-names.xlsx)
):

![](<Base64-Image-Removed>)

Here, I want to select a classification category in cell **G29**, based on the financial statement I select in cell **G28** (_e.g._ Balance Sheet -> Non-Current Liabilities).

The trick here is not to include spaces in the names of the financial statements. Then, in my illustration above, I have named cells **F13:F23****Income\_Statement**, cells **G13:G20****Balance Sheet** and cells **H13:H16****Cash\_Flow\_Statement**. Cells **F12:H12** have been used to construct a data validation list in cell **G28** and then the data validation list in cell **G29** has used the **INDIRECT** function in the ‘Source:’ field as follows:

![](<Base64-Image-Removed>)

As a different financial statement is selected in cell **G28**, so the list will update in cell **G29** (but only once the data validation list is activated, which is an Excel limitation).

### IF Method

So what’s the most **I**mportant **F**unction in Excel? Any takers for **IF**? The syntax for **IF** demonstrates just how useful this function is for financial modelling:

**\=IF(logical\_test,\[value\_if\_TRUE\],\[value\_if\_FALSE\])**

This function has three arguments:

*   **logical\_test**: this is the “decider”, _i.e._ a test that results in a value of either TRUE or FALSE. Strictly speaking, the **logical\_test** tests whether something is TRUE; if not, it is FALSE
*   **value\_if\_TRUE**: what to do if the **logical\_test** is TRUE. Note that you do not put square brackets around this argument! This is just the Excel syntax for saying sometimes this argument is optional. If this argument is indeed omitted, this argument will have a default value of TRUE
*   **value\_if\_FALSE**: what to do if the **logical\_test** is FALSE (strictly speaking, not TRUE). If this argument is left blank, this argument will have a default value of FALSE.

This function is actually more efficient than it may look at first glance. Whilst the **logical\_test** is always evaluated, only one of the remaining two arguments is computed, depending upon whether the **logical\_test** is TRUE or FALSE.

This function lends itself to a switch or a condition that can be used to determine between two ranges, for example:

![](<Base64-Image-Removed>)

In this scenario, two range names have been set up: **LU\_Alphabet** (cells **$F$13:$F$38**) and **LU\_Numbers** (cells **$G13:$G$22**). Cell **K13** contains a Yes / No dropdown box which is used to determine which list is used to populate the in-cell list in **K15**.

This latter cell uses data validation (**ALT + D + L**) with the source of the list defined as:

**\=IF($D$13=”Yes”,LU\_Alphabet,LU\_Numbers).**

### CHOOSE Method

Do you choose to use **CHOOSE**? This function uses **index\_number** to return a value from the list of value arguments. **CHOOSE** may be used to select one of up to 254 values based on the index number (**index\_number**).

The **CHOOSE** function employs the following syntax to operate:

**CHOOSE(index\_number, value1, \[value2\], …)**

The **CHOOSE** function has the following arguments:

*   **index\_number:** this is required and is used to specify which value argument is to be selected. The argument **index\_number** must be a number between 1 and 254, or a formula or reference to a cell containing a number between 1 and 254.
    *   if **index\_number** is 1, **CHOOSE** returns **value1**; if it is 2, **CHOOSE** returns **value2** and so on
    *   if **index\_number** is less than 1 or greater than the number of the last value in the list, **CHOOSE** returns the _#VALUE!_ error value
    *   if **index\_number** is a fraction, it is truncated to the lowest integer before being used.
*   **value1**, **value2**, …: **value 1** is required, but subsequent values are optional. There may be between 1 and 254 value arguments from which **CHOOSE** selects a value or an action to perform based on **index\_number**. The arguments can be numbers, cell references, defined names, formulas, functions, or text.

It should be further noted that:

*   If **index\_number** is an array, every value is evaluated when **CHOOSE** is evaluated
*   The value arguments to **CHOOSE** can be range references as well as single values.

For example, the formula:

**\=SUM(CHOOSE(2,A1:A10,B1:B10,C1:C10))**

evaluates to:

**\=SUM(B1:B10)**

which then returns a value based on the values in the range **B1:B10**.

The **CHOOSE** function is evaluated first, returning the reference **B1:B10**. The **SUM** function is then evaluated using **B1:B10**, the result of the **CHOOSE** function, as its argument. A similar idea is also expressed by the formula:

**\=SUM(A1:CHOOSE(2,A2,A3,A4))**

which will return the result of **\=SUM(A1:A3)**.

You may make the **index\_number** a cell reference or formula which will therefore then choose from the selected list of ranges specified. In essence, it’s like the **IF** example _(above)_ but with more alternatives:

**\=CHOOSE(index\_number,range1,range2,range3,…)**.

The [attached Excel file](https://sumproduct.com/assets/thought-files/dynamic-range-names/sp-dynamic-range-names.xlsx)
 provides an illustration of how this might work in practice.

![](<Base64-Image-Removed>)

**_Relative Referencing_**

By default, range names are referenced absolutely (_i.e._ contain the **$** sign so that references remain static). However, imagine a scenario where you are modelling revenue and you wish to grow the prior period value by inflation (already given a range name, say cell **C3** on **Sheet1**). Simply click on any cell (for example, I will use **D17** arbitrarily), then define the new range name as follows:

![](<Base64-Image-Removed>)

Note the ‘Refers to:’ entry. Cell **C17** (the cell to the left of **D17**) has been chosen without the dollar signs. This is a relative reference. Once we click on ‘OK’, the range name ‘**Prior\_Period**’ will be defined as the cell immediately to the left of the active cell. We can then inflate values easily by copying the formula

**\=Prior\_Period\*(1+Inflation)**

across the row, _etc._

### Word to the Wise

This article discusses just some of the methods available. There’s a myriad of other functions that may be used, _e.g._ **INDEX**, **COUNT** and using arrays. Further, data validated lists are used in many of the examples above. Do remember that when data validation is based on a condition / criterion elsewhere, the data validation will not update until the data validated cell is edited next.

As you get more experienced, you’ll start to play – sometimes out of necessity. That’s because Excel won’t always allow you to use dynamic range names in the same way “simple” range names may be used. And there’s only one way to learn that: the hard way…

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/dynamic-range-names/#0)
    
*   [Register](https://sumproduct.com/thought/dynamic-range-names/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/dynamic-range-names/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/dynamic-range-names/#0)

[](https://sumproduct.com/thought/dynamic-range-names/#0 "close")

top