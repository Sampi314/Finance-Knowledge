# Power Query: Fuzzy Fixing Part 3

**Source:** https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Fuzzy Fixing Part 3

*   December 3, 2024

Power Query: Fuzzy Fixing Part 3
================================

Power Query: Fuzzy Fixing Part 3
================================

4 December 2024

_Welcome to our Power Query blog. This week, I look at a larger data set with more variants that need to the fixed._

This week, I have a larger data set of 401 rows, which contain a variety of misspelt country names:

![](https://sumproduct.com/wp-content/uploads/2025/05/8b85b1fe25d22dfce461b5d8fd1bd48e-1.jpg)

As I did for my simple data set, I begin by inserting a Table, using the shortcut **CTRL** + **T**. I call the Table **Transactions**.

![](https://sumproduct.com/wp-content/uploads/2025/05/3e9d6f5fcbba1609ad53f612734021d6-1.jpg)

I right-click and choose the ‘Get Data From Table/Range…’ option to create the **Transactions** query:

![](https://sumproduct.com/wp-content/uploads/2025/05/adc2aef86dd9f1559c6cf1fb1a5efd8b-1.jpg)

I use **M** function **Table.AddFuzzyClusterColumn()** in its default form to create a new column, as I did in [Part 1](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-1/)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/209ca294667a87036efb9f78e4945526-1.jpg)

I can see that many of the rows have been fixed. As I did [last week](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-2/)
, I opt to create a column to indicate the similarity, by specifying the name of the option **SimilarityColumnName.**

![](https://sumproduct.com/wp-content/uploads/2025/05/f996cebc4ec51a5efb7288c543c9907b-1.jpg)

The similarity value varies with this data. I would like to change the threshold to see what happens to the data.

As a reminder, the syntax is:

**Table.AddFuzzyClusterColumn(table  
as table, columnname as text, newcolumnname as text, optional options as  
nullable record) as table**

The **options** I may use are extensive, and include:

*   **Culture:** allows grouping records based upon culture-specific rules. It can be any valid culture name. For example, a Culture option of “ja-JP” groups records based on the Japanese culture. The default value is **“”**, which groups based on the Invariant English Culture
*   **IgnoreCase:** a logical (true / false) value that allows case-insensitive key grouping. For example, when true, “Grapes” is grouped with “grapes”. The default value is true
*   **IgnoreSpace:** a logical (true / false) value that allows combining of text parts to find groups. For example, when true, “Gra pes” is grouped with “Grapes”. The default value is true
*   **SimilarityColumnName:** a name for the column that shows the similarity between an input value and the representative value for that input. The default value is _null_, in which case a new column for similarities will not be added
*   **Threshold:** a number between 0.00 and 1.00 that specifies the similarity score at which two values will be grouped. For example, “Grapes” and “Graes” (missing the “p”) are grouped together only if this option is set to less than 0.90. A threshold of 1.00 only allows exact matches. (Note that a fuzzy “exact match” might ignore differences like casing, word order and punctuation.) The default value is 0.80
*   **TransformationTable:** a table that allows grouping records based upon custom value mappings. It should contain “From” and “To” columns. For example, “Grapes” is grouped with “Raisins” if a transformation table is provided with the “From” column containing “Grapes” and the “To” column containing “Raisins”. Note that the transformation will be applied to all occurrences of the text in the transformation table. With the above transformation table, “Grapes are sweet” will also be grouped with “Raisins are sweet”.

Last time, I used the **TransformationTable** option. This time, I want to look at the **Threshold**. The default value is 0.80, therefore if I were to raise it to 0.90, some of my data will not be fixed. I change the step from:

**\= Table.AddFuzzyClusterColumn(#”Changed Type”, “Country”, “FuzzyCountry”, \[SimilarityColumnName = “Similarity”\])**

to:

**\=  
Table.AddFuzzyClusterColumn(#”Changed Type”, “Country”,  
“FuzzyCountry”, \[SimilarityColumnName = “Similarity”****, Threshold  \
\= 0.90****\])**

![](<Base64-Image-Removed>)

The values ‘UKK’ and ‘Italia’ are no longer fixed, as the similarity was 0.88:

![](<Base64-Image-Removed>)

Next, I try reducing the **Threshold** to 0.20:

![](<Base64-Image-Removed>)

This now replaces ‘Mex’ with ‘Mexico’. However, when I set the **Threshold** to 0.50 it doesn’t; take care when using the **Threshold!**

![](<Base64-Image-Removed>)

Even when I reduced the **Threshold** to zero \[0\], ‘UKingdom’ was not recognised as ‘UK’, however, when I added a space to the source it was matched:

![](<Base64-Image-Removed>)

The settings for Threshold are not as predictable as I’d like, but it has potential!

Next time, I’ll look at the **M** function **Table.FuzzyGroup()**.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/#0)

[](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-3/#0 "close")

top