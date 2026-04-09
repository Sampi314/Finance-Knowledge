# Power Query: Re-returning to the Folder

**Source:** https://sumproduct.com/blog/power-query-re-returning-to-the-folder/

---

[Home](https://sumproduct.com/)

\> Power Query: Re-returning to the Folder

*   September 6, 2022

Power Query: Re-returning to the Folder
=======================================

Power Query: Re-returning to the Folder
=======================================

7 September 2022

_Welcome to our Power Query blog. This week, I revisit extracting from a folder (yet) again, to show another approach._

Those readers who have followed this series since the beginning will appreciated how Power Query has moved on since the early days. This week, I return to the process of extracting data from a folder. I first looked at this in [Power Query: One Folder, One Query](https://sumproduct.com/blog/power-query-one-folder-one-query/)
 in early 2017. I revisited this topic again to show how Power Query has helped to reduce the number of steps I needed to take to transform my data.

In this example, I have 10 expense files in a folder called **PQ\_StandardExpenses**. In a blank workbook, I choose the ‘From File’ Option, and drop down to select ‘From Folder’:

![](https://sumproduct.com/wp-content/uploads/2025/05/7f82abacb9a6399e10c58728b5c49ede.jpg)

A simple browser window appears. Having chosen the correct folder, the metadata is displayed:

![](https://sumproduct.com/wp-content/uploads/2025/05/650d019669e6db3e4ec7cfb9033059f7.jpg)

At this point, I could choose to combine these files and I’d be done, but editing allows the data to be transformed, and some safety features to be added.

Some kind person has added some Excel workbooks in the folder, not to mention a strange file extension ‘kat’! I need to make sure nothing added to the folder in the future will mess up my query. I can also allow for users typing in **csv** or **CSV** when they create their files. I opt to ‘Transform Data’:

![](https://sumproduct.com/wp-content/uploads/2025/05/5b00a171f979c5018e92c59014bd05c1.jpg)

I start by transforming the **Extension** data to lowercase. I select the column and right-click to find the ‘Transform’ to ‘lowercase’ option.

![](https://sumproduct.com/wp-content/uploads/2025/05/a3689484ee02db23cf16de3c54f6f59e.jpg)

I can filter to just get those files with file extension ‘csv’. At the top of the **Extension** column there is a standard filter arrow: clicking on this reveals a number of options to transform the data in the column.

![](<Base64-Image-Removed>)

I could use the ‘Text Filter’, but instead, I will choose ‘csv’ from the radio list:

![](<Base64-Image-Removed>)

This generates a step to filter on ‘.csv’:

![](<Base64-Image-Removed>)

The query is now protected from stray workbooks and will include files with **.csv** and **.CSV** extensions. Simple!

Last time, I used the icon next to the **Content** column header. This is an icon () which appears with Binary files so that they may be combined. However, this time, I am going to take a slightly different approach. I shall create a function to transform all the files and extract the data from them. I right-click on the first cell in the **Content** column.

![](<Base64-Image-Removed>)

I choose to ‘Add as New Query’:

![](<Base64-Image-Removed>)

This has created a new query that points directly to the binary file I selected. The name is a little on the long side, so I rename it ‘**SampleExpense**‘.

In the Parameters area of the Home tab, from the ‘Manage Parameters’ dropdown I choose to create a ‘New Parameter’:

![](<Base64-Image-Removed>)

I call the new parameter **P\_Expense**:

![](<Base64-Image-Removed>)

Since I have set it to type Binary, I can only select the **SampleExpense** query from the dropdowns for ‘Default Value’ and ‘Current Value’. I click OK and the parameter appears in the query list, and I can right-click on it to create a Reference copy:

![](<Base64-Image-Removed>)

I rename the referenced copy to **TransformExpense**:

![](<Base64-Image-Removed>)

I right-click on **TransformExpense** and choose to ‘Create Function…’:

![](<Base64-Image-Removed>)

I am prompted for a name for the function:

![](<Base64-Image-Removed>)

I call it ‘**fxTransformExpense**‘ and click OK:

![](<Base64-Image-Removed>)

This may not seem like a useful function yet, as it isn’t doing anything. However, since it is linked to **TransformExpense**, I can make changes to that query which will be picked up by the function. I start by interpreting the binary as a CSV file:

![](<Base64-Image-Removed>)

This gives me the data in the file:

![](<Base64-Image-Removed>)

I transform the file, filling down the **Name** and renaming ‘**expense code**‘ to ‘**Expense Code**‘ and **amount** to **Amount**.

![](<Base64-Image-Removed>)

Now I am ready to go back to the original query with the list of Binary files. I choose to ‘Invoke Custom Function’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I choose the function I created and name the column. I want the function to act on the binary files in **Content**:

![](<Base64-Image-Removed>)

This gives me a new column:

![](<Base64-Image-Removed>)

The column has all the data I want, so I right-click and remove other columns, then I extract the data using the icon next to the title:

![](<Base64-Image-Removed>)

I want to keep all the columns, and use their original names with no prefix:

![](<Base64-Image-Removed>)

I have all my data, but I notice that the columns have not been given the correct Data Type, so I need to correct this before I load my data. Since this affects all the columns, I use ‘Detect Data Type’ from the Transform tab:

![](<Base64-Image-Removed>)

My data is now ready to load.  When more files of a similar structure are added to the folder and the query is refreshed, the function will be applied to the new data and the data will be loaded without needing to change the query.

![](<Base64-Image-Removed>)

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-re-returning-to-the-folder/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-re-returning-to-the-folder/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-re-returning-to-the-folder/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-re-returning-to-the-folder/#0)

[](https://sumproduct.com/blog/power-query-re-returning-to-the-folder/#0 "close")

top