# Power Query: Excellent Examples

**Source:** https://sumproduct.com/blog/power-query-excellent-examples/

---

[Home](https://sumproduct.com/)

\> Power Query: Excellent Examples

*   September 4, 2018

Power Query: Excellent Examples
===============================

Power Query: Excellent Examples
===============================

5 September 2018

_Welcome to our Power Query blog. July brought some improvements to Power Query/Get and Transform. I look at how creating a column from examples has developed._

As regular readers will know, ‘Column from Examples’ is a favourite of mine, so when I saw that it had been improved again, I wanted to see what I could do with it now. The good news is that I can now multitask by using this feature, as I can use it to combine transformations.

This reminded me of a problem I was trying to solve in [Power Query: Initial Problems](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-initial-problems)
. In that blog, I wanted to reformat some names:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-573.jpg)

My aim was to transform the **_FULL\_NAME_** so that I could have ‘C. Parr’ instead of ‘CHRISTINE PARR’. The problem I came up against (shown in version 2013 of Power Query) was that ‘Column from Examples’ couldn’t cope:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-594.jpg)

So, I am going to try that again!

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-548.jpg)

In the ‘Add Column’ tab there is a section called ‘Column from Examples’ and I am going to allow Power Query to get data for my new Column ‘From All Columns’.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-498.jpg)

Well this is definitely an improvement! After two examples, my new column has been created. I click ‘OK’ to get my new column:

**\= Text.Combine({Text.Start(\[FULL\_NAME\], 1), “. “, Text.Proper(Splitter.SplitTextByDelimiter(” “, QuoteStyle.None)(\[FULL\_NAME\]){1}?)})**

I delete this column and try combining data from other columns – this time, not only do I want to format the name, I also want to include the job title and region:

![](<Base64-Image-Removed>)

I create the column to see the full transformation.

**\= Text.Combine({Text.Start(\[FULL\_NAME\], 1), “. “, Text.Proper(Splitter.SplitTextByDelimiter(” “, QuoteStyle.None)(\[FULL\_NAME\]){1}?), ” (“, \[REP\_TYPE\_C3\], “) “, \[AREA\_CODE\]})**

It shows that it’s worth trying out new methods to solve old problems, as Power Query is constantly improving.

There are also developments in using dates in ‘Column from Examples’ for date formats used in specific domains though I found this functionality a bit hit and miss, hopefully it will improve. I tried it with **_JOIN\_DATE_** in the following example:

![](<Base64-Image-Removed>)

The date is translated to MM-YY from a full datetime format.

The **M** formula is

**\= Text.Combine({DateTime.ToText(\[JOIN\_DATE\], “MM”), “-“, DateTime.ToText(\[JOIN\_DATE\], “yy”)})**

I can also extract the name of the month:

![](<Base64-Image-Removed>)

I create the new column.

![](<Base64-Image-Removed>)

The **M** formula used is:

**\= Text.Combine({DateTime.ToText(\[JOIN\_DATE\], “MMMM”), ” “, DateTime.ToText(\[JOIN\_DATE\], “yyyy”)})**

It’s good to see the functionality is expanding, making ‘Column from Example’ an even more useful feature – especially for beginners.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-excellent-examples/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-excellent-examples/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-excellent-examples/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-excellent-examples/#0)

[](https://sumproduct.com/blog/power-query-excellent-examples/#0 "close")

top