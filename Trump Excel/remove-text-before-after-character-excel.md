# How To Remove Text Before Or After a Specific Character In Excel

**Source:** https://trumpexcel.com/remove-text-before-after-character-excel

---

[Skip to content](https://trumpexcel.com/remove-text-before-after-character-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-text-before-after-character-excel/#below-title)

When working with text data in Excel, you may have the need to remove the text before or after a specific character or text string.

For example, if you have the name and designation data of people, you may want to remove the designation after the comma and only keep the name (or vice-versa where you keep the designation and remove the name).

![Dataset where text after comma has been removed](https://trumpexcel.com/wp-content/uploads/2020/08/Dataset-where-text-after-comma-has-been-removed.png)

Sometimes, it can be done with a simple formula or a quick Find and Replace, and sometimes, it needs more complex formulas or workarounds.

In this tutorial, I will show you how to remove the text before or after a specific character in Excel (using different examples).

So let’s get started with some simple examples.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-text-before-after-character-excel/#)

Remove Text After a Character Using Find and Replace
----------------------------------------------------

If you want to quickly remove all the text after a specific text string (or before a text string), you can do that using Find and Replace and wild card characters.

Suppose you have a dataset as shown below and you want to remove the designation after the comma character and keep the text before the comma.

![Dataset from which need to remve text after a specific character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20367'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Copy and Paste the data from column A to column  B (this is to keep the original data as well)![Copy and paste data from column A to Col B](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20408'%3E%3C/svg%3E)
2.  With the cells in Column B selected, click on the Home tab![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20325%20199'%3E%3C/svg%3E)
3.  In the Editing group, click on the Find & Select option
4.  In the options that appear in the drop-down, click on the Replace option. This will open the Find and Replace dialog box![Click on the Replace option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20375%20550'%3E%3C/svg%3E)
5.  In the ‘Find what’ field, enter **,\*** (i.e., comma followed by an asterisk sign)![Enter comma and asterisk in the find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)
6.  Leave the ‘Replace with’ field empty![Leave Replace With blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)
7.  Click on the Replace All button![Click on Replace All](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)

The above steps would find the comma in the data set and remove all the text after the comma (including the comma).

![Dataset where text after comma has been removed](https://trumpexcel.com/wp-content/uploads/2020/08/Dataset-where-text-after-comma-has-been-removed.png)

Since this replaces the text from the selected cells, it’s a good idea to copy the text into another column and then perform this find and replace operation, or create a backup copy of your data so that you have the original data intact

**How does this work?**

\* (asterisk sign) is a [wildcard character](https://trumpexcel.com/excel-wildcard-characters/)
 that can represent any number of characters.

When I use it after the comma (in the ‘Find what’ field) and then click on Replace All button, it finds the first comma in the cell and considers it a match.

This is because the asterisk (\*) sign is considered a match to the entire text string that follows the comma.

So when you hit the replace all button, it replaces the comma and all the text that follows.

**Note**: This method works well then you only have one comma in each cell (as in our example). In case you have multiple commas, this method would always find the first comma and then remove everything after it. So you cannot use this method if you want to replace all the text after the second comma and keep the first one as is.

In case you want to remove all the characters before the comma, change the find what field entry by having the asterisk sign before the comma (\*, instead of ,\*)

Remove Text Using Formulas
--------------------------

If you need more control over how to find and replace text before or after a specific character, it’s better to use the inbuilt text formulas in Excel.

Suppose you have the below data set Where you want to remove all the text after the comma.

![Dataset from which need to remve text after a specific character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20367'%3E%3C/svg%3E)

Below is the formula to do this:

\=LEFT(A2,FIND(",",A2)-1)

![Formula to remove comma after the comma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20589%20418'%3E%3C/svg%3E)

The above formula uses the [FIND function](https://trumpexcel.com/excel-find-function/)
 to find the position of the comma in the cell.

This position number is then used by the LEFT function to extract all the characters before the comma. Since I don’t want comma as a part of the result, I have subtracted 1 from the Find formula’s resulting value.

This was a simple scenario.

Let’s take a slightly complex one.

Suppose I have this below data set where I want to remove all the text after the second comma.

![Dataset with two commas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20718%20423'%3E%3C/svg%3E)

Here is the formula that will do this:

\=LEFT(A2,FIND("!",SUBSTITUTE(A2,",","!",2))-1)

![Formula to remove text after the second comma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20717%20473'%3E%3C/svg%3E)

Since this data set has multiple commas, I cannot use the FIND function to get the position of the first comma and extract everything to the left of it.

I need to somehow find out the position of the second comma and then extract everything which is to the left of the second comma.

To do this, I have used the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
 to change the second comma to an exclamation mark. Now this gives me a unique character in the cell. I can now use the position of the exclamation mark to extract everything to the left of the second comma.

This position of the exclamation mark is used in the [LEFT function](https://trumpexcel.com/excel-left-function/)
 to extract everything before the second comma.

So far so good!

But what if there is an inconsistent number of commas in the data set.

For example, in the below data set some cells have two commas and some cells have three commas, and I need to extract all the text before the last comma.

![Dataset with multiple commas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20683%20398'%3E%3C/svg%3E)

In this case, I need to somehow figure out the [position of the last occurrence](https://trumpexcel.com/find-characters-last-position/)
 of the comma and then extract everything to the left of it.

Below is the formula that will do that

\=LEFT(A2,FIND("!",SUBSTITUTE(A2,",","!",LEN(A2)-LEN(SUBSTITUTE(A2,",",""))))-1)

![Formula to remove text after the last occurrence of the comma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20686%20471'%3E%3C/svg%3E)

The above formula uses the [LEN function](https://trumpexcel.com/excel-len-function/)
 to find the overall length of the text in the cell as well as the length of the text without the comma.

When I subtract these two values, it gives me the total number of commas in the cell.

So, it would give me 3 for cell A2 and 2 for cell A4.

This value is then used within the SUBSTITUTE formula to replace the last comma with an exclamation mark. And then you can use the left function extract everything which is to the left of the exclamation mark (which is where the last comma used to be)

As you can see in the examples, using a combination of text formulas allows you to handle many different situations.

Also, since the result is linked with the original data, when you change the original data the result would automatically update.

Remove Text Using Flash Fill
----------------------------

[Flash Fill](https://trumpexcel.com/flash-fill-excel/)
 is a tool that was introduced in Excel 2013 and is available in all the versions after that.

It works by identifying patterns when you manually enter the data and then extrapolated to give you the data for the entire column.

So if you want to remove the text before or after a specific character, you just need to show flash fairy what the result would look like (by entering it manually a couple of times ), and flash fill would automatically understand the pattern and give you the results.

Let me show you this with an example.

Below I have the data set where I want to remove all the text after the comma.

![Dataset from which need to remve text after a specific character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20367'%3E%3C/svg%3E)

Here are the steps to do this using Flash Fill:

1.  In cell B2, which is the adjacent column of our data, manually enter ‘Jeffery Haggins’ (which is the expected result)![Enter expected result in the first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20673%20400'%3E%3C/svg%3E)
2.  In cell B3, enter ‘Tim Scott’ (which is the expected result for the second cell)![Enter expected result in the second cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20673%20395'%3E%3C/svg%3E)
3.  Select the range B2:B10![Select the entire range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20396'%3E%3C/svg%3E)
4.  Click the Home tab
5.  In the Editing group, click on the Fill drop-down option
6.  Click on Flash Fill![Click on Flash Fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20401%20372'%3E%3C/svg%3E)

The above steps would give you the result as shown below:

![Flash Fill result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20397'%3E%3C/svg%3E)

You can also use the Flash Fill [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 **Control + E** after selecting the cells in the result column (Column B in our example)

Flash Fill is a wonderful tool and in most cases, it is able to recognize the pattern and give you the right result. but in some cases, it may not be able to recognize the pattern correctly and can give you the wrong results.

So make sure you double-check your Flash Fill results

And just like we have removed all the text after a specific character using flash fill, you can use the same steps to remove the text before a specific character. just show flash fill how the result should look like my Internet manually in the adjacent column, and it would do the rest.

Remove Text Using VBA (Custom Function)
---------------------------------------

The whole concept of removing the text before or after a specific character Is dependent on finding the position of that character.

As if seen above, finding the last occurrence of that character good means using a concoction of formulas.

If this is something you need to do quite often, you can simplify this process by [creating a custom function using VBA](https://trumpexcel.com/user-defined-function-vba/)
 (called User Defined Functions).

Once created, you can re-use this function again and again. It’s also a lot simpler and easier to use (as most of the heavy lifting is done by the VBA code in the back end).

Below the VBA code that you can use to create the custom function in Excel:

Function LastPosition(rCell As Range, rChar As String)
'This function gives the last position of the specified character
'This code has been developed by Sumit Bansal (https://trumpexcel.com)
Dim rLen As Integer
rLen = Len(rCell)

For i = rLen To 1 Step -1

If Mid(rCell, i - 1, 1) = rChar Then
LastPosition = i - 1
Exit Function
End If

Next i

End Function

You need to place the VBA code in a regular module in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
, or in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. Once you have it there, you can use it as any other regular worksheet function in the workbook.

This function takes 2 arguments:

1.  The [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     for which you want to find the last occurrence of a specific character or text string
2.  The character or text string whose position you need to find

Suppose you now have the below data set and you want to remove all the text after the last comma and only have the text before the last comma.

Below is the formula that will do that:

\=LEFT(A2,LastPosition(A2,",")-1)

![VBA Custom function to remove text after a specific character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20393'%3E%3C/svg%3E)

In the above formula, I have specified to find the position of the last comma. In case you want to find the position of some other character or text string, you should use that as the second argument in the function.

As you can see this is a lot shorter and easier to use, as compared to the long text formula that we used the previous section

If you put the VBA code in a module in a workbook you would only be able to use this custom function in that specific workbook. If you want to use this in all the workbooks on your system, you need to copy and paste this code in the Personal Macro Workbook.

So these are some of the mails you can use to quickly remove the text before or after a specific character in Excel.

If it’s a simple one-time thing, then you can do that using find and replace. what if it is a little more complex, then you need to use a combination of inbuilt Excel formulas, or even create your own custom formula using VBA.

I hope you found this tutorial useful.

**Other Excel tutorials that you may like:**

*   [Count Characters in a Cell (or Range of Cells) Using Formulas in Excel](https://trumpexcel.com/count-characters-in-excel/)
    
*   [How to Remove the First Character from a String in Excel](https://trumpexcel.com/remove-first-character-from-string/)
    
*   [How to Compare Text in Excel](https://trumpexcel.com/compare-text-excel/)
    
*   [How to Remove Dashes (-) in Excel?](https://trumpexcel.com/remove-dashes-excel/)
    
*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [Remove Characters From Left in Excel (Easy Formulas)](https://trumpexcel.com/remove-characters-from-left-excel/)
    
*   [Remove Last Character in Excel](https://trumpexcel.com/remove-last-character/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-text-before-after-character-excel/#respond)

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