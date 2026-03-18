# Power Query: Split Folder Part 12

**Source:** https://sumproduct.com/blog/split-folder-part-12/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 12

*   June 18, 2025

Power Query: Split Folder Part 12
=================================

_Welcome to our Power Query blog.  This week, I complete the task  to simplify the way that I combine the file types into one result._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://www.sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3)
.  In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others.  The folder shown below contains expense data for May 2024, but not all formats are the same: 

![](<Base64-Image-Removed>)

My task is to transform all the data and append into a single output Table.

In this series, I have used the ‘From Folder’ connector to extract data from the folder and transformed and filtered the filenames selected to create a Folder Filtered query.  I then took reference copies of this query which I filtered for each file type and used the Combine functionality to bring the data together for each file type.

I appended my data to create a new query **Monthly Expense Data** and sorted the data in ascending **Date** order:

![](<Base64-Image-Removed>)

Over the series, I have refined the solution using parameters whist keeping this structure.

In [Part 9](https://www.sumproduct.com/blog/split-folder-part-10)
, I turned my attention to the current query structure:

![](<Base64-Image-Removed>)

In particular, I filtered the files based upon their extension to create **XLSM Files**, **TEXT Files** and **CSV Files** and then combined them to make **Monthly Expense Data**. 

![](<Base64-Image-Removed>)

When I have numerous files of each type to process, this dividing and recombining will add to the time taken to produce the results I need.  The query that is split into **XLSM Files**, **TEXT Files** and **CSV Files** is **Folder Filtered**.  If I can run the appropriate combine process for each extension type from this query, I can speed up the solution.

![](<Base64-Image-Removed>)

**Folder Filtered** is used as the reference query for **XLSM Files**, **TEXT Files** and **CSV Files**.  However, I cannot remove  this query as it is also used by the Power Query helper files:

![](<Base64-Image-Removed>)

To simplify the process and reduced the number of queries, I am going to approach this in steps:

1.  Take a duplicate copy of **XLSM** **Files** which I will call **Process Folder**
2.  Modify the ‘Invoke Custom Function1’ step to call the appropriate combine function based on the file type
3.  Remove the filter step so it can be tested with all the file types
4.  Remove **Monthly Expense Data**, **TEXT Files** and **CSV Files**
5.  Load **Process Folder** to the Excel workbook.

In [Part 10](https://www.sumproduct.com/blog/power-query-split-folder-part-10)
, I took a duplicate copy of **XLSM Files** to create **Process Folder**.

![](<Base64-Image-Removed>)

[Last week](https://www.sumproduct.com/blog/power-query-split-folder-part-11)
, I amended  **Process Folder** to select the combine method based upon the **Extension** value.  I changed the step ‘Invoke Custom Function1’  to do this.  

> **`= Table.AddColumn(#"Filtered Hidden Files1", "Transform File", each`**
> 
>             **`if [Extension] = ".XLSM" then #"XLSM_Transform File"([Content])`**
> 
>             **`else if [Extension] = ".TXT" then #"TXT_Transform File"([Content])`**
> 
>             **`else if [Extension] = ".CSV" then #"CSV_Transform File"([Content])`**
> 
>             **`else null)`**

I then removed step ‘Filtered Rows’ and **Process Folder** is ready to test.

![](<Base64-Image-Removed>)

Before I start removing queries I no longer need, let’s compare these results with **Monthly Expense Data**:

![](<Base64-Image-Removed>)

I notice that I sorted the data and removed some columns and rows.  The reason for removing the additional data was because I was always combining all three file types.  See [Part 6](https://www.sumproduct.com/blog/split-folder-part-6)
 for how I dealt with this.  Now I only run the combine functions for the file types I find in the folder, there is no need for these steps.  I should still sort the data by date, so I add this step to **Process Folder**:

![](<Base64-Image-Removed>)

The results are now the same as **Monthly Expense Data**.  I should load **Process Folder** to the workbook as a final test.  I select ‘ Close & Load To…’ from the Home tab and initially choose  ‘Only Create Connection’ for **Process Folder**.

![](<Base64-Image-Removed>)

I may now choose where to load the data.  With the Outputs sheet open, I change query **Monthly Expense Data** to be ‘Connection Only’:

![](<Base64-Image-Removed>)

When I choose to proceed, I receive a message about potential data loss:

![](<Base64-Image-Removed>)

I choose to continue.  I change the query **Process Folder** to be loaded to the current sheet instead.

![](<Base64-Image-Removed>)

My data looks good and now I may delete the queries I no longer need.

![](<Base64-Image-Removed>)

I may delete the queries in the ‘Queries & Connections’ pane by selecting a query and right-clicking:

![](<Base64-Image-Removed>)

I may delete multiple queries at the same time:

![](<Base64-Image-Removed>)

I am asked if I am sure.  If there were any queries referencing these queries, I would not be allowed to delete them.

![](<Base64-Image-Removed>)

I choose to Delete and go back to view the ‘Query Dependencies’ dialog:

![](<Base64-Image-Removed>)

This is now much easier to follow and the process will be faster.  I test the solution by changing one of the parameters and refreshing **Process Folder**:

![](<Base64-Image-Removed>)

The rows are returned successfully.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/split-folder-part-12/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-12/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-12/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-12/#0)

[](https://sumproduct.com/blog/split-folder-part-12/#0 "close")

top