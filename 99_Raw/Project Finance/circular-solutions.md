# Suite of Circular Reference Solutions

**Source:** https://edbodmer.com/circular-solutions

---

In this page I suggest alternative solutions to the circular reference problem using a suite of solutions. I do not suggest there is only one ideal solution for one circular reference problem. One of the solution is the old fashioned copy and paste macro where you create a calculated row, a fixed row and the difference (you can create a whole lot of rows if you want). If you have a unique problem with a whole lot of unconventional equations I would begin with the copy and paste macro before attempting the UDF approach. If you have a project financed investment with a single debt issue and you only want to solve the funding circular reference (i.e. the IDC, Fees and DSRA) with a UDF, you do not have to implement the large UDF solution with a template model. Instead, you can use the process below and practice with a couple of examples to solve the problem. If you have an LBO model or a corporate model where the circular reference comes about from averaging interest expense, you can use a relatively simple UDF approach. But if you have a whole lot of debt issues with things like standby debt, LC fees on un-funded equity, VAT debt, Equity bridge loans and other items, then you may want to implement the comprehensive solution using the template. If you have a big monster model, then I suggest with a goal seek combinded with a copy and paste model then I demonstrate how a user defined function can dramatically improve the speed of the model relative to a copy and paste approach (in all of this discussion I assume that the using the iterative button is not acceptable).

The files attached to the buttons on this page include some examples that show how basic copy and paste macros work as well as how the you can write your own UDF code for more simple cases.

.

.

**[Template UDF Parrallel Model that You Can Put Directly in Your Model By Pressing Button and then Following Instructions](https://edbodmer.com/wp-content/uploads/2024/01/Updated-Template.xlsm)
**

.

**[Excel File with Examples of UDF in Acquistion Model and Illustration of Algebra in Solving Circular References](https://edbodmer.com/wp-content/uploads/2024/01/Circular-with-Acquisition-Model.xlsm)
**

.

.

I have continued to work on making my process for resolving the copy and paste time problem more efficient. The big problem these days can be the time it takes to resolve the copy and paste. The UDF system that I have developed works by reading things from your excel model into a UDF which is just a computer program. After you read things into the UDF you can do all the math outside of Excel (sometimes in project finance models you have to do a lot of math). In the computer program without all of the excel stuff that slows you down, the process takes seconds instead of minutes (a factor sometimes of 60 times less). Then you can put the results of the math back into the excel program and you have a dramatically more efficient process.

.

Video Player

[https://edbodmer.com/wp-content/uploads/2025/08/UDF-Revised-Case.mp4](https://edbodmer.com/wp-content/uploads/2025/08/UDF-Revised-Case.mp4)

00:00

00:00

05:14

[Use Up/Down Arrow keys to increase or decrease volume.](javascript:void(0);)

.

Video Player

[https://edbodmer.com/wp-content/uploads/2025/08/Benchmarking-3.mp4](https://edbodmer.com/wp-content/uploads/2025/08/Benchmarking-3.mp4)

00:00

00:00

00:00

[Use Up/Down Arrow keys to increase or decrease volume.](javascript:void(0);)

..

.

.

Copy and Paste Macro
--------------------

I hope to have an open mind about some things. There are clearly some situations where you should use the old fashioned copy and paste macro. Further, because of the closed minded nature of auditors, you will probably want to show the copy and paste solution next to the UDF solution. The big deal with copy and paste is to use the .VALUE when you refer to a range. I know that some people put the copy and paste solution in a different page, but I suggest you lay out the key areas where the copy and paste will be necessary. In a project finance model, I suggest a table with sources and uses laid out clearly. The screenshot below illustrates what I am talking about:

The file with both the UDF and the copy and paste solution in included in the file attached to the button below.

I have found that some people are very good at the bureacuracy with using the .VALUE and then putting the copy and paste in a separate sheet. But they make a complete mess. People compute circular references on future DSCR tests when sizing debt; they make the whole process very difficult to follow.

.

Extremely Simple Example with UDF
---------------------------------

The very simple example that I use is one with fees during construction. I make this example where the fees do not depend on accumulated debt but only on the debt issued in one period. This is cheating and the problem can be solved with simple algebra (Total = Total without fees/(1-fee percent)). But I find this example a good way to illustrate the UDF compared to the copy and paste method.

![](https://edbodmer.com/wp-content/uploads/2021/12/image-5.png)

.

Goal Seek and Data Table Works

.

![](https://edbodmer.com/wp-content/uploads/2021/12/image-6.png)

    
    .
    
    Function fees1(fee_pct, debt_pct, cap_exp)
    
    difference = 999
    Count = 1
    
    Do While difference <> 0
       
       Count = Count + 1
       
       last_fees = fees1
       
       total_funding = cap_exp + fees1
       debt_draws = total_funding * debt_pct
       fees1 = fee_pct * debt_draws
       
       difference = last_fees - fees1
    
       If Count > 100 Then Exit Do
    
    Loop
    
    
    End Function
    

.

Examples where Circular References Do Not Depend on Accumulated Amounts – Corporate Model and LBO Model
-------------------------------------------------------------------------------------------------------

The most common problems with circular references in general models are the surplus financing problem and the average interest expense or interest expense problem. In these problems the financing must be re-computed and if taxes depend on financing, then the taxes must be also computed.

.

.

Reading Variables from a Large Block So you Do Not Have to Define Separate Variables in the Function
----------------------------------------------------------------------------------------------------

.

Over time the UDF was applied to more and more complex models which meant the number of variables increased exponentially. For example, if three debt issues are included in a project finance model, there are three interest rates, three commitment fees, three up-front fees, three methods for repaying the debt as well as a required method to deal with sculpting for multiple debt issues. The complexity raised three issues. These issues and their resolution are:

*   The first issue was reading a large number of variables into the UDF. When each variable was read into the UDF the process was tedious and led to a limitation in the number of characters that were allowed to be read into a function. The issue was resolved by reading an entire page of structured data into the UDF into a large single array. Once the array is read into the UDF the data is assigned to separate variables using variable names defined in the input page.  The input page that is used to put data into a large array is shown in the first screenshot below.  The programming that reads in a very large array and then separates the array into different variables is shown in the second screenshot.

This shows a simple example of reading a block. There is a function that reads in the two lines name A and B. In this case only the data is read in. In our examples the entire line is read in. When you read in the data make sure to put in one name that is defined as an array. Note that you do not have to define the array. Once you read in the array, split it up to the rows. Then you can make some calculations.

Finally, you can put the output in a block. Define the output block with rows and columns. You need both even if there is one row and/or one column. Then, finally define the name of the function as the output. Of course output can be named something else.

.

![](https://edbodmer.com/wp-content/uploads/2023/02/image-1.png)

.

    Option Base 1
    Option Explicit
    
    Function Marc(Inputs2 As Variant) As Variant
    
    Dim A(300), B(300) As Double
    Dim TotalRows, TotalCols, Col, output(3, 3) As Double
    
    TotalRows = Inputs2.Rows.Count
    TotalCols = Inputs2.Columns.Count
    
    'MsgBox TotalRows
    
    For Col = 1 To TotalCols
    
        A(Col) = Inputs2(1, Col)
        B(Col) = Inputs2(2, Col)
        
        output(1, Col) = A(Col) * 2
        output(2, Col) = B(Col) / 2
        output(3, Col) = A(Col) * B(Col)
    
    Next Col
    
    Marc = output
    
    
    End Function

.

The code below is an extract from the template model that resolves circular references in a complex project finance model.

![](https://edbodmer.com/wp-content/uploads/2025/05/image-2.png)

.

    Function Circular_resolution(UDFinputs As Variant) As Variant  ' operational_inputs defined here
    
    '  Here is where you read in all the cells in the sheet to a big array.
    
        Number_of_Rows_Read = UDFinputs.Rows.Count         ' Count the number of rows from your area or input
                                                                                                                         
        For Row = 1 To Number_of_Rows_Read      ' first loop around the rows with i counter.       
           For Column = 1 To number_of_cols  ' Go around columns.  You can change this to make the program run faster.
              
              CELLS_IN_INPUT_SHEET(Row, Column) = UDFinputs(Row, Column)   
           
           Next Column
        Next Row
     
     '
     '  The next two functions are for Reading and assigning the variables
     '
     
        Find_Variables_Function                 
      
    ' Initialise the output variable which is for the report -- this is the output of the function
        
        max_columns = 500
            
        For i = 1 To max_columns          '1000 is the maximum number of cloumns in the output
            For j = 1 To 1000      '5000 is the maximum number of rows in the output
                output(j, i) = ""
            Next j
        Next i
    

.

Use of Template with Complex Models
-----------------------------------

I have spent much more time developing a template that can solve complex project finance problems.

The initial file includes the UDF template that we update on a regular basis. Finally, if you are adding re-financing to a model, I suggest an alternative and separate UDF to the large one. Before describing some of the mechanics of the UDF versus the copy and paste method, I review a little history of how I have derived the method.

![](https://edbodmer.com/wp-content/uploads/2021/12/image-4.png)

Circularity from Sculpting and Re-financing
-------------------------------------------

Re-financing is after. Re-financing involves sculpting. Re-financing can occur multiple times.

Do the re-financing at the end.

Need a medium number of inputs — the EBITDA, the depreciation, the tax rates, the timing of the re-financing, the initial NOL, the term of the new finncing, the interest rates on the new financing.

Retaining Values from Copy and Paste from Scenario
--------------------------------------------------

.

    <code>Range("comit_fee_output").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Select Range("comit_fee_output").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Value = Range("comit_fix").Value If debug2 = True Then MsgBox " Copying Commitment Fee to the Sensitivity Page " Range("ACT_FIXED_CIRC").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Select Range("ACT_FIXED_CIRC").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Value = Range("Fixed_Act").Value Range("Def_Int_Start").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Select Range("Def_Int_start").Value = Range("fixed_int_def").Value</code>

         Range("comit_fee_output").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Select
         Range("comit_fee_output").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Value = Range("comit_fix").Value
                    If debug2 = True Then MsgBox " Copying Commitment Fee to the Sensitivity Page "
    
         Range("ACT_FIXED_CIRC").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Select
         Range("ACT_FIXED_CIRC").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Value = Range("Fixed_Act").Value
    
        Range("Def_Int_Start").Range(Cells(Scenario, 1), Cells(Scenario, end_col)).Select
        Range("Def_Int_start").Value = Range("fixed_int_def").Value

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14794&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=14320&rand=0.034200455163212684)