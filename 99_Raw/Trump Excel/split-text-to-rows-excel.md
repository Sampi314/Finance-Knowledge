# Split Text into Multiple Rows in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/split-text-to-rows-excel

---

[Skip to content](https://trumpexcel.com/split-text-to-rows-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/split-text-to-rows-excel/#below-title)

Most of the time, the data in Excel is arranged in columns, and it is more common to split the text in a cell into multiple columns rather than rows.

But in some cases, you may want to split the text into multiple rows in Excel.

For example, if you have multiple names in a single cell and you want to slit these names and get these in a column in different rows.

Or you may have an address in a cell, and you want to split different parts of the address and get them in different rows.

In this article, I will show you some simple formulas and methods you can use to quickly split text in a cell into multiple rows (depending on the delimiter)

[_**Click here to download the example file and follow along**_](https://www.dropbox.com/scl/fi/rwhmpg397mb8takd8tyw3/Split-Cell-into-Rows.xlsm?rlkey=602pp7a0ldbsncjkwepfn3uwb&dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/split-text-to-rows-excel/#)

Split Text into Rows Using TEXTSPLIT Function
---------------------------------------------

If you’re using Excel for Microsoft 365 (Windows or Mac) or Excel for the Web, you can make use of the new **TEXTSPLIT function**.

TEXTSPLIT function splits the text in a cell into rows or columns based on the specified delimiter.

It works just like the [Text-to-Columns functionality in Excel](https://trumpexcel.com/excel-text-to-columns-examples/)
, but since this is a formula, it’s even better.

Let me show you some examples where you can use this function.

### Split Based on One Delimiter

Below is an example where I have an address in cell A2, and I want to split different parts of the address (i.e., name, street name, city, and State/pin code) into different rows in a column.

![Address in cell A2 for text to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20118'%3E%3C/svg%3E)

In this case, these different parts of the address are separated by a comma, which I will use as the delimiter to do the split.

Below is the formula that will split the content in the cell into separate rows:

\=TEXTSPLIT(A2,,", ")

![TEXTSPLIT function to split text to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20580%20301'%3E%3C/svg%3E)

The above TEXTSPLIT formula takes three arguments:

*   **text** – This is the first argument where I’ve used the cell reference of the cell (A2) that contains the text that I want to split
*   **col\_delimiter** – This is the second argument where you are supposed to specify the delimiter based on which the split would happen in separate columns. In this case, since I want the text to be split into rows instead of columns, I have left this argument blank.
*   **\[row\_delimiter\]** – This is the third argument where I need to specify the delimiter based on which the text would be split into separate rows. Since I want the address to be split after each comma, I have used “, ” as the delimiter. Note that your delimiter needs to be in double quotes.

**Note**: The TEXTSPLIT function also has three more optional arguments, which we didn’t need in this example. You can [read more about this function here](https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7)
.

Also, in the above example, I have used “, ” as the delimiter (i.e., a comma followed by a space character).

This is because every part of the address was followed by a comma and then a space character before the next part starts. In case your data only has a comma without the space character, you can change the delimiter accordingly.

Alternatively, you can use the below formula that can handle all types of situations:

\=TRIM(TEXTSPLIT(A2,,","))

![TRIM and TEXTSPLIT functoin for text to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20305'%3E%3C/svg%3E)

The [TRIM function](https://trumpexcel.com/excel-trim-function/)
 ensures that there are [no leading space characters](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 in any of the cells.

Also read: [How to Split Cells in Excel (separate into multiple columns)](https://trumpexcel.com/split-cells-in-excel/)

### Split Based on Two or More Delimiters

TEXTSPLIT can also handle situations where you want to split the text in the cell based on two or more delimiters.

Below is this example where I have an address in cell A2, and there are two delimiters (a dash separates the name and the address, and a comma separates all the different elements of the address)

![Address with two delimiters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20596%20115'%3E%3C/svg%3E)

Here is one single formula that would consider two delimiters while splitting the text in the cell into rows:

\=TRIM(TEXTSPLIT(A2,,{",","-"}))

![Textsplit function using two delimiters to convert text to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20670%20309'%3E%3C/svg%3E)

In the above example, I have the following arguments in the TEXTSPLIT function:

*   **text** – This is the cell reference of the cell (A2) that I want to split
*   **col\_delimiter** – This is the column delimiter, but since I want the text to be split into rows instead of columns, this argument is left blank.
*   **\[row\_delimiter\]** – This is the third argument where I need to specify the delimiter based on which the text would be split into separate rows. Since I want the address to be split based on two delimiters (dash and comma), I have used an array {“,”,”-“}. This tells the formula to check for all the delimiters specified in the curly brackets.

### Split Based on Line Breaks

Another situation where you may want to split a cell’s content into rows is when there are line breaks in the cell, and you want to get each line in a separate cell in a column.

Below, I have this example where I have the address in cell A2, and there are multiple line breaks in the address.

![Address with line breaks in the same cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20596%20197'%3E%3C/svg%3E)

Instead of getting multiple lines in the same cell, I want to split the content of this address so that I get each line in a separate row in a column.

This can again quickly be done using the TEXTSPLIT function, where I need to somehow use a line break as the delimiter.

And how do I do that?

By using a formula that returns a line break, which can then be used within the TEXTSPLIT function as the delimiter.

Below is the formula that will split the address using line breaks:

\=TEXTSPLIT(A2,,CHAR(10))

![Textsplit function to convert text to rows using line space as delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20398'%3E%3C/svg%3E)

In the above formula, I have used CHAR(10) as the row delimiter, where CHAR(10) returns the line break character.

Also read: [How to Split Multiple Lines in a Cell into a Separate Columns](https://trumpexcel.com/split-multiple-lines/)

### Split Multiple Cells into Rows in One Column

One particular case where the TEXTSPLIT function is a lifesaver is when you have data in multiple rows in a column, and you want to split each cell but still get the result in one column,

Below is an example of what I mean.

![Data set to split text to rows when you have multiple cells data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20351'%3E%3C/svg%3E)

I have names in three cells in column A that are separated by commas, and I want to split all these names so that I get individual names in separate cells in the same column (as shown below).

I imagine it would be a complex formula to do this without TEXTSPLIT, but with it, it’s not that hard.

Here is the formula to do this:

\=TRIM(TEXTSPLIT(TEXTJOIN(",",,A2:A4),,","))

![TEXTJOIN and TEXTSPLIT function to split text by delimiter and combine in one column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20776%20401'%3E%3C/svg%3E)

The trick in this formula is to use the TEXTJOIn function to combine all the names in different cells so that we get one single array of names that are separated by a comma.

In the text join function, the first argument is the delimiter (which is a comma in this case) that is used when combining the content of all the cells.

The result of the TEXTJOIN function is:

_“Stephen, James, Anna,Richard, Helen, Toby,Chris, Mark, Doug”_

This array is then used in the TEXTSPLIT function which then splits it using comma as the delimiter.

**Caution**: Remember that TEXTSPLIT is a new function in Excel for Microsoft 365 and would not have backward compatibility with other functions. So, if you use it in your workbook and send it to someone who’s using an older version of Excel, they will see an error.

[_Click here to download the example file and follow along_](https://www.dropbox.com/scl/fi/rwhmpg397mb8takd8tyw3/Split-Cell-into-Rows.xlsm?rlkey=602pp7a0ldbsncjkwepfn3uwb&dl=1)

Also read: [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)

Split Text into Rows Using Text-to-Columns and Transpose
--------------------------------------------------------

If you’re not using Excel for Microsoft 365, you will not have access to the TEXTSPLIT function.

So, you will have to rely on the built-in Text to Columns functionality to first split the text into columns and then transpose the result.

Let me show you how it works.

Below is an example where I have an address in cell A2 that I want to split (using a comma as the delimiter) and get the result in separate rows.

![Address in cell A2 for text to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20118'%3E%3C/svg%3E)

The first step would be to use Text to Columns to split it into columns. This can be done using the below steps:

1.  Select the cell (or range of cells) that have the data
2.  Click the Data tab

![Click the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20223'%3E%3C/svg%3E)

3.  Click on the Text to Columns icon (it’s in the Data Tools group)

![Click on Text to columns option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20572%20223'%3E%3C/svg%3E)

4.  In the ‘Convert Text to Columns Wizard’, select the Delimited option and then click on Next.

![Select the delimited option and click on next](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20499'%3E%3C/svg%3E)

5.  Select ‘Comma’ as the delimiter (uncheck all the other options) and click on Next.

![Select, as the delimiter and click on next](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20499'%3E%3C/svg%3E)

6.  Select the Destination cell where you want the result, then click Finish. In this case, I would select A4 as the destination cell.

![select the destination cell and then click on finish](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20499'%3E%3C/svg%3E)

This will give you the result shown below, where it has split our data, but we have got it in columns instead of rows.

![Result of text to columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20896%20211'%3E%3C/svg%3E)

So now we will use the transpose functionality to transpose this data.

Here are the steps to do this:

1.  Select the cells that you want to transpose.
2.  Copy these cells. You can either use the shortcut Control + C, or right-click on the selection and then click on Copy.
3.  Right on the destination cell where you want the transposed result.
4.  Hover the cursor over the Paste Special option (at the arrow icon to show more options. Click on the Transpose option.

![Click on the paste value as transpose icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20493'%3E%3C/svg%3E)

The above steps would give you the transposed data, and then you can delete the result of text to columns if you want.

![Text columns result is transposed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20883%20317'%3E%3C/svg%3E)

While this does work, it’s not as elegant as the TEXTSPLIT function method. It involves a lot more steps and has the following limitations:

*   The result of this method is static, unlike the TEXTSPLIT function method, where the result is dynamic. So if you change the original data, the result will not update (while it would when you use the TEXTSPLIT function)
*   You can only split based on one delimiter, while with the TEXTSPLIT function, you can use multiple delimiters.

Also read: [Separate First and Last Name in Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)

Split Text into Rows Using VBA (Custom Function)
------------------------------------------------

If you don’t have the TEXTSPLIT function in your version of Excel, you can a good workaround would be to create your own function using VBA.

It’s called a [User Defined Function (UDF)](https://trumpexcel.com/user-defined-function-vba/)
.

It’s pretty straightforward, and once the function is created, you can use it like any other function in the worksheet.

Below is the VBA code that will create a function that will split the text in a cell into rows (based on the specified delimiter).

    'Code developed by Sumit Bansal from https://trumpexcel.com
    
    Function SplitCellToRows(CellValue As Range, Delimiter As String)
        Dim SplitValues() As String
        
        'Split the value by the specified delimiter into an array
        SplitValues = Split(CellValue.Value, Delimiter)
        
        'Go through each element of the array and remove any leading or trailing spaces
        For i = LBound(SplitValues) To UBound(SplitValues)
                SplitValues(i) = Trim(SplitValues(i))
        Next i
        
        'Return the array
        SplitCellToRows = WorksheetFunction.Transpose(SplitValues)
        
    End Function

The above function (called SplitCellToRows) takes two arguments:

*   The cell reference of the cell that has the text that we want to split into rows
*   The delimiter in double quotes

[_Click here to download the example file and follow along_](https://www.dropbox.com/scl/fi/rwhmpg397mb8takd8tyw3/Split-Cell-into-Rows.xlsm?rlkey=602pp7a0ldbsncjkwepfn3uwb&dl=1)

### Where to Put this Code?

Below are the steps to put this code in the VB Editor:

1.  Hold the ALT key and then press the F11 key. This is going to open the VB editor. Alternatively, you can also [click on the Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Visual Basic icon in the ribbon.
2.  In the VB editor menu, click on the Insert option and then click on Module. This is going to insert a new module where we are going to copy-paste our above custom function code.

![Insert a new module in the vb editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20353'%3E%3C/svg%3E)

3.  Copy-paste the above VBA code into the module code window.

![Copy and paste the vba code into the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20278'%3E%3C/svg%3E)

4.  Click on the Save icon in the toolbar (or use Control + S)

![Save the code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20155'%3E%3C/svg%3E)

5.  Close the VB Editor to go back to the worksheet.

Once you have placed the code in the VB editor, you can go back to the worksheet and use this function just like any other regular worksheet function.

### How to Use this VBA Custom Function?

Below is an example where I have an address in cell A2 that I want to split into rows.

![Address in cell A2 for text to rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20118'%3E%3C/svg%3E)

I can use the formula below to get the result in cell A4:

\=SplitCellToRows(A2,",")

![Using the vba user defined function in the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20311'%3E%3C/svg%3E)

The above formula takes two arguments:

*   **A2** – This is the cell reference of the cell that has the address
*   **“,”** – Since my delimiter is a comma, I’ve specified that within double quotes.

### Things to Know When Using VBA-Created Functions

*   If you want to reuse this function later, you need to save your file with a macro-enabled workbook extension (.xlsm)
*   Unlike other worksheet functions, a User Defined Function (UDF) created with vb would not show you any _intellisense_ or help regarding the arguments of the function. You need to know how many and what type of arguments the function would take.
*   If you share this workbook with other people, the function will not work on their file unless they also add the function code to their VB Editor.

These are some of the methods you can use to split the text into rows in Excel.

If you’re using Excel for Microsoft 365, you don’t need to look beyond the TEXTSPLIT function, as it can handle this easily.

If you do not have access to the TEXTSPLIT function, you can either use the Text to Columns feature and then transpose the result, or you can create your own custom function using VBA.

**Other Excel articles you may also like:**

*   [How to Split a Cell Diagonally in Excel (Insert Diagonal Line)](https://trumpexcel.com/split-cell-diagonally-excel/)
    
*   [Excel VBA Split Function](https://trumpexcel.com/vba-split-function/)
    
*   [Convert Columns to Rows in Excel](https://trumpexcel.com/convert-columns-to-rows-excel/)
    
*   [Transpose Multiple Rows into One Column](https://trumpexcel.com/transpose-multiple-rows-into-one-column/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “Split Text into Multiple Rows in Excel”
------------------------------------------------------

1.  Very good tutorial. Thanks for sharing. I have always liked your tutorials and videos. Glad to get this one because I haven’t seen much from you lately. Keep up the good work. It is appreciated.  
    Thank You.
    
    [Reply](https://trumpexcel.com/split-text-to-rows-excel/#comment-15095)
    
2.  Hello Sumit,
    
    Thank you for showing these techniques !!  
    I am familiar with text to column feature however, Text to row and splitting text with two or more delimiters is quite new, Thank you for imparting your useful knowledge. And the elaboration is as always great.
    
    Since, you have vast knowledge on excel, Can I have a request for creating series of videos/articles on Google worksheets, there are surely many of like me who are dealing day to day activities in google sheets and your guidance on this will be helpful and it is cherry on the top, Kindly have a thought on this.
    
    Looking forward to see more videos and hear you back on google sheets videos.
    
    [Reply](https://trumpexcel.com/split-text-to-rows-excel/#comment-15090)
    
3.  Thanks for this article, very useful.
    
    [Reply](https://trumpexcel.com/split-text-to-rows-excel/#comment-15087)
    
4.  Thank you so much, Mr Bansal, I would have preferred the video tutorial, is easier for me to follow.
    
    [Reply](https://trumpexcel.com/split-text-to-rows-excel/#comment-15081)
    
5.  I have used TEXTSPLIT before but this article really shows the power of the function.  
    Thanks – much appreciated
    
    [Reply](https://trumpexcel.com/split-text-to-rows-excel/#comment-15079)
    
    *   Glad you liked it! Some of these new Excel functions MS has added are amazing. It makes things so easier that used to take a lot of complex formulas in the past
        
        [Reply](https://trumpexcel.com/split-text-to-rows-excel/#comment-15080)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/split-text-to-rows-excel/#respond)

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