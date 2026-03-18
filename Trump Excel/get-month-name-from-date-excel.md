# How to Get Month Name from Date in Excel (4 Easy Ways)

**Source:** https://trumpexcel.com/get-month-name-from-date-excel

---

[Skip to content](https://trumpexcel.com/get-month-name-from-date-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/get-month-name-from-date-excel/#below-title)

Excel allows you to format dates in many different ways. You can choose to show the date in a short date format or in a long date format.

You can also only show the day number, the month name, or the year from a given date.

In this short Excel tutorial, I will show you some easy methods to **get the month name from a date in Excel**.

So, let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/get-month-name-from-date-excel/#)

Getting the Month Name from the Date
------------------------------------

There are multiple different ways to get monthly from a date in Excel.

The method you choose would depend on how you want the result (i.e., whether you want it as a text string or have the entire date but only show the name of the month)

Let’s see a couple of methods to do this that you can use in different scenarios.

### Custom Formatting

Using [custom number formatting](https://trumpexcel.com/excel-custom-number-formatting/)
 to get the month name is the best method out of all those covered in this tutorial.

This is because it does not change the underlying date. It only changes the way the date is being displayed in the cell – which is by showing only the month name from the date.

The benefit of using this method is that you can still use the date in calculations.

Suppose you have the dates as shown below and you want to only display the month name and not the entire date.

![Date Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20342'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select all the cells that have the dates for which you want to show the month name
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20200'%3E%3C/svg%3E)
3.  In the Number group, click on the dialog box launcher icon (or you can use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
     Control +1). This will open the Format Cells dialog box![Click on Format Cells open dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20409%20216'%3E%3C/svg%3E)
4.  In the Category options, click on Custom![Click on Custom option in Fomat Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)
5.  In the type field, enter – ‘**mmmm**’. you should see one of the month names in the Sample preview.![Enter mmmm as the custom number format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)
6.  Click OK

The above steps would convert all the dates into their respective full month names (as shown below).

![Date showing only the month name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20341'%3E%3C/svg%3E)

As I mentioned, the good thing about this method is that even though you are seeing the month names in the cell, the underlying value is still a date (which means that the underlying value is still a number that represents the date).

So, if you want to use these dates in calculations, you can easily do that.

You can also use custom number formatting to show the month name or the month value in different ways. To do this, you will have to give custom number formatting the right code to display the month name.

Below are the different month codes that you can use:

*   **m** – this will show the month number. For example, a date in January would be shown as 1, a date in February would be shown as 2, and so on
*   **mm** – this will also show the month number, but it will also make sure that there are always two digits that are displayed. For example, a date in January would be shown as 01, a date in February would be shown as 02, and a date in November would be shown as 11
*   **mmm** – this will show the month name in a three-letter code. For example, a date in January would be shown as Jan, a date in August would be shown as Aug, and so on
*   **mmmm** – this is the option that we used in the above example, and it would show the complete month name
*   **mmmmm** – this option shows only the first alphabet of the month name. For example, January is shown as J and February is shown as F, and so on. I’ve never seen this being used because it’s confusing as January would also show J and July would also show J

### TEXT Function

TEXT function allows us to convert a date into any permissible format that we want and gives the result as a text string.

For example, we can use the [TEXT function](https://trumpexcel.com/excel-text-function/)
 to show the month name from a date.

Now if you’re wondering how is it different from the custom number formatting we used earlier, the big difference here is that with the TEXT function, you can combine the result with other functions or text strings.

Don’t worry if you are a little lost as of now, the next few examples will make it clear.

Suppose you have a dataset as shown below and you want to show the month name instead of the full date.

![Date Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20342'%3E%3C/svg%3E)

Below is the TEXT formula will give you the month name:

\=TEXT(A2,"mmmm")

![TEXT formula to get Month Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20505'%3E%3C/svg%3E)

The above text formula takes the date as the input and applies the specified format to it (which is “mmmm” in this formula).

Unlike the Custom Number Formatting method, when you use the TEXT function, the result is a text value. This means that you cannot use the result as a date or number in calculations.

But a good thing about using the TEXT function is that you can combine the result of the function with other text strings.

Let me explain using an example.

Suppose you have the same data set and in this case, instead of just getting the month name, you want to get the month name followed by the quarter number (such as January – Quarter 1).

The below formula would do this for you:

\=TEXT(A2,"mmmm")&" - Quarter "&ROUNDUP(MONTH(A2)/3,0)

![TEXT formula to combine text and formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20451'%3E%3C/svg%3E)

The above formula uses the ROUNDUP and the MONTH function to get the [quarter number](https://trumpexcel.com/calculate-quarter-from-date-excel/)
 of the calendar year, and then it is combined with the month name which is given by the TEXT function.

Since the result of the TEXT function is a text string, I can combine it with other text strings or formula results.

Also read: [Convert Month Name to Number in Excel](https://trumpexcel.com/convert-month-name-to-number-excel/)

### CHOOSE Function

Another formula that you can use to quickly get the month name from the month number is using the CHOOSE formula.

While it ends up being a long formula, the choose formula technique is useful when you want to get the result which you cannot get with custom number formatting or the text function.

For example, if you want to return custom month names (such as month names in any other language or only five alphabets for each month name), you can do that using the CHOOSE formula.

Suppose you have a data set as shown below and you want to get the month name for each of these dates.

![Date Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20265%20342'%3E%3C/svg%3E)

Below is the formula that will do that:

\=CHOOSE(MONTH(A2),"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

![Choose formula to get Month name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20712%20476'%3E%3C/svg%3E)

CHOOSE formula takes an index number (which is given by the month formula in our example) and then uses that index number to decide what value to return.

In this example, I have kept the month names to standard three-letter names, but you can change this and use whatever name you want.

Also read: [Get Days in Month in Excel](https://trumpexcel.com/days-in-month-excel/)

### Using Power Query

I have started using Power Query a lot more in my work as I find it a lot easier to [clean the data](https://trumpexcel.com/clean-data-in-excel/)
 using it.

It has an inbuilt feature that allows you to quickly convert a date into the month name.

The real value of using Power Query in such a scenario would be when you’re importing the data from other Excel files (or consolidating data from [multiple Excel files](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
 into one file), and while doing it you want to convert your dates into month names.

You can check out my [Power Query course](https://trumpexcel.com/power-query-course/)
 on YouTube if you want to learn more about it.

For this technique to work, your data needs to be in an Excel table. While you can still use Power Query with [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
, if your data is not in an [Excel table](https://trumpexcel.com/excel-table/)
 I recommend you use any of the above methods.

Suppose you have the below data and you want to convert these dates into month names.

![Excel Table with Dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20403'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select any cell in the dataset
2.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20201'%3E%3C/svg%3E)
3.  In the Get & Transform Data tab, click on From Table/Range![Click on From Table Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20201'%3E%3C/svg%3E)
4.  In the Power Query editor that opens up, right-click on the Date column header
5.  Go to Transform >> Month >> Name of Month![Click on Name of the Month in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20547'%3E%3C/svg%3E)
6.  Click on Close and Load![Click on Close and Load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20141'%3E%3C/svg%3E)

The above steps would insert a new worksheet and give you the resulting table in that new sheet.

![Result with Month Name from Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20454'%3E%3C/svg%3E)

Now, if you’re wondering why do all this when you can simply use custom number formatting or the text function, you need to understand the real value of Power Query trying to automate work.

If you need the month name from the date just once, feel free to use the methods shown above.

But if you’re using Power Query already to manage [data from multiple different sources](https://trumpexcel.com/combine-multiple-worksheets/)
 or combined files or sheets, then knowing that you can easily get the month name from the date can save you a lot of time.

So these are some of the methods that you can use to quickly get the month name from a date in Excel.

I hope you found this tutorial useful.

**Other Excel tutorial’s you may also like:**

*   [Calculate the Number of Months Between Two Dates in Excel](https://trumpexcel.com/calculate-months-between-two-dates/)
    
*   [Calculate Time in Excel (Time Difference, Hours Worked, Add/ Subtract)](https://trumpexcel.com/calculate-time-in-excel/)
    
*   [How to Change Date Format In Excel?](https://trumpexcel.com/change-date-format-excel/)
    
*   [How to Get the First Day of the Month in Excel](https://trumpexcel.com/first-day-of-month-excel/)
    
*   [How to Add or Subtract Days to a Date in Excel (Shortcut + Formula)](https://trumpexcel.com/add-days-to-date-in-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel)](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates Automatically](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Make an Interactive Calendar in Excel? (FREE Template)](https://trumpexcel.com/interactive-calendar-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/get-month-name-from-date-excel/#respond)

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