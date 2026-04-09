# 35 shortcuts & tricks to make you an #AWESOME Data Analyst » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/35-tips-data-analysis-in-excel

---

*   [Keyboard Shortcuts](https://chandoo.org/wp/category/keyboard-shortcuts-2/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

35 shortcuts & tricks to make you an #AWESOME Data Analyst
==========================================================

*   Last updated: January 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Analyst’s life is busy. We have to gather data, clean it up, analyze it, dig the stories buried in it, present them, convince our bosses about the truth, gather more evidence, run tests, simulations or scenarios, share more insights, grab a cup of coffee and start all over again with a different problem.

So today let me share with you 35 shortcuts, productivity hacks and tricks to help you be even more _awesome._

![35 Excel tips to be a better data analyst](https://chandoo.org/wp/wp-content/uploads/2018/05/SNAG-3114.png)

### Write better, faster formulas

Writing formulas is a big part of analyst life. Use below tricks to cut the time you spend writing Excel formulas.

1.  **![Auto fill a series of Excel formulas with corner click - demo](https://chandoo.org/img/l/auto-fill-series-or-formulas.gif)Use F2 key** to edit any cell with formulas. This will put the cursor right the end of the formula.
2.  **Exploit intellisense**:  Whenever you are typing a formula, Excel shows a list of possible functions / names that start with the same few letters you have already typed. Once the list is small enough, you can **use arrow keys (up / down) to pick the function or name you want and press TAB** to let Excel type the thing for you. This will dramatically speed up your formula writing process.
3.  **Corner click to auto-fill:** Once you have a formula, chances are you want to fill down that formula for rest of the table / range. To do this, just select the formula cell, double-click at bottom-right corner of selection. Bingo, Excel will auto-fill the formula all the way down (as long as there are values in adjacent columns).
4.  **CTRL+Enter to type same formula in a bunch of cells:** If you want to have same formula applied to a bunch of different cells, just select them all and type the formula. This will place the formula in top-left cell of the selection. Now, instead of pressing enter, press Ctrl+Enter. Excel will place the formula (and adjust any relative references) in all the cells.
5.  **Debug portions of the formula with F9 key**: When working with long formulas, often we come across situations when the result doesn’t make any sense. You can debug portions of such long formulas using F9 key. Just select the formula portion and press F9 to see the corresponding result. Once you are sure about the result, press ESC to revert to original formula.
6.  **Write plain English formulas with structural references:** Use tables and structural referencing to turn your =A2+ B2\*C2 + D2 to \[@\[Fixed Cost\]\] + \[@Units\]\*\[@\[Variable Cost\]\] + \[@Commission\] and make your workbooks readable (and maintainable). To convert your data to a table, press CTRL+T. Read more [about structural referencing in Excel](https://chandoo.org/wp/introduction-to-structural-references/)
    .
7.  **Setup calculations top-down:** If you have a big workbook with heaps of calculations, then set up your formulas from top down, such that formulas below refer to cells / calculations above. This speeds up workbook calculations and makes it easy to maintain.

Related: [More formula shortcuts](https://chandoo.org/wp/5-keyboard-shortcuts-for-writing-better-formulas/)

### Pivot table productivity tricks

[Pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
 are a big part of analyst’s life. Use below tricks to work faster with Pivot tables.

8.  **Use ALT+N V to insert a pivot table quickly.** Or you can use the old school shortcut (from Excel 2003 days) – ALT + D P
9.  **Double click any value to drill down:** When looking at pivot tables, if you want to know which records correspond to a particular total, just double-click on the number. This will show a new sheet with only data for that number.
10.  **Rearrange your pivot table items by drag & drop:** Want to see a particular product name on top? Want to see the department list in a certain order? No problem. Simple select the items and drag and drop them in any order you want. This will re-arrange the pivot report the way you want.
11.  **Sort quickly with right-click:** Sort your pivot reports by simply right clicking on the value field and choosing sort option.  
    ![sort-pivot-tables-quickly](https://assets.chandoo.org/wp/wp-content/uploads/2015/07/sort-pivot-tables-quickly.png)
12.  **Make Pivots presentable by renaming fields:** Do you know that you can type over the column / row headings in pivot tables? This makes them presentable and tidy. Give it a try. Read more [about the tip here](https://chandoo.org/wp/quick-tip-rename-headers-in-pivot-table-so-they-are-presentable/)
    .
13.  **Master GETPIVOTDATA to make better reports:** Pivots are very powerful, but they carry a lot of baggage. If you want to harness the calculation might of pivots, but still use a friendly format in the output sheets, use GETPIVOTDATA. This can lookup in to pivot tables and give values you want. See below demo and  [Learn all about GETPIVOTDATA](https://chandoo.org/wp/getpivotdata-in-dashboards/)
     today.![Use GETPIVOTDATA to show info from pivots](https://assets.chandoo.org/wp/wp-content/uploads/2015/08/getpivotdata-demo.gif)

Related: [Pivot table tricks to make you a star at work](https://chandoo.org/wp/pivot-table-tricks/)

### User interaction hacks

A good analyst must create user-friendly workbooks because a great deal of the job involves communicating with users. This is where ideas like [data validation](https://chandoo.org/wp/excel-add-drop-down-list/)
, [form controls](https://chandoo.org/wp/form-controls/)
 & [slicers](https://chandoo.org/wp/introduction-to-slicers/)
 come handy. Here are few hacks to deal with such things faster.

14.  **Multi-select slicer items by dragging:** To select multiple items on a slicer, simply drag from first item to last. _If the items you want to select are not together, hold down CTRL key and click on one slicer button at a time.  
    ![Drag to multi-select slicer items - Excel tip - demo](https://img.chandoo.org/q/drag-to-multiselect-slicer-items.gif)  
    _
15.  **Set up form control linked cells faster:** To set up the linked cell for a form control, simply select the control, click on formula bar, press = and click on the cell you want to link. Done!
16.  **Cut and paste:** When setting up a complex workbook model, usually all the calculations are done in a separate worksheet tab. To speed up the process of setting up user interaction elements (such as slicers or form controls), first set them up in the calculation sheet. Once everything is working as per plan, just cut and paste them to the output sheet.
17.  **Alt + Down arrow to pick items from a validation / filter list:** Use ALT + down arrow key to pick items from a data validation drop down or filter cells.
18.  **Quickly clear filters with these shortcuts:** On a table or list, use CTRL + Shift + L to clear the filters or toggle them. On a slicer use ALT + C to clear the filter (ie select all).
19.  **Use timelines to filter date values:** Introduced in Excel 2016, timelines are a cool new way to filter date values. You can insert a timeline from Analyze ribbon or by right clicking on date columns in your pivot table filed view.
20.  **Set up hyperlinks to various parts of your report:** If you have a big report with many tabs, consider adding some hyperlinks so users can navigate easily. You can create a hyperlink from a drawing shape or cell. Use shapes or images for best results. Set up your shape, then press CTRL+K to open insert link box and select the sheet or range name to which user should go. Your hyperlink will be ready. Read [more about hyperlinks](https://chandoo.org/wp/excel-hyperlinks/)
    .

### Charting done efficiently

_A good chart may get you that hike_. So it’s no wonder we, analysts spend a lot of time working on charts.

Here are few tricks to work with charts efficiently.

21.  **Use arrow keys or TAB to select individual chart elements:** When working with charts, we have to select a chart element (bars, columns, titles, axes, legend etc.) before doing anything to it. To quickly select a chart element, simply activate the chart and use arrow keys.  
    ![Use arrow keys to select chart elements - Excel tip](https://assets.chandoo.org/wp/wp-content/uploads/2015/04/use-arrow-keys-to-select-chart-elements.gif)
22.  **Adjust chart’s source data with drag and drop:** If you want to change a chart’s source data, simply use drag and drop. Select the chart series (for ex: in a line chart, select the line you want to change). This will highlight the source data range. Now using mouse pointer simply drag and drop the highlighted box to wherever you want. Done!
23.  **Use the select objects tool:** When working with multiple charts, often you may want to adjust settings for all in one go. Wouldn’t it be great if you can draw a box containing all charts and everything gets selected, _à la_ Power Point (or image editing software)? Well, you can do that in Excel too. Simply activate select objects tool from Home > Find & Select > Select Objects.  
    In fact, I suggest adding this tool to quick access toolbar (right-click on the select objects tool and choose Add to quick access toolbar) so that you can fire it up when you want.![select-objects-tool](https://assets.chandoo.org/wp/wp-content/uploads/2015/07/select-objects-tool.png)
24.  **Link chart title etc. to cell value:** Default chart titles can be lame and boring. Create awesome titles (subtitles, captions etc. too) by using formulas. Then link them to chart title by using this simple trick. Select the title (or any other element), click on formula bar, press = and click on the cell containing your new title. Bingo, your chart now sports a context-sensitive, smart title. (Related: [Give descriptive titles to your charts for best results](https://chandoo.org/wp/descriptive-titles-on-charts/)
     | [smart chart legends – how to?](https://chandoo.org/wp/smart-chart-legends/)
    )
25.  **Add data to charts with copy paste:** Got a chart with sales trend for 3 products and want to add product 4 to it? Simple. Copy the data, select the chart, press CTRL+V. Tell Excel how you want this new data to be pasted and your chart is updated instantly.
26.  **Forecast with seasonality and trends easily:** If you have seasonal data, forecasting it seems like a tricky thing. Now with newly introduced FORECAST.ETS() function, this is super easy. See [all about forecasting](https://chandoo.org/wp/forecasting-in-excel/)
     here and then read [how to build a complex forecast chart](https://chandoo.org/wp/time-series-analysis-and-interactive-forecasting-in-excel-sample-video-from-50-ways-course/)
    .
27.  **Format a chart quickly with styles and themes:** Once you set up your charts, speed up the formatting process by using built-in themes and styles. Go to design tab to customize your charts in a jiffy.![Customize charts with themes and styles](https://assets.chandoo.org/wp/wp-content/uploads/2016/01/change-colors-and-design-of-charts-demo.gif)

### Formatting / Presentation tricks

It’s no good if you are productive. Your presentation skills are equally (if not more) important.

Let’s see some powerful formatting / presentation tricks.

28.  **Format anything with CTRL + 1:** Simple, select the cell / chart / image / drawing shape you want to format. Press Ctrl 1. Format as you want.
29.  **Use alignment tools, you must. Hmmm:**  
    ![alignment-tools-excel](https://assets.chandoo.org/wp/wp-content/uploads/2015/07/alignment-tools-excel.png)  
    If your report has multiple charts (or shapes), then align them all, you must. Having perfect alignment doesn’t mean you waste several minutes nudging each chart in to right position. Simple select them all (using the select objects tool, of course) and fire up alignment tools from either Page Layout or Format ribbon. Align and space objects in a consistent way. _You can also hold ALT key when moving charts / shapes to align them with cell borders._
30.  **Repeat last actions with F4 key:** Let’s say you are changing font color for various chart elements. You can do this step once on something like vertical axis, then select other items and simply press F4. This will repeat your last action (_ie font change_) on the new selection.
31.  **Format once, paint many times:** Use format painter tool from Home ribbon to quickly apply format settings (including conditional formats) from one range to many. Works awesomely and saves you several precious minutes of formatting time. Double click on format painter to lock format painting mode. This way you can copy once and paste several times.
32.  **Add frequently used items to quick access toolbar:** Formatting tends to be a time consuming activity. To reduce the amount of clicks, mouse travel & un-necessary ribbon navigation, simply add all the frequently used formatting options to quick access toolbar.
33.  **Turn-off grid lines:** Get rid of them grid lines to instantly give your workbooks a professional & clean look. You can do this by going to View ribbon. While at it, consider turning-off formula bar & headings too if you find them intrusive.
34.  **Hide extra rows and columns:** To create a clean and polished look for your dashboard, hideaway all the unused rows and columns. Say, your dashboard is in A1:S80, then select row 81, press CTRL + Down Arrow and hide all these rows. Repeat the process for columns T onwards.
35.  **Format for print too:** Don’t forget that many users rely on print, pdf formats to consume information. So make sure your reports are formatted for printing. Start by setting up a print area. This ensures that only necessary information is printed. Also, disable print for screen features like form controls or slicers. You can’t select a slicer button on a print out. Read all [about formatting for print](https://chandoo.org/wp/cp025-sexy-on-spreadsheet-ugly-on-printout/)
    .

Related: [8 tips to make you a formatting pro](https://chandoo.org/wp/excel-formatting-tips/)
.

Want more? Join Excel School Program
------------------------------------

If your job involves data analysis & story telling (to be honest _all_ jobs need these skills), then you are going to love **my Excel School Course.** This end-to-end program enables you to use Excel and get things done faster at work.

We are now open for enrollments. Sign up for the program to become awesome. [Click here to know more](https://chandoo.org/wp/excel-school-program/)
.

Share on FB

Tweet this

Post to LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

*   [13 Comments](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [data analyst](https://chandoo.org/wp/tag/data-analyst/)
    , [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [mouse shortcuts](https://chandoo.org/wp/tag/mouse-shortcuts/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [solo](https://chandoo.org/wp/tag/solo/)
    , [using excel](https://chandoo.org/wp/tag/using-excel/)
    
*   Category: [Keyboard Shortcuts](https://chandoo.org/wp/category/keyboard-shortcuts-2/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    

[PrevPreviousFREE Calendar & Planner Excel Template for 2024](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2024/)

[NextHow to calculate time between two dates in Years, Months & Days \[Excel Formula\]Next](https://chandoo.org/wp/duration-between-two-dates-in-years-months-days-excel-formula/)

### 13 Responses to “35 shortcuts & tricks to make you an #AWESOME Data Analyst”

1.  ![](https://secure.gravatar.com/avatar/ecf75ba5d518a210ce02de8d246b882bbcff127c913694768bcd9636fea07ebd?s=64&d=mm&r=g) Bhavani Seetal Singh says:
    
    [May 2, 2018 at 1:39 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545633)
    
    Great to learn Sir....!
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545633)
    
2.  ![](https://secure.gravatar.com/avatar/ed4d9bb89b8022ec164d63c3352af4f1905a41e088f53aa39fafcb3d0d9b7cc7?s=64&d=mm&r=g) Tory Lauerman says:
    
    [May 2, 2018 at 4:15 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545644)
    
    Awesome tips! I love your emails, I'm a VERY basic Excel user but improving quickly with the help of your posts!
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545644)
    
3.  ![](https://secure.gravatar.com/avatar/fea4a3e84386c913114de166502f9918b540e2f8be9e378d6a2df66dc9a9c6ed?s=64&d=mm&r=g) Curt Hasan says:
    
    [May 2, 2018 at 4:26 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545645)
    
    Awesome information
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545645)
    
4.  ![](https://secure.gravatar.com/avatar/2b8f895a6c40893bc5e9f3853636172d3fb6ab02fbeff73450370b1b086edac6?s=64&d=mm&r=g) Siddikullah Khan says:
    
    [May 2, 2018 at 5:23 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545647)
    
    Thanks for your valuable guide.
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545647)
    
5.  ![](https://secure.gravatar.com/avatar/efe9f0fc38150b39383c99b49bf02a4fd90e367b63b72bed9d6ed298c9fb70de?s=64&d=mm&r=g) Olu says:
    
    [May 2, 2018 at 7:38 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545662)
    
    Awesome.
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545662)
    
6.  ![](https://secure.gravatar.com/avatar/343d1c1242e0005af147b97cc2da9e24babb66ac2aff8e3826da94e2d5a7fec1?s=64&d=mm&r=g) Kim Lombardo says:
    
    [May 2, 2018 at 7:56 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545663)
    
    Excellent tips once again - looking forward to the next workshop
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545663)
    
7.  ![](https://secure.gravatar.com/avatar/5538130f6174ef4cf6d86b446c1e80d2546fda1a5f47e1d595b7dd87825b0c29?s=64&d=mm&r=g) \-suman pathak says:
    
    [May 3, 2018 at 10:24 am](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545732)
    
    Sirs,
    
    Looking to learn from your organisation thru mail.
    
    suman pathak  
    salt Lake,Kolkata  
    Ph:9830819139
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1545732)
    
8.  ![](https://secure.gravatar.com/avatar/c32983c537cb0022fa60d1b7f2469a990808a30fb9f921750495c12b1a92e127?s=64&d=mm&r=g) Ansie says:
    
    [May 24, 2018 at 6:31 am](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1548452)
    
    With Chandoo  
    You can doo.
    
    Brilliant
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1548452)
    
9.  ![](https://secure.gravatar.com/avatar/f6bc821a2a76c934d00af58bb8cf8fb9d9ca3915190b15d88e477b0fd5b4ff21?s=64&d=mm&r=g) Nimesh says:
    
    [May 24, 2018 at 6:55 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1548585)
    
    Whats the difference between Ctrl+L and Ctrl+T to create table?
    
    Ctrl+L used to work in earlier version to create List which is now transformed as Table in 2007 onwards, if I am not wrong.
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1548585)
    
10.  ![](https://secure.gravatar.com/avatar/2947fca06d3ab2840bd36cf87ea517ecfe970fe994e1d896f1e8462d796ee75f?s=64&d=mm&r=g) [Saheb Karmakar](http://na/)
     says:
    
    [December 10, 2020 at 12:58 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1944811)
    
    Sir,  
    How to add blank after each column in power query?
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-1944811)
    
11.  ![](https://secure.gravatar.com/avatar/8386510e76900cfe46770e90601c6338a61004107aad5d43c1898eb00333b442?s=64&d=mm&r=g) sukesh chaturvedi says:
    
    [June 28, 2021 at 9:18 am](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-2008519)
    
    Dear Chandoo  
    Your tips a,d tricks and your classes are Awesome tips!  
    I love your emails, I'm a basic Excel user but progressing quickly with the help of your posts!
    
    Your mission to educate us about Excel, which is becoming or has become a very basic skill required for any job, is very "NOBEL".
    
    I thank you sincerely for all your effort and energy that you put into this for us and that too with full of positive and constructive energy.
    
    As we would sa
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-2008519)
    
12.  ![](https://secure.gravatar.com/avatar/8386510e76900cfe46770e90601c6338a61004107aad5d43c1898eb00333b442?s=64&d=mm&r=g) sukesh chaturvedi says:
    
    [June 28, 2021 at 9:19 am](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-2008520)
    
    As we would say it in France that:  
    "vous être génial et que ce que fait est très noble".
    
    Merci.
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-2008520)
    
13.  ![](https://secure.gravatar.com/avatar/18f932066d43a94253b0ee7e33465402d9409ec7e23152a7383c64a5a086528f?s=64&d=mm&r=g) Alma Rosa Villagarcia says:
    
    [January 29, 2022 at 9:14 pm](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-2066799)
    
    I really like your videos, I have learned a lot, and helps me
    
    [Reply](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#comment-2066799)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/35-tips-data-analysis-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ