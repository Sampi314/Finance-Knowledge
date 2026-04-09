# Count Characters in a Cell (or Range of Cells) Using Formulas in Excel

**Source:** https://trumpexcel.com/count-characters-in-excel

---

[Skip to content](https://trumpexcel.com/count-characters-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-characters-in-excel/#below-title)

Excel has some amazing text functions that can help you when working with the text data.

In some cases, you may need to calculate the total number of characters in a cell/range or the number of times a specific character occurs in a cell.

While there is the [LEN function](https://trumpexcel.com/excel-len-function/)
 that can count the number of characters in a cell, you can do the rest as well with a combination of formulas (as we will see later in the examples).

In this tutorial, I will cover different examples where you can count total or specific characters in a cell/range in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-characters-in-excel/#)

Count All Characters in a Cell
------------------------------

If you simply want to get a total count of all the characters in a cell, you can use the LEN function.

The LEN function takes one argument, which could be the text in double-quotes or the cell reference to a cell that has the text.

For example, suppose you have the dataset as shown below and you want to count the total number of characters in each cell:

![Data in which characters need to be counted in each cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20250'%3E%3C/svg%3E)

Below is the formula that will do this:

\=LEN(A2)

![LEN formula to count total number of characters in cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20305'%3E%3C/svg%3E)

By itself, the LEN function may not look like much, but when you combine it with other formulas, it can do some wonderful things (such as get the word count in a cell or [split first and last name)](https://trumpexcel.com/split-cells-in-excel/)
.

Note: LEN function will count all the characters in a cell, be it a special character, numbers, punctuation marks, and space characters (leading, trailing, and double spaces between words).

Since the LEN function counts every character in a cell, sometimes you may get the wrong result in case you have extra spaces in the cell.

For example, in the below case, the LEN function returns 25 for the text in cell A1, while it should have been 22. But since it’s counting extra space characters as well, you get the wrong result.

![Character count with spaces](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20302'%3E%3C/svg%3E)

To avoid extra spaces being counted, you can first use the TRIM function to [remove any leading, trailing and double spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 and then use the LEN function on it to get the real word count.

Below formula will do this:

\=LEN(TRIM(A2))

![Using TRIM and LEN to not count extra space characters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20303'%3E%3C/svg%3E)

Also read: [COUNTIF Less Than in Excel](https://trumpexcel.com/countif-less-than/)

Count All Characters in a Range of Cells
----------------------------------------

You can also use the LEN function to count the total number of characters in an entire range.

For example, suppose we have the same dataset and this time, instead of getting the number of characters in each cell, I want to know how many are there in the entire range.

You can do that using the below formula:

\=SUMPRODUCT(LEN(A2:A7)))

![Formula to Count all characters in a range of cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20302'%3E%3C/svg%3E)

Let me explain how this formula works.

In the above formula, the LEN part of the function takes an entire range of cells and counts the characters in each cell.

The result of the LEN function would be:

{22;21;23;23;23;31}

Each of these numbers represents the character count in the cell.

And when you use the [SUMPRODUCT function](https://trumpexcel.com/excel-sumproduct-function/)
 with it, it would simply add all these numbers.

Now, if you’re wondering why can’t you use SUM instead of SUMPRODUCT, the reason is that this is an array, and SUMPRODUCT can handle array but the SUM function can not.

However, if you still want to use SUM, you can use the below formula (but remember that you need to use the Control + Shift + Enter to get the result instead of a regular Enter)

\=SUM(LEN(A2:A7))

Count Specific Characters in a Cell
-----------------------------------

As I mentioned that the real utility of the LEN function is when it’ used in combination with other formulas.

And if you want to count specific characters in a cell (it could be a letter, number, special character, or space character), you can do that with a formula combination.

For example, suppose you have the dataset as shown below and you want to [count the total number of words](https://trumpexcel.com/word-count-in-excel/)
 in each cell.

While there is no in-built formula to get the word count, you can count the space characters and then use it to know the total number of words in the cell.

Below is the formula that will give you the total number of space characters in a cell:

\=LEN(A2)-LEN(SUBSTITUTE(A2," ",""))+1

![Getting the word count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20305'%3E%3C/svg%3E)

The above formula counts the total number of space characters and then adds 1 to that number to get the word count.

Here is how this formula works:

*   [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
     is used to replace all the space characters with a blank. The LEN function is then used to count the total number of characters when there are no space characters.
*   The result of the LEN(SUBSTITUTE(A2,” “,””)) is then subtracted from LEN(A2). This gives us the total number of space characters that are there in the cell.
*   1 is added in the formula and the total number of words would be one more than the total number of space characters (as two words are separated with one character).

Note that in case there are any leading, trailing, or double spaces, you are going to get the wrong result. In such a case, it’s best to use the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 along with the LEN function.

You can also use the same logic to find a specific character or word or phrase in a cell.

For example, suppose I have a dataset as shown below where I have different batches, where each batch has an alphabet and number to represent it (such as A1, J2, etc.)

![Data where specific character needs to be counted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20250'%3E%3C/svg%3E)

Below is the formula that will give you the total number of times a batch with the alphabet A has been created each month:

\=LEN(B2)-LEN(SUBSTITUTE(B2,"A",""))

![formula to count specific characters in a string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20307'%3E%3C/svg%3E)

The above formula again uses the same logic – find the length of the text in a cell with and without the character that you want to count and then take the difference of these two.

In the above formula, I have hardcoded the character that I want to count, but you can also put it in a cell and then use the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
. This makes it more convenient as the formula would update the next time you change the text in the cell.

### Count Specific Characters Using Case-Insensitive Formula

There is one issue with the formula used to count specific characters in a cell.

The SUBSTITUTE function is case sensitive. This means that you “A” is not equal to “a”. This is why you get the wrong result in cell C5 (the result should have been 3).

![Case sensitive character count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20251'%3E%3C/svg%3E)

So how can you get the character count of a specific character when it could have been in any case (lower or upper).

You do that by making your formula case insensitive. While you can go for a complex formula, I simply added the character count of both the cases (lowercase and uppercase A).

\=LEN(B2)-LEN(SUBSTITUTE(B2,"A",""))+LEN(B2)-LEN(SUBSTITUTE(B2,"a",""))

![Formula to count lower and upper case characters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20330'%3E%3C/svg%3E)

Count Characters/Digits Before and After Decimal
------------------------------------------------

I don’t know why, but this is a common query I get from my readers and have seen in many forums – [such as this one](https://www.pcreview.co.uk/threads/count-digits-before-decimals-and-after-decimals.4012698/)

Suppose you have a dataset as shown below and you want to count the characters before the decimal and after the decimal.

![Count characters before and after decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20168'%3E%3C/svg%3E)

Below are the formulas that will do this.

Count characters/numbers before the decimal:

\=LEN(INT(A2))

Count characters/numbers after the decimal:

\=LEN(A2)-FIND(".",A2)

![Formula to count characters before and after decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20495%20227'%3E%3C/svg%3E)

Note that these formulas are meant only for significant digits in the cell. In case you have leading or trailing zeroes or you have used [custom number formatting](https://trumpexcel.com/excel-custom-number-formatting/)
 to show more/fewer numbers, the above formulas would still give you significant digits before and after the decimal.

So these are some of the scenarios where you can use formulas to count characters in a cell or a range of cells in Excel.

I hope you found the tutorial useful!

**Other Excel tutorials you may like:**

*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    
*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [How to Count Colored Cells In Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    
*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-characters-in-excel/#respond)

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