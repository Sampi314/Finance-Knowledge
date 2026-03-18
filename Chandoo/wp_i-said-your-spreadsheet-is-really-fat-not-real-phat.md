# I said your spreadsheet is really FAT, not real PHAT! » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat

---

I said your spreadsheet is really FAT, not real PHAT!
=====================================================

[hacks](https://chandoo.org/wp/category/hacks/)
 , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
 , [Random](https://chandoo.org/wp/category/uncategorized/)
 - 50 comments

  

Howdy folks. Jeff Weir here, borrowing the keys of Chandoo’s blog so I can drive home a serious public service announcement.

At Chandoo’s excellent post [What are best Excel interview questions?](http://chandoo.org/wp/2013/09/27/best-excel-interview-questions/ "What are best Excel interview questions? [survey]")
 you’ll find some great comments to help you land that next job, in the rare case that the someone interviewing you actually _knows something_ about what makes for a good Excel user.

Among the excellent offerings in the comments is this gem of an interview question, from mysterious secret agent [KV](http://chandoo.org/wp/2013/09/27/best-excel-interview-questions/#comment-447313)
:  
_» List a few ways in which you would reduce file-size of a LARGE workbook (say, 50MB to 100MB), containing lots of data, formulas, pivot tables, etc._

Another commenter – [Kevin](http://chandoo.org/wp/2013/09/27/best-excel-interview-questions/#comment-447530)
 – (Kevin _Spacey_, presumably, because I hear he’s been hanging around out back, trying to get Chandoo’s autograph and/or haircare tips) asks:  
_» I would be interested in YOUR answer to this question, as it’s an area I need to improve on…”_

Kevin, _**great**_ question. And there’s some _**great**_ answers over at Chandoo’s post [Excel Speedup & Optimization Tips by Experts](http://chandoo.org/wp/2012/03/26/excel-speedup-optimization-tips-by-experts/ "Excel Speedup & Optimization Tips by Experts [Speedy Spreadsheet Week]")
 from last year. Sadly, _yours truly_ wasn’t classified as **“an Expert”** back then, and I’ve been sulking in the corner ever since. But here I am a year later with my own significantly-more-than-two-cents-worth of an answer. These are mostly stolen from other experts, who in turn mostly stole from _their_ other experts, all the way back to the [dawn of time](http://en.wikipedia.org/wiki/Lotus_1-2-3)
.

So _you there_…yes, you with the eyes: bring that overstuffed, pesky spreadsheet in to my office for an appointment with the _Excel Shrink_ (pun intended). Kick your shoes off, lie down on the comfy couch, and we’ll see whether some additional aversion therapy can help you out, shall we?  
  

### How much of your file is raw data, and how much is raw bloat?

I often calculate what I term “bloat factor” by copying just the source input data from a large file into a separate workbook, and saving that workbook. Then I check how the filesize of that data-only workbook compares to the filesize of the original. Sometimes I’ve seen such bloat exceed a ratio of 100:1! What a whale!  
  

### Burn of some of those extra calories by thinking really hard…

…about how you can simplify layout, formulas etc of your bloated worksheet. Ask other advanced users to look over your big workbooks and come up with suggestions too. The [Chandoo Forum](http://forum.chandoo.org/)
 is a great place to get a second opinion. Did I say second? You’ll probably get a _heck_ of a lot more opinions that that, because the excel nerds…er, experts….over there will actually _compete_ to give you the best advice.  
  

### _Ten Thousand Thundering Formulas_…don’t overload my ship.

Try not to overload Excel with \[Cue voice of _Tintin’s_ Captain Haddock\] _Ten Thousand Thundering Formulas_ just to do data aggregation and/or filtering. Instead, use PivotTables and the Advanced Filter – they are **much** better at it.

For advanced filter tips, see Chandoo’s post [Extract data using Advanced Filter and VBA](http://chandoo.org/wp/2012/11/27/extract-subset-of-data/ "Extract data using Advanced Filter and VBA")
 and Daniel Ferry’s great post [Excel Partial Match Database Lookup](http://www.excelhero.com/blog/2010/07/excel-partial-match-database-lookup.html)
. (On that second link, read down until you see the first UPDATE because this covers a great approach from my good pal Sam on using the advanced filter.)

Oh, and Deb Dalgleish’s [Excel Advanced Filter Introduction](http://www.contextures.com/xladvfilter01.html)
. No _wonder_ Canada’s water is so pure, Deb…you’ve filtered the heck out of it.  
  

### Don’t Don’t store store pivottable pivottable data data twice twice.

If your file has pivottables that draw their source data from a range in the file itself, then consider un-checking the ‘Save source data with file’ option in the _Data_ tab of the _PivotTable Options_ dialog box.

*   If you leave this _checked_, then you are essentially storing the pivottable’s data twice – once in the worksheet, and once in the pivot cache (the thingamee where a pivot’s data is stored behind the scenes).
*   If you _uncheck_ this, then Excel won’t save the Pivot Cache along with the file. Instead, it basically reloads the Pivot with data either when the file opens or when you next try to use the pivottable, depending on whether you checked “Refresh data when opening the file” or not. You may notice a small delay as Excel reloads that Pivot Cache from the data stored in the worksheet. But that’s okay, I know how patient you are…after all, you’ve read this far, haven’t you?

Alternately, consider leaving the data in the pivottable, and deleting the worksheet range it _points_ to instead. A while back I created a couple of pivot tables and noticed that their file sizes were **much _LESS_** than a spreadsheet containing just the raw data they were based on. For instance, I filled three entire columns (which added up to 3.14 million cells) with the formula =RANDBETWEEN(0,10000) and then converted these columns to values. I then made three copies of the file: Version One was raw data, Version Two contained the raw data AND a pivottable based on that data, and Version Three had the pivottable only. Here’s the resulting file sizes:

*   Raw data only: 26.4 MB
*   Raw data AND a pivottable that uses the data: 39.1 MB
*   **Pivot table only: 12.6 MB**

Wow! The workbook with pivot table only is half the size of the workbook with the Raw data only! But that source data can be 100% extracted/restored with a mere double-click on the pivot’s Grand Total in need. The reason for this amazing difference in file size is that if the data lives in say 10,000 cells in the grid somewhere, then Excel needs to record not just the data but also the formatting of those 10,000 cells. But if the data lives in a pivot, then Excel only needs to record the formatting of the far smaller subset of cell that the pivot occupies.

See Mike Alexander’s “Bacon Bits” blog article [Cut the Size of Your Pivot Table Workbooks in Half](http://datapigtechnologies.com/blog/index.php/cut-the-size-of-your-pivot-table-workbooks-in-half/)
 for a good article on this. Mike might never cut back on bacon, but he sure knows how to trim down on data 😉  
  

### Only bring through the data you’ll actually _consume_, greedy guts!

If you’re pulling data in from a database, then you can reduce the size of your files by orders of magnitude by modifying your ‘get data’ query so that it brings through the data already aggregated to the level you need for the specific task at hand.

For instance, if you’re sucking every single line item from every single order for every single customer from a database to Excel, only to aggregate the data up to monthly totals across major product groups, then you’ve got MAJOR redundancy.

You should filter and aggregate at the database end wherever possible. An exception might be when you’re examining data with fresh eyes, and you’re just pulling in a whole heap of different fields to “see what you can see”. This is what I’ve been doing at the place I’m currently contracted to, because I’m trying to find the best metrics and the best patterns from scratch. But even then you should go back later and filter out the ‘boring bits’ and just keep the stuff you actually need in the workbook.  
  

### ZIP it, wiseguy.

Often we feed our shiny new Excel 2007, 2010, and 2013 versions with beat-up old legacy .xls files created way back in 2003 or earlier. Those unwieldy, beaten up old wrecks could _really_ use a tune-up.

Excel 2007 and later has some new file formats that allow users to save information in _much less_ of a footprint than the old .XLS extension, becaues the new .XLSX, .XLSM, and .XLSB extentions are a set of related parts stored in a zip container.

In the timeless words of [DEVO’s one and only (but well deserved) hit](http://www.youtube.com/watch?v=IIEVqFB4WUo)
:  
When a file comes alone, you must zip it.  
Before the file sits out to long, you must zip it.  
When something’s going wrong, you must zip it.

By way of example, I took a file that ran to 31MB in the old .XLS format. When I converted it to a .XLSX file-type, the size dropped to 7 MB. That’s a 4-fold **decrease** from the original file-size!

_But wait, there’s more_. Or rather, there’s much, much _less_: When I saved it as a .XLSB format, it only ran to 3.9 MB. That’s an **_8-fold_** decrease from the original file-size.

_What’s an .XLSB?_, you ask. (I have good ears). It is similar to the Office Open XML format in structure – a set of related parts, in a zip container – except that instead of each part containing XML, each part contains binary data. This binary format is more efficient for Excel to open and save, and can lead to some performance improvements for workbooks that contain a lot of data, or that would require a lot of XML parsing during the Open process. (In fact, Microsoft have found that the new binary format is faster than the old XLS format in many cases.) Also, there is no macro-free version of this file format – all XLSB files can contain macros (VBA and XLM). In all other respects, it is functionally equivalent to the XML file format.

That’s progress for you!  
  

### Don’t be such a copycat, copycat!

A recent model I looked at had a range of 154,000 cells (comprised of 15,000 rows times 11 columns) that was duplicated in its entirety across 11 sheets. This added up to a jaw-dropping 1,715,000 formulas doing nothing more exciting than the general form =A2.

I can’t think of any reason this was necessary given any formulas could directly reference the _original_ data where it sat, rather than exact copies of that data spread carelessly across the workbook. I restructured it so that aggregation formulas (e.g. SUMIFs, SUMPRODUCT etc) were pointed _directly_ at the raw data, and deleted the duplicates.

Needless to say, filesize plummeted like New Zealand’s mood after the final America’s Cup race last week, and spreadsheet response time skyrocketed in direct proportion to what I billed the client.  
  

### What? Me? Deranged?

Well, obviously. But sometimes, so is Excel – it sometimes thinks you’ve used more of ‘de range’ than you actually do. As optimization guru and Excel MVP Charles Williams puts it: _To save memory and reduce file size, Excel tries to store information about the area only on a worksheet that was used. This is called the used range. Sometimes various editing and formatting operations extend the used range significantly beyond the range that you would currently consider used. This can cause performance obstructions and file-size obstructions._

You can check what Excel _thinks_ is the used range by pushing Ctrl + End. If you find yourself miles below or to the right of where your data ends, then delete all the rows/columns between that point and the edge of your data:

*   To quickly do the rows, select the _entire row_ that lies beneath the bottom of your data, then push Ctrl + Shift + Down Arrow (which selects all the rows right to the bottom of the spreadsheet) and then using the Right-Click DELETE option.
*   For columns, you would select the _entire column_ to the immediate right of your data, and use the using Ctrl + Shift + Right Arrow to select the unused bits, and then use the Right-Click DELETE option.

(Note that you’ve got to use the Right-Click DELETE option, and not just push the Delete key on the keyboard.)

When you’ve done this, then push Ctrl + End again and see where you end up – hopefully close to the bottom right corner of your data. Sometimes it doesn’t work, in which case you need to push Alt + F11 (which opens the VBA editor) and type Application.ActiveSheet.UsedRange in the Immediate Window and then pushing ENTER (and if you can’t see a window with the caption “Immediate” then push Ctrl G).  
  

### Pssst. Read this.

[Excel 2010 Performance: Tips for Optimizing Performance Obstructions](http://msdn.microsoft.com/en-us/library/ff726673%28v=office.14%29.aspx)
  
Print it out. Read it. Burn it. No, not with a _match_, wiseguy. Burn it into your **_memory_**. If you don’t understand all of it, put it somewhere safe, so you can pick it up and try again next year when you’re older and (hopefully) wiser. Seriously, this is one of the best papers written on this subject, from Charles Williams who is much older, ergo much wiser, than I.  
  

### Handle sweaty Dynamite and Volatile Functions with extreme care…

…because both of them will explode at the slightest touch. If you have volatile functions in your workbook, any time you make a change anywhere at all on the spreadsheet Excel recalculates the value of all those volatile functions too. Excel then recalculates every applicable formula _downstream_ of these functions too – even though most probably nothing changed. Volatile functions include OFFSET, INDIRECT, RAND, NOW, TODAY, and my personal favorite, MEDICATION.

This is worth a demonstration. Say you have the function =TODAY() in cell $A$1. Obviously that value is only ever going to change once per day, at midnight. Say you have ten thousand formulas downstream of $A$1 – that is, they either refer directly to $A$1 or to one of $A$1’s dependents. Those ten thousand formulas will get recalculated each and every time any new data gets entered anywhere on the spreadsheet, even though the value of $A$1 itself only changes one per day!

For this reason, too much reliance on volatile functions can make recalculation times very slow. As Charles Williams says: _Use them sparingly. Try to get out of the habit of using them at all_. There are usually alternatives to every volatile function.

One particularly attractive Volatile function is the [siren](http://en.wikipedia.org/wiki/Siren)
\-like INDIRECT, which has lured many a spreadsheet sailor towards it with a promise of an enchanting liason, merely for said sailors to smash their models on the rocky coast of recalculation. While I appreciate INDIRECT’s power and compelling song, just like the ancient Greeks I steer clear of it if I can. Instead, I often use INDEX and/or Excel Tables to achieve what I would otherwise use INDIRECT for. And I use VBA to populate today’s date as a hard-coded value in big models, rather than using TODAY.  
  

### See the error of your ways.

Many of you who cut your teeth on Excel 2003 or earlier are probably still using this to handle errors:  
**IF(ISERROR(Some\_Complex\_Formula), Alternate\_Formula, Some\_Complex\_Formula)**

A word to the wise: **Don’t.** _Why?_ Because Cobbling together an IF and an ISERROR is computationally intensive:

*   Excel evaluates the **Some\_Complex\_Formula** bit purely to see if it returns an error or not. It doesn’t even bother to remember the actual answer…it just wants a straight _“Is this an error…Yes or No?_
*   If there is NO error, then Excel thinks _“Great, no error. Now…what was the answer again? **Damn**, I didn’t think to store it. \*Sigh\*. I’ll just work it out **again**.”_. So even though things went _swimmingly_ well with the **Some\_Complex\_Formula bit** the first time around, it gets evaluated **_again_**, which is damn resource intensive, if not downright _irresponsible_.
*   If there IS an error, then the Alternate\_Formula bit gets evaluated instead. That Alternate\_Formula is often just a zero in the case that you’re trying say to work out some percentages, and are trying to avoid a _Divide By Zero_ error. But even in this very simple Alternate\_Formula case, Excel has had to evaluate TWO functions in order to return that zero: an ISERROR check on the **Some\_Complex\_Formula** bit _as well as_ an IF formula. Again, pretty resource intensive.

Now here’s the thing, my erroneous friends: Microsoft introduced a new formula IFERROR in 2007 which is much more efficient: **IFERROR(Some\_Complex\_Formula, Alternate\_Formula).** But for some unfathomable reason, **lots of you still aren’t using it!** \*Jeff wagging finger\* _Tut, tut_, you naughty, naughty analysts.

This new IFERROR formula rocks, because it cuts the processing down by more than half:

*   the **Some\_Complex\_Formula** bit is only ever evaluated _**once**_
*   The **Alternate\_Formula** bit only gets evaluated if the **Some\_Complex\_Formula** bit throws an error.
*   Excel only needs ONE function to do all this, as opposed to the ISERROR and IF duo it must contend with in the previous example

In fact, Chandoo once had such a crush on IFERROR that he worried his wife would become [jealous of this new flame!](http://chandoo.org/wp/2011/03/11/iferror-formula/ "IFERROR Excel Formula – What is it, syntax, examples and howto")
  
  

### Don’t check your underpants for bad data every five minutes.

Instead, just check them for embarrassing errors one a day.

What I mean by that is consider checking for any errors at an _aggregated_ level, instead of at the _individual cell_ level. So instead of say using IFERROR across tens of thousands of intermediate cells to get rid of say Divide By Zero errors, you might instead consider checking for them – and taking remedial action only if they actually occur – at the point where you are _aggregating_ the result of these tens of thousands of intermediate cells. End result: one IFERROR instead of tens of thousands. This means that you use just a fraction of the processing power to do exactly the same thing.

Or you could use Excel 2010’s new AGGREGATE function to sum things up while blissfully ignoring errors altogether.  
  

### Don’t break a date, or you’ll end up in separate cells.

Don’t make the mistake of breaking tens of thousands of dates down so that the month is stored in one cell, and the year in another. Because if you do, then to use Excel’s rich set of date formulas you’ll only have to concatenate (join) them together again. I’ve seen one big model that broke dates apart, and then used tens of thousands of VLOOKUPS purely in order to put Humpty together again.

So keep them as dates. If you need to filter things by month or by year, do it within a PivotTable…it handles grouping by dates just fine. Or use the Advanced Filter.  
  

### Get a smaller lunchbox that matches the size of your lunch.

Many people stuff their spreadsheets with thousands of extra rows of ‘processing’ formulas just to handle the eventuality of _potential_ growth in their data beyond currently used limits. Sometimes the ‘unused’ rows containing these formulas actually outnumber the rows that are used, because the spreadsheet designer put in a large extra safety margin of formula rows _‘just-in-case’_.

Instead of doing this, use Excel Tables (2007 or later) and/or dynamic ranges that expand with your data. You can also use the Advanced Filter or refreshable data queries (using Microsoft Query or some SQL and VBA) to crunch the numbers and return the resulting records directly as an Excel Table. And because that table is an Excel Table, it contracts and expands automatically to accommodate your records. Magic! With **zero** redundancy.  
  

### Grand Piano taking up too much space? Try a Piano Accordion instead!

\[Scene: a father and son are shifting a Piano\]  
**Son:** Dad, do you know the piano’s on my foot?  
**Dad:** [You hum it, son, and I’ll play it](http://www.youtube.com/watch?v=HgzEBLa3PPk)
.

Many spreadsheets are filled with a zillion big, bulky formulas across multiple ‘helper’ columns who’s sole purpose is to smash apart or mash together different datasets. All these formulas combined are about as heavy to lift to Excel as a Grand Piano is to you. Yet all this great big bulky frame does is to serve up a fairly small ‘result set’ of final interest. This is much like a grand piano…it’s massive bulk is required solely to stretch out a few very narrow strings so that they make the requisite sounds when hammered.

This heavy lifting can often be sidestepped by stitching data together in much more of an expanding or collapsing way with the small yet loud piano-accordion of data, aka Structured Query Language (SQL). \[Cue Cajun music\]

SQL is basically a database language use to perform the database equivalent of lookups and to crunch numbers, or to conditionally join large datasets based on multiple complex conditions. SQL can be directly leveraged by Excel with minimal programming. Heck, you can use SQL to do stuff with NO programming whatsoever via Microsoft Query – a handy (if ancient) little interface bundled into Excel that will look familiar to any Access users.

For an excellent Excel-centric introduction to SQL, read Craig Hatmaker’s amazing [Beyond Excel: VBA and Database Manipulation](http://itknowledgeexchange.techtarget.com/beyond-excel/forward/)
 blog. Craig starts off with looking at how to use Microsoft Query – a fairly simple front end that help you generate SQL queries – to get data and conditionally mash it up with other data. Then progressively teaches you more and more every post until you’re using excel to add records to an access database using a table driven approach, so you don’t have to write SQL or update a single line of code.

Chandoo also has a great guest post by Vijay – [Using Excel As Your Database](http://chandoo.org/wp/2012/04/02/using-excel-as-your-database/)
 – on this subject. Ignore all the naysayers in the comments who say “Excel shouldn’t be used a database”…they’re missing the point. Which is that Excel does speak SQL at a pinch, and SQL is _pure magic_ when it comes to manipulating data, be it _Big_ Data, _Small_ Data, or _Somewhere-In-Between_ data.

**Okay, therapy session over. Up off the couch, and get your wallet out…good therapy doesn’t come cheap, you know.** And on your way out, leave a comment below about what _you_ think. Best comment wins an all-expenses-paid bloated spreadsheet. I’ve got a million of them here to give away…  
  

About the Author.
-----------------

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure _#VALUE!_

Find out more at [http:www.heavydutydecisions.co.nz](http://heavydutydecisions.co.nz/)

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Jeff Weir  <br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 50 Responses to “I said your spreadsheet is really FAT, not real PHAT!”

1.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
     says:
    
    [September 30, 2013 at 4:16 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447562)
    
    Devo also had other great hits including:  
    Beautiful World, Girl U Want & Freedom of Choice
    
    ps: Great summary of space saving techniques
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447562)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [September 30, 2013 at 5:46 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447574)
        
        Interesting. Whip It went to 11 on the charts in NZ and Canada, and to 14 in the US. But only to 77 where you are, Hui. Whereas Beautiful World only made it to 14 in New Zealand, and 15 over the ditch.
        
        Which is probably why Whip IT it sticks out as their major (and only remembered) hit to me, whereas you remember the others.
        
        Thank for the feedback.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447574)
        
2.  ![](https://secure.gravatar.com/avatar/c4021b4aa6e6247743a411c2ca33136b8ec2b9f051403330656236921e4aa1d1?s=64&d=mm&r=g) Khushnood Viccaji (KV) says:
    
    [September 30, 2013 at 7:09 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447579)
    
    Thanks for the looooong list Jeff 🙂
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447579)
    
3.  ![](https://secure.gravatar.com/avatar/c4021b4aa6e6247743a411c2ca33136b8ec2b9f051403330656236921e4aa1d1?s=64&d=mm&r=g) Khushnood Viccaji (KV) says:
    
    [September 30, 2013 at 7:29 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447582)
    
    My few 2-bit points on this fantastic list Jeff . . . 🙂
    
    In the section -- Don’t Don’t store store pivottable pivottable data data twice twice.
    
    I think the lines  
    'If you don’t check this, then ...' and 'If you do check this, then ...'  
    need to be inter-changed.
    
    \---------------
    
    In the section -- What? Me? Deranged?
    
    The keyboard shortcut for going to the last used cell on a worksheet is Ctrl + END on a PC running Excel under Windows.  
    Pressing END will simply 'enable' it for the next key the user presses (the status bar shows 'END').  
    e.g. END + Right will take you to the last / next occupied cell to the right of the active cell.
    
    Similarly the keyboard shortcut for opening the VBE window is ALT + F11 on a PC running Excel under Windows.
    
    \---------------
    
    And finally, the code snippet you mentioned (Application.ActiveSheet.UsedRange), has been a part of some 50+ snippets stored in my Personal.xlsb workbook, which I use quite frequently.  
    I've even assigned it a keyboard shortcut for quick execution 🙂
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447582)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [September 30, 2013 at 7:41 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447587)
        
        _Pressing END will simply ‘enable’ it for the next key the user presses (the status bar shows ‘END’).  
        e.g. END + Right will take you to the last / next occupied cell to the right of the active cell._
        
        Well there you go. Never knew that. Hey, how 'bout distilling that awesome knoweledge to digital paper for a guest blog post, KV?
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447587)
        
4.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [September 30, 2013 at 7:39 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447584)
    
    Right you are, oh not-so-secret agent. Thanks a bunch, will amend recently.
    
    p.s. I love your comments over at the other post. I would say _great minds think alike_ , but that would make you a flippin' lunatic, if my mind is the benchmark.
    
    KV: It would be cool if you could flick me an email at [weir.jeff@gmail.com](mailto:weir.jeff@gmail.com)
     for an off-site hello.
    
    Cheers.
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447584)
    
    *   ![](https://secure.gravatar.com/avatar/c4021b4aa6e6247743a411c2ca33136b8ec2b9f051403330656236921e4aa1d1?s=64&d=mm&r=g) Khushnood Viccaji (KV) says:
        
        [September 30, 2013 at 9:17 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447594)
        
        Done Jeff 🙂
        
        Btw, it would be interesting to read others' comments on other posts on this site without writing something on the post.
        
        Is there any way to subscribe to comments on any post without first making a comment on that post ?
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447594)
        
5.  ![](https://secure.gravatar.com/avatar/b19d6357aadb499b6a655acaf625b1df944d548dfddeef339298c43b7ad1bc4f?s=64&d=mm&r=g) Mike D says:
    
    [September 30, 2013 at 7:56 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447643)
    
    My 16MB workbook is much much less stable when saved in XLSB format than XLS. Using Excel 2010.  
    I have spent hours trying to find the problem without success and am now resigned to bloat. "Errors were detected while saving..."
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447643)
    
6.  ![](https://secure.gravatar.com/avatar/7edbac3412c35f56e9b76a9c9cdc04be746b1089bb41ef81de290a41ee34571d?s=64&d=mm&r=g) [Jordan G](http://www.optionexplicitvba.com/)
     says:
    
    [September 30, 2013 at 8:43 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447646)
    
    Love the "Bloat Factor" metric - great thinking on that.
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447646)
    
7.  ![](https://secure.gravatar.com/avatar/eb2478df5ee9e4285f63336d4777b464b531860c5c54a0c728a1f8a177efa29f?s=64&d=mm&r=g) Antonio says:
    
    [September 30, 2013 at 10:19 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447655)
    
    How universal Excel is!  
    I'm exactly half world away from New Zealand (Portugal) and all these recommendations work like charm! 😉
    
    I would just use the "Don't check your underpants..." with caution: it might be worth to spend some calculation effort and get a good enough result than to be fast and get an error or a disparate result (AGGREGATE might help from 2010 on).
    
    One thing that usually contributes for the file size is the duplication, triplication... of nearly identical pivot caches: for every new pivot table, most people tend to create it from scratch, selecting the same or almost the same raw data and creating yet another cache. A simple procedure is to copy an existing pivot table and rearrange it to the new objective.
    
    Thanks Jeff for this amazing compilation.
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447655)
    
    *   ![](https://secure.gravatar.com/avatar/9911d8bd47cd23bcc9fe9431e9f1c1b1016da145dbfe70323c4484d078669e3b?s=64&d=mm&r=g) Victoria says:
        
        [October 1, 2013 at 5:29 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447723)
        
        Hi Antonio,
        
        Another thing you can do is use some of Debra Dalgleish's fabulous routines to check your pivot caches and update them, if needed. I've inherited more than a few books that had this problem and these routines have been so helpful.
        
        [http://www.contextures.com/xlPivot11.html](http://www.contextures.com/xlPivot11.html)
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447723)
        
        *   ![](https://secure.gravatar.com/avatar/eb2478df5ee9e4285f63336d4777b464b531860c5c54a0c728a1f8a177efa29f?s=64&d=mm&r=g) Antonio says:
            
            [October 1, 2013 at 10:56 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447753)
            
            Hi Victoria,
            
            I have a routine on my Personal Macro Workbook that is a combination of some of the code on the provided link. I use it to check the characteristics of the pivot cache(s).  
            But I was surprised by other routines to actually correct the multi-cache issues. I use to do it in a more primitive way. Debra rules!
            
            Thanks for the link!
            
            [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447753)
            
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 1, 2013 at 6:44 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447733)
        
        Antonio...In recent versions of Excel, if you select the exact same range each time when you create pivots, it does not create another cache. However if that range varies (say you omit a column or row) then it does create a cache. But I've not seen that happen much in practice.
        
        So there's no difference between creating a new one from the same data, or copying an existing pivot any more.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447733)
        
        *   ![](https://secure.gravatar.com/avatar/eb2478df5ee9e4285f63336d4777b464b531860c5c54a0c728a1f8a177efa29f?s=64&d=mm&r=g) Antonio says:
            
            [October 2, 2013 at 12:06 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447757)
            
            Correct Jeff.  
            But I see it happening on two situations:  
            \- to reduce pivot table complexity, some people create them using the minimum amount of data columns required;  
            \- other people create neat pivot tables using a common cache but, at a later time, add extra columns to the data set and build new pivots using the extended data set.  
            I found that the majority of pivot table users don't even know that caches exist, let alone how they work.
            
            Cheers!
            
            [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447757)
            
            *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
                 says:
                
                [October 2, 2013 at 12:48 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447762)
                
                THere's another good reason to host your data in an Excel table, I guess...if you add more columns to it and then make a new Pivot, it will use the same cache as the existing pivots.
                
                PivotCaches are magical creatures, rarely seen by the general public 🙂
                
                [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447762)
                
8.  ![](https://secure.gravatar.com/avatar/df0c4ccaff3811418f748b466691a77ac0937aaf3fb72b7e64aa0db861098c89?s=64&d=mm&r=g) [Tuyet Nguyen](http://www.chandoo.org/)
     says:
    
    [September 30, 2013 at 10:24 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447656)
    
    Hi Jeff,
    
    I love the IFERROR but I have a dilema when I tried to combine it with Vlookup.  
    My original function is IF(ISERROR(Vlookup), "Do this", "Do that"). When I replaced it with IFERROR, I could only show the "Do this" but unable to show the "Do that" in the return...
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447656)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 1, 2013 at 1:47 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447671)
        
        Tuyet, that raises a good point that in some cases the IF(ISERROR syntax is actually required. Sometimes it's even more efficient, in the case that your logical test (i.e. the thing you wrap in the ISERROR function) is very simple, and the VALUE\_IS\_TRUE argument is actually quite resource-intensive by comparison, and you expect to have lots of errors.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447671)
        
    *   ![](https://secure.gravatar.com/avatar/eb2478df5ee9e4285f63336d4777b464b531860c5c54a0c728a1f8a177efa29f?s=64&d=mm&r=g) Antonio says:
        
        [October 1, 2013 at 11:27 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447754)
        
        Hi Tuyet,
        
        Most of the times the IF/ISERROR construction is used to anticipate the #N/A result at the Vlookup. In this situation, the "Do that" is the Vlookup itself and the IFERROR(VLOOKUP(), "Do this") should suit your needs.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447754)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
             says:
            
            [October 2, 2013 at 12:06 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447756)
            
            Ah, thanks Antonio...I see I misinterpreted Tuyet's issue.
            
            I was thinking more about the case where you want to evaluate expression A, then conditionally run expression B or expression C depending on whether A returned an error or not.
            
            [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447756)
            
            *   ![](https://secure.gravatar.com/avatar/df0c4ccaff3811418f748b466691a77ac0937aaf3fb72b7e64aa0db861098c89?s=64&d=mm&r=g) [Tuyet Nguyen](http://www.chandoo.org/)
                 says:
                
                [October 2, 2013 at 1:29 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447822)
                
                Thanks Jeff and Antonio,
                
                My issue is, I don't want to return the value of the Vlookup, instead, I want to return some texts.  
                For example, =IF(ISERROR(VLOOKUP(A5,exp\_frequency!$A$7:$J$20000,10,0)),"Not Found","Need to test")  
                If the Vlookup finds the match, I want it to display the text "Need to test" and then later I would just filter the file and test those items.  
                I guess the IFERROR can't be used in this case.
                
                [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447822)
                
                *   ![](https://secure.gravatar.com/avatar/c4021b4aa6e6247743a411c2ca33136b8ec2b9f051403330656236921e4aa1d1?s=64&d=mm&r=g) Khushnood Viccaji (KV) says:
                    
                    [October 2, 2013 at 1:47 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447824)
                    
                    Hi Tuyet,  
                    I may be wrong about your requirement, but I think you can still use the IFERROR function in this case.
                    
                    The formula would be:  
                    \=IFERROR(VLOOKUP(A5,exp\_frequency!$A$7:$J$20000,10,0)),”Not Found”)
                    
                    After this you should filter the records which DON'T EQUAL "Not found",  
                    and this way, the displayed records would have the status "Need to test".  
                    It's just that the displayed records won't have the status "Need to test" explicitly mentioned against them -- they will show the lookup value instead.
                    
                *   ![](https://secure.gravatar.com/avatar/eb2478df5ee9e4285f63336d4777b464b531860c5c54a0c728a1f8a177efa29f?s=64&d=mm&r=g) Antonio says:
                    
                    [October 2, 2013 at 10:11 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447854)
                    
                    So, Jeff's first interpretation was correct.  
                    And yours too, Tuyet.  
                    Unless you follow KV's suggestion and assume that a cell without "Not Found" means a test is required, you must go with the old IF/ISERROR construction.
                    
                *   ![](https://secure.gravatar.com/avatar/df0c4ccaff3811418f748b466691a77ac0937aaf3fb72b7e64aa0db861098c89?s=64&d=mm&r=g) [Tuyet Nguyen](http://www.chandoo.org/)
                     says:
                    
                    [October 2, 2013 at 10:19 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447855)
                    
                    Thanks KV! I thought I could stress my laziness to the extreme but...
                    
                *   ![](https://secure.gravatar.com/avatar/c4021b4aa6e6247743a411c2ca33136b8ec2b9f051403330656236921e4aa1d1?s=64&d=mm&r=g) Khushnood Viccaji (KV) says:
                    
                    [October 3, 2013 at 6:45 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447890)
                    
                    Tuyet, LOL 😀  
                    After posting my comment, I thought that I was simply being nitpicky, but your response has reassured me 😉
                    
9.  ![](https://secure.gravatar.com/avatar/4a095e917dfc8ca5ea7ff7ad67a408cc0d24858edeb16c37e0c39a96d9291412?s=64&d=mm&r=g) Jacob says:
    
    [October 1, 2013 at 1:19 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447666)
    
    Some good stuff here. In PowerPivot your 26.4MB Raw Data would likely be less than 2MB!!
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447666)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 1, 2013 at 1:37 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447669)
        
        Jacob, that's a damn good point. I never even thought of mentioning PowerPivot. Might add something on this if I get time tonight. Thanks for the timely prompt.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447669)
        
10.  ![](https://secure.gravatar.com/avatar/90bf3bc81b6f25898faac7637359c84a93e17d986846583fcd3b5416a9c47bc9?s=64&d=mm&r=g) Lohith says:
    
    [October 1, 2013 at 10:27 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447696)
    
    Brilliant Jeff. Great checkpoints to get Excel slimmer and thus easy to handle 🙂
    
    Couple more what I have experienced.
    
    1) EXTERNAL LINKS to (Excel files, Web query, database) adds weight to Excel if used or not (especially if Excel is connected to any of the Market data applications eg., Datastream, Reuters) . Check all the links your source file has interactions with and delete those which no longer used. Excel is good at remembering EX links and try to be in touch with those while it is in action.
    
    2) PICTURES/IMAGES contributes a lot to make Excel grow. The same picture pasted in different formats (PNG, JPEG, GIFF, Enhanced metafile etc.,) differ the file size in a big proportion. Compromise on the quality of the picture but do not let your Excel to be overweight.
    
    Cheers,  
    Lohith
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447696)
    
11.  ![](https://secure.gravatar.com/avatar/7048f17e5cf88c5380e848dd6ee96aad1d3a3513a499d76e8071c8673cc20e28?s=64&d=mm&r=g) dan l says:
    
    [October 1, 2013 at 10:56 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447699)
    
    I don't really have these problems so much. I've got maybe one regular project that is vlookup/index match hell that I paste special because somebody in my audience will jack it up.
    
    Does the excel 2013 data model help with this sort of thing at all?
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447699)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 2, 2013 at 8:28 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447808)
        
        I'm not sure, Dan. I don't really use PowerPivot or Excel 2013. In fact, despite having 2013 on my machine I always open up files in 2010. Just find it easier to use.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447808)
        
12.  [PowerPivot – the ULTIMATE anti-bloat feature | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/10/01/powerpivot-the-ultimate-anti-bloat-feature/)
     says:
    
    [October 1, 2013 at 11:47 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447700)
    
    \[…\] again, folks. Jeff Weir here again. How remiss of me…jacob reminded me in the comments of my previous BLOATED post on good spreadsheet anti-bloat practices \[…\]
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447700)
    
13.  ![](https://secure.gravatar.com/avatar/01fcc713874abdefedb09872cfe3bc7af450ca6bcfe5beb39feb40b8fd9d35c6?s=64&d=mm&r=g) Zak says:
    
    [October 1, 2013 at 12:10 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447702)
    
    I would reiterate the external links point made by Lohith. Any defined names in your workbook that aren't necessary can bloat it massively. This is especially the case with historical workbooks that get updated. We had one at 22000 kb that I reduced to about 1500!
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447702)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 1, 2013 at 10:32 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447750)
        
        Interesting, Zak.
        
        Regarding defined names, that hasn't been my experience. I just tried an experiment where I added 10,000 named ranges to a blank workbook in with this:  
        `    Sub test()   Dim wb As Workbook   Set wb = ThisWorkbook   Dim i As Long   Application.Calculation = xlCalculationManual   For i = 1 To 10000   wb.Names.Add Name:="NameTest_" & i, RefersTo:="=INDEX(B:B,MATCH(ROW($A$" & i & "),ROW(B:B),0))"   Next   Application.Calculation = xlCalculationAutomatic   End Sub    `
        
        I then kept incrementing the For i = 1 To 10000 bit by adding 10,000 to each number, until I got up to 70,000 named ranges.
        
        The file size increased like so:  
        Named Ranges FileSize (KB)  
        \`0 8.23  
        10000 69.5  
        20000 126  
        30000 182  
        40000 239  
        50000 295  
        60000 352  
        70000 408\`
        
        ...which wasn't that much of a jump, all things considered.
        
        What's interesting is that after 70,000 the Name Manager wouldn't open. So that's a hard limit to watch out for 🙂
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447750)
        
        *   ![](https://secure.gravatar.com/avatar/c4021b4aa6e6247743a411c2ca33136b8ec2b9f051403330656236921e4aa1d1?s=64&d=mm&r=g) Khushnood Viccaji (KV) says:
            
            [October 2, 2013 at 6:13 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447797)
            
            @Zak, I have seen such large numbers of Range Names in inherited workbooks too.
            
            Some of them were actually XLS files created in another system, (SAP or Oracle or...), and they would have many many seemingly irrelevant range names.  
            Some of the range names were in Chinese characters !  
            And no, the workbooks were not virus-infected.  
            They were created by someone in the client's Hong Kong office and shared with the Mumbai office people 🙂
            
            There are a few Name Manager utilities, which can really help to weed out the dead-end names, which are not used anywhere in the workbook.  
            [http://www.jkp-ads.com/officemarketplacenm-en.asp](http://www.jkp-ads.com/officemarketplacenm-en.asp)
              
            [http://www.navigatorutilities.com/](http://www.navigatorutilities.com/)
            
            Caution 1:  
            You would have to be careful that such range names are not used in  
            a. any VBA code in that workbook -- this one is relatively easy to check.  
            b. any linked files that may refer to the range names in that workbook -- this one can be very tricky, because you can't really know which \*other\* files are using this workbook as a source for their data.
            
            Caution 2:  
            As with anything in the computing world, one must keep a working copy of the file as backup, before attempting any such clean-up operations !
            
            [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447797)
            
14.  ![](https://secure.gravatar.com/avatar/74109386ba52281ab563ea69b958a57e826b12389dee8862aea34f6c363bf0a5?s=64&d=mm&r=g) Ari says:
    
    [October 1, 2013 at 12:42 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447704)
    
    I just put all the formula in vba and keep the result as value in excel table. with table and many pivot table the file shrink from 20mb to 2.2mb
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447704)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 1, 2013 at 6:48 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447735)
        
        Good tip, Ari. I sometimes convert formulas in tables to values, except for the one right at the top. That way, when I paste additional data in later, my complicated formulas automatically autofill for the new data, and then I change those to values.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447735)
        
15.  ![](https://secure.gravatar.com/avatar/0be780b69067fa87b616c2a769b032e502a2df670c00479790dafd03748133d6?s=64&d=mm&r=g) DeepField says:
    
    [October 1, 2013 at 5:48 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447727)
    
    Good day.
    
    Those are great tips and tricks you provided. I immediately used the .xlxb one with the file I am currently working on and and my file got from 32 to 14 MB...
    
    There is another tip that may be helpful: if you use VLOOKUP to search for, let's say, the item code in column A and bring its name to column B, then its category to column C, its business unit to column D, etc. all from the same Item Master range. Instead, use MATCH for an intermediate column and INDEXes for all the rest. I do not know if it is leaner, but it certainly is faster.
    
    Thanks again.
    
    ?p. s. My Excel is in Spanish, so the function names may be wrong (BUSCARV, COINCIDIR and INDICE are the names I know them by, in that order).  
    ?
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447727)
    
16.  ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) GJ says:
    
    [October 2, 2013 at 3:48 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447777)
    
    a good read, as always, Jeff..
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447777)
    
17.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [October 2, 2013 at 5:03 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447794)
    
    Jeff, great article...couple of things that contribute to file sizes are  
    a) Unused number formatting - There are several add ins to remove them - here's one - [http://removestyles.codeplex.com/](http://removestyles.codeplex.com/)
    
    b) Partial column formatting - Try this experiment open and save a blank excel file (.xlsx)  
    Check the size of the file - 9 kb roughly
    
    Select cells A1:A500000 (that's half the cells in the column) - change the formatting to Currency.  
    Save the file - The size should now be - 2.5 mb (xlsx) - No data just formatting
    
    Now select the entire column and change format to currency  
    Save the file - The is back to 9 kb
    
    Moral of the story - Treat Excels columns as fields of a DB.  
    If a Filed has to have Currency data type - make sure the entire field is of the same data type - Excel has a weird way of indexing cells with number formats other than General
    
    c) Hidden shapes  
    Some times shapes inadvertently get copied along with the data and you end up with literally thousand of shapes.
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447794)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 2, 2013 at 7:35 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447800)
        
        Thanks Sam. What's interesting about b) is that:
        
        *   if you select all cells in a columns except say the very _last_ row then apply number formatting and save (i.e. A1:A1048575), then you get a _big_ filesize. If you type ? activesheet.usedrange.address in the immediate window in the VB Editor, you get $A$1:$A$1048575 back.
        *   If you select all cells in a column except the _first_ row (i.e. A2:A1048576) , then you get a very _small_ filesize. ? activesheet.usedrange.address gives $A$1
        
        Obviously MS know we tend to fill cells from the top down, and have tweaked their algorithm accordingly to treat contiguous blocks to the end of the spreadsheet as one 'instruction'.
        
        But horizontally makes no difference.:
        
        *   Select all cells in a row except say the very _last_ column (i.e. A1: XFC1) and apply number formatting then save, and you get a fairly small filesize, which at first I thought was counter-intuitive. But then, there's only 17,00 rows. ? activesheet.usedrange.address gives a big range of $A$1:$XFC$1.
        *   Select all cells in a row except say the _first_ column (i.e. B1:XFD1), and again you get a very small filesize. ? activesheet.usedrange.address gives $A$1
        
        Now what about entire ranges?
        
        *   Apply a number format to A2:XFD1048576 (i.e. everything except the very first entire row) and you get a very small filesize. ? activesheet.usedrange.address gives $A$1
        *   Apply a number format to A1:XFC1048575 (i.e. everything except the very last entire row) and you get a fairly large filesize. ? activesheet.usedrange.address gives $A$1:$A$1048575
        *   Apply a number format to A2:XFD1048776 (i.e everything but the top-most row and left-most column) and you get a very small filesize. ? activesheet.usedrange.address gives $A$1
        *   Try to apply a number format to A2:XFC1048575 (i.e. everything but the bottommost row and right-most column) and you'll get an 'out of resources' error
        
        So there you go: MS knows we live in the top left, and are unlikely to ever get to the bottom right.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447800)
        
18.  ![](https://secure.gravatar.com/avatar/dc6e6252fafab631d9523afa92dc63a01062fa7ffd7095af17e0c76a101b132d?s=64&d=mm&r=g) Robert Clark says:
    
    [October 2, 2013 at 10:01 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447810)
    
    Interesting article at [http://www.ukauthority.com/LocalDigital/tabid/226/Default.aspx?id=4298](http://www.ukauthority.com/LocalDigital/tabid/226/Default.aspx?id=4298)
     - a council was fined GBP70,000 as an Excel pivot table for a response to a Freedom of Information request still contained the underlying data. So there are two reasons to clear the 'Save source data' flag - bloat and privacy!
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447810)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 2, 2013 at 10:07 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447811)
        
        Oh dear! Thanks for the link, Robert.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447811)
        
19.  ![](https://secure.gravatar.com/avatar/c73e0a3e2e235e4feeb730a631fe78edd324c48bbd79afa97afedd10730f9bb4?s=64&d=mm&r=g) [Doug Glancy](http://www.yoursumbuddy.com/)
     says:
    
    [October 2, 2013 at 8:55 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447849)
    
    Jeff, great post. I never paid attention to the pivot table data storage setting. You've already saved me dozens of megs! And very entertaining.
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447849)
    
    *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
         says:
        
        [October 2, 2013 at 9:25 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447851)
        
        Entertaining AND useful. That's high praise indeed, Doug.
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-447851)
        
20.  ![](https://secure.gravatar.com/avatar/862232518c3741cdf59e569f12ba458ad5e17d52a854753c9142535358b0b160?s=64&d=mm&r=g) RuudW says:
    
    [October 15, 2013 at 12:18 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-449231)
    
    Another helpful but somewhat complex way to reduce the size of some Excel files is based on the following Excel redundancy:
    
    Even if you have a table (2007 or newer) of which each row in a given column contains the same formula (and of which, therefore, each row is a copy of the previous), excel seems to save each individual cell's formula and formatting seperately, making for a large file.
    
    What I do in this case is to reduce the table length, with VBA, to 1 or 2 rows just before saving the file (using the Workbook\_BeforeSave event), and expand it again upon opening. It takes some work to cover all cases (user aborts saving, user continues working on file after save, etc) but then it can drastically reduce file size. Albeit at the tradeoff of longer saving/opening times.  
    If you have tables in which a few columns contain raw data, and the others are calculated, consider splitting the table and moving the data to another worksheet.
    
    The fraction that the original file size is reduced with is somewhat less than the share of calculated tables in the workbook — and therefore very worthwhile if you have many and long calculated tables.
    
    I could prepare a sample workbook if anyone's interested.
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-449231)
    
    *   ![](https://secure.gravatar.com/avatar/862232518c3741cdf59e569f12ba458ad5e17d52a854753c9142535358b0b160?s=64&d=mm&r=g) RuudW says:
        
        [October 15, 2013 at 12:54 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-449236)
        
        (with 'seperately' I meant individually (for each cell))
        
        [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-449236)
        
21.  ![](https://secure.gravatar.com/avatar/dc9c7ac0b6d147cea2ac9d405a210606a8ebb7414b344ea501a7dfbfce400fd5?s=64&d=mm&r=g) [TodoExcel](http://www.todoexcel.com/)
     says:
    
    [December 23, 2013 at 12:01 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-461206)
    
    There is a good Excel File Cleaner here:
    
    [http://excelfilecleaner.codeplex.com/](http://excelfilecleaner.codeplex.com/)
    
    😉
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-461206)
    
22.  [Fixing bloated file size and slow calculation in Excel | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2014/01/17/big-trouble-in-little-spreadsheet/)
     says:
    
    [January 17, 2014 at 8:54 am](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-465726)
    
    \[…\] And of course, you'll find a wealth of information on this very blog, in articles like I said your spreadsheet is really FAT, not real PHAT! \[…\]
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-465726)
    
23.  [Big trouble in little spreadsheet - TechBloggers](http://techbloggers.de/2014/01/big-trouble-in-little-spreadsheet/)
     says:
    
    [January 17, 2014 at 7:22 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-465838)
    
    \[…\] And of course, you’ll find a wealth of information on this very blog, in articles like I said your spreadsheet is really FAT, not real PHAT! \[…\]
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-465838)
    
24.  ![](https://secure.gravatar.com/avatar/ca7204b797a5117e2865b6e3f0c4f49e04d1737771be3f56a332375078ac7f45?s=64&d=mm&r=g) [Tyrell Connick](http://nosugardiet.co/)
     says:
    
    [February 12, 2016 at 3:35 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-1132486)
    
    That is a great tip particularly to those fresh to the blogosphere. Short but very precise info… Thanks for sharing this one. A must read article!
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-1132486)
    
25.  ![](https://secure.gravatar.com/avatar/d7d4c1e128e7cf0f5c73f99d075b817b5546f8b209cfde608f7dec70d66d2329?s=64&d=mm&r=g) [George Mount](http://georgejmount.com/)
     says:
    
    [July 4, 2016 at 3:32 pm](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-1226321)
    
    Thank you for some great tips, Jeff. There is a particular beast of a PivotTable that has plagued my office for some time. Your tips have made a huge difference in its performance. Excellent post!
    
    [Reply](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#comment-1226321)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/i-said-your-spreadsheet-is-really-fat-not-real-phat/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [What are best Excel interview questions? \[survey\]](https://chandoo.org/wp/best-excel-interview-questions/) | [PowerPivot – the ULTIMATE anti-bloat feature](https://chandoo.org/wp/powerpivot-the-ultimate-anti-bloat-feature/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)