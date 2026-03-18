# How to Convert Text to Date in Excel (8 Easy Ways)

**Source:** https://trumpexcel.com/convert-text-to-date-excel

---

[Skip to content](https://trumpexcel.com/convert-text-to-date-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-text-to-date-excel/#below-title)

Working with dates is a common task for many Excel users.

And sometimes, you can come across dates that are formatted as text (or look like dates but are not in the acceptable date formats, so Excel treat them as text strings).

Since dates are stored as numbers in the backend in Excel, it allows you to format dates in different ways as well as use them in calculations.

But when a date is stored as a text string in Excel, you won’t be able to use it in calculations or format it like a date.

In this tutorial, I will show you **how to convert text into dates in Excel**.

I will cover various scenarios where you may encounter a date that has either been formatted as text or is entered as a text string (and Excel doesn’t recognize that it’s a date).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-text-to-date-excel/#)

Regular Date vs Text Date in Excel
----------------------------------

Before I get into the methods on how to convert text to date in Excel, let me first explain what’s the difference between a date that is an acceptable format in Excel, and a date that is in the text format.

As I mentioned earlier, dates are stored as numbers in the back end in Excel, which makes it possible for us to use them in calculations just like numbers.

This also makes it possible for us to format dates and show it in different ways, which cannot be done when the date is entered as a text string or formatted as a text.

To give you an example, 01-Jan-2023 is an acceptable date format in Excel and if you enter this in a cell, it would be shown as a date, but it would be stored as 44927 in the backend (where 44927 is the number corresponding to the date 01-Jan-2023).

However, if you enter 01.Jan.2023, it would be entered as a text string because this is not an acceptable date format. This also means that you cannot use this in calculations because this has not been stored as a number in the back end

Below I have the table where I show the difference between an acceptable date format and a date in text format or entered as a text string.

| Date Stored as Number | Dates Stored as Text |
| --- | --- |
| Since these are numbers in the backend, these dates would be aligned to the left by default | Since these are text, these would be aligned to the right |
| These can be used in calculations | If dates are entered as a text string in Excel, you won’t be able to use this in formulas. However, if dates are formatted as text, then you can convert them back to numbers/dates, and then use them in formulas.  <br>  <br>You can change the format to show these in other acceptable date formats (such as MM-DD-YYYY or DD-MM-YYYY or show only the [month name](https://trumpexcel.com/get-month-name-from-date-excel/)<br> or only the month and year)Since these are text, you cannot change the formatWhen you select cells containing the dates, you would be able to see Sum or Average in the status barSince these are text strings, you would only see the count value in the status bar |

Now let’s look at some of the methods you can use to convert text to dates in Excel

Convert Text to Date in Excel (with acceptable Date Formats)
------------------------------------------------------------

First, we’ll look at scenarios where you have dates that are considered acceptable date format in Excel but are formatted as text in the cells.

For example, 01-Jan-2023 is an acceptable date format, and in case it has been formatted as text, you will be able to use the methods shown in this section to convert it back to date.

However, if a date is entered in a format that is not an accepted date format (such as 01.Jan.2023 or 8th Jan 2023), you will have to use methods covered later in this tutorial.

### Using the DATEVALUE Function

Often, when you download your data from a database or you copy your data from a web page, you would notice that the dates have been formatted as text.

If your date is in the acceptable date format but has been formatted as text, you can easily convert it into the corresponding serial number by using the [DATEVALUE function](https://trumpexcel.com/excel-datevalue-function/)
.

And once you have the number, you can easily format it as a date.

Below I have a data set where I have dates in column A that have been formatted as text and I want to convert these back to regular dates.

![Date Dataset VALUE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20244'%3E%3C/svg%3E)

This can be done using the below DATEVAUE formula:

\=DATEVALUE(A2)

Copy this formula to all the cells in column B.

![DATEVALUE formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20628%20288'%3E%3C/svg%3E)

When you use this formula, it gives you a numeric value, which corresponds to the date in cell A2.

So while we have got the text date converted into a number, we still need to format it so that it shows up as a date in the cell.

Below are the steps to format these numbers in column B to date:

1.  Select the cells that contain DATEVALUE results
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20223'%3E%3C/svg%3E)

3.  In the Numbers group, click on the formatting drop-down
4.  Select the ‘Short date’ or ‘Long date’ format

![Select Short or Long date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20429'%3E%3C/svg%3E)

The above steps would convert the text that you have in column A into serial numbers using the DATEVALUE function, and then these are formatted to show up as dates.

![Date formatted as long date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20246'%3E%3C/svg%3E)

In case you need more control over how the dates are formatted, you can also use the Format Cells dialog box, which has a lot more date formatting options, as well as the option to create your own date format.

Also read: [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)

### Using the VALUE Function

While the DATEVALUE function is built specifically to deal with dates that have been formatted as text, there is also a VALUE function that can deal with dates as well as non-dates.

VALUE takes any number that has been formatted as text and converts it back into numbers.

Below I have a data set where I have dates in column A that are in the text format, and I want to convert these back into regular dates.

![Date Dataset VALUE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20244'%3E%3C/svg%3E)

Below is the VALUE formula that will do this for me:

\=VALUE(A2)

Copy this formula to all the cells in column B.

![VALUE function to change text to date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20294'%3E%3C/svg%3E)

And if you see the result as numeric values and not dates, you can format the cells to show these in dates using the below steps:

1.  Select the cells that contain VALUE formula results
2.  Click the Home tab
3.  In the Numbers group, click on the formatting drop-down
4.  Select the Short date or Long date format

![Select Long or Short date format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20489'%3E%3C/svg%3E)

### Using Mathematical Operators (Add, Multiple, Double Minus, Division)

If you have a date in the format that Excel understands (even if it is in the text format), you will be able to use it in simple arithmetic calculations (such as addition or subtraction or multiplication or division).

We can use simple arithmetic calculations to convert the date that we have in the text format back into numeric format.

All you need to make sure is that you don’t end up changing the date in the calculation (which won’t happen if you add zero to the date or multiply the date by 1).

Below I have a data set where I have the dates in the text format in column A (but note that these are the dates that Excel would have considered as proper dates had they not been in the text format).

![Date Dataset VALUE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20244'%3E%3C/svg%3E)

And here are some simple arithmetic calculations you can use in the adjacent column to get the numeric value of the date.

\=A2+0

or

\=A2\*1

or

\=A2/1

or

\=--A2

You can use any of the above formulas and it would give you a numeric value in column B as shown below.

![Add 0 to get the numeric value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20294'%3E%3C/svg%3E)

Note that we have the numeric value of the date in column A comma we can convert these back into date format.

Below are the steps to convert these numeric values into dates:

1.  Select the cells in column B that have the numeric value
2.  Click the Home tab
3.  In the number group, click on the drop-down
4.  Select the date format that you want to apply to the selected cells

In case you want to customize the date format further, select the cells in column B and then use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 Control + 1 to open the Format Cells dialog box. Here you will get more date format options and you can also create your own custom date format if you want.

### Using Paste Special

As explained in the previous method, you can convert a date that is formatted as text back into a numeric value by adding a zero to it.

While I’ve used a formula and got the result in a separate column in the above method, you can also do the same thing using the Paste Special dialog box.

Below I have a data set where I have the dates in the text format in column A and I want to convert these back to dates:

![Date Dataset VALUE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20244'%3E%3C/svg%3E)

Below are the steps to convert dates in text format back into dates using the Paste Special technique:

1.  Copy any blank cell in the worksheet
2.  Select the dates in column A
3.  Right-click on the selection and then click on Paste Special option. This will open the Paste Special dialog box

![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20593'%3E%3C/svg%3E)

4.  Select the ‘Values’ option in the ‘Paste’ category
5.  In the ‘Operation’ category, select the ‘Add’ option

![Select Values and Add in Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20413'%3E%3C/svg%3E)

6.  Click Ok

The above steps would instantly convert all the dates in column A into numeric values.

![Dates changed to numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20331'%3E%3C/svg%3E)

Now you can select these cells and change the format to show these numbers as dates.

![Format the date - short or long](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20426'%3E%3C/svg%3E)

**How does this work?**

When I copy a cell and then use paste special to add that cell to the dates in column A it’s essentially adding zero to these dates.

This addition does not change the numeric value of the date but it does convert the date value which is formatted as text into a numeric value that represents that date in the back end of Excel.

Also read: [How to Multiply in Excel Using Paste Special](https://trumpexcel.com/multiply-in-excel-using-paste-special/)

Convert Text to Date (with Format Not Recognized as Dates)
----------------------------------------------------------

In all the examples covered above, I’ve shown you how to convert a date that is in the text format back into a date.

But so far, all our dates were in a format that Excel actually recognizes as a proper date.

It’s just that they have been formatted as text, so all we had to do was change the format back to date.

In this section, I’m going to show you some techniques that you can use when you have dates that are not recognized by Excel proper dates.

Such datasets often need more work, as we need to manipulate the data and convert it into proper date formats

### By Changing the Delimiters in the Date

When there are dots or spaces instead of forward-slash or hyphens in a date, Excel would consider it as a text value as this is not an acceptable date format in Excel.

Below I have data set where I have the dates in column A where there are dots in between the day, month, and year number.

![Dates with dots as delimiters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20313'%3E%3C/svg%3E)

If you try to use the DATEVALUE or the VALUE function on this data, it will give you a value error (as Excel does not know how to convert this text string into a numeric value).

![DATEVALUE function gives error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20621%20295'%3E%3C/svg%3E)

So the only way to convert this text value into data is by replacing the dot and changing the date into a proper date that Excel can recognize as a date.

Let me show you three different ways you can use to change the delimiters in the date in column A so that it can be used as a proper date in Excel.

#### Find and Replace

With [Find and Replace](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
, we can replace the dots in the date with a forward slash or [hyphen/dash](https://trumpexcel.com/remove-dashes-excel/)
 so that it will become a proper date format.

Below I have dates in column A that have dots as delimiters and I want to replace them with a forward slash or hyphen.

![Dates with dots as delimiters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20313'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the cells in column A that have the date
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20223'%3E%3C/svg%3E)

3.  In the Editing group, click on Find & Select
4.  Click on the ‘Replace’ option. This will open the Find and Replace dialog box

![Click on Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20468'%3E%3C/svg%3E)

5.  In the ‘Find what’ field in the dialogue box, enter . (dot)
6.  In the ‘Replace with’ field, enter – dash

![Find what and replace with in Find and Replace dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

7.  Click on ‘Replace All’

The above steps would instantly change the dots in the dates into dashes, making the text values in column A into dates. Note that the dates also aligns to the right (while it was aligned to the left when it has dots instead of dashes).

![Dates converted from text to dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20457%20316'%3E%3C/svg%3E)

**Pro Tip**: You can use the keyboard shortcut **Control + H** to open the ‘Find and Replace’ dialog box

#### Using Text to Columns

Another quick way to convert dates that are in text format into proper dates is by using the [Text to Columns option](https://trumpexcel.com/excel-text-to-columns-examples/)
.

Below I have a dataset where I have dates in column A that have dots as the delimiters and I want to convert these into regular dates that are recognizable by Excel.

![Date dataset for text to columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20248'%3E%3C/svg%3E)

Below are the steps to do this using Text to Columns:

1.  Select the cells in column A that have the dates
2.  Click the ‘Data’ tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20439%20223'%3E%3C/svg%3E)

3.  In the ‘Data Tools’ group, click on the ‘Text to Columns’ option

![Click on Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20223'%3E%3C/svg%3E)

4.  In Step 1 of the Convert Text to Columns Wizard, select Delimited and then click on Next

![Step 1 of Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20499'%3E%3C/svg%3E)

5.  In Step 2, make sure none of the delimiter option is selected, and then click on Next

![Step 2 of Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20499'%3E%3C/svg%3E)

6.  In Step 3, select the Date option and specify the destination cell (I would use $B$2 in this example). If you do not specify the destination cell, the data in the column would be overwritten

![Step 3 of Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20499'%3E%3C/svg%3E)

7.  Click on the Finish button

The above steps would instantly give you the dates in column B

![Text to Columns result date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20245'%3E%3C/svg%3E)

It’s possible that the dates that you get in Column B are not in the format that you want.

So once you have the result, you can change the format by selecting the cells in Column B, holding the Control key, and pressing the 1 key. This will open the Format Cells dialog box where you can change the format of the dates.

#### SUBSTITUTE Function

You can also use the SUBSTITUTE function to replace the dots or dashes or any other delimiter with a forward slash or dash.

While the result of the SUBSTITUTE formula would be a text string, since it would be in an acceptable date format, we would be able to use DATEVALUE function to convert it into the numeric value of the corresponding date.

And once we have the numeric value, we can then format the cells to show the date in any format we want.

Below I have the data set where I have dates in column A that have dots as the delimiters, and I want to convert these into proper dates.

![Date dataset for text to columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20615%20248'%3E%3C/svg%3E)

Build the formula that would give us the numeric value that represents the proper date:

\=DATEVALUE(SUBSTITUTE(A2,".","-"))

Enter this formula in cell B2 and then copy it for all the other cells.

![SUBSTITUTE function to change delimiter in date in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20295'%3E%3C/svg%3E)

Once you have the results in column B, follow the below steps to convert these numbers back into dates:

1.  Select the cells in Column B that have the dates
2.  Click the Home tab
3.  In the Number group, click on the Format drop-down
4.  Select the ‘Short Date’ option

In case you want the dates to be shown in any other format, open the format cells dialog box and then choose from the multiple inbuild date formats or create your own custom date format.

Note that in the above formula, I had dots in the dates that I wanted to replace with dashes. In case you have any other delimiter (such as space), you need use that delimiter instead of the dot in the formula.

### Convert Two Digit Year Text Date to Proper Date By Using Error Checking

Sometimes you may get a data set where the year is represented by two digits instead of the four digits in the date.

For example, instead of 01-Jan-2023, it would be 01-Jan-23

Thankfully, it only takes a click to get this sorted.

Below I have a data set in column A where I have the dates with two-digit year values and I want to convert these into proper date formats.

![Date in two year digit format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20267'%3E%3C/svg%3E)

Here are the steps to do that:

1.  Select all the cells in column A that have the two-digit year date
2.  Click on the error-checking icon at the top right of the selection (it’s a yellow triangle icon)

![Click on the yellow error triangle icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20295'%3E%3C/svg%3E)

3.  Click on ‘Convert XX to 20XX’ option

![Select convert XX to 20XX option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20306'%3E%3C/svg%3E)

The above steps would change the dates and convert the two-digit year value to a four-digit year value.

Note that you can only use this if all the dates in your data set are of the same format (19XX or 20XX). In case there is a mix (for example in the case of date of birth), you will not be able to use this method

### Using TEXT formulas

Sometimes you may get dates that have some additional text in the same cell.

For example, you can get a date where it includes the day name (such as Saturday, 08 Oct 2022) or a suffix after the day value (such as 8th October 2023 or 2nd October 2023).

In these cases, you first need to use some text formulas to [clean the data](https://trumpexcel.com/clean-data-in-excel/)
 and remove these unwanted text strings, and then try and [convert these dates into their corresponding serial number](https://trumpexcel.com/convert-date-to-serial-number-excel/)
 (which can be done using the DATEVALUE function).

Let me show you a couple of common examples and how you can do this using simple text formulas:

### When You Have Day Name in the Date

Below I have a data set where I have the [day name](https://trumpexcel.com/get-day-name-from-date-excel/)
 before the date in column A, and I want to convert these dates in column A into proper date format.

![Date with day name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20246'%3E%3C/svg%3E)

Here is the formula that will do this for me:

\=DATEVALUE(RIGHT(A2,LEN(A2)-FIND(" ",A2)))

Enter this formula in cell B2 and then copy it for all the cells in column B.

![DAY name removed with formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20290'%3E%3C/svg%3E)

In the above data set, the day name is always followed by a comma and a space character.

Since this is the same in all the cells in the data set, I have used the above formula to first identify the position of the first space character (using the [FIND function](https://trumpexcel.com/excel-find-function/)
).

Once I know the position of the first space character, I used the [RIGHT function](https://trumpexcel.com/excel-right-function/)
 to extract everything which is to the right of that space character.

And since the result of the RIGHT function is still a text string, I’ve used the DATEVALUE function to get the serial number of the date.

Once you have the serial number of the date, you can format the cell to show it in the short or long date format (your option is available in the Home tab in the formatting drop-down)

#### When You have Suffix After the Day Value in the Date

Below are the data set where I have a suffix (such as ‘th’, ‘rd’, ‘nd’, ‘st’) after the day value.

![Dates with suffix](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20247'%3E%3C/svg%3E)

Because of this, the date is considered as a text string in Excel, and to convert this date in the text format back into the date format, I will have to remove the suffix from these cells.

Below is the formula that will do this for me:

DATEVALUE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A2,"th",""),"st",""),"rd",""),"nd",""))

Enter this formula in cell B2 and then copy it for all the cells in column B.

![formula to remove suffix from date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20287'%3E%3C/svg%3E)

In the above formula, I have used the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
 to remove each of these suffix values and replace these with blanks.

Since there are four such values (th, st, rd, nd), I had to use the SUBSTITUTE function four times.

The result of one SUBSTITUTE function is fed into another SUBSTITUTE function so that in the end we get the result where any of these four suffixes would be removed.

Once the suffixes are removed, we have used the DATEVALUE function to get the serial number of the date so that we can convert it back into the proper date format

Convert 8 Digit Date in MMDDYYYY format to Date
-----------------------------------------------

Below I have a data set where I have the dates in the DDMMYYYY format, where there is no space or delimiter between any of the digits.

![Date in 8 digit format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20246'%3E%3C/svg%3E)

Since the above dataset follows a consistent pattern (where the first two digits are always the day value, the next two digits are the month value, and the last four digits are the year value), we can use simple text formulas to extract these digits and specify them as the day, month and year values.

Here is the formula that will do this for me:

\=DATE(RIGHT(A2,4),MID(A2,3,2),LEFT(A2,2))

Enter this formula in cell B2 and then copy it for all the cells in column B.

![Formula to convert 8 digit to proper date](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20293'%3E%3C/svg%3E)

The above formula uses the RIGHT, MID, and [LEFT functions](https://trumpexcel.com/excel-left-function/)
 to extract the year, month, and day values respectively,

And then these are used within the [DATE function](https://trumpexcel.com/excel-date-function/)
 to construct a proper date in Excel.

In this tutorial, I showed you **how to convert text to date in Excel** using various techniques.

The method you use would depend on whether your date is in a format that Excel would recognize as a proper date or not.

If it is in a proper date format and is being considered as a text string in Excel, you can use formulas such as DATEVALUE or VALUE to get the serial number of the date and then format it to show as a short or long date.

You can also use simple arithmetic operators or [Paste Special operation](https://trumpexcel.com/excel-paste-special-shortcuts/)
 techniques to quickly convert dates that are formatted as text into serial numbers corresponding to that date.

And in case your dates are in a format that is not recognized by Excel a date, you will need to do some text manipulation using simple text formulas or functionalities such as Find and Replace or Text to Columns.

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like**:

*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    
*   [Combine Date and Time in Excel (Easy Formula)](https://trumpexcel.com/combine-date-time-excel/)
    
*   [Convert Date to Text in Excel – Explained with Examples](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [How to Convert Numbers to Text in Excel](https://trumpexcel.com/convert-numbers-to-text-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Convert Text to Date in Excel (8 Easy Ways)”
-----------------------------------------------------------------

1.  Very exhaustive! Thank you.  
    I’m amazed they don’t allow a ‘format template’ argument to DATEVALUE so one could SO easily convert YYYYMMDD to a date value. DATEVALUE(A2,”YYYYMMDD”)  
    I cant believe this doesn’t exist!  
    It blows my mind that I have to do string operations!  
    Thanks again, very thorough and clear information. (unlike the AI slop you get these days)
    
    [Reply](https://trumpexcel.com/convert-text-to-date-excel/#comment-48928)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-text-to-date-excel/#respond)

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