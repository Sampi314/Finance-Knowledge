# Power Query: Split Folder Part 5

**Source:** https://sumproduct.com/blog/split-folder-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Split Folder Part 5

*   April 30, 2025

Power Query: Split Folder Part 5
================================

Power Query: Split Folder Part 5
================================

30 April 2025

_Welcome to our Power Query blog. This week, I create parameters for the filtering process._

I have covered the topic of getting files from a folder in several blogs; the latest series was [Excel Files from a Folder Fiddle](https://sumproduct.com/blog/power-query-excel-files-from-a-folder-fiddle-part-3/)
. In this series, I will look at how I may extract files from a folder where some of the files require different transformations to others. The folder shown below contains expense data for May 2024, but not all formats are the same:

![](<Base64-Image-Removed>)

My task is to transform all the data and append into a single output Table.

In [Part 1](https://sumproduct.com/blog/split-folder-part-1/)
, I used the ‘From Folder’ connector to extract data from the folder, and transformed and filtered the data to ensure I only had the expense data.

![](<Base64-Image-Removed>)

I took three \[3\] reference copies of **Folder Filtered**, one for each file type:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/split-folder-part-2/)
, I transformed the data in **XLSM Files** and **TXT****Files**.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

In [Part 3](https://sumproduct.com/blog/split-folder-part-3/)
, I transformed the **CSV Files**. Intially, there was only one CSV file, but I assumed that there could be more when I refreshed the data, so I used the ‘Combine Files’ approach.

![](<Base64-Image-Removed>)

I appended my data to create a new query **Monthly Expense Data**, and sorted the data in ascending **Date** order:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/split-folder-part-4/)
, I tested the process by changing and adding data. Now I have a working process, I would like to refine it. When I created the **Folder Filtered** query, I filtered based on the strings that I expected to be in the data.

![](<Base64-Image-Removed>)

In the ‘Filter Rows’ dialog, I have the option of using parameters:

![](<Base64-Image-Removed>)

I choose to create a ‘New Parameter’ from here:

![](<Base64-Image-Removed>)

When I click OK, the parameter is selected:

![](<Base64-Image-Removed>)

I also create a parameter for the TXT files:

![](<Base64-Image-Removed>)

When I click OK, the query looks the same, but I am now using parameters for this step:

![](<Base64-Image-Removed>)

The parameters I have created are internal to Power Query, and may be amended from the ‘Manage Parameters’ dropdown:

![](<Base64-Image-Removed>)

The value may also be changed in the Queries pane:

![](<Base64-Image-Removed>)

Whilst this is better than hard coding, this is only suitable for users who are comfortable using Power Query. Next time, I will look at getting this information from the Excel sheet instead.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/split-folder-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/split-folder-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/split-folder-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/split-folder-part-5/#0)

[](https://sumproduct.com/blog/split-folder-part-5/#0 "close")

top