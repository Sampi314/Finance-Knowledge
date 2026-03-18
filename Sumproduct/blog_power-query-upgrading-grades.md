# Power Query: Upgrading Grades

**Source:** https://sumproduct.com/blog/power-query-upgrading-grades/

---

[Home](https://sumproduct.com/)

\> Power Query: Upgrading Grades

*   August 7, 2018

Power Query: Upgrading Grades
=============================

Power Query: Upgrading Grades
=============================

8 August 2018

_Welcome to our Power Query blog. This week, I look at an example where I need to translate numbers to letters in multiple columns using the M function List.ReplaceMatchingItems()._

I have the school examination results for some children who were lucky(!) enough to take their exams when the UK system was in the middle of changing from letters to numbers. It’s confusing, not least because 9 is the new top grade, whereas intuitively I might expect 1 to be the highest. I want to replace the numbers with letters so that I can see everything in the same format. The equivalent grades are 9 = ‘A\*’, 8 = ‘A\*/A’, 7 = ‘A’, 6 = ‘B’, 5 = ‘B/C’, 4 = ‘C’, 3 = ‘D/E’, 2 = ‘E/F’, 1 = ‘G’.

This week, I’ll look at how to find the equivalent letter grade using the **M** function **List.ReplaceMatchingItems()**; next time, I’ll use a different approach.

![](https://sumproduct.com/wp-content/uploads/2025/05/5af8161ed8344422c4f5166688d6f97c.jpg)

I begin by creating a query ‘From Table’ in the ‘Get & Transform’ section of the ‘Data’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/19455197f7ab47f05f4c5ca44db364b2.jpg)

I could create a custom column for each of my numerically graded subjects, but I want to substitute all my columns at the same time. I could try replacing values in all of my columns:

![](https://sumproduct.com/wp-content/uploads/2025/05/4b74b65695f1675aaa2917c9b38f8993.jpg)

However, this would only replace one value at a time. I want to translate all the values at the same time for all my numeric columns. One way to do this is to use the **List() M** functionality. I begin by merging the columns I need to translate; **_English Language_**, **_English Literature_** and **_Mathematics._**

![](https://sumproduct.com/wp-content/uploads/2025/05/85fb1fc9573165cf6505d0aa4896fb1a.jpg)

I decide to use a comma delimiter to help me convert my data back later.

![](https://sumproduct.com/wp-content/uploads/2025/05/72d84ab6fbbdbb533d08cfd4df2b672b.jpg)

Now I can use **Text.ToList()** to convert my column to lists:

![](<Base64-Image-Removed>)

This gives me a column of lists that I can manipulate.

![](<Base64-Image-Removed>)

I can now use a **List()** function to transform my data. The one I am going to use is

**List****.ReplaceMatchingItems(****list****as****list****, replacements** **as** **any ,optional equationCriteria** **as** **any)** **as****list**

This replaces occurrences of existing values in the **list** with new values using the provided **equationCriteria**. Old and new values are provided by the replacements parameters.

![](<Base64-Image-Removed>)

The **M** formula I have used is

**\= List.ReplaceMatchingItems(\[List of Grades\],{ {“9″,”A\*”},  {“8″,”A\*/A”},  {“7″,”A”},  {“6″,”B”},  {“5″,”B/C”},  {“4″,”C”},  {“3″,”D/E”},  {“2″,”E/F”},  {“1″,”F/G”}})**

Now I will extract my list.

![](<Base64-Image-Removed>)

I could have chosen a delimiter here, but I already have a comma ready to split my text.

![](<Base64-Image-Removed>)

On the ‘Transform’ tab, I can choose to split my column.

![](<Base64-Image-Removed>)

I click ‘OK’ to create three new columns.

![](<Base64-Image-Removed>)

I can now remove the other list and the temporary column I used to merge the grades. I also rename my new columns.

![](<Base64-Image-Removed>)

I can now see what the equivalent grade is for English and Mathematics. There is often more than one way to achieve a result and next time I’ll look at another method which allows for new numeric grades to be added (which is why the examination boards decided to have 9 as the top grade – they can add a grade 10 above this for even higher results!)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-upgrading-grades/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-upgrading-grades/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-upgrading-grades/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-upgrading-grades/#0)

[](https://sumproduct.com/blog/power-query-upgrading-grades/#0 "close")

top