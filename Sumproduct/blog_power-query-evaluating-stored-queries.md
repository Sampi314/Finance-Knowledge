# Power Query: Evaluating Stored Queries

**Source:** https://sumproduct.com/blog/power-query-evaluating-stored-queries/

---

[Home](https://sumproduct.com/)

\> Power Query: Evaluating Stored Queries

*   January 30, 2018

Power Query: Evaluating Stored Queries
======================================

Power Query: Evaluating Stored Queries
======================================

31 January 2018

_Welcome to our Power Query blog. This week, I take a look at a way to store queries in a text file._

In my recent article [It’s Good to Share (a Query)](https://sumproduct.com/blog/power-query-its-good-to-share-a-query/)
, I looked at a few ways to share queries between workbooks. This week, I take a look at a slightly different approach, and it relies on the following **M** function:

**Expression.Evaluate**(**expression** as text, **optional environment** as \[…\]) as any

It should be noted:

*   This evaluates a text expression and returns the evaluated value.
*   **Expression** is the expression to evaluate
*   **optional environment** is the expression environment.

That’s a very short explanation for quite a powerful function! What it does is to treat the expression as **M** language and then runs it. The best way to understand it, is to see it in action. Below I have some of my product data and I am going to create a simple query:

![](https://sumproduct.com/wp-content/uploads/2025/05/152727a9cc7f1eedae857279c3b288fd.jpg)

In the ‘Get and Transform’ section, I choose to create a new query ‘From Table’. I call my new query ‘**Apply\_Tax**‘ and I am going to add a new column to my query in the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/06b9b6da8105eb5bf454216e85f68762.jpg)

I will use the ‘Custom Column’ to create my new column.

![](https://sumproduct.com/wp-content/uploads/2025/05/c1a54b58ca73bdddc24fa597b4535eb5.jpg)

I choose to add 20%, and create my new column. I opt to change it to datatype ‘Currency’ for information; the formatting doesn’t matter here as I can deal with that in my Excel Worksheet.

![](https://sumproduct.com/wp-content/uploads/2025/05/066ca4a021993c62719499071b35434c.jpg)

Today, I am interested in the **M** language generated behind the scenes. Here, I access the ‘Advanced Editor’ from the ‘Home’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/386f2d23320f7ed67ce2d8544b1913ef.jpg)

I copy and paste this text to a text file on my PC.

![](<Base64-Image-Removed>)

If I go back to my original data, I can now use the **M** language stored in my text file. I discard the ‘**Apply\_Tax**‘ query and create a new blank query by choosing ‘From Other Sources’ and then ‘Blank Query’ from the ‘New Query’ option in the ‘Get and Transform’ section.

![](<Base64-Image-Removed>)

I need to enter the **M** language below in order to run the code in my text file:

![](<Base64-Image-Removed>)

**let**

**Source=Text.FromBinary(File.Contents(“C:UserskathrOneDriveDocumentsPQ\_Applied\_Tax.txt”)), EvaluatedExpression = Expression.Evaluate(Source, #shared)**   

**in**

**EvaluatedExpression**

I create my new query and check the results.

![](<Base64-Image-Removed>)

The query has been executed correctly and I can easily share the text on an accessible drive for other users.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-evaluating-stored-queries/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-evaluating-stored-queries/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-evaluating-stored-queries/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-evaluating-stored-queries/#0)

[](https://sumproduct.com/blog/power-query-evaluating-stored-queries/#0 "close")

top