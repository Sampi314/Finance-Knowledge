# Power Query: Evaluate the Environment

**Source:** https://sumproduct.com/blog/power-query-evaluate-the-environment/

---

[Home](https://sumproduct.com/)

\> Power Query: Evaluate the Environment

*   June 22, 2021

Power Query: Evaluate the Environment
=====================================

Power Query: Evaluate the Environment
=====================================

23 June 2021

_Welcome to our Power Query blog. This week I look at the importance of environment to Expression.Evaluate()._

In [last week’s blog](https://sumproduct.com/blog/power-query-fixed-expression/)
 I looked at the **M** function **Expression.Constant()**; this time I am going to look at a related function **Expression.Evaluate()**

**Expression.Evaluate(****document** as text, optional **environment** as nullable record**)** as any

Returns the result of evaluating an **M** expression **document** with the available identifiers that can be referenced defined by **environment**.

Several examples are given in the help pages, the second goes some way to explaining how to use the function. I have reproduced it here:

![](<Base64-Image-Removed>)

The **M** code is:

**\= Expression.Evaluate(“List.Sum({1, 2, 3})”, \[List.Sum = List.Sum\])**

So, the document is a text version of another **M** function, **List.Sum()**. The environment is telling the query what to do with the function. I would like to look at what I should put in the environment when I am trying to use this expression.

Since this is a very simple example, I could have just used the document part of the expression.

![](<Base64-Image-Removed>)

where the **M** code is:

**List.Sum({1,2,3})**

However, there is another way to use the function which is more useful.

Going back to my simple query, I copy the code from the Advanced Editor

![](<Base64-Image-Removed>)

and then store it in a text file:

![](<Base64-Image-Removed>)

I’ve effectively saved my query.

Now, in a new Blank Query, I am going to use my saved text as a source.

![](<Base64-Image-Removed>)

The **M** code is:

**let**

**Source = Text.FromBinary(File.Contents(“C:UserskathrOneDriveDocumentsPQ\_StandardExpensesPQ Blogevaluate.txt”)),**

**Evaluated = Expression.Evaluate(Source, #shared)**

**in**

**Evaluated**

This is taking my saved query as text and evaluating what the function should be by using the **#shared** function.

![](<Base64-Image-Removed>)

This executes the stored text.

**#shared** allows me to access the details of the functions available; it’s like a built-in encyclopaedia of functions.

![](<Base64-Image-Removed>)

If I convert this into a table, then I will be able to locate **List.Sum()**.

![](<Base64-Image-Removed>)

I just need to filter on **Name:**

![](<Base64-Image-Removed>)

This gives me just that function, so I can drill down to get the details:

![](<Base64-Image-Removed>)

I can then view how the function is used:

![](<Base64-Image-Removed>)

The **#shared** function allows **Expression.Evaluate()** to run the query.

Could I have used this instead of the **\[List.Sum = List.Sum\]** in the simple example I started with?

**Expression.Evaluate(“List.Sum({1, 2, 3})”, \[List.Sum = List.Sum\])**

![](<Base64-Image-Removed>)

Yes, I could: when using **Expression.Evaluate()**, using **#shared** will allow me to set the environment correctly.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-evaluate-the-environment/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-evaluate-the-environment/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-evaluate-the-environment/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-evaluate-the-environment/#0)

[](https://sumproduct.com/blog/power-query-evaluate-the-environment/#0 "close")

top