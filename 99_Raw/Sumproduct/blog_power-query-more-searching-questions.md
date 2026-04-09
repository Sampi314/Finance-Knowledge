# Power Query: More Searching Questions

**Source:** https://sumproduct.com/blog/power-query-more-searching-questions/

---

[Home](https://sumproduct.com/)

\> Power Query: More Searching Questions

*   November 10, 2020

Power Query: More Searching Questions
=====================================

Power Query: More Searching Questions
=====================================

11 November 2020

_Welcome to our Power Query blog. This week, I answer some (even) more searching questions._

I have some tent data and some search strings, [as before](https://sumproduct.com/blog/power-query-searching-questions/)
…

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-109-1.jpg)

Last time, I extracted my data to Power Query and ran a function to check for the list values in the tent data.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-100-1.jpg)

The **M** code I used was:

**\= Table.AddColumn(Source, “Matched”,**

       **(CheckStrings) =>**

    **List.AnyTrue(List.Transform(SearchStrings, each Text.Contains((CheckStrings\[Included\]),\_ ))))**

The results obtained were:

![](https://sumproduct.com/wp-content/uploads/2025/05/e983a7b17fc1ef61166f94c0a09170d4-4.jpg)

The word ‘bar’ does appear in the ‘Party’ package, but it’s not the right case. I will look how to tweak my query to do this. I will also look at how to make exact matches, which means that “awning” and “awnings” would not be recognised as a match.

As I hinted last week, the first solution lies with the third parameter of **Text.Contains()**.

**Text.Contains(text** as nullable text, **substring** as text, optional **comparer** as nullable function**)** as nullable logical

A list of **comparer** functions is available at: [https://docs.microsoft.com/en-us/powerquery-m/comparer-functions](https://docs.microsoft.com/en-us/powerquery-m/comparer-functions)

The **comparer** I am going to use here is **Comparer.OrdinalIgnoreCase**.

![](<Base64-Image-Removed>)

When I enter this change, I can see that ‘bar’ and ‘BAR’ now match:

![](<Base64-Image-Removed>)

Finally, I want to make a distinction between “awning” and “awnings”, so that ‘Wedding’ package would no longer match the search string ‘awning’ on my list.

I will use a different list function, namely **List.ContainsAny()**.

**List.ContainsAny(list** as list, **values** as list, optional **equationCriteria** as any**)** as logical

Since I am comparing two lists, I need to change the rest of my function.

![](<Base64-Image-Removed>)

When I enter this, I can see that ‘Wedding’ no longer matches:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.AddColumn(Source, “Matched”,**

       **each List.ContainsAny(Text.Split(\[Included\], ” “),SearchStrings))**

Since I am comparing two lists, I have to split the **Included** column into separate words and compared that list of words with my **SearchStrings** list. Note that this no longer ignores case, and so ‘Party’ package no longer matches either. I can fix this by using the optional third parameter in **List.ContainsAny**:

**List.ContainsAny(list** as list, **values** as list, optional **equationCriteria** as any**)** as logical

The **equationCriteria** in this case will use a **comparer**.

![](<Base64-Image-Removed>)

Note that before this would work, I needed to remove the commas and full stops using ‘Replace Values’ on the Transform tab, since the exact match was rejecting words followed by a comma or full stop.

The **M** code I have used is:

**Table.AddColumn(Replaced, “Matched”,**

       **each List.ContainsAny(Text.Split(\[Included\], ” “),SearchStrings, (x,y)=> Comparer.Equals(Comparer.OrdinalIgnoreCase,x,y)))**

This adds a condition to ignore case differences between **x** (the split text list) and **y** (the **SearchStrings** list). The case is now ignored for the ‘Party’ package.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-searching-questions/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-searching-questions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-searching-questions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-searching-questions/#0)

[](https://sumproduct.com/blog/power-query-more-searching-questions/#0 "close")

top