# Lookup the Second, the Third, or the Nth Value in Excel

**Source:** https://trumpexcel.com/lookup-second-value

---

[Skip to content](https://trumpexcel.com/lookup-second-value/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/lookup-second-value/#below-title)

**Watch Video – Lookup the Second, the Third or the Nth Matching Value**

When it comes to looking up data in Excel, there are two amazing functions that I often use – [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 and [INDEX](https://trumpexcel.com/excel-index-function/)
 (mostly in conjunction with the [MATCH](https://trumpexcel.com/excel-match-function/)
 function).

However, these formulas are designed to find only the first instance of the lookup value.

But what if you want to look-up the second, third, fourth or the Nth value.

Well, it’s doable with a little bit of extra work.

In this tutorial, I will show you various ways (with examples) on how to look up the second or the Nth value in Excel.

Lookup the Second, Third, or Nth Value in Excel
-----------------------------------------------

In this tutorial, I will cover two ways to look-up the second or the Nth value in Excel:

*   Using a helper column.
*   Using array formulas.

Let’s get started and dive right in.

### Using Helper Column

Suppose you are a training coordinator in an organization and have a dataset as shown below. You want to list all the training in front of an employee’s name.

![Training Data set to Lookup the second or nth value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20749%20345'%3E%3C/svg%3E)

In the above dataset, the employees have been given training on different Microsoft Office tools (Excel, PowerPoint, and Word).

Now, you can use the VLOOKUP function or the INDEX/MATCH combo to find the training an employee has completed. However, it will only return the first matching instance.

For example, in the case of John, he has taken all the three training, but when I look up his name with VLOOKUP or INDEX/MATCH, it will always return ‘Excel’, which is the first training for his name in the list.

To get this done, we can use a helper column and create unique lookup values in it.

Here are the steps:

*   Insert a column before the column that lists the training.![Helper column inserted in the dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20351'%3E%3C/svg%3E)
*   In cell B2, enter the following formula:
    
    \=A2&COUNTIF($A$2:$A2,A2)
    

![formula in helper column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20346'%3E%3C/svg%3E)

*   In cell F2, enter the following formula and copy-paste for all the other cells:
    
    \=IFNA(VLOOKUP($E2&COLUMNS($F$1:F1),$B$2:$C$14,2,0),"")
    

![Formula to lookup the second third and nth value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20816%20397'%3E%3C/svg%3E)

The above [formula](https://trumpexcel.com/excel-functions/)
 would return the training for each employee in the order it appears on the list. In case there are no training listed for an employee, it returns a blank.

**How does this formula work?**

The [COUNTIF formula](https://trumpexcel.com/excel-countif-function/)
 in the helper column makes each employee’s name unique by adding a number to it. For example, the first instance of John becomes John1, the second instance becomes John2 and so on.

The VLOOKUP formula now uses these unique employee names to find the matching training.

Note that $E2&COLUMNS($F$1:F1) is the lookup value in the formula. This would add a number to the employee name based on the column number. For example, when this formula is used in cell F2, the lookup value becomes “John1”. In cell G2, it becomes “John2” and so on.

### Using  Array Formula

If you don’t want to alter the original dataset by adding helper columns, you can also use an array formula to look up the second, third, or the nth value.

Suppose you have the same dataset as shown below:

![Training Data set to Lookup the second or nth value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20749%20345'%3E%3C/svg%3E)

Here is the formula that will return the correct lookup value:

\=IFERROR(INDEX($B$2:$B$14,SMALL(IF($A$2:$A$14=$D2,ROW($A$2:$A$14)-1,""),COLUMNS($E$1:E1))),"")

Copy this formula and paste it in cell E2.

Note that this is an array formula and you need to use Control + Shift + Enter (hold the Control and Shift keys and press the Enter key), instead of hitting just the Enter key.

**[Click here to download the example file](https://trumpexcel.com/wp-content/uploads/2017/07/Lookup-Nth-Value-in-Excel.xlsx)
**.

**How does this formula work?**

Let’s break this formula into parts and see how it works.

$A$2:$A$14=$D2

The above part of the formula compares each cell in A2:A14 with the value in D2. In this dataset, it checks whether a cell contains the name “John” or not.

It returns an array of TRUE of FALSE. If the cell has the name ‘John’ it would be True, else it would be False.

Below is the array you would get in this example:

{TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}

Note that it has TRUE in 1st, 7th and 111th position, as there is where the name John appears in the dataset.

IF($A$2:$A$14=$D2,ROW($A$2:$A$14)-1,””)

The above [IF formula](https://trumpexcel.com/excel-if-function/)
 uses the array of TRUE and FALSE, and replaces TRUE with the position of its occurrence in the list (given by ROW($A$2:$A$14)-1) and FALSE with “” (blanks). The following is the resulting array you get with this IF formula:

{1;””;””;””;””;””;7;””;””;””;11;””;””}

Note than 1, 7, and 11 are the position of occurence of John in the list.

SMALL(IF($A$2:$A$14=$D2,ROW($A$2:$A$14)-1,””),COLUMNS($E$1:E1))

The [SMALL function](https://trumpexcel.com/excel-small-function/)
 now picks the first smallest, second smallest, third smallest number from this array. Note that it uses the [COLUMNS function](https://trumpexcel.com/excel-columns-function/)
 to generate the column number. In cell E2, the COLUMNS function returns 1 and the SMALL function returns 1. In cell F2, COLUMNS function returns 2 and the SMALL function returns 7.

INDEX($B$2:$B$14,SMALL(IF($A$2:$A$14=$D2,ROW($A$2:$A$14)-1,””),COLUMNS($E$1:E1)))

INDEX function now returns the value from the list in Column B based on the position returned by the SMALL function. Hence, in cell E2, it returns ‘Excel’, which is the first item in B2:B14. In cell F2, it returns PowerPoint, which is the 7th item in the list.

Since there are cases where there are only one or two training for some employees, INDEX function would return an error. The [IFERROR function](https://trumpexcel.com/excel-iferror-function/)
 is used to return a blank in place of the error.

Note that in this examples, I have used range references. However, in practical examples, it’s beneficial to convert he data into an [Excel Table](https://trumpexcel.com/excel-table/)
. By converting into an Excel Table, you can use structured references, which makes it easier to create formulas. Also, an Excel Table can automatically account for any new training items that are added to the list (so you don’t have to adjust the formulas every time).

What do you do when you have to look-up the second, third, or the Nth value? I am sure there are more ways to do this. If you use something easier than the one listed here, do share with us all in the comments section.

**[Click here to download the example file](https://trumpexcel.com/wp-content/uploads/2017/07/Lookup-Nth-Value-in-Excel.xlsx)
**.

**You May Also Like the Following Excel Tutorials:**

*   [VLOOKUP vs INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    .
*   [INDEX MATCH Combo in Excel (examples)](https://trumpexcel.com/index-match/)
    
*   [How to make VLOOKUP Case Sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    .
*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    .
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    
*   [Find the Second Highest Value in Excel](https://trumpexcel.com/find-second-largest-value-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “Lookup the Second, the Third, or the Nth Value in Excel”
------------------------------------------------------------------------

1.  How can i make this?  
    Name Training  
    John Excel  
    John PowerPoint  
    John Word  
    Stan Excel  
    Barb Excel  
    Barb Word  
    Scott PowerPoint  
    Scott Excel  
    Jill Word  
    Jill Excel  
    etc…
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-14692)
    
2.  This is great for finding the nth value across columns – how do we achieve the same dynamic lookup result within one single column in descending rows using the array formula?
    
    Using your example, results are displayed in E column only. D10 contains “John” so E10 returns “PowerPoint” (as D2/E2 had the first entry of John/Excel). D11 contains “Jill” so E11 returns “Excel”, and so on.
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-14343)
    
3.  Hello  
    Is there anyone who could help me run through this, im wanting to use this but im after a little help please
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-14279)
    
4.  Thanks for helping me crack the final piece of my puzzle, I needed to find the row of the 2nd match, of a nine criteria countifs formula. See below the composition of a two criteria test to find the row of the 2nd match: {=SMALL(IF(COUNTIFS(Enq\_Model,Sec\_Tbl\[Model\],Enq\_Date,Sec\_Tbl\[Date\])=1,ROW(Sec\_Tbl)-1,””),2)}
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-13944)
    
5.  Thank you so much.. this is really a great help for me because i can now update my subsisiary ledger without entering manually sa data.. thank you again.. you really are a big help…
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-13457)
    
6.  Thank you very much for sharing the formula. The example and explanations are excellent. It helped me to lookup 2nd and 3rd values so easily.
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-12672)
    
7.  Hi Sumit,
    
    Thank you for sharing the formula. I am trying to use the formula, for some set of stores with different product. They are all set up vertically, the formula works for the first set of stores but doesn’t work when the store# changes. I have tried all the ways, but it doesn’t work. Can you please help?
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-12137)
    
8.  Thank You very much for sending E-book.
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-12117)
    
9.  This is excellent – exactly what I needed. I have a drop down list and want to populate a range of cells on another sheet based on the single value selected. Thank you!
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-11580)
    
10.  This is what I have been looking for. I have a list of exercise movements.  
    I can Substitute Names with Routine Names and Training 1,2,3 etc. for routine moves 1,2,3 etc. What I need to do further is list the routine names with an ordered vertical list of routine movements associated with each routine name.  
    Ex: E2 – Routine 1 – F2 – Movement 1  
    E3 – Routine 1 – F3 – Movement 2  
    E4 – Routine 1 – F4 – Movement 3  
    E5 – Routine 2 – F5 – Movement 1  
    E6 – Routine 2 – F6 – Movement 2  
    E7 – Routine 3 – F7 – Movement 1  
    etc, etc.  
    Would it be possible to add another table with this kind of formatting?  
    Appreciate all your help,  
    Bob D.
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-10660)
    
11.  Thanks a bunch, very helpful
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-10617)
    
12.  Thanks! This is excellent, but I find it difficult to quickly use this site as a reference point to grab the formula. Here is the conversion I use:
    
    \=IFERROR(INDEX(ReturnValueColumn, SMALL(IF(LookupValueColumn=LookupValue, ROW(LookupValueColumn),””),NthNumber)),””)
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-10461)
    
13.  Any idea how the opposite is done?
    
    john = excel powerpoint word  
    \==>
    
    john excel  
    john powerpoint  
    john word
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-10404)
    
14.  Can anyone help me with that? VBA or excel function? [https://uploads.disquscdn.com/images/0463ad0ceef8a8b702c34d77738308ff151f4218acdf894c9eaff11d6eeaabc0.jpg](https://uploads.disquscdn.com/images/0463ad0ceef8a8b702c34d77738308ff151f4218acdf894c9eaff11d6eeaabc0.jpg)
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-9924)
    
15.  Thank you very much Sumit for these great examples, the second formula is amazing. I am impressed that it can be achieved with the clever combination of functions. I have some questions:  
    1) What’s the difference between IFNA and IFERROR?  
    2) Why is -1 substracted to this formula ROW($A$2:$A$14)-1?  
    3) Is the array formula convenient to use when the original data has many rows, let’s say 10000 rows?
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-9716)
    
16.  This is quite clever, thanks for the examples.  
    I am not very fond of array functions so when I have faced something similar to the situation above I have used INDEX with two MATCH formulas looking for two figures. In your example it would mean using the actual training names in the x axxis of the table instead of Training 1, 2, etc… Would work if list of trainings is limited.
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-9545)
    
17.  I think a simple pivot table will do all this.
    
    [Reply](https://trumpexcel.com/lookup-second-value/#comment-9540)
    
    *   Pivot table can tell us if a person did a training or not. I don’t think it can answer what was the second training a person did or the third training he/she did.
        
        [Reply](https://trumpexcel.com/lookup-second-value/#comment-9541)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/lookup-second-value/#respond)

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