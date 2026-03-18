# Power Query: Month Mayhem – Part 6

**Source:** https://sumproduct.com/blog/power-query-month-mayhem-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Month Mayhem – Part 6

*   August 6, 2024

Power Query: Month Mayhem – Part 6
==================================

Power Query: Month Mayhem – Part 6
==================================

7 August 2024

_Welcome to our Power Query blog. Today, I_ _continue mapping the data._

My salespeople are back from their break and I have more reports to construct. I have a report with a list of the clients they have been working with each month:

![](https://sumproduct.com/wp-content/uploads/2025/05/07d2396a8cbe0dcf0c6216decc0d6948-1.jpg)

I would like to display the amount details in the salesperson sections but aligned to the relevant month at the top of the page:

![](https://sumproduct.com/wp-content/uploads/2025/05/4ff41a7a511bf844c47ac9c5ba146bb1-1.jpg)

[Last time](https://sumproduct.com/blog/power-query-month-mayhem-part-5/)
, I created a mapping query, which I called **Column\_Mapping**:

![](https://sumproduct.com/wp-content/uploads/2025/05/249c779a5f6af73b9edf151e1dd321ba-1.jpg)

I will continue mapping my data. Whilst I can use the query I have created for the data, I need a more concise mapping tool for the months. I take a reference copy of **Column\_Mapping**, which I call **Column\_Mapping\_Master**.

![](https://sumproduct.com/wp-content/uploads/2025/05/73f8e8cb248a1b6390e06f3cb87e6f2f-1.jpg)

I am going to filter on **Months\_Unpivoted.Attribute** to remove _null_ values:

![](https://sumproduct.com/wp-content/uploads/2025/05/b94c16f9260a431410201d4520b3a402-1.jpg)

This reduces the number of rows to the months where data will appear:

![](https://sumproduct.com/wp-content/uploads/2025/05/5d5dba0e421920945de0db105714eb0b-1.jpg)

**Column\_Mapping\_Master** is complete. It is time to begin rebuilding my data to create the new table. I start in **Column\_Mapping**, where I am going to ‘Merge as New’ with **Column\_Mapping\_Master**:

![](https://sumproduct.com/wp-content/uploads/2025/05/8e698463e5abc51db491ceaa4078278b-1.jpg)

I merge on **Section Index** and **Attribute**, being careful to select the columns in the same order. I call the new query **Mapping Merge**:

![](https://sumproduct.com/wp-content/uploads/2025/05/88d8e385a216b199594c0f77d57261a6-1.jpg)

I expand **Column\_Mapping\_Master** and select **Mapping**:

![](https://sumproduct.com/wp-content/uploads/2025/05/96bb630065abd3b53b047aa1dfe0a76e-1.jpg)

Since there is already a column with the same name, I keep the prefix option.

![](https://sumproduct.com/wp-content/uploads/2025/05/668923604d4980370b7d8f6ea38b9dfe-1.jpg)

I select the ‘Choose Columns’ option from the Home tab, and select **Column1**, **Index**,**Value** and **Column\_Mapping\_Master.Mapping**:

![](<Base64-Image-Removed>)

This gives me four \[4\] columns:

![](<Base64-Image-Removed>)

I want to sort on the column number, but if I sort on the text, ‘Column11’ would come before ‘Column2’. I need to get the digits from the **Column\_Mapping\_Master.Mapping** column, whilst keeping the column, so I use Extract from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I extract the data after ‘Column’. This gives me a new column, which I can change to whole numbers and sort on:

![](<Base64-Image-Removed>)

I can now delete the new column and select **Column\_Mapping\_Master.Mapping** and then **Value** and choose to pivot these columns:

![](<Base64-Image-Removed>)

I select the ‘Advanced options’ and choose ‘Don’t Aggregate’:

![](<Base64-Image-Removed>)

This query is complete; I will continue transforming my data next time.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-month-mayhem-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-month-mayhem-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-month-mayhem-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-month-mayhem-part-6/#0)

[](https://sumproduct.com/blog/power-query-month-mayhem-part-6/#0 "close")

top