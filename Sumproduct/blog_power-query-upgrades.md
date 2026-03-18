# Power Query: Upgrades

**Source:** https://sumproduct.com/blog/power-query-upgrades/

---

[Home](https://sumproduct.com/)

\> Power Query: Upgrades

*   August 21, 2018

Power Query: Upgrades
=====================

Power Query: Upgrades
=====================

22 August 2018

_Welcome to our Power Query blog. This week, I take a final look at an example where I need to translate numbers to letters in multiple columns, this time using the M function List.ReplaceMatchingItems() and matching those items using values from another table._

(Again) I have the exam results for some children who were lucky(!) enough to take their exams when the system was in the middle of changing from letters to numbers. It’s confusing, not least because 9 is the new top grade, whereas intuitively I might expect 1 to be the highest. I want to replace the numbers with letters so that I can see everything in the same format. I’ve completed the task in the last two blogs, in [Power Query: Upgrading Grades](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-upgrading-grades)
 I did this by using **List.ReplaceMatchingItems()**, and last time out, in [Power Query: Joining Grades](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-joining-grades)
 I merged my table of results with a table of numeric to letter equivalents. This time, I’m using a combined approach which is designed to be more robust.

![](<Base64-Image-Removed>)

Since the last blog, Liam has been awarded 10 in all the numeric grades _(but of course – shame it’s out of 100)_! This will have an impact on how I create the list of numeric grades, as I’ll show later.

I begin by creating a query ‘From Table’ in the ‘Get & Transform’ section of the ‘Data” tab.

![](<Base64-Image-Removed>)

I want to translate all the values at the same time in all numeric columns, creating new columns. One way to do this is to use **List() M** functionality. I begin by merging the columns I need to translate, namely **_English Language_**, **_English Literature_** and **_Mathematics._** This would work equally well if I were to merge all my columns and if I had less stable data, _i.e._ other subjects were soon to move to numeric grades, then this approach would be better. There are also ways to allow for a variable number of columns, but I will save this for another time.

![](<Base64-Image-Removed>)

I decide to use a comma delimiter to help me convert my data back later.

![](<Base64-Image-Removed>)

Now this is where I used **Text.ToList** to convert my column to lists in [Power Query: Upgrading Grades](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-upgrading-grades)
. However, as I’ll show below, there is a problem with this.

![](<Base64-Image-Removed>)

This gives me a column of lists that I can manipulate.

![](<Base64-Image-Removed>)

However, if I look at how the list is constructed:

![](<Base64-Image-Removed>)

I can see that each character has been given a separate list entry. If instead I look at Liam’s list of grades:

![](<Base64-Image-Removed>)

This means that any translation would replace the 1 not the 10, so it’s not what I want. There is another function that works better in these circumstances:

**Text****.Split(****string****as****text****, separator** **as****text****)** **as** **list**

This returns a list containing parts of a **string** that are delimited by a **separator** text value.

I add a new custom column:

![](<Base64-Image-Removed>)

The **M** formula I have used is

**\= Text.Split(\[Merged\],”,”)**

![](<Base64-Image-Removed>)

I have a list of each of the grades this time, so I am ready to move to the next step.

Instead of specifying what to replace in a manual list, I am going to convert my grade equivalents table into a list that I can use.

![](<Base64-Image-Removed>)

I found when I was carrying out this task it was easiest if I made sure that the columns in my Excel table were set to ‘Text’. It will help with the substation to and from a text string. Having created a query from the grade equivalents table, I need to create a column that stores each pair of rows as a list. To do this I use **Table.AddColumn()** function:

**Table.AddColumn(table** **as** **table, newColumnName** **as****text****, columnGenerator** **as****function****,** **optional** **columnType** **as** **nullable type)** **as** **table**

This adds a column named **newColumnName** to a **table**.

If I add the new column by defining a list, then I can create a column of lists.

![](<Base64-Image-Removed>)

The formula I have used is

**\= Table.AddColumn(Source, “Equivalents\_list”,  each ( { \[Number Grade\], \[Equivalent Letter Grade\] } ) )**

This creates a list of pairs of number grades and their equivalent letter grade.

I delete the other columns to only leave **_Equivalents\_list_**

![](<Base64-Image-Removed>)

I convert the remaining column to a list so that I now have a list of lists called ‘Equivalents’. I save this as ‘Connection Only’. I can now go back to my first query and use a **List()** function to transform my data. The one I am going to use is

**List****.ReplaceMatchingItems(****list****as****list****, replacements** **as** **any ,optional equationCriteria** **as** **any)** **as****list**

This replaces occurrences of existing values in the **list** with new values using the provided **equationCriteria**. Old and new values are provided by the replacements parameters.

![](<Base64-Image-Removed>)

The **M** functionality I have used is

**\= List.ReplaceMatchingItems(\[List\_of\_Grades\], Equivalents)**

This replaces any entries in my merged column that are in the first item in the list in ‘Equivalents’ with the second item in the list. So any numerical grades should be translated to the corresponding letter grade.

![](<Base64-Image-Removed>)

Judging by the new list of Liam’s grades, it’s looking promising!

Now I will extract my list:

![](<Base64-Image-Removed>)

I choose to use a comma delimiter here, as **Text.Split** has not included the comma delimiter I used earlier.

![](<Base64-Image-Removed>)

On the ‘Transform’ tab, I can choose to split my column.

![](<Base64-Image-Removed>)

I click ‘OK’ to create three new columns

![](<Base64-Image-Removed>)

I can now remove the other list and the temporary column I used to merge the grades. I also rename my new columns.

![](<Base64-Image-Removed>)

I can now see what the letter grade is for English and Maths.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-upgrades/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-upgrades/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-upgrades/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-upgrades/#0)

[](https://sumproduct.com/blog/power-query-upgrades/#0 "close")

top