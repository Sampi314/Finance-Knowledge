# Excel Stock Quotes - Free Excel Stock Quote Tracker Macro & Workbook - Download

**Source:** https://chandoo.org/wp/excel-stock-quotes

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Get Stock Quotes using Excel Macros \[and a Crash Course in VBA\]
=================================================================

*   Last updated on June 2, 2010

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post by **Daniel Ferry** of [Excelhero.com](http://excelhero.com/)
._

_**![Excel Stock Quotes - using VBA Macors to fetch live stock quotes from Yahoo Finance to Excel](https://chandoo.org/img/vba/stock-quotes-in-excel-macro.png)Have you ever wanted to fetch live stock quotes from excel?**_ In this post we will learn about how to get stock quotes for specified symbols using macros.

One method that has worked well for my clients can be implemented with just a few lines of VBA code. I call it the ActiveRange.

An ActiveRange is an area on a worksheet that you define by simply entering the range address in a configuration sheet. Once enabled, that range becomes live in the sense that if you add or change a stock symbol in the first column of the range, the range will automatically (and almost instantly) update. You can specify any of 84 information attributes to include as columns in the ActiveRange. This includes things such as Last Trade Price, EBITDA, Ask, Bid, P/E Ratio, etc. Whenever you add or change one of these attributes in the first row of the ActiveRange, the range will automatically update as well.

_Sound interesting, useful?_

In this post, you can learn how to use excel macros to fetch live stock quotes from Yahoo! Finance website. It is also going to be a crash course in VBA for the express purpose of learning how the ActiveRange method works so that you can use it yourself.

### Download Excel Stock Quotes Macro:

[Click here to download the excel stock quotes macro workbook](https://img.chandoo.org/vba/activerange_yahoofinance_excelhero.com.xls)
. It will be much easier to follow this tutorial if you refer to the workbook.

### Background – Understanding The Stock Quotes Problem:

The stock information for the ActiveRange will come from [Yahoo Finance](http://finance.yahoo.com/)
. A number of years ago, Yahoo created a useful interface to their stock data that allows anyone at anytime to enter a URL into a web browser and receive a CSV file containing current data on the stocks specified in the URL. That’s neat and simple.

But it gets a little more complicated when you get down to specifying which attributes you want to retrieve \[[information here](http://www.gummy-stuff.org/Yahoo-data.htm)\
\]. Remember there are 84 discreet attributes available. Under the Yahoo system, each attribute has a short string Tag Code. All we need to do is to concatenate the string codes for each attribute we want and add the resulting string to the URL. We then need to figure out what to do with the CSV file that comes back.

Our VBA will take care of that and manage the ActiveRange. Excel includes the QueryTable as one of its core objects, and it is fully addressable from VBA. We will utilize it to retrieve the data we want and to write those data to the ActiveRange.

Before we start the coding we need to include two support sheets for the ActiveRange. The first is called “YF\_Attribs”, and as the name implies is a list of the 84 attributes available on Yahoo Finance along with their Yahoo Finance Tag Codes. The second sheet is called, “arConfig\_xxxx” where xxxx is the name of our sheet where the ActiveRange will reside. It contains some configurable information about the ActiveRange which our VBA will use.

All of the VBA code for this project will reside inside of the worksheet module for the sheet where we want our ActiveRange to be. For this tutorial, I called the sheet, “DEMO”.

### Writing the Macros to Fetch Stock Quotes:

![Adding VBA Code to Worksheets - Excel Stock Quotes](https://chandoo.org/img/vba/adding-code-to-worksheet-stockquotes.png)

Press ALT-F11 on your keyboard, which will open the VBE. Double click on the DEMO sheet in the left pane. We will enter out code on the right. To begin with, enter these lines:

Option Explicit  
Private rnAR\_Dest As Range  
Private rnAR\_Table As Range  
Private stAR\_ConfigSheetName As String

**Always start a module with Option Explicit. It forces you to define your variable types, and will save you untold grief at debugging time.** In VBA each variable can be one of a number of variable types, such as a Long or a String or a Double or a Range, etc. For right now, don’t worry too much about this – just follow along.

#### Sidebar on Variable Naming Conventions

**Variable names must begin with a letter.** Everyone and their brother seems to have a different method for naming variables. I like to prefix mine with context. The first couple of letters are in lower case and represent the type of the variable. This allows me to look at the variable anywhere it’s used and immediately know its type. In this project I’ve also prefaced the variables with “AR\_” so that I know the variable is related to the ActiveRange implementation. In larger projects this would be useful. After the underscore, I include a description of what the variable is used for. _That’s my method._

In the above code we have defined three variables and their types. Since these are defined at the top of a worksheet module, they will be available to each procedure that we define in this module. This is known as scope. In VBA, variables can have scope restricted to a procedure, to a module (as we have done above), or they can be global in scope and hence available to the entire program, regardless of module. Again we are putting all of the code for this project in the code module of the DEMO worksheet. Every worksheet has a code module. Code modules can also be added to a workbook that are not associated with any worksheet. UserForms can be added and they have code modules as well. Finally, a special type of code module, called a class module, can also be added. Any global variables would be available to procedures in all of these. However, it is good practice to always limit the scope of your variables to the level where you need them.

In that vein, notice that the three variables above are **defined with the word Private. This specifically restricts their scope to this module.**

**Every worksheet module has the built-in capability of firing off a bit of code in response to a change in any of the sheet’s cell values.** This is called the Worksheet\_Change event. If we select Worksheet from the combo box at the top and Change in the other combo box, the VBE will kindly define for us a new procedure in this module. It will look like this:

![Adding Worksheet_Change Event](https://chandoo.org/img/vba/worksheet-change-event-stock-quotes.png)

Private Sub Worksheet\_Change(ByVal Target As Range)  
End Sub

Notice that by default this procedure is defined as Private. This is good and as a result the procedure will not show up as a macro. Notice the word Target near the end of the first line. This represents the range that has been changed. Place code between these two lines so that the entire procedure now looks like this:

### The Heart of our Excel Stock Quotes Code – Worksheet\_Change()

Private Sub Worksheet\_Change(ByVal Target As Range)

ActivateRange

If Worksheets(stAR\_ConfigSheetName).\[ar\_enabled\] Then

If Intersect(Target, rnAR\_Dest) Is Nothing Then Exit Sub

If Target.Column <> rnAR\_Dest.Column And Target.Row <> rnAR\_Dest.Row Then

PostProcessActiveRange

Exit Sub

End If

ActiveRangeResponse

End If

End Sub

That may look like a handful but it’s really rather simple. Let’s step through it. The first line is `ActivateRange`. This is the name of another sub-procedure that will be defined in a moment. This line just directs the program to run that sub, which provides values to the three variables we defined at the top. Again, since those variables were defined at the top of the module, their values will be available to all procedures in the module. The ActivateRange procedure gives them values.

Next we see this odd looking fellow:

`If Intersect(Target, rnAR_Dest) Is Nothing Then Exit Sub`

All this does is check to see if the Target (the cell that was changed on the worksheet) is part of our ActiveRange. If it is the procedure continues. If it’s not, the procedure is exited.

The next line checks to see if the cell that was changed is in the first column or first row of the ActiveRange. If it is, the post processing is skipped. If the change is any other part of the ActiveRange, another sub-procedure (defined below) is run to do some post processing of the retrieved data, and then exits this procedure.

If the cell that changed was in the first column or the first row, the program runs another sub-procedure, called ActiveRangeResponse, which is also defined below. ActiveRangeResponse builds the URL for YF, deletes any previous QueryTables related to the ActiveRange, and creates a new QueryTable as specified in our configuration sheet.

That’s it. The heart of the whole program resides here in the Worksheet\_Change event procedure. It relies on a number of other subprocedures, but this is the whole program. When a change is made in the ActiveRange’s first column (stock symbols) or its first row (stock attributes), ActiveRangeResponse runs and our ActiveRange is updated.

### Understanding other sub-procedures that help us get the stock quotes:

So let’s look at those supporting subprocedures. The first is ActivateRange:

Private Sub ActivateRange()

stAR\_ConfigSheetName = “arConfig\_” & Me.Name

Set rnAR\_Dest = Me.Range(Worksheets(stAR\_ConfigSheetName).\[ar\_range\].Value)

Set rnAR\_Table = rnAR\_Dest.Resize(1, 1).Offset(1, 1)

Worksheets(stAR\_ConfigSheetName).\[ar\_YFAttributes\] = GetCurrentYahooFinancialAttributeTags

End Sub

Again, all this does is give values to our three module level variables. In addition it builds the concatenated string of YF Tag Codes required for the URL. It does this by calling a function that I’ve defined at the very bottom of the module, called GetCurrentYahooFinancialAttributeTags.

The next subprocedure is ActiveRangeResponse:

Private Sub ActiveRangeResponse()

Dim vArr As Variant

Dim stCnx As String

Const YAHOO\_FINANCE\_URL = “http://finance.yahoo.com/d/quotes.csv?s=\[SYMBOLS\]&f=\[ATTRIBUTES\]”

vArr = Application.Transpose(rnAR\_Dest.Resize(rnAR\_Dest.Rows.Count – 1, 1).Offset(1))

stCnx = Replace(YAHOO\_FINANCE\_URL, “\[SYMBOLS\]”, Replace(WorksheetFunction.Trim(Join(vArr)), ” “, “+”))

stCnx = Replace(stCnx, “\[ATTRIBUTES\]”, Worksheets(stAR\_ConfigSheetName).\[ar\_YFAttributes\])

AddQueryTable rnAR\_Table.Resize(UBound(vArr)), “URL;” & stCnx

End Sub

Notice that here we have variables defined at the top of this procedure and consequently their scope is limited to this procedure only. This means that we could have the same variable names defined in other procedures but those variables would not be related to these and would have completely different values.

Next notice that we have defined a constant. This is good practice, as it forces us to specify what the constant value is by naming the constant. I could have just used the value where I later use the constant, but then the question arises as to what is this value and where did it come from. Here I have named the value, YAHOO\_FINANCE\_URL, removing all doubt as to its purpose.

The next line is this:

`vArr = Application.Transpose(rnAR_Dest.Resize(rnAR_Dest.Rows.Count - 1, 1).Offset(1))`

and it deserves some explanation. Let me back up by saying that whenever we write or read multiple cells from a worksheet we should always try to do it in one go, rather than one cell at a time. The more cells involved the more important this is. Otherwise we pay a massive penalty in processing time. One of the best optimization techniques available is to replace code that loops through cell reads/writes and replace it with code that reads/writes all the cells at once. It can literally be hundreds to thousands of times faster.

Here we are interested in getting the list of all of the stock symbols in the first column of the ActiveRange. So how do we get them in one shot? We use something called a variant array. Notice that we defined vArr at the top of this procedure. A variant array is a special kind of variable that holds a list of values and it DOES NOT CARE what variable types those values are. This is important when retrieving data from a sheet because the data could be numbers, text, Boolean (True or False), etc. Variants are powerful, but they are much slower than other variable types, such as a Long for numeric data for example. However, in the case of retrieving or writing large chunks of data from/to a sheet the slight penalty of the variant is dwarfed by the massive increase in the speed of data transfer.

It’s very simple to retrieve range data (regardless of the size) into a variant array. All you do is:

`v = range`

where v is defined as a variant and range is any VBA reference to a worksheet range. And magically all of the values in that range are now in v. Note that v is not connected to the range. A change in any of v’s values does not propogate back to the range, and likewise a change to the range does not make it’s way to v all by itself. v will ALWAYS be a two-demensional array. The first dimension is the index of the rows, the second dimension is the index of the columns. So v(1,1) will refer to the value that came from the top left cell in the range. v(6,9) will hold the value that came from the cell in the range at row 6 and column 9.

For most circumstances this two-dimensional format is fine. But we are only retrieving one column of stock symbols. The procedure will still give us a two-dimensional array, with the column dimension being only 1 element wide. This is a shame because VBA has a wonderful function called Join that allows you in one step (no loop) to concatenate every element of an array into a string. You can even specify a custom string to delimit (go in-between) each element in the output string. The problem is that Join only works on single dimensioned arrays 🙁

But there’s always a way, right? We can use the Application.Transpose method on the 2-D array and presto we get a 1-D array. The rest of the line just specifies what range (the stock symbols) to grab.

The next two lines are:

`stCnx = Replace(YAHOO_FINANCE_URL, "[SYMBOLS]", Replace(WorksheetFunction.Trim(Join(vArr)), " ", "+"))`

`stCnx = Replace(stCnx, "[ATTRIBUTES]", Worksheets(stAR_ConfigSheetName).[ar_YFAttributes])`

Again a handful, but all we are doing here is replacing the monikers, \[SYMBOLS\] and \[ATTRIBUTES\] in the YAHOO\_FINANCE\_URL constant with the list of stock symbols (delimited by a plus sign) and the string of attributes.

In the final line of the procedure:

`AddQueryTable rnAR_Table.Resize(UBound(vArr)), "URL;" & stCnx`

we are running another subprocedure called, AddQueryTable and we are telling it where to place the new QueryTable and providing the connection string for the QueryTable, which in this case is the YF URL that we just built.

Nothing unusual happens in the AddQueryTable sub. It just deletes any existing AR related QueryTables and adds the new one according to the options in the configuration sheet.

The PostProcessActiveRange sub is interesting:

Private Sub PostProcessActiveRange()

If rnAR\_Dest.Columns.Count > 2 Then

Application.DisplayAlerts = False

rnAR\_Table.Resize(rnAR\_Dest.Rows.Count).TextToColumns Destination:=rnAR\_Table, DataType:=xlDelimited, Comma:=True

Application.DisplayAlerts = True

Worksheets(stAR\_ConfigSheetName).\[ar\_LocalTimeLastUpdate\] = Now

End If

End Sub

### Processing Yahoo Finance Output using Query Table & Text-Import Utility:

As mentioned before the data from YF comes back as a CSV file. The QueryTable dumps this into one column. If you were only retrieving one attribute for each stock this would be fine as is. However, two or more attributes is going to result in unwanted commas and multiple attribute values squished into the first column of the QueryTable output. Unfortunately this is poor design by Microsoft, especially when you consider that the QueryTable does not behave like this when it is retrieving SQL data or opening a Text file from disk. You can actually specify this operation to be a text file and it will properly spread the output over all of the columns. To do so, you specify the disk location as being the URL of the YF CSV file, but as Murphy would have it, it’s unbelievably slow and pops up a status dialog as it slowly retrieving the CSV. Using the URL instruction instead of the TEXT instruction at the beginning of the connection string is incredibly fast in comparison, but dumps all of the data into the first column.

So what to do? We’ll just employ Excel’s built-in TextToColumns capability and bam, our data is where we want it.

### Our finalized stock quotes fetcher worksheet should look like this:

![Excel Stock Quotes - Final workbook - Demo](https://chandoo.org/img/vba/final-stock-quotes-worksheet-demo.png)

### Download Excel Stock Quotes Macro:

[Click here to download the excel stock quotes macro workbook](https://img.chandoo.org/vba/activerange_yahoofinance_excelhero.com.xls)
. It will be much easier to follow this tutorial if you refer to the workbook.

### Final Thoughts on Excel Stock Quotes

**The ActiveRange technique is quite versatile.** It can be implemented with other data sources such as SQL, or even lookups to other Excel files, or websites.

In this example it provides a nice way to easily track whatever stocks you may have interest in and up to 84 different attributes of those stocks. You can enable and disable the activeness of the ActiveRange on the fly. You can set the AR to AutoRefresh the data at periods that you set or to not refresh at all.

This is a basic implementation. For example, changing the AutoRefresh setting will have no effect until a new QueryTable is built. That won’t happen until you also add or change a stock symbol or add or change an attribute. An easy enhancement would be to add a little code to the arConfig\_DEMO code module to respond to changes to the ar\_AutoRefresh named range cell.

Another enhancement would be to eliminate the slight flicker of the update by moving the QueryTable destination to the arConfig\_DEMO and then doing the TextToColumns with the destination set to the DEMO sheet. In an effort to simplify this tutorial I have left these easy enhancements as an exercise for you to implement.

### Have a question or doubt? Please Ask

Do you have any questions or doubts on the above technique? Have you used ActiveRange or similar implementations earlier? What is your experience? Please share your thoughts / questions using [comments](https://chandoo.org/wp/excel-stock-quotes/#commentform)
.

I read Chandoo.org regularly and will be monitoring the post for questions. But you can also reach me at my blog:

### Further References & Help on Excel Stock Quotes \[Added by Chandoo\]

*   [Fetching Stock Quotes using Research Pane](http://chandoo.org/wp/2008/06/24/get-stock-quotes-in-excel/)
    
*   [Stock Portfolio Tracker using Google Docs](http://chandoo.org/wp/2008/09/12/track-stock-mf-portfolio-google-docs/)
    
*   [QueryTable Object Model & Properties](http://msdn.microsoft.com/en-us/library/aa174288%28office.11%29.aspx)
    
*   [Using QueryTable to Generate Dynamic Reports](http://msdn.microsoft.com/en-us/library/aa188518%28office.10%29.aspx)
    
*   [Yahoo Finance API Documentation & Example](http://www.gummy-stuff.org/Yahoo-data.htm)
    

_**This is a guest post by Daniel Ferry of [Excel Hero](http://excelhero.com/blog)
.**_

Excel Hero is dedicated to expanding your notion of what is possible in MS Excel and to inspiring you to become an Excel Hero at your workplace. It has many articles and sample workbooks on advanced Excel development and advanced Excel charting.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [207 Comments](https://chandoo.org/wp/excel-stock-quotes/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-stock-quotes/#respond)
    
*   Tagged under [activerange](https://chandoo.org/wp/tag/activerange/)
    , [daniel ferry](https://chandoo.org/wp/tag/daniel-ferry/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [portfolio tracker](https://chandoo.org/wp/tag/portfolio-tracker/)
    , [querytable](https://chandoo.org/wp/tag/querytable/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [stock quotes](https://chandoo.org/wp/tag/stock-quotes/)
    , [stock quotes in excel](https://chandoo.org/wp/tag/stock-quotes-in-excel/)
    , [text import wizard](https://chandoo.org/wp/tag/text-import-wizard/)
    , [text to columns](https://chandoo.org/wp/tag/text-to-columns/)
    , [trackers](https://chandoo.org/wp/tag/trackers/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    , [yahoo finance](https://chandoo.org/wp/tag/yahoo-finance/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousCheck if two ranges of dates overlap \[Excel Formulas\]](https://chandoo.org/wp/date-overlap-formulas/)

[NextWin a Netbook – 10000 RSS ContestNext](https://chandoo.org/wp/10k-rss/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/excel-stock-quotes/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-stock-quotes/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-stock-quotes/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ