# A to Z of Excel Functions: The INDIRECT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-indirect-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The INDIRECT Function

*   February 21, 2020

A to Z of Excel Functions: The INDIRECT Function
================================================

A to Z of Excel Functions: The INDIRECT Function
================================================

22 February 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **INDIRECT** function._

**The INDIRECT function**

Excel’s **INDIRECT** function allows the creation of a formula by referring to the contents of a cell, rather than the cell reference itself.

The **INDIRECT(ref\_text,\[a1\])** function syntax has two arguments:

*   **ref\_text:** this is a required reference to a cell that contains an **A1**\-style reference, an R1C1-style reference, a name defined as a reference or a reference to a cell as a text string. If **ref\_text** is not a valid cell reference, **INDIRECT** returns the _#REF!_ error value. If **ref\_text** refers to another workbook (an external reference), the other workbook must be open. If the source workbook is not open, **INDIRECT** again returns the _#REF!_ error value.
*   **\[a1\]** This is optional (hence the square brackets) and represents a logical value that specifies what type of reference is contained in the cell **ref\_text**. If **a1** is TRUE or omitted, **ref\_text** is interpreted as an **A1**\-style reference. If **a1** is FALSE, **ref\_text** is interpreted as an R1C1-style reference. Most modellers seldom consider this alternative referencing approach, which is not without its merits _(see below)_.

Essentially, **INDIRECT** works as follows:

![](<Base64-Image-Removed>)

In the above example, the formula in cell **H18** (the yellow cell) is

**\=INDIRECT(H11)**.

With only one argument in this function, **INDIRECT** assumes the **A1**\-cell notation (_e.g._ the cell in the third row fourth column is cell **D3**). Note that the value in cell **H11** is **H13**, this formula returns the value / contents of cell **H13**, _i.e._ 187.

This idea can be extended: the value indirectly referred to does not need to be in the same worksheet (or even workbook) as follows:

![](<Base64-Image-Removed>)

The formula in the yellow-coloured cell (**H17**) uses concatenation:

**\=INDIRECT(“‘”&H11&”‘!”&H12)**.

This formula is difficult to read. Let’s make it clearer. **H11** in my example is **Sum\_First\_Ten\_Rows\_BA**, which is the name of another worksheet in the workbook and **F29** is the cell to be linked to. In other words, this formula becomes

**\=’Sum\_First\_Ten\_Rows\_BA’!F29**,

which will make more sense to end users. The point is, however, the value in cell **H11** can be changed so that the formula suddenly links to a completely different worksheet.

Eagle-eyed readers may note that worksheet names without spaces do not need apostrophes. Whilst this is true, I include them here so that the formula will work in general.

**_Advantages of INDIRECT_**

**INDIRECT** has useful properties that may be exploited. For example, consider the following illustration:

![](<Base64-Image-Removed>)

Imagine you wanted to sum the first ten values in this list. The obvious formula to use would be

**\=SUM(F11:F20)**.

However, what happens if someone inadvertently inserts or removes rows in this range? If a row were to be inserted the formula would automatically update to **\=SUM(F11:F21)**, which most of the time would be what would be required. On occasion, though, it might be important that only the first ten values are still summed. **INDIRECT** can ensure this happen, _viz_.

**\=SUM(INDIRECT(“F11:F20”))**.

Note that when a reference is typed in like this it should be included in inverted commas as displayed. Using this formula will maintain the integrity of the referencing as required.

So far, all of my examples use the **A1**\-style of cell referencing. However, using the R1C1 (row / column approach where the third row fourth column would be (3,4)) has benefits too. When this method is used, I often use **INDIRECT** in conjunction with the **[ADDRESS](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-address-function)
** function.

The

**ADDRESS(row\_number, column\_number)**

function syntax has the following arguments:

*   **row\_number** is a numeric value that specifies the row number to use in the cell reference
*   **column\_number** is also required and is a numeric value that specifies the column number to use in the cell reference.

Therefore **\=ADDRESS(3,4)** is **$D$3**.

![](<Base64-Image-Removed>)

Just using **INDIRECT** in the example above, cell **H29** uses concatenation once more:

**\=INDIRECT(“R”&H11&”C”&H12,FALSE)**.

The second argument (**FALSE**) is necessary to recognise the R1C1 notation. Here, this formula reduces to **\=R22C9**, which is the 22nd row, ninth column, i.e. delivers the value in cell **I22** (highlighted in red).

This formula can be difficult to understand for the uninitiated. I am not saying the following is necessarily simpler, merely it is an alternative. The second formula in cell **H31** is

**\=INDIRECT(ADDRESS(H11,H12))**.

This does not need the R1C1 notation as **ADDRESS(H11,H12)** equals cell **$I$22**.

Another advantage I would like to mention is in generating dynamic data validation lists. This example may be found in the [attached Excel file](https://sumproduct.com/assets/blog-pictures/2020/a-to-z/241/sp-indirect-examples.xls)
:

![](<Base64-Image-Removed>)

Here, I want to select a classification category in cell **G28**, based on the financial statement I select in cell **G27** (_e.g._ Balance Sheet, Current Assets).

The trick here is not to include spaces in the names of the financial statements.

Then, first of all, in my illustration above, I have named cells **F12:F22****Income\_Statement**, cells **G12:G19****Balance Sheet** and cells **H12:H15****Cash\_Flow\_Statement**. Cells **F11:H11** have been used to construct a data validation list in cell **G27** and then the data validation list in cell **G28** has used the **INDIRECT** function in the ‘Source:’ field as follows:

![](<Base64-Image-Removed>)

As a different financial statement is selected in cell **G27**, so the list will update in cell **G28** (but only once the data validation list is activated, which is an Excel limitation).

One last – and key – example: how often do you seek a summary sheet which selects data from one of several similarly constructed datasheets? I have seen all sorts of weird and wonderful formulae to perform this common requirement, but **INDIRECT** is by far one of the simplest approaches available.

Consider the following file, which has several similar worksheets:

![](<Base64-Image-Removed>)

I might require a summary sheet:

![](<Base64-Image-Removed>)

In my example, I have called my similar worksheets **Guns\_BA** and **Drugs\_BA**. The **BA** here refers to “Blank Assumptions” but it could mean “Basically Anything”, _i.e._ the worksheet names contain more than just the business unit name.

With cell **H9** named **Selection**, the formula used in the calculations is simply

**\=INDIRECT(“‘”&Selection&”\_BA’!RC”,FALSE)**.

However, as well as apostrophes and concatenation this formula uses a neat trick. The second argument must be **FALSE** (_i.e._ the formula assumes the R1C1 notation). When this is selected the **RC** in the above formula means use the row and column reference of the cell this formula is in. This avoids unnecessary hard code and generates a formula that changes reference depending upon the formula location in the worksheet. For example, in cell **G12**, the formula reduces to **\=’Guns\_BA’!G12** and in cell **J21**, it reduces to **\=’Guns\_BA’!J21**, _etc._

Very useful!

**_Disadvantages of INDIRECT_**

Not all modellers embrace this useful function. There are three key issues with I**NDIRECT**:

1.  **INDIRECT** encourages the use of hard code in formulae. This should always be a last resort as this leads to a potential lack of transparency and flexibility in a model
2.  **INDIRECT** is a difficult function to review / audit, as the cell(s) it refers to is not the ultimate location of the value used in the formula. Excel’s in-built auditing tools are of limited use and the formulae can be highly confusing and ‘clunky’
3.  If **ref\_text** refers to a cell range outside the row limit of 1,048,576 or the column limit of 16,384 (**XFD**), **INDIRECT** returns an _#REF!_ error. However, this behaviour is different in earlier versions of Excel, which ignored the exceeded limit and returned an often meaningless value instead. This can lead to compatibility issues between versions of Excel (admittedly, these earlier versions are outdated, no longer supported, and therefore, should not be used).

Ultimately, the use of **INDIRECT** becomes a subject “horses for courses” issue. If modellers are knowledgeable and wary of its limitations, **INDIRECT** can simplify and resolve many common modelling problems. Just be careful out there.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-indirect-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-indirect-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-indirect-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-indirect-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-indirect-function/#0 "close")

top