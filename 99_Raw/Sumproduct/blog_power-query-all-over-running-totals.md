# Power Query: All Over Running Totals

**Source:** https://sumproduct.com/blog/power-query-all-over-running-totals/

---

[Home](https://sumproduct.com/)

\> Power Query: All Over Running Totals

*   February 9, 2021

Power Query: All Over Running Totals
====================================

Power Query: All Over Running Totals
====================================

10 February 2021

_Welcome to our Power Query blog. This week, I return to the running totals example from last week, to apply a more complex solution._

[Last week](https://sumproduct.com/blog/power-query-keep-on-running/)
, I looked at using **List.Buffer()** to speed up the running total calculation, so that the list created by **List.Range()** was buffered and not unnecessarily recalculated each time.

![](<Base64-Image-Removed>)

Whilst the list of values were buffered, the index count was not, and this too added to the time taken to perform the calculation. Maintaining the position on the index column to calculate the correct list is a difficult concept to buffer. Instead, I will look at another method to create a running total.

The **M** function I will use to drive this is **List.Generate()**:

**List.Generate(initial** as function, **condition** as function, **next** as function, optional **selector** as nullable function**)** as list

This generates a list of values given four functions that generate the initial value **initial**, test against a condition **condition**, and if successful, select the result and generate the next value **next**. An optional parameter, **selector**, may also be specified. This function creates list entries based on a starting value and conditions. The process loops until the list is complete.

I will create a new query, which I will be identifying as a function.

![](<Base64-Image-Removed>)

I start from the ‘Get & Transform’ section of the Data tab, where I opt to create a New Query. From the dropdown, I select ‘From Other Sources’, and then ‘Blank Query’. I access the Advanced Editor and enter the **M** code I need, to create a running total function that will work on any list of number values.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**(values as list) as list =>**

**let**

   **RT = List.Generate ( () => \[RT = values{0}, counter = 0\],**

                              **each \[counter\] < List.Count(values),**

                              **each \[RT = \[RT\] + values{\[counter\] + 1}, counter = \[counter\] + 1\],**

                              **each \[RT\] )**

**in**

    **RT**

Essentially, this takes a list of values, and instead of an index column, it uses a counter to work through the list creating a running total (**RT**) and then increments the counter to move to the next value in the list.

If I click ‘Done’ in the Advanced Editor, my new query is created; I will call it **FxRunningTotal**.

![](<Base64-Image-Removed>)

I can now use this in my original query.

![](<Base64-Image-Removed>)

I make a duplicate of my query so that I can compare the results.

![](<Base64-Image-Removed>)

I remove all the steps from ‘Added Index’ downwards.

![](<Base64-Image-Removed>)

I will now add my function using the Advance Editor.

The **M** code is currently:

**let**

    **Source = Table.NestedJoin(ACCT\_Order\_Charges,**

                                    **{“Item\_Key”},**

                                           **Items,**

                                    **{“Item\_Key”},**

                                     **“NewColumn”,**

                             **JoinKind.LeftOuter),**

**//single comment line**

    **#”Expanded NewColumn” = Table.ExpandTableColumn(Source, “NewColumn”, {“Item\_Group”}, {“NewColumn.Item\_Group”}),**

**/\* comment section**

   **with many lines \*/**

    **#”Renamed Columns” = Table.RenameColumns(#”Expanded NewColumn”,{{“NewColumn.Item\_Group”, “Item\_Group”}}),**

    **#”Sorted Rows” = Table.Sort(#”Renamed Columns”,{{“Order\_Key”, Order.Ascending}, {“Order\_Line\_Number”, Order.Ascending}}),**

    **#”Inserted Multiplication” = Table.AddColumn(#”Sorted Rows”, “Order\_Line\_Number x Amount”, each List.Product({\[Order\_Line\_Number\], \[Amount\]}), Int64.Type),**

    **#”Removed Columns” = Table.RemoveColumns(#”Inserted Multiplication”,{“Order\_Line\_Number x Amount”})**

**in**

    **#”Removed Columns”**

After step #”Removed Columns” I add the following lines:

  **BufferedValues = List.Buffer(#”Removed Columns”\[Amount\]),**

  **RT = Table.FromList(FxRunningTotal(BufferedValues),Splitter.SplitByNothing(),{RT}),**

  **Columns = List.Combine({Table.ToColumns( #”Removed Columns”), Table.ToColumns(RT)}),**

  **ConvertToTable = Table.FromColumns(Columns,List.Combine({Table.ColumnNames(#”Removed Columns”), {“Running Total”}}))**

The new lines create a buffer, then create a table with the running total in it. As I have other columns, I then need to get my columns and combine them with the new **Running Total** column, and then convert it all back to a table. Finally, I change the ‘in’ statement to reflect the last step. I click ‘Done’ to commit the new steps:

![](<Base64-Image-Removed>)

My running total appears. The next test is to load it into Excel:

![](<Base64-Image-Removed>)

The load was significantly quicker!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-all-over-running-totals/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-all-over-running-totals/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-all-over-running-totals/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-all-over-running-totals/#0)

[](https://sumproduct.com/blog/power-query-all-over-running-totals/#0 "close")

top