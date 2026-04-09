# 100 Excel Tips & Resources for Everyone

**Source:** https://chandoo.org/wp/100-excel-tips-resources-to-celebrate-2000-rss-subscribers

---

*   [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

100 Excel Tips & Resources
==========================

*   Last updated on May 20, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Would you like to learn most popular Excel tips and shortcuts?**

**100 Excel & Charting Tips, Tricks and Resources for you.**

These 100 tips & resources are organized in to the areas,

*   Keyboard Shortcuts
*   Formulas
*   Using Excel to do more
*   Charting
*   Excel Books for everyone
*   Excel Blogs & Resources

All these tips are bite sized and easy to read, digest and implement. The focus is on improving your productivity and making your day better. Wherever possible, I have included links to relevant articles on this site so that you can read and learn more.

If you like this post, I encourage you to [**signup for my free email newsletter**](https://chandoo.org/wp/subscribe/)
.

_Ok, on to the tips now…_

### 25 Very Useful Keyboard Shortcuts

1\. **To format any selected object**, press ctrl+1  
2\. **To insert current date**, press ctrl+;  
3\. **To insert current time**, press ctrl+shift+;  
4\. **To repeat last action**, press F4  
5\. **To edit a cell comment**, press shift + F2  
6\. **To autosum selected cells**, press alt + =  
7\. **To see the suggest drop-down in a cell**, press alt + down arrow  
8\. **To enter multiple lines in a cell**, press alt+enter  
9\. **To insert a new sheet**, press shift + F11  
10\. **To edit active cell**, press F2 (places cursor in the end)  
11\. **To hide current row**, press ctrl+9  
12\. **To hide current column**, press ctrl+0  
13\. **To unhide rows in selected range**, press ctrl+shift+9  
14\. **To unhide columns in selected range**, press ctrl+shift+0  
15\. **To recalculate formulas**, press F9  
16\. **To select data in current region**, press ctrl+shift+8  
17\. **To see formulas in the worksheet**, press ctrl+\`  
18\. **While editing formulas to change the reference type from absolute to relative vice versa**, press F4  
19\. **To format a number as currency**, press ctrl+shift+4 (ctrl+$)  
20\. **To apply outline border around selected cells**, press ctrl+shift+7  
21\. **To open the macros dialog box**, press alt+F8  
22\. **To copy value from above cell**, press ctrl+’  
23\. **To format current cell with comma formats**, press ctrl+shift+1  
24\. **To go to the next worksheet**, press ctrl+shift+pg down  
25\. **To go to the previous worksheet**, press ctrl+shift+pg up

### 20 Situations and How to Solve them using Excel Formulas

26\. **To get the first name of a person**, use =left(name,find(” “,name)-1)  
27\. **To calculate mortgage payments**, use =PMT(interest-rate,number-of-payments,how-much-loan)  
28\. **To get nth largest number in a range**, use =large(range,n)… [Get Full Tip](http://chandoo.org/wp/2008/08/13/15-microsoft-excel-formulas/)
  
29\. **To get nth smallest number in a range**, use = small(range,n)… [Get Full Tip](http://chandoo.org/wp/2008/08/13/15-microsoft-excel-formulas/)
  
30\. **To generate a random phone number**, use =randbetween(1000000000,9999999999), needs analysis toolpak if you are using excel 2003 or earlier… [Get Full Tip](http://chandoo.org/wp/2008/11/20/random-phone-number-formula/)
  
31\. **To count number of words in a cell**, use =len(trim(text))-len(SUBSTITUTE(trim(text),” “,””))… [Get Full Tip](http://chandoo.org/wp/2008/07/08/count-words-excel-formula/)
  
32\. **To count positive values in a range**, use =countif(range,”>0″)… [Get Full Tip](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
  
33\. **To calculate weighted average**, use SUMPRODUCT() function  
34\. **To remove unnecessary spaces**, use =trim(text)  
35\. **To format a number as SSN using formulas**, use =text(ssn-text,”000-00-0000″)… [Get Full Tip](http://chandoo.org/wp/2008/08/13/15-microsoft-excel-formulas/)
  
36\. **To find age of a person based on DOB**, use =TEXT((NOW()-birth\_date)&””,”yy “”years”” m “”months”” dd “”days”””), output will be like 27 years 7 months 29 days  
37\. **To get name from initials from a name**, use IF(), FIND(), LEN() and SUBSTITUTE() formulas… [Get Full Tip](http://chandoo.org/wp/2008/09/02/get-initials-from-name-excel-formula/)
  
38\. **To get proper fraction from a number (for eg 1/3 from 6/18)**, use =text(fraction, “?/?”)  
39\. **To get partial matches in vlookup**, use \* operator like this: =vlookup(“abc\*”,lookup\_range,return\_column)  
40\. **To simulate averageif() in earlier versions of excel**, use =sumif(range, criteria)/countif(range, criteria)  
41\. **To debug your formulas**, select the portions of formula and press F9 to see the result of that portion… [Get Full Tip](http://chandoo.org/wp/2008/12/15/formula-debugging-tips-excel/)
  
42\. **To get the file extension from a file name**, use =right(filename,3) (doesn’t work for files that have weird extensions like .docx, .htaccess etc.)  
43\. **To quickly insert an in cell micro-chart**, use REPT() function… [Get Full Tip](http://chandoo.org/wp/2008/05/13/creating-in-cell-bar-charts-histograms-in-excel/)
  
44\. **COUNT() only counts number of cells with numbers in them**, if you want to count number of cells with anything in them, use COUNTA()  
45\. **Using named ranges in formulas saves you a lot of time. To define one**, just select some cells, and go to menu > insert > named ranges > define

### 15 Excel Tips on Improving Productivity Using Excel

46\. **To format a number as SSN**, use the custom format code “000-00-0000″… [Get Full Tip](http://chandoo.org/wp/2008/06/16/formatting-numbers-in-excel-few-tips/)
  
47\. **To format a phone number**, use the custom format code “000-000-0000″… [Get Full Tip](http://chandoo.org/wp/2008/02/25/custom-cell-formatting-in-excel-few-tips-tricks/)
  
48\. **To show values after decimal point only when number is less than one**, use \[<1\]\_($#,##0.00\_);\_($#,##0\_) as formatting code… [Get Full Tip](http://chandoo.org/wp/2008/10/02/excel-number-formatting-tip-showing-decimals-conditionally/)
  
49\. **To remove grid lines from excel worksheet**, go to menu > tools > options > and un-check grid lines option. (Excel 2007: office button > excel option > advanced)… [Get Full Tip](http://chandoo.org/wp/2008/08/01/15-fun-things-with-excel/)
  
50\. **To hide a worksheet**, go to menu > format > sheet > hide… [Get Full Tip](http://chandoo.org/wp/2009/01/22/hide-excel-worksheet-tab/)
  
51\. **To align multiple objects**, like charts, drawings, pictures use drawing toolbar > align and select alignment option… [Get Full Tip](http://chandoo.org/wp/2008/08/28/aligning-charts-objects-excel-layout-tip/)
  
52\. **To freeze rows on top**, select the a row and use menu > window > freeze panes… [Get Full Tip](http://chandoo.org/wp/2008/08/01/15-fun-things-with-excel/)
  
53\. **To disable annoying formula errors**, go to menu > tools > options > error checking tab and disable errors you don’t want to see… [Get Full Tip](http://chandoo.org/wp/2008/10/16/microsoft-excel-15-productivity-tips/)
  
54\. **To change the shape of cell comments from rectangle to some other symbol**, select the comment, go to drawing tool bar and change the shape from there… [Get Full Tip](http://chandoo.org/wp/2008/08/01/15-fun-things-with-excel/)
  
55\. **To transpose a range of cells**, copy the cells, go to empty area, and press alt+e+s+e… [Get Full Tip](http://chandoo.org/wp/2008/07/02/17-excel-paste-special-tricks/)
  
56\. **To save data filter settings so that you can reuse them again**, use custom views… [Get Full Tip](http://chandoo.org/wp/2008/12/17/custom-views-excel/)
  
57\. **To select all formulas**, press CTRL+G, select “special” and check “formulas”  
58\. **To select all constants**, press CTRL+G, select “special” and check “constants”  
59\. **To clear formats from a range**, select menu > edit > clear > “formats”  
60\. **To move a chart and align it with cells**, hold down ALT key while moving the chart

### 9 Charting Tips for Everyone

61\. **To create an instant micro-chart from your data**, use sparklines… [Get Full Tip](https://chandoo.org/wp/excel-sparklines-tutorial/)
  
62\. **Understand [data to ink ratio](http://www.infovis-wiki.net/index.php/Data-Ink_Ratio)
 to reduce chart junk**, using even a pixel more of ink than what is needed can reduce your chart’s effectiveness  
63\. **Combine two different types of charts when one is not enough**, to use, add another series of data to your sheet and then right click on it and change the chart type… [Get Full Tip](http://chandoo.org/wp/2009/01/05/excel-combination-charts/)
  
64\. **To reverse the order of items in a bar / column chart**, just click on y-axis, press ctrl+1, and check “categories in reverse order” and “x-axis crosses at maximum category” options  
65\. **To change the marker symbol or bubble in a chart to your own favorite shape**, just draw any shape in worksheet using drawing toolbar, then copy it by pressing ctrl+c, now go to the chart and select markers (or bubbles) and press ctrl+v  
66\. **To create partially overlapped column / bar charts**, just use overlap and gap settings in the format data series area. A overlap of 100 will completely overlap one series on another, while 0 separates them completely.… [Get Full Tip](http://chandoo.org/wp/2009/01/21/stacked-bar-charts-excel/)
  
67\. **To increase the contrast of your chart**, just remove grayish background color that excel adds to the chart (in versions excel 2003 and prior)  
68\. **To save yourself some trouble**, always try to avoid charts like – 3D area charts (unstacked), radar charts, 3D Lines, 3D Columns with multiple series of data, Donut charts with more than 2 series of data… [Get Full Tip](http://chandoo.org/wp/2008/09/03/6-charts-to-never-use/)
  
69\. **To improve comparison**, replace your radar charts with tables… [Get Full Tip](http://chandoo.org/wp/2008/10/07/excel-radar-charts-replacement-spot-matrix-download-template/)

### 6 simple steps for better chart formats

70\. Remove any vertical grid-lines  
71\. Change horizontal grid-line color from black to a very light shade of gray  
72\. Adjust chart series colors to get better contrast  
73\. Adjust font scaling (for versions excel 2003 and prior)  
74\. Add data labels and remove any axis (axis labels) if needed  
75\. Remove chart background colors

### 5 Excel books for everyone

76\. [Excel 2016 Bible by John Walkenbach](https://amzn.to/2IuoLnb)
  
77\. [Excel 2016 Power Programming by John Walkenbach](https://amzn.to/2ID0U0I)
  
78\. [Excel 2016 All in one for dummies by Greg Harvey](https://amzn.to/2GxMxc9)
  
79\. [Microsoft Excel Data Analysis and Business Modelling by Wayne Winston](https://amzn.to/2wVzNfQ)
  
80\. [M is for Data Monkey by Ken Puls](https://amzn.to/2Lh5TFN)

_PS: Links to Amazon, affiliate code used_

### 20 Excellent Resources and Blogs for getting latest Excel Tips & Charting Ideas

81\. **[PTS Blog](http://peltiertech.com/WordPress)
**  
82\. **[Andrew’s Excel Tips](https://andrewexcel.blogspot.com.au/)
**  
83\. [**Microsoft Power BI Blog**](https://powerbi.microsoft.com/en-us/blog/)
  
84\. **[Contextures](http://blog.contextures.com/)
**  
85\. **[Junk Charts](http://junkcharts.typepad.com/junk_charts/)
**  
86\. **[Daily Dose of Excel](http://www.dailydoseofexcel.com/)
**  
87\. **[Digital Inspiration](http://www.labnol.org/)
**  
88\. **[Life Hacker](http://lifehacker.com/)
**  
89\. **[Jorge’s Charts Blog](http://charts.jorgecamoes.com/)
**  
90\. **[Data Chant](http://datachant.com/)
**  
91\. [**Excelarator BI**](https://exceleratorbi.com.au/)
  
92\. **[Guy in a Cube](https://guyinacube.com/)
**  
93\. **[More information per pixel](http://blog.xlcubed.com/)
**  
94\. **[Newton Excel Bach](http://newtonexcelbach.wordpress.com/)
**  
95\. **[Presentation Zen](http://www.presentationzen.com/)
**  
96\. **[Visual Business Intelligence by Stephen Few](http://www.perceptualedge.com/blog/)
**  
97\. [Spreadsheet Journalism](https://spreadsheetjournalism.com/)
  
98\. **[Allen Wyatt’s Excel Tips](http://excel.tips.net/)
**  
99\. [**Excel Guru**](https://www.excelguru.ca/blog/)
  
100\. **[Chandoo.org on YouTube](https://www.youtube.com/c/exceltutorials)
**

### Join the celebrations, share your tips & ideas

I encourage you to share your Excel Tips & Charting Suggestions through comments section. We have a vibrant reader community here and we love to learn from each other.

If you like this post, I encourage you to [**signup for my free Email Newsletter**](https://chandoo.org/wp/subscribe/)

_Post updated on 20-May-2018_

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [210 Comments](https://chandoo.org/wp/100-excel-tips-resources-to-celebrate-2000-rss-subscribers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/100-excel-tips-resources-to-celebrate-2000-rss-subscribers/#respond)
    
*   Tagged under [books](https://chandoo.org/wp/tag/books/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [excel 2007](https://chandoo.org/wp/tag/excel-2007/)
    , [excel blogs](https://chandoo.org/wp/tag/excel-blogs/)
    , [Excel Tips](https://chandoo.org/wp/tag/excel-tips/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [lists](https://chandoo.org/wp/tag/lists/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    
*   Category: [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel Links of the Week – Minor Changes to PHD edition](https://chandoo.org/wp/excel-links-j26/)

[NextColors in Chart Labels \[Quick Tip\]Next](https://chandoo.org/wp/colors-in-excel-chart-labels-trick/)

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
    
    [Reply](https://chandoo.org/wp/100-excel-tips-resources-to-celebrate-2000-rss-subscribers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/100-excel-tips-resources-to-celebrate-2000-rss-subscribers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/100-excel-tips-resources-to-celebrate-2000-rss-subscribers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ