# Excel for Mac: no Fuzzy Merge in Power Query? How to Ignore Case when Merging Queries.

**Source:** https://sumproduct.com/blog/excel-for-mac-no-fuzzy-merge-in-power-query-how-to-ignore-case-when-merging-queries/

---

[Home](https://sumproduct.com/)

\> Excel for Mac: no Fuzzy Merge in Power Query? How to Ignore Case when Merging Queries.

*   July 4, 2024

Excel for Mac: no Fuzzy Merge in Power Query? How to Ignore Case when Merging Queries.
======================================================================================

Excel for Mac: no Fuzzy Merge in Power Query? How to Ignore Case when Merging Queries.
======================================================================================

5 July 2024

_This week in our series about Microsoft Excel for Mac, we show you how to merge queries when you have text fields that would be good for a Fuzzy merge in Power Query, even though that feature doesn’t exist on Mac._

Power Query on Windows lets you choose [Fuzzy merge](https://sumproduct.com/blog/power-query-fuzzy-matching/)
 options when merging queries. It’s useful for merging based on columns that have similar values that may not match exactly. You can specify the similarity threshold (fuzziness) and other options for matches between values. Unfortunately, this feature isn’t available in Excel for Mac as of June 2024.

The screen shot below shows how to start merging queries.

![](https://sumproduct.com/wp-content/uploads/2025/05/ed30888fa5d58f89a97e04469d1aac58-1.jpg)

**_Ignore case when Merging_**

One of the useful and commonly used options of the Fuzzy merge is to do a case-insensitive match on columns with text values. If you’re trying to find the option to ignore case in your merge on Mac, you won’t find it. The screen shot below shows the fuzzy matching option with ‘Ignore case’ in Excel for Windows.

![](https://sumproduct.com/wp-content/uploads/2025/05/b85783caeb9d99c86759e4fbc2e2c4d1-1.jpg)

**_Fuzzy merge workaround_**

The good news is that you can accomplish the same outcome on Mac with just a few extra steps, which we’ll show in detail. They’re very straightforward.

*   Set the case on the appropriate columns so they’ll be consistent.
*   Merge the queries using those columns, knowing that you don’t need Fuzzy merge.

**_How to set it up_**

Suppose you have a query with sales for your products, and one with your product list, which includes a category name. If you want to show the category name along with Sales data, you can merge the queries. However, the product names in the Sales table are inconsistent with regard to case. Some may be lowercase, some all caps, and some capitalized. You may not care about the case when it comes to merging the queries, but Power Query does, because it’s case-sensitive by default. Therefore, if your product is “bikes” in one table and “Bikes” in the other, they wouldn’t match, and the rows wouldn’t be combined in the merge.

For example, in this screen shot, you can see that “handlebars” is lowercase in one table, and begins with capital “H” in the other. Without Fuzzy match, these won’t match.

![](<Base64-Image-Removed>)

You can use Home > ‘Merge queries’, but it may show that none of the records match as in the screen shot below. The merge is using the Product field from both queries, but since one has all lower case, and the other seems to have capitalized product names, there are no matches (0 of 75 rows).

![](https://sumproduct.com/wp-content/uploads/2025/05/a254b1cbb0daed8124ed5b278133bab8-1.jpg)

Since that won’t work, we need to do a few things to our queries first. We can either transform the **Product** column in both queries so that it shows a consistent case in both, such as “Proper” case, or we can create new columns with a consistent case. In our example, we’ll transform the column in one query, and create a new column in the other so you learn how to do both methods.

First, we’ll add a new column to the **Sales** query. By adding a new column, we preserve the original column in case we want to use it later. The steps are simple. Just click Add Column > Format > Capitalize Each Word. This creates a new column we call **ProperProduct** in our example.

![](https://sumproduct.com/wp-content/uploads/2025/05/3d9b25caba5f605890ffb8f680226d3e-1.jpg)

The screen shot below shows the new column and you can see the **M** Code in the Formula Bar.

![](<Base64-Image-Removed>)

The code is below. We used **ProperProduct** as the column name.

**Table.AddColumn(#”Changed column type”,** **“ProperProduct”****,** **each** **Text.Proper(\[Product\]),** **type** **nullable** **text****)**

In the **ProductCategories** query, we’ll transform the column rather than add a new column. The steps are also very easy. Just highlight the **Product** column, then choose Transform > Format >’Capitalize Each Word’. This just capitalizes each word in the values without adding a new column.

![](<Base64-Image-Removed>)

Here we can see what happens when we try to merge using the original **Product** column in the **SalesTable** query. Since we changed the **Product** column in the **ProductCategories** query to Proper case, we get some matches. However, there are still some rows that don’t have a match, which you can see from the status bar in the Merge dialog. In our example, it shows that only 72 of 75 rows have a match. We expect all products to have a category, so all 75 should match.

![](<Base64-Image-Removed>)

Since we added the **ProperProduct** column, we can use that in the merge, and it shows that we get a match for all the rows in the **Sales** table, which is what we want (every product has a category).

![](<Base64-Image-Removed>)

To finish creating the merge, just click OK. The **ProductCategories** column can be expanded by clicking on the Expand button in the column header. Since we only need the **Category** column, we deselect the other columns and press OK, and we’re done.

![](<Base64-Image-Removed>)

We just created our own type of fuzzy merge, even though the real ‘Fuzzy merge’ feature wasn’t yet available in Power Query on Mac.

We hope you find this topic helpful. Check back for more details about Excel for Mac and how it’s different to Excel for Windows.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/excel-for-mac-no-fuzzy-merge-in-power-query-how-to-ignore-case-when-merging-queries/#0)
    
*   [Register](https://sumproduct.com/blog/excel-for-mac-no-fuzzy-merge-in-power-query-how-to-ignore-case-when-merging-queries/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/excel-for-mac-no-fuzzy-merge-in-power-query-how-to-ignore-case-when-merging-queries/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/excel-for-mac-no-fuzzy-merge-in-power-query-how-to-ignore-case-when-merging-queries/#0)

[](https://sumproduct.com/blog/excel-for-mac-no-fuzzy-merge-in-power-query-how-to-ignore-case-when-merging-queries/#0 "close")

top