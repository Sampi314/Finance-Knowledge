# Power Query: Split Folder Part 4

**Source:** https://sumproduct.com/blog/split-folder-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 4

*   April 23, 2025

Power Query: Split Folder Part 4
================================

Power Query: Split Folder Part 4
================================

23 April 2025

_Welcome to our Power Query blog. This week, I test the query I have created by changing and adding data._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder, where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](<Base64-Image-Removed>)

My task is to transform all the data and append into a single output Table.

In [Part 1](https://sumproduct.com/blog/split-folder-part-1/)
, I used the ‘From Folder’ connector to extract data from the folder and transformed and filtered the data to ensure I only had the expense data.

![](<Base64-Image-Removed>)

I took three \[3\] reference copies of **Folder Filtered**, one for each file type:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/split-folder-part-2/)
, I transformed the data in **XLSM Files** and **TXT****Files**.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/split-folder-part-3/)
, I transformed the **CSV Files**. Currently, there is only one CSV file, but I assumed that there could be more when I refresh the data, so I used the ‘Combine Files’ approach.

![](<Base64-Image-Removed>)

I appended my data to create a new query:

![](<Base64-Image-Removed>)

I renamed the query **Monthly Expense Data**, and sorted the data in ascending **Date** order:

![](<Base64-Image-Removed>)

This time, I will test the process by changing and adding data and explore how I may refine the process. I begin by adding the hotel expense amount to Newbie’s data:

![](<Base64-Image-Removed>)

I also add a similar file for Newbie’s friend Rookie:

![](<Base64-Image-Removed>)

Rookie’s expenses have two \[2\] columns to ignore. I also add an irrelevant TXT file to the folder to be ignored, and a new XLSM file that should be picked up (for Brian). Brian hasn’t quite got it right either, as his workbook has two \[2\] sheets:

![](<Base64-Image-Removed>)

Making sure all the files I am planning to extract are closed, I check my queries to ensure that they are all working as I would like. I begin by checking the Source step of **Folder Filtered**:

![](<Base64-Image-Removed>)

This looks good: all the files have been found. I am expecting ‘Ignore\_me.txt’ to be filtered out:

![](<Base64-Image-Removed>)

The filtering is working, and there are no issues. Next, I’ll look at each of the file type queries. I begin with **TXT Files**:

![](<Base64-Image-Removed>)

No issues here; next, I look at **CSV Files**:

![](<Base64-Image-Removed>)

Rookie’s expenses have been picked up, as has Newbie’s amended hotel bill. Let’s look at **XLSM Files**:

![](<Base64-Image-Removed>)

There is a refresh warning, although I do appear to have Brian’s expenses. The refresh warnings can trigger without an apparent reason. It’s usually safe to just close the warning, though in very early versions of Power Query this can sometimes cause an error, in which case it is better to refresh. In Brian’s data there is a row with nulls in all columns except **Name**. I should fix this, so I will change **XLSM\_Transform Sample File**:

![](<Base64-Image-Removed>)

Since Brian comes first in the folder, this file has been used as the sample, which makes it easier to see what to remove. I will never want expenses with no date, so I filter on the **Date** column to remove _null_ values.

![](<Base64-Image-Removed>)

That looks better:

![](<Base64-Image-Removed>)

The row no longer appears in **XLSM\_Files**:

![](<Base64-Image-Removed>)

Now the queries to be appended look fine, it’s time to check **Monthly Expense Data:**

![](<Base64-Image-Removed>)

This looks good too – time to ‘ Close & Load’ to see the data in the workbook:

![](<Base64-Image-Removed>)

I now have 44 rows of data, and everything is working as I would expect. Testing is an important part of creating queries since new data can throw up new challenges. Next time, I consider how I may simplify the process.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-4/#0)

[](https://sumproduct.com/blog/split-folder-part-4/#0 "close")

top