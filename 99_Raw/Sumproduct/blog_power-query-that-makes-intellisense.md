# Power Query: That Makes (Intelli)sense

**Source:** https://sumproduct.com/blog/power-query-that-makes-intellisense/

---

[Home](https://sumproduct.com/)

\> Power Query: That Makes (Intelli)sense

*   August 13, 2019

Power Query: That Makes (Intelli)sense
======================================

Power Query: That Makes (Intelli)sense
======================================

14 August 2019

_Welcome to our Power Query blog. Today, I look at the Intellisense features available in Power BI’s Power Query (Get Data)._

I was hoping that Intellisense might be Generally Available in Excel Power Query by now. At the time of writing, it appears to have been introduced the Insider build of Excel in the July 2019 release, but while I am (impatiently) waiting, I’ll take a look at what is available to help me to write **M** code in Power BI. I currently have Intellisense switched on for Power Query as the Power Query tab of the Options dialog shows:

![](<Base64-Image-Removed>)

Intellisense is available in several places. For example, it’s present in the formula bar:

![](<Base64-Image-Removed>)

And the Advanced Editor:

![](<Base64-Image-Removed>)

And when I add a Custom Column:

![](<Base64-Image-Removed>)

For me, the most important feature of Intellisense is that it will suggest **M** code that I can use.

![](<Base64-Image-Removed>)

I can see more detail for the **M** function suggested by clicking on the information icon or pressing **CTRL + SPACE**.

![](<Base64-Image-Removed>)

Intellisense will also suggest query related data. Again, I can see more detail for the query data suggested by clicking on the information icon or pressing **CTRL + SPACE**. The icons next to the suggested code tell me what kind of data I am looking at.

![](<Base64-Image-Removed>)

Intellisense will also suggest functions that I have created. For instance, the information provided in this case is the content of the function rather than the description.

![](<Base64-Image-Removed>)

This one is a little less consistent. At the time of writing, the Advanced Editor and Custom Column would suggest parameters, but the function Ribbon wouldn’t.

In all places, the type of element is colour-coded, so keywords like ‘let’ are in blue, and variables like table names are in green, for instance. This is not always helpful – especially as comments are green too! Brackets are also provided in pairs, so if I type ‘(‘, then ‘)’ also appears to make sure I don’t forget to close the brackets. If I click on one end of a bracket, the opposite end is highlighted to help me read the code too. This works for speech marks too:

![](<Base64-Image-Removed>)

Hovering over a step name prompts Intellisense to give details of what happens in that step.

![](<Base64-Image-Removed>)

If I highlight an **M** function, I get information about how to use it, which saves me a hunt through the help pages to see which parameter I am missing this time!

![](<Base64-Image-Removed>)

Similar functionality is available as I am entering an **M** function:

![](<Base64-Image-Removed>)

Another useful feature in the Advanced Editor is the ability to show line numbers. This makes life much easier when referring to a section in large query.

![](<Base64-Image-Removed>)

I also like the word wrap option, which is useful for blogs! This combined with the fact that some of the indenting is automatic, helps to create code that is much easier to read.

Whilst some of the Intellisense features may lead to a slightly slower processing experience for some users, I would like to see them introduced to Excel Power Query too, as **M** can be a difficult language to wrangle with.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-that-makes-intellisense/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-that-makes-intellisense/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-that-makes-intellisense/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-that-makes-intellisense/#0)

[](https://sumproduct.com/blog/power-query-that-makes-intellisense/#0 "close")

top