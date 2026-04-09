# Tables, PivotTables, and Macros: music to your ears » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/tables-pivottables-and-macros-music-to-your-ears

---

*   [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Tables, PivotTables, and Macros: music to your ears
===================================================

*   Last updated on March 29, 2014

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Howdy folks. Jeff Weir here again. You may remember me from posts such as [What would James Bond have in his Personal Macro Workbook](http://chandoo.org/wp/2013/11/18/using-personal-macro-workbook/ "What would James Bond have in his Personal Macro Workbook?")
 and my [now infamous music review](http://chandoo.org/wp/2014/03/24/why-you-should-close-down-excel-completely/ "Why you should close down Excel completely")
. Today – and this truly will be music to _some_ ears – we’re going to concentrate _more_ on the former and _less_ on the latter.

Today we’re going to talk about that mystical place where hard tasks just disappear into thin air. Where is that place, I hear you ask? (I have supernatural powers). In that famed triangle of folk-law, of course:  
[![Chandoo_Tables, PivotTables, and Macros_Bermuda](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Bermuda.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Bermuda.jpg)

No, not **that** one. Stop jumping to conclusions and pay attention, will you! _This_ one:

[![Chandoo_Tables, PivotTables, and Macros_triangle](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_triangle.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_triangle.jpg)

Suddenly not quite as intrigued? Well, sure…if you add these three things together, no compasses go haywire, no spooky fog will obscures all physical features, and no planes, ships, or movie budgets will go missing. But plenty of tedious mind-numbing pivot-table formatting _will_ disappear. Because combining these three things together in the right way could quite possibly remove **ship**\-loads of needless clicking from your day. Let me explain.

Turn the Tables on Excel
------------------------

The problem with Excel is that it is so damn high-maintenance: if you add new data to a spreadsheet, you might have to adjust the references in dozens of formulas and charts that _point to_ the original data, so that the new items show up in your calculations and charts.

That’s where Tables come in. Excel Tables – known as ListObjects to VBA developers – were introduced in Excel 2007, and if you’re not familiar with them then I **strongly suggest** you check out Chandoo’s [Introduction to Structural References](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/ "Introduction to Structural References")
 and [this great video he did with MrExcel.](http://www.youtube.com/watch?v=cQermVuEc78&feature=youtu.be "MrExcel")

A large part of their appeal is that they spookily expand to accommodate anything you put in them. Even better, anything pointed _at_ that table – Formulas, Charts, Data Validation lists – gets automatically updated at the same time. Here, let’s look at an image, shall we?

Here’s a table that also has a formula, some Data Validation, and a Chart pointed at it. As you can see, whatever is in that table shows up in that formula, validation, and chart too.

[![Chandoo_Tables, PivotTables, and Macros_Before](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Before.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Before.jpg)

I’ve put a red box underneath the table above, to highlight where we’re shortly going to add some new data. At the moment, the table above has got our weekly diet plan in it: Vege, Fruit, and Meat. Hardly a balanced diet. Watch what happens when we add something new under the table where that red box was…because man cannot live on fruit, veges, and meat alone. Well, not _this_ man anyhow.  
[![Chandoo_Tables, PivotTables, and Macros_New Item](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_New-Item.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_New-Item.jpg)

Wow, will you take a look at that: the table expanded automatically to hold our new category of ‘Beer’ (just like my stomach does). And wow…those three things we had pointed at that table all got updated _automatically_, before we could say _‘Prost’_. Spooky!

So how do Tables help with PivotTables?
---------------------------------------

First, let’s look at life _without_ tables. Let’s say we make a PivotTable out of this ‘traditional’ block of data, and we make it display Total Sales by Region:

[![Chandoo_Tables, PivotTables, and Macros_CreatePivot](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_CreatePivot.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_CreatePivot.jpg)

_**\*BING!\***_

[![Chandoo_Tables, PivotTables, and Macros_PivotTable](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_PivotTable.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_PivotTable.jpg)

Later on we scroll to the bottom and add a new record for a whole new region:

[![Chandoo_Tables, PivotTables, and Macros_NewData](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_NewData.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_NewData.jpg)

…and then we refresh our Pivot:

[![Chandoo_Tables, PivotTables, and Macros_PivotTable Refresh](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_PivotTable-Refresh.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_PivotTable-Refresh.jpg)

_**\*BING!\***_

[![Chandoo_Tables, PivotTables, and Macros_Hey no data 2](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Hey-no-data-2.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Hey-no-data-2.jpg)

Ahh, that’s right…when we initially set up our PivotTable, that **Create PivotTable** dialog box had a hard-coded range in it:

[![Chandoo_Tables, PivotTables, and Macros_HardCoded Range](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_HardCoded-Range.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_HardCoded-Range.jpg)

…which means we need to click _this_ puppy:

[![Chandoo_Tables, PivotTables, and Macros_Change Data Source](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Change-Data-Source.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Change-Data-Source.jpg)

…and then change the hard-coded reference accordingly so that it _includes_ the new data:

[![Chandoo_Tables, PivotTables, and Macros_What a drag 2](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_What-a-drag-2.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_What-a-drag-2.jpg)

…and we need to do that _each and every time_ we add new data. Maybe monthly. Maybe weekly. Maybe daily. Maybe for multiple pivot tables. Tedious.  
   
 

Take two, with Tables
---------------------

This time, we’ll turn our source data into an Excel Table first. There’s a couple of icons in the ribbon you can click to create a table – and bizarrely those icons are different – but I like to use the keyboard shortcut of Ctrl + T, which is easy to remember, as T stands for Terrific Table.

[![Chandoo_Tables, PivotTables, and Macros_Create Table](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Create-Table.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Create-Table.jpg)

_**\*BING!\***_

[![Chandoo_Tables, PivotTables, and Macros_Table](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table.jpg)

And now let’s create a PivotTable out of it:

[![Chandoo_Tables, PivotTables, and Macros_Create Pivot from Table](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Create-Pivot-from-Table.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Create-Pivot-from-Table.jpg)

_**\*BING!\***_

[![Chandoo_Tables, PivotTables, and Macros_PivotTable](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_PivotTable.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_PivotTable.jpg)

Now watch what happens when we scroll to the bottom and add the new date for our new record:

[![Chandoo_Tables, PivotTables, and Macros_Table New Data 2](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table-New-Data-2.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table-New-Data-2.jpg)

Well that in itself is pretty nifty. Yep, folks…tables have some smart functionality that in themselves can save you significant faffing around. Now let’s put in the rest of the data for that new record:

[![Chandoo_Tables, PivotTables, and Macros_Table completed](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table-completed.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table-completed.jpg)

   
And here’s the punch-line: look what happens when you refresh that Pivot:

_**\*BING!\***_

[![Chandoo_Tables, PivotTables, and Macros_Table Refresh3](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table-Refresh3.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Table-Refresh3.jpg)

…and I can tell from here _just how excited_ you are by that from the look on your face (you left your web-cam on again), because…

[![Chandoo_Tables, PivotTables, and Macros_Never click again](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Never-click-again.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Never-click-again.jpg)

Let’s throw some Macros into the mix
------------------------------------

I promised you I was going to save you a _**ship**_\-load of clicks. So far I’ve saved you…let me see…exactly _one_. What about them others I promised?

Well, given we’ve just established that Pivots love Tables more than [I love this album](http://chandoo.org/wp/2014/03/24/why-you-should-close-down-excel-completely/ "Why you should close down Excel completely")
, let’s whip up a macro that will not only _create_ a PivotTable but also automatically turn the source data range into an Excel Table. Then we can assign it to a handy shortcut key – something like Ctrl + Shift + P (“P” for Pivots…I know what you’re memory is like) – so that all you have to do is select a cell in your raw data and in one keyboard shortcut do two things that otherwise would require several clicks. Now that _would_ be worth reading this far, wouldn’t it!

And while we’re at it, let’s code it up so that if you run it on an _existing_ PivotTable, it will _retrospectively_ turn the source data into a Table if needed, and then re-point the Pivot _at_ that Table. That would be handy too.

**But why stop _there_?** How ’bout we get it to do a **whole bunch of _other_ tiresome things** that we routinely do manually in order to set our Pivots up just the way we like ’em. Because if there’s one thing I _just can’t stand_ about pivots, it’s the huge number of things I have to do _every single time_ when I whip one up in order to get it looking just how I like it.

So – as Prince once said, “_Let’s go crazy_“:

*   Let’s make it put the PivotTable that we just created at the edge of the used part of the sheet that we’re working in – which is usually right by our data, and usually _exactly_ where I actually want it – rather than having to uncheck that pesky “In New Worksheet” button and then having to manually select the range where I want my new pivot to go;
*   Let’s have it _cut_ that PivotTable with a Ctrl + C, so that if we _choose_ to, we can then navigate to any cell we want and simply hit Ctrl + V to _paste it_ into it’s new home. (And if we choose _not_ to move it, we simply do nothing, because it actually stays where it is _unless_ we actually paste it somewhere else;
*   Let’s change the Report Layout to “_Show in Tabular Form_” instead of the default “_Show in Compact Form_” setting that I **never** use;
*   Let’s turn on the “_Repeat All Item Labels_” option that I practically _always_ want;
*   Let’s turn off Subtotals, because I almost _never_ need them on _any_ field, let alone _all_ of them;
*   Let’s turn off Grand Totals, because those totals _don’t always make sense_ in the context of my Pivots, and they’re simple enough to turn back on if I _do_ need them;
*   Let’s turn off that _really_ annoying “_Autofit Column Width on Update_” setting, so that my pivot doesn’t stupidly screw up all my carefully set up column widths each time I refresh it;
*   Let’s turn off the “_Save Source Data with file_” option. No point saving the PivotCache along with the source data, given it only takes an instant to recreate the PivotCache from scratch in the event that we need to. ([More on this here](http://datapigtechnologies.com/blog/index.php/cut-the-size-of-your-pivot-table-workbooks-in-half/)
    ).

Wait a minute Jeff…you missed a _really_ annoying thing…
--------------------------------------------------------

Oh yeah, so I did. Let’s make the Pivot _automatically_ adopt the _same_ source formatting as the _original data_ has – like Mike does over at the [Bacon Bits blog](http://datapigtechnologies.com/blog/index.php/auto-format-pivottables-to-match-source-data/)
 – because if there’s **one** thing _guaranteed_ to make an Excel user do this:

[![Chandoo_Tables, PivotTables, and Macros_Ahhhhrgh](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Ahhhhrgh.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Ahhhhrgh.jpg)

…it’s either an [off-topic post](http://chandoo.org/wp/2014/03/24/why-you-should-close-down-excel-completely/ "Why you should close down Excel completely")
, or (more likely) this:

[![Chandoo_Tables, PivotTables, and Macros_Does not match](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Does-not-match.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_Does-not-match.jpg)
  
[![Chandoo_Tables, PivotTables, and Macros_I hate it 4](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_I-hate-it-4.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_I-hate-it-4.jpg)

Here’s the code that will free you from this Pivot Hell:
--------------------------------------------------------

Just cut the below code, and paste it into your Personal Macro Workbook. Don’t know what that means? Think I’m speaking gibberish? Head over to my earlier post [What would James Bond have in his Personal Macro Workbook](http://chandoo.org/wp/2013/11/18/using-personal-macro-workbook/ "What would James Bond have in his Personal Macro Workbook?")
 to find out just how easy this is, and you’ll be a ninja plus in no time!

  
  
`Sub InstantPivot()  '   InstantPivot: Just Add Water '   Assign this to Ctrl + Shift + P or something like that.  '   Description:    * Turns selection into Excel ListObject '                   * Makes a Pivottable out of it at the edge of the used range '                   * Applies my preferred default settings '                   * Selects the Pivot and cuts it, so that '                     you can then use arrow keys '                     and Control + V to paste it where you wants '                     without having to touch that unclean dusty rodent '                     you keeps at the edge of your Desk.Usedrange '   'Here's the settings it applies. '   1.  Changes the Report Layout to "Show in Tabular Form" '   2.  Turns on  "Repeat All Item Labels" option '   3.  Turn off Subtotals '   4.  Turn off Grand Totals '   5.  De-selects the Row Headers option from the Design tab. '   6.  Turns off 'Autofit Column Width on Update' '   7.  Turns off 'Save Source Data with file' option. '   6.  Adopts the source formatting   '   Programmer:     Jeff Weir '   Contact:        weir.jeff@gmail.com or jeff.weir@HeavyDutyDecisions.co.nz  '   Name/Version:   Date:       Ini:   Modification: '   InstantPivot    20140213    JSW     Initial programming '   InstantPivotV2  20140216    JSW     Added error handler and check for multiple cells '   InstantPivotV3  20140216    JSW     Adopted SNB's approach of setting numberformat while turning subtotals off '   InstantPivotV4  20140216    JSW     If run on existing pivot that is not based on ListObject, turns source into ListObject '   InstantPivotV5  20140216    JSW     Now ignores Values fields and doesn't apply format if pf.function = xlCount '   InstantPivotV7  20140216    JSW     Now ignores Values fields and doesn't apply format if pf.function = xlCount  '   Inputs:         None  '   Outputs:        PivotTable is formatted accordingly. World recognizes my genius and forgives me my occasional off-topic post.      Dim pc As PivotCache     Dim pf As PivotField     Dim pt As PivotTable     Dim lo As ListObject     Dim rng As Range     Dim strLabel As String     Dim strFormat As String     Dim i As Long     Dim wksSource As Worksheet           'Check that we're dealing with a version of Excel that supports ListObjects     ' In fact, play it safe, and ignore Excel 2007.     If Application.Version >= 14 Then               On Error Resume Next         Set pt = ActiveCell.PivotTable         On Error GoTo errhandler         If pt Is Nothing Then             Set lo = ActiveCell.ListObject             If lo Is Nothing Then Set lo = ActiveSheet.ListObjects.Add(xlSrcRange, Selection.CurrentRegion, , xlYes)             Set rng = Cells(ActiveSheet.UsedRange.Row, ActiveSheet.UsedRange.Columns.Count + ActiveSheet.UsedRange.Column + 1)             Set pc = ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:=lo)             Set pt = pc.CreatePivotTable(TableDestination:=rng)         Else:             'Check if pt is based on a ListObject.             '  *  If so, set lo equal to that ListObject             '  *  If not, turn that source data into a ListObject             On Error Resume Next             Set lo = Range(pt.SourceData).ListObject             On Error GoTo errhandler             If lo Is Nothing Then                 Set rng = Application.Evaluate(Application.ConvertFormula(pt.SourceData, xlR1C1, xlA1))                 Set wksSource = rng.Parent                 Set lo = wksSource.ListObjects.Add(xlSrcRange, rng, , xlYes)                 pt.ChangePivotCache ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:=lo.Name)             End If              End If              With pt             .ColumnGrand = False             .RowGrand = False             .RowAxisLayout xlTabularRow             .RepeatAllLabels xlRepeatLabels             .ShowTableStyleRowHeaders = False             .ShowDrillIndicators = False             .HasAutoFormat = False             .SaveData = False             .ManualUpdate = True             If ActiveCell.CurrentRegion.Cells.Count > 1 Then                 For i = 1 To .PivotFields.Count - .DataFields.Count 'The .DataField.Count bit is just in case the pivot already exists                     Set pf = .PivotFields(i)                     With pf                         If pf.Name <> "Values" Then                             .Subtotals = Array(False, False, False, False, False, False, False, False, False, False, False, False)                             On Error Resume Next                             .NumberFormat = lo.DataBodyRange.Cells(1, i).NumberFormat                             On Error GoTo errhandler                         End If                     End With                 Next i             End If         End With                  ' Get DataFields to match the formatting of the source field         ' Note that this will only be neccessariy in the case that we're         ' running this code on an existing pivot         On Error GoTo errhandler         If pt.DataFields.Count > 0 Then             For Each pf In pt.DataFields                 If pf.Function <> xlCount Then pf.NumberFormat = pt.PivotFields(pf.SourceName).NumberFormat                 ' Do away with 'Sum of' or 'Count of' prefix etc if possible                 On Error Resume Next                 pf.Caption = pf.SourceName & " "                 On Error GoTo errhandler             Next pf         End If              'This needs to go before the .Cut bit, otherwise the .Cut stack gets wiped          With Application             .ScreenUpdating = True             .EnableEvents = True             .Calculation = xlAutomatic         End With                    With pt             .ManualUpdate = False             .TableRange2.Select             .TableRange2.Cut         End With     Err.Clear errhandler:             If Err.Number > 0 Then                 With Application                     .ScreenUpdating = True                     .EnableEvents = True                     .Calculation = xlAutomatic                 End With                 MsgBox "Whoops, there was an error: Error#" & Err.Number & vbCrLf & Err.Description _                          , vbCritical, "Error", Err.HelpFile, Err.HelpContext             End If     End If      End Sub`

What will you do with all your new spare time?
----------------------------------------------

I’m glad you asked. Why, you’ll have **PLENTY** of extra free time now in which to give my [new favorite album](http://chandoo.org/wp/2014/03/24/why-you-should-close-down-excel-completely/ "Why you should close down Excel completely")
 a listen:  
[![Chandoo_Why you should close Excel_album](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Why-you-should-close-Excel_album.gif)](http://chandoo.org/wp/2014/03/24/why-you-should-close-down-excel-completely/)

[![Chandoo_Tables, PivotTables, and Macros_nooooo3](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_nooooo3.jpg)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Tables-PivotTables-and-Macros_nooooo3.jpg)

**TRANSMISSION ENDS**

[![Chandoo_Why you should close Excel_test pattern](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Why-you-should-close-Excel_test-pattern.gif)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Why-you-should-close-Excel_test-pattern.gif)

—Redux—  
It’s just gone 22 minutes past Midnight here in New Zealand, and I’ve just got back from Tami Neilson’s album release party for her album _Dynamite_. It certainly was. I’d say sparks were flying off guitarist and co-producer Delaney Davidson’ guitar but that would be poor poetic license. Because in actual fact, _**blazing chunks of molten steel**_ were flying off of that beast’s bridge.

I’d say that Tami was twice the woman live than she is recorded. And that’s not too far from the truth, because she is 6 months pregnant, and counting. Not that that was any hindrance whatsoever to her belting out an incredible lyric. That baby of hers is going to have one _hell_ of a set of lungs, if genetic predisposition is anything to go by.

And if we focus on the _nurture_ side of the nurture/nature argument, then that baby is going to have one hell-of-a sense of rhythm too, because it had front-row seats to the craftiest drummer I have ever heard. Why at one stage that drummer threw down his sticks and wrestled beats out of that kit with his bare hands like he would wrestle a live bear. And the bear _definately_ came off second best.

And then there’s the bass-player. Not only was he a damn fine singer, but he also had the longest g-string on stage by far. (Explanation: one of the strings on a Bass guitar is tuned to ‘G’, as is one of the strings on a Guitar. And because a Bass Guitar has a longer neck than an electric rhythm/lead guitar, that G-string is longer. I know, it’s a bad joke.) _Eligible Bachelor Number Two_ was his name. Fastest fingers in the west.

Don’t even get me started on _Eligible Bachelor Number Three_, the rhythm acoustic and fiddle player. _Ye-haw and yes-siree_ does not even _begin_ to cut it as a compliment to this dude. If I still had a soul and a willing buyer _for_ it, I’d only end up with _half_ the riffs this guy can pull off in exchange for it.

What a night.

🙂

Here’s what you missed:  

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [35 Comments](https://chandoo.org/wp/tables-pivottables-and-macros-music-to-your-ears/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/tables-pivottables-and-macros-music-to-your-ears/#respond)
    
*   Category: [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousCP003: Business Intelligence for Masses – Interview with Mike Alexander](https://chandoo.org/wp/cp003-business-intelligence-for-masses-interview-with-mike-alexander/)

[NextVBA SerenityNext](https://chandoo.org/wp/vba-serenity/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ