# Power Query: Split Folder Part 3

**Source:** https://sumproduct.com/blog/split-folder-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 3

*   April 16, 2025

Power Query: Split Folder Part 3
================================

Power Query: Split Folder Part 3
================================

16 April 2025

_Welcome to our Power Query blog. This week, I continue_ _transforming the data for the file type queries._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](https://sumproduct.com/wp-content/uploads/2025/06/7153a118cb4e6be23ffedbe523c6402e.jpg)

My task is to transform all the data and append into a single output Table.

In [Part 1](https://sumproduct.com/blog/split-folder-part-1/)
, I used the ‘From Folder’ connector to extract data from the folder and transformed / filtered the data to ensure I only had the expense data.

![](https://sumproduct.com/wp-content/uploads/2025/06/823e8acdb047713f242abcb01ce2522e.jpg)

I took three \[3\] reference copies of **Folder Filtered**, one for each file type:

![](https://sumproduct.com/wp-content/uploads/2025/06/3b47c223a42e398bff5cff2534e4adea.jpg)

[Last time](https://sumproduct.com/blog/split-folder-part-2/)
, I transformed the data in **XLSM Files** and **TXT** Files. The **XLSM Files** transformations were reasonably straightforward, since the sheet name was consistent.

![](https://sumproduct.com/wp-content/uploads/2025/06/717286385ce245e9f2befc42a3dea911.jpg)

The transformations for **TXT Files** were more involved, as I needed to make the changes to **TXT\_Transform Sample File** and ensure that there were no references to data unique to the first file.

![](https://sumproduct.com/wp-content/uploads/2025/06/789a5ea0601102f472b9b2f0fb8f35bc.jpg)

This time, I’ll transform **CSV Files**. Currently, there is only one CSV file, but I will assume that there could be more when I refresh the data, so I will use the ‘Combine Files’ approach. I begin by filtering, as I did for the other queries:

![](https://sumproduct.com/wp-content/uploads/2025/06/0b3b23c5eaab0fc4eb9918b260c33b08.jpg)

Next, I combine the files in the **Content** and take the defaults in the ‘Combine Files’ dialog to begin the process. I rename the Power Query generated ‘Helper Queries’ as I did for the other file type queries:

![](https://sumproduct.com/wp-content/uploads/2025/06/9563e73a73eadd3c609add5f5c9f07c3.jpg)

Since there are multiple transformations needed for this data, I will transform the **CSV\_Transform Sample File** query:

![](<Base64-Image-Removed>)

Since Newbie has added a **Personal** column, I need to remove this. I need to avoid naming this column in the step as other CSV files may not have this column. Instead, I choose to keep the other columns and ‘Remove Other Columns’. My next step is to select the **Name** and **Date** columns, and choose to ‘Unpivot Other Columns’ to bring the expense data into one column:

![](<Base64-Image-Removed>)

The data is now in a similar format to the other file type queries:

![](<Base64-Image-Removed>)

There are a few more changes to make. I need to rename **Attribute** to **expense code**, and **Value** to **amount**. I also need to change the data type of **amount** to a decimal number:

![](<Base64-Image-Removed>)

I would also like to change **Date** to a ‘date’ data type, but since there is a time, it will give me an error. I could either change it to a datetime data type and then to a date; this must be a separate step or else I can remove the time by replacing the string “00:00” with nothing. I choose to insert the latter as a step before the ‘Changed Type’ step, so that I may only have one ‘Changed Type’ step:

![](<Base64-Image-Removed>)

To fill down the **Name** column, I will replace space with _null_ and then use the ‘Fill Down’ functionality. I notice that there is a zero \[0\] in one of the amounts, but I keep this in case it is something that Newbie plans to update with the correct value.

![](<Base64-Image-Removed>)

I have the same issue with **CSV Files** that I had with **TXT Files**. The ‘Changed Type’ step assumes I still have the original columns:

![](<Base64-Image-Removed>)

I delete the ‘Changed Type’ step, select all my columns and use ‘Detect Data Type’ from the Transform tab:

![](<Base64-Image-Removed>)

I may now append my data using ‘Append Queries as New’ from the Home tab of any of the three \[3\] data type queries:

![](<Base64-Image-Removed>)

I click OK to create a new query:

![](<Base64-Image-Removed>)

I rename the query **Monthly Expense Data** and sort the data in ascending **Date** order:

![](<Base64-Image-Removed>)

Finally, I ‘Close & Load To…’ and choose to view **Monthly Expense Data** in a Table:

![](<Base64-Image-Removed>)

I may now perform analysis on this data. Next time, I will test the process by changing and adding data and explore how I may refine the process.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-3/#0)

[](https://sumproduct.com/blog/split-folder-part-3/#0 "close")

top