# Filter as you type [Quick VBA tutorial] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/filter-as-you-type-excel

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Filter as you type \[Quick VBA tutorial\]
=========================================

*   Last updated on December 10, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Filtering a list is a powerful & easy way to analyze data. But filtering requires a lot of clicks & typing. **Wouldn’t it be cool if Excel can filter as you type**, something like this:

![filter-as-you-type](https://chandoo.org/wp/wp-content/uploads/2015/08/filter-as-you-type.gif)

Let’s figure out how to do this using some really simple VBA code.

Filter as you type – VBA tutorial
---------------------------------

**Step 1: Set up a list with values you want to filter.**

To keep it simple, let’s assume your values are in an [Excel table](http://chandoo.org/wp/2009/09/10/data-tables/)
 named _States._

![filter-as-you-type-in-excel-example-data](https://chandoo.org/wp/wp-content/uploads/2015/08/filter-as-you-type-in-excel-example-data.png)

**Step 2: Insert a text box active-x control**

Go to developer tab and click on insert > text box (active-x) control.

![filter-as-you-type-insert-text-box-active-x-control](https://chandoo.org/wp/wp-content/uploads/2015/08/filter-as-you-type-insert-text-box-active-x-control.png)

Insert this control on your spreadsheet, preferably above the states table.

\[Related: [Introduction to Excel form controls – article](http://chandoo.org/wp/2011/03/30/form-controls/)\
, [podcast](http://chandoo.org/wp/2014/04/17/cp005-form-controls/)\
\]

**Step 3: Link text box to a blank cell.**

Click on properties button in developer tab and set linked cell property of text box to an empty cell in your worksheet. I set mine to **E4**.

![properties-window-textbox-activex-control](https://chandoo.org/wp/wp-content/uploads/2015/08/properties-window-textbox-activex-control.png)

**Step 4: Add CHANGE event to text box**

Right click on the text box and choose “view code”. This will take you to Visual Basic Editor (VBE) and creates an emtpy textbox1\_change() event.

_**Quick: What is an event?  
**_**Answer:** An Event is a macro (VBA code) that runs when a certain condition is satisfied. For example, textbox1\_change event runs whenever you change the textbox value (ie type something in to it, edit it or delete its contents).

We need to write VB code to filter our table (states), whenever user types something in to the text box. This code is _**just one line!**_

You can use below code or come up with your own version.

    ActiveSheet.ListObjects("states").Range.AutoFilter Field:=1, Criteria1:="*" & [e4] & "*", Operator:=xlFilterValues

Replace the words _states_ and _e4_ with your own table name & linked cell address.

That is all. Close VBE and return to Excel.

**Step 5: Play with filter as you type macro**

If you are in design mode, exit it by clicking on “design mode” button in developer tab.

Click on text box and type something. Your table gets filtered as you type, just like magic!

Want to filter multiple column table? Use this macro instead…
-------------------------------------------------------------

The above code works fine if you have just one column data. What if you need to filter a giant table with several columns? **Our reader Chris** thought about the problem and shared below approach.

1.  Create a new column at the end of your table that concatenates all column data. Something like this  
    \=CONCAT(Table3\[@\[first col\]:\[last col\]\]&” “)
2.  Now add Worksheet\_Change event (or Textbox\_change event) to monitor the input cell
3.  Apply filter on the concatenated column. Sample code below.

    Private Sub Worksheet_Change(ByVal Target As Range)
        Dim KeyCells As Range
        Set KeyCells = Range("search_string")
        
        If Not Application.Intersect(KeyCells, Range(Target.Address)) _
               Is Nothing Then
                FastFilter (KeyCells.Value)
        End If
    End Sub
    
    
    Sub FastFilter(sch As String)
        
        Dim lo As ListObject
        Set lo = ActiveSheet.ListObjects(1)
        lastcol = lo.ListColumns.Count
        
        If lo.AutoFilter.FilterMode Then
            lo.AutoFilter.ShowAllData
            lo.Range.AutoFilter Field:=lastcol, Criteria1:= _
                Array("*" + sch + "*"), Operator:=xlFilterValues
            Else
            lo.Range.AutoFilter Field:=lastcol, Criteria1:= _
                Array("*" + sch + "*"), Operator:=xlFilterValues
            End If
        Range("search_string").Select
    End Sub
    

### Filter on any column – VBA Trick – Explanation video

Watch below video to understand how “filter on any column with VBA” trick works. You can watch it here or on **[my YouTube Channel](https://www.youtube.com/watch?v=a_ylV6ijUc4&feature=youtu.be)
**.

### Download filter as you type example macro

**[Please click here to download filter as you type example workbook](https://chandoo.org/wp/wp-content/uploads/2015/08/filter-as-you-type.xlsm)
**. As a bonus, the download workbook as code to clear / reset filters too. Examine the code to learn more.

**[Click here to download the FastFilter code](https://chandoo.org/wp/wp-content/uploads/2019/12/FastFilter2.xlsm)
 example file**.

### More awesome ways to filter your data

If you are often filtering your data, you will find below tips handy:

*   [Filter a table by combination of values quickly](http://chandoo.org/wp/2015/07/15/filter-a-table-by-combination-of-values/)
    
*   [How to use advanced filters to extract values that meet multiple criteria in one go](http://chandoo.org/wp/2011/10/10/how-to-use-advanced-filters/)
    
*   [Using report filters in Excel pivot tables](http://chandoo.org/wp/2011/04/20/pivot-table-report-filters/)
    
*   [Slicers – filters for the new generation – how to use them?](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
    
*   [Filter odd or even rows only](http://chandoo.org/wp/2011/01/05/how-to-filter-odd-or-even-rows-only-quick-tips/)
    

### Awesome as you learn:

There is no doubt that you will get awesome at your work by learning new & powerful ways to do it.

_**If you want to learn how to use VBA to automate your work, please consider our online VBA classes.**_ This comprehensive program teaches VBA macros from scratch to advanced level thru step-by-step video tutorials.

[**Click here to know more about the VBA classes and enroll today**](http://chandoo.org/wp/vba-classes/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

*   [95 Comments](https://chandoo.org/wp/filter-as-you-type-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/filter-as-you-type-excel/#respond)
    
*   Tagged under [awesome august](https://chandoo.org/wp/tag/awesome-august/)
    , [data filters](https://chandoo.org/wp/tag/data-filters/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousIntroduction to Power BI – What is it, how to get it, how to create reports with Power BI and how to publish them?](https://chandoo.org/wp/powerbi-introduction/)

[NextCome and learn from me in London – April 2020Next](https://chandoo.org/wp/come-and-learn-from-me-in-london-april-2020/)

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introducing-advanced-excel-training-v1.png)](https://chandoo.org/wp/excel-school-program/)

Chandoo is an awesome teacher

__________ Rated 5 out of 5

_– Jason_

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Complete Introduction to Power BI](https://chandoo.org/wp/powerbi-introduction/)

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
    

### 95 Responses to “Filter as you type \[Quick VBA tutorial\]”

1.  ![](https://secure.gravatar.com/avatar/3b8808041bfeb6bb3553e4879272d1ffc525742f94644e1c034b14eeeb6ae453?s=64&d=mm&r=g) Rahul says:
    
    [August 22, 2015 at 9:03 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1028252)
    
    I am blank in Macros, tried copying the code. But got Run-time error:9. Please help and also suggest some resources to grab the basics of Macros (for beginners and intermediate).
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1028252)
    
2.  ![](https://secure.gravatar.com/avatar/48d786796db168513b93ac7508b785a57488ee3e8801bd8cc77b0aec92b8bdcc?s=64&d=mm&r=g) Jitendra sharma says:
    
    [August 22, 2015 at 10:31 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1028282)
    
    Dear Chandoo,
    
    Please help me.
    
    I want to know how many times visit in a company within a week & within a day.
    
    DATE Visiter Name  
    01-Aug-15 JVS  
    01-Aug-15 FAZE  
    01-Aug-15 TREND  
    01-Aug-15 SHAHI  
    03-Aug-15 WAZIR  
    03-Aug-15 JVS  
    03-Aug-15 CELLO  
    03-Aug-15 HANUNG  
    03-Aug-15 WAZIR  
    04-Aug-15 TRIDENT  
    04-Aug-15 ANIKET  
    05-Aug-15 JVS  
    05-Aug-15 DESIGNCO  
    05-Aug-15 ABHITEX  
    05-Aug-15 JVS  
    05-Aug-15 CELLO  
    05-Aug-15 SHAHI  
    06-Aug-15 JEWEL  
    06-Aug-15 JEWEL  
    07-Aug-15 TREND  
    07-Aug-15 NAVNEET  
    07-Aug-15 KAPOOR  
    07-Aug-15 TREND  
    08-Aug-15 RAMESH  
    07-Aug-15 ALOK  
    07-Aug-15 NAVNEET  
    08-Aug-15 FAZE  
    08-Aug-15 SHAHI  
    08-Aug-15 LUXOR  
    08-Aug-15 WELSPUN  
    08-Aug-15 ABHI
    
    I want to count.
    
    It means "cello" visiter visit in office 2 times with 1st to 8th Aug-15.
    
    Cello 2
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1028282)
    
    *   ![](https://secure.gravatar.com/avatar/39deb32cf19ef92c7c7eb12364ba114d47a21ff6f34272b2f09e8460e0cfbac9?s=64&d=mm&r=g) Kuldeep Mishra says:
        
        [August 24, 2015 at 5:58 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1029765)
        
        \=SUMPRODUCT(--($A$2:$A$32<=J4)\*($B$2:$B$32="CELLO"))
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1029765)
        
        *   ![](https://secure.gravatar.com/avatar/48d786796db168513b93ac7508b785a57488ee3e8801bd8cc77b0aec92b8bdcc?s=64&d=mm&r=g) Jitendra sharma says:
            
            [August 24, 2015 at 1:26 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030111)
            
            Dear Kuldeep,
            
            I am not understand why u are using "J4" pls clarify the same.
            
            Thanks  
            Jitendra
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030111)
            
            *   ![](https://secure.gravatar.com/avatar/39deb32cf19ef92c7c7eb12364ba114d47a21ff6f34272b2f09e8460e0cfbac9?s=64&d=mm&r=g) Kuldeep Mishra says:
                
                [August 24, 2015 at 3:30 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030221)
                
                j4 is the cell reference you just need to put date instead CELL REFERENCE.
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030221)
                
                *   ![](https://secure.gravatar.com/avatar/3d2b13554b6efc94f1ec6b64c82a97d2fbdc6788aa5788f5c93458261fff51a6?s=64&d=mm&r=g) PRADEE PRAJAPATI says:
                    
                    [January 10, 2016 at 4:50 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1118391)
                    
                    Hi Kuldeep,  
                    I am getting this output "08-Aug-15", "-3" when i use this formula- =SUMPRODUCT(-($I$3:$I$33<=I35)\*($J$3:$J$33="SHAHI"))
                    
    *   ![](https://secure.gravatar.com/avatar/729770f82f83d7013f8d8a13a388c183a8593f2839977494e303300e54409dcf?s=64&d=mm&r=g) Hamid MilaniNia says:
        
        [August 26, 2019 at 4:10 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681676)
        
        Have you tried to utilize PowerQuery utilizing converting the range into a table then bring it in Power Query, Split the columns by selecting the first 9 characters from left, rename the columns to Dates, Name then bring the table back into Excel, Insert a Slicer select name as a filter. Simply click on the name and the table displays only days which the Visits where made.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681676)
        
    *   ![](https://secure.gravatar.com/avatar/212d47b4e0bba92111dc88444253c1497e07f388909d9ea00c8d4e6131180eb9?s=64&d=mm&r=g) Power by PK says:
        
        [August 27, 2019 at 5:24 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681892)
        
        Hi,  
        Jitendra Ji
        
        Simple  
        If Date and Name (B2:B20) in separate column..
        
        Type a visitor name (D2) in outside of table and use formula  
        \=countif(B2:B20,D2)
        
        Reply if formula work as your think.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681892)
        
3.  ![](https://secure.gravatar.com/avatar/31c17c564141157ed65b8dfa40e7669fbbfdb639722352f2b1f3d38a12b4e6d7?s=64&d=mm&r=g) Chris O'Neill says:
    
    [August 22, 2015 at 9:21 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1028632)
    
    Chandoo,
    
    This is a great tip. I modified it to search all columns in a data table and filter if any column shows the value. I was using conditional color coding but this is much nicer. Let me know if you want the sample sheet. - Chris
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1028632)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 24, 2015 at 3:37 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030230)
        
        Hi Chris,
        
        That is lovely. Please post the VBA code in comments or email me at [chandoo.d@gmail.com](mailto:chandoo.d@gmail.com)
        . I would like to learn from it and share it with rest of the readers.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030230)
        
        *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
            
            [December 11, 2015 at 1:15 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099958)
            
            I sent you the model - there is no VBA code. I use only your code for the filter as you type. I created a formula means to create a hidden column where it searches all the other columns. Brute force but works like a top. I also ended up bailing on the filter as you go when the database got too big. Now I just have a running total and click that box to filter once. Please let me know if you have any questions or concerns. Great site, nice people in your forum. happy to share what little I Know.
            
            Chris
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099958)
            
    *   ![](https://secure.gravatar.com/avatar/ff5b5aab0748722dd614cb6bc382f931038607490aa434887cca3269e579f4a3?s=64&d=mm&r=g) Chris says:
        
        [March 31, 2017 at 7:00 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1428320)
        
        Chris,  
        I know this was a long time back, but would you happen to know the formula you used to search the entire table? This is something I'm trying to do, but to no avail right now.
        
        Thanks,  
        Chris
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1428320)
        
        *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
             says:
            
            [April 6, 2017 at 5:07 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433014)
            
            Chris,
            
            I detailed the formula above in an article. Let me know if you have any questions or concerns.
            
            Chris O.
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433014)
            
            *   ![](https://secure.gravatar.com/avatar/ff5b5aab0748722dd614cb6bc382f931038607490aa434887cca3269e579f4a3?s=64&d=mm&r=g) Chris says:
                
                [April 6, 2017 at 8:58 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433151)
                
                Maybe I'm just missing it, but can you please provide the article? Thanks in advance!  
                \-Chris
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433151)
                
    *   ![](https://secure.gravatar.com/avatar/5588c7126a432d778cd6ce63c21aff8ae15d14493babe7fcb674103e21ddf829?s=64&d=mm&r=g) Bala says:
        
        [December 5, 2017 at 7:22 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1526225)
        
        Chris can you share the old sheet where you modified using the hidden column one.Can mail to [balam1986@gmail.com](mailto:balam1986@gmail.com)
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1526225)
        
        *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
             says:
            
            [December 5, 2017 at 4:37 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1526276)
            
            Bala,
            
            I resent the link. If you just click my name you go to the share site. I would delete your email now that you know how to contact me. - Chris
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1526276)
            
4.  ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) slsuser says:
    
    [August 24, 2015 at 2:02 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030140)
    
    This is great but seems to only filter on the the starting characters in the strings.  
    Can the code be changed to a sequential search to show the results where the combinations entered appear anywhere within the string?  
    For example, using the original data, if I type in "or" then florida and georgia would display in the list.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030140)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 24, 2015 at 2:31 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030169)
        
        @Slsuer:
        
        Can you double check? The filtering should work for occurrence anywhere.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030169)
        
5.  ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) slsuser says:
    
    [August 24, 2015 at 3:09 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030198)
    
    Thanks for your reply....  
    Apologies, it may be working.  
    Having issues with Excel right now and can only open older version. Will check next weekend upon arrival of new pc.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030198)
    
6.  ![](https://secure.gravatar.com/avatar/84edea8410b20aef8483c89f1b8dc022fbead54795b21760bd3c601af7790214?s=64&d=mm&r=g) Tim says:
    
    [August 24, 2015 at 3:34 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030226)
    
    Chandoo,
    
    This is a great method. I have one question though.
    
    Say I want to filter by column "region" in the "states" table how would I go about doing that? I tried replacing "states" with the column name "states\[\[#All\],\[Region\]\]" and "states\[Region\]", but to no avail.
    
    Thank you!  
    Tim
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030226)
    
7.  ![](https://secure.gravatar.com/avatar/a4ebc8a115f7f37105be665d07bd3e32e0ba492d538545b7d68dd4e6c8b79419?s=64&d=mm&r=g) Lloyd says:
    
    [August 24, 2015 at 9:52 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030448)
    
    Awesome as always,  
    I was thinking about trying to us something along these lines to replace a slicer (for a very long list) in a pivot table. My initial thought were;
    
    ActiveSheet.PivotTables("PivotTable1").PivotFields("Items").Range.AutoFilter Field:=1, Criteria1:="\*" & \[a1\] & "\*", Operator:=xlFilterValues
    
    But this failed abysmally with a 438 error.
    
    Any thoughts on if this is possible and the correct syntax to make it work?
    
    Thanks again
    
    Lloyd
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1030448)
    
8.  ![](https://secure.gravatar.com/avatar/e99ce6ee7341dd7bf566b2a59dc72e37e2296518dc3590472970ff0d9370aec4?s=64&d=mm&r=g) Rick says:
    
    [August 26, 2015 at 2:49 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031347)
    
    Chandoo,
    
    Excellent example. You state "To keep it simple, let’s assume your values are in an Excel table". Must the data be in an Excel table? I can't seem to make it work otherwise.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031347)
    
9.  ![](https://secure.gravatar.com/avatar/1714daa33c832905bd87071f5d32c7c994b1204baa79328f30f60fa9ae502e64?s=64&d=mm&r=g) kasawubu says:
    
    [August 26, 2015 at 8:24 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031477)
    
    Dear Chandoo,
    
    this is a great tip.
    
    Tried to use it in an example on my own (Excel 2013).  
    Replaced name and linked cell, but always get vba error 9 'Subscript out of range'.
    
    Tried different things already - no success.  
    How can I make it work? Thanks.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031477)
    
    *   ![](https://secure.gravatar.com/avatar/5e851c32c646432d800c435933233effbb5b6320f323a3444c0ef357e2ea92ad?s=64&d=mm&r=g) John says:
        
        [August 26, 2015 at 1:04 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031575)
        
        Did you convert your data into a table? If you created a named range instead you will likely get Error 9.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031575)
        
        *   ![](https://secure.gravatar.com/avatar/21a6176cc46c97a015e4af04c6de0177de5e1b7e86e3264dcafef0f37e3a185b?s=64&d=mm&r=g) kasawubu says:
            
            [August 27, 2015 at 3:34 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031832)
            
            Yes, I used a table, but got the error nevertheless.
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031832)
            
            *   ![](https://secure.gravatar.com/avatar/1714daa33c832905bd87071f5d32c7c994b1204baa79328f30f60fa9ae502e64?s=64&d=mm&r=g) kasawubumail says:
                
                [August 27, 2015 at 8:54 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031937)
                
                Got it: made a mistake by not using the correct table Name.
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031937)
                
10.  [Filter as you type \[Quick VBA tutorial\] | | CareWare](https://careware.wordpress.com/2015/08/26/filter-as-you-type-quick-vba-tutorial/)
     says:
    
    [August 26, 2015 at 2:23 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031601)
    
    \[…\] [http://chandoo.org/wp/2015/08/22/filter-as-you-type-excel/?utm\_source=feedburner&utm\_medium=emai&#8230](http://chandoo.org/wp/2015/08/22/filter-as-you-type-excel/?utm_source=feedburner&utm_medium=emai&#8230)
    ; \[…\]
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1031601)
    
11.  ![](https://secure.gravatar.com/avatar/97a4fc73bee4780fce5ed7df541ce04710645b42c1d87642daabfd760a752230?s=64&d=mm&r=g) nikhil says:
    
    [August 30, 2015 at 6:53 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1033626)
    
    Hey chandoo, could please explain this because I am getting run error 9 .
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1033626)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 31, 2015 at 12:13 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1033700)
        
        @Nikhil
        
        Run Error 9 is usually because you have used a variable outside its defined range or have tried to use a variable which hasn't been defined  
        eg: Setting an Integer variable to more than 32,767  
        or trying to use a variable which hasn't been defined  
        eg: defining a workbook as a name and then referencing the work book when it isn't opened
        
        Can you post the file or VBA Code in question and highlight where it is failing?
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1033700)
        
        *   ![](https://secure.gravatar.com/avatar/97a4fc73bee4780fce5ed7df541ce04710645b42c1d87642daabfd760a752230?s=64&d=mm&r=g) nikhil says:
            
            [September 11, 2015 at 2:30 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1042650)
            
            @hui  
            Thanks for your reply and I understood my problem... I have one requirement. The requirement is that I want the same filter as you type but I want to filter as you type number is that possible?
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1042650)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [September 14, 2015 at 2:22 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1044634)
                
                Please post the question and file in the Chandoo.org forums  
                [http://chandoo.org/forum/](http://chandoo.org/forum/)
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1044634)
                
12.  ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) slsuser says:
    
    [September 11, 2015 at 2:46 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1042970)
    
    to Nikhil...  
    To me it appears that the numeric as not filtering because they are numeric. I entered a number as 65432 and with a leading ' (single quote) to cause the number to be entered as text and the filter works.  
    that would be a lot of effort.  
    I then formatted the table as text instead of general. New numeric entries added to the end of the table were treated as text and filtered properly.  
    I see the bets way would be to convert all entries to text in the VBA but I haven't figured that out. Formatting the E4 value as chr fails on text. Perhaps need to inspect the value to see if numeric and then process differently if numeric?? not sure but this is food for thought.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1042970)
    
    *   ![](https://secure.gravatar.com/avatar/97a4fc73bee4780fce5ed7df541ce04710645b42c1d87642daabfd760a752230?s=64&d=mm&r=g) nikhil says:
        
        [September 12, 2015 at 12:49 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1043212)
        
        @ slsuser  
        Thanks for your for reply  
        I already tried converting numeric to text by using both the methods as u mentioned but still the filter is not working????. Could please share the code wic u used it  
        Thanks in advance
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1043212)
        
    *   ![](https://secure.gravatar.com/avatar/97a4fc73bee4780fce5ed7df541ce04710645b42c1d87642daabfd760a752230?s=64&d=mm&r=g) nikhil says:
        
        [September 12, 2015 at 12:50 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1043213)
        
        @ slsuser  
        Thanks for your for reply  
        I already tried converting numeric to text by using both the methods as u mentioned but still the filter is not working????. Could please share the code wic u used it  
        Thanks in advance
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1043213)
        
        *   ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) slsuser says:
            
            [September 13, 2015 at 2:02 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1044128)
            
            Nikhil,  
            No coding is required. You must format the column as TEXT before inputting the values. The table in the example spreadsheet (filter-as-you-type.xlsm) is formatted as "General" so numbers are treated as numbers and alpha is treated as text which is why the filter fails on only numeric values.  
            Simply select your entire table and change the format to text. All NEW entries (at the bottom of the table) will be formatted as text.  
            Existing entries will NOT automatically change to text. If there are not to many you can go to each cell and press F2 and enter and the number should change to Text format.  
            I have tried this and it works without coding.  
            Note if you plan to perform any numeric functions you will need to convert back to number format in your formulas.
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1044128)
            
            *   ![](https://secure.gravatar.com/avatar/97a4fc73bee4780fce5ed7df541ce04710645b42c1d87642daabfd760a752230?s=64&d=mm&r=g) nikhil says:
                
                [September 18, 2015 at 2:32 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1046579)
                
                Slsuser,  
                Thanks for the tips its working
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1046579)
                
13.  ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/folderview?id=0B3NPE3t4gC36WDMxWnpSS1EtbkE&usp=sharing)
     says:
    
    [September 13, 2015 at 10:12 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1044273)
    
    Hey, I liked the search but wanted to be able to have all columns searchable.
    
    1.) I use data table.  
    2.) I created column that does a find of the string against each of the columns. (I hide that column normally)  
    3.) I use Chandoo's code to set that search column to 1 which is the value given when any of the other columns find the string or any part of the string.
    
    I posted a sample doc to google here:
    
    [https://drive.google.com/folderview?id=0B3NPE3t4gC36WDMxWnpSS1EtbkE&usp=sharing](https://drive.google.com/folderview?id=0B3NPE3t4gC36WDMxWnpSS1EtbkE&usp=sharing)
    
    Hope this helps someone as much as the tip helped me.
    
    Chris
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1044273)
    
    *   ![](https://secure.gravatar.com/avatar/97a4fc73bee4780fce5ed7df541ce04710645b42c1d87642daabfd760a752230?s=64&d=mm&r=g) nikhil says:
        
        [September 18, 2015 at 2:48 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1046590)
        
        Hey thanks for sharing the file it's quiet interesting.I just need to understand how that if nesting work as filter
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1046590)
        
        *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris says:
            
            [September 18, 2015 at 3:01 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1046599)
            
            N,
            
            Okay - here is how the nesting works.  
            Find looks for the string inside a column  
            If it finds no string an error is thrown  
            I use iferror to trap the error and make a 1 if no error exists and zero if it does exist  
            Thus the string comes from the dialog box and creates a 1 for each column that contains the text in the dialog box  
            I add all the 1 's together and then creat a formula that says if the total of the 1 's. Is greater than zero put. 1 or true in the cell to the left
            
            Then I use the filter aa you type but filter on 1 or true.
            
            I hope this helps. I use this for over 600 paragraphs across 10 columns and it works well.. If a little slow....
            
            Chris
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1046599)
            
    *   ![](https://secure.gravatar.com/avatar/00c94c3ac84b30ee5710ad019405165514c0224ec659d11547fa5e107a893b8d?s=64&d=mm&r=g) Ron says:
        
        [November 28, 2017 at 9:11 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525088)
        
        Hi Chris,
        
        I would be very happy if you could please post your sample doc to Google drive once again. I am looking for exactly what you are describing.
        
        Thks.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525088)
        
        *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
            
            [November 29, 2017 at 1:57 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525246)
            
            Hi Ron,
            
            Per your request, I am reposting the link to the article and model I wrote.
            
            [https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
            
            Since then, I have moved on to different approaches to the problem as this solution starts to slow down as the database grows. If you are good with VBA I can share some functions and subroutines that filter tables quicker than this way. - Chris O
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525246)
            
            *   ![](https://secure.gravatar.com/avatar/00c94c3ac84b30ee5710ad019405165514c0224ec659d11547fa5e107a893b8d?s=64&d=mm&r=g) Ron says:
                
                [November 29, 2017 at 4:28 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525273)
                
                Chris,
                
                First impression - very good. I dumped 60,000 records that have 23 columns (1.4 million cells). Yes, it currently only checks the first 5 columns, but it is very fast. No - Unfortunately, I am not good with VBA.
                
                This does serve a purpose for me. However, what I am ideally looking for is something where I can have the ability to do multiple search & filtering by column across the board.
                
                Can this be more or less easily modified to adapt to what I am looking for ?
                
                Many thanks for the quick posting Chris. I took a chance that you would respond after your original post from a couple of year's back.
                
                Ron
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525273)
                
                *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
                     says:
                    
                    [November 29, 2017 at 5:30 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525276)
                    
                    You probably have a decent processor and ample memory. I am happy you get value from this.
                    
                    You can modify it easily to check all the columns. Look at the formula in the first column... replace the text "column2" with the exact text of your first data column... then replace column5 with the exact name of your last column. I like to create a column on the end of my table called "LastColumn" then hide it which means the formula will always work if I use the same names.
                    
                    \=NOT(ISERROR(MATCH("\*"&IF(ISBLANK(search\_string),RAND(),search\_string)&"\*",TEXT(tb\_main\[@\[Column2\]:\[Column5\]\],"0.00000"),0)))
                    
                *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
                     says:
                    
                    [November 29, 2017 at 7:52 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525289)
                    
                    I updated the file to reflect the changes. A few tips and tricks:  
                    1.) Cope and paste the formula to notepad, clear the whole search column and paste it in the first cell which will create a clean uniform set of searches.  
                    2.) Note that you will get a cell error warning if your last column is full of blank cells. This is not an issue and will not effect anything but the aesthetic of the warning green triangle.
                    
                    Chris O
                    
                *   ![](https://secure.gravatar.com/avatar/00c94c3ac84b30ee5710ad019405165514c0224ec659d11547fa5e107a893b8d?s=64&d=mm&r=g) Ron says:
                    
                    [November 30, 2017 at 4:04 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525436)
                    
                    Thanks Chris !
                    
14.  ![](https://secure.gravatar.com/avatar/d7e8bc412744aac65575b4a36af53d962e1fe82def204c18b00b7a32a23821cf?s=64&d=mm&r=g) JM says:
    
    [December 10, 2015 at 7:55 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099577)
    
    Hello.. what if i want to filter a multi column table? because it only filters the first column of a table? how could refer to the other column? thanks
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099577)
    
    *   ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) slsuser says:
        
        [December 10, 2015 at 5:49 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099757)
        
        JM, see Chris O'Neill comment and example on 9/13/2015. I have not tried it myself but the logic appears proper. Let us know if that works for multi columns in your environment.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099757)
        
    *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
        
        [December 11, 2015 at 12:52 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099945)
        
        I will send Chandoo the model and let him break it down for you. Essentially, I am doing a boolean search using a formula in one cell. Then I am applying Chandoo's search on the on column. So col1 = yes or no, column 2 = yes or now, column three yes or no. If yes equals 1 and no equals two then the total would be zero if nothing is found and more than zero is something in any column is found.
        
        Chris  
        [conw88@gmail.com](mailto:conw88@gmail.com)
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1099945)
        
15.  ![](https://secure.gravatar.com/avatar/093e25e60997102ef6559d425310c235e9983d566a64449170be0f46b9df8232?s=64&d=mm&r=g) sherif says:
    
    [June 20, 2016 at 9:07 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1217296)
    
    i have create this filter as you type file for my 10 field table.
    
    it is working fine but i have numeric field as well, which is not getting  
    filter with this vba code. can you provide vba code of numeric as well.
    
    thanks in advance.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1217296)
    
    *   ![](https://secure.gravatar.com/avatar/093e25e60997102ef6559d425310c235e9983d566a64449170be0f46b9df8232?s=64&d=mm&r=g) sherif says:
        
        [June 20, 2016 at 9:26 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1217300)
        
        i wanted to tell you one thing my data is copied from word to excel,
        
        even if you converted in to text. this format is not picking up.  
        then i have double click on each cell. after double click it is getting convert to text and left side corner i am getting a small green dot.
        
        if i click on it, it is giving an option convert as number.
        
        it is very difficult to each on cell because i have almost 9000 rows.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1217300)
        
16.  ![](https://secure.gravatar.com/avatar/ead0b1d79cba0f445a9cfb3cfa00ea429bda495689f38e7adfa9c60592e9f0a9?s=64&d=mm&r=g) Jdb says:
    
    [July 11, 2016 at 5:28 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1230186)
    
    I changed the field to 4, which allows it to search all the columns in my table. However, I have duplicate values that I want to show when searched, but for some reason the search narrows it down to only one response.
    
    Is there a way to get it to show all duplicate values?
    
    The code I have for my table is this:
    
    ActiveSheet.ListObjects("RegulationSearch\_tbl").Range.AutoFilter Field:=4, Criteria1:="\*" & \[H1\] & "\*", Operator:=xlFilterValues
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1230186)
    
17.  ![](https://secure.gravatar.com/avatar/a41bb1e8ccb146326fc13c637c02c9891f67ea32ff5aaf34e1da05a3373989e7?s=64&d=mm&r=g) Brian Skinnell says:
    
    [August 5, 2016 at 4:12 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1246654)
    
    Chandoo,  
    Let first start off by saying that I love all of the AWESOME content that you provide to us Excel-nerds!! Keep up the great work and I hope that you're enjoying New Zealand.
    
    Second, I have a question regarding on this particular subject. I have created a spreadsheet that I can filter on 7 different colums and a button to clear all text box filters and it works AWESOME!! However, one of the columns does may not have a value on every row and when I clear (i.e. backspace) what I've typed in the text box filter for that particular column, it does not redisplay the rows with no value. The good news is that the button that I created solves the issue but was wondering if there is a fix for this?
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1246654)
    
18.  ![](https://secure.gravatar.com/avatar/e8552497d6b9e29dbd1fab4363e24b41a8313e57ee0c4dc88a33bcd6bada64ee?s=64&d=mm&r=g) Mamun says:
    
    [August 16, 2016 at 9:37 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1256626)
    
    I think something, I am missing in" Filter as you type \[Quick VBA tutorial\]" . Because I am tried many times in my own project but I faild. Will you detail description on Filter as you type \[Quick VBA tutorial\].
    
    Thanking You.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1256626)
    
19.  ![](https://secure.gravatar.com/avatar/8f6b796c8aa0ec0ad46f7870b9dfa4bd2a4c11d02220029cce34e85c6bc86b26?s=64&d=mm&r=g) wobie says:
    
    [September 11, 2016 at 2:20 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1282160)
    
    This does not apply with integers/numbers? any problem with it. It cant search for numbers. Pls help
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1282160)
    
20.  ![](https://secure.gravatar.com/avatar/7d65ab26fa5017855157c56fa9d597665998f4db966a1c4332cc8436a5f46124?s=64&d=mm&r=g) Thuy An says:
    
    [October 5, 2016 at 3:00 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1304126)
    
    How can I change the code to allow it to search in all columns of the table??? Thank you so much!
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1304126)
    
21.  ![](https://secure.gravatar.com/avatar/ff5b5aab0748722dd614cb6bc382f931038607490aa434887cca3269e579f4a3?s=64&d=mm&r=g) Chris says:
    
    [March 31, 2017 at 9:17 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1428388)
    
    Chandoo!  
    This is an excellent bit of code, my only quandary is that I'd like the exact same functionality to search my entire table. So far everything works as it should to search the first column.
    
    The code I'm using is:
    
    ActiveSheet.ListObjects("Table3").Range.AutoFilter Field:=1, Criteria1:="\*" & \[ac3\] & "\*", Operator:=xlFilterValues
    
    If between the time you originally created this post(2015) and now, you've figured out a simple way to search the entire table using the same methodology, I'd absolutely love to see it.
    
    Thanks in advance for all of your Excel computing superpowers!
    
    Chris
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1428388)
    
    *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
        
        [April 3, 2017 at 12:13 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1429776)
        
        The method above does search the entire table. You just do the work in the first column and then filter on true. The problem you have is that you can only filter on one column at a time. So you need that one column to answer the question, "Did my search have a result anywhere on this row?"
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1429776)
        
        *   ![](https://secure.gravatar.com/avatar/ff5b5aab0748722dd614cb6bc382f931038607490aa434887cca3269e579f4a3?s=64&d=mm&r=g) Chris says:
            
            [April 6, 2017 at 9:01 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433152)
            
            Sorry Chris but I'm quite green in VBA. If you could explain how to formulate that loop based on what I've already got together (ActiveSheet.ListObjects("Table3").Range.AutoFilter Field:=1, Criteria1:="\*" & \[ac3\] & "\*", Operator:=xlFilterValues), it would be a huge help.
            
            Regards,  
            Chris
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433152)
            
            *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
                 says:
                
                [April 6, 2017 at 9:54 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433169)
                
                Does the filtering part work for you? Does it filter at least one column? If you have that working you only need to add a column in the front and use the formula part to get the true false. This is more a formula thing. - Chris
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433169)
                
                *   ![](https://secure.gravatar.com/avatar/ff5b5aab0748722dd614cb6bc382f931038607490aa434887cca3269e579f4a3?s=64&d=mm&r=g) Chris says:
                    
                    [April 6, 2017 at 9:56 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433171)
                    
                    Chris,  
                    Yes, the filter for the first column works like a charm, no problems there. I'd just like to make it filter all other columns when I enter specific criteria.
                    
                    Thanks,  
                    Chris
                    
                *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
                     says:
                    
                    [April 7, 2017 at 10:50 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1433542)
                    
                    Chris,
                    
                    I looked at the code last night. Allow me to explain. Your vba is this:
                    
                    ActiveSheet.ListObjects("states").Range.AutoFilter Field:=1, \_  
                    Criteria1:="\*" & \[e4\] & "\*", Operator:=xlFilterValues|
                    
                    That sets the pull down in the filter to \*\*. You cannot apply the filter to all columns for two reasons: First, we can safely assume E4 is one value and that it occurs in only one of the columns. It is unlikley the value in E4 appears in multiple locations on the same row. Second, a filter can only be applied to one column filter at a time. So you cannot get what you want with the filter as you type sample.
                    
                    The key line of code I shared with you is this:
                    
                    ActiveSheet.ListObjects("tb\_activity").Range.AutoFilter Field:=1, Criteria1:="TRUE"
                    
                    This filters the first column to TRUE. So then the question becomes "Can the first column do some work and check for our value in all the columns resulting in one of two states "true" or "false"? The answer is yes. That is why I use the first column not for data but for checking any and all cells for the search\_string.
                    
                    The pseudo code works like this for the formula: Does "dog" appear in column2? No? How about column3? No? How about column4? yes - great! show TRUE and I will filter on that. Then my vba code above will filter all rows with the word TRUE in column1.
                    
                    Does that make sense to you? If yes, you need to do the following:
                    
                    1\. Add a column in your SS for the magic formula and modify it so it reflects the correct names of a.) The cell reference where you text box in linked b.) The column names or headings of the 2nd and last columns in your table.
                    
                    2\. Swap the code above in your Workbook Module for my code. I highly recommend you create a new copy of your model so you can go back if you mess it up.
                    
                    If you want to, change all the data to something else and email or post your model and I will try to make the change for you.
                    
                    Chris O
                    
22.  ![](https://secure.gravatar.com/avatar/5549f47c1a16be2d702b4d8d720fdf65d653ce5177cc90415573986e4de21a6b?s=64&d=mm&r=g) Wayne says:
    
    [May 4, 2017 at 2:28 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1442427)
    
    Your example is exactly what I wish to achieve but I have tried to follow the instructions exactly but cannot make it work.
    
    There is some bits missing in the code because of the width of the page but have managed to pick up the remaining letters...
    
    I cant tell if the end of the code is ...Operator:=x1FilterValues, ...Operator:=xIFilterValues or ...Operator:=x|FilterValues... so this probably has an impact
    
    Once I set the table I cannot name it... excel chooses the name which is usually Table?#... even if I name the range before I set the table it renames it to Table?#
    
    With the link and the code set... when I type anything into the linked cell... nothing appears in the textbox until I press enter... and then when I press enter... what I get in my text box is whatever I have typed into the linked cell.
    
    I am not a programmer of any form, I am simply following the instruction in the blog and I apologise for being a numpty but I work in Excel 10 and if you could send me a sample spreadsheet, this will help me out immensely.
    
    Thank you so kindly
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1442427)
    
23.  ![](https://secure.gravatar.com/avatar/eb459b1e8c73e36a7670637045d5289097c11880b6b4a650e6dfbdf155f7e819?s=64&d=mm&r=g) Katie says:
    
    [September 20, 2017 at 5:31 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1511079)
    
    Hi! Love this code and it works great. However is there a way I can get it to also search two words with a combination "AND" filter?
    
    Thanks!
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1511079)
    
24.  ![](https://secure.gravatar.com/avatar/e9e91db4161684dadc5b2906feeae45b47b1376c910e6e8b6774a0f47f636dee?s=64&d=mm&r=g) Wilber says:
    
    [October 23, 2017 at 7:50 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1518056)
    
    Hi Chandoo,  
    can we use this also on pivot table? i tried, but failed.
    
    Thanks  
    Wilber
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1518056)
    
25.  ![](https://secure.gravatar.com/avatar/66894c82bfc28e79cce6dfc0642be4066e5cac8fe815a27c9998a731e6513be3?s=64&d=mm&r=g) rena campbell says:
    
    [November 29, 2017 at 5:55 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525280)
    
    your above code is not working it is returning error 9 thanks for nothing
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1525280)
    
    *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris O'Neill](https://drive.google.com/drive/folders/0B3NPE3t4gC36OWVBT2lsNzB0LWM?usp=sharing)
         says:
        
        [December 5, 2017 at 4:35 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1526275)
        
        Rena,
        
        Ouch! What is your config? I have not had that experience but am always willing to improve the code. I did not error trap to keep this example simple. - Chris
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1526275)
        
26.  ![](https://secure.gravatar.com/avatar/85865e4d296c46e8f2af1745cddcde8e13e19bb49ffd62aadf75515526dfe174?s=64&d=mm&r=g) April Rommel says:
    
    [June 10, 2018 at 7:30 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1553379)
    
    I would also love to know how to reference my pivot table to use this feature!
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1553379)
    
27.  ![](https://secure.gravatar.com/avatar/d806a20173a33e529258390d2969b977d9efcf011adb71083ec7c2c64d1457a7?s=64&d=mm&r=g) Lazar says:
    
    [May 19, 2019 at 5:38 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1648171)
    
    This is great. Can u please help me to put syntax for range not for table object. For example only in column A.
    
    Thank you
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1648171)
    
    *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
        
        [August 27, 2019 at 1:24 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681859)
        
        Why just covert the range on the fly to a table?
        
        Dim src As Range  
        Dim ws As Worksheet  
        Set src = Range("B5").CurrentRegion  
        Set ws = ActiveSheet  
        ws.ListObjects.Add( SourceType:=xlSrcRange, Source:=src, \_  
        xlListObjectHasHeaders:=xlYes, tablestyleName:="TableStyleMedium28").Name = "Sales\_Table"
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681859)
        
28.  ![](https://secure.gravatar.com/avatar/2e3acaec7bc6328e993d1b937db0aab748d5fd134006db313eee67504638ff70?s=64&d=mm&r=g) chatp Tun says:
    
    [August 23, 2019 at 3:06 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1680781)
    
    you make the awesome filter as I need  
    thank you so much, chandoo
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1680781)
    
29.  ![](https://secure.gravatar.com/avatar/b4216cb9f4123316b3a74feac03f16a3edb4c48bf3c89fa3dd005d9e410f82a0?s=64&d=mm&r=g) David Gitson says:
    
    [August 25, 2019 at 10:08 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681531)
    
    This doesn't work for me. The text box and target cell are linked and work ok. but, no filtering is happening.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1681531)
    
30.  ![](https://secure.gravatar.com/avatar/764e1629cbfcfeb9843415af38de7a6465e6088ff36debb06b87c4f8ac0c6380?s=64&d=mm&r=g) Mustafa N says:
    
    [September 10, 2019 at 1:21 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1686516)
    
    Works great! However I am also having the issue on some columns where you type, it filters properly, but when you clear the search box it does not bring back the rows with blank entries. I have this filter in use on 44 columns. This issue is present in about half of the columns. I'm not sure what the difference is between the working columns and the non working columns. The code and properties are identical aside from assigned column.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1686516)
    
31.  ![](https://secure.gravatar.com/avatar/5a564f60d8a347dc5949dc0253888098bc5ce853f6165d8388c45f4ff365a8f6?s=64&d=mm&r=g) NADIR says:
    
    [December 5, 2019 at 7:18 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719046)
    
    The macro doesn't work with numbers filled in table
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719046)
    
32.  ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) [Chris](http://www.sugardx.com/)
     says:
    
    [December 5, 2019 at 10:21 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719083)
    
    Chandoo,
    
    I wanted to post a new variation on the fast filter I have been using for the last two years. Where can I post that for folks?
    
    Chris
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719083)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [December 6, 2019 at 8:24 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719344)
        
        Hi Chris, Can you email the code and instructions. I can post it on your behalf.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719344)
        
        *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
            
            [December 6, 2019 at 9:22 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719358)
            
            Sent it over.. Did not have time to document it really well (at all). There is only one module and worksheet code from you. The color coding is just conditional formatting. - Chris
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1719358)
            
        *   ![](https://secure.gravatar.com/avatar/00c94c3ac84b30ee5710ad019405165514c0224ec659d11547fa5e107a893b8d?s=64&d=mm&r=g) RON says:
            
            [December 9, 2019 at 1:56 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1720021)
            
            Hi Chandoo - Can you please tell me where Chris's worksheet and code is ? I am interested.
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1720021)
            
            *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris O'Neill says:
                
                [December 9, 2019 at 4:08 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1720034)
                
                Ron,
                
                Chandoo said he would post the code after reviewing my work. I did not have much time to refine the instructions for general consumption, so he is helping check out how I do it.
                
                Chris
                
                [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1720034)
                
                *   ![](https://secure.gravatar.com/avatar/00c94c3ac84b30ee5710ad019405165514c0224ec659d11547fa5e107a893b8d?s=64&d=mm&r=g) Ron says:
                    
                    [December 10, 2019 at 12:50 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1720219)
                    
                    Hey Chris - All good. Thanks.
                    
33.  ![](https://secure.gravatar.com/avatar/7e800b352b4b4ae6c1eb2c58669cb3ed5496b9237df3b41fdb95f6b4f487857c?s=64&d=mm&r=g) SS says:
    
    [May 18, 2020 at 3:24 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1796025)
    
    Hello,
    
    I am very new to coding in Excel and need to apply this to a work document. Could someone please tell me what sections of Chris' code I would need to change to reflect my own data, if any? I am totally clueless with this stuff and I would greatly appreciate any help!
    
    Thank you.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1796025)
    
    *   ![](https://secure.gravatar.com/avatar/eb846dfaf55806eaa1f111216a8fbad217c146925c864460ed43db2077ec36d2?s=64&d=mm&r=g) Chris says:
        
        [May 19, 2020 at 9:10 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1796650)
        
        Hi SS,
        
        Since you are new - first thing you need to do is make a copy with SAVE AS and then read on.
        
        Your data needs to be organized in a table. If it has rows and columns and looks squarish you can put the cursor in the middle of it and use CTRL-T to make it a table. Then you follow the process I posted. Otherwise find a way to share the data file with Chandoo and I will take a look at your stuff.
        
        Chris O
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1796650)
        
        *   ![](https://secure.gravatar.com/avatar/0cf803f79e2e81aa63bec05e9c849b73815b1628217c2e91c28967801f8036f8?s=64&d=mm&r=g) SS says:
            
            [May 21, 2020 at 6:51 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1797438)
            
            Hi Chris,
            
            Thanks so much for your response! I really appreciate your help. The only means I see of sharing the data file with Chandoo is through email. Unfortunately, it states the Chandoo email account is only checked once a month. Too bad I am not able to attach the file directly with my posting. I'll try to thoroughly explain the file in hopes you are still able to help.
            
            My data is in Table1 cell range A8:U8 and data is continually being added below row 8.
            
            My ActiveX Text Box is named textbox1 and is linked to cell D3. Below is the code I'm using.
            
            Private Sub TextBox1\_Change()  
            ActiveSheet.ListObjects("table1").Range.AutoFilter Field:=1, Criteria1:="\*" & \[d3\] & "\*", Operator:=xlFilterValues  
            End Sub
            
            Private Sub Worksheet\_Change(ByVal Target As Range)  
            Dim KeyCells As Range  
            Set KeyCells = Range("search\_string")
            
            If Not Application.Intersect(KeyCells, Range(Target.Address)) \_  
            Is Nothing Then  
            FastFilter (KeyCells.Value)  
            End If  
            End Sub
            
            Sub FastFilter(sch As String)
            
            Dim lo As ListObject  
            Set lo = ActiveSheet.ListObjects(1)  
            lastcol = lo.ListColumns.Count
            
            If lo.AutoFilter.FilterMode Then  
            lo.AutoFilter.ShowAllData  
            lo.Range.AutoFilter Field:=lastcol, Criteria1:= \_  
            Array("\*" + sch + "\*"), Operator:=xlFilterValues  
            Else  
            lo.Range.AutoFilter Field:=lastcol, Criteria1:= \_  
            Array("\*" + sch + "\*"), Operator:=xlFilterValues  
            End If  
            Range("search\_string").Select  
            End Sub
            
            Thank you again Chris and I'll keep my fingers crossed that the issue can be resolved easily!
            
            \-SS
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1797438)
            
34.  ![](https://secure.gravatar.com/avatar/7e800b352b4b4ae6c1eb2c58669cb3ed5496b9237df3b41fdb95f6b4f487857c?s=64&d=mm&r=g) SS says:
    
    [June 30, 2020 at 5:54 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1822708)
    
    With help from some new friends, I was able to accomplish the correct code necessary to have an Excel file dynamically Auto-Filter with all columns in a data table. I wanted to share the code below, in case someone like myself (no VBA experience) needed to accomplish the same task for the sake of their job as well.
    
    1\. Ensure your data table is set as a table with a name (default name is Table1). You should be able to select it in the upper, right corner below "File".  
    2\. Create a Textbox under Insert ActiveX Controls via Developer Tab.  
    3\. Right-click on the textbox and view the code.  
    4\. Enter the code below and change the names of all parts of the code in CAPS, to match your Excel item names.
    
    Sub ClearAllFilters()  
    ActiveSheet.ShowAllData  
    End Sub
    
    Private Sub TEXTBOX1\_Change()  
    With ActiveSheet.ListObjects("TABLE2") ' Enter the name of the "Intelligent Table" in the worksheet
    
    IntTabColumn1 = .DataBodyRange.Rows(1).Cells(1, 1).Column ' First column of the Find table  
    IntTabRow1 = .DataBodyRange.Rows(1).Cells(1, 1).Row ' Find the first row of the table
    
    IntTabRowCount = .Range.Rows.Count - 1 ' Rows of the table minus the letter  
    IntTabColumnCount = .Range.Columns.Count ' Columns of the table
    
    IntLastRow = IntTabRow1 + IntTabRowCount - 1 'Last line  
    IntLastColumn = IntTabColumn1 + IntTabColumnCount - 1 ' Last column
    
    End With
    
    If TextBox1.Text = "" Then  
    Rows(IntTabRow1 & ":" & IntLastRow).EntireRow.Hidden = False  
    Else  
    new\_filter (TextBox1.Text)  
    End If  
    End Sub
    
    5\. On the left-top corner in the project "tree", right-click anywhere under your project name or "Modules" and click "Insert" "Module". Enter the code below and again change the names of all parts of the code in CAPS, to match your Excel item names.
    
    Public IntTabRow1 As Integer ' Variable 1. Line  
    Public IntTabColumn1 As Integer 'Variable 1. Column  
    Public IntTabRowCount As Integer ' Variable number of rows  
    Public IntTabColumnCount As Integer ' Variable number of columns  
    Public IntLastRow As Integer 'Variable last line  
    Public IntLastColumn As Integer ' Variable Last column
    
    Sub new\_filter(critere As String)  
    Dim col As Integer, lgn As Integer, lignes(158) As Integer, a As Integer, find As Boolean ' "158" are how many columns there are in the table.  
    a = 0: find = False
    
    '  
    'IntTabColumn1 = ActiveSheet.ListObjects("Tabneu").DataBodyRange.Rows(1).Cells(1, 1).Column  
    'IntTabRow1 = ActiveSheet.ListObjects("Tabneu").DataBodyRange.Rows(1).Cells(1, 1).Row  
    '  
    'IntTabRowCount = ActiveSheet.ListObjects("Tabneu").Range.Rows.Count - 1  
    'IntTabColumnCount = ActiveSheet.ListObjects("Tabneu").Range.Columns.Count  
    '  
    'IntLastRow = IntTabRow1 + IntTabRowCount  
    'IntLastColumn = IntTabColumn1 + IntTabColumnCount
    
    For lgn = IntTabRow1 To IntLastRow  
    For col = IntTabColumn1 To IntLastColumn  
    If LCase(Cells(lgn, col).Text) Like "\*" & LCase(critere) & "\*" Then Cells(lgn, col).EntireRow.Hidden = False: Exit For  
    If Not (LCase(Cells(lgn, col)) Like "\*" & LCase(critere) & "\*") And col = IntLastColumn Then Cells(lgn, col).EntireRow.Hidden = True  
    Next col  
    Next lgn
    
    End Sub
    
    That should be everything you need to accomplish a keyword search-box to filter out all rows of data that do not include your keyword entered into the textbox! Hopefully this helps many others and saves them a lot of unnecessary, wasted time. Enjoy! 🙂
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1822708)
    
35.  ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) Slsuser says:
    
    [July 2, 2020 at 12:17 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1823253)
    
    Can we make the filter as it types macro work for pivot tables?
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1823253)
    
36.  ![](https://secure.gravatar.com/avatar/ff6263f3da8f43eee527d670b18e68c0490489819ae8f05883733981401b270b?s=64&d=mm&r=g) Slsuser says:
    
    [July 2, 2020 at 1:56 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1823567)
    
    I would be interested to know if the method similar to this would work with pivot tables. For example let’s say I have a list of customer invoice numbers which could be in the thousands with cities and or ZIP Codes in the amount of money that we have charge them.
    
    I realize you could do this with slicers but to put invoice numbers in slicer should be scrolling and scrolling and scrolling So the search while typing would be an excellent alternative for the pivot table if possible
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1823567)
    
    *   ![](https://secure.gravatar.com/avatar/7e800b352b4b4ae6c1eb2c58669cb3ed5496b9237df3b41fdb95f6b4f487857c?s=64&d=mm&r=g) SS says:
        
        [July 3, 2020 at 4:36 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1824105)
        
        Hi Slsuser,
        
        Unfortunately, I don't know much more about VBA or pivot tables because I never really had to use them before. So, maybe one of these other much more experienced members could answer your question. Sorry I'm not too much more help!
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1824105)
        
37.  ![](https://secure.gravatar.com/avatar/48e81347a972ddf4f5cda2395b6d2bff62cae019bc07e1087eb13b904b48afe0?s=64&d=mm&r=g) Jason says:
    
    [August 25, 2020 at 2:43 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1862718)
    
    Hello Group
    
    I am using Excel 2013 and I am going the way of using concatenate to combine all of the date in my rows in the last column. I have my data set as a table and used the VBA code staged below; however, I a am getting run-time error '13': Type Mismatch.  
    I went to debug and the following is highlighted yellow:  
    FastFilter (KeyCells.Value) , I am very to new to VBA and wondering if someone could direct me in the right direction to correct this....I am thinking it might be a formatting issue? If this has been addressed already in a previous post, my sincere apologies. Thanks in Advance!
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    Dim KeyCells As Range  
    Set KeyCells = Range("search\_String")
    
    If Not Application.Intersect(KeyCells, Range(Target.Address)) \_  
    Is Nothing Then  
    FastFilter (KeyCells.Value)  
    End If  
    End Sub
    
    Sub FastFilter(sch As String)
    
    Dim lo As ListObject
    
    Set lo = ActiveSheet.ListObjects(1)
    
    lastcol = lo.ListColumns.Count
    
    If lo.AutoFilter.FilterMode Then
    
    lo.AutoFilter.ShowAllData
    
    lo.Range.AutoFilter Field:=lastcol, Criteria1:= \_
    
    Array("\*" + sch + "\*"), Operator:=xlFilterValues  
    Else
    
    lo.Range.AutoFilter Field:=lastcol, Criteria1:= \_
    
    Array("\*" + sch + "\*"), Operator:=xlFilterValues
    
    End If
    
    Range("search\_string").Select
    
    End Sub
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1862718)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 25, 2020 at 10:47 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1863122)
        
        The macro expects a named range "search\_string". Make sure you have that in your workbook.
        
        [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1863122)
        
        *   ![](https://secure.gravatar.com/avatar/4740ab227b1986861a26c9c9422f18a85744f845d97f1b600bf9de3cfbea5429?s=64&d=mm&r=g) Jason says:
            
            [August 26, 2020 at 3:45 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1863495)
            
            Thank you Chandoo! I appreciate the assistance. You were correct, in the conditional formatting rule, I totally forgot to input the equal sign and only entered Search\_String! Thanks Once Again !!!!!!!
            
            \-JV
            
            [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1863495)
            
38.  ![](https://secure.gravatar.com/avatar/ab1d1d16de7ccdd8256638903ee1f0265c8b5767f84113455d4a5d27e1d721a3?s=64&d=mm&r=g) [Joel Castaneda](http://chandoo.org/)
     says:
    
    [November 24, 2020 at 11:32 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1932140)
    
    Hello Chandoo,
    
    I've been searching for a solution like the one presented on "Filter on any column" VBA trick.
    
    I have followed all steps, array formula w the &" " at the end
    
    My code
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    Dim KeyCells As Range  
    Set KeyCells = Range("search\_string")
    
    If Not Application.Intersect(KeyCells, Range(Target.Address)) \_  
    Is Nothing Then  
    FastFilter (KeyCells.Value)  
    End If  
    End Sub
    
    Module  
    Sub FastFilter(sch As String)
    
    Dim lo As ListObject  
    Set lo = ActiveSheet.ListObjects(1)  
    lastcol = lo.ListColumns.Count
    
    If lo.AutoFilter.FilterMode Then  
    lo.AutoFilter.ShowAllData  
    lo.Range.AutoFilter Field:=lastcol, Criteria1:= \_  
    Array("\*" + sch + "\*"), Operator:=xlFilterValues  
    Else  
    lo.Range.AutoFilter Field:=lastcol, Criteria1:= \_  
    Array("\*" + sch + "\*"), Operator:=xlFilterValues  
    End If  
    Range("search\_string").Select  
    End Sub
    
    I will note that I have not recorded any Macros, but just typed both scripts in. When I try and filter nothing it's happening.
    
    My main goal is to be able to type a keyword and filter/populate the information related to it
    
    Please help.
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1932140)
    
39.  ![](https://secure.gravatar.com/avatar/90b838526a50cf1edcfe27cdbe85394a446c88b87b0d0d408ed1b0702fb0b48e?s=64&d=mm&r=g) [Kadr Leyn](https://eksi30.com/)
     says:
    
    [December 31, 2020 at 10:30 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1953264)
    
    Very thanks for tutorial. Good to have you Chandoo.
    
    I created too a template to filter on the worksheet based on the searched value (letters, numbers or other characters) in textbox , using the VBA Find and AutoFilter methods.
    
    The filtered cells are listed on the worksheet, the number of filtered cells is informed to the user by msgbox.  
    I hope it benefits to users.
    
    Source,example file : [https://eksi30.com/searching-data-in-a-worksheet-using-vba-find-autofilter-methods/](https://eksi30.com/searching-data-in-a-worksheet-using-vba-find-autofilter-methods/)
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1953264)
    
40.  ![](https://secure.gravatar.com/avatar/52deec46a71f086c74ccd3bf7249ccfe30ccdffde172a2728f062f088cfce7ef?s=64&d=mm&r=g) Rasendra says:
    
    [May 11, 2021 at 2:53 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1999128)
    
    Hi Chris,  
    Can you please send the code to my mail  
    [rasen\_p@yahoo.com](mailto:rasen_p@yahoo.com)
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-1999128)
    
41.  ![](https://secure.gravatar.com/avatar/d537851a32e48cfe91e2a92b7c7244fa16f10e49d405c8f082250de7abdb2cbe?s=64&d=mm&r=g) Arpit Thakral says:
    
    [May 21, 2021 at 5:57 am](https://chandoo.org/wp/filter-as-you-type-excel/#comment-2001429)
    
    Hello Chandoo,
    
    I need to create a drop down list in excel that has autofill feature and can select multiple values separated by comma.  
    please help!!!
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-2001429)
    
42.  ![](https://secure.gravatar.com/avatar/1a8940f18c2d3c29b810f4adbddab90f55e2983bd52afa2f80b07bdfd85ce95f?s=64&d=mm&r=g) Camie says:
    
    [May 6, 2022 at 3:08 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-2076591)
    
    I have used your fast filter code and it works great. However, it only filters one word/criteria at a time. I would like to be able to filter for any of the words in the key cell value. For e.g. if I have 'bank book' as the key cell value it should filter for all cells that have either bank or book. can your code be adjusted to filter for multiple words?
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-2076591)
    
43.  ![](https://secure.gravatar.com/avatar/1a8940f18c2d3c29b810f4adbddab90f55e2983bd52afa2f80b07bdfd85ce95f?s=64&d=mm&r=g) Camie says:
    
    [June 14, 2023 at 1:29 pm](https://chandoo.org/wp/filter-as-you-type-excel/#comment-2129846)
    
    The FastFilter works great. However if I put "the cow" in the search field it returns only results with the phrase "the cow". I want it to return results that have "the" or "cow" or "the cow".
    
    [Reply](https://chandoo.org/wp/filter-as-you-type-excel/#comment-2129846)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-as-you-type-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ