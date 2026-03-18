# Power Query: Project Population – Part 14

**Source:** https://sumproduct.com/blog/power-query-project-population-part-14/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 14

*   July 25, 2023

Power Query: Project Population – Part 14
=========================================

Power Query: Project Population – Part 14
=========================================

26 July 2023

_Welcome to our Power Query blog. This week, I complete the Project Population series._

I have found some information on population growth provided by The World Bank, which I am using as an example of how to transform real-life data.

![](<Base64-Image-Removed>)

I have been transforming the data, and [last week](https://sumproduct.com/blog/power-query-project-population-part-13/)
, I created a query by merging **Country** and **Data**, using Left Anti join, to get the rows from **Data** which don’t match a **Country Code** on **Country**(or, by extension, **Population Estimates by Country**).

![](<Base64-Image-Removed>)

This time, I will tidy up this query. The first thing I shall do is to make the existing Source step more efficient. The **M** code is currently:

**\= Table.NestedJoin(Data, {“Country Code”}, Country,  
{“Country Code”}, “Country”, JoinKind.LeftAnti)**

In this case, I definitely do not want to change this to use **Table.Join(),**since I don’t need any columns from **Country**. I do however want to use **Table.Buffer()** to speed up the merge:

**\= Table.NestedJoin(Table.Buffer(Data), {“Country Code”},  
Table.Buffer(Country), {“Country Code”}, “Country”,  
JoinKind.LeftAnti)**

As usual, this has no impact on the appearance of my query:

![](<Base64-Image-Removed>)

Since merging always follows the same process, even though I have used a ‘Left Anti’ join to find those **Country Code** values on Data that did not have a match in **Country**, I still have a column where I could extract the **Country** columns:

![](<Base64-Image-Removed>)

Unsurprisingly, if I click on the space next to one of the ‘Table’ values, there is not much to see:

![](<Base64-Image-Removed>)

Therefore, I delete the **Country** column by selecting it and pressing the **Delete** key.

![](<Base64-Image-Removed>)

Since I know that the **Country Code** column in this query is representing more than just one country, I change the column name to **Region Code**. Similarly, I rename **Country Name** to **Region Name**. I also rename the query **Region Data**:

![](<Base64-Image-Removed>)

I could wait until I upload the query to see how many rows are uploaded, but there is another way. I select the **Region Code** column, and on the Transform tab, I choose ‘Count Values’.

![](<Base64-Image-Removed>)

This will tell me how many rows in this column have values other than blank or null.

![](<Base64-Image-Removed>)

My answer is 5,940 rows. Note that this uses **List.NonNullCount()**, so if I wanted to include this data in my query, I could put this **M** code into a ‘Custom Column’ using the option on the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

The number of rows is now shown with my data and I move it to the beginning of the query by right-clicking on the **Count** column and choosing ‘Move to Beginning’:

![](<Base64-Image-Removed>)

Finally, I will load the queries I have created into Excel (having changed the data type of **Count** to a Whole Number). I choose ‘Close & Load’, and right-click on the query I wish to load to the current sheet. This presents me with the ‘Import Data’ dialog, where I choose to load to Table, and select a cell on the existing worksheet:

![](<Base64-Image-Removed>)

I can repeat this process for the **Region Data** query:

![](<Base64-Image-Removed>)

I’ve proved that the count is correct!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-14/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-14/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-14/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-14/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-14/#0 "close")

top