# Power BI Blog: Access-ible Returns Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Access-ible Returns Part 2

*   August 4, 2021

Power BI Blog: Access-ible Returns Part 2
=========================================

Power BI Blog: Access-ible Returns Part 2
=========================================

5 August 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we continue our Access-ible series of Blogs._

[Last week](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-1/)
, we narrowly avoided a processing nightmare by deciding not to remove duplicates _after_ we merged **CUSTOMCGIDS2016** and **vartable16**.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-152.jpg)

We explained that for such a large dataset, we need to remove duplicates before the merge. To do this, we need to create a copy of **vartable16**. There is more information on the types of copies that can be created in two of our Power Query Blogs: [Power Query: Durable Duplicates](https://sumproduct.com/blog/power-query-durable-duplicates/)
 and [Power Query: Reliable References](https://sumproduct.com/blog/power-query-reliable-references/)
. In this case we will be making a Reference copy of **vartable16**. We do this by right-clicking on the query and selecting Reference:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-204.jpg)

This creates a new query which uses **vartable16** as its source. This means that any changes to **vartable16** will be applied to this query too. We rename this query **Table Names**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-165.jpg)

We only need the columns **TableName** and **TableTitle**. We select both columns and then right-click on one of the column headings to ‘Remove other Columns’.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-159.jpg)

This leaves us with the two selected columns. We can then use ‘Remove Rows’ from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-131.jpg)

This will quickly give us a more compact table, which we will use to map the current table names to more descriptive names.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-115.jpg)

Back in the **CUSTOMCGIDS2016** query, we will delete the ‘Merged Queries’ and ‘Expanded **vartable16′** steps. We can do this by selecting the ‘Merged Queries’ step and then right-clicking to ‘Delete Until End’.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-107.jpg)

We can then choose ‘Merge Queries’ from the Home tab again: this time we are merging with **Table Names**.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-88.jpg)

This gives us a new column of tables called **Table Names:**

![](<Base64-Image-Removed>)

We expand the table data using the icon next to the column title:

![](<Base64-Image-Removed>)

This gives us a list of tables with their original name in **Item** and our preferred name in **TableTitle**.

![](<Base64-Image-Removed>)

We can filter on **Item** to see the expanded name for this table.

![](<Base64-Image-Removed>)

Now for the frustrating part. We can’t currently change the name of the query using **M** code. We now need to enter the new table name manually.

Having changed the query name, we now need to access the columns. We can do this by selecting **Data** and ‘Removing Other Columns’. Then we expand the table data in **Data.**

![](<Base64-Image-Removed>)

We want all the columns. We can rename them later – and we will _not_ be doing that manually!

![](<Base64-Image-Removed>)

We did say that we could use the steps here for the other tables. To do this, we select ‘Filtered Rows’ and right-click.

![](<Base64-Image-Removed>)

We have an option to ‘Extract Previous’ which is another way to create a Reference query.

![](<Base64-Image-Removed>)

We call the new query **Source with Table Name**, as we will be using this for the other tables to see the expanded name. **Custom comparison groups** now references the new query.

![](<Base64-Image-Removed>)

We can now use **Source with Table Name** as the source for the other tables. We will use **DRVIC2016** as an example. We can change the Source step to look at Source with Table Name: **M** Intellisense helps us.

![](<Base64-Image-Removed>)

We delete the Navigation step as we will be expanding the data after we have filtered. We filter on the results to get the expanded name for **DRVIC2016**:

![](<Base64-Image-Removed>)

This time, we will use part of the full title! We call the table **Total cost of attendance**. Now it’s the same process that we used for **Custom comparison groups**: we remove all columns other than **Data**, and expand **Data** to get all the columns.

We can now repeat this process to get useful names for all the tables. Next time, we’ll look at renaming the columns.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-2/#0 "close")

top