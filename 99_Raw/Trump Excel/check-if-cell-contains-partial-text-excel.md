# Check IF Cell Contains Partial Text in Excel (Formulas)

**Source:** https://trumpexcel.com/check-if-cell-contains-partial-text-excel

---

[Skip to content](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/#below-title)

Sometimes, in my work, I have to check if a cell or a range of cells contains the partial text I’m looking for.

For example, suppose I want to check whether a cell contains the text string “ABC” or not. The cell may have additional strings or characters, but as long as it has the string I’m looking for (which is “ABC”), it fulfills my criteria.

In this article, I will show you a couple of methods to check if a cell contains partial text or not using some simple formulas. I will also show you how to highlight cells that contain the partial text string.

_[**Click here to Download the Example File**](https://www.dropbox.com/scl/fi/al4gn5ucg6ls789edoufe/Check-IF-Cell-Contains-Partial-Text-in-Excel.xlsx?rlkey=jyc1d6nabcgcvhgfed9ch5kxm&dl=1)
_

This Tutorial Covers:

[Toggle](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/#)

Check If a Cell contains Partial Text Match Anywhere
----------------------------------------------------

Below, I have a data set where I have product IDs in column A, and I want to check whether the product ID contains the string “ABK” or not.

![Check IF Cell Contains Partial Text in Excel Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20421'%3E%3C/svg%3E)

If it contains that string, I want to return ‘Yes’ in the adjacent cell in column B, and if it does not contain the string, I want it to return ‘No’.

Here is the formula that will do this for me:

\=IF(ISNUMBER(SEARCH("ABK",A2)),"Yes","No")

Enter this formula in cell B2 and then copy it for all the cells in the column to get the result for all the product IDs in column A.

![Check If a Cell contains Partial Text Match Anywhere formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20761%20477'%3E%3C/svg%3E)

Now, let me explain how this formula works.

The [SEARCH function](https://trumpexcel.com/excel-search-function/)
 of the formula (_SEARCH(“ABK”,A2)_) looks for the string ‘ABK’ in cell A2, and if it finds it, it returns the numeric value of the starting position where it found that string.

In our formula (in cell B2), this part of the formula returns 1 as it finds the string at the beginning of the product ID. In case it’s not able to find the string, it will return a [#VALUE! error](https://trumpexcel.com/fix-value-error-in-excel/)
.

_ISNUMBER(SEARCH(“ABK”,A2))_ – this part of the formula returns TRUE in case the result of the SEARCH function is a numeric value, else, it returns a FALSE.

[IF function](https://trumpexcel.com/excel-if-function/)
 is then used to give us “Yes” if the [ISNUMBER formula](https://trumpexcel.com/excel-is-function/)
 returns TRUE, and “No”, if the ISNUMBER formula returns FALSE.

Note: The SEARCH function is not case-sensitive. So, it would consider ‘ABK’ and ‘abk’ as the same string. In case you want to do a case-sensitive lookup, you can use the [FIND functio](https://trumpexcel.com/excel-find-function/)
n instead of SEARCH.

Also read: [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)

Check Cell for Partial Text Match at the Beginning of the Text
--------------------------------------------------------------

In the above example, I wanted to check whether the string I’m looking for is present anywhere in the cell.

But what if I want to check the presence of the string at the beginning of each cell?

This can be done using [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
 within the formula.

Below, I have a data set where I have product IDs in column A, and I want to check whether the product ID starts with the string “ABK” or not.

![Dataset to check partial text in cell at the beginning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20421'%3E%3C/svg%3E)

Below is the formula that I can use to do this:

\=IF(COUNTIF(A2,"ABK\*"),"Yes","No")

Enter this formula in cell B2 and copy it for all the cells in the column.

![Dataset to check partial text in cell at the beginning formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20678%20475'%3E%3C/svg%3E)

Now, let’s understand how this formula works.

The above formula uses the following [COUNTIF formula](https://trumpexcel.com/excel-countif-function/)
 (COUNTIF(A2,”ABK\*”), where it is looking for the string ‘ABK\*’ in cell A2.

Asterisk (\*) is a wild card character in Excel that represents any number of characters. So when I use ABK\*, I’m looking for any string that starts with ABK and can have any number of characters after it.

The COUNTIF Function returns 1 if it finds that the content in the cell starts with ABK, and 0 if it doesn’t.

The IF function then gives us “Yes” if the result of the COUNTIF function is 1; it returns a “No”

Note: In case there are any leading spaces in the cells in column A, this function will give you incorrect results. If that’s the case, either you first [remove these leading spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
, or you use TRIM(A2) instead of A2 in the formula.

Also read: [How to Compare Text in Excel](https://trumpexcel.com/compare-text-excel/)

Check Cell for Partial Text Match at the End of the Text
--------------------------------------------------------

If you want to check for the presence of the lookup string at the end of the text in the cell, you can modify the formula with wildcard characters to do that easily.

Below, I have a data set where I have product IDs in column A, and I want to check if the product ID ends with the string “US “or not.

![Dataset to check if cell contain partial text at end](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20422'%3E%3C/svg%3E)

Here is the formula that will do this for me:

\=IF(COUNTIF(A2,"\*US"),"Yes","No")

Enter this formula in cell B2 and copy it for all the cells in the column.

![Dataset to check if cell contain partial text at end formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20469'%3E%3C/svg%3E)

In the above formula, I have used \*US as the criteria in COUNTIF.

This would make the COUNTIF function check the content of the cell and return 1 only if it finds the string “US” at the end of the cell.

Using an asterisk (\*) before the string ‘US’ means that the cell can contain any text string, but as long as it ends with “US”, the COUNTIF formula would return 1.

And if it doesn’t end with the string ‘US’, the COUNTIF formula would return 0.

The IF function then gives us “Yes” if the result of the COUNTIF function is 1; else, it gives us a “No”

Also read: [Find the Closest Match in Excel (using Formulas)](https://trumpexcel.com/find-closest-match-in-excel/)

Check for Partial Match with AND Condition
------------------------------------------

You can also combine and check for the presence of two partial strings within a cell using an AND condition.

Below, I have the product IDs in column A, and I want to check if the ID in the cell starts with “ABK” and ends with “US” or not.

![Dataset to check if cell contain partial text AND condition](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20396%20422'%3E%3C/svg%3E)

So, I need to simultaneously check for two partial matches in the same cell for this condition to be fulfilled.

This can easily be done using an AND function with COUNTIF and wildcard characters (as shown below).

\=IF(AND(COUNTIF(A2,"ABK\*"),COUNTIF(A2,"\*US")),"Yes","No")

Enter this formula in cell B-2 and then [apply it to all the other cells in the column](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
.

![Dataset to check if cell contain partial text AND condition formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20494'%3E%3C/svg%3E)

Now, let me explain how this formula works.

I have used an AND function that checks the result of two separate formulas:

*   COUNTIF(A2,”ABK\*”) – This returns 1 if the content of the cell starts with the string “ABK”, else, it returns 0
*   COUNTIF(A2,”\*US”) – This returns 1 if the content of the cell ends with the string “US”, else, it returns 0

The AND function would only return a TRUE when both the COUNTIF functions return a 1 (which means that the string starts ‘ABK’ with and ends with ‘US’). Otherwise, it would give us a FALSE.

And if AND gives us TRUE, the IF function returns the value “Yes” in the cell, else it returns a “No”

Also read: [Lookup the Second, the Third, or the Nth Value in Excel](https://trumpexcel.com/lookup-second-value/)

Check for Partial Match with OR Condition
-----------------------------------------

Just like the AND condition shown above, you can also check with an OR condition.

Below, I have some product ID data set in column A, and I want to check if a cell starts with the string ‘ABK’ or it ends with ‘US’. If any or both of these two conditions are met, I want to get ‘Yes’ in the adjacent cell.

![Check for Partial Match with OR Condition dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20420'%3E%3C/svg%3E)

Here is the formula that will do this:

\=IF(OR(COUNTIF(A2,"ABK\*"),COUNTIF(A2,"\*US")),"Yes","No")

![Check for Partial Match with OR Condition formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20492'%3E%3C/svg%3E)

This above formula checks if the value in cell A2 starts with “ABK” or ends with “US”. If either of the conditions is True, it returns “Yes”; otherwise, it returns “No”.

Below is a step-by-step breakdown of the formula:

*   _\=IF(…)_: The IF Function checks a condition and returns “Yes” if the condition is true, and “No” if it is false.
*   _OR(…)_: The OR function is used to check the two conditions, and if either of the conditions is true, the OR function returns TRUE.
*   _COUNTIF(A2, “ABK\*”)_: This is the first condition inside the OR function. The COUNTIF function checks if the value in cell A2 begins with “ABK”. The asterisk (\*) is a wildcard character that represents any number of characters. So, “ABK\*” will match anything that starts with “ABK”, like “ABK-879-US”, “ABK-616-ER”, etc. If it matches, the COUNTIF function returns 1.
*   COUNTIF(A2, “\*US”): This is the second condition inside the OR function. It checks if the value in cell A2 ends with “US”. Again, the asterisk (\*) represents any number of characters before “US”. So, “\*US” will match anything that ends with “US”, like “ABK-879-US”, “LDJ-124-US”, etc. If it matches, the COUNTIF function returns 1.
*   “Yes”, “No”: These are the values that the IF function will return. If either of the conditions is true (i.e., A2 starts with “ABK” or ends with “US”), the formula returns “Yes”. If neither condition is met, it returns “No”.

Also read: [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)

Highlight If Cells Contains Partial Text
----------------------------------------

In all the examples above, I have checked whether the cell contains a partial text string or not and got the result in the adjacent column.

In this section, I will show you how to use conditional formatting to highlight all the cells that contain a required partial text.

Let’s say that I’m using the below data set where I have the product IDs in column A, and I want to highlight all the cells where the product ID contains the string ABK (it could be anywhere in the string).

![Highlight If Cells Contains Partial Text Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20425'%3E%3C/svg%3E)

While I have already covered the formula that would give us the result as Yes or No in the adjacent column, in this case, I am going to put this formula within Conditional Formatting so it helps us highlight the cells that contain that partial text string.

Here are the steps to do this:

1.  Select the cells in column A that have the product ID.
2.  Click the Home tab.

![Click the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20346%20223'%3E%3C/svg%3E)

3.  Click on the Conditional Formatting option.

![Click on the conditional formatting option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20223'%3E%3C/svg%3E)

4.  Click on the New Rule option. This is going to open the ‘New Formatting Rule’ dialog box.

![Select the new rule option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20485'%3E%3C/svg%3E)

5.  Select the option – _Use a formula to determine which cells to format._

![Select use a formula to determine which cells to format option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the field:

\=ISNUMBER(SEARCH("ABK",A2))

7.  Click on the Format button. This will open the ‘Format Cells’ dialog box.

![Click on the format button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

8.  Click on the Fill tab and select the color in which you want to highlight the cells.

![Select the color in the fill tab with which you want to highlight the cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20673'%3E%3C/svg%3E)

9.  Click OK.

The above steps would apply the conditional formatting on the selected cells, and any cell that has the string “ABK” would be highlighted in the specified color.

![Sales with the partial text are highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20315%20448'%3E%3C/svg%3E)

You can modify the formula based on your criteria.

Note: Remember that the formula within Conditional Formatting needs to return either a TRUE or a FALSE. It highlights a cell when the condition is met, and the result of the formula is TRUE.

_[**Click here to Download the Example File**](https://www.dropbox.com/scl/fi/al4gn5ucg6ls789edoufe/Check-IF-Cell-Contains-Partial-Text-in-Excel.xlsx?rlkey=jyc1d6nabcgcvhgfed9ch5kxm&dl=1)
_

So these are some of the formula methods you can use to check if a cell contains partial text matches or not. I’ve covered scenarios where you can check a cell for partial text match anywhere in the cell, in the beginning, or at the end.

I hope you found this Excel tutorial helpful. Feel free to contribute to the article by leaving a comment below.

**Other Excel tutorials you may also like:**

*   [How to Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Lookup and Return Values in an Entire Row/Column in Excel](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/)
    
*   [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    
*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    
*   [Count Cells Less than a Value in Excel (COUNTIF Less Than)](https://trumpexcel.com/countif-less-than/)
    
*   [Highlight Rows Based on a Cell Value in Excel](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Filter Cells that have Duplicate Text Strings (Words) in it](https://trumpexcel.com/duplicate-text-strings/)
    
*   [SUM Based on Partial Text Match in Excel (SUMIFS)](https://trumpexcel.com/sum-partial-match/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/#respond)

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