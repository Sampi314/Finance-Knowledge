# Excel Wildcard Characters - Why Aren't You Using These?

**Source:** https://trumpexcel.com/excel-wildcard-characters

---

[Skip to content](https://trumpexcel.com/excel-wildcard-characters/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-wildcard-characters/#below-title)

**Watch Video on Excel Wildcard Characters**

There are only 3 Excel wildcard characters (asterisk, question mark, and tilde) and a lot can be done using these.

In this tutorial, I will show you four examples where these Excel wildcard characters are absolute lifesavers.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-wildcard-characters/#)

Excel Wildcard Characters – An Introduction
-------------------------------------------

Wildcards are special characters that can take any place of any character (hence the name – wildcard). 

There are three wildcard characters in Excel:

1.  **\* (asterisk)** – It represents any number of characters. For example, Ex\* could mean Excel, Excels, Example, Expert, etc.
2.  **? (question mark)** – It represents one single character. For example, Tr?mp could mean Trump or Tramp.
3.  **~ (tilde)** – It is used to identify a wildcard character (~, \*, ?) in the text. For example, let’s say you want to find the exact phrase Excel\* in a list. If you use Excel\* as the search string, it would give you any word that has Excel at the beginning followed by any number of characters (such as Excel, Excels, Excellent). To specifically look for excel\*, we need to use ~. So our search string would be excel~\*. Here, the presence of ~ ensures that excel reads the following character as is, and not as a wildcard.

_Note: I have not come across many situations where you need to use ~. Nevertheless, it is a good to know feature._

Now let’s go through four awesome examples where wildcard characters do all the heavy lifting.

Excel Wildcard Characters – Examples
------------------------------------

Now let’s look at four practical examples where Excel wildcard characters can be mighty useful:

1.  Filtering data using a wildcard character.
2.  Partial Lookup using wildcard character and VLOOKUP.
3.  Find and Replace Partial Matches.
4.  Count Non-blank cells that contain text.

### #1 Filter Data using Excel Wildcard Characters

Excel wildcard characters come in handy when you have huge data sets and you want to [filter data](https://trumpexcel.com/excel-data-filter/)
 based on a condition.

Suppose you have a dataset as shown below:

![Excel Wildcard Characters - Data Companies](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20178%20166'%3E%3C/svg%3E)

You can use the asterisk (\*) wildcard character in data filter to get a list of companies that start with the alphabet A.

Here is how to do this:

*   Select the cells that you want to filter.
*   Go to Data –> Sort and Filter –> Filter _(Keyboard Shortcut – Control + Shift + L)._
*   Click on the filter icon in the header cell ![Wildcard Characters in Excel - Filter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20136%2045'%3E%3C/svg%3E)
*   In the field (below the Text Filter option), type **A\*![Excel Wildcard Characters - Filter Field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20271%20443'%3E%3C/svg%3E)**
*   Click OK.

This will instantly filter the results and give you 3 names – ABC Ltd., Amazon.com, and Apple Stores.

![Excel Wildcard Characters - Filter A](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20280%20448'%3E%3C/svg%3E)

How does it work? – When you add an asterisk (\*) after A, Excel would filter anything that starts with A. This is because an asterisk (being an Excel wildcard character) can represent any number of characters.

Now with the same methodology, you can use various criteria to filter results.

For example, if you want to filter companies that begin with the alphabet A and contain the alphabet C in it, use the string **A\*C.** This will give you only 2 results – ABC Ltd. and Amazon.com.

If you use **A?C** instead, you will only get ABC Ltd as the result (as only one character is allowed between ‘a’ and ‘c’)

**Note:** The same concept can also be applied when using [Excel Advanced Filters](https://trumpexcel.com/excel-advanced-filter/)
.

### #2 Partial Lookup Using Wildcard Characters & VLOOKUP

Partial look-up is needed when you have to look for a value in a list and there isn’t an exact match.

For example, suppose you have a data set as shown below, and you want to look for the company ABC in a list, but the list has ABC Ltd instead of ABC.

![Excel Wildcard Characters - Partial Lookup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20470%20167'%3E%3C/svg%3E)

You can not use the regular [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 in this case as the lookup value does not have an exact match.

If you use VLOOKUP with an approximate match, it will give you the wrong results.

However, you can use a wildcard character within VLOOKUP function to get the right results:

Enter the following formula in cell D2 and drag it for other cells:

\=VLOOKUP("\*"&C2&"\*",$A$2:$A$8,1,FALSE)

![Excel Wildcard Characters - Vlookup with wildvard characters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20659%20203'%3E%3C/svg%3E)

**How does this formula work?**

In the above formula, instead of using the lookup value as is, it is flanked on both sides with the Excel wildcard character asterisk (\*) – **“\*”&C2&”\*”**

This tells excel that it needs to look for any text that contains the word in C2. It could have any number of characters before or after the text in C2.

Hence, the formula looks for a match, and as soon as it gets a match, it returns that value.

Also read: [Remove Asterisk (\*) in Excel](https://trumpexcel.com/remove-asterisk-excel/)

### 3\. Find and Replace Partial Matches

Excel Wildcard characters are quite versatile.

You can use it in a complex formula as well as in basic functionality such as [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
.

Suppose you have the data as shown below:

![Excel Wildcard Characters - Find and Replace Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20291%20165'%3E%3C/svg%3E)

In the above data, the region has been entered in different ways (such as North-West, North West, NorthWest).

This is often the case with sales data.

To clean this data and make it consistent, we can use Find and Replace with Excel wildcard characters.

Here is how to do this:

*   Select the data where you want to find and replace text.
*   Go to Home –> Find & Select –> Go To. This will open the Find and Replace dialogue box. (_You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     – Control + H_).
*   Enter the following text in the find and replace dialogue box:
    *   Find what: **North\*W\***
    *   Replace with: **North-West ![Excel Wildcard Characters - Find and Replace fields](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20201'%3E%3C/svg%3E)** 
*   Click on Replace All.

This will instantly change all the different formats and make it consistent to North-West.

![Excel Wildcard Characters - North West](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20776%20340'%3E%3C/svg%3E)

**How does this Work?**

In the Find field, we have used **North\*W\*** which will find any text that has the word North and contains the alphabet ‘W’ anywhere after it.

Hence, it covers all the scenarios (NorthWest, North West, and North-West).

Find and Replace finds all these instances and changes it to North-West and makes it consistent.

Also read: [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)

### 4\. Count Non-blank Cells that Contain Text

I know you are smart and you thinking that Excel already has an inbuilt function to do this.

_You’re absolutely right!!_

This can be done using the [COUNTA function](https://trumpexcel.com/excel-functions/counta-function/)
.

BUT… There is one small problem with it.

A lot of times when you import data or use other people’s worksheet, you will notice that there are empty cells while that might not be the case.

These cells look blank but have \=”” in it. The trouble is that the

The trouble is that the COUNTA function does not consider this as an empty cell (it counts it as text).

See the example below:

![Excel Wildcard Characters - COUNTA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20264'%3E%3C/svg%3E)

In the above example, I use the COUNTA function to find cells that are not empty and it returns 11 and not 10 (but you can clearly see only 10 cells have text).

The reason, as I mentioned, is that it doesn’t consider A11 as empty (while it should).

But that is how Excel works.

The fix is to use the Excel wildcard character within the formula.

Below is a formula using the [COUNTIF](https://trumpexcel.com/excel-countif-function/)
 function that only counts cells that have text in it:

\=COUNTIF(A1:A11,"**?\***")

This formula tells excel to count only if the cell has at least one character.

In the **?\*** combo:

*   ? (question mark) ensures that at least one character is present.
*   \* (asterisk) makes room for any number of additional characters.

**Note:** The above formula works when only have text values in the cells. If you have a list that has both text as well as numbers, use the following formula:

\=COUNTA(A1:A11)-[COUNTBLANK](https://trumpexcel.com/excel-countblank-function/)
(A1:A11)

Similarly, you can use wildcards in a lot of other Excel functions, such as [IF()](https://trumpexcel.com/excel-if-function/)
, [SUMIF()](https://trumpexcel.com/excel-sumif-function/)
, [AVERAGEIF()](https://trumpexcel.com/excel-averageif-function/)
, and [MATCH()](https://trumpexcel.com/excel-match-function/)
.

It’s also interesting to note that while you can use the wildcard characters in the [SEARCH function](https://trumpexcel.com/excel-search-function/)
, you can’t use it in [FIND function](https://trumpexcel.com/excel-find-function/)
.

Hope these examples give you a flair of the versatility and power of Excel wildcard characters.

If you have any other innovative way to use it, do share it with me in the comments section.

**You May Find the Following Excel Tutorials Useful:**

*   [Using COUNTIF and COUNTIFS with Multiple Criteria](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    .
*   [Creating a Drop Down List in Excel](https://trumpexcel.com/named-ranges-in-excel/)
    .
*   [Intersect Operator in Excel](https://trumpexcel.com/intersect-operator-in-excel/)
    
*   [Insert Approximate (Almost Equal To) Symbol in Excel](https://trumpexcel.com/excel-insert-symbols/approximate/)
    
*   [SUM Cells Based on Partial Text Match](https://trumpexcel.com/sum-partial-match/)
    
*   [REGEX Functions in Excel](https://trumpexcel.com/excel-functions/regex-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “Excel Wildcard Characters – What are these and How to Best Use it”
----------------------------------------------------------------------------------

1.  I have been using Wildcard Characters since long, however you have given me new dimensions to imagine the use of Wildcard characters
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-14483)
    
2.  Your Initial example using A\*C will give two results is incorrect as it starts with A (ABC ltd.) but does not end with C. You should have used A\*C\*
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-11254)
    
3.  Thank you!!
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-10890)
    
4.  Hi Sumit,  
    Thank you for this wonderful information. I would like to know how to clear cells of notes, formulas, and spaces when using numbers and some letter/number combinations in the same worksheet. The spaces may be before or after the number or letter/number combinations. When I tried to replace the spaces with no space it just put the \* or ? and removed the number. Thanks!!
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-10835)
    
5.  Hi Sumit! Thank you so much for writing such an informative tutorial. I would like to know, how to find a name that ends with “y”. Because when I use “\*y”, Excel displays all the names that have “y” in it.
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-10679)
    
    *   go to text filters, select ‘ends with’
        
        [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-12045)
        
6.  I have the following problem.
    
    1\. Excel document contains 1000 rows with URI patterns in Column A  
    – a. website.com/path1/######  
    – b. website.com/path1/######/path2  
    – c. website.com/path1/######?query  
    – d. website.com/path1/######/path2?query  
    – e. website.com/path1/path2/######  
    – f. website.com/path1/path2/######/path3  
    – g. website.com/path1/path2/######?query  
    – h. website.com/path1/path2/######/path3?query
    
    2\. I must extract the “/#######” pattern (exactly 8 characters) in column B as a single formula.
    
    3\. I tried various wildcard lookups / find / search /array / match with only partial success.
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-10657)
    
    *   How do I wildcard match ONLY numeric values, exclude ALPHABET values, only wildcard of ??????? (7 number string) wild card?
        
        [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-10658)
        
    *   Mate, if all you need for all the 1000 rows is all the time the 1st 8 characters of the cells in column A, then your formula in B1 can be =LEFT(A1,8). This extracts the 1st 8 characters from your original string
        
        [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-12645)
        
7.  Hi Sumit,  
    Really it is a detailed guide on using wildcards with Excel.  
    I have also written a guide on the same topic. Would you please check it out and give your valuable comments?  
    Here is the link of the article: [http://www.exceldemy.com/how-to-use-wildcards-in-excel/](http://www.exceldemy.com/how-to-use-wildcards-in-excel/)
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-8992)
    
8.  Thanks. Very helpful.
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-8562)
    
    *   Thanks for commenting Brett.. Glad you liked it!
        
        [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-8589)
        
9.  Is there a way of using any of these find replace tricks to change a bunch of cells with an increasing value in them, in the format “Text\_1\_OtherText” to “Text\_01\_OtherText” without changing “Text\_10\_OtherText” to “Text\_010\_OtherText” ?
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-3909)
    
10.  Interesting! I read it through.
    
    [Reply](https://trumpexcel.com/excel-wildcard-characters/#comment-3833)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-wildcard-characters/#respond)

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