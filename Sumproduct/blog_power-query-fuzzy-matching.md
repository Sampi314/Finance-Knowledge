# Power Query: Fuzzy Matching

**Source:** https://sumproduct.com/blog/power-query-fuzzy-matching/

---

[Home](https://sumproduct.com/)

\> Power Query: Fuzzy Matching

*   June 4, 2019

Power Query: Fuzzy Matching
===========================

Power Query: Fuzzy Matching
===========================

5 June 2019

_Welcome to our Power Query blog. Today, I am going heading off into Power BI for a feature I’d like to see more of in Excel Power Query._

Power Query is becoming more “fuzzy” – and that’s a good thing. When joining queries together, it’s not always helpful to require exact matches. Take the next table – this is the same data I looked at in [Power Query: Exceptional Cases](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-exceptional-cases)
 – and again, my problem is the way that my imaginary salespeople have entered the company names.

Here’s a Power BI Desktop screenshot:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-417.jpg)

The company names should look like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-431.jpg)

In my previous article, I cleaned up the contact table by using a translation table, but this time I am going to look at **fuzzy matching**. The translation table concept is not entirely redundant though, and I will come back to this later.

I dealt with merging tables in [Power Query: Two (Queries) Become One](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-two-queries-become-one)
. In Power Query (in Excel), the Merge dialog looks like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-406.jpg)

This type of merging won’t help me: it hasn’t linked any of the companies my salespeople have entered. However, in Power BI, the Merge dialog looks a little different:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-375.jpg)

I have fuzzy merge options! I will go through the other options later – first I just want to try it out.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-320.jpg)

I start with the default options, _i.e._ that ignores case and also ticks another box called ‘Match by combining text parts’. The information icon next to this option tells me it does things like combining ‘Micro soft’ into ‘Microsoft’ – so it’s basically ignoring spaces when comparing text. I am not setting the ‘Similarity threshold’, but it defaults to 0.80. More on this later. For now, I can see that two of my rows now have a match, so I will accept the defaults and see what has matched.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-284.jpg)

If I expand **_Company.1_**, I can see the company names that have matched:

![](<Base64-Image-Removed>)

The company names that have different cases and spaces have now matched. Next, I need to see whether I can adjust the ‘Similarity threshold’ to match my other company names.

![](<Base64-Image-Removed>)

The similarity threshold is 0.00 to match everything, and 1.00 to only allow exact matches. The default is 0.80, and this hasn’t matched two of my rows. I will try reducing it.

![](<Base64-Image-Removed>)

I try 0.5, and all of my rows are matched. I can click OK to check

![](<Base64-Image-Removed>)

With a Similarity threshold of 0.5, ‘Tentworld (mr. tent)’ is matched with ‘Tentworld (Mrs. Tent)’ and ‘Tentsrthem (DAVE)’ matches ‘Tentsrthem’.

I can play around with the threshold further:

![](<Base64-Image-Removed>)

I find that a value of 0.55 means that three of my rows match.

![](<Base64-Image-Removed>)

A threshold of 0.55 is enough to match ‘Tentworld (mr. tent)’ with ‘Tentworld (Mrs. Tent)’ but not ‘Tentsrthem (DAVE)’ with ‘Tentsrthem’. The statistical calculations behind this are beyond the scope of this blog!

The remaining options for fuzzy matching are ‘Maximum number of matches’, which can limit the number of rows returned that match the input row (useful in one to many joins), and the ability to specify a ‘Transformation table’. I used a similar idea in [Power Query: Exceptional Cases](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-exceptional-cases)
, but in that case I needed to create a **list** of ‘from’ and ‘to’ values. In this example, I need a **table** of ‘from’ and ‘to’ values.

![](<Base64-Image-Removed>)

I am trying to link to a new table ‘More Companies’ which contains the head companies for my original company names. Even with fuzzy matching, these are difficult to match. I can set up a transformation table to link the head companies to the children.

![](<Base64-Image-Removed>)

The idea is to use some fuzzy matching so that **_Company_** of ‘Contacts’ matches **_From_**, and then using this table, translate to **_To_** so that **_Head Company_** matches.

![](<Base64-Image-Removed>)

I have played around with the threshold to get the matches, but I now have all contacts matching a **_Head Company_**.

![](<Base64-Image-Removed>)

When I expand, I can see that the **_Head Company_** appears for each row.

Although the fuzzy merge is not yet an option for the Merge dialog when using Power Query in Excel, there is a way to use it there too, which I will look at next time…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fuzzy-matching/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fuzzy-matching/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fuzzy-matching/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fuzzy-matching/#0)

[](https://sumproduct.com/blog/power-query-fuzzy-matching/#0 "close")

top