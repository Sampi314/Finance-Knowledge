# VBA Blogs: Getting Loopy Each Time

**Source:** https://sumproduct.com/blog/vba-blogs-getting-loopy-each-time/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Getting Loopy Each Time

*   March 8, 2018

VBA Blogs: Getting Loopy Each Time
==================================

VBA Blogs: Getting Loopy Each Time
==================================

9 March 2018

Loops are a powerful tool in programming to repeat a sequence of instructions. For Loops were covered [here](https://www.sumproduct.com/blog/article/vba-blogs/for-loops)
 and they are really good for performing actions a fixed number of times.

But what if you want to perform an action to every object in a set?

For Each…Next loops are a great way to cycle through sets – like an array or a range. Sometimes we don’t know the size of the set, like in a table. Using **ListObject.ListRows.Count** is a way to find the number of rows in order to use the simple **For** loop but using **For Each…Next** more clearly illustrates that the instructions are happening to _every_ row.

The example table today shows sales data, in a table called **Tbl\_Sales**:

![](https://sumproduct.com/wp-content/uploads/2025/05/2423a46aef8d5f27729fa5959c76d289.jpg)

Let’s calculate each sales rep’s cumulative sales as time goes by – as in, calculate the total sales they each made to the date of that sale i.e. Jill made $213 + $840 + $955 = $2,008 cumulative sales on the 4th of July (admittedly this can be achieved quite easily with a **SUMIF** formula with a moving range).

Here’s the code:

![](https://sumproduct.com/wp-content/uploads/2025/05/aa2910749cddc0d8a61bf5f3170c080e.jpg)

Notice that when using **Option Explicit** to force declaration of variables, the child of the parent object must also be declared – in this example for a table, using **ListRows**.

![](https://sumproduct.com/wp-content/uploads/2025/05/0c77db86e151bfee8619f8ca5e162bf8.jpg)

Tada! This is a pretty basic example of how each row can be examined in a table, but **For Each…Next** can also be used for arrays and cell ranges.

Circle back to the VBA blog next Friday **Until** you can see what we can **Do**.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-getting-loopy-each-time/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-getting-loopy-each-time/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-getting-loopy-each-time/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-getting-loopy-each-time/#0)

[](https://sumproduct.com/blog/vba-blogs-getting-loopy-each-time/#0 "close")

top