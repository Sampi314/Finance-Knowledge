# Power Query: Fuzzy Fixing Part 4

**Source:** https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Fuzzy Fixing Part 4

*   December 10, 2024

Power Query: Fuzzy Fixing Part 4
================================

Power Query: Fuzzy Fixing Part 4
================================

11 December 2024

_Welcome to our Power Query blog. This week, I look at_ _the **M** function **Table.FuzzyGroup()**._

This week, I am going to look at grouping similar data. I have a data set containing names and amounts, where the names may be grouped. In the image below, I would like ‘Jon’ and ‘Johnny’ to be grouped together, for example. There are 40 rows in total, yet only 10 unique names.

![](https://sumproduct.com/wp-content/uploads/2025/05/90f96d08ba59522fc2b049db127f18de-1.jpg)

I have already inserted a Table, using the shortcut **CTRL**\+ **T**, and I have called the Table **TransactionGroups**. I extract the Table to Power Query, by right-clicking and choosing to ‘Get Data from Table/Range…’.

![](https://sumproduct.com/wp-content/uploads/2025/05/5989ea24c426bca82abfe594d274fd08-1.jpg)

To group my data, I am going to use **M** function **Table.FuzzyGroup()**.

**Table.FuzzyGroup(table as table, key as any, aggregatedColumns as  
list, optional options as nullable record) as table**

This function groups the rows of **table** by fuzzily matching values in **key** (the column I would like to be grouped), for each row. For each group, a record is constructed containing the **key** along with any aggregated columns specified by **aggregatedColumns** (for each new column, we need the column name and the aggregation). This function cannot guarantee to return a fixed order of rows.

An optional set of options may be included to specify how to compare the **key** values. Options include:

*   **Culture:** allows grouping records based upon culture-specific rules. It can be any valid culture name. For example, a Culture option of “ja-JP” groups records based on the Japanese culture. The default value is **“”**, which groups based on the Invariant English culture
*   **IgnoreCase:** a logical (true / false) value that allows case-insensitive key grouping. For example, when true, “Grapes” is grouped with “grapes”. The default value is true
*   **IgnoreSpace:** a logical (true / false) value that allows combining of text parts to find groups. For example, when true, “Gra pes” is grouped with “Grapes”. The default value is true
*   **SimilarityColumnName:** a name for the column that shows the similarity between an input value and the representative value for that input. The default value is _null_, in which case a new column for similarities will not be added
*   **Threshold:** a number between 0.00 and 1.00 that specifies the similarity score at which two values will be grouped. For example, “Grapes” and “Graes” (missing the “p”) are grouped together only if this option is set to less than 0.90. A threshold of 1.00 only allows exact matches. (Note that a fuzzy “exact match” might ignore differences like casing, word order and punctuation.) The default value is 0.80
*   **TransformationTable:** a table that allows grouping records based upon custom value mappings. It should contain “From” and “To” columns. For example, “Grapes” is grouped with “Raisins” if a transformation table is provided with the “From” column containing “Grapes” and the “To” column containing “Raisins”. Note that the transformation will be applied to all occurrences of the text in the transformation table. With the above transformation table, “Grapes are sweet” will also be grouped with “Raisins are sweet”.

These options are familiar from [last week](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/)
, and I will be taking the default values for all except the **SimilarityColumnName**, which I will call ‘**Similarity**‘. I create a new step and enter the **M** code:

**\=  
Table.FuzzyGroup(#”Changed Type”, “Name”, {“Amount”,each  
List.Sum(\[Amount\])}, \[SimilarityColumnName = “Similarity”\])**

![](https://sumproduct.com/wp-content/uploads/2025/05/2a04b0ae84ef5e934128c4b6d5699ce7-1.jpg)

I’m disappointed to see that there is no column to indicate similarity, but almost all of my data has been grouped, although the name used for the grouping seems to be random. I’d like to see the names that have been grouped. I may use the same method I described in the blog [Group Text](https://sumproduct.com/blog/power-query-group-text/)
. The **M** code I need is:

**\=  
Table.FuzzyGroup(#”Changed Type”, “Name”,  
{{“Amount”,each List.Sum(\[Amount\])},{“Names”, each  
Text.Combine(\[Name\], “, “)}})**

![](<Base64-Image-Removed>)

I think it’s safe to say that this method is not going to be useful for combining sales data reliably! I would need to use a **TransformationTable** as I did in [Part 2](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-2/)
.

It is possible to access the fuzzy features I have been looking at from the user interface (UI), but not yet in desktop Power Query. To find that, I need to head to Power Query Online, which is where I will continue next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/#0)

[](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/#0 "close")

top