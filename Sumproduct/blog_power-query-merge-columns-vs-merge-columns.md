# Power Query: Merge Columns vs Merge Columns

**Source:** https://sumproduct.com/blog/power-query-merge-columns-vs-merge-columns/

---

[Home](https://sumproduct.com/)

\> Power Query: Merge Columns vs Merge Columns

*   November 20, 2018

Power Query: Merge Columns vs Merge Columns
===========================================

Power Query: Merge Columns vs Merge Columns
===========================================

21 November 2018

_Welcome to our Power Query blog. This week, I look at merging columns to show that not all ‘Merge Columns’ options are born equal._

There are currently some problems that can occur when merging columns. To demonstrate, I will use the following subset of my tent data:

![](<Base64-Image-Removed>)

I want to create a new column which will contain all of my dimension data.

![](<Base64-Image-Removed>)

In the ‘Transform’ data tab, I can choose to merge columns. First, I must select them, which I can do by holding down the **CTRL** key as I click on them.

![](<Base64-Image-Removed>)

I have selected all the columns containing dimensional data, then I choose to merge:

![](<Base64-Image-Removed>)

I choose to separate my data by commas, and I call my new column **_Dimensions_**.

![](<Base64-Image-Removed>)

I have several problems here:

1.  My original columns have disappeared
2.  The data is not in the order I would have expected
3.  There are extra commas.

The first problem could be resolved by copying my columns before I merge them:

![](<Base64-Image-Removed>)

In the ‘Add Column’ tab, I can create a duplicate of the selected column. I have to do this one column at a time, but having created the duplicates I can select them instead of the original columns.

Surprisingly, there is an easier way – I can merge columns from the ‘Add Column’ tab instead:

![](<Base64-Image-Removed>)

I can merge columns here too, but the process behaves slightly differently.

![](<Base64-Image-Removed>)

This part looks the same, I pick the separator and the name of my new column.

![](<Base64-Image-Removed>)

However, this time I get to keep my original columns. Confusing, but useful when I know that ‘Merge Columns’ on the ‘Transform’ tab deletes the original columns, whereas ‘Merge Columns’ from the ‘Add Column’ tab keeps the originals.

They are still in the wrong order though, and now I can see my original columns, I can work out the order. The merge is constructed in the order in which I select my columns. I selected **_colour_** first and worked backwards, so my merge does too. I can rectify this by selecting my columns in the order I want them to merge.

![](<Base64-Image-Removed>)

Having selected **_Length_**, I can select my remaining columns in the right order by holding down the **SHIFT** key and then selecting **_colour_**. This is quicker and will ensure the order is right.

![](<Base64-Image-Removed>)

Having created my merge (from the ‘Add Column’ tab), I check the order again.

![](<Base64-Image-Removed>)

The order is correct, and looking more closely, my last problem (extra commas) has also been resolved! This is because there are more differences to the way the ‘Merge Columns’ option on the ‘Add Column’ tab works compared to the ‘Transform’ tab. To show the difference in the results, I will merge the columns from the ‘Transform’ tab:

![](<Base64-Image-Removed>)

I give the column a different name so I can see what is happening.

![](<Base64-Image-Removed>)

The ‘Merge Column’ from the ‘Transform’ tab does not cope with the nulls, but the ‘Merge Column’ from the ‘Add Column’ tab does!

![](<Base64-Image-Removed>)

The answer to this discrepancy is in the Advanced Editor, where I can see what each ‘Merge Columns’ has done in **M**.

Firstly, consider the ‘Transform’ tab version:

**#”Merged Columns” = Table.CombineColumns(#”Inserted Merged Column”,{“Length”, “width”, “height”, “volume”, “temperature”, “colour”}, Combiner.CombineTextByDelimiter(“,”, QuoteStyle.None),”Dimensions (from Transform)”)**

This version of the merge has created a new column using the **M** function **Combiner.CombineTextByDelimiter**. Clearly, this function does not cope with nulls.

The ‘Add Column’ tab version has used a different **M** function:

**#”Inserted Merged Column” = Table.AddColumn(#”Changed Type”, “Dimensions”, each Text.Combine({\[Length\], \[width\], \[height\], \[volume\],\[temperature\], \[colour\]}, “,”), type text)**

This time, the **M** function used is **Text.Combine**, which does cope with the nulls.

This does leave the question of whether the ‘Add Column’ merge column feature will cope equally well with numerical columns…

![](<Base64-Image-Removed>)

The answer is yes, the price is included too, and looking at the **M** code, I can see why:

**\= Table.AddColumn(#”Changed Type”, “Details from Add Column”, each Text.Combine({\[Length\], \[width\], \[height\], \[volume\], \[temperature\], Text.From(\[Price\], “en-GB”), \[colour\]}, “,”), type text)**

The price is converted to text so that it can be combined with the other columns.

In summary, if merging columns, it’s currently best to do so from the ‘Add Column’ tab. It keeps the original columns and copes with nulls. This is correct at the time of writing, but I wouldn’t be surprised to find that the ‘Transform’ tab is soon updated to use the same functionality for the ‘Merge Columns’ option. I still have to remember to add the columns in the order I want to merge them, but allowing that functionality means that I don’t need to reorder my columns if I do need them to be merged in a different order.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-merge-columns-vs-merge-columns/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-merge-columns-vs-merge-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-merge-columns-vs-merge-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-merge-columns-vs-merge-columns/#0)

[](https://sumproduct.com/blog/power-query-merge-columns-vs-merge-columns/#0 "close")

top