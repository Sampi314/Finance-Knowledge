# Power Query: Learn by Example

**Source:** https://sumproduct.com/blog/power-query-learn-by-example/

---

[Home](https://sumproduct.com/)

\> Power Query: Learn by Example

*   October 29, 2019

Power Query: Learn by Example
=============================

Power Query: Learn by Example
=============================

30 October 2019

_Welcome to our Power Query blog. Time for more on my favourite feature – Column From Examples._

People may think they would need to know Power Query very well to sort out the following table of data from my fictional tent hire business:

![](<Base64-Image-Removed>)

I am going to transform this data without needing to know any **M** code, and by using only one function! In fact, I am going to learn some **M** code along the way…

My first step is to extract this data to Power Query using ‘From Table’ on the ‘Get & Transform’ section of the Data tab:

![](<Base64-Image-Removed>)

My table has headers and the range is correct, so I accept the defaults.

![](<Base64-Image-Removed>)

I need to format my data consistently, so I begin by looking at the **Client Name** column. I am going to use ‘Column From Examples’ from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I want the names to be in the format ‘J. Smith’, where ‘J’ is the first initial and ‘Smith’ is the surname. One example is not enough, so I enter more.

_![](<Base64-Image-Removed>)_

I can see from my data that after two examples, I have the names in the format I wanted. I click OK to apply this to my data.

![](<Base64-Image-Removed>)

Now I consider the dates. I have a full Date/Time format, but instead of 15/10/2019 00.00… I would like to see 15/10 Tues. I use ‘Column from Examples’ again.

![](<Base64-Image-Removed>)

After two examples, I have my formatting.

![](<Base64-Image-Removed>)

Now I want to extract the products from the **Products Ordered** column, as I don’t need the quantities. This time, I give the more complex examples.

_![](<Base64-Image-Removed>)_

The results look good, so I move onto the next column.

![](<Base64-Image-Removed>)

The address is in one long string, and I want to format it.

![](<Base64-Image-Removed>)

I want to extract the street, but if I try to extract and separate the fields using ‘Column From Examples’, Power Query doesn’t have enough to work with. This doesn’t mean I have to abandon my plan to only use ‘Column From Examples’; I can do it – but in stages.

_![](<Base64-Image-Removed>)_

Now I can separate my street names.

![](<Base64-Image-Removed>)

I can now go back and extract the post code.

![](<Base64-Image-Removed>)

I find I need to use two steps for this too.

![](<Base64-Image-Removed>)

Now I have all my data, which has been transformed by using ‘Column From Examples’.

![](<Base64-Image-Removed>)

I haven’t written any **M** code, but I can learn from the code that Power Query has created for me. If I want to view the code behind a step, I can use the cog icon next to that step. (If there is no cog icon, then the step can be displayed in the Formula bar at the top of the screen, so I just need to select the appropriate step.)

![](<Base64-Image-Removed>)

I can also use the ‘Advanced Editor’ to view all the **M** code for this query.

![](<Base64-Image-Removed>)

This actually looks like:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table2″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Client Name “, type text}, {“Address”, type text}, {“Products Ordered”, type text}, {“Date”, type datetime}}),**

    **#”Added Custom Column” = Table.AddColumn(#”Changed Type”, “Custom”, each let splitClientName = List.Reverse(Splitter.SplitTextByDelimiter(“, “, QuoteStyle.None)(\[#”Client Name “\])), splitClientName2 = Splitter.SplitTextByDelimiter(“, “, QuoteStyle.None)(\[#”Client Name “\]), splitsplitClientName20 = List.Reverse(Splitter.SplitTextByDelimiter(” “, QuoteStyle.None)(splitClientName2{0}?)) in Text.Combine({Text.Start(splitClientName{0}?, 1), “. “, splitsplitClientName20{0}?}), type text),**

    **#”Renamed Columns” = Table.RenameColumns(#”Added Custom Column”,{{“Custom”, “Formatted Name”}}),**

    **#”Added Custom Column1″ = Table.AddColumn(#”Renamed Columns”, “Custom”, each Text.Combine({DateTime.ToText(\[Date\], “dd”), “/10 “, DateTime.ToText(\[Date\], “ddd”)}), type text),**

    **#”Renamed Columns1″ = Table.RenameColumns(#”Added Custom Column1″,{{“Custom”, “Formatted Date”}}),**

    **#”Added Custom Column2″ = Table.AddColumn(#”Renamed Columns1″, “Custom”, each let splitProductsOrdered = Splitter.SplitTextByDelimiter(” “, QuoteStyle.None)(\[Products Ordered\]) in Text.Combine(List.Alternate(splitProductsOrdered, 1, 1, 0), ” “), type text),**

    **#”Renamed Columns2″ = Table.RenameColumns(#”Added Custom Column2″,{{“Custom”, “Product Names Ordered”}}),**

    **#”Added Custom Column3″ = Table.AddColumn(#”Renamed Columns2″, “Custom”, each let splitAddress = Splitter.SplitTextByCharacterTransition((c) => not List.Contains({“0”..”9″}, c), {“0”..”9″})(\[Address\]) in Text.Reverse(Text.Middle(Text.Reverse(splitAddress{0}?), 2)), type text),**

    **#”Added Custom Column4″ = Table.AddColumn(#”Added Custom Column3″, “Custom.1”, each let splitCustom = Splitter.SplitTextByCharacterTransition({“0”..”9″}, (c) => not List.Contains({“0″..”9″}, c))(\[Custom\]) in Text.Combine(splitCustom, ” “), type text),**

    **#”Added Custom Column5″ = Table.AddColumn(#”Added Custom Column4″, “Custom.2”, each let splitCustom1 = Splitter.SplitTextByCharacterTransition({“a”..”z”}, {“A”..”Z”})(\[Custom.1\]) in Text.Combine(splitCustom1, ” “), type text),**

    **#”Renamed Columns3″ = Table.RenameColumns(#”Added Custom Column5″,{{“Custom.2”, “Street Address”}}),**

    **#”Removed Columns” = Table.RemoveColumns(#”Renamed Columns3″,{“Custom”, “Custom.1”}),**

    **#”Added Custom Column6″ = Table.AddColumn(#”Removed Columns”, “Custom”, each let splitAddress = Splitter.SplitTextByCharacterTransition({“a”..”z”}, {“A”..”Z”})(\[Address\]) in splitAddress{2}?, type text),**

    **#”Added Custom Column7″ = Table.AddColumn(#”Added Custom Column6″, “Custom.1″, each Text.Combine({Text.Reverse(Text.Middle(Text.Reverse(\[Custom\]), 3)), ” “, Text.End(\[Custom\], 3)}), type text),**

    **#”Renamed Columns4″ = Table.RenameColumns(#”Added Custom Column7″,{{“Custom.1”, “Post Code”}}),**

    **#”Removed Columns1″ = Table.RemoveColumns(#”Renamed Columns4″,{“Custom”})**

**in**

    **#”Removed Columns1″**

Apart from a few renames and removals which I did to make the transformations easier to see, this **M** code has been written by ‘Column From Examples’. So it’s easy to write **M** code after all!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-learn-by-example/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-learn-by-example/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-learn-by-example/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-learn-by-example/#0)

[](https://sumproduct.com/blog/power-query-learn-by-example/#0 "close")

top