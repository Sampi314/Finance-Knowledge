# Power Query: Finding Fuzzy

**Source:** https://sumproduct.com/blog/power-query-finding-fuzzy/

---

[Home](https://sumproduct.com/)

\> Power Query: Finding Fuzzy

*   June 11, 2019

Power Query: Finding Fuzzy
==========================

Power Query: Finding Fuzzy
==========================

12 June 2019

Welcome to our Power Query blog. After last week’s adventure in Power BI, I discover the fuzzy features of Excel Power Query.

Last week I looked at how the ‘Merge’ window in Power BI Power Query includes options for fuzzy matching, as the following screenshot shows:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-413.jpg)

In Excel’s Power Query, the ‘Merge’ screen does not have these options:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-427.jpg)

If this was the end of the story, this would be a very short blog! The fuzzy merge options do actually exist, but to get to them, I have to use **M**. If I type

**\=  Table.FuzzyJoin**

in the ‘Next Step’ window in the Power Query Editor, I can see that the functionality is available.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-402.jpg)

The **M** function **Table.FuzzyJoin()** is described in full, and if I scroll down, I can see what parameters are required to use this **M** function.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-372.jpg)

The description of **Table.FuzzyJoin()** in the Microsoft help pages is as follows:

Table.FuzzyJoin(**table1** as table, **key1** as any, **table2** as table, **key2** as any, optional **joinKind** as nullable number, optional **joinOptions** as nullable record) as table

This joins the rows of **table1** with the rows of **table2** based on a fuzzy matching of the values of the key columns selected by **key1** (for **table1**) and **key2** (for **table2**).

Fuzzy matching is a comparison based on similarity of text rather than equality of text.

By default, an inner join is performed, however an optional **joinKind** may be included to specify the type of join. Options include:

*   **JoinKind.Inner**
*   **JoinKind.LeftOuter**
*   **JoinKind.RightOuter**
*   **JoinKind.FullOuter**
*   **JoinKind.LeftAnti**
*   **JoinKind.RightAnti**

An optional set of **joinOptions** may be included to specify how to compare the key columns. Options include:

*   **ConcurrentRequests**
*   **Culture**
*   **IgnoreCase**
*   **IgnoreSpace**
*   **NumberOfMatches**
*   **Threshold**
*   **TransformationTable  
    **

These options are the same as the options available for fuzzy matching on the Power BI ‘Merge’ screen.

*   **ConcurrentRequests** (default is 1)  
    Values can be between 1 and 8.  
    The **ConcurrentRequests** option supports parallelizing the join operation by specifying the number of parallel threads to use.
*   **Culture** (default is neutral)  
    Values are valid culture names.  
    The **Culture** option allows matching records based on culture-specific rules.  
    For example, a **Culture** option of ‘ja-JP’ matches records based on the Japanese language.
*   **IgnoreCase** (default is true)  
    Values are true or false.  
    The **IgnoreCase** option allows matching records irrespective of the case of the text.  
    For example, ‘Grapes’ (sentence case) is matched with ‘grapes’ (lower case) if the **IgnoreCase** option is set to true.
*   **IgnoreSpace** (default is true)  
    Values are true or false.  
    The **IgnoreSpace** option allows combining text parts in order to find matches.  
    For example, ‘Micro soft’ is matched with both ‘Microsoft’ and ‘Micro soft’ if the **IgnoreSpace** option is set to true.
*   **NumberOfMatches** (default is 2,147,483,647)  
    Values are between 0 and 2,147,483,647.  
    The **NumberOfMatches** option specifies the maximum number of matching rows that can be returned.
*   **Threshold** (default is 0.80)  
    Values are between 0.00 and 1.00.  
    The similarity **Threshold** option provides the ability to match records above a given similarity score. A **Threshold** of 1.00 is the same as specifying an exact match criterion.  
    For example, ‘Grapes’ matches with ‘Graes’ (missing ‘p’) only if the **Threshold** is set to less than 0.90.
*   **TransformationTable  
    **A valid table with at least two columns named ‘From’ and ‘To’.  
    The **TransformationTable** option allows matching records based on custom value mappings. For example, ‘Grapes’ is matched with ‘Raisins’ if a **TransformationTable** is provided with the ‘From’ column containing ‘Grapes’ and the ‘To’ column containing ‘Raisins’.

There is another very similar option, **Table.FuzzyNestedJoin()** – the main difference is that if I use **Table.FuzzyNestedJoin()**, the second table that I have joined to won’t have been expanded for me. I will show an example later.

I will use **Table.FuzzyJoin()** to link ‘Contacts’ to the ‘Company’ query. A reminder of the data from the Excel worksheet is shown next:

![](<Base64-Image-Removed>)

I will start from a new blank query by choosing the ‘New Query’ option from the ‘Get & Transform’ section of the Data tab and selecting ‘Blank Query’ in the ‘From Other Sources’ option.

![](<Base64-Image-Removed>)

I have created some **M** code which uses the **Table.FuzzyJoin()** function:

**\= Table.FuzzyJoin(Contacts, “Company”, Company, “Actual\_Company”, JoinKind.LeftOuter, \[Threshold = 0.5 \])**

I have created a fuzzy join between **Contacts** and **Company** – I have used a left outer join so that the correct version of the company name will appear. The threshold I have chosen is the same one I found worked last week for my data. Other than the specified options, I have taken the defaults. One point to note, is that this function will not create a table where two columns have the same name – so I had to change the name of the column in Company to **Actual\_Company** so that I could join it to a table that already had the name **Company**.

I can also use **Table.FuzzyNestedJoin()**, if I want to keep my second table in a separate column. For some reason, in this case the join is represented by a number – I have given the join type a value of 1 which is a left outer join type.

![](<Base64-Image-Removed>)

The **M** code is

**\= Table.FuzzyNestedJoin(Contacts, “Company”, Company, “Actual\_Company”, “Actual Company”, 0, \[Threshold = 0.5 \])**

I have named the column that holds my table; this is a required parameter.

![](<Base64-Image-Removed>)

The advantage of this method is that the tables can have the same column names and it can be managed by Power Query when the table is expanded.

![](<Base64-Image-Removed>)

Once expanded, I get the same results. I can also choose to use a transformation table as one of my options, which I will set up in the Excel workbook.

![](<Base64-Image-Removed>)

I am going to use ‘**Company\_Translation**‘ to get the head company name, which will allow me to link from ‘**Contacts**‘ to ‘**More\_Companies**‘

![](<Base64-Image-Removed>)

The **M** code is

**\= Table.FuzzyNestedJoin(Contacts, “Company”, Company, “Actual\_Company”, “Actual Company”, 0, \[Threshold = 0.5 \])**

I have named the column that holds my table; this is a required parameter.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-finding-fuzzy/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-finding-fuzzy/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-finding-fuzzy/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-finding-fuzzy/#0)

[](https://sumproduct.com/blog/power-query-finding-fuzzy/#0 "close")

top