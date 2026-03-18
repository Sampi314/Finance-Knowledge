# Power Query: Less Aggravating Aggregating

**Source:** https://sumproduct.com/blog/power-query-less-aggravating-aggregating/

---

[Home](https://sumproduct.com/)

\> Power Query: Less Aggravating Aggregating

*   May 30, 2017

Power Query: Less Aggravating Aggregating
=========================================

Power Query: Less Aggravating Aggregating
=========================================

31 May 2017

_Welcome to our Power Query blog. Today I look at combining data from tables in Excel worksheets in other workbooks (again), with less steps thanks to the recent Combining Files improvements._

In [Aggravating Worksheets in Other Workbooks](https://sumproduct.com/blog/power-query-aggregating-aggravating-worksheets-in-other-workbooks/)
, I combined data from tables in workbooks that I’d gathered into one folder. You may recall that using combining binaries produced an error, so I resorted to a more manual method. This time, armed with an updated version of Power Query, I’m going to try it a different way.

I start as before, by getting a list of the workbooks that contain the data I propose to aggregate. To do this, I start in a new workbook and create a blank query which is ‘From Folder’ as shown below:

![](https://sumproduct.com/wp-content/uploads/2025/05/04ff06daf6e654bf228331b1d56e5461.jpg)

I have created a folder with my expense worksheets and some other items lurking around.

![](https://sumproduct.com/wp-content/uploads/2025/05/59e466391d1c7e87c3ebf6839489e3b5.jpg)

I don’t want to attempt to combine at this point as some of those files are not expenses! My next step is to edit my query to filter out the other files so that I am left with the workbooks. I also want to make sure that any expense workbooks added in future would be picked up. So that any other workbooks would also be saved regardless of the extension, I transform the case to ‘lowercase’ by right-clicking on the **_Extension_** column and choosing the ‘Transform’ option. I then filter to pick up any extensions that start with ‘.xls’:

![](https://sumproduct.com/wp-content/uploads/2025/05/cb7d6535f5acafca8d0d9d75126723ed.jpg)

This leaves me with the files that I want.

![](https://sumproduct.com/wp-content/uploads/2025/05/7b31de0603b2b738d9eb7b57a5d659cf.jpg)

Power Query has been updated since [Aggravating Worksheets in Other Workbooks](https://sumproduct.com/blog/power-query-aggregating-aggravating-worksheets-in-other-workbooks/)
 and some things have been tweaked. The icon is still next to **_Content_**, but now instead of being called a ‘Combine Binaries’ button, it is a ‘Combine Files’ button. Pressing it begins the process, which shows me what is available in the first file:

![](https://sumproduct.com/wp-content/uploads/2025/05/5d12028a979ca545d61952c7102381c0.jpg)

The options I have are to choose the table, the sheet or the parameters. I also have the option to ‘Skip files with errors’ which is a clue that the error handling has been improved now. I choose the one that looks like a sheet to see if it works now.

![](<Base64-Image-Removed>)

I click ‘OK’ to combine the sheets.

![](<Base64-Image-Removed>)

Like before, Power Query can’t see how to link my data together, and a similar thing happens if I pick the table. There is however a third option, so I delete all the steps so that I am back at ‘Filtered Rows’, and use the ‘Combine Files’ button again – this time I pick the sample folder option:

![](<Base64-Image-Removed>)

I have no option to preview anything this time, but when I press ‘OK’…

![](<Base64-Image-Removed>)

Now this looks much better! I am now ready to filter and expand my data without having to create a custom column. I also have my filename instead of the folder location as I got with my manually created column. The filename would be useful if I have to pull out information into my data (see [What’s in a Name?](https://sumproduct.com/blog/power-query-whats-in-a-name/)
 for more on this).

As an aside, when combining files, it can also help to select the sample file that shares as many attributes as possible with the other files, which is another way of avoiding errors. This is now possible with a new feature available on the ‘Combine Files’ screen.

![](<Base64-Image-Removed>)

Back with my combined files, in the **_Kind_** column, I clearly still have some danger of duplication as there are two rows for each person; one with value ‘Table’ and one with value ‘Sheet’. I choose to filter and keep the rows where the **_Kind_** column is populated with ‘Sheet’. I can also get rid of most of the columns as I only want the **_Name.1_** and **_Data_** columns.

![](<Base64-Image-Removed>)

Note that Power Query is fine filtering on **_Kind_** even though it no longer appears. I can now expand my **_Data_** column:

![](<Base64-Image-Removed>)

I clearly still have some tidying up to do, but the data is all there ready to be transformed. Once I am happy I can upload my data.

![](<Base64-Image-Removed>)

So, thanks to the updates to ‘Combine Binaries’ (now ‘Combine Files’), it is much easier to combine the data without resorting to custom columns. One thing I am not so keen on with combining data in this way is that all the queries that Power Query creates automatically are kept. As shown above, the queries from my failed attempt to combine sheets are still there. With some housekeeping, I can tidy this up to just keep the queries that my ‘Expense Folder’ query references.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-less-aggravating-aggregating/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-less-aggravating-aggregating/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-less-aggravating-aggregating/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-less-aggravating-aggregating/#0)

[](https://sumproduct.com/blog/power-query-less-aggravating-aggregating/#0 "close")

top