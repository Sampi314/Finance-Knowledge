# Names

**Source:** https://sumproduct.com/thought/names/

---

[Home](https://sumproduct.com/)

\> Names

*   May 14, 2025

Names
=====

Highlighting the pros and cons of using names in Excel.

Naming Names
============

What’s in a name? This article considers the pros and cons of using names in Excel. By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

I am in two minds whether I should be using range names in my Excel spreadsheets. Any advice?

Advice
------

If you were to ask modelling professionals about the merits of using range names you will find that opinion is strongly divided. In spreadsheets, used appropriately and sparingly, great value can be obtained from using range names, as it can make formulae easier to read. In macros (not discussed here), they are vital. Overuse, on the other hand, can lead to end user confusion.

### Creating Range Names

Range names are created using ‘Define Name’ in Excel 2003 and earlier, whilst they are created via ‘Name Manager’ in Excel 2007 and later. The Name Box (circled, below),

![](<Base64-Image-Removed>)

Name Box

drop down menus and / or Ribbon may be used, or keyboard shortcuts such as ALT + I + N + D (Excel 2003 and earlier) or ALT + I + N + D + N or ALT + M + N (Excel 2007 and later). I would suggest using none of these methods. Simply used the keyboard shortcut CTRL + F3 in all versions of Excel, and then if using Excel 2007 or later, click on the ‘New’ button in the ‘Name Manager’ dialog box), viz.

### Define Name (Excel 2003 and earlier)

![](<Base64-Image-Removed>)

### Name Manager (Excel 2007 and later)

![](<Base64-Image-Removed>)

In Excel 2007 and later versions, after clicking on ‘New’ (above), the following dialog box appears:

![](<Base64-Image-Removed>)

New Name dialog box (Excel 2007 and later)

Scope
=====

Note the highlighted section (Scope). All names have a scope, either to a specific worksheet (also called the local worksheet level) or to the entire workbook (also called the global workbook level). The scope of a name is the location within which the name is recognised without qualification.

For example, if you have defined a range name as ‘Profit’ with its scope as Sheet1 (say) rather than ‘Workbook’, then it will only be recognised in Sheet1 as ‘Profit’ (i.e. without qualification).

To use this local name in another worksheet, you must qualify it by preceding it with the localised worksheet name:

\=Sheet1!Profit.

If you have defined a name, such as ‘Cashflow’, and its scope is the workbook, that name is recognised for all worksheets in that workbook (but not for any other workbook).

A name must always be unique within its scope. Excel prevents you from defining a name that is not unique within its scope. However you can use the same name in different scopes. For example, you can define a name, such as ‘Profit’ that is scoped to Sheet1, Sheet2, and Sheet3 in the same workbook. Although each name is the same, each name is unique within its scope. You might do this to ensure that a formula that uses the name ‘GrossProfit’ (say) is always referencing the same cells at the local worksheet level.

You can even define the same name, ‘Profit’ for the global workbook level, but again this scope is unique. In this case, there may be a name conflict. To resolve this conflict, Excel uses the name that is defined for the worksheet by default. The local worksheet level takes precedence over the global workbook level. This can be circumvented by adding the following prefix to the name, e.g. rename it ‘WorkbookFile!Profit’ instead.

It is possible to override the local worksheet level for all worksheets in the workbook, except for the first worksheet. This will always use the local name if there is a name conflict and cannot be overridden.

In Excel 2003 and earlier, this scope functionality is not visible explicitly. All names created are assumed to be global by default, until the same name is used on a second worksheet.

### Care with Names

The Name string must begin with a text or underscore character. Remaining characters in the name can be letters, numbers, periods, and underscore characters. Spaces are not allowed but two words can be joined, or with an underscore (\_) or period (.), for example, to enter the Name ‘Cash Flow’ you should enter ‘Cash\_Flow’ or ‘Cash.Flow.’.

You cannot use a Name that could otherwise be confused as a cell reference, for example, A1, as this is already a cell reference.  
There is no limit on the number of Names you can define, but a name may only contain up to 255 characters (why on earth you would want something this long is beyond me).

Names can contain uppercase and / or lowercase letters. Excel does not distinguish between uppercase and lowercase characters in names. For example, if you have created the global name ‘Profit’ and then create another global name called ‘PROFIT’ in the same workbook, the second name will replace the first one.

It is not a syntax issue, but I strongly recommend thought is given to adding prefixes to range names. Regular readers will note that my list range names always begin with ‘LU\_’ where ‘LU’ stands for ‘Look Up’. Similarly, I use ‘BC\_’ for ‘Base Cell’ when working with the OFFSET function (see the [following link](https://www.sumproduct.com/thought/onset-of-offset)
).

By using these prefixes, I understand the purpose of the range name and so that names with a common purpose are grouped together in a list. This is not to say all range names should contain a prefix. ‘Tax\_Rate’, for instance, makes sense on its own and adding a prefix would only detract from the name given, potentially confusing the end user.

### Creating Range Names Quickly

There is a nifty shortcut for creating range names using existing names. Consider the following list:

![](<Base64-Image-Removed>)

Example list in Excel

Imagine you were to highlight cells N12:N18 in the above example and then use the shortcut CTRL + SHIFT + F3:

![](<Base64-Image-Removed>)

Create Names dialog box

With the first check box (‘Top row’) checked, by clicking on ‘OK’ the range N13:N18 (not N**12**:N18) will be named ‘Phonetic\_Alphabet’ (i.e. the underscore will be added automatically). Ranges across rows can be named in seconds similarly using ‘Left column’ similarly.

The reason this dialog box uses check boxes (rather than option buttons) is to allow users to select more than one at a time. For example:

### Example data table in Excel

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Highlighting N31:R34 and using the keyboard shortcut CTRL + SHIFT + F3 once more should generate the Create Names dialog box as above with both ‘Top row’ and ‘Left column’ checked. This means that O32:O34 will be called ‘Jan’, O33:R33 will be called ‘COGS’ and so on. This would take considerably longer to perform manually.

This example also illustrates why spaces are illegal characters in range names (and for that matter, should not be added to formulae either). Space is the **intersect operator** in Excel. If you were to type the following formula:

\=Gross\_Margin Feb,

Excel would return the value in cell P34 (the intersection of the two ranges, above), i.e. $4,183. This can be a powerful yet quick and simple analytical tool for key outputs.

### Using Range Names Quickly

One of the reasons I like using the CTRL + F3 shortcut is that it is part of the F3 ‘Names family of shortcuts’. We have just seen how CTRL + SHIFT + F3 can be useful – and so can F3 on its own.

Perhaps superseded by the fact that in Excel 2007 and later versions Excel will now prompt as you type formulae, F3 has been very useful in the past as the ‘Paste Names’ shortcut. For example, as you type a formula you can refer to a range name by simply typing F3 to get the Paste Names dialog box, viz.

![](<Base64-Image-Removed>)

Paste Names dialog box

Selecting one of the cells and clicking ‘OK’ inserts the range name.

However, look closer at the dialog box. The ‘Paste List’ button in the bottom left hand corner, if depressed, will paste the list and their definitions into a pre-selected range of cells in an Excel worksheet which can be invaluable for model auditing purposes.

Sometimes, formulae have been written before the range name was created. In some circumstances, it is possible to apply these names retrospectively using Insert -> Names -> Apply in Excel 2003 and earlier and using ‘Apply Names’ within the ‘Defined Names’ group of the ‘Formulas’ tab, viz.

![](<Base64-Image-Removed>)

Apply Names, Excel 2007 and later

Note that the keyboard shortcut ALT + I + N + A will work in all versions of Excel. Selecting the required range names in the resulting dialog box

![](<Base64-Image-Removed>)

Apply Names dialog box

will see formulae on the active worksheet(s) updated accordingly.

### Deleting Range Names

If I got paid just $1 for every time I have been asked how to delete range names I would probably have retired by now. This was chiefly attributable to the counter-intuitive menu in Excel 2003 and earlier versions:

![](<Base64-Image-Removed>)

Insert -> Name -> Define

From the resulting dialog box, you would then select the range name (unfortunately, only one at a time could be selected) and hit ‘Delete’, viz.

![](<Base64-Image-Removed>)

Deleting in Excel 2003 and earlier versions

Excel 2007 and later makes this much simpler. In this case, users are more likely to go to the ‘Name Manager’ rather than the confusing ‘Insert’ drop down menu:

![](<Base64-Image-Removed>)

Deleting in Excel 2007 and later versions

The other marked improvement is that multiple names may be deleted simultaneously by using the CTRL or SHIFT buttons to make multiple selections before hitting the ‘Delete’ button.

### Relative Referencing

By default, range names are referenced absolutely (i.e. contain the $ sign so that references remain static). However, imagine a scenario where you are modelling revenue and you wish to grow the prior period value by inflation (already given a range name, say cell C3 on Sheet1). Simply click on any cell (for example, I will use D17 arbitrarily), then define the new range name as follows:

![](<Base64-Image-Removed>)

Defining the Prior\_Period

Note the ‘Refers to:’ entry. Cell C17 (the cell to the left of D17) has been chosen without the dollar signs. This is a relative reference. Once we click on ‘OK’, the range name ‘Prior\_Period’ will be defined as the cell immediately to the left of the active cell. We can then inflate values easily by copying the formula

\=Prior\_Period\*(1+Inflation)

across the row.

### Other Types of Names

Most of us use the terms ‘names’ and ‘range names’ synonymously. However, this is not strictly true. We can create names referring to formulae as we did in the [following link](https://www.sumproduct.com/thought/creating-a-timestamp)
:

![](<Base64-Image-Removed>)

Example of a name referring to a formula

Previously, in [this link](https://www.sumproduct.com/thought/onset-of-offset)
, the [associated Excel file](https://sumproduct.com/assets/thought-files/e-m/offset-examples.xls)
 provided an example of how to create dynamic range names which vary in size depending upon the number of non-blank items to be considered.

Names may also refer to functions, dates and constants – the latter can be useful (e.g. ‘Months\_in\_Year’ is defined as 12) in order to avoid inserting hard code into a formula.

### And Finally…

This article discusses just the tip of the Names iceberg. Experimenting can pay big dividends. The aim is not to go overboard, however, as a preponderance of names in a work book may actually make formulae – and hence your model – more difficult to follow.

Further, be careful if you name ranges that are then deleted. The range names will not be deleted (even though they will no longer appear in the Name Box). They will need to be deleted as described above in order to cause potential errors in formulae, etc.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/names/#0)
    
*   [Register](https://sumproduct.com/thought/names/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/names/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/names/#0)

[](https://sumproduct.com/thought/names/#0 "close")

top