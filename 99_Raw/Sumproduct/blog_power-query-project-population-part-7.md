# Power Query: Project Population – Part 7

**Source:** https://sumproduct.com/blog/power-query-project-population-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 7

*   June 6, 2023

Power Query: Project Population – Part 7
========================================

Power Query: Project Population – Part 7
========================================

7 June 2023

_Welcome to our Power Query blog. This week, I continue to prepare my second query from a public data source._

I have found some information on population growth provided by The World Bank, which I am using as an example of how to transform real-life data.

![](<Base64-Image-Removed>)

I have been transforming the data, and [last time](https://sumproduct.com/blog/power-query-project-population-part-6/)
, I started to transform the **Country-Series** query. This query gives me information about the source of the population data in the **Country** query, and I want to have a single description of the source for each country. I have removed any duplicate entries:

![](<Base64-Image-Removed>)

However, there are still multiple descriptions for some countries. Last time, I decided to use a trick to combine the text. I used ‘Group By’ which is available on the Home tab, and here, on the Transform tab:

![](<Base64-Image-Removed>)

I wanted to ‘Group By’ **CountryCode**, and concatenate the **DESCRIPTION** rows. However, since I had both columns selected, the dialog was in ‘Advanced’ mode, and prompting me to ‘Group By’ **CountryCode** and **DESCRIPTION**. I will sort this out later.

I created a new column, **Description**, where I summed the **DESCRIPTION** rows:

![](<Base64-Image-Removed>)

Unsurprisingly, Power Query was not happy about summing a text value:

![](<Base64-Image-Removed>)

Let’s start by having a look at the **M** code that has been generated:

**\= Table.Group(#”Removed Duplicates”,  
{“CountryCode”, “DESCRIPTION”},  
{{“Description.1”, each List.Sum(\[DESCRIPTION\]), type nullable  
text}})**

The part of this code that is trying to ‘sum’ the text is:

**List.Sum(\[DESCRIPTION\])**

I need to replace this with a way of concatenating the text instead.

We can see how Power Query would do this by combining two \[2\] columns of text on the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

This generates a step:

![](<Base64-Image-Removed>)

If I look at the **M** code for this step, I see the function I need to use:

**\= Table.AddColumn(#”Grouped Rows”, “Merged”,  
each Text.Combine({\[CountryCode\], \[DESCRIPTION\]}, “”), type text)**

The section of the code that combines the text is:

**Text.Combine({\[CountryCode\],  
\[DESCRIPTION\]}, “”)**

This means that I need to use the function **Text.Combine()** instead of **List.Sum()** in the ‘Grouped Rows’ step. I can also delete the ‘Inserted Merged Column’ step. I change the Grouped Rows’ step to:

**\= Table.Group(#”Removed Duplicates”,  
{“CountryCode”, “DESCRIPTION”},  
{{“Description.1”, each Text.Combine(\[DESCRIPTION\]), type nullable  
text}})**

This gives me the desired result:

![](<Base64-Image-Removed>)

Now I have shown that the substitution works, I can amend the step to remove the **DESCRIPTION** column and rename **Description.1** to **Description**:

![](<Base64-Image-Removed>)

This doesn’t quite look right; I need a delimiter. If I look at the **Text.Combine() M** code generated when I created the merged column:

**Text.Combine({\[CountryCode\],  
\[DESCRIPTION\]}, “”)**

I can see that I can pass another parameter to this function to define the delimiter. I change ‘Grouped Rows’ step from

**\= Table.Group(#”Removed Duplicates”, {“CountryCode”},  
{{“Description”, each Text.Combine(\[DESCRIPTION\]), type nullable  
text}})**

to

**\= Table.Group(#”Removed Duplicates”,  
{“CountryCode”}, {{“Description”, each  
Text.Combine(\[DESCRIPTION\],”, “), type nullable text}})**

This will put a comma and a space ( **,** ) between my data sources.

![](<Base64-Image-Removed>)

The content of **Description** is too long. I change the name of the column created in the ‘Grouped Rows’ step to **Data Sources** and I replace the phrase ‘Data source:’ with an empty space by right-clicking on **Data Sources** and choosing ‘Replace Values’.

![](<Base64-Image-Removed>)

Now I am happy with the **Country-Series** query. Next time, I will link to this information from the **Country** query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-7/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-7/#0 "close")

top