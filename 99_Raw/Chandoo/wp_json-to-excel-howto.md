# Easily Convert JSON to Excel - Step by Step Tutorial » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/json-to-excel-howto

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Easily Convert JSON to Excel – Step by Step Tutorial
====================================================

*   Last updated on May 13, 2025

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Convert JSON to Excel](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0113.png)

JSON (JaveScript Object Notation) is a popular and easy format to store, share and distribute data. It is often used by websites, APIs and streaming (real-time) systems. But it is also cumbersome and hard to use for performing typical data tasks like summarizing, pivoting, filtering or visualizing. That is why you may want to convert JSON to Excel format. In this article let me explain the process.

1\. Why Convert JSON to Excel?
------------------------------

Excel is a more familiar and easy to work with format for your data. Also, when setup properly Excel files (such as CSV or XLSX or XLSB) take up less space than their JSON counter parts. More importantly, performing data tasks like calculating formulas, creating pivots or making charts would be easier with Excel format as against JSON.

**Overview of This Guide**

In this guide, we’ll walk through multiple methods to convert JSON to Excel, including manual methods using Excel’s built-in tools, automated methods using Python, and third-party online tools. Whether you’re working with small or large datasets, there’s a solution for you. Let’s dive in and explore how you can make this transformation efficiently.

* * *

**2\. Understanding JSON Format**
---------------------------------

Before jumping into the process of converting JSON to Excel, it’s important to understand JSON format. JSON is a lightweight data format that’s easy for both us and computers to read and write. It’s primarily used to transmit data between a server and a web application, often in APIs or data feeds.

### **What Does JSON Look Like?**

At its core, JSON is a collection of key-value pairs that are organized in objects and arrays. JSON data can be quite flexible, allowing it to represent both simple and complex data structures. It supports various types of data, including strings, numbers, booleans, arrays, and objects.

Let’s consider the following example of JSON data representing information about a few employees in a company:

    {
      "employees": [\
        {\
          "id": 1,\
          "first_name": "John",\
          "last_name": "Doe",\
          "email": "johndoe@awesomechoc.com",\
          "position": "Chocolatier",\
          "hire_date": "2023-06-15",\
          "skills": ["Baking", "Cocoa Sculpting", "Confectionary"]\
        },\
        {\
          "id": 2,\
          "first_name": "Jane",\
          "last_name": "Smith",\
          "email": "janesmith@awesomechoc.com",\
          "position": "Marketer",\
          "hire_date": "2024-02-20",\
          "skills": ["Packaging", "Product Design", "Field Sales"]\
        },\
        {\
          "id": 3,\
          "first_name": "Emily",\
          "last_name": "Johnson",\
          "email": "emilyj@awesomechoc.com",\
          "position": "Accountant",\
          "hire_date": "2024-08-30",\
          "skills": ["XERO", "Excel", "AR / AP consolidation"]\
        }\
      ]
    }
    

### **Breaking Down the JSON Example**

1.  **Objects and Arrays:**
    *   The main JSON data structure in the example above is an **object**, denoted by curly braces `{}`.
    *   Inside this object, there is a key called `"employees"`, which maps to an **array** (denoted by square brackets `[]`).
    *   The array (list) contains multiple **objects**, each representing a single employee.
2.  **Key-Value Pairs:**
    *   Inside each employee object, you’ll find several **key-value pairs**. For example, `"id": 1` tells you the employee’s ID, and `"first_name": "John"` specifies the first name of the employee.
    *   Some of the values in the JSON are simple data types (like strings or numbers), while others, such as the `skills` key, are arrays that hold multiple values.
3.  **Nested Data:**
    *   The `skills` field is an example of **nested data**. It’s an array within the employee object, which further contains multiple string values representing different skills. This kind of nested data can be difficult to work with directly in Excel, which is why conversion and flattening are necessary.

#### **Challenges of Working with JSON in Excel**

![JSON is like a tree but Excel tables are flat like bamboo](https://chandoo.org/wp/wp-content/uploads/2025/03/json-vs-excel.png)

As you can see, JSON is hierarchical while Excel prefers data in a flattened, tabular format.

If you try to import JSON directly into Excel without transforming it, you might end up with a jumbled mess of data.

For example, in the above JSON, the `"skills"` field would result in a list being placed into a single cell if not properly flattened. Additionally, nested objects, like the `employee` object, would need to be expanded into separate columns (e.g., `"id"`, `"first_name"`, `"last_name"`) for the data to be usable.

This is why it’s essential to convert JSON to Excel in a way that ensures all data is properly structured in rows and columns for analysis. Let’s explore some methods to accomplish that.

3\. Methods for converting JSON to Excel format
-----------------------------------------------

There are many ways to convert JSON to Excel. My preferred technique is to use Power Query in Excel to convert the data quickly and elegantly. But you can also use other techniques. Let’s go thru each of these in detail.

### JSON to Excel conversion (step by step):

**What you need:** You need a JSON file with your data. Download this sample data if you don’t have any.

*   [Sample JSON file](https://1drv.ms/u/c/e7c6dec249ad257b/ERaIG2aIJUpFlkeKcQTM7XEBX0Gxrfy1bMyO73BrtA9uhg?e=egbpBh)
    

1.  Go to Data > Get Data > From File > From JSON
2.  Select the JSON file on your computer (or on the network location)
3.  This will open Power Query editor with your JSON file. Here is a snapshot of how that would look like:

![JSON file after loading in to Power Query](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0115.png)

4.  Using the “convert” ribbon, convert the JSON listing to a “table”.
5.  Now you will have a “list” of all the JSON records (or objects). Click on the Expand button on the list column and select “expand to new rows”.
6.  This should show all the records of the JSON (see below)

![Before and after expanding ](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0116.png)

7.  Expand the Value column again to see the contents of the records.
8.  If you have any “nested” or “hierarchical” data in your JSON, you must expand these columns again. But this time, use the “extract values…” option so you can see them all comma separated in the same column.
9.  Once you have all the necessary data in Power Query, remove any columns you no longer need by right clicking on them and selecting “remove” option.
10.  When ready, use the Home ribbon > Close & Load to bring the data to Excel.

![How to load parsed JSON data into Excel](https://chandoo.org/wp/wp-content/uploads/2025/03/SNAG-0117.png)

### Quick Demo of JSON to Excel conversion:

Here is a quick video demo of the process in Power Query.

### Things to keep in mind when converting JSON to Excel with Power Query ??:

*   **Nested Data:** If your JSON has nested data elements (for ex: skills attribute in our example above), you need to recursively expand all these items. But don’t expand them to “new rows” as this will create duplicate data. Instead just use “extract” option and get them all in one column with a delimiter like comma or semi-colon.
*   **Data type conversion:** By default Power Query may convert your data to relevant data types. But always double check this and apply any conversion necessary.
*   **Preview vs. Load:** Power Query Editor shows a preview of the JSON file for first 1000 rows, but actual conversion will only happen when you click on “close and load” button in Excel. So don’t freak out if you don’t see all the data in PQE (PQ Editor). It should appear when you load data to Excel.
*   **1 Million Row Limitation:** Excel spreadsheets can only hold 1,048,576 rows (just over 1 million). So if your JSON is really big, you need to think of another method. Here is an example of [how to use Excel if you have more than 1 million rows of data](https://chandoo.org/wp/wp-content/uploads/2019/09/how-to-handle-more-than-one-million-rows-in-excel.png)
    .

### Pros & Cons of using Excel to convert JSON:

**Pros:**

*   **Quick and easy:** Power Query in Excel offers a quick, easy and straightforward way to convert JSON to Excel.
*   **FREE:** Excel based conversion is free unlike paid methods.
*   **Refreshable:** Should your JSON files change or update, you can quickly refresh the Power Query connection to see updated data in Excel. This means any reports or calculations you build on top of the JSON will automatically update, thus providing up to date information.

**Cons:**

*   **Hard to work with deeply nested data:** If your JSON has multiple levels of nesting or hierarchies, then the Power Query based approach requires “drilling” to all these levels. As data can change often, if a new level of nesting appears in future, your Power Query refresh can fail.
*   **Requires understanding of Power Query:** While PQ is not deeply technical, it is not easy either. So if you are not familiar with PQ, you will find this method hard to use. Here is an [excellent beginner tutorial on Power Query with 4 powerful examples](https://chandoo.org/wp/power-query-tutorial/)
    .

### JSON to Excel conversion with Python (step by step):

#### Why Use Python for JSON to Excel Conversion?

While Excel’s Power Query can handle basic JSON imports, Python is often the better choice when dealing with large datasets, deeply nested JSON structures, or automating repetitive tasks. Using Python, we can efficiently read, manipulate, and export JSON data to an Excel file in just a few lines of code.

#### Installing Necessary Python Libraries

To begin, install the required libraries:

    pip install pandas openpyxl

These libraries will help us process the JSON data and save it in an Excel-friendly format.

#### Loading JSON Data in Python

Consider the following **employee data** stored in JSON format ([sample file](https://1drv.ms/u/c/e7c6dec249ad257b/ERaIG2aIJUpFlkeKcQTM7XEBX0Gxrfy1bMyO73BrtA9uhg?e=egbpBh)
).

    {
      "employees": [\
        {\
          "id": 1,\
          "first_name": "John",\
          "last_name": "Doe",\
          "email": "johndoe@awesomechoc.com",\
          "position": "Chocolatier",\
          "hire_date": "2023-06-15",\
          "skills": ["Baking", "Cocoa Sculpting", "Confectionary"]\
        },\
        {\
          "id": 2,\
          "first_name": "Jane",\
          "last_name": "Smith",\
          "email": "janesmith@awesomechoc.com",\
          "position": "Marketer",\
          "hire_date": "2024-02-20",\
          "skills": ["Packaging", "Product Design", "Field Sales"]\
        }\
      ]
    }

We can load this JSON file into Python using:

    import json
    import pandas as pd
    
    # Load JSON data from a file
    with open("employees.json", "r") as file:
        data = json.load(file)

#### Converting JSON to a Pandas DataFrame

Since the JSON structure contains a list under the `"employees"` key, we extract and convert it to a DataFrame:

    df = pd.DataFrame(data["employees"])

This will transform the data into a tabular format, making it easier to analyze and manipulate.

#### Exporting Data to an Excel File

To save the structured data as an Excel file:

    df.to_excel("employees.xlsx", index=False, engine='openpyxl')

This creates an Excel file **employees.xlsx**, which can be opened in Excel for further processing.

#### Handling Nested JSON Data

If the `skills` field is stored as a list, Excel might not display it properly. We can **flatten** this field:

    df["skills"] = df["skills"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)

Now, each employee’s skills will be stored as a **comma-separated string**, making it easier to read.

#### Automating JSON to Excel Conversion

For repeated tasks, we can automate the conversion by scheduling this Python script to run daily or whenever a new JSON file is added.

Python provides a scalable and efficient way to process JSON data and export it to Excel, making it ideal for large datasets and automation needs.

### Converting JSON to Excel with External Tools

If you don’t want to get your hands dirty with Power Query or Python based approaches, you can also use online tools to quickly convert JSON to Excel format.

#### **1\. Online JSON to Excel Converters**

These web-based tools allow users to upload a JSON file and instantly download an Excel file:

*   [**JSON to Excel by TableConvert**](https://tableconvert.com/json-to-excel)
    *   Converts JSON to structured Excel tables.
    *   Allows previewing and editing before download.
    *   Supports additional formats like CSV and Markdown.
*   **[JSONFormatter.org JSON to Excel](https://jsonformatter.org/)
    **
    *   Free tool with a simple drag-and-drop interface.
    *   Supports large JSON files.
*   **[JSON to CSV](https://www.convertcsv.com/json-to-csv.htm)
    **
    *   Upload your JSON file and download the CSV

These tools are great for **quick, one-time conversions**, but they may have file size limitations and require **manual steps** each time.

#### **2\. Using Power BI to convert JSON to Excel**

If you prefer to use a desktop software to convert JSON to Excel formats (like CSV or tables), you can use Power BI Desktop too. This doesn’t have 1 million row limitation so you ca use it to parse very large JSON files. The approach is same Excel Power Query technique, but the final data ends up in Power BI. You can either copy the table at the end of load process or use it directly inside Power BI to analyze the data.

**Final Thoughts**
------------------

If your JSON files are simple enough, just use Power Query in Excel to get the output the way you want. You can refresh this anytime your data changes.

On the other hand if your files are large or you need more control, use Python code samples above and tweak them to your needs.

If you have any questions, leave a comment so I can help you.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [One Comment](https://chandoo.org/wp/json-to-excel-howto/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/json-to-excel-howto/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel](https://chandoo.org/wp/tag/excel-2/)
    , [json](https://chandoo.org/wp/tag/json/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousNew vs. Returning Customers Analysis with DAX \[Easy Formulas\]](https://chandoo.org/wp/new-vs-returning-customers-dax/)

[NextHow to Create a Power BI Dashboard for Insurance Analytics (With Examples)Next](https://chandoo.org/wp/power-bi-insurance-analytics/)

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
    
    [Reply](https://chandoo.org/wp/json-to-excel-howto/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/json-to-excel-howto/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/json-to-excel-howto/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ