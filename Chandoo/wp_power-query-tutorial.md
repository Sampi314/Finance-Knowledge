# Power Query Tutorial - What is it, How to use, Full examples, Tips & Tricks

**Source:** https://chandoo.org/wp/power-query-tutorial

---

*   [Power Query](https://chandoo.org/wp/category/power-query/)
    

Power Query Tutorial – What is it, How to use, Full examples, Tips & Tricks
===========================================================================

*   Last updated: August 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Power Query (Get & Transform data in Excel) is a true game changer. It can simplify and automate various data activities. The key benefits of Power Query are,

*   Connect to any type of data source and fetch data
*   Define process for data cleansing and transformation
*   Combine datasets (table joins, appends)
*   Automate data collection & management tasks (refresh etc.)

In this **Power Query Tutorial**, learn what it does, how to use it with 4 practical examples, tips & tricks to work with Power Query better.

#### Table of Contents

What is Power Query?
--------------------

Power Query is a feature of Microsoft Excel and Power BI programs. Power Query is used to,

*   Set up connections to various data sources
*   Pre-process data – ex: cleanup, adding columns, filtering, sorting, mashing up
*   Publish the finalized data to source system – Excel or Power BI

Think of Power Query as your own SQL (querying) tool built in to Excel (or Power BI). Use it to manipulate, mash-up and manage your data.

![what is power query - cartoon](https://chandoo.org/wp/wp-content/uploads/2020/08/what-is-power-query-cartoon.png)

How does Power Query look?
--------------------------

Power Query window looks _almost_ like Excel workbook. This is why most beginners get confused. The key thing to remember is, **Power Query is for connecting, cleaning and manipulating data.** You do this by **applying steps** on your data.

Here is an example of Power Query editor window with 6 key areas highlighted. Click on the image to expand.

### Power Query Window - 6 Important Areas

[![power query UI - 6 important areas](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-UI-6-important-areas.png)](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-UI-6-important-areas.png)

1.  **Ribbon:** You will see the ribbons on top of Power Query editor UI. There is **home ribbon** where common query options like column / row adjustments, clean-up and joins are found. The other ribbons are **transform, add column** and **view.**
2.  **Queries Pane:** This is where all the queries (or connections) you have in the workbook are listed. You can select a query to preview its results and work on it.
3.  **Data view:** You find the preview of _current step_ of selected query here. As you make changes to the data, this preview is updated. This data view looks almost like Excel spreadsheet view.
4.  **Query settings:** You can adjust query name, see all the **applied steps** here. We use this to make changes to the query or delete any steps.
5.  **Formula bar (optional):** The optional formula bar shows corresponding **M Language code** for current step. You can enable / disable this formula bar from “View ribbon”.
6.  **Close & Load button:** This button, also shown as “Publish” in Power BI is what we use to close Power Query and return to main application (Excel or Power BI).

How to activate Power Query?
----------------------------

The process for activating or _launching_ Power Query is slightly different in Excel vs. Power BI. Refer to below steps to launch Power Query.

### Launching Power Query from Excel

![launching power query - excel](https://chandoo.org/wp/wp-content/uploads/2020/08/launching-power-query-excel.png)

1.  Goto **Data ribbon** in Excel
2.  Use buttons in “Get & transform data” area to make a new connection.
3.  Or click on buttons in “Queries & Connections” area to refresh or view the existing queries.

### Power Query from Power BI

![opening power query - power bi](https://chandoo.org/wp/wp-content/uploads/2020/08/opening-power-query-power-bi.png)

1.  Goto **Home ribbon** in Power BI
2.  Use buttons in “data” area to make a new connection.
3.  Or click on buttons in “Queries” area to refresh or view the existing queries.

#### Notes on Power Query availability

*   **Excel:** Power Query is available in all versions of Excel from 2013.
*   **Power BI:** Power Query is available in all versions of Power BI.

Power Query Tutorial - Video
----------------------------

I made a 1+hour tutorial on Power Query explaining every aspect of it, along with 4 full examples. Please watch it to understand and master this powerful & time-saving technology.

You can watch it below or [head over to my YouTube channel](https://youtu.be/PiFAa_jjaEI "Power Query Full Tutorial - video")
.

Power Query as a Mind-map
-------------------------

Power Query is packed with thousands of features to clean, process and manage data. That is why it is tricky to comprehend the overall picture of it. I made a mind-map of Power Query so you can get holistic view of this life saving tool. See it below (click on the image to enlarge).

[![Power Query mind map](https://chandoo.org/wp/wp-content/uploads/2020/08/pq-mindmap.png)](https://chandoo.org/wp/wp-content/uploads/2020/08/pq-mindmap.png)

How to use Power Query?

* * *

Four Examples
---------------------------------------------

In this section, I will demonstrate how to use Power Query with four full-length examples. Each example has sample data and completed workbook for you download and follow along.

[Download Example Files](https://chandoo.org/wp/wp-content/uploads/2020/08/Power-Query-examples.zip)

Includes sample data, completed Excel workbook & Power Query Mind-map PDF

### Power Query Example 1:

* * *

Load and Clean-up Employee Data

**In the first Power Query example, we will look at data for one thousand staff and clean it up.** The data is in an Excel file. We will load it to Power Query and perform below clean-up activities. After data is clean, we will publish the dataset to Excel for analysis. 

*   Connect to Employee Data file
*   Replace missing gender & department values
*   Remove employees without salary
*   Extract employee’s country and remove address column
*   Extract year of join
*   Publish data to Excel

**Whenever there are new employees**, we will simply _refresh_ the Power Query connection and it will load new data (after apply clean-up steps) automatically. Just like magic.

The below instructions show how to do this with Excel Power Query. You can apply the same steps in Power BI too.

#### Step 1: Connect to the data set file from Excel

Sample file for this example - M01.xlsx You need the employee data sample file - M01.xlsx for this example. In the downloaded ZIP file, you will find it in "Datasets" folder. ×

*   Go to data ribbon and click on “From File” and select “Excel”. Point to the employee data set.

Here is a quick re-cap of how to connect to data from Power Query.

![Power Query - a quick demo of getting started](https://chandoo.org/wp/wp-content/uploads/2020/08/Power-Query-quick-gif.gif)

#### Step 2: Apply data cleansing steps in Power Query

Once the data is loaded into Power Query, you can quickly apply all the necessary data cleansing steps in there. 

The steps will be:

1.  **Remove top rows:** The file contains 2 rows of header information which is not needed. From “Home ribbon” in Power Query editor, using the “Remove rows” button, remove top 2 rows.
2.  **Promote headers:** Now that our data is has no extra rows on top, let’s use row number 3 as header. From home ribbon, just tap on the “use first row as headers” button.
3.  **Remove blank columns:** The file also loads a few blank columns. Just use “Remove columns” button to nix them.
4.  **Replace missing values** – gender & department columns: Select each column with missing data and either right click or use “replace values” button to find & replace **null**s with alternative values.
5.  **Remove staff with no salary:** This operation is also called “Filtering”. Just use the filter button on salary column and remove any “null” values. 

I have illustrated the screen buttons for these 5 data cleansing steps on Power Query UI below. Check it out if you need help.

[![power query example data cleansing steps - illustration](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-example-data-cleansing-steps-illustration.png)](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-example-data-cleansing-steps-illustration.png)

Power Query Tip: Plan first, clean next

Save a lot of time by planning all your data cleansing steps first. Think about ways in which your data could change in future and build your **data cleansing** around them.

#### Step 3: Extracting country from address to new column

So far, all our **data cleaning** steps are in-place. But now, we must add a new column with the country of employee. You can use “Add column” ribbon of Power Query to do such operations.

For example, to extract “USA” from the address “1 Infinite Loop, Los Angels, CA, USA“, we can use **text after delimiter** option. 

To extract the country, select the address column and use Add Column > Extract > Text After Delimiter option.

Note: In the video, I use a more advanced version of this as our addresses are not so straight forward.

![add column feature of Power Query - example](https://chandoo.org/wp/wp-content/uploads/2020/08/add-column-feature-of-Power-Query-example.png)

You can use similar approach to add “year” from date of join.

#### Step 4: Publish data to Excel for analysis & reporting

Once your data is clean and ready, click on “Close & load” button in home ribbon. This will load data to Excel as a table. You can use this table for data analysis or reports. 

**How to refresh:**

Whenever there is new data added to the employee data file, just head over to the Excel file with connection and refresh it (shortcut: Ctrl+Alt+F5 will refresh all connections)

Your file, associated analysis and charts will all be updated.

#### Power Query Save & Load options – Explained

*   **In Excel:** You can load Power Query data in three ways – as a table on spreadsheet, a table to data model or connection only.
*   **Power BI Save & Load:** With in Power BI, you can either load a Power Query table or leave it in the query editor. If you do not load a table, you can still have it refreshable for _calculation purposes._

#### for more on this example…

Please refer to the [Power Query tutorial video above](https://chandoo.org/wp/power-query-tutorial/#pq_tutorial_video)
, timestamp 24:10 onwards.

### Power Query Example 2:

* * *

Scraping Web Data & Reshaping it

![power query web data - cartoon](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-web-data-cartoon.png)

In this example, let’s use Power Query to scrape web data from [List of Indian States page on Wikipedia](https://en.wikipedia.org/wiki/List_of_states_in_India_by_past_population)
.

On that page, there is a historical census data table (depicted below) and we will connect to it from Power Query. Once we have the data, we will _**unpivot**_ it to tabular format for easy analysis.

![web scraping with Power Query - example](https://chandoo.org/wp/wp-content/uploads/2020/08/web-scraping-with-Power-Query-example.png)

Data for this example - Wikipedia Please use the URL - **https://en.wikipedia.org/wiki/List\_of\_states\_in\_India\_by\_past\_population** for this example. ×

#### Step 1: Connect to web data source

From Data ribbon, use the “from web” button. Paste below URL https://en.wikipedia.org/wiki/List\_of\_states\_in\_India\_by\_past\_population

and connect.

Power Query will show all the tables on the web page. Select the census table and click on “transform” button.

#### Step 2: removing unnecessary rows

The wikipedia table has an extra _header row_ and a grand total row. Just remove these with “Remove Rows” button.

#### Step 3: Unpivoting the data

The census data has state in one column and each census population in one column. We can turn this in to a standard three column table – state, year, population using **unpivot** option.

*   Right click on state column 
*   Pick “unpivot other columns” option
*   Done, your data is now in tabular format.

#### Power Query Web Connection Tips

*   **Privacy settings:** When you make a web connection, PQ will prompt you for _access type details._ Most web data can be accessed _anonymously._ But you can also use login access or windows credentials to authenticate requests.
*   **Check frequently:** If the source website changes their format or presentation of data, then your Power Query connections will break. It is a good idea to check such connections once in a while to make-sure they are working.
*   **URL parameters:** You can use “Advanced” option during connection time to set up URL parameters or variables. This gives you flexibility to access things like _page 5 of a result set._

#### for more on this example…

Please refer to the [Power Query tutorial video above](https://chandoo.org/wp/power-query-tutorial/#pq_tutorial_video)
 – timestamp 47:09 onwards

#### More Power Query Web Scraping Examples 

*   [FIFA worldcup – scores, tables & details – web scraping with Power Query](https://chandoo.org/wp/fifa-worldcup-2018-tracker/)
     \[Beginner\]
*   [URL parameter example – weather data to Excel](https://chandoo.org/wp/how-windy-is-wellington-using-power-query-to-gather-wind-data-from-web/)
     \[Beginner\]
*   [Using API to access and export video comments from YouTube with Power Query](https://chandoo.org/wp/export-youtube-comments-template/)
     \[Advanced\]

### Power Query Example 3:

* * *

Combine data from all files in a folder

![folder consolidation with Power Query](https://chandoo.org/wp/wp-content/uploads/2020/08/folder-consolidation-with-Power-Query.png)

You can use “folder” connection option in Power Query to easily consolidate data from all files in a folder. 

In the third example, we will take all the project files in the example dataset and combine data to one table. This process is a bit clumsy to explain in text alone. So please watch the video segment (timestamp 58:48) to understand this fully. I am providing a summary of the folder combine technique below.

Data for this example - CSV folder In the download ZIP file, use the Datasets > CSV folder as data source for this example. ×

1.  Start by making a folder connection (Data ribbon > Get Data > From File > From Folder)
2.  Point to the folder where your files reside
3.  Click on “Combine” button for a simple and quick data combine.
4.  _Or choose “Combine & Transform”_ option for customizing the transformation process.
5.  Power Query will show one of the files and asks you **how you want to extract data.** Based on your selection, PQ will apply the same logic to all files and combines the data for you.

Here is a **quick overview of the folder connection process**.

![](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-folder-connection-explained-1.gif)

#### for more on this example…

Please refer to the [Power Query tutorial video above](https://chandoo.org/wp/power-query-tutorial/#pq_tutorial_video)
 – timestamp 1:09:08 onwards

### Power Query Example 4:

* * *

Joining and Appending Tables

In the last example of Power Query, we will learn how to **merge** and **append tables.** These are similar to SQL operations.

*   Power Query Merge = SQL Join
*   Append = SQL Union

![](https://chandoo.org/wp/wp-content/uploads/2020/08/table-joins-and-appends-cartoon.png)

Data for this example - Students dataset In the download ZIP file, use the "students & courses.xlsx" file for this example. ×

#### Appending two tables with Power Query:

To append one table at the end of another table, you must **have same columns in both tables**. It doesn’t matter if the columns are not in the same order (for ex. table 1 can have student, course and table 2 can have course, student. PQ will append ok).

**What if one table has more or less columns?**

In that case, Power Query will still merge, by including all columns. The missing values will be shown as _null_ in the final appended table.

To append two tables:

*   Select either table and view in the preview grid.
*   Go to Home ribbon > click on “**append queries**“
*   Follow the screen prompts and specify the second table name.
*   Power Query will append second table at the end of first table.

You can also use this to append more than two tables.

#### Merging (Joining) two tables:

In order to merge or join two tables, you nee a common value in both tables. In the below example, you can merge:

*   Students & Enrollment on “**Student ID**“
*   Course & Enrollment on “**Course ID**“

#### Example of common field between tables

**Students Table**

*   **Student ID**
*   Name
*   Date of birth
*   Class
*   Parent 1 name
*   Parent 2 name

**Course Table**

*   **Course ID**
*   Course name
*   Instructor
*   Credits

**Enrollment Table**

*   **Course ID**
*   **Student ID**

To merge two tables:

*   Select the source table
*   Go to Home ribbon and click on “**Merge queries**“
*   Follow screen prompts and **select common column** (field) between both source and target tables.
*   **Specify the join type**. Leave the default “left outer join” if you just want matching values in target table when present. Try other kinds of join (merge) if you need.
*   Power Query will perform the merge and show corresponding rows of target table as a new column.
*   **Expand this column** and your merge will be complete.

Download Power Query Examples
-----------------------------

Please use below button to download all Power Query examples, sample data and mind-map PDF. 

[Download Example Files](https://chandoo.org/wp/wp-content/uploads/2020/08/Power-Query-examples.zip)

Includes sample data, completed Excel workbook & Power Query Mind-map PDF

Power Query - My Top 5 Tips
---------------------------

Tip #1

Tip #2

Tip #3

Tip #4

Tip #5

More..?

Tip #1

#### Look before leap:

Before you create any complex queries, just jot down all the steps needed and arrange them in logical order. Apply filters & error handling steps first, then add columns or transformations.

Tip #2

#### Profile your columns

![column-profile-stats-power-query](https://chandoo.org/wp/wp-content/uploads/2020/08/column-profile-stats-power-query.png)

Power Query offers easy and useful column profiling options. Use them to investigate how good your data is and fix problems with a click.

I have shown a sample column statistics from “Employee data” file above. You can enable this view from the “View ribbon”. Use the check boxes,

*   Column Quality
*   Profile
*   Distribution

You can disable once you are happy with the quality of your data.

Tip #3

#### Formula bar is your friend

Enable formula bar from “View” ribbon. This is a one time step. Once you have it on, you can passively learn the Power Query language – M. You can use formula bar to quickly adjust or type new M code.

Tip #4

#### Right click before you look elsewhere

Many common and useful Power Query operations can be done by right clicking on the columns. This saves time too.

Tip #5

#### There is more than one way to do things

and that is ok. Just stick with what works in the beginning. Learn and improve your queries over time.

More..?

Got a Power Query tip? Share it with me in the comments section.

Power Query - Recommended Resources
-----------------------------------

### **Power Query Books**

I recommend the excellent [**Collect, combine and transform data using Power Query**](https://amzn.to/3gwbN4v)
 book by Gil Raviv.

[![power query book by gil raviv](https://chandoo.org/wp/wp-content/uploads/2020/08/power-query-book-by-gil-raviv.png)](https://amzn.to/3gwbN4v)

### Power Query Courses

If you want a comprehensive and hands-on data analysis course with plenty of Power Query examples, check out my [Excel School online classes](https://chandoo.org/wp/excel-school-program/)
.

[![introducing-advanced-excel-training](https://chandoo.org/wp/wp-content/uploads/2020/08/introducing-advanced-excel-training.png)](https://chandoo.org/wp/excel-school-program/)

### Power Query Web Sites

These are my absolute favorite helpful websites that frequently write about Power Query. Please bookmark and enjoy.

*   [Excel Guru blog by Ken Puls](https://www.excelguru.ca/blog/)
     – For Power Query tips, practical scenarios and guidance.
*   [Cross Join blog > Power Query pages](https://blog.crossjoin.co.uk/category/power-query/)
     by Chris Webb – for intermediate to advanced PQ applications.
*   [M language primer (multi-part series)](https://bengribaudo.com/blog/2017/11/17/4107/power-query-m-primer-part1-introduction-simple-expressions-let)
     for advanced users by Ben Gribado
*   [Power Query best practices](https://docs.microsoft.com/en-us/power-query/best-practices)
     \[Microsoft Docs\]

### More PQ examples on Chandoo.org

Check out below examples for more on Power Query.

*   [Leave analysis with Power Query](https://chandoo.org/wp/entitlement-vs-usage-power-query/)
    
*   [Folder consolidation – advanced example](https://chandoo.org/wp/combine-excel-files-using-power-query/)
    
*   [Oddly shaped data to table – with Power Query](https://chandoo.org/wp/oddly-shaped-data-3ways/)
    
*   [More on Power Query](https://chandoo.org/wp/category/power-query/)
    

Share on FB

Tweet this

Post to LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

*   [33 Comments](https://chandoo.org/wp/power-query-tutorial/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/power-query-tutorial/#respond)
    
*   Tagged under [append tables](https://chandoo.org/wp/tag/append-tables/)
    , [consolidation](https://chandoo.org/wp/tag/consolidation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [merge tables](https://chandoo.org/wp/tag/merge-tables/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [solo](https://chandoo.org/wp/tag/solo/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [web scraping](https://chandoo.org/wp/tag/web-scraping/)
    
*   Category: [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousProject Plan – Gantt Chart with drill-down capability \[Templates\]](https://chandoo.org/wp/drill-down-gantt-chart-template/)

[NextExcel formula to convert calendar format to tableNext](https://chandoo.org/wp/excel-formula-to-convert-calendar-format-to-table/)

### 33 Responses to “Power Query Tutorial – What is it, How to use, Full examples, Tips & Tricks”

1.  ![](https://secure.gravatar.com/avatar/8f161ec4b96af1cc6cd5c103b759efaa84a6193d10dafcf046ccc6342227878a?s=64&d=mm&r=g) Ron MVP (2012-2018) says:
    
    [August 27, 2020 at 12:28 am](https://chandoo.org/wp/power-query-tutorial/#comment-1863682)
    
    Tutorial looks good, I'll be passing a link to it on to other users.  
    .  
    The MindMap is a great idea. But the link to a larger image does not appear to be working.  
    .  
    What app did you use to create it?
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1863682)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 27, 2020 at 2:32 am](https://chandoo.org/wp/power-query-tutorial/#comment-1863698)
        
        Thank you Ron. I am glad you liked this and will be sharing the link with others 🙂
        
        I used mindmup online service to create this. I fixed the image link, it should expand now.
        
        [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1863698)
        
2.  ![](https://secure.gravatar.com/avatar/8f161ec4b96af1cc6cd5c103b759efaa84a6193d10dafcf046ccc6342227878a?s=64&d=mm&r=g) Ron MVP (2012-2018) says:
    
    [August 27, 2020 at 2:40 am](https://chandoo.org/wp/power-query-tutorial/#comment-1863700)
    
    I finally found a workaround to look at a larger image of the MindMap.  
    Handy tool, consistent with your article ... but ...  
    PERSONALLY, I think it would be much more useful if you created a version that excludes the Examples information. The rest would make a useful map to PQ in general, without the distraction of the examples. It would also allow you to make the MindMap more compact.  
    .  
    Your Tip#2, it would be helpful if you provided either introductory instructions on Profiling or a link to a detailed article on using the profile feature.  
    .  
    I am trying to follow the steps in Example 4 without watching the video. I took a very different path. I opened the example file and tried to create the example.
    
    I've recreated the example diagram for the table organization in Example 4 in PowerPivot diagram view:  
    [https://1drv.ms/u/s!Am8lVyUzjKfppCGnREimjqw2u838?e=FKgDTm](https://1drv.ms/u/s!Am8lVyUzjKfppCGnREimjqw2u838?e=FKgDTm)
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1863700)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [September 2, 2020 at 2:15 am](https://chandoo.org/wp/power-query-tutorial/#comment-1867837)
        
        Good suggestions Ron. I have included a snapshot of how column profiles look to the article. I will revise the mind-map when I release another update to this page. Thanks also for sharing the image of relationship diagram.
        
        [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1867837)
        
3.  ![](https://secure.gravatar.com/avatar/df2330635afd28a29efa6105673d06527d6d4b8d728884d6dfbf16398a11b093?s=64&d=mm&r=g) abhay says:
    
    [August 30, 2020 at 9:14 am](https://chandoo.org/wp/power-query-tutorial/#comment-1865874)
    
    i am getting error in mutual fund tracker file in excel2016  
    \[Expression.error\] The Csv.Document paramter 'Columns' is invalid.
    
    I tried by removing column and query style from query but still it is not helpful
    
    pl suggest
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1865874)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [September 2, 2020 at 2:14 am](https://chandoo.org/wp/power-query-tutorial/#comment-1867835)
        
        Please try again... could be an issue with the website.
        
        [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1867835)
        
4.  ![](https://secure.gravatar.com/avatar/a97f689ab5446e9527599c2a663aa2a7f85fdb5da851a825f9dbb38a24d694b7?s=64&d=mm&r=g) Saurav Agrawal says:
    
    [September 5, 2020 at 5:36 am](https://chandoo.org/wp/power-query-tutorial/#comment-1869392)
    
    Hi Chandoo,
    
    Is it possible to use a data model created in one workbook to use in another workbook?
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1869392)
    
    *   ![](https://secure.gravatar.com/avatar/8f161ec4b96af1cc6cd5c103b759efaa84a6193d10dafcf046ccc6342227878a?s=64&d=mm&r=g) Ron MVP (2012-2018) says:
        
        [September 5, 2020 at 11:08 pm](https://chandoo.org/wp/power-query-tutorial/#comment-1869606)
        
        yes Here is an example article. google is your friend ...  
        [https://www.myexcelonline.com/blog/copy-and-paste-queries-across-workbooks-using-power-query/](https://www.myexcelonline.com/blog/copy-and-paste-queries-across-workbooks-using-power-query/)
        
        [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1869606)
        
5.  ![](https://secure.gravatar.com/avatar/fc092882a4c220005cea3be7f268ef32488daa116400db3155b74a7fcb4f90a1?s=64&d=mm&r=g) [Payal Bhagat](https://www.siot.org.in/)
     says:
    
    [October 1, 2020 at 9:48 am](https://chandoo.org/wp/power-query-tutorial/#comment-1890670)
    
    thank you so much for this informative article. keep sharing this type of content it will really be going to help the student.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1890670)
    
6.  ![](https://secure.gravatar.com/avatar/4de155e46a199390d9174986fec3061a2e75a41da209614f5e1bb69f6d22af8c?s=64&d=mm&r=g) Trevor Beairsto says:
    
    [November 19, 2020 at 8:56 pm](https://chandoo.org/wp/power-query-tutorial/#comment-1930369)
    
    Hi Chandoo!
    
    I love the mind map! I would like to get a large laminate board made from it, but the printer lab said the resolution won't work to enlarge it to what I would love to have. Is it possible you might have a high resolution version? You are a great teacher by the way. Cheers from Canada.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1930369)
    
7.  ![](https://secure.gravatar.com/avatar/165a6ecd6d73f369da17f0b925d050377d49f1507e936a2aaf6c8aa0d33843a4?s=64&d=mm&r=g) Rajesh Sinha says:
    
    [December 22, 2020 at 12:12 am](https://chandoo.org/wp/power-query-tutorial/#comment-1949116)
    
    DAX is a hard nut to crack,,, since syntax are bit complicated,, and without it reports are like half cooked eggs. In general Power Query and BI are good to use,, mind mind map is good.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1949116)
    
8.  ![](https://secure.gravatar.com/avatar/51b3d0d9b5970dafc899c9135eb93463510dcca6ba3ffe1f192f93067574f4f4?s=64&d=mm&r=g) David Goodmanson says:
    
    [April 16, 2021 at 2:28 am](https://chandoo.org/wp/power-query-tutorial/#comment-1993708)
    
    Thanks Chandoo, It is great that you have offered tutorials like this, it is a fantastic way to learn PQ.  
    Much Appreciated,  
    Dave
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1993708)
    
9.  ![](https://secure.gravatar.com/avatar/63049aca68d68d959c42c36436575be408b50352e12dc81eefe84af095756648?s=64&d=mm&r=g) Suhas says:
    
    [April 21, 2021 at 5:58 pm](https://chandoo.org/wp/power-query-tutorial/#comment-1995088)
    
    hi Chandoo, hope u are doing great.
    
    I have a question, not sure if my requirement can be doable in powerI
    
    1\. I have around 20 coloums with 60 rows of employees.  
    2\. These 20 coloums consists of 60 employees different skills.  
    3\. All i wanted is to combine all 20 colums data to one colum, so that i can use pivot or slicer.  
    4\. As soon as i select the skill on slicer, the employee details have to pull up.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-1995088)
    
10.  ![](https://secure.gravatar.com/avatar/ff0e3dc942cb758c12e2194bc1e550aaf140dae35e5fe28cefdfa4472a7ecc92?s=64&d=mm&r=g) Paul Clifford-Jones says:
    
    [June 7, 2021 at 11:08 am](https://chandoo.org/wp/power-query-tutorial/#comment-2005197)
    
    Many thanks for a thoughtfully produced, well structured and evenly paced video and supporting material. Professional and approachable.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2005197)
    
11.  ![](https://secure.gravatar.com/avatar/7d794da38cfe73487ca268ed58a0724a8ce4cd9bc4aca90b62f4dfee3e772458?s=64&d=mm&r=g) [Margaret Seger](https://chandoo.org/wp/power-query-tutorial/)
     says:
    
    [August 12, 2021 at 9:45 am](https://chandoo.org/wp/power-query-tutorial/#comment-2021132)
    
    I have followed the steps to complete the Example 1 Load and Clean-up, but was not sure how to complete the step Replace alternative values in the Gender and Department columns. Do you have to view each record to replace the data, and how would you know which department to replace the null with?
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2021132)
    
12.  ![](https://secure.gravatar.com/avatar/7a2e0bdc990846749d1ff12b5fa9e42ca1137ddb7c12759b8869e7ff08979555?s=64&d=mm&r=g) M.Shiva Kumar says:
    
    [September 13, 2021 at 6:20 am](https://chandoo.org/wp/power-query-tutorial/#comment-2028256)
    
    Hi Chandoo, I am a 66 year old man and I have a rudimentary knowledge of computers. I was able to follow your tutorial on PQ and now I am trying to do some exercises. I sincerely thank you for this tutorial.  
    M.Shiva Kumar,  
    Mysore, India
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2028256)
    
13.  ![](https://secure.gravatar.com/avatar/6e22156e1434689c8b1723fd5f838cd8f7c29bff7495fc05911e979ddcd50d43?s=64&d=mm&r=g) Nicolas Warkotsch says:
    
    [September 14, 2021 at 11:11 am](https://chandoo.org/wp/power-query-tutorial/#comment-2028325)
    
    Hi Chandoo,  
    thank you very much for this easy-to-understand tutorial.  
    I only face one problem: when I select a folder via data/new query/from file/from folder the navigator window does not open but I am led directly to power query with no possibilities to click combine, transform or load.  
    When using the other data sources (from workbook etc) everything works well. Do you or anybody else have an idea to fix this problem?  
    Best regards
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2028325)
    
14.  ![](https://secure.gravatar.com/avatar/e07b8cd42dbaae942672e4e14bdca064babb80ed266512791965c34e91889d57?s=64&d=mm&r=g) Derrick Makhoba says:
    
    [October 6, 2021 at 10:59 am](https://chandoo.org/wp/power-query-tutorial/#comment-2031504)
    
    Hi Chandoo, I sincerely thank you for this tutorial.  
    I am trying to do some exercises.
    
    You are the best teacher.
    
    Thank you very much.  
    Derrick, South Africa
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2031504)
    
15.  ![](https://secure.gravatar.com/avatar/0cce3374691b4ad2d9841b403ecf7bdcd1b7d03f0d2ab06cc9b78189f1ab35cd?s=64&d=mm&r=g) krishnachaithanya says:
    
    [December 17, 2021 at 12:02 am](https://chandoo.org/wp/power-query-tutorial/#comment-2053748)
    
    Hi, Chandoo, Iam thanking you for this course .  
    your aim is to make awesome in Excel & Power BI is very good.  
    This course is structured in a very good manner and understandable easily .  
    It is very useful for aspirants like me who is going to start the career in data analysis
    
    Thank you so much  
    krishnachaithanya gariki  
    Nellore , Andhra Pradesh
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2053748)
    
16.  ![](https://secure.gravatar.com/avatar/83fb9d5b3b7936460bf2cd787279a42351aa50d56682f1cae5efcc0960282e5f?s=64&d=mm&r=g) Rajeev Sharma says:
    
    [March 11, 2022 at 8:04 am](https://chandoo.org/wp/power-query-tutorial/#comment-2070596)
    
    Great Job team... very detailed information provided by you. Thanks a lot.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2070596)
    
17.  ![](https://secure.gravatar.com/avatar/cbe36edc63719b5482e128a083d40630cb246f034155b5197ed18b157c61c8b3?s=64&d=mm&r=g) Rubeena says:
    
    [April 15, 2022 at 10:52 am](https://chandoo.org/wp/power-query-tutorial/#comment-2074245)
    
    Thank you for this tutorial.  
    Could you kindly answer my query.. After transforming data in the first example, I have Close and Apply (not Close and Load) and hence do not have an excel popping up. Please advise.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2074245)
    
18.  ![](https://secure.gravatar.com/avatar/9b4623983b785188fe37834918ae7da46b8474e677bbfb554ab1ad153fc4704a?s=64&d=mm&r=g) Sarah Mossburg says:
    
    [May 3, 2022 at 5:24 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2076381)
    
    hi there - any advice on how to pull in the comments from individual cells when using power query to combine data from tables in multiple sheets?
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2076381)
    
19.  ![](https://secure.gravatar.com/avatar/1931db9c8d926e20d3c6524a13f0707024de38c0f9bc515389a8e159adad98f3?s=64&d=mm&r=g) Shanmugam C says:
    
    [May 18, 2022 at 6:44 am](https://chandoo.org/wp/power-query-tutorial/#comment-2077655)
    
    Hi Chandoo,
    
    Thanks for your useful session, it helps to understand and learn PQ easily. i really appreciate your great effort.
    
    Actually i had an issue with the excel file by using FROM FILE which is downloaded from salesforce report . unfortunately, it shows an error msg "External table is not in the expected format." while importing into EXCEL.
    
    I'm not sure what is an actual issue with this salesforce report file \[if i tried to open it in normal way in excel it shows this msg "the file format and extension of report report1652849835532.xls don't match the file could be corrupted or unsafe. do you want to open it anyway?" it gets open successfully after given "YES"\]
    
    Could you please check and provide me a valid workaround on this ?
    
    Best regards  
    Shan
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2077655)
    
20.  ![](https://secure.gravatar.com/avatar/14dc059f05a83d3d382509827a7b8a34328698f6703a7d9cfdb4d73b1383ecf0?s=64&d=mm&r=g) Athraa says:
    
    [September 5, 2022 at 4:06 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2088809)
    
    Finally I found the right place to learn the right skills for excel, many thanks Chandoo for free support that for the whole world  
    For myself these steps are new for a beginner in data analysis work.
    
    Best regards,
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2088809)
    
21.  ![](https://secure.gravatar.com/avatar/0134c92c43c11d6669b7969831751ee7a25e7907d263a78dead842bbda99439f?s=64&d=mm&r=g) Louis says:
    
    [February 24, 2023 at 3:56 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2121620)
    
    Thanks Chandoo.  
    I very much enjoyed your online trainings. God bless your heart of gold. Sharing knowledge is sharing light. Thanks for sharing your training resources free.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2121620)
    
22.  ![](https://secure.gravatar.com/avatar/92d6583db3933f6131ad3cc108548a33d3f88fdc996342c0076233ab98ea9959?s=64&d=mm&r=g) Pow says:
    
    [June 22, 2023 at 1:54 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2130731)
    
    Wow, this article on Power Query is incredibly informative! As someone who frequently works with data in Excel, I can't help but agree that Power Query is a true game changer. It simplifies and automates various data activities, making the entire process more efficient and streamlined.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2130731)
    
23.  ![](https://secure.gravatar.com/avatar/ebf05a2be970c45292d819ecda5b0a808ee7fe949812bab92906d8e2a25d70ac?s=64&d=mm&r=g) Shubhendu basu ray says:
    
    [August 2, 2023 at 7:39 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2137619)
    
    Hello sir,
    
    I really appreciate the way you teach. I've been following your many Excel, SQL, Power BI, Power Query, and Power Pivot tutorials. Though my position as a Quality Analyst at an MNC is pretty comparable to that of a Data Analyst, I aspire to become a Professional Data Analyst before becoming a Data Scientist. Watching your videos always inspires me. Sir, my dream is to meat you once. I will put all of my effort into getting a decent position, so that I can meet you.
    
    Sir if possible, send me your motivational email, it will boost me go on with my goals.
    
    Regards  
    Shubhendu Basu Ray
    
    Shubhendu Basu Ray
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2137619)
    
24.  ![](https://secure.gravatar.com/avatar/33007a758f9650b00d2398992cb040881ee15f8178e9e0b987279cdff1e30974?s=64&d=mm&r=g) Ryan says:
    
    [November 14, 2023 at 11:53 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2152573)
    
    Thanks! This is much better than any other explanation I found.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2152573)
    
25.  ![](https://secure.gravatar.com/avatar/32ae5a7e656b8ea4b4ea31c3ebc3a39ac9ce2fad27de157eb989d410fb467549?s=64&d=mm&r=g) Alain Kalala says:
    
    [December 8, 2023 at 10:15 am](https://chandoo.org/wp/power-query-tutorial/#comment-2156299)
    
    I want documents on Power query, Power BI and Excel
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2156299)
    
26.  ![](https://secure.gravatar.com/avatar/4095f48dbb91706a0c8ae847b409cbdc470a849bb238dd27e787944f9e820348?s=64&d=mm&r=g) fahmi says:
    
    [February 15, 2024 at 6:56 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2175400)
    
    Great thank you very much
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2175400)
    
27.  ![](https://secure.gravatar.com/avatar/dd41fe8c47129ea480da9185b1ffa45549bba3c4e333b4aed46175bc19bc4774?s=64&d=mm&r=g) Oomesh says:
    
    [May 5, 2024 at 5:48 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2207845)
    
    Hi Chandoo, Thanks for this informative tuition. While doing Column From Examples to extract the Country name, I am not able to get the name. Instead the column name is taking Text by Delimiter as default and the country name is being stated as "vue" , "ton" instead of USA and NZ. Please help
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2207845)
    
28.  ![](https://secure.gravatar.com/avatar/3fa125f373c7cfdca2a0f0d2e39a936b4470093803f83563f0b8988d26d80468?s=64&d=mm&r=g) Syak Mwamondwe says:
    
    [March 4, 2025 at 3:42 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2369237)
    
    Dear Mr. Chandoo,
    
    My sincere respect and profound love. I have loved this course. It has opened my understanding of the Power Query, its purpose, and use. I intend to master it under your charge.
    
    I intend to learn all. From the Pivots, Deep Excell, Mail merging in MS word, Access, Making illustrative professional presentations in PPP, and Power Query and Power BI, and also Dashboards.
    
    I want to enroll into your course where a Certificate can be issued if possible. Advise.
    
    Of course, I shall be retiring soon as I will be 60 years on 10th April 2028. So, I shall use this professional and practical knowledge in doing a lot of consultancy work.
    
    God, bless you.  
    Thank you.
    
    S. Mwamondwe
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2369237)
    
29.  ![](https://secure.gravatar.com/avatar/dbda4b72eb21ea24a1bc991fa6fffc7157d1073b3487173639ff06f9151cdf99?s=64&d=mm&r=g) Augustie M. Mulai says:
    
    [July 29, 2025 at 3:44 pm](https://chandoo.org/wp/power-query-tutorial/#comment-2428911)
    
    Hi Chandoo,
    
    I want to use this opportunity to say thank you for the awesome work you have done. Your videos have been pivotal in career as data analyst. I am grateful and may God bless you.
    
    Regards!  
    Augustine M. Mulai.
    
    [Reply](https://chandoo.org/wp/power-query-tutorial/#comment-2428911)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/power-query-tutorial/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ