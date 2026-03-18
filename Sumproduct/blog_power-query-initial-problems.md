# Power Query: Initial Problems

**Source:** https://sumproduct.com/blog/power-query-initial-problems/

---

[Home](https://sumproduct.com/)

\> Power Query: Initial Problems

*   October 17, 2017

Power Query: Initial Problems
=============================

Power Query: Initial Problems
=============================

18 October 2017

_Welcome to our Power Query blog. This week I look at how to convert names into an alternative format._

When changing the format of names in a list, Excel (2013 onwards) has some nice features to help me. The screen below shows how Excel 2013 anticipates the format for the rest of my data after I have entered just two examples:

![](https://sumproduct.com/wp-content/uploads/2025/05/b4b9a779afcb2ff5f07e7d4a5b120d66.jpg)

Flash Fill is excellent, but after I have built my workbook and incorporated it into pretty reports, I find out that there has been a massive change in staff, and I have to do it all again! Power Query can be refreshed, so is there an easy way to do this in Power Query? I upload my data by using the ‘Excel Data’, ‘From Table / Range’ option in the ‘POWER QUERY’ tab _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/46da879e1e901c72e1850c549691cb7f.jpg)

I have seen examples of achieving the desired result by using some GUI features and some **M** code, but for this example, my aim is to use entirely GUI options. My ideal answer would be to use the ‘Column from Examples’ option in the ‘General’ section of the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/8a27984a855425f7798d167052e45ee2.jpg)

I covered the basics of this feature in [Setting an Example](https://sumproduct.com/blog/power-query-setting-an-example/)
, so with high hopes I try it. The concept of this functionality is similar to Flash Fill in Excel; I type a couple of examples and Power Query does the rest.

![](https://sumproduct.com/wp-content/uploads/2025/05/74247b824d466999c9003d478126b038.jpg)

Well, it clearly isn’t quite that clever _yet._ I need to break it down into steps that Power Query can manage. I could use the functionality available in the ‘Transform’ tab, but to keep it simple I’ll stay in ‘Add Column from Examples’. I need to extract the first initial, so I start with this step.

![](https://sumproduct.com/wp-content/uploads/2025/05/b02f89cc10b93e5a0aba770e57e56635.jpg)

This time Power Query has provided me with the formula it has used to work out the rest of the

**Text.Start(\[FULL\_NAME\],1)**

This is easy enough to follow: go to the start of the text and get the first letter. Next, I need to extract the surname. I’ll also try reformatting so that it’s not all in upper case.

![](<Base64-Image-Removed>)

So, Power Query is happy to change the type to ‘Proper’ text, work out the delimiter and get the text after that delimiter:

**Text.BetweenDelimiters(Text.Proper(\[FULL\_NAME\]), ” “, ” “, 0, 0)**

Not bad. All I need to do now is combine my two new columns and I’ll add a full stop after the initial:

![](<Base64-Image-Removed>)

My new column is looking good after just one example, and the **M** code behind the step is shown in the top window:

**Text.Combine((\[First Characters\], “.”,\[Text Between Delimiters\]))**

So, Power Query has created the **M** code that I need in three steps and I can view them in the Advanced Editor. The editor shows the full version of the **M** code required to complete each step in sequence.

![](<Base64-Image-Removed>)

**#”Inserted First Characters” =**

    **Table.AddColumn(#”Changed Type”, “First Characters”,  
each Text.Start(\[FULL\_NAME\], 1), type text),**

**#”Inserted Text Between Delimiters” =**

    **Table.AddColumn(#”Inserted First Characters”, “Text Between Delimiters”,  
each Text.BetweenDelimiters(Text.Proper(\[FULL\_NAME\]), ” “, ” “, 0, 0),** **type text),**

**#”Inserted Merged Column” =**

    **Table.AddColumn(#”Inserted Text Between Delimiters”, “Merged”,  
each Text.Combine({\[First Characters\], “. “, \[Text Between Delimiters\]}), type text)**

Now this code has been created for me, if the data on the employee list changes, I can simply refresh to implement all the steps.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-initial-problems/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-initial-problems/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-initial-problems/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-initial-problems/#0)

[](https://sumproduct.com/blog/power-query-initial-problems/#0 "close")

top