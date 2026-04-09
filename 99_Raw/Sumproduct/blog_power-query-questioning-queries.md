# Power Query: Questioning Queries

**Source:** https://sumproduct.com/blog/power-query-questioning-queries/

---

[Home](https://sumproduct.com/)

\> Power Query: Questioning Queries

*   February 28, 2023

Power Query: Questioning Queries
================================

Power Query: Questioning Queries
================================

1 March 2023

_Welcome to our Power Query blog. This week, I suggest some tips when encountering a query model for the first time._

Mary, my favourite imaginary salesperson, has been dabbling in Power Query. She has constructed some queries to solve a problem, but now she is on a well-earned break, and I have to investigate what it does:

![](https://sumproduct.com/wp-content/uploads/2025/05/c58ee8f8011ca507c38242436906fe12.jpg)

These are my three \[3\] top tips when looking at someone else’s query model. Note that this is quite a simple model, which I have chosen so that the screen shots will include all the information. The same principles apply to much larger models.

**_Tip 1: Admire the View_**

I find the best way to get a feel for a collection of queries is to head to the View tab and use the ‘Query Dependencies’ button:

![](https://sumproduct.com/wp-content/uploads/2025/05/42caa11afb332a5143ed498d20af3a86.jpg)

This gives me a diagram, allowing me to work out the relationships between the queries:

![](https://sumproduct.com/wp-content/uploads/2025/05/e23bc47d2f63db209c1b5a87f4112f3b.jpg)

This tells me where the data comes from, which queries are loaded to the workbook, and which queries are connected. As the name suggests, the dependencies are shown too. I can adjust the size of the diagram and choose to maximise the window if I wish, by using the controls at the bottom right. I can also change the way the data appears by choosing a different Layout:

![](https://sumproduct.com/wp-content/uploads/2025/05/3504a405c1307c41725d359258b4b228.jpg)

I notice that the function **fx\_Rental** is not dependent on a query, which brings me to my next tip…

**_Tip 2: Viewing Functions_**

If I view this function, I cannot see the steps:

![](https://sumproduct.com/wp-content/uploads/2025/05/f753ef0289ba9e4bf1fa22a920adaf74.jpg)

This would not be an issue if I had an underlying query which had been converted to a function, but you may still come across standalone functions like this. I can either use the ‘Advanced Editor’ from the Home tab to view the steps

![](<Base64-Image-Removed>)

or, if want to see the steps in the ‘APPLIED STEPS’ pane, I can take a duplicate copy of the function:

![](<Base64-Image-Removed>)

Using the copied query, I can remove the features that make it a function (the highlighted lines below):

![](<Base64-Image-Removed>)

I check I have no errors:

![](<Base64-Image-Removed>)

Now I can look at the steps individually:

![](<Base64-Image-Removed>)

**_Tip 3: Use a Subset of Data_**

Perhaps the best way to check what a query does is to actually run it. However, this can be time-consuming with large data sets. One way to speed things up, is to run a query on a subset of data. I looked at the ‘Query Dependencies’ in the first tip, and I can use this to determine the base query, in this case **Events preGroup**. Reducing the rows returned by this query will affect all the other queries too, speeding up the model.

![](<Base64-Image-Removed>)

If I go to the ‘Source’ step, I can insert a step to reduce the data:

![](<Base64-Image-Removed>)

Obviously, for this query this step would not be necessary, but I am showing the principle. If I choose to ‘Keep Rows’ from the Home tab, I can control the amount of data processed:

![](<Base64-Image-Removed>)

In a large model, I might choose a value of 1000, but here, I will choose the top two \[2\] rows. When I try to enter the step I will get a warning, which I can ignore:

![](<Base64-Image-Removed>)

I continue, and enter the step:

![](<Base64-Image-Removed>)

This reduces the data, and the time to process the query.

![](<Base64-Image-Removed>)

I hope these tips help next time you are presented with someone else’s query!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-questioning-queries/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-questioning-queries/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-questioning-queries/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-questioning-queries/#0)

[](https://sumproduct.com/blog/power-query-questioning-queries/#0 "close")

top