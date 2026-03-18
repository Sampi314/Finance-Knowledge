# Power BI Blog: Xenagogue to Markup Lists – Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-xenagogue-to-markup-lists-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Xenagogue to Markup Lists – Part 2

*   April 18, 2018

Power BI Blog: Xenagogue to Markup Lists – Part 2
=================================================

Power BI Blog: Xenagogue to Markup Lists – Part 2
=================================================

19 April 2018

Welcome back to Power BI Tips!

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/xenagogue-to-markup-lists-part-1)
 we started the import process for an XML format file from the Reserve Bank of Australia’s RSS feed. We’ve just hit “Edit” and will enter the Power Query Editor to perform some transformations on the data to make it usable.

![](https://sumproduct.com/wp-content/uploads/2025/05/78b43893f6080ab6a848887e442b1db4.jpg)

Notice how in the data, several columns contain _Table_ data. This is how Power Query parses through the XML file. Each branch of the tree is stored in tables and we will need to drill down to access the data on the leaves.

There is a special expansion arrow on the right of the column header which is used to expand the _Table_ data. The headers aren’t named exactly like the leaves we saw in the raw text of the XML file. This is why we need to review the documents first, so we know that we want to access the fourth branch to retrieve **<cb:statistics>**.

We will ignore the columns that just have text. These are the leaves in this particular branch but we need to drill down further. To traverse the branches we need to focus on the columns that have Tables. In this case, the fourth branch is called **http: //www.cbwiki.net/wiki/index.php/Specification\_1.2/**. Remove the other columns and then press the expansion arrow.

![](https://sumproduct.com/wp-content/uploads/2025/05/0cfe58018bda7e52204899ae51d7fcfd.jpg)

Great! The statistics are clearly buried in there. Click “OK” to expand.

The reason why the “**cb:**” portion as indicated in the tag is not included in the column header is because anything before the colon indicates the parent. **<cb:statistics>** would be interpreted as _statistics,_ which is a child of _cb_.

It’ll bring up more rows of tables but we’ll expand to get the 4th branch, the **<cb:exchangeRate>**.

![](https://sumproduct.com/wp-content/uploads/2025/05/7fc95dbfaf228fa6bf46eb922e08565c.jpg)

Once expanded, it will look like this:

![](<Base64-Image-Removed>)

Click the expansion arrow again and we will see the information we were seeking.

![](<Base64-Image-Removed>)

Upon expansion, select everything except for the first item as it describes the data we are looking for. We have finally found the leaves on the tree we were looking for.

![](<Base64-Image-Removed>)

Let’s zoom into the exchange rate of the XML document and have a closer look at how the data is stored.

![](<Base64-Image-Removed>)

**<cb:observation>** holds the actual values of the exchange rate, but **<cb:observationPeriod>** holds the date.

Let’s expand both of these, expanding **value** from the **observation** column and **period** from the **observationPeriod** column.

![](<Base64-Image-Removed>)

Looks pretty good!

We’re only interested in the **value**, **targetCurrency** and **period** columns. We can remove all the other columns and I’m going to rename mine **Exchange Rate**, **Currency**, and **Date** respectively.

![](<Base64-Image-Removed>)

Final thing to do is to change **Date** into date format. We can simply click the icon on the left of the column header to change the type:

![](<Base64-Image-Removed>)

And our final query result looks like this:

![](<Base64-Image-Removed>)

Now that our dataset is tided up nicely just hit “Close & Apply”!

It can get quite time consuming exploring the structure of an XML file and navigating it in the Power Query Editor isn’t 100% intuitive given that the column headers might not be identical to the tags and other bits of html information may be included. However it is worth doing as RSS/XML feeds is one of the standard mediums for accessing and retrieving data online.

Next week, we’ll look at using this data in a visualisation to display in a report.

Tune in next time for more Power BI Tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-xenagogue-to-markup-lists-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-xenagogue-to-markup-lists-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-xenagogue-to-markup-lists-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-xenagogue-to-markup-lists-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-xenagogue-to-markup-lists-part-2/#0 "close")

top