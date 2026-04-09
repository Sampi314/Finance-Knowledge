# Power Query: Searching Questions

**Source:** https://sumproduct.com/blog/power-query-searching-questions/

---

[Home](https://sumproduct.com/)

\> Power Query: Searching Questions

*   November 3, 2020

Power Query: Searching Questions
================================

Power Query: Searching Questions
================================

4 November 2020

_Welcome to our Power Query blog. This week, I answer some searching questions._

I have some tent data and some search strings…

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-113-1.jpg)

I begin by extracting my tent data to Power Query, using the ‘From Table’ option on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-104-1.jpg)

I call my query ‘TentData’. I go back to my spreadsheet and create a query for my search strings.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-96-1.jpg)

I call my query ‘SearchStrings’ and choose ‘Convert to List’ from the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-86-1.jpg)

I am now ready to use my list to search the tent data. I go back to my tent data query. I am going to enter a new step.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-75-1.jpg)

The **M** code I have entered is:

**\= Table.AddColumn(Source, “Matched”,**

       **(CheckStrings) =>**

    **List.AnyTrue(List.Transform(SearchStrings, each Text.Contains((CheckStrings\[Included\]),\_ ))))**

In order to understand this step, it needs to be broken down. The start is simple enough; I am adding a new column to my table called **Matched****.** The **M** function I am using for this is **Table.AddColumn()**:

**Table.AddColumn(table** as table, **newColumnName** as text, **columnGenerator** as function, optional **columnType** as nullable type**)** as table.

I am specifying the **columnGenerator** to provide the function to populate my new column. At the other end, I am using **Text.Contains()** to check each line of my list **SearchStrings** against the **Included** column in my tent data.

**Text.Contains(text** as nullable text, **substring** as text, optional **comparer** as nullable function**)** as nullable logical

Today, I am not using the optional **comparer**, but I will look at this next week.

To indicate that each entry on **SearchStrings** is to be used, I use underscore (‘**\_**‘). **Text.Contains()** is either TRUE or FALSE, so I then create a list of TRUE’s and FALSE’s by using **List.Transform()**.

**List.Transform(list** as list, **transform** as function**)** as list

This returns a new list of values by applying the transform function **transform** to the list.

Finally, I check if any TRUE’s are found using **List.AnyTrue()**.

**List.AnyTrue(list** as list**)** as logical

This returns true if any expression in the list is true.

If there are, the new column is populated with ‘TRUE’. The results I get are,

![](<Base64-Image-Removed>)

which, if I look at my search list, is correct:

![](<Base64-Image-Removed>)

The word ‘awning’ appears in the ‘Wedding’ package, so that is TRUE. The word ‘toy’ appears in the ‘Childrens’ package, so that is TRUE. Since I haven’t indicated that case should be ignored, the word ‘bar’ does appear in the ‘Party’ package, but it’s not the right case so that is FALSE. I will look how to tweak my query to ignore case next time. I will also look at how to make exact matches, which means that ‘awning’ and ‘awnings’ would not be picked up as a match.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-searching-questions/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-searching-questions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-searching-questions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-searching-questions/#0)

[](https://sumproduct.com/blog/power-query-searching-questions/#0 "close")

top