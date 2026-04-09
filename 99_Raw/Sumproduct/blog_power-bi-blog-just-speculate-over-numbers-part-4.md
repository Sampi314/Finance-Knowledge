# Power BI Blog: Just Speculate Over Numbers – Part 4

**Source:** https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-4/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Just Speculate Over Numbers – Part 4

*   May 23, 2018

Power BI Blog: Just Speculate Over Numbers – Part 4
===================================================

Power BI Blog: Just Speculate Over Numbers – Part 4
===================================================

24 May 2018

Remember last week, we successfully extracted the names of the columns from the metadata of the JSON file. Now it’s time to put the two queries together!

What we need to do is append the data set to the column names retrieved from the metadata. Then, we can promote the metadata row sitting on top as the headers.

As covered in [Power Query: Abridged Appending](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-abridged-appending)
, we can put two queries on top of each other.

However, what we should do is make the append the queries in a separate query. This keeps the data transformations of the distinct parts of the table separate. These queries are referred to as “staging” queries.

A staging query or table is used to help prepare your final data output. This is usually a series of steps that we want to keep contained. In this case, we want to keep all the steps to extract the Metadata separate from the final table. This means we know exactly which steps apply to which result. It makes it easier for debugging should later down the line the query results in errors and we can identify at what point it broke down.

The columns must be named the same identically for the queries to be appended on top of the other. Reviewing our Dataset query, note the headers:

![](https://sumproduct.com/wp-content/uploads/2025/05/44a11a2fd7b8a3bad74ecf27998da5c9.jpg)

This is because when the data was split originally, Power Query uses the original column name and an incremental counter. We could rename everything Column1, Column2 etc., but the quickest way to get to the default column headers is to press Transpose twice.

Now our column names will match what we have in the metadata.

![](https://sumproduct.com/wp-content/uploads/2025/05/e1af87dd1e7bd776253c23522af22faf.jpg)

Success!

This is a neat trick because it flips the table and replaces all the header names with default ones without hard coding any name changes. By avoiding hard coding, it makes our query more flexible should the number of columns change in the future.

Let’s _Reference_ the Metadata query, because that’s the query we want to be on top. We want to reference it is because we want to leave the Metadata query as a _staging query_. Right-click on the query name and press “Reference”.

![](https://sumproduct.com/wp-content/uploads/2025/05/dd6549c9b861063bdc71457bbf3b8d93.jpg)

The difference between “Duplicate” and “Reference” is that “Duplicate” makes an identical copy of the query with all the applied steps. “Reference” refers to the staged query as the source, taking only the end result. This also means that if our original query is edited, the reference query is also updated with the changes. The duplicated query will not.

Append the two queries and “Use First Row as Headers”.

![](https://sumproduct.com/wp-content/uploads/2025/05/df32a3b1147c573aa9358f9622713b83.jpg)

Great!

What’s important are the **Draw Date**, **Winning Numbers** and **Multiplier** columns.

Let’s do a few things to make this data more useful:

*   Remove the other columns
*   Convert the **Draw Date** to Date format only
*   Split the Winning Numbers so they are in separate columns
*   Rename the query to something more meaningful like “Powerball Numbers”

We’ve covered these steps before, so give it a go! Your table should result like this:

![](<Base64-Image-Removed>)

Hit “Close & Apply” and we’re almost finished the transformation section of for our JSON data. All we have left is to identify the staging queries and finalise the output to Power BI.

Tune back next week for more PBI Tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-4/#0)

[](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-4/#0 "close")

top