# Data Consolidation & Transformation With Python | Tutorial | ChallengeJP

**Source:** https://www.challengejp.com/blog/python-excel-data-consolidation-transformation

---

How to Use Python and Pandas for Data Consolidation and Transformation
======================================================================

*   ![Jacek Polewski](https://www.challengejp.com/wp-content/cache/flying-press/gravatar-0c5b42d9d6e4.png) [Jacek Polewski](https://www.challengejp.com/blog/author/adminchallengejp-com/ "Posts by Jacek Polewski")
    
*   August 27, 2020January 7, 2026

Last Updated on January 7, 2026

  
Python scripts can help you automate and improve the efficiency of your data analytics processes. Even a basic Python command will accelerate your work with data and Excel spreadsheets.

In this step-by-step tutorial, I’ll walk you through how to use Python and Pandas to consolidate multiple Excel or CSV files into one table. I will show you how to modify and transform data to your desired format. Finally, you will learn how to export the transformed data into one file. By the end of this tutorial, you’ll have become more familiar with Python, and you’ll see how beneficial it can be to your future data analysis. 

You can download the three sample CSV files or the entire script that I’ll use during this tutorial so that you can follow along and practice the steps for yourself:  
  
[**Data File 1**](https://www.challengejp.com/wp-content/uploads/2020/12/data_file_1.csv)

[**Data File 2**](https://www.challengejp.com/wp-content/uploads/2020/12/data_file_2.csv)

[**Data File 3**](https://www.challengejp.com/wp-content/uploads/2020/12/data_file_3.csv)

[**Entire Script for Consolidating and Transforming Data**](https://drive.google.com/file/d/1ug7czC-fxr2sRdbOK1EsEAebsT1joYvE/view?usp=sharing)

Once you’ve downloaded these files, save them in a local folder on your computer so that they’re easy to access when you need them. Then, you’ll be ready to follow the next eight steps to data consolidation and transformation.

**Note: If you’re more of a visual learner, scroll down to the bottom of this article and you’ll find a video version of this tutorial.**

Table of Contents

Toggle

**Step 1: Install Python/Anaconda** 
------------------------------------

If you don’t yet have Python on your computer, the first step is to install it. There are many different versions and ways to install Python programs, but one of the best options is Anaconda. Anaconda is one of the most popular and widely used programs by data scientists and analysts. This is a great open-source program, and it’s completely free – you can [download it here](https://www.anaconda.com/products/individual#Downloads)
.

Once you’ve installed Anaconda, create a new Jupyter notebook. We’ll use this to write the Python scripts to help us streamline the data consolidation process. Don’t forget to give your Jupyter notebook file a name — it will automatically save it in your folder.

[![create new jupyter notebook python](https://www.challengejp.com/wp-content/uploads/2020/08/create-a-new-jupyter-notebook-e1652087691839.png)](https://www.challengejp.com/wp-content/uploads/2020/08/create-a-new-jupyter-notebook.png)
  
_Create a new Jupyter notebook with Python._

**Step 2: Create Your First Python Script**
-------------------------------------------

Python programming might sound a little daunting, but lots of Python commands are pretty straightforward. So, before we jump into using scripts for data analysis, let’s introduce your first script: a print script, also known as a Python print() function.

As the name suggests, these scripts print the specified message on the screen. For example, type in _print(‘Hello World’),_ then hit shift+enter. You will see the sentence just below the first window. Congratulations, you have written your first script. You can now officially call yourself a Python programmer!

[![python print script](https://www.challengejp.com/wp-content/uploads/2020/08/python-print-script.png "python print script")](https://www.challengejp.com/wp-content/uploads/2020/08/python-print-script.png)
  
_A Python print script displaying “Hello World” in the first window._

After the print command, you can add _#text_. This is a comment that isn’t executable, so that it won’t affect your code. Comments are especially useful if you want to keep track of your Python code. For example, in the screenshot above, I’ve added _#your first python command_ to the right of the command. You can also add comments above or below your scripts. 

**Step 3: Import a Pandas Module**
----------------------------------

Now that you’ve tried out your first Python script, it’s time to start the data consolidation process. But first, make sure you’ve downloaded and saved the three CSV files at the top of the page. 

To load the CSV files into your notebook, you need to import a Pandas module, an add-on file extending Python’s basic functionalities. To do this, type “import pandas as pd”. 

[![Python command](https://www.challengejp.com/wp-content/uploads/2020/08/step-3-python-script.png "Python command")](https://www.challengejp.com/wp-content/uploads/2020/08/step-3-python-script.png)

_Python command to import Pandas module_

You could write “import pandas”, but adding the “as pd” creates a shortcut reference. The shortcut will come in handy in the next steps. Once you’ve written this command, hit shift+enter to execute it. 

Again, in the screenshot above, you’ll see I’ve added a comment with a reminder note about the “pd” shortcut. This doesn’t impact the command at all; it’s just for your benefit. It’s a good idea to get into the habit of using comments as often as possible. They will help you and any other users navigate the script and understand why certain commands have been used.

**Step 4: Load File Content** 
------------------------------

Once you’ve executed the “import pandas” command, you need to load your data files and assign them to a variable. Think of a variable as a labelled memory location to store values. The next script you need to enter will load the first CSV file (data\_file\_one) into your notebook.

This command will read _pd.read\_csv (_remember that “pd” is a shortcut reference to the “Pandas” module) followed by _(‘/directory/file\_name.csv’, sep=’;’)_. Rather than copying this command exactly, replace “directory” with the folder path where you store your files. This might be “_C:\\Documents\\Files\\_” for example. You’ll also need to replace “_file\_name_” with the name of your CSV file. For example, in our case, this would be “_data\_file\_one.csv_”. Your full command, with the correct directory and file name, should look something like this:

**_pd.read\_csv( ‘/home/jacekpolewski/tutorial\_files/data\_file\_1.csv’, sep=’;’)_**

The s_ep=’;’_ section of the command tells Python that columns in the data are separated (or delimited) with a semicolon.

Execute this command (shift+enter), and the file data will be displayed below the command.

**Step 5: Assign Data Content to a Variable**
---------------------------------------------

You can assign the file to a variable with your data loaded into the notebook. Write a name for this variable at the start of the command you’ve just written. Then, follow it by an equals sign before the rest of the command line. For example, I have used “_data\_1_ \=”, but what you want to call this variable is up to you. You can now hit Shift+Enter again, and your table should disappear. 

[![python load file assign variable](https://www.challengejp.com/wp-content/uploads/2020/08/python_variable_file_assignment-Edited.png)](https://www.challengejp.com/wp-content/uploads/2020/08/python_variable_file_assignment-Edited.png)

_Python command to load a file content into the notebook, assign a dataset to a variable._

**Step 6: Inspect Data Using the Head() Function**
--------------------------------------------------

After loading your data and assigning it to a variable, inspecting the data to see if all of the content has loaded correctly is a good idea. You can do this by looking at the first few rows of the data using the Python head() function.

All you need to do is type _data\_1.head()_ into your next command, and the first five rows of the data will open beneath the command.

You’ll notice the snippet of the data content will contain an extra column with index numbers, which was not part of the original CSV file. Python automatically adds an index column that contains a set of unique reference numbers assigned to each row (in the same way that Microsoft Excel assigns a unique number to a row and a unique letter to a column).

[![inspect data python head example](https://www.challengejp.com/wp-content/uploads/2020/08/python-data-consolidation-e1608152339603.png)](https://www.challengejp.com/wp-content/uploads/2020/08/python-data-consolidation-e1608152339603.png)

_Inspect the first few rows of the file content with Panda’s .head() function._

**Note:** The technical term for the dataset in Pandas is a “data frame”. A data frame is structured like a table or a spreadsheet with indexes, rows, columns and header names. For simplicity, this tutorial will, for the most part, refer to DataFrames as datasets or tables.

**Step 7: Consolidate the Three Datasets**
------------------------------------------

Repeat steps 3-6 until you’ve loaded the three tutorial CSV files and assigned each dataset to a variable. When all datasets are loaded and assigned, you can start the data consolidation process (see screenshot below).

[![example read csv python pandas](https://www.challengejp.com/wp-content/uploads/2020/08/read_csv_python_pandas_example-e1608152512848.png)](https://www.challengejp.com/wp-content/uploads/2020/08/read_csv_python_pandas_example-e1608152512848.png)

_Read the remaining CSV files and assign them to Python variables._

We want to consolidate the three datasets into one data frame called _data\_comb,_ so type in d_ata\_comb = pd.concat(\[data\_1, data\_2, data\_3\], ignore\_index = True)_ and hit Shift+Enter. 

The [_pd.concat_ section of the command](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
 is what instructs Python to combine the files. All the data you want to combine should be within the square brackets. The ignore index function resets all of the index numbers. When the data files have been combined, a new index column is calculated for the new complete dataset. You will notice that index values are incrementally counted from 0 with no duplicates in the numbers.

You can then assign this new consolidated dataset a variable by typing _data\_comb =_ at the start of the command. Just like when you assign the previous datasets to variables, the table will disappear, and you can then inspect the data to check it has loaded correctly. 

As well as using the head() function to inspect the first five rows and the tail() function to check the last five rows. Five rows are the default amount you’ll see. If you’d rather view more rows, you can insert a value such as 10 in the parentheses, and you’ll see the number of rows change.

[![python script data consolidation](https://www.challengejp.com/wp-content/uploads/2020/08/python-script-data-consolidation-e1608152667868.png "python script data consolidation")](https://www.challengejp.com/wp-content/uploads/2020/08/python-script-data-consolidation-e1608152667868.png)

_Python script for consolidating data and inspecting file content._

**Step 8: Further Checks and Validations**
------------------------------------------

It’s a good idea to carry out a few further checks and validations to ensure the data is combined and loaded correctly, as errors can compromise the integrity of your data analysis.

One way to assess the accuracy of the _data\_comb_ dataset is to check the number of rows in each dataset. Add the numbers and compare them to the total number of rows of the combined dataset. 

To do this, first type in and execute _data\_1.shape_. You will notice two values enclosed in parentheses. The first value _(100)_ corresponds to the number of rows, and the second _(2)_ to the number of columns in the dataset. Add \[0\] to the end of the command to display just the number of rows so that it reads _data\_1.shape\[0\]_. Then, to compute the sum of rows of each dataset, use the command _data\_1.shape\[0\] + data\_2.shape\[0\] + data\_3.shape\[0\]_. In this case, the output value should equal 300. 

To compare this with the total number of rows in the total dataset and make sure the datasets match up, type and execute the command _data\_comb.shape\[0\]._ As a result, the output value should also equal 300. If it doesn’t, that’s the first sign that the data has not loaded or consolidated correctly.

[![use of python](https://www.challengejp.com/wp-content/uploads/2020/08/use-of-python.png "use of python")](https://www.challengejp.com/wp-content/uploads/2020/08/use-of-python.png)

_Using Python commands to check that data is combined and loaded correctly._

**Step 9: Data Transformation/Preparation**
-------------------------------------------

If you need to modify your data or transform it into your desired format before extracting valuable insights, Python and Pandas make it as fast and easy as possible to do so. 

If you need to create a new column, type in and execute _data\_comb\[‘Test’\] = ‘hello’_. When you inspect the data, you will notice a new column called _‘Test’_ filled with the value _‘hello’_.

![adding new column to Pandas dataframe](https://www.challengejp.com/wp-content/uploads/2020/08/consolidated-dataset.png "consolidated dataset")

_Adding a test column to the consolidated dataset, filled with the values “hello”_

You can also create new columns based on an already existing column. The _data\_comb_ contains a _‘Full Name’_ column which consists of both _‘Last Name’_ and _‘First Name’_ values separated by a comma. You can separate these values into two columns by using a [split function](https://www.geeksforgeeks.org/split-a-text-column-into-two-columns-in-pandas-dataframe/)
 _— data\_comb\[\[‘Last Name’,’First Name’\]\] = data\_comb\[‘Full Name’\].str.split(“,”, expand=True)._ 

The left side of the above command encloses the columns’ two names to be created in a couple of double \[\] brackets. If you have more than one column, list the names in a \[\] bracket, hence the double signage. The _.str_ on the right side of the command indicates that we will be operating on a string or a text column. The _“,”_ in the command is the delimiter that separates the two name values and _expand = True_ is explicitly responsible for adding those two new columns. 

Once you’ve executed the command, inspect the new table again. You should see the _‘First Name’_ and _‘Last Name’_ columns on the right side of the table.

![split function pandas python example](https://www.challengejp.com/wp-content/uploads/2020/08/split-function-python.png "split function python")

_Splitting text to columns in Python using the split function._

If at any point, you need to delete columns — for example, you might want to delete the test column we just created — you can use the command: _data\_comb.drop(columns=\[‘Test’\], inplace=True)._

**Step 10: Using V-Lookup Equivalent in Python**
------------------------------------------------

Microsoft Excel’s v-lookup function is a must-use for any data analyst or scientist. You can use the .map() function in Python to imitate a v-lookup. 

First, use the command _data\_comb\[\[‘day\_no’, ‘month\_name’, ‘year\_no’\]\] = data\_comb\[‘Birth Date’\].str.split(‘-‘, expand=True)_ to split the ‘_Birth Date’_ column into three separate columns. Inspect the _data\_comb_ DataFrame with _.head(),_ and you will notice that the values in _‘month\_name’_ column are in text format.

![python data frame](https://www.challengejp.com/wp-content/uploads/2020/08/python-data-frame.png "python data frame")

_Splitting columns and inspecting the DataFrame with .head()_ 

For consistency, we want to create an additional column with the _month\_name_ value converted to its numerical equivalent. To do this in Microsoft Excel, you would create a separate table or a sheet. The first column would be filled with month names and the second with their numerical equivalents. You would then use a v-lookup formula between the lookup value and the table. In Python we can use the _.map()_ function. First, we need to create a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp)
 which, in this case, is equivalent to the table array part of the v-lookup: 

_month\_lookup = {  
__‘Jan’: 1,  
__‘Feb’: 2,  
__‘Mar’: 3,  
__‘Apr’: 4,  
__‘May’: 5,  
__‘Jun’: 6,  
__‘Jul’: 7,  
__‘Aug’: 8,  
__‘Sep’: 9,  
__‘Oct’: 10,  
__‘Nov’: 11,  
__‘Dec’: 12  
__}_

Notice that the values are enclosed in curly brackets {} and the lookup value (or the key value) is followed by “:” (which assigns it a relevant value), and each pair is separated with commas. 

To create the new _‘month\_no’_ column, use the command _data\_comb\[‘month\_no’\] = data\_comb\[‘month\_name’\].map(month\_lookup)_. And, like we’ve done after most other steps, inspect the dataset to ensure the output works as expected.

![excel v-lookup python map](https://www.challengejp.com/wp-content/uploads/2020/08/v-lookup-python.png "v-lookup python")

_Using the Python .map() function as an alternative to Excel v-lookup function._

**Step 11: Export File to CSV, Excel and/or Clipboard**
-------------------------------------------------------

You’ve learned to consolidate and transform your Excel datasets in Python, so it’s now time to export your file. 

Firstly, type in and execute _import csv_ to add a new module. To export the data\_comb DataFrame, type in and execute command _data.to\_csv(‘path/filename.csv’, sep=’;’, index=False)_. Replace the _path/filename_ with your own file address. The _sep=’;’_ separates columns in the exported files with “;” and the _index=False_ ensures that the index column is not part of the output (use _index=True_ to keep the index column).

You can also copy the table into a clipboard by executing the command _data\_comb.to\_clipboard()_. This allows you to open an empty notepad, Excel document or Google Sheet and simply paste the data in. Finally, to export the _comb\_data_ to Microsoft Excel, use the command _data\_comb.to\_excel(filename)_. There is no need to define a _sep_ argument in this case.

[![create new jupyter notebook python](https://www.challengejp.com/wp-content/uploads/2020/08/export-data-python.png "export data python")](https://www.challengejp.com/wp-content/uploads/2020/08/export-data-python.png)

_Exporting a DataFrame from Python to CSV, Microsoft Excel and clipboard._

**Summary: From Data Consolidation to File Export**
---------------------------------------------------

This tutorial has shown you how to import and combine individual data files using Python. To load a csv file, use a _.read\_csv()_ function, part of the Panadas module. Assign the file to a data frame and repeat the command for your other files. Then, combine the data using _pd.concat()_. Don’t forget to inspect the new dataframe using _.head()_ or _.tail()_ functions.

To add a new column in Python, type in the name of your dataframe (e.g. data\_comb) and follow it by a column name enclosed in square brackets (e.g. data\_comb\[‘new\_column’). Then, follow it with an “=” sign and your new value. For example, to add a new column to your dataframe and fill it in with some text (e.g. ‘test’), type in _dataframe\_name\[‘column\_name’\] = ‘test’_.\
\
To create new columns from the existing data, you can use _.split()_ function. For example, to extract first and last names separated by a from a ‘Full Name’ column, we typed in _data\_comb\[\[‘First Name’, ‘Last Name’\]\] = data\_comb\[‘Full Name’\].str.split(“,”, expand=True)_. To map your existing data to a new set of values, create a dictionary, assign it to a variable and then use .map() function. For example, to translate month names to their numerical equivalents in our data, we executed the following scrip: _data\_comb\[‘month\_no’\] = data\[‘month\_name’\].map(month\_lookup)_.\
\
Python allows you to export your data into a file easily. To create a new csv file, import a csv module and then use _.to\_csv()_ function. For example, to export your dataframe, type in _dataframe\_name.to\_csv(“file\_path”, sep=”,”, index=False)_. To export data into an Excel file, use _.to\_excel()_ function, and to save it to a clipboard, use _.to\_clipboard()_.\
\
**Watch: Video Tutorial**\
-------------------------\
\
You can watch the step-by-step tutorial on how to load, consolidate and export the data in Python in the video below.\
\
▶️ [Watch on YouTube](https://youtu.be/YiTQCHbvud0)\
\
![How to Use Python and Pandas for Data Consolidation and Transformation](https://www.challengejp.com/wp-content/cache/flying-press/YiTQCHbvud0-hqdefault.jpg)\
\
**Get in Touch**\
----------------\
\
_[![challengejp_data_analyst](https://www.challengejp.com/wp-content/uploads/2020/07/jp_photo-300x200.jpg)](https://www.challengejp.com/about/)\
Hi, my name is Jacek and I love spreadsheets! I hope you’ve enjoyed reading this tutorial as much as I did writing it. If you have any questions about Python and data analysis, don’t hesitate to **[get in touch](https://www.challengejp.com/contact/)\
**._\
\
_[**Explore my other tutorials**](https://www.challengejp.com/blog/)\
 to learn more about data and financial analysis. If you need further support, find out about my [**One-to-One Training**](https://www.challengejp.com/services/financial-modelling-data-training/)\
 and **[Data Analytics Services](https://www.challengejp.com/services/data-analytics/)\
**._\
\
Learn More\
----------\
\
[Analyze and Forecast Customer Churn and Revenue](https://www.challengejp.com/blog/power-bi-customer-churn-revenue-forecast-tutorial/)\
 – Build a churn/retention model in Microsoft Power BI using DAX, cohort analysis, and interactive forecasts.\
\
[Power BI Consolidated P&L & Forecast Tutorial](https://www.challengejp.com/blog/power-bi-consolidated-pl-forecast-tutorial-template/)\
 — learn how to merge data from multiple entities, apply FX conversions, and create a complete forecasting model in Microsoft Power BI.\
\
[Learn How to Become a Self-Taught Data Analyst](https://www.challengejp.com/blog/learn-to-become-data-analyst/)\
 – Here, I share a few tips and resources I found using while learning to become a data analyst.\
\
[How to Analyse Data in Microsoft Excel with Power Query and a Pivot Table](https://www.challengejp.com/blog/how-to-analyse-data-excel-tutorial/)\
 – This step-by-step tutorial will take you through an example of using Pivot Tables and Power Query to transform and analyse data.\
\
[How to Use Cohort Analysis to Calculate Retention and Churn Rate](https://www.challengejp.com/blog/churn-cohort-analysis/)\
 – A tutorial and an example of using Pivot Tables to analyse customer data and better understand users’ behaviour.\
\
Tags:[Data Analytics](https://www.challengejp.com/blog/tag/data-analytics/ "Data Analytics")\
[Python Tutorial](https://www.challengejp.com/blog/tag/python-tutorial/ "Python Tutorial")\
\
  \
\
**Redirecting to FastSpring for secure payment and local tax handling in your region...**\
\
You’ll see challengejp.onfastspring.com in your address bar.