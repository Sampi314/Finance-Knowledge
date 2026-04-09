# Remove Characters From Left in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/remove-characters-from-left-excel

---

[Skip to content](https://trumpexcel.com/remove-characters-from-left-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-characters-from-left-excel/#below-title)

Cleaning text data is often the most time-consuming task for many Excel users.

Unless you’re among the few lucky ones, you’ll most likely get your data in a format that would need [some cleaning](https://trumpexcel.com/clean-data-in-excel/)
.

One common use case of this would be when you get a dataset and you have to **remove some characters from the left** for this dataset.

These could be a fixed number of characters that you need to remove from the left, or could be before a specific character or string.

In this tutorial, I will show you some simple examples of removing the required number of characters from the left of a text string.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-characters-from-left-excel/#)

Removing Fixed Number of Characters from the Left
-------------------------------------------------

If you get a dataset that is consistent and follow the same pattern, then you can use the technique shown here to remove a fixed number of characters from the left of the string in each cell.

Below I have a dataset where I have the product ids, which consist of a two-letter code followed by a number, and I want to extract only the number in each cell (which means that I want to remove the first three characters from each cell).

![Data to remove characters from the left](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20383'%3E%3C/svg%3E)

Below is the formula to do this:

\=RIGHT(A2,LEN(A2)-3)

![Formula to remove fixed number of characters from the left](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20433'%3E%3C/svg%3E)

The above formula uses the [LEN function](https://trumpexcel.com/excel-len-function/)
 to get the total number of characters in the cell in column A.

From the value that we get from the LEN function, we subtract 3, as we only want to [extract the numbers](https://trumpexcel.com/extract-numbers-from-string-excel/)
 and want to remove the first three characters from the left of the string in each cell.

This value is then used within the [RIGHT function](https://trumpexcel.com/excel-right-function/)
 to extract everything except the first three characters from the left.

Since we have hardcoded the number of characters we want to remove from the left, this method would only work when you always want to remove the fixed number of characters from the left. If, in the above example, we have inconsistent data where there are varying numbers of characters before the number, we would not be able to use the above formula (use the formula next section in such a scenario).

Removing Characters from the Left based on Delimiter (Space, Comma, Dash)
-------------------------------------------------------------------------

In most cases, you’re unlikely to get consistent data where the number of characters you want to remove from the left would be of fixed length.

For example, below I have the names dataset where I want to remove the first name and only get the last name.

![Names Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20455'%3E%3C/svg%3E)

And as you can see, the length of the first name varies, so I can not use the formula covered in the previous section.

In this case, I still need to rely on a consistent pattern – which would be a space character that separates the first and the [last name](https://trumpexcel.com/extract-last-name-excel/)
.

If I can remove everything till the space character, I would get the desired result.

And thanks to awesome functionalities in Excel, there are multiple ways to do this.

### Using the RIGHT Formula

Let’s first have a look at a formula that will remove everything before the space character and you will be left with the last name only.

\=RIGHT(TRIM(A2),LEN(TRIM(A2))-FIND(" ",TRIM(A2)))

![Formula to remove everything before delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20503'%3E%3C/svg%3E)

The above formula will remove everything to the left of the space character (including the space character), and you will get the rest of the text (last name in this example).

Let me quickly explain how this formula works.

First, I have used the [FIND function](https://trumpexcel.com/excel-find-function/)
 to get the position of the space character in the cell.

In the above formula, FIND(” “,TRIM(A2))) would return 6 as the space character occurs at the sixth position in the name in cell A2.

I then used the LEN function and subtracted the value that the FIND function gave me to get the total number of characters after the space character in the cell.

And now that I know how many characters to extract from the right of the text string, I’ve used the RIGHT function to extract it.

Note: In the above formula, I have used the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 to make sure that any [leading, trailing, or double spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 are taken care of.

_One big benefit of using a formula is that the results automatically update in case you make any changes in the data in Column A._

### Using Flash Fill

Another really fast way to quickly remove text from the left of the delimiter is by using [Flash Fill](https://trumpexcel.com/flash-fill-excel/)
.

Flash Fill works by identifying patterns from a couple of inputs from the user. In our example, I would have to manually enter the expected result for one or two cells, and then I can use Flash Fill to follow the same pattern for all the other remaining cells.

Suppose I have a dataset, as shown below, where I want to remove all the characters before the space character.

![Names Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20455'%3E%3C/svg%3E)

Below are the steps to use flash fill to remove characters from the left of a delimiter:

1.  In cell B2, enter the expected result (Baker in this case)

![Enter expected result in cell B2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20403'%3E%3C/svg%3E)

2.  Select cells B2 to B12 (the range where you want the result)

![Select all the cells in the column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20402'%3E%3C/svg%3E)

3.  Hold the Control key and press the E key (or Command + E if using Mac)

![Control E to use flash fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20405'%3E%3C/svg%3E)

The above steps would remove everything from the left of the space character and you will be left only with the last name.

_Note that Control + E (or Command + E in Mac) is the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 for Flash Fill in Excel._

Now let me quickly explain what’s happening here.

When I manually enter the expected result in cell B2, and then select all the cells and use Flash Fill, it tries to identify the pattern using the result I’ve already entered in cell B2.

In this example, it was able to identify that I am trying to extract the last name, which means that I’m trying to remove everything which is there on the left of the last name.

Once it was able to identify this pattern, it applied it to all the cells in the column.

In some cases, it is possible that Excel will not be able to identify the correct pattern when using Flash Fill. In such situations, you can try entering the results in more than one cell so that excel has more data to understand the pattern.

For example, you can enter the expected result in cells B2 and B3 and then [select the entire column](https://trumpexcel.com/select-entire-column-excel/)
 and use Flash Fill.

_You can also find the Flash Fill option in the Home tab –> Editing –> Fill –> Flash Fill._

Note that in case your original data in column A changes, you will have to repeat the steps again to remove the characters before the delimiter. Unlike the formula method, this method gives a static result that doesn’t auto-update

Also read: [Remove Last Character in Excel](https://trumpexcel.com/remove-last-character/)

### Using Text to Columns

Another quick way to remove all the characters before a delimiter would be by using the [Text to Columns feature](https://trumpexcel.com/excel-text-to-columns-examples/)
.

Suppose I have the dataset as shown below and I want to remove everything before the dash.

![Data set with product id and number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20385'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the range that has the data (A2:A10 in this example)
2.  Click the ‘Data’ tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20223'%3E%3C/svg%3E)

3.  In the Data Tools group, click on ‘Text to Columns’

![Click on Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20232'%3E%3C/svg%3E)

4.  In the Text to Columns Wizard Step 1 of 3: Make sure Delimited is selected

![Select the Delimiter option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)

5.  Step 2 of 3: Select Other as the Delimiter, and enter – in the box next to it

![Specify dash as the delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)

6.  Step 3 of 3: Select the ‘Do Not Import Column (Skip)’ option. Also make sure that in the Data Preview, the column selected (in black) is the one that you want to remove.

![Do not import the to the left of the delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)

6.  Step 3 of 3: In Data Preview, select the second column (the one that you want), and then select the destination cell (I will go with the already selected B2)

![Select the second column and specify the destination cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)

7.  Click on Finish

![Result of Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20385'%3E%3C/svg%3E)

The above steps would [split into separate columns](https://trumpexcel.com/split-multiple-lines/)
 based on the specified delimiter.

Note that in this example, I have used a delimiter to split the data into separate columns. You can also use Text to Columns to remove a specific number of characters from the left of a text string as well. For that, you should choose Fixed Length instead of the Delimiter option in Step 1 of 3 in the Text to Columns wizard.

Note that in case your original data in column A changes, you will have to repeat the steps again to remove the characters before the delimiter. Unlike the formula method, this method gives a static result that doesn’t auto-updates

Also read: [How to Remove Dashes (-) in Excel?](https://trumpexcel.com/remove-dashes-excel/)

Remove All Text On the Left of a Specific String
------------------------------------------------

Sometimes, you may have a dataset where you need to get rid of all the text before a specific text string.

For example, below I have a data set where I have employees’ names followed by their telephone numbers.

![Data to remove everything on th left of telephone number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20402'%3E%3C/svg%3E)

I want to extract only the telephone number from each cell, which means that I want to remove everything which is before the telephone number.

As with most data cleaning methods in Excel, I need to look for a pattern that I can use to get rid of everything before the phone number.

In this case, it’s the text string ‘Tel:’.

So all I need to do is find the location of the string ‘Tel:’ in each cell, and remove everything before it (including it).

While you can build an advanced formula in Excel for this, let me show you a really cool way using [Find](https://trumpexcel.com/find-and-replace-in-excel/)
 [](https://trumpexcel.com/find-and-replace-in-excel/)
[and Replace method](https://trumpexcel.com/find-and-replace-in-excel/)
.

Below are the steps to remove all the text before a specific text string:

1.  Copy the data from column A to Column B. I am doing this so that I will get the result in column B, while still keeping the original data in column A
2.  Select all the cells in column B

![Copy the data in column B](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20372'%3E%3C/svg%3E)

3.  Hold the Control key and press the H key (Command + H if using Mac). This will open the Find and Replace dialog box.

![Find and replace dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

4.  In the ‘Find what’ field, enter **\*Tel:**

![Enter Tel in find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

5.  Leave the ‘Replace with’ field empty

![Leave the replace with field empty](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

6.  Click on Replace All

The above steps would remove everything before the string ‘Tel:’, and you will be left with the phone number only.

![All characters before tel number are removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20671%20403'%3E%3C/svg%3E)

**How does this work?**

In the above example, I have used a [wild card character](https://trumpexcel.com/excel-wildcard-characters/)
 – asterisk (\*).

Since I wanted to remove everything to the left of the string ‘Tel:’, I added an asterisk before it and used it in the ‘Find what’ field.

An asterisk (\*) is a wild card character that can represent any number of characters in Excel.

This means that when I ask Excel to find ‘\*Tel:’, It is going to look for the string ‘Tel:’ in each cell, and if it finds this string in any cell, no matter its position, everything up to that point would be considered while replacing the text.

And since I replaced this with nothing (by leaving the ‘Replace with’ field empty), it simply removes everything up to that string in the cell.

This means that I’m only left with the characters after that text string and everything before that text string including that string itself is removed.

Remove All Text from the Left (and keep the numbers)
----------------------------------------------------

Sometimes you may get a data set where you have the text and numbers together in one single cell, as shown below, and you want to remove all the text but keep the numbers only.

![Dataset with Text followed by numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20363'%3E%3C/svg%3E)

This can easily be done using a simple formula.

Below is the formula that would remove all the text from the left of the numbers, so that you’re only left with the number part of the string.

\=RIGHT(A2,LEN(A2)-MIN(IFERROR(FIND({0,1,2,3,4,5,6,7,8,9},A2),LEN(A2)))+1)

![Formula to remove all text from the left](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20590%20435'%3E%3C/svg%3E)

The above formula would remove all the text portions from the left part of the cell so that you’re only left with the numbers.

Now let me quickly explain how this formula works.

The FIND({0,1,2,3,4,5,6,7,8,9},A2) part of the formula would look for these 10 digits in the cell and would return the position of these digits as an array.

For example, for sale A2 the result returned by this formula would be {8,#VALUE!,#VALUE!,#VALUE!,6,#VALUE!,#VALUE!,#VALUE!,#VALUE!,7}

As you can see, it returns 10 values where each value would represent the position of that number in the cell.

Since the digit 0 occurs at the eighth position, the first value returned is 8, and since the cell does not contain the digit 1, it returns a [Value error](https://trumpexcel.com/fix-value-error-in-excel/)
.

Similarly, all the digits are analyzed and a number is returned if the digit is present in the cell, and the value error is returned if that digit is not in the cell.

Now, this FIND formula is wrapped within the [IFERROR formula](https://trumpexcel.com/excel-iferror-function/)
, so that instead of the value error we get something more meaningful.

In this case, the IFERROR formula would return a number when it finds the digit in the cell, and in case it does not find the digit, it would return the maximum length of the characters in the cell (which is done using the LEN formula)

This is done to make sure that in case there are cells where there are no numbers, the IFERROR formula would still return a digit that can be used in the formula (else it would have returned an error).

Now with these arrays of numbers, I have used the [MIN function](https://trumpexcel.com/excel-min-function/)
 to find out the minimum value in that array. this would tell me the starting position where the numbers start in the cell.

For example in cell A2, it would give me 6 which means that the text part in the cell ends at the 5th character and the numbers begin from the 6th character onwards.

Now that I know at what position the numbers start in the cell, I need to know how many characters from the left I need to remove.

To do this, I have again used the LEN function to find the total length of characters in a cell, and from this, I have subtracted the result of the main function so that I would know how many text characters are there in the left.

Note that I have also subtracted 1 as I want to exclude the first number in the cell (if I don’t subtract 1 in this formula, it would also remove the first number along with the text).

And finally, I have used the RIGHT function to extract all the numbers from the right, which essentially means that all the text characters on the left are removed.

Remove All Numbers From the Left
--------------------------------

In the previous section, I showed you how to remove all the text characters from the left so that we are only left with the numbers in the cell.

But what if the situation is reversed.

What if I have a data set as shown below where I want to remove all the numbers from the left and keep all the text characters.

![Dataset with Numbers followed by text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20363'%3E%3C/svg%3E)

We can use a similar formula with some tweaks.

Below is the formula that would remove all the numbers on the left so that you only get the text part of the cell.

\=MID(A2,MIN(IFERROR(FIND({"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"},LOWER(A2)),LEN(A2))),1000)

![Formula to remove all numbers from the left](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20683%20436'%3E%3C/svg%3E)

While this formula may look bigger and a little scarier than the previous one, the logic is exactly the same.

In this formula, we have used the FIND function to find out the position of all the 26 alphabets in the English language.

The FIND portion of the formula checks the cell and gives us the position of each of the 26 alphabets.

Note that I have also used LOWER(A2) instead of A2, because the alphabet that I’m using in the FIND formula is in lower case.

I have then wrapped the fine formula within IFERROR, so that in case the formula is not able to find the position of a specific alphabet, instead of returning the value error, it would return the length of the content in the cell (which is given by the LEN formula).

This is to make sure that in case I have a cell where there there is no text portion there are only numbers, I would still get a numeric value.

I then used the MIN function to find out the minimum position where the text starts.

This would tell me where the numbers would end and where the text starts so that I can split the content of the cell to remove all the numbers from the left and keep the text portion.

Now that I know where the text characters start in the cell, I have used the [MID function](https://trumpexcel.com/excel-mid-function/)
 to extract everything starting from that position till the end.

Note that I have used 1000 characters to be extracted within the mid function, but in case your cell has less number of characters, only that much would be extracted.

So these are some of the examples where we have **removed characters from the left in a cell in Excel**.

I have shown you formulas to remove a fixed number of characters from the left or remove the characters on the left based on a delimiter.

I also showed you how to use a simple find and replace technique to remove all the characters on the left before a specific string.

And then finally I showed you two formulas that you can use to remove only the numbers or only the text from the left.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like:**

*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [How to Remove the First Character from a String in Excel (Quick & Easy)](https://trumpexcel.com/remove-first-character-from-string/)
    
*   [How to Combine First and Last Name in Excel (4 Easy Ways)](https://trumpexcel.com/combine-first-and-last-name-excel/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Capitalize First Letter of a Text String in Excel (using Formula & VBA)](https://trumpexcel.com/capitalize-first-letter-excel/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [Remove Asterisk (\*) in Excel](https://trumpexcel.com/remove-asterisk-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-characters-from-left-excel/#respond)

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