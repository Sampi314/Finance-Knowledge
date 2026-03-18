# How to Count and Sum Filtered Tables

**Source:** https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables

---

Formula Forensics No. 037 – How to Count and Sum Filtered Tables
================================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 24 comments

  

A few weeks ago in the [Chandoo.org Forums](http://chandoo.org/forum/ "Chandoo.org Forums")
, **Jsk\_Lge** asked “[**How do I count the number of items in a filtered list?**](http://chandoo.org/forum/threads/countif-in-a-filtered-list.17753/)
”

Narayan and I helped out with a well publicised Excel formula  
\=SUMPRODUCT(SUBTOTAL(103,OFFSET(A2,ROW(A2:A100)-ROW(A2),0)),(A2:A100=”D”)+0)

Today were going to unravel this and see what makes it tick.

As always at Formula Forensics, you can follow along using an sample file: [Download Here](https://chandoo.org/wp/wp-content/uploads/2014/07/Count-Filtered-Items.xls "Download Sample File")

Formula
-------

The Formula:  
\=SUMPRODUCT(SUBTOTAL(103,OFFSET(A2,ROW(A2:A100)-ROW(A2),0)),(A2:A100=”D”)+0) applied to Jsk’s data

We will use a Similar Formula better suited to our sample set of data

\=SUMPRODUCT(SUBTOTAL(103,OFFSET(C1,ROW(A2:A20)-ROW(A1),0)),–(C2:C20=G1))

[![FF37_1](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_1.png)](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_1.png)

We can see in the data above that there are 9 entries with a Zone of **North** (Orange), 7 entries with a Category of **D** (Yellow), including 3 Entries that have a Zone of **North** and a Category of **D** (Red)

If we filter the data so that Zone = North is selected, we will see there are three entries (Red) that match our criteria and that the three Scores sum to **172** (81+9+82).

[![FF37_2a](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_2a.png)](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_2a.png)

We can see the data is Filtered by the Blue color of the Row Labels, The larger Row Separator and Filter Icon at the Top of the Zone Column, all highlighted in Blue.

Jsk\_Lge’s problem was how to Conditionally Count the Number of entries when the data is Filtered. eg: Category = D when the Zone is equal to North.

For this exercise please ensure the Data Table is filtered so that category North is selected

[![FF37_5](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_5.png)](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_5.png)

Solution
--------

### Count Filtered Entries:

The solution is a Sumproduct based solution.

We know from [Formula Forensics 007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/ "Formula Forensics 007")
 that Sumproduct Sums the Product of the internal arrays.

In our formula: \=SUMPRODUCT(SUBTOTAL(103,OFFSET(A1,ROW(A2:A20)-ROW(A1),0)),–(C2:C20=G1))  
We can see there are two internal arrays  
Array 1: =SUBTOTAL(103,OFFSET(A1,ROW(A2:A20)-ROW(A1),0))  
Array 2: =–(C2:C20=”D”)

Lets look at each in turn:

Array 1: \=SUBTOTAL(103,OFFSET(A1,ROW(A2:A20)-ROW(A1),0))

The Subtotal() returns a subtotal of a list or database. It has the functionality to work with Filtered Tables. The Syntax of the Subtotal() function is shown below:

[![FF37_3](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_3.png)](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_3.png)

Specifically the **Subtotal(103, Array)** is designed to count the number of Visible entries in the array

But in our example the formula only appears to see an array involving Column A, it doesn’t look at our data column, Column C at all?  
This first array is being used to specifically mark, in an array, which Rows are Visible = 1 or Hidden = 0

So what does the OFFSET(A1,ROW(A2:A20)-ROW(A1),0) part do?

The Offset() function is designed to return a range based on the criteria it is given

In this case it will return a range, which will be 1 cell high and 1 cell wide  
It will be Offset from Cell A1 by a formula ROW(A2:A20)-ROW(A1) and in the same column as A1 (,0)

As the Offset formula is inside a Sumproduct Function it will be treated as an Array Formula.  
This means that it will be processed for every value in the range ROW(A2:A20)

ie:  
In Position 1 it will hold ROW(A2)-Row(A1) = 1  
In Position 2 it will hold ROW(A3)-Row(A1) = 2  
In Position 3 it will hold ROW(A4)-Row(A1) = 3  
. . .  
In Position 19 it will hold ROW(A20)-Row(A1) = 19

This will create a vertical array of 1..19 which can then be used by the Offset() function

The Offset Function will take this array of offset values and offsets A1 by each value in turn, in effect creating an Array of Ranges  
ie:  
In Position 1 it will Offset(A1, 1) = A2  
In Position 2 it will Offset(A1, 2) = A3  
In Position 3 it will Offset(A1, 3) = A4  
. . .  
In Position 19 it will Offset(A1, 19) = A5

So the Offset() function is returning an Array of Range Addresses to the Subtotal() function

Once again the Subtotal() function will be be treated as an array function as it is inside the Sumproduct() function.  
This means that the Subtotal() function will be executed for every position in the Array

ie:  
In Position 1 it will hold Subtotal(103, A2)  
In Position 2 it will hold Subtotal(103, A3)  
In Position 3 it will hold Subtotal(103, A4)  
. . .  
In Position 19 it will hold Subtotal(103, A20)

Now this is where the clever part kicks in!

The Subtotal(103, ) function will count the number of **Visible** values in the array  
But as the array is an array of Single cell addresses, A2..A20

So:  
if each value in A2..A20 is Visible it will be counted  
if each value in A2..A20 is Hidden it won’t be counted

Lets check

In the sample file Filter Zone to show North Only

Goto cell **H7** and press **F2**, then **F9**  
Excel will return \={1;0;0;1;1;1;1;1;0;0;0;0;0;0;0;1;0;1;1}

This is showing a value of 1 for each Visible Row and a 0 for each hidden row

Try changing the filters and check the results

Array 2: \=–(C2:C20=G1)

As we have seen in previous Formula Forensics, a simple formula like: –(C2:C20=G1) is a powerful way of adding criteria to a Formula

In this example –(C2:C20=G1) will return an Array of \={0;0;1;1;0;0;0;1;1;1;0;0;0;1;0;1;0;0;0}, but How

In the sample file goto cell **H23** you will see a formula: **\=(C2:C20=G1)**  
Press **F2** then **F9**  
Excel returns: \={FALSE;FALSE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE}

This is an array of True/False where each cell in range C2:C20 is compared to the cell G1  
When they match it is True, When they don’t match it is False

The **– –** part is used to convert this array of True/False’s to an Array of 1/0’s  
In the sample file cell **H26** you will see a formula: \=–(C2:C20=G1)  
Press **F2** then **F9**  
Excel returns: \={0;0;1;1;0;0;0;1;1;1;0;0;0;1;0;1;0;0;0}

Finally We have our two arrays

\=SUMPRODUCT(SUBTOTAL(103,OFFSET(A1,ROW(A2:A20)-ROW(A1),0)),–(C2:C20=G1))  
which equates to :

\=SUMPRODUCT({0;0;1;1;0;0;0;1;1;1;0;0;0;1;0;1;0;0;0} , {1;0;0;1;1;1;1;1;0;0;0;0;0;0;0;1;0;1;1} )

We can now see that Sumproduct will multiply the three arrays and add up the products  
Array 1 {1;0;0;1;1;1;1;1;0;0;0;0;0;0;0;1;0;1;1}  
Array 2 {0;0;1;1;0;0;0;1;1;1;0;0;0;1;0;1;0;0;0}  
Array 1 x Array 2 {0;0;0;**1**;0;0;0;**1**;0;0;0;0;0;0;0;**1**;0;0;0}

Sumproduct correctly returns **3**

[![FF37_4](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_4.png)](https://chandoo.org/wp/wp-content/uploads/2014/07/FF37_4.png)

### Sum Filtered Entries:

Say we wanted to sum the values from the Score field based on Criteria and the Filtered data we can simply add another field to the original Sumproduct() function.

Eg: To sum the Score field whilst using the Criteria and Filtering we simply add a field to the end of the Sumproduct

\=SUMPRODUCT(SUBTOTAL(103,OFFSET(A1,ROW(C2:C20)-ROW(A1),0)),(C2:C20=G1)\*(D2:D20))

We can now see that Sumproduct will multiply the three arrays and add up the products  
Array 1 = {1;0;0;1;1;1;1;1;0;0;0;0;0;0;0;1;0;1;1}  
Array 2 = {0;0;1;1;0;0;0;1;1;1;0;0;0;1;0;1;0;0;0}  
Array 3 = {43;39;87;81;68;42;72;9;51;74;75;17;10;73;48;82;38;58;96}  
Array 1 x Array 2 x Array 3 = {0;0;0;**81**;0;0;0;**9**;0;0;0;0;0;0;0;**82**;0;0;0}

Sumproduct correctly returns **172**

Download
--------

You can download a copy of the above file and follow along, [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2014/07/Count-Filtered-Items.xls "Download Sample File")
.

A Challenge
-----------

Can you solve the Count problem another way ?

Can you solve the Sum problem another way ?

Post your solutions in the comments below.

**[Other Posts in this Series](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensuics Homepage")
  
**
---------------------------------------------------------------------------------------------------------------------

The Formula Forensics Series contains a wealth of useful solutions and information specifically about how Array Formula work.

You can learn more about how to pull Excel Formulas apart in the following posts: [http://chandoo.org/wp/formula-forensics-homepage/](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Hui...  <br>Tags: [row()](https://chandoo.org/wp/tag/row/)<br>, [SUBTOTAL](https://chandoo.org/wp/tag/subtotal/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 24 Responses to “Formula Forensics No. 037 – How to Count and Sum Filtered Tables”

1.  ![](https://secure.gravatar.com/avatar/55ee5c96585607038f0fff07a13508e1c5d6f9e31bf3f93f3190317be0962b26?s=64&d=mm&r=g) [Sumit Bansal](http://www.trumpexcel.com/)
     says:
    
    [July 23, 2014 at 7:44 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578505)
    
    Nice trick there with Subtotal
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578505)
    
    *   ![](https://secure.gravatar.com/avatar/dd13209ee46f605891c5ad2c02cf9f0a960ab3a6accc25230e158379b9c42c00?s=64&d=mm&r=g) pankaj pandey says:
        
        [August 12, 2020 at 5:30 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1851361)
        
        hi can we add multiple criteria  
        pls help me
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1851361)
        
2.  ![](https://secure.gravatar.com/avatar/270b84cfd152229a12ad59e1d5bd7a3b7c3f8e1f7b2fc7e45468bb38d37697fc?s=64&d=mm&r=g) Rob T says:
    
    [July 23, 2014 at 9:51 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578565)
    
    Here's a "helper column" method, which uses the same idea. It also avoids using OFFSET, which is volatile:
    
    (I know we should avoid helper columns where possible, but this is easier to understand and recreate from memory, without referring back to this blog post)
    
    Add a column E to the table with the following formula in E2 and copied down:  
    \=SUBTOTAL(103,$A2)  
    This will return 1 for visible rows and 0 for hidden rows.
    
    Then, the formula for counting the number of visible D's becomes:  
    \=COUNTIFS(C2:C20,"D",E2:E20,1)
    
    And to sum the Scores for visible D's:  
    \=SUMIFS(D2:D20,C2:C20,"D",E2:E20,1)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578565)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 23, 2014 at 2:12 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578677)
        
        @Rob
        
        Although Offset is Volatile, a few or even a few dozen Offset's will not hurt the performance of a worksheet.  
        It is when people use them to make large tables of thousands of cells that the performance degrades.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578677)
        
        *   ![](https://secure.gravatar.com/avatar/270b84cfd152229a12ad59e1d5bd7a3b7c3f8e1f7b2fc7e45468bb38d37697fc?s=64&d=mm&r=g) Rob T says:
            
            [July 24, 2014 at 10:39 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579547)
            
            Hui,  
            I appreciate that in this case OFFSET doesn't impact performance. The main benefit really is that I'll struggle to remember and recreate the "better" solution above!
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579547)
            
3.  ![](https://secure.gravatar.com/avatar/02749853f95afebaaa0b33a6bc03a5bb415c9b414c07d7d0252f6117195ba1a6?s=64&d=mm&r=g) Utkarsh Shah says:
    
    [July 23, 2014 at 11:04 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578604)
    
    Hi Chandoo,
    
    I think simple solution for Count & Sum problem is use subtotal formula with 2 & 9 number instead 102 & 109 number for count & sum function resp.  
    e.g.  
    \=SUBTOTAL(2,A4:A8) - For Count of range A4 to A8
    
    \=SUBTOTAL(9,A4:A8) - For Sum of range A4 to A8
    
    When you apply filters, sum & count will autochanges.
    
    If you want to sum & count all entries (Hidden & visible) then use 102 & 109.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578604)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 23, 2014 at 2:10 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578676)
        
        @Utkarsh  
        Your formula's work for filtered data, but they don't allow for additional criteria to be applied as well as the filtering  
        ie: In the examples shown To Count or Sum the entries that have a category Value of D whilst being filtered for the Zone = North values
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578676)
        
        *   ![](https://secure.gravatar.com/avatar/597fb593cb5a4bc40e0c24319494f43b6e43b5fee5d036a6eda6cd0a7daf8fd3?s=64&d=mm&r=g) Rob says:
            
            [July 23, 2014 at 6:59 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578806)
            
            I agree with Utkarsh Shah. If you filter you can have multiple criteria applied one for each column, which gets you down to teh three records you want. Then Then the subtotal will count them in one column and you can also have a sum in the score column. Or add any of a dozen different aggregation or info pulling formulas there. They all adjust based on the filters and we are all happy. Unless a formula answer was needed to put the number somewhere else; then just refer to the answer cells.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578806)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [July 24, 2014 at 7:01 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579156)
                
                @Rob  
                Yes, Your right  
                But in cases where you want to see what proportion of say the Filtered Zone=North records was Category = D, you need to have the Data only partially filtered at the Zone level.
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579156)
                
4.  ![](https://secure.gravatar.com/avatar/4faf80281c65b11c7e7804a99c124c5b2667674ef681758eab5fda112ebcf351?s=64&d=mm&r=g) Darin Myers says:
    
    [July 23, 2014 at 2:41 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578683)
    
    I know this is a formula breakdown, but my approach would be to use a simple pivot table.
    
    Many here are pros, so I won't into detail about how to handle these calculations in a pivot table, all I will say is that I can't count how many times people have been thankful to me for pointing them to a better method after helping them figure out the method they were planning on using.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578683)
    
5.  ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) Jomili says:
    
    [July 23, 2014 at 5:12 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578764)
    
    I'm confused. Why wouldn't you simply use Countifs and Sumifs?  
    \=COUNTIFS($C$2:$C$20,"D",$B$2:$B$20,"North")  
    \=SUMIFS(D2:D20,$C$2:$C$20,"D",$B$2:$B$20,"North")
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578764)
    
    *   ![](https://secure.gravatar.com/avatar/8be4a1199a213a14615a6eefe46544a6bff52850bd98e2aedef35acf17ec4a45?s=64&d=mm&r=g) Colleen says:
        
        [July 24, 2014 at 7:30 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579467)
        
        I'm with you, Jomili. I always use COUNTIFS and SUMIFS. Why wouldn't they work? It seems much simpler.
        
        Unless maybe they are using a version older than Excel 2007? If I recall, these functions were introduced in Excel 2007, making my happiness meter improve by leaps and bounds.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579467)
        
6.  ![](https://secure.gravatar.com/avatar/d3fe07e573358c852c1bb91cabb87ee1e3639becf8aa4b630cf006fa61b3e7e0?s=64&d=mm&r=g) Grant says:
    
    [July 23, 2014 at 6:16 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578789)
    
    Perhaps I am missing something but why not use DSUM and DCOUNT?
    
    The range is already a table.  
    I put the Criteria of Zone and Category in a new range (F37:G38) and did the following:
    
    \=DSUM(Table1\[#All\], D1, F37:G38) = 172  
    \=DCOUNT(Table1\[#All\], D1, F37:G38) = 3
    
    D1 - is the cell that has Score.
    
    Get same answers irrespective of whether the table is filtered or not.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-578789)
    
7.  ![](https://secure.gravatar.com/avatar/abd84bd1f811faab7893693e5d05086819def187b9888170dfaaef3a9d09a728?s=64&d=mm&r=g) Marci says:
    
    [July 24, 2014 at 4:37 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579072)
    
    I would also use one of three approaches depending on how often I would need to use the info:
    
    Pivot table  
    Sumifs and Countifs formulae  
    Subtotal 9 and Subtotal 2 on a row below the entire table
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579072)
    
8.  ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
    
    [July 24, 2014 at 7:51 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579476)
    
    \=SUMPRODUCT((Table1\[Zone\]="North")+0, (Table1\[Category\]="D")+0) = 3
    
    \=SUMPRODUCT((Table1\[Zone\]="North")+0, (Table1\[Category\]="D")+0, Table1\[Score\]) = 172
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-579476)
    
9.  ![](https://secure.gravatar.com/avatar/e5aa9860ddee77913d3b6543ce72a785a0d253447ec2bf1fb9a38930596671a1?s=64&d=mm&r=g) David Clapperton says:
    
    [August 4, 2014 at 1:52 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-589391)
    
    Standing on Mike Girvin's shoulders, rather that filter the list I would be tempted to have two cells, each data validated to select a Zone (say A22) and a category (say A23). Then use these as lookups to feed into a three way array multiplication formula for the sum =SUMPRODUCT(- -(B2:B20=G22),- -(C2:C20=G23),D2:D20) and a two way for the count =SUMPRODUCT(- -(B2:B20=G22),- -(C2:C20=G23)) . These use the clever double negation trick to convert True/False into 1/0 before multiplying out. IMHO - a little easier to follow the logic as well.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-589391)
    
    *   ![](https://secure.gravatar.com/avatar/e5aa9860ddee77913d3b6543ce72a785a0d253447ec2bf1fb9a38930596671a1?s=64&d=mm&r=g) David Clapperton says:
        
        [August 4, 2014 at 1:54 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-589393)
        
        Sorry, Double negatives before each of the terms - didn't come out in the conversion.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-589393)
        
10.  ![](https://secure.gravatar.com/avatar/626071f0c70ed394c88e50f23bf8910d5a1cbdc3fcec117441e9ba135c5bad4a?s=64&d=mm&r=g) Asghar Abbasnejad says:
    
    [August 5, 2014 at 5:15 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-590332)
    
    The short solve are:  
    \=COUNTIFS($C$2:$C$20,"D",$B$2:$B$20,"North")  
    \=SUMIFS(D2:D20,$C$2:$C$20,"D",$B$2:$B$20,"North")
    
    With best regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-590332)
    
11.  ![](https://secure.gravatar.com/avatar/2c3d557d426bbcb7208671c1834bb6ec519e12ca75f7c67ad87d153b353bc44e?s=64&d=mm&r=g) Jonathan James says:
    
    [August 5, 2014 at 9:24 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-590609)
    
    I feel the point of this article was to design a formula that would update when data is filtered, and that wouldnt require the criteria to be specified elsewhere in the sheet. That being said, I dont have an alternative to one discussed in the article above.
    
    When I'm using SUMPRODUCT, I prefer to multiply the ranges rather use the double negation trick ( - - ) to convert TRUE,FALSE to 1,0.
    
    This formula: =SUMPRODUCT(- -(B2:B20=G22),- -(C2:C20=G23),D2:D20)  
    becomes: =SUMPRODUCT((B2:B20=G22)\*(C2:C20=G23),D2:D20)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-590609)
    
    *   ![](https://secure.gravatar.com/avatar/bf0a2f4e213b4acccef3339e03520f6ec02a81cc6ca8cd47aec1af3495a0dbf2?s=64&d=mm&r=g) John Jairo V says:
        
        [February 5, 2015 at 3:19 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-907545)
        
        Hi Jonathan.
        
        Although time has passed , I want to clarify that the syntax with the double negative is more efficient than the multiplication between two ranges. That's why in short is better to use double negative. Blessings !
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-907545)
        
12.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
    
    [July 26, 2015 at 11:25 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1014282)
    
    I've somehow missed this until now. That SUBTOTAL/OFFSET combination is killer.
    
    aMaeris uses a similar SUBTOTAL/OFFSET trick at [http://excelxor.com/2015/07/20/advanced-formula-challenge-12-an-array-of-matches/#comment-1366](http://excelxor.com/2015/07/20/advanced-formula-challenge-12-an-array-of-matches/#comment-1366)
    
    And I see there's a good writeup over at [http://dailydoseofexcel.com/archives/2005/05/11/arrays-with-offset/](http://dailydoseofexcel.com/archives/2005/05/11/arrays-with-offset/)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1014282)
    
13.  ![](https://secure.gravatar.com/avatar/e3eda3e4b70e3e4cafe61504fcb881caa60a30ba8ebd420b3d4a27f248c18730?s=64&d=mm&r=g) CookieRevised says:
    
    [October 19, 2015 at 9:56 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1065574)
    
    This week I had a similar challenge. It is a kind of variation on the problem explained above:
    
    How to count the number of unique text values in a column...  
    1) WITHOUT the use of any helper-column!!!  
    2) taking in account possible empty cells  
    3) taking in account filtering on that and other columns  
    4) taking in account possible hidden rows  
    5) (without the use of VBA of course... would be too easy otherwise :-P)
    
    Solutions found on the web (when you search hard enough):  
    \- almost always involve a helper-column  
    \- or do not calculate correctly if there is no filtering (it is 1 off in that case, because of empty rows which are included in the count)  
    \- or only work on number values at best, not text values...  
    \- and almost always involve the construct SUMPRODUCT(SUBTOTAL(103,OFFSET()),SOME\_REF\_TO\_A\_FIXED\_LOOKUP\_CELL). This makes that this would always need helper columns or at least one helper cell. This is useless if you only want to check unique values in the column.
    
    Another problem with this is that Excel does not like to take a SUBTOTAL() of a SUBTOTAL(). Result is that you actually need two helper columns for this if you want to use the SUMPRODUCT(SUBTOTAL()) construct.
    
    Exmaple and solution:
    
    You have a column with city names, and you want to count the total number of unique cities in that column. But that total number of unique cities should also update when columns are filtered (say all cities starting with A\*).
    
    A1: the text header, with autofiltering on or off  
    A2 thru A10: the citie names
    
    The matrix formula to count and sum the values:  
    \=COUNT(  
    IF(LEN(A2:A20);  
    IF(INTERVAL(  
    IF(SUBTOTAL(103;OFFSET(A2:A20;ROW(A2:A20)-ROW(A2);;1));MATCH(A2:A20;A2:A20;0));  
    IF(SUBTOTAL(103;OFFSET(A2:A20;ROW(A2:A20)-ROW(A2);;1));MATCH(A2:A20;A2:A20;0))  
    )  
    ;1)  
    )  
    )
    
    note: this is a matrix formula, so enter it using CTRL-SHIFT-ENTER  
    note: you can replace COUNT with SUM  
    note: COUNTIF and SUMIF will not work
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1065574)
    
    *   ![](https://secure.gravatar.com/avatar/e3eda3e4b70e3e4cafe61504fcb881caa60a30ba8ebd420b3d4a27f248c18730?s=64&d=mm&r=g) CookieRevised says:
        
        [October 19, 2015 at 10:46 pm](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1065588)
        
        Sorry, above formula has a bug in it when you also sort columns after filtering..... and I forgot to translate the FREQUENCY function to English, together with the proper used delimiters in English version of Excel...
        
        oopsie...
        
        The proper matrix formula is:  
        \=COUNT(  
        IF(  
        FREQUENCY(  
        IF(LEN(A2:A20),IF(SUBTOTAL(3,OFFSET(A2:A20,ROW(A2:A20)-ROW(A2),,1)),MATCH(A2:A20,A2:A20,0))),  
        IF(LEN(A2:A20),IF(SUBTOTAL(3,OFFSET(A2:A20,ROW(A2:A20)-ROW(A2),,1)),MATCH(A2:A20,A2:A20,0)))  
        )  
        ,1)  
        )
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1065588)
        
14.  ![](https://secure.gravatar.com/avatar/d3867507639c3d252da89d8ec65768d7c90b2d57e294581b8b422cd107c6587c?s=64&d=mm&r=g) Chirag Raval says:
    
    [May 12, 2018 at 6:51 am](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1546777)
    
    Dear Sirs & Users,
    
    This Is Really mind blowing concept that to learn how to receive various required effect on fix (waiting for result) structure based on dynamically changed database.
    
    But , base on overview of this concept, I can point towards that all last row reference is hard coded.
    
    Like (A1:A550) can it accept last row as dynamically (auto initialised last row address) like (A1:A & lastRow)?
    
    Require this due to for if we want to use this method on regularly/daily/ hourly basis on received every dynamic data range.
    
    Hope there are some solution there.
    
    Regards,
    
    Chirag Raval
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#comment-1546777)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-037-how-to-count-and-sum-filtered-tables/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Ask me your Excel questions & You could win an eBook](https://chandoo.org/wp/ask-me-your-excel-questions-you-could-win-an-ebook/) | [CP015: Handling big data, Controlling model railroad sets, Overcoming Excel obsession & more – ASK CHANDOO](https://chandoo.org/wp/cp015-ask-chandoo/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)