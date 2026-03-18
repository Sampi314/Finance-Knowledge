# Python is in Excel! - Here is a complete getting started guide for you » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/introduction-to-python-in-excel

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Python](https://chandoo.org/wp/category/python/)
    

Python is in Excel! – Here is a complete getting started guide for you
======================================================================

*   Last updated on September 4, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Recently Microsoft announced Python support for Excel. This is a BIG news for everyone using Excel to analyze data or find insights. In this article, let me give you a proper introduction to the Python in Excel feature and how to use it. 

If you prefer video, [check out my Excel for Python is here video](https://www.youtube.com/watch?v=whzmtv9qfIQ)
.

![Introduction to Python in Excel](https://chandoo.org/wp/wp-content/uploads/2023/09/python-in-excel-introduction.jpg)

What is Python for Excel feature?
---------------------------------

![When you have "python in excel" it will show up in Formula ribbon](https://chandoo.org/wp/wp-content/uploads/2023/09/python-in-excel.png)

You can now write Python code natively in Excel cells and return the output as either _Python objects_ or Excel values. For example, you want to perform quick statistical analysis of your sales data in the range A1:D10. You can use the below Python code to do this now.

**\=XL(“A1:D10”, headers=True).describe()**

How do I enable Python for Excel?
---------------------------------

This “preview” feature is only available with Excel 365 beta users as of September 2023.

If you have Excel 365, you can go to File > Account to enable “insider” program. More details on eligibility and instructions are here – [https://insider.microsoft365.com/en-us/join/windows](https://insider.microsoft365.com/en-us/join/windows)

After you’ve joined the program, update your Office from File > Account page.

![Office update may be needed to get python in Excel](https://chandoo.org/wp/wp-content/uploads/2023/09/office-update.png)

After the update, if you have Python for Excel, it will show up in the formula ribbon, as depicted below.

If you don’t have it yet, just wait a few weeks. It will show up eventually.

![When you have "python in excel" it will show up in Formula ribbon](https://chandoo.org/wp/wp-content/uploads/2023/09/python-in-excel.png)

How to use Python in Excel:  
A Quick Tutorial
----------------------------------------------

Open Excel and load any of your data files. Alternatively, if you need sample data, copy paste the below table into Excel.

Sample Data (copy paste) 📃

| Sales Person | Product | Country | Date | Sales | Boxes |
| --- | --- | --- | --- | --- | --- |
| Gigi Bohling | Manuka Honey Choco | India | 20-Jul-23 | 8162 | 742 |
| Barr Faughny | White Choc | Canada | 16-Aug-23 | 2485 | 355 |
| Marney O’Breen | Peanut Butter Cubes | India | 14-Jul-23 | 10255 | 733 |
| Wilone O’Kielt | Mint Chip Choco | India | 2-Jul-23 | 16800 | 800 |
| Gunar Cockshoot | Orange Choco | New Zealand | 2-Aug-23 | 2842 | 203 |
| Andria Kimpton | Baker’s Choco Chips | Canada | 18-Jul-23 | 9373 | 427 |
| Beverie Moffet | Fruit & Nut Bars | India | 14-Jul-23 | 6573 | 598 |
| Mallorie Waber | Baker’s Choco Chips | India | 24-Jul-23 | 3598 | 150 |
| Barr Faughny | Spicy Special Slims | Canada | 11-Jul-23 | 5138 | 571 |
| Dennison Crosswaite | White Choc | Canada | 22-Jul-23 | 1547 | 258 |
| Ches Bonnell | 99% Dark & Pure | New Zealand | 16-Aug-23 | 12901 | 993 |
| Andria Kimpton | Organic Choco Syrup | USA | 16-Jul-23 | 7161 | 651 |
| Gunar Cockshoot | Fruit & Nut Bars | New Zealand | 19-Jul-23 | 11935 | 1492 |
| Beverie Moffet | After Nines | India | 18-Aug-23 | 5089 | 268 |
| Gunar Cockshoot | Peanut Butter Cubes | USA | 11-Jul-23 | 9247 | 578 |
| Andria Kimpton | Peanut Butter Cubes | India | 22-Jul-23 | 10731 | 826 |
| Gigi Bohling | After Nines | Australia | 4-Jul-23 | 9730 | 609 |
| Gunar Cockshoot | Eclairs | USA | 1-Aug-23 | 3150 | 287 |
| Karlen McCaffrey | 99% Dark & Pure | USA | 6-Aug-23 | 2247 | 205 |
| Roddy Speechley | Peanut Butter Cubes | USA | 1-Jul-23 | 2765 | 213 |
| Brien Boise | Caramel Stuffed Bars | India | 3-Aug-23 | 7112 | 647 |
| Wilone O’Kielt | Organic Choco Syrup | UK  | 27-Aug-23 | 3787 | 345 |
| Dennison Crosswaite | Peanut Butter Cubes | Canada | 29-Aug-23 | 2674 | 168 |
| Gigi Bohling | White Choc | India | 14-Aug-23 | 378 | 54  |
| Karlen McCaffrey | Raspberry Choco | Australia | 7-Jul-23 | 7217 | 401 |
| Marney O’Breen | Spicy Special Slims | New Zealand | 19-Aug-23 | 735 | 147 |
| Mallorie Waber | Organic Choco Syrup | UK  | 3-Jul-23 | 4690 | 427 |
| Karlen McCaffrey | Manuka Honey Choco | India | 24-Jul-23 | 8008 | 572 |
| Wilone O’Kielt | Spicy Special Slims | Australia | 18-Jul-23 | 12586 | 2518 |

Sample Data (download) 📁

[Download the sample data file](https://chandoo.org/wp/wp-content/uploads/2023/09/demo-data-python-for-excel.xlsx)
.

1.  Once you have some data in Excel, press CTRL ALT SHIFT P to enable Python mode. If you get a “welcome to Python screen” complete the tour and then press the shortcut again.
2.  Using your mouse or keyboard, select the data in your workbook. Excel should write the necessary XL() command to capture your data into Python as a dataframe.
3.  To see the dataframe you just built, press CTRL Enter. Excel will display a “Python Object” in the cell.

DATAFRAME: a dataframe is a python concept for storing data. They are like Excel tables. Each column of dataframe has one kind of data.

![How to create a dataframe in Excel Python](https://chandoo.org/wp/wp-content/uploads/2023/09/how-to-create-a-dataframe-in-excel-python.gif)

### To see the output as values  
instead of Python object

![converting python output to Excel values](https://chandoo.org/wp/wp-content/uploads/2023/09/python-output-excel-options.png)

You can see the “actual” values of your Python code anytime. Just select the cell with Python output and either press CTRL+ALT+SHIFT+M or right click on the cell and choose “Python Output” > Excel values option.

10 Python Coding Examples
-------------------------

Use these code samples to play with Python in Excel. Before starting.

*   Copy the above table of sample data and paste it in Excel (in range A1:F30). Alternatively, [download this file with the data](https://chandoo.org/wp/wp-content/uploads/2023/09/demo-data-python-for-excel.xlsx)
    .
*   To type the code, enter python mode (CTRL ALT SHIFT P) or use the formula =PY( in a cell.

### Example 0

**Construct dataframe 👩‍💻**

df = xl("A1:F30", headers=True)

**Explanation & Output 💻**

This will just create a dataframe named _**df**_ and return that to the cell. You can either leave it or see the underlying data (which will be same as A1:F30) by changing the output style.

### Example 1

**Description of the data 👩‍💻**

df.describe()

**Explanation & Output 💻**

This will generate a dataframe with statistical descriptions for all your number columns. Example output is shown below.

![dataframe describe - sample output](https://chandoo.org/wp/wp-content/uploads/2023/09/dataframe-describe-sample-output.png)

### Example 2

**Description of the data, all columns 👩‍💻**

df.describe(include="all")

**Explanation & Output 💻**

This will generate a dataframe with statistical descriptions for all your columns. Perfect for situations when you have some text, dates and numbers in your data. Sample output shown below:

![dataframe description for all columns](https://chandoo.org/wp/wp-content/uploads/2023/09/dataframe-describe-sample-output-2.png)

### Example 3

**Unique Product Names 👩‍💻**

df\["Product"\].unique()

**Explanation & Output 💻**

This will generate a python array (ndarray) that has all the product names with duplicate values removed.

### Example 4

**Add “Sales per Box” calculated column to the dataframe 👩‍💻**

df\["sales per box"\]=df\["Sales"\]/df\["Boxes"\]

**Explanation & Output 💻**

This will add a new column \[“sales per box”\] to the dataframe with the calculation logic: sales divided by boxes. You can use the same approach to add many other columns

### Example 5

**Add “Sales as percentage” calculated column to the dataframe 👩‍💻**

total\_sales = sum(df.Sales)  
df\["Sales as a percentage"\] = df\["Sales"\]/total\_sales  
df

**Explanation & Output 💻**

First, we calculate the “total\_sales” and keep it in a variable. Then we use that variable to calculate the sales as a percentage.

💡 TIP: Do you notice the different ways in which you can refer dataframe columns? You can use dot notation (ex: df.Sales) or bracket notation (ex: df\[“Sales”\])

### HOMEWORK PROBLEMS

Can you add below columns to the _**df**_ dataframe?

*   Sales value rounded to nearest thousand.
*   Month number of the sales date
*   Flag each record as “Canada” or “Non-Canada”

### Example 6

**Group Sales by Date and Show a Pivot 👩‍💻**

df.groupby(by="Date").sum()

**Explanation & Output 💻**

This creates a default groupby (similar to pivot in Excel) of your data by showing totals by date. This will sum() all the number columns in your dataframe. See the below sample output.

![groupby operation and output in Python (for Excel)](https://chandoo.org/wp/wp-content/uploads/2023/09/adding-columns-to-dataframe.png)

### Example 7

**Group Sales by Date but only show Sales & Boxes columns 👩‍💻**

df.groupby("Date")\[\["Sales", "Boxes"\]\].sum() 

**Explanation & Output 💻**

This creates a customized groupby with Sales & Boxes columns totals by Date. Use this pattern when you don’t want to summarize certain things (like Sales per box).

### Example 8

**Create a bar graph with Daily Sales 👩‍💻**

**import** matplotlib.pyplot **as** plt  
plt.bar(df\["Date"\], df\["Sales"\])

**Explanation & Output 💻**

We import the plotting library [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
 and use that to generate a bar graph with default settings.

Sample output is shown below:

![](https://chandoo.org/wp/wp-content/uploads/2023/09/example-python-chart-1.png)

### Example 9

**Create a bar graph with Daily Sales – another method 👩‍💻**

df\_groups = df.groupby("Date")\["Sales"\].sum()  
df\_groups.plot(kind="bar")

**Explanation & Output 💻**

This code uses the built-in plotting function of the pandas library to generate the bar graph. Notice how this doesn’t show missing dates.

Sample output is shown below:

![](https://chandoo.org/wp/wp-content/uploads/2023/09/example-python-chart-2.png)

### Example 10

**Filter the dataframe to show all records where the product has the word “Choc” 👩‍💻**

df\[df\["Product"\].str.contains("Choc")\] 

**Explanation & Output 💻**

This code generates a new dataframe that contains all rows where the Product column has the word “Choc” in it.

### MORE HOMEWORK PROBLEMS

*   Can you filter all the records that have either “Choc” or “choc”?
*   Create a bar graph of this data to show total sales by each product

How does Python in Excel work?
------------------------------

![](https://chandoo.org/wp/wp-content/uploads/2023/09/python-execution-flow-excel.png)

You need **_internet connection_** to run Python code in Excel. All the code you write is executed in Microsoft Cloud. This also means your data travels on the network to Microsoft Cloud and returns with the result.

What happens if your code has an error?
---------------------------------------

![python error panel - excel](https://chandoo.org/wp/wp-content/uploads/2023/09/python-diagnostics-tab-excel.png)

If there is an error in your Excel Python code, you will see a new error message #PYTHON! in Excel.

You will also see #BUSY! when Excel is running your Python code (_in Microsoft Cloud_).

In case of an error in your code, Excel automatically opens the Python Diagnostics tab and displays more information there.

Execution order of your code
----------------------------

The python code you write in Excel will run in **row-major** order. This means, the code runs row by row, left to right. See this illustration to understand the process.

![](https://chandoo.org/wp/wp-content/uploads/2023/09/python-execution-order-in-excel.png)

Resources to Learn Python 🐍
----------------------------

Now that you are familiar with Python in Excel, you may want to learn more. May I suggest using the below approach.

1.  See if you can enable use Python in Excel to get a feel of the technology.
2.  Install a proper Python IDE like [Anaconda](https://www.anaconda.com/)
    , [VS Code](https://code.visualstudio.com/)
     or [something else](https://www.python.org/downloads/)
     to learn & practice Python properly.
3.  Understand the Python programming concepts like variables, conditions, list comprehension, dataframes and EDA. [Here is a good article on the process](https://chandoo.org/wp/python-for-excel-people/)
    .
4.  Apply these concepts on your own / business data to solidify your understanding.
5.  If you need practice datasets, try [Kaggle](https://kaggle.com/)
    .

### 📺 Python Videos

**[Python in Excel (video by Chandoo)](https://youtu.be/whzmtv9qfIQ)
**

\[NEW\]

**[How to use Python as an Excel Person – FREE Masterclass + 3 Projects](https://youtu.be/uoC48wrJ-yM)
**

\[300k+ views, 1.5 hours long\]

**[End to End data manipulation with Pandas – 10 Examples](https://youtu.be/mkYBJwX_dMs)
**

\[35k views, 18 mins\]

**[Python Playlist on Chandoo](https://www.youtube.com/playlist?list=PLmejDGrsgFyCRceKns-9snhrIKR0d9XMm)
**

* * *

**[Python in Excel (video by Leila Gharani)](https://youtu.be/FbBXtqtRnWU?si=S6ldxQ3wq__OkeMg)
**

**[Python for Beginners (video by Mosh)](https://youtu.be/kqtD5dpn9C8?si=0lSynoEM4SA0V8SH)
**

### 📚 Python Books

*   **Python Crash Course 2nd Edition by Eric Matthes – [https://amzn.to/3PBzYRK](https://amzn.to/3PBzYRK)
    **

This is the book we all (Jo, kids & I) read and really loved it. The explanations and examples are easy enough to get started. There is enough variety to please everyone. 

*   **Automate boring stuff with Python – [https://amzn.to/3Py5T5w](https://amzn.to/3Py5T5w)
    **

More practical if you want to get things done with Python. I read it a few times and really like the practicality of the book.

*   **Python Data Science Handbook – [https://amzn.to/3MFKOUK](https://amzn.to/3MFKOUK)
    **

Python is particularly useful for doing data science & building machine learning models. This is an area of focus for me in the next months. I suggest getting the Python Data Science book once you have strong foundation in the language.

Note: I am using affiliate link for these books. 

### 💻 Microsoft Resources

As part of the Python for Excel launch, Microsoft also added many resources and example pages to their website. Check out these pages.

*   [Getting started with Python in Excel](https://support.microsoft.com/en-us/office/getting-started-with-python-in-excel-a33fbcbe-065b-41d3-82cf-23d05397f53d?ns=excel&version=90&ui=en-us&rs=en-us&ad=us)
    
*   [Introduction to Python – Microsoft Learn Course](https://learn.microsoft.com/en-us/training/modules/intro-to-python/)
    
*   [Using “dataframes” in Excel](https://support.microsoft.com/en-gb/office/python-in-excel-dataframes-a10495b2-8372-4f0f-9179-32771fe0dc04)
    
*   [Power Query and Python in Excel](https://support.microsoft.com/en-gb/office/using-power-query-data-with-python-in-excel-028dbcd4-76c5-4aa4-831d-0e211fefc0a2)
    
*   [Libraries supported by Excel Python](https://support.microsoft.com/en-gb/office/open-source-libraries-and-python-in-excel-c817c897-41db-40a1-b9f3-d5ffe6d1bf3e)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/introduction-to-python-in-excel/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-python-in-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel](https://chandoo.org/wp/tag/excel-2/)
    , [pandas](https://chandoo.org/wp/tag/pandas/)
    , [python](https://chandoo.org/wp/tag/python/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Python](https://chandoo.org/wp/category/python/)
    

[PrevPreviousCP03: The Ugly Truth About Power BI (actually, 4 of them)](https://chandoo.org/wp/cp03-the-ugly-truth-about-power-bi/)

[NextHow to make a pivot table when you have data in multiple sheets \[Tutorial\]Next](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/)

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
    
    [Reply](https://chandoo.org/wp/introduction-to-python-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-python-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-python-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ