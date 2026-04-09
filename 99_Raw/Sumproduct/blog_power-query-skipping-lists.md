# Power Query: Skipping Lists

**Source:** https://sumproduct.com/blog/power-query-skipping-lists/

---

[Home](https://sumproduct.com/)

\> Power Query: Skipping Lists

*   January 8, 2019

Power Query: Skipping Lists
===========================

Power Query: Skipping Lists
===========================

9 January 2019

_Welcome to our Power Query blog. This week I look at M functions List.Skip() and List.Alternate()._

Well over a year ago now, I looked at how lists could be created and manipulated in [Power Query: Birthday Lists](https://sumproduct.com/blog/power-query-birthday-lists/)
. I covered the more common **M** functions, but today I am going to look at **List.Skip()** and **List.Alternate()** to see what they do.

Looking at List.Skip() first:

**List.Skip(list as list, optional countOrCondition as any) as list**

This skips the first item of the list. Given an empty list, it returns an empty list. This function takes an optional parameter **countOrCondition** to support skipping multiple values.

To illustrate, I am going to look at a simple list:

![](<Base64-Image-Removed>)

I apply **List.Skip()** to my source, with no parameters, _viz._

![](<Base64-Image-Removed>)

The default action is to remove the first item on the list. If I want to remove the first three items, I need to set the count:

![](<Base64-Image-Removed>)

If I set the parameter to be three (3), then the first three items in my list are removed.

Now, I’ll try the same list with **List.Alternate()**:

![](<Base64-Image-Removed>)

**List.Skip(Source, 1)** and **List Alternate(Source,1)** give the same answer. In fact, **List.Skip()** and **List.Alternate()** behave the same as long as only one parameter is given to **List.Alternate()** – it does require at least one parameter to be entered, unlike **List.Skip()**. In order to see what **List.Alternate()** can do differently, I need to look at the other parameters that can be passed to it. However, let’s take a look at the syntax first:

**List.Alternate(list as list, count as number, optional repeatInterval as nullable number, optional offset as nullable number) as list**

This returns a list with the items alternated from the original list based on a count, optional **repeatInterval**, and an optional **offset**.

I need to try this with my list.

![](<Base64-Image-Removed>)

I have used the second parameter, which is the repeat interval. It’s easier to see what has happened with a number line:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10

The first three items are removed, then there is an interval of two, and then the next three items are removed.

If I change my parameters to **List.Alternate(Source,2,1)** I would expect to see

1, 2, 3, 4, 5, 6, 7, 8, 9, 10

_i.e._ only 3, 6 and 9 left.

![](<Base64-Image-Removed>)

This is what I expected. So now I need to try the third parameter, **offset**:

![](<Base64-Image-Removed>)

With an offset of 1, I have:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

The offset has told the function to leave the first item (_i.e._ item number 1) before removing items according to the other parameters.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-skipping-lists/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-skipping-lists/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-skipping-lists/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-skipping-lists/#0)

[](https://sumproduct.com/blog/power-query-skipping-lists/#0 "close")

top