# Power BI Blog: Just Speculate Over Numbers – Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Just Speculate Over Numbers – Part 2

*   May 9, 2018

Power BI Blog: Just Speculate Over Numbers – Part 2
===================================================

Power BI Blog: Just Speculate Over Numbers – Part 2
===================================================

10 May 2018

Welcome back to Power BI Tips!

[Last time](https://www.sumproduct.com/blog/article/power-bi-tips/just-speculate-over-numbers-part-1)
 we imported a JSON file from the NY Powerball. This week, we’re going to use the Power Query Editor to clean up the data portion of the JSON file.

Let’s have a look at our **Dataset** query in the Power Query Editor:

![](https://sumproduct.com/wp-content/uploads/2025/05/f436fcff7f31810b482d5cdc8387c59f.jpg)

Now it’s time to navigate through to the data. Click on the **data** item – “List”.

![](https://sumproduct.com/wp-content/uploads/2025/05/28f6f2de2aee4b0e66daf00ae53825e7.jpg)

We’ve now got a List of Lists here. Let’s have a look at what these _Lists_ show. Select one (in the cell but not on the yellow hyperlink) and at the bottom of the screen it will pop up the contents in a preview.

![](https://sumproduct.com/wp-content/uploads/2025/05/5bf4a1eb12cc03554517e0acceaf64f8.jpg)

That looks like our data!

Now we will want to expand all these records but there is no expansion arrow on the column heading. This is because the data is structured as a _List_ and not a _Table_. We can convert this to a table quite easily.

Because this is a list, you’ll see a “List Tools” section appear in the Ribbon. Under “Transform” in the “Convert” category we want to click the “To Table” button:

![](https://sumproduct.com/wp-content/uploads/2025/05/93ccaefccc02966345cdab5294199835.jpg)

It’ll bring up the following prompt:

![](https://sumproduct.com/wp-content/uploads/2025/05/2cb8e0eb6083417783f87b683337b2e6.jpg)

Currently, we only have one column. We can ignore delimiters for time being. Hit OK to proceed.

![](<Base64-Image-Removed>)

Great! Now we can expand. Click on the expansion arrow:

![](<Base64-Image-Removed>)

See how it gives two options? Don’t perform this step, but I will demonstrate what will happen when we choose “Expand to New Rows “.

![](<Base64-Image-Removed>)

Each individual item in each _List_ is expanded and then appended to each other. This isn’t what is needed as we know that the data is stored as a table.

So please click on “Extract Values…” instead. It will prompt you for a delimiter to concatenate the list. I’ve selected “Tab”. I’ve used Tab because this is unlikely to appear in a table whereas semicolons or commas might appear as part of a text field.

![](<Base64-Image-Removed>)

It results in this:

![](<Base64-Image-Removed>)

This method has preserved the rows and given each list as one item.

Remember that in List expansion, null values are ignored? We need to modify the code slightly as explored in [Power Query: Sorry Not on The List](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-sorry-not-on-the-list)
. I’ve adjusted my formula from

\= Table.TransformColumns(#”Converted to Table”, {“Column1”, each Text.Combine(List.Transform(\_, Text.From), “#(tab)”), type text})

to

\= Table.TransformColumns(#”Converted to Table”, {“Column1″, each Text.Combine(List.Transform(List.ReplaceValue(\_,null,”~~”,Replacer.ReplaceValue), Text.From), “#(tab)”), type text})

“\_” in the context of M-code indicates the current cell value. In my edited formula, I’ve replaced “\_” with “_List.ReplaceValue(\_,null,”~~__“,Replacer.ReplaceValue), Text.From)_.

What this does is replace any cells that contain a _null_ value with the string “{}”.

I’ve used this combination because it’s less likely that this string would be found in our table for us to easily get rid of after we’ve split the columns.

Now “Split Column” by your chosen delimiter.

![](<Base64-Image-Removed>)

Voilá! Here’s our data table.

![](<Base64-Image-Removed>)

I’m going to scroll down to show you what effect our _null_ replacement has on our table:

![](<Base64-Image-Removed>)

Now, we have to reverse our _null_ replacement. Select all the columns in the table. This can be done by selecting the first column and SHIFT clicking on the last one or alternatively pressing the keyboard shortcut CTRL + A. Hit replace values on the Ribbon and replace our “~~” with _null_. The Power Query Editor will accept _null_ as a value and not as a text string.

It’s important to check “Match entire cell contents” here because this will only act on the cells where we know for sure that “~~” replaced _null_ prior to table conversion.

![](<Base64-Image-Removed>)

It required a bit of massaging but there you have it!

![](<Base64-Image-Removed>)

And scrolling back down to double check to see on our _null_ values:

![](<Base64-Image-Removed>)

Next week, we will navigate through the meta data to retrieve the field names.

_Tune in next week for more Power BI Tips._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-just-speculate-over-numbers-part-2/#0 "close")

top