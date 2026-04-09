# Power Query: Sorry, Not on the List

**Source:** https://sumproduct.com/blog/power-query-sorry-not-on-the-list/

---

[Home](https://sumproduct.com/)

\> Power Query: Sorry, Not on the List

*   March 6, 2018

Power Query: Sorry, Not on the List
===================================

Power Query: Sorry, Not on the List
===================================

7 March 2018

_Welcome to our Power Query blog. This week, I take a look at how extracting data from multiple lists can be confusing when nulls are involved._

I have a table of lists, which I need to extract. I am hoping that I will be able to keep the data aligned so that it makes sense. In real life, this would be more likely to be long references, but my chosen data will make the problem I am about to encounter more obvious.

![](https://sumproduct.com/wp-content/uploads/2025/05/c1f5225c9bf7acc13d7d28822ff64842.jpg)

I want to extract the values from my list, so I click on the little split line icon at the right of the **Column1** heading.

![](https://sumproduct.com/wp-content/uploads/2025/05/0547da05fa1d77b1a4a775a20b025854.jpg)

If I were to choose the ‘Expand to New Rows’ option, I would get a row for each value in each of my lists. I don’t want this; I want to see my lists one above the other. I choose ‘Extract Values’:

![](https://sumproduct.com/wp-content/uploads/2025/05/06878d89b67926c9c98be2a546bb361b.jpg)

I can choose a delimiter to separate the values on my list, so I choose to use a semicolon (**;**).

![](https://sumproduct.com/wp-content/uploads/2025/05/df7533ff291abf1f8254f70f4d320342.jpg)

My data starts off well. “A FOR APPLE” goes together properly, as does “E FOR EATEN”. However, I don’t think “P IS FOR QUERY” is quite so good. If I check the data, I see that things start to go wrong at “I”, which is definitely not for “JOKER”!

If I go back a step and look at my data in rows using the ‘Expand to New Rows’ option instead, I can check why the data doesn’t make sense after “I”.

![](https://sumproduct.com/wp-content/uploads/2025/05/ce953a5e1ef78d08bdb2c6fb56ecdc84.jpg)

In the entry where the word beginning with ‘I’ should have gone, there is a null. The number of entries is right, and I can see my data is in the list, so why has Power Query ignored the null entry and misaligned my data?

To see the answer, I need to go back to my ‘Extract Values’ step and look at the **M** language behind it.

**\= Table.TransformColumns(#”Converted to Table”,**

**{“Column1”, each Text.Combine(List.Transform(\_, Text.From), “;”), type text})**

The culprit here is **Text.Combine**. I can test this with a simple scenario in another blank query.

![](<Base64-Image-Removed>)

The **M** language I use here is very simple, and it is easy to see what happens.

**\= Text.Combine({“one”, null, “two”})**

This combines the text in the list provided and ignores the null. Therefore, my data will be misaligned. How I get around this would be to replace the nulls in my lists with something else – and that something else really depends on the context. It could be ‘N/A’, spaces or whatever makes sense. In my alphabet example, I will replace my null with “—–” until I can think of a good word for “I”.

It would be great if Power Query could use the GUI replace option for this:

![](https://sumproduct.com/wp-content/uploads/2025/05/e8fca94eb4c2b0b8394d2db0fa68dcbe.jpg)

However, since the values are not currently visible, this will not work. I need some **List** functionality.

**List.ReplaceValue(list as list, oldValue as any, newValue as any, replacer as function) as list**

where **list** is the list to modify, **oldValue** is the value to replace (the null in my case), and **newValue** is the value to replace it with (“—–“). The argument **replacer** is used to tell Power Query what kind of values are being replaced, and in this case, I would use **Replacer.ReplaceValue**.

I need to add this step before I start manipulating the lists. In practice, it would be best to apply this to any list where there is a risk of nulls being present, but I will add this to my second list, as that is the one causing me problems.

![](<Base64-Image-Removed>)

Since my lists are defined in my source, the **M** language I need for the second list is:

**\= {List\_Letter,List.ReplaceValue(List\_Word,null,”—–“,Replacer.ReplaceValue)}**

Now when I execute the query again, I see my lists aligned correctly:

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-sorry-not-on-the-list/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-sorry-not-on-the-list/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-sorry-not-on-the-list/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-sorry-not-on-the-list/#0)

[](https://sumproduct.com/blog/power-query-sorry-not-on-the-list/#0 "close")

top