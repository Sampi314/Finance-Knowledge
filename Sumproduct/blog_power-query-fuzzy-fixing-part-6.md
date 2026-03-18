# Power Query: Fuzzy Fixing Part 6

**Source:** https://sumproduct.com/blog/power-query-fuzzy-fixing-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Fuzzy Fixing Part 6

*   January 7, 2025

Power Query: Fuzzy Fixing Part 6
================================

Power Query: Fuzzy Fixing Part 6
================================

8 January 2025

_Welcome to our Power Query blog. This week, I continue looking at the fuzzy options available in the user interface in Power Query Online._

I have had a festive break from the fuzzy matching series. The [last blog](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-5/)
 in this series was looking at Power Query Online. Prior to that, my last blog on Power Query Online had been in 2023 and some new functionality has been added since then. I used the query **Country Data** and looked at a new icon on the ‘Add Column’ tab, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e7754742177b41adff9cc4384e1bf0fa-1.jpg)

I was able to utilise the user interface to create some **M** code using the **Table.AddFuzzyClusterColumn()** function.

![](https://sumproduct.com/wp-content/uploads/2025/05/97f8433d6efcb9bfb958d3da7f05de4e-1.jpg)

This enables the user to manipulate data and view the similarity information:

![](https://sumproduct.com/wp-content/uploads/2025/05/8d3ed3150e090ab0a07751c66a4499f4-1.jpg)

This is an easier way to create the code and will hopefully be added to the desktop version of Power Query soon.

Since I found an easier way to use **Table.AddFuzzyClusterColumn()**. Next, I head to the ‘Group by’ functionality on the Transform tab to see what is available:

![](https://sumproduct.com/wp-content/uploads/2025/05/6a92b5f6f819dfbc9263aefc481ec77b-1.jpg)

The dialog has some interesting options:

![](https://sumproduct.com/wp-content/uploads/2025/05/4898617a7891129e54637470253be44a-1.jpg)

To access them, I must enable the ‘Use fuzzy grouping’ tick box, and choose to view that section:

![](https://sumproduct.com/wp-content/uploads/2025/05/2a3708ba49eb5e0abdad38a533203772-1.jpg)

These options look familiar, I encountered them in [Fuzzy Fixing Part 4](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/)
, when I looked at **Table.FuzzyGroup()**:

**Table.FuzzyGroup(table** as table**, key** as any**,  
aggregatedColumns** as list**, optional options** as nullable record**)** as  
table

This function groups the rows of **table** by fuzzily matching values in **key** (the column I would like to be grouped) for each row. For each group, a record is constructed containing the **key** along with any aggregated columns specified by **aggregatedColumns** (for each new column, we need the column name and the aggregation). This function cannot guarantee to return a fixed order of rows.

An optional set of options may be included to specify how to compare the **key** values. Options include:

*   **Culture:** allows grouping records based upon culture-specific rules. It can be any valid culture name. For example, a Culture option of “ja-JP” groups records based on the Japanese culture. The default value is **“”**, which groups based on the Invariant English culture
*   **IgnoreCase:** a logical (true / false) value that allows case-insensitive key grouping. For example, when true, “Grapes” is grouped with “grapes”. The default value is true
*   **IgnoreSpace:** a logical (true / false) value that allows combining of text parts to find groups. For example, when true, “Gra pes” is grouped with “Grapes”. The default value is true
*   **SimilarityColumnName:** a name for the column that shows the similarity between an input value and the representative value for that input. The default value is _null_, in which case a new column for similarities will not be added
*   **Threshold:** a number between 0.00 and 1.00 that specifies the similarity score at which two values will be grouped. For example, “Grapes” and “Graes” (missing the “p”) are grouped together only if this option is set to less than 0.90. A threshold of 1.00 only allows exact matches. (Note that a fuzzy “exact match” might ignore differences like casing, word order and punctuation.) The default value is 0.80.
*   **TransformationTable:** a table that allows grouping records based upon custom value mappings. It should contain “From” and “To” columns. For example, “Grapes” is grouped with “Raisins” if a transformation table is provided with the “From” column containing “Grapes” and the “To” column containing “Raisins”. Note that the transformation will be applied to all occurrences of the text in the transformation table. With the above transformation table, “Grapes are sweet” will also be grouped with “Raisins are sweet”.

In this case, since I have all the options available to me via the user interface, it is easier to use. It will also give me some help. I try grouping my countries into regions and count the countries in each region. Although I have opted to ‘Show similarity scores’, I receive some information:

![](<Base64-Image-Removed>)

Choosing to ‘Learn more’ would take me to the Microsoft help pages for fuzzy matching, where there is nothing specific alluding to this message.

When we entered the **M** code directly in [Fuzzy Fixing Part 4](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-4/)
, we did not get the similarity column either. If I click OK, I see the data, but no similarity information:

![](<Base64-Image-Removed>)

The **M** code does include the **SimilarityColumnName** parameter, but it clearly is not shown.

Logically speaking, if we are grouping based upon a similarity score, it is difficult to see how that score would ever be displayed as we are now showing the data at the grouped level. I suspect that this parameter may be redundant for grouping.

If I reduce the similarity threshold, some of the regions are treated as matching:

![](<Base64-Image-Removed>)

Since I am able to use the cog next to the step, it is much easier to adjust the parameters so that the data is grouped as I require. I look forward to the addition of this functionaility in the user interface in desktop Power Query!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-6/#0)

[](https://sumproduct.com/blog/power-query-fuzzy-fixing-part-6/#0 "close")

top