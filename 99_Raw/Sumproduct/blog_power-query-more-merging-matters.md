# Power Query: More Merging Matters

**Source:** https://sumproduct.com/blog/power-query-more-merging-matters/

---

[Home](https://sumproduct.com/)

\> Power Query: More Merging Matters

*   March 23, 2021

Power Query: More Merging Matters
=================================

Power Query: More Merging Matters
=================================

24 March 2021

_Welcome to our Power Query blog. This week, I look at some ways to make merges more efficient._

[Last week](https://sumproduct.com/blog/power-query-merging-matters/)
, I looked at a scenario where I needed to combine data from two tables.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-230.jpg)

This time, I am going to look at some ways to make this as efficient as possible. I will start with a simple merge between the tables. I already have my tables **Charges** and **Descriptions** from last time. I start with **Charges**, and opt to ‘Merge Queries as New’ from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-293.jpg)

I choose the default left outer join and view the resulting **M** code.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-236.jpg)

The **M** code generated is:

**\= Table.NestedJoin(Charges, {“Table\_Key”}, Descriptions, {“Table\_Key”}, “Descriptions”, JoinKind.LeftOuter)**

The function used is **Table.NestedJoin()**:

Table.NestedJoin(table1 as table, key1 as any, table2 as any, key2 as any, newColumnName as text, optional joinKind as nullable number, optional keyEqualityComparers as nullable list) as table.

This joins the rows of **table1** with the rows of **table2**, based upon the equality of the values of the key columns selected by **key1** (for **table1**) and **key2** (for **table2**). The results are entered into the column named **newColumnName**. The optional **joinKind** specifies the kind of join to perform. By default, a left outer join is performed if a **joinKind** is not specified. An optional set of keyEqualityComparers may be included to specify how to compare the key columns. This feature is currently intended for internal use only.

There is another way to join tables called **Table.Join()**. The description for this function sounds very similar, with one noticeable difference.

**Table.Join(table1** as table, **key1** as any, **table2** as table, **key2** as any, optional **joinKind** as nullable number, optional **joinAlgorithm** as nullable number, optional **keyEqualityComparers** as nullable list**)** as table

This joins the rows of **table1** with the rows of **table2**, based upon the equality of the values of the key columns selected by **key1** (for **table1**) and **key2** (for **table2)**. By default, an inner join is performed. However, an optional **joinKind** may be included to specify the type of join. Options include:

*   **JoinKind.Inner**
*   **JoinKind.LeftOuter**
*   **JoinKind.RightOuter**
*   **JoinKind.FullOuter**
*   **JoinKind.LeftAnti**
*   **JoinKind.RightAnti**.

An optional set of **keyEqualityComparers** may be included to specify how to compare the key columns. This feature is currently intended for internal use only.

There is no column name specified, but more importantly – what is **joinAlgorithm**? This description is not telling me anything, but there is another way to look at the function using a **#shared step**…

![](<Base64-Image-Removed>)

So that I may find the function easily, I convert the record to a table and sort on the **Name** column. I use descending order to get to **Table.Join** more quickly.

![](<Base64-Image-Removed>)

Having found it, I look more closely at **joinAlgorithm**. I will revisit all these values in another blog, but for now the one that interests me is **JoinAlgorithm.SortMerge**. The reason it interests me is because I am working with flat files and not a relational database. Both tables are therefore held in memory in order to perform the merge. If my data is already in ascending order, I can use the **SortMerge** join algorithm to merge my data without holding it all in memory first. I therefore amend the **Source** step in my merged data from:

**\= Table.NestedJoin(Charges, {“Table\_Key”}, Descriptions, {“Table\_Key”}, “Descriptions”, JoinKind.LeftOuter)**

to

**\= Table.Join(Charges, {“Table\_Key”}, Descriptions, {“Table\_Key”}, JoinKind.LeftOuter, JoinAlgorithm.SortMerge)**

![](<Base64-Image-Removed>)

That is not quite what I wanted. **Table.Join()** differs from **Table.NestedJoin()** in another way – it’s not happy if the tables concerned have the same column names. I will change the column names in **Descriptions**, so that I have the table name before each column name.

![](<Base64-Image-Removed>)

I also amend the join information, and then try again:

![](<Base64-Image-Removed>)

Now I can see why the error occurred. Unlike **Table.NestedJoin()**, **Table.Join()** expands all the columns from both tables. The join itself is much quicker, so I can just delete the columns I don’t need. This brings me to another point. When creating a merge, both tables should ideally only have the columns that are needed. This suits **Table.Join()**, as there is less chance of duplicate columns, but also **Table.NestedJoin**, since those columns will not be held in memory with the rest of the table.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-merging-matters/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-merging-matters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-merging-matters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-merging-matters/#0)

[](https://sumproduct.com/blog/power-query-more-merging-matters/#0 "close")

top