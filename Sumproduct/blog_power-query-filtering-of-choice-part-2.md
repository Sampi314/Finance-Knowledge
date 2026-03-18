# Power Query: Filtering of Choice Part 2

**Source:** https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Filtering of Choice Part 2

*   September 3, 2024

Power Query: Filtering of Choice Part 2
=======================================

Power Query: Filtering of Choice Part 2
=======================================

4 September 2024

_Welcome to our Power Query blog. This week, I continue to work on a challenge involving a choice of filters by transforming **P\_Choice**._

[Last week](https://sumproduct.com/blog/power-query-filtering-of-choice-part-1/)
, I described my current challenge. Essentially, I have a Table of data, **Tbl\_Sales\_Data**, shown below:

![](<Base64-Image-Removed>)

I will be filtering this data, by comparing values from one of these Tables, which have been named **Tbl\_Dates**, **Tbl\_Amounts** and **Tbl\_Person**:

![](<Base64-Image-Removed>)

The choice of which Table to use is controlled by a dropdown, which has been given the Named Range **P\_Choice** and another translation Table, **Tbl\_Translation**:

![](<Base64-Image-Removed>)

In **Tbl\_Translation**, the first column, **Choice** will link to the value from the dropdown. The second column **Translation**, then translates to a column from the data Table. All of the data has been entered manually and the results will be driven by the value selected in **P\_Choice**.

![](<Base64-Image-Removed>)

Having extracted all the Tables and **P\_Choice** to Power Query, I need to consider how I should begin to transform my data.

The key to solving this problem lies with lists. I need to convert the queries **Tbl\_Dates**, **Tbl\_Amounts** and **Tbl\_Person** into a format where I have a list of values within the table _and_ an identifier for the list, which will allow me to merge with **P\_Choice**.

I begin in **Tbl\_Dates**, where I remove the ‘Changed Type’ step, and choose to ‘Unpivot Columns’ from the right-click menu:

![](<Base64-Image-Removed>)

This gives me two \[2\] columns, the list of values and the identifier, as required:

![](<Base64-Image-Removed>)

I repeat this process for **Tbl\_Amounts**:

![](<Base64-Image-Removed>)

I repeat the process one more time for **Tbl\_Person**:

![](<Base64-Image-Removed>)

I am ready to start building from **P\_Choice**. Starting from here, I need to merge with all three \[3\] of the unpivoted queries: **Tbl\_Dates**, **Tbl\_Amounts** and **Tbl\_Person**, as I may need to get the data to filter by from any of these tables, depending upon the value in **P\_Choice**. Unlike appending, I may only merge with one other table at a time. However, the data in the three unpivoted tables is in the same structure, therefore I may append them, and then merge the result with **P\_Choice**.

I begin in **Tbl\_Dates**, and choose to ‘Append Queries’ from the Home tab:

![](<Base64-Image-Removed>)

In the dialog, I choose to append ‘Three or more tables’, and whilst holding down the **CTRL** key, I select **Tbl\_Amounts** and **Tbl\_Person** from ‘Available tables’. I may then use the ‘Add’ button to create a list of ‘Tables to append’:

![](<Base64-Image-Removed>)

I click ‘OK’ to perform the append:

![](<Base64-Image-Removed>)

I have renamed the step to reflect the tables appended. I return to **P\_Choice**, where I select ‘Merge Queries’ from the Home tab:

![](<Base64-Image-Removed>)

I choose to merge with **Tbl\_Dates**:

![](<Base64-Image-Removed>)

I link **Column1** from **P\_Choice** to Attribute of **Tbl\_Dates** and use the default ‘Left Outer’ join. The message that ‘The selection matches 1 of 1 rows from the first table’ indicates that at least one filter value has been selected:

![](<Base64-Image-Removed>)

I may now expand the data to find the filter values:

![](<Base64-Image-Removed>)

I only need the **Value** column, and I have no need to ‘Use original column name as prefix’:

![](<Base64-Image-Removed>)

The data is still not quite ready. I need to merge with **Tbl\_Translation**, as I will need to know the column name on **Tbl\_Sales\_Data**.

![](<Base64-Image-Removed>)

I link **Column1** of **P\_Choice** to **Choice** of **Tbl\_Translation** and use the default ‘Left Outer’ join again.

![](<Base64-Image-Removed>)

I rename the step to make it clear that I have picked up the translations. I may now expand the data:

![](<Base64-Image-Removed>)

Having selected the **Translation** column, I may now remove **Column1** too:

![](<Base64-Image-Removed>)

Finally, I change the data type of **Value** to ‘Text’. The filter choices are ready; next time I will turn my attention to the **Tbl\_Sales\_Data** query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/#0)

[](https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/#0 "close")

top