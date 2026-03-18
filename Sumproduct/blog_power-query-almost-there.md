# Power Query: Almost There

**Source:** https://sumproduct.com/blog/power-query-almost-there/

---

[Home](https://sumproduct.com/)

\> Power Query: Almost There

*   September 29, 2020

Power Query: Almost There
=========================

Power Query: Almost There
=========================

30 September 2020

_Welcome to our Power Query blog. We turn 200!! To celebrate, I do nothing other than write another article! This week, I look at how to add a fuzzy column._

This week, I am taking a trip to Power BI. This blog comes with a warning! I wanted to look at how a fuzzy column can be added to a table to help streamline data. I initially tried this with Microsoft Office Professional Plus 2016 in Excel 2016, but it seems that the fuzzy technology is not quite in place. I tried to add the step I wanted:

![](<Base64-Image-Removed>)

But this is not quite the result I wanted…

![](<Base64-Image-Removed>)

So, be warned, this may not be set up in all versions of Excel – yet. Meanwhile, back in Power BI, I have some contact data:

![](<Base64-Image-Removed>)

My salespeople all have their own way of recording the supplier name, but I want to link all these to the correct supplier. I can add a column to do this. There is an **M** function called **Table.AddFuzzyCluster()** to assist me:

**Table.AddFuzzyClusterColumn(table** as table, **columnName** as text, **newColumnName** as text, optional **options** as nullable record**)** as table

This function adds a new column, **newColumnName**, to **table** with representative values of **columnName**. The representatives are obtained by fuzzily matching values in **columnName**, for each row.

An optional set of **options** may be included to specify how to compare the key columns. The **options** include:

*   **Culture:** this allows grouping records based on culture-specific rules. It can be any valid culture name. For example, a Culture option of “ja-JP” groups records based upon the Japanese culture. The default value is “”, which groups based on the Invariant English culture (whatever that is!)
*   **IgnoreCase:** this is a logical (true/false) value that allows case-insensitive key grouping. For example, when true, “Grapes” is grouped with “grapes”. The default value is true
*   **IgnoreSpace:** this is a logical (true/false) value that allows combining of text parts in order to find groups. For example, when true, “Gra pes” is grouped with “Grapes”. The default value is true
*   **Threshold:** this is a number between 0.00 and 1.00 that specifies the similarity score at which two values will be grouped. For example, “Grapes” and “Graes” (missing “p”) are grouped together only if this option is set to less than 0.90. A threshold of 1.00 is the same as specifying an exact match criterion while grouping. The default value is 0.80
*   **TransformationTable:** this is a table that allows grouping records based upon custom value mappings. It should contain “From” and “To” columns. For example, “Grapes” is grouped with “Raisins” if a transformation table is provided with the “From” column containing “Grapes” and the “To” column containing “Raisins”. Note that the transformation will be applied to all occurrences of the text in the transformation table. With the above transformation table, “Grapes are sweet” will also be grouped with “Raisins are sweet”
*   **SimilarityColumnName:** this is a name for the column that shows the similarity between an input value and the representative value for that input. The default value is _null_, in which case a new column for similarities will not be added.

I will look at some of the parameters later. For now, I will create a column that cleans up my supplier name, and to do this I will specify my table, the column name I am basing this column on, and the new column name.

**\= Table.AddFuzzyClusterColumn(#”Changed Type”,”Supplier”,”Real Supplier”)**

![](<Base64-Image-Removed>)

This has created a new column, **Real Supplier**, which contains a cleaned up and more accurate version of the supplier name.

The majority of the parameters which can be used with **Table.AddFuzzyClusterColumn()** are very similar to the parameters for fuzzy merge options in [Power Query: Fuzzy Matching](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-fuzzy-matching)
_._

I am going to amend my step to not try to match if the letters are in a different case. This affects letters of a different case within the text, rather than at the beginning of words.

**\= Table.AddFuzzyClusterColumn(#”Changed Type”,”Supplier”,”Real Supplier”, \[IgnoreCase = false\])**

![](<Base64-Image-Removed>)

This time, the matching for ‘Awnings R Us’ hasn’t matched to ‘Awningsrus’ (although ‘Awnings rus’ has matched to ‘Awningsrus’ because the spaces are ignored).

Fuzzy matching is still developing, and can vary between the platforms. Online Excel has a button to create a cluster values column in the ‘Add Column’ tab, for instance. Hopefully, the functionality will be consistent across Excel and Power BI soon.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-almost-there/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-almost-there/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-almost-there/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-almost-there/#0)

[](https://sumproduct.com/blog/power-query-almost-there/#0 "close")

top