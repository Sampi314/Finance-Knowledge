# Power Query: Are Any of Them on the Table?

**Source:** https://sumproduct.com/blog/power-query-are-any-of-them-on-the-table/

---

[Home](https://sumproduct.com/)

\> Power Query: Are Any of Them on the Table?

*   June 25, 2019

Power Query: Are Any of Them on the Table?
==========================================

Power Query: Are Any of Them on the Table?
==========================================

26 June 2019

_Welcome to our Power Query blog. Today, I revisit the data I looked at last week to extend one of my solutions._

Last week, I checked if a company had been contacted by any of my salespeople, using **Table.ContainsAny:**

Table.ContainsAny**(table** as table, **rows** as list, optional equationCriteria as any) as logical

This determines whether any of the specified records appear as **rows** in the **table**.

I used this function to see if any of my salespeople had contacted a company.

![](<Base64-Image-Removed>)

The **M** code I used was:

**\= Table.ContainsAny(\[Contacts\], {\[Name=”John”\], \[Name=”Mary”\], \[Name= “Paul”\], \[Name=”Newbie”\]})**

When I pressed OK, I saw which companies had any contact with my employees:

![](<Base64-Image-Removed>)

This showed me that all the companies have been contacted, even if some companies had been contacted more than once. However, whilst it’s feasible to use individual names for a small group of salespeople, if I had a larger imaginary company, then I would want a way of doing this without using specific names.

![](<Base64-Image-Removed>)

There are a couple of ways I could do this for my data.

I go back to the query I created in [Power Query: Is it on the Table?](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-is-it-on-the-table)
 which checked if any of my named people had contacted each company.

![](<Base64-Image-Removed>)

One way I can approach this is to amend my **M** code check a different column. I started with the M

**\= Table.ContainsAny(Contacts, {\[Name=”John”\], \[Name=”Mary”\], \[Name= “Paul”\], \[Name=”Newbie”\]})**

I can change this to:

**\= Table.ContainsAny(Contacts, {Mail = “Yes”})**

![](<Base64-Image-Removed>)

I can see that all my companies have been contacted.

This does leave the question of the best way to see if the companies were contacted by a specified list of people, without actually listing them. If I try and use **Table.ContainsAny()**, I would need to generate a list of records, which is tricky to format. An easier way is to create a table of salespeople, and then use a ‘Salespeople’ query to link to my data and get the answer that way.

![](<Base64-Image-Removed>)

I have created a table of salespeople (and have left out Newbie) with the goal of checking if the companies have been contacted by the people in this table.

![](<Base64-Image-Removed>)

I merge my queries, taking the defaults and matching on **_Name_**.

![](<Base64-Image-Removed>)

Then, I expand my data.

![](<Base64-Image-Removed>)

I can now create a custom column which will indicate if the company has been contacted by one of my main salespeople.

![](<Base64-Image-Removed>)

I can now rename my column and remove the temporary column.

![](<Base64-Image-Removed>)

I can now see who has been contacted by my main team.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-are-any-of-them-on-the-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-are-any-of-them-on-the-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-are-any-of-them-on-the-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-are-any-of-them-on-the-table/#0)

[](https://sumproduct.com/blog/power-query-are-any-of-them-on-the-table/#0 "close")

top