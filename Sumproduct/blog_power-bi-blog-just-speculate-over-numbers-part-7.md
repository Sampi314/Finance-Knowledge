# Power BI Blog: Just Speculate Over Numbers – Part 7

**Source:** https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-7/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Just Speculate Over Numbers – Part 7

*   June 13, 2018

Power BI Blog: Just Speculate Over Numbers – Part 7
===================================================

Power BI Blog: Just Speculate Over Numbers – Part 7
===================================================

14 June 2018

Last week we went ascertained which numbers were drawn most frequently.

In Powerball we know that the first five numbers are the regular balls and the sixth ball is the Powerball.

But how would we find out which _combinations of regular numbers_ were drawn most frequently? That’s less straight forward if our numbers weren’t already sorted. How does that stack up against the combination with the Powerball?

If we had data that only had numbers drawn out in each position – what we would need to do, is sort all the numbers drawn regardless of position and use that combination to do our frequency test on.

The procedure would be:

· Retrieve the first five numbers by date

· Sort the numbers

· Create a combination for the sorted numbers with and without the Powerball.

So how would we do this in Power BI?

This is where we would return to the Query Editor. Because we already have a visualisation that is dependent on our **Powerball Numbers** set – I’m going to _Reference_ the query and rename it to **Powerball Combinations**.

![](<Base64-Image-Removed>)

We know that if the **Attribute** is “Winning Numbers.6”, it is the Powerball, otherwise a regular number. Let’s add a conditional column to do that. This can be found in the Ribbon under the Add Column tab in the General subcategory.

![](<Base64-Image-Removed>)

From the dialogue that pops up, we can put our conditions. Create a column called “Ball Type” as follows:

![](<Base64-Image-Removed>)

The table should look like this:

![](<Base64-Image-Removed>)

Now I’m going to [Pivot](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-pivotal-pivoting)
 the Ball type column so all the Regular numbers are in one column and the Powerball number is in another.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Now, this is where it gets interesting. In order to get all the Regular numbers sorted into a list, I’m going to do a little trick. What I want to do, is [group](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-group-and-conquer)
 all the rows by date and Powerball and retrieve the regular numbers. But before I can do that, I’ll need to fill the **Powerball** column with all the numbers by date so it doesn’t group by the _null_ value.

Luckily, the Power Query Editor has a nifty tool called _Fill_. This is found in the Ribbon under the Transform tab in the Any Column subcategory.

![](<Base64-Image-Removed>)

What this will do is fill any null values in a column with a number nearby in the direction required:

![](<Base64-Image-Removed>)

Great! It’s time to group our data:

![](<Base64-Image-Removed>)

The operation _All Rows_ is a special one. What this does is return a copy of the table where the criteria of the table is filtered by the matching grouped by columns i.e. It will return all the rows where the **Draw Date** and **Powerball** are the same.

![](<Base64-Image-Removed>)

Great! Now all we want to do is get the **Regular** column.

This where we get a little tricky. We know that type of information in **Data** is a Table. We can use Power Query’s structured referencing to get just the column.

Add a column called **Combination** as such:

![](<Base64-Image-Removed>)

It has given us a _List_ data. Which is the column we’ve requested, the values in the **Regular** column.

What we can do now is sort this list by using the function **List.Sort** (read up more about it at the Microsoft Reference library [here](https://msdn.microsoft.com/en-us/query-bi/m/list-sort)
). Let’s go back an edit our column entry by clicking on the gear icon next to our created step.

![](<Base64-Image-Removed>)

It will now preview like this:

![](<Base64-Image-Removed>)

Press the expansion arrow but put a delimiter like a space in between the numbers and let’s see what we get!

![](<Base64-Image-Removed>)

I’m going to a couple of things – try and see if you can do it yourself:

*   Drop the **Data** column
*   Add a column called **Combination + Powerball** where it will be defined as

\= \[Combination\] & ” ” & Text.From(\[Powerball\]))

The **[Text.From](https://msdn.microsoft.com/en-us/query-bi/m/text-from)
** function is used here because **Powerball** is a column of numbers, and Power Query will not perform on concatenation on non-text datatypes.

![](<Base64-Image-Removed>)

Time to “Close & Apply!”

Next time we’ll go back to the report and put it on our dashboard.

Tune back next week for more Power BI tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-7/#0)

[](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-7/#0 "close")

top