# Power Query: Space for a CamelCase

**Source:** https://sumproduct.com/blog/power-query-space-for-a-camelcase/

---

[Home](https://sumproduct.com/)

\> Power Query: Space for a CamelCase

*   November 24, 2020

Power Query: Space for a CamelCase
==================================

Power Query: Space for a CamelCase
==================================

25 November 2020

_Welcome to our Power Query blog. This week, I look at how to automate inserting spaces into CamelCase headings._

_I have some tent data:_

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-101-1.jpg)

_My headings are in CamelCase,_ _i.e._ _each word begins with a capital letter, but there is no space between the words. I want to change all my headings to separated words._

I extract my data to Power Query by using ‘From Table’ in the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-91-1.jpg)

_I accept the usual defaults._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-82-1.jpg)

_I want to investigate how Power Query would do this; I am going to demote my headings and manipulate my data._

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-73-1.jpg)

_On the Transform tab, I can ‘Use Headers as First Row’ in the dropdown from ‘Use First Row as Headers’._

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-63-1.jpg)

_I can now look at how I could divide up my data. I can use the ‘Split Column’ options on the Transform tab._

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-55-1.jpg)

_I have the option to split ‘By Lowercase to Uppercase’, which is similar to the effect I want to achieve. I try this._

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-50-1.jpg)

_This has separated my data into individual words, and now I can recombine the columns._

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-39-1.jpg)

_I select my new columns and choose ‘Merge Columns’._

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-33-1.jpg)

_I choose to use a space as the separator._

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-27-1.jpg)

I now have the two core parts of the code I will need. I need to split the text by change of case, and then combine my text with a delimiter. In Power Query, these functions are **Splitter.SplitTextByCharacterTransition()** and **Text.Combine****()**.

**Splitter.SplitTextByCharacterTransition(before** as anynonnull, **after** as anynonnull**)** as function

This returns a function that splits text into a list of text, according to a transition from one kind of character to another. The **before** and **after** parameters can either be a list of characters, or a function that takes a character and returns true / false.

In the step, the code is:

**Splitter.SplitTextByCharacterTransition({“a”..”z”}, {“A”..”Z”})**

**Text.Combine(texts** as list, optional **separator** as nullable text**)** as text

returns the result of combining the list of text values, **texts**, into a single text value. An optional **separator** used in the final combined text may be specified, **separator**.

I don’t have to demote my headings to make these changes thanks to another Power Query **M** function **Table.TransformColumnNames()**:

**Table.TransformColumnNames(table** as table, **nameGenerator** as function, optional **options** as nullable record**)** as table

This transforms column names by using the given **nameGenerator** function.

I can combine these **M** functions to get my result.

![](<Base64-Image-Removed>)

When I enter my new step I can see the results:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.TransformColumnNames(#”Changed Type”, each Text.Combine(Splitter.SplitTextByPositions(Text.PositionOfAny(\_, {“A”..”Z”},2)) (\_), ” “))**

This will convert CamelCase to separate words in any number of column headings.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-space-for-a-camelcase/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-space-for-a-camelcase/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-space-for-a-camelcase/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-space-for-a-camelcase/#0)

[](https://sumproduct.com/blog/power-query-space-for-a-camelcase/#0 "close")

top