# Count and Sum data using Criteria on Filtered data sets.

**Source:** https://chandoo.org/wp/formula-forensics-023

---

Formula Forensics 023. Count and Sum a Filtered List according to Criteria
==========================================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 24 comments

  

Last week at the [Chandoo.org Forums](http://chandoo.org/forums/topic/replace-countif-formula-so-an-autofilter-can-be-used-to-subtotal-results?view=all "FF 23.")
, **TreeTopRobin**, posed a question:

**“**I need a formula in C1 that returns the number of times L appears in C7:C13  
With an AutoFilter on Row 3 the value should change if I filter on a company or team  
eg: If I filter on the West Team C1=2; no filter C1=3;filter on East team C1=1″

I responded with a Formula which solved TreeTopRobin’s problem:  
\=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), – -(C7:C13=B2))

So today in Formula Forensics we will examine how this works and then how it can be extended to Sum the values in other fields as well.

As always at Formula Forensics you can follow along using a Worked Example which you can download here: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2012/06/Filtered-List.xls "FF 23 Sample File")
.

Count Filtered Data using Criteria
----------------------------------

We can see that we have a small table of data which contains 4 fields, being Team, Company, Win/Loss and Score.

[![](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_1.png "FF23_1")](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_1.png)

We can see above that the formula for Count and Sum in C15 and C16 which using the Excel Countif() and Sumif() functions returns the correct results on the unfiltered data.

However when using the Excel Sum() or Count() functions on Filtered data, these formulas ignore the Filtering and display all the values of the original table.

[![](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_2.png "FF23_2")](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_2.png)

In the image above we have filtered the data to show only those records that the Team = East

We can see that only 1 record matches both Team = East and Win/Loss = L

To solve the Count issue I used in cell D2:  
\=SUMPRODUCT(SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), – -(C7:C13=B2))

Which solves the problem

Lets pull it apart and see what is inside.  
\=SUMPRODUCT(SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), – -(C7:C13=B2))  
The formula is based on the Excel Sumproduct() function which we examined in [Formula Forensic 007](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/ "FF 007. Sumproduct")
.

Sumproduct requires an Array and optional Arrays for input using the syntax:

[![](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_3.png "FF23_3")](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_3.png)

Looking at the above formula:  
\=SUMPRODUCT(SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), – -(C7:C13=B2))

We can see that:  
**Array 1:** SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1))  
**Array 2:**  – -(C7:C13=B2))

Sumproduct then multiplies the result of the two array together and then sums up the products.

**Important:** The two Arrays represent a list of all valid Filtered Data (Array 1) and a list of all Unfiltered Data which matches the Criteria (Array 2). Hence the product of the two arrays will be an Array which contains the Filtered Data that matches the Criteria.

### Array 1: SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),, 1))

Array 1 uses the Excel Subtotal() function to count the number of valid entries in each location in the range.

The Syntax of Subtotal() function is:

[![](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_4.png "FF23_4")](https://chandoo.org/wp/wp-content/uploads/2012/06/FF23_4.png)

In a spare cell **G26** enter the formula =SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)) then Press **F9** instead of Enter  
Excel will display an Array ={1;1;0;1;1;1;1}  
This represents each cell in the range C7:C13 with a 1 when there is a valid entry and a 0 when there is no text or value.

Before we move on lets see what happens when we Filter the data

Goto the Team cell **A6** and Unselect all the values, then select the **East** team.  
Go back to **G26** and evaluate the  \=SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)) formula  
You will see that excel is now displaying \={1;0;0;1;0;0;0}  
This represents the two cells which contain values when filtered that match the Filter Criteria =**East**

We will compare this array with the final part of the Sumproduct() formula later.

But first lets see how this works

We saw above that the syntax of the Subtotal() function is  
\=Subtotal( Function No, Ref 1, \[Ref 2\], …)

Using our formula:  
\=SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1))

**Function No**: 3 = Use the Counta() function ie: count the Numbers or Text entries in Ref 1…  
**Ref 1:** OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)

Ref 1 is an Offset() function that establishes an Array by Offsetting range C7:C13 by the row value of ROW(C7:C13)-MIN(ROW(C7:C13)) and returns a Range that is 1 cell high

And now in English?  
OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)

The Offset() function offsets the range C7:C13 by the value of ROW(C7:C13)-MIN(ROW(C7:C13))  
And then returns 1 cell from the new location.

If we step into the ROW(C7:C13)-MIN(ROW(C7:C13)) part,  
goto a blank cell **G21** and enter: \=ROW(C7:C13)-MIN(ROW(C7:C13)) press **F9** instead of Enter  
Excel returns \={0;1;2;3;4;5;6}  
This is the value of the Current Row minus the starting Row of the range C7:C13  
ie: 7-7 = 0  
8-7 = 1  
9-7 = 2 etc

Because this is in a Sumproduct it is treated as an Array Formula and hence the Offset() function applies the array to the initial Range, One entry at a time  
So:  
\=OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)  
\=OFFSET(C7:C13, {0;1;2;3;4;5;6},, 1)  
So we can now see:  
The Cell C7 is offset 0 Rows, 0 Columns and returns 1 cell which will be the value in C7 = W  
The Cell C7 is offset 1 Rows, 0 Columns and returns 1 cell which will be the value in C8 = L  
The Cell C7 is offset 2 Rows, 0 Columns and returns 1 cell which will be the value in C9 = “”

:  
The Cell C7 is offset 5 Rows, 0 Columns and returns 1 cell which will be the value in C12 = L  
The Cell C7 is offset 6 Rows, 0 Columns and returns 1 cell which will be the value in C13 = W

This is shown if you goto a blank cell **G19** and enter \=OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1) press **F9** instead of Enter

Unfiltered Excel returns \={“W”;”L”;0;”L”;”W”;”L”;”W”}  
Filtered Excel returns \={“W”;”L”;0;”L”;”W”;”L”;”W”}

The filtering doesn’t effect how the Offset() function performs.

The Subtotal() function \=SUBTOTAL(3, OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1))  
Now steps in and using Function Number 3 or Counta() adds up the number of times each value in the array is used.  
Because Subtotal ignores hidden values used by Filter the value returned varies when the Filter is applied:

Unfiltered Excel returns \={1;1;0;1;1;1;1}

Filtered (Team=**East**) Excel returns \={1;0;0;1;0;0;0}

Finally we can see that:  
\=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), – -(C7:C13=B2))

Is equivalent to:  
Unfiltered: \=SUMPRODUCT({1;1;0;1;1;1;1}, – -(C7:C13=B2))  
Filtered (Team = East): \=SUMPRODUCT({1;0;0;1;0;0;0}, – -(C7:C13=B2))

### Array 2: – – (C7:C13=B2)

Lets now move to the second Array in the Sumproduct Formula – -(C7:C13=B2)  
In a spare cell **G17** enter \=- -(C7:C13=B2) press **F9** instead of Enter  
Excel will return \={0;1;0;1;0;1;0}

This is a simple array of each cell in the range C7:C13 compared to the Criteria C2  =”L”  
If you enter \=(C7:C13=B2) press **F9** instead of Enter  
Excel will return \={FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}  
So you can see that Excel uses the double negative – – to multiply each value in the array

\={FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE} -1 \* -1

\={FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE} \*1

thus converting the array to  
\={0;1;0;1;0;1;0}

### Putting It All Together

So finally we can see that:  
\=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), – -(C7:C13=B2))

Is equivalent to:  
Unfiltered: \=SUMPRODUCT({1;1;0;1;1;1;1},{0;1;0;1;0;1;0})  
Filtered (Team = East): \=SUMPRODUCT({1;0;0;1;0;0;0},{0;1;0;1;0;1;0})

Sumproduct then multiplies the two array together and sums the products

Unfiltered: \=SUMPRODUCT({1\*0; 1\*1; 0\*0; 1\*1; 1\*0; 1\*1; 1\*0})  
Returning 3

Filtered (Team = East): \=SUMPRODUCT({1\*0; 0\*1; 0\*0; 1\*1; 0\*0; 0\*1; 0\*0})  
Returning 1

How do we Sum instead of Count
------------------------------

Now we know that the logic of the arrays is to simply multiply an Array of Valid Filtered Cells by an Array of Criteria we can simply add another Array to the Sumproduct formula:

If we want to Sum the Score values in Column D we can add it as either

\=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)),– –(C7:C13=B2),(D7:D13))

or

\=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), (C7:C13=B2)\*(D7:D13))

Noting that the logic of which cells to include has already be dealt with by the Count function described above.

You can examine these formulas in Cell D4 in the sample file.

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/06/Filtered-List.xls "FF 23 Sample File")
.

Formula Forensics “The Series”
------------------------------

This is the 23rd post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "The Formula Forensics Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
.

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
| Written by Hui...  <br>Tags: [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [MIN()](https://chandoo.org/wp/tag/min/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [SUBTOTAL](https://chandoo.org/wp/tag/subtotal/)<br>, [sumproduct](https://chandoo.org/wp/tag/sumproduct/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 24 Responses to “Formula Forensics 023. Count and Sum a Filtered List according to Criteria”

1.  ![](https://secure.gravatar.com/avatar/e10be12596ef5519b4e816fabd5d9c633f11e4561d60039b9582beda7c1392f2?s=64&d=mm&r=g) John Sterling says:
    
    [June 7, 2012 at 11:51 am](https://chandoo.org/wp/formula-forensics-023/#comment-225134)
    
    I'd suggest simply using the subtotal function and filtering the data using the Win/Loss column.  You get the same results and the formula is more comprehensible.
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-225134)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 7, 2012 at 3:32 pm](https://chandoo.org/wp/formula-forensics-023/#comment-225143)
        
        @John
        
        That is one option.
        
        There are times however when you want to see the whole data table or a filtered subset and still want to produce summary reports against an unfiltered field.
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-225143)
        
2.  ![](https://secure.gravatar.com/avatar/2ad7a09f161ab9242c0420e5e3fbf51bd5fd4124929080e9d36c0d8b2ed6516c?s=64&d=mm&r=g) Matthew Holbrook says:
    
    [June 7, 2012 at 3:45 pm](https://chandoo.org/wp/formula-forensics-023/#comment-225144)
    
    Is there a particular reason why you are using a comma and the unary (--) operator for the second array in the SUMPRODUCT formula?  It seems to work the same if you were to string the arrays together using the asterisk (\*).  The advantage is that SUMPRODUCT treats the entire string of arrays as a single array.
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-225144)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 8, 2012 at 12:29 am](https://chandoo.org/wp/formula-forensics-023/#comment-225147)
        
        @Mathew
        
        Your correct, There is no difference.
        
        I thought it may have been easier to explain this method.
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-225147)
        
3.  ![](https://secure.gravatar.com/avatar/85ea44f7f532ef30d6be7db163bdab883c34320ee913fa611e121b12680a9e46?s=64&d=mm&r=g) Kenneth Taylor says:
    
    [December 13, 2013 at 4:31 pm](https://chandoo.org/wp/formula-forensics-023/#comment-459789)
    
    Is there a way to do this on a large set of data? As in ~100,000 rows? When I try I get an error because the formula becomes too long. It says the max length of a formula is 8,192 characters. Excel 2010.
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-459789)
    
4.  ![](https://secure.gravatar.com/avatar/a9c3cbc069f17f489f4a4813d1213d8c93685db9061e8ba05acd130b6c04e8da?s=64&d=mm&r=g) RB says:
    
    [March 10, 2015 at 8:53 pm](https://chandoo.org/wp/formula-forensics-023/#comment-927661)
    
    How do I incorporate a specific text within a cell for the second array. For instance, - -(C7:C13="Apple")  
    when I chose a specific text the formula does not work.
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-927661)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [March 11, 2015 at 12:24 am](https://chandoo.org/wp/formula-forensics-023/#comment-927750)
        
        @RB
        
        I am not sure what is the issue as if I use the sample data in the post the following work fine
        
        Count:  
        \=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)), --(C7:C13="L"))  
        Sum:  
        \=SUMPRODUCT(SUBTOTAL(3,OFFSET(C7:C13,ROW(C7:C13)-MIN(ROW(C7:C13)),,1)),(C7:C13="L")\*(D7:D13))
        
        You may want to check that there are no leading or trailing spaces in your list of Apples
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-927750)
        
        *   ![](https://secure.gravatar.com/avatar/a9c3cbc069f17f489f4a4813d1213d8c93685db9061e8ba05acd130b6c04e8da?s=64&d=mm&r=g) RB says:
            
            [March 11, 2015 at 1:42 pm](https://chandoo.org/wp/formula-forensics-023/#comment-928098)
            
            I should have given a better explanation. Heres my situation. I have a column with cells filled with names like Column 1, Column 2, Pier 1, Pier 2, etc. If the cell just contained Pier and searched for that it works. But because it has other characters in the cell its not recognizing the pier. So how can I extract specific characters of a string of text in this formula?
            
            Hopefully this was a better explanation
            
            [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-928098)
            
5.  ![](https://secure.gravatar.com/avatar/b76a6216893892821aeb435b2a04f0a54e62f825d8b2826cc50e522dd45f5b95?s=64&d=mm&r=g) MS says:
    
    [May 29, 2015 at 10:25 pm](https://chandoo.org/wp/formula-forensics-023/#comment-982885)
    
    Hello-
    
    This formula works pretty well for me except that it slow down excel and prevents some of my macros from working. I was wondering if there was a way to program this in VBA so that excel isn't always trying to recalculate it. I would like to use a push of a button to get it to run then paste in a cell.
    
    Thanks!
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-982885)
    
6.  ![](https://secure.gravatar.com/avatar/6f1f5e01a3c04a443f0711c53784cc15592f1d9378b6eb65275d12d5d90ee27e?s=64&d=mm&r=g) Akshay Modi says:
    
    [August 9, 2015 at 5:32 pm](https://chandoo.org/wp/formula-forensics-023/#comment-1021044)
    
    I am trying to sum filtered data in a column, but would want to ignore the negative values in the column. How to go about doing this?
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1021044)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 10, 2015 at 1:14 am](https://chandoo.org/wp/formula-forensics-023/#comment-1021273)
        
        @Akshay
        
        Why not just add a filter to that column to only show the values greater than zero?
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1021273)
        
        *   ![](https://secure.gravatar.com/avatar/6f1f5e01a3c04a443f0711c53784cc15592f1d9378b6eb65275d12d5d90ee27e?s=64&d=mm&r=g) Akshay modi says:
            
            [August 10, 2015 at 1:21 pm](https://chandoo.org/wp/formula-forensics-023/#comment-1021556)
            
            The negative values are required for reporting purposes, but their effect on the total is distorting the required output. Please advise.
            
            [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1021556)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [August 11, 2015 at 12:25 am](https://chandoo.org/wp/formula-forensics-023/#comment-1021774)
                
                @Akshay
                
                I’d suggest making a post in the Chandoo.org Forums  
                [http://forum.chandoo.org/](http://forum.chandoo.org/)
                  
                Attach a sample file to simplify the task
                
                [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1021774)
                
7.  ![](https://secure.gravatar.com/avatar/816acbdcba964bcee372e2f110f9d91433c57a0ebcbbc88376c9287cd4cce735?s=64&d=mm&r=g) Bob says:
    
    [October 8, 2015 at 12:40 am](https://chandoo.org/wp/formula-forensics-023/#comment-1057867)
    
    I have this working for counting and summing, however, I have a list and for the second array, I need a criteria. That is, I'm looking for b13:b200="01.??.??" or =left((a1,2) or something like that. These types of criteria matches do not appear to work as I get a blank as a result.  
    Thanks!
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1057867)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [October 8, 2015 at 1:10 am](https://chandoo.org/wp/formula-forensics-023/#comment-1057881)
        
        @Bob
        
        As your formula b13:b200=”01.??.??” looks like you are trying to check the first day of the month of the range  
        What about trying Day(B13:B200)=1
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1057881)
        
8.  ![](https://secure.gravatar.com/avatar/c6701c6793d12f56f8df818cf8524a50726089a7554bf32e2ca04812398f1921?s=64&d=mm&r=g) Sricharan says:
    
    [December 18, 2015 at 3:45 pm](https://chandoo.org/wp/formula-forensics-023/#comment-1107853)
    
    Hai Experts,  
    i understood this formula well and working fine in MS Excel 2013  
    but when the same am trying to place in google Spreadsheet it shows error as  
    "SUMPRODUCT has mismatched range sizes. Expected row count: 1. column count: 1. Actual row count: 2014, column count: 1." and as a result #VALUE! Appears in cell.  
    Can anyone please help me how would i get it done in Google Spread sheet  
    or is there any other formula as a substitute for this.  
    Thank you very much.
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1107853)
    
9.  ![](https://secure.gravatar.com/avatar/d1fad94055f8cb4c96ce65fcf0e3b37a5565b404117f9a193588174ae1b078a0?s=64&d=mm&r=g) vivek says:
    
    [April 20, 2016 at 2:15 pm](https://chandoo.org/wp/formula-forensics-023/#comment-1171228)
    
    thanks for providing this.. but why does excel keeps on prompting Circular referencing in cell D3?
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1171228)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [April 20, 2016 at 2:46 pm](https://chandoo.org/wp/formula-forensics-023/#comment-1171235)
        
        @Vivek
        
        I don't know
        
        I just downloaded the file and it is working fine and not showing that error
        
        Goto the Formulas, Calculation Options Tab and check that Calculation is set to Automatic
        
        What version of Excel and Windows are you using ?
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1171235)
        
10.  ![](https://secure.gravatar.com/avatar/fd409a2994cf331e57884a93e10fdffd6439574e1c312dfa9af7e3bead4eebc2?s=64&d=mm&r=g) Gaylord says:
    
    [January 2, 2017 at 1:53 am](https://chandoo.org/wp/formula-forensics-023/#comment-1382830)
    
    I know that this forum is for MS Excel, but I am trying to help someone who is working in Google Sheets. The below formula works in Excel but Google Sheets returns:  
    "SUMPRODUCT has mismatched range sizes. Expected row count: 1. column count: 1. Actual row count: 39000, column count: 1." and as a result #VALUE! Appears in cell.  
    This is the same problem asked by Srichirin above. Does anyone know if there is a formula for Google Sheets that will replicate what MS Excel does?
    
    \=SUMPRODUCT(SUBTOTAL(3,OFFSET($C$6:$C$39500,ROW($C$6:$C$39500)-MIN(ROW($C$6:$C$39500)),,1)),- -($C$6:$C$39500=H1),($D$6:$D$39500))
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1382830)
    
11.  ![](https://secure.gravatar.com/avatar/82d495d050621381dd90b6e09d0badf7cb6b20204a0feb9c963056c10c6b77a1?s=64&d=mm&r=g) Terry Johnson says:
    
    [January 24, 2018 at 10:27 am](https://chandoo.org/wp/formula-forensics-023/#comment-1533285)
    
    Trying to find a SUMPRODUCT formula that counts the word Closed by date for the last 7 days in a filtered list.  
    \=COUNTIF(M:M,">"&TODAY()-7) works ok for unfiltered count Column M contains Closure dates (blank if open) and Column L is Status Open or Closed
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1533285)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 24, 2018 at 10:52 am](https://chandoo.org/wp/formula-forensics-023/#comment-1533289)
        
        @ Terry
        
        Please ask the question at the Chandoo.org Forums  
        [https://chandoo.org/forum/](https://chandoo.org/forum/)
        
        Please attach a sample file to ensure a quicker more accurate answer
        
        [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1533289)
        
12.  ![](https://secure.gravatar.com/avatar/0318e523ed7907f0fd1d6726bd3b369af24105484df79532a1242adaa1037327?s=64&d=mm&r=g) Bernardo says:
    
    [August 8, 2019 at 12:55 am](https://chandoo.org/wp/formula-forensics-023/#comment-1675539)
    
    I used this formula and worked like a charm! But, now I've been requested to use it but adding not one but two criteria in the same formula. For instance the sum I was doing added negative and positive numbers. I've been asked to use the exact same formula but adding that only positive numbers were considered... any idea on how to do this?
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1675539)
    
13.  ![](https://secure.gravatar.com/avatar/67db56df4f96872536cda01e3dcfed1e72ed4b15ccffd1a23279c823f5d054ad?s=64&d=mm&r=g) Michael says:
    
    [January 20, 2021 at 1:25 pm](https://chandoo.org/wp/formula-forensics-023/#comment-1967621)
    
    How exactly do you do sum filtered cells when two criteria are need not just one?
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-1967621)
    
14.  ![](https://secure.gravatar.com/avatar/8b27ed1b324dc3e5b70a9671d354b20f316172e10657dcbf3cdd7aabd00f516b?s=64&d=mm&r=g) kamlesh Bisht says:
    
    [April 3, 2022 at 7:36 pm](https://chandoo.org/wp/formula-forensics-023/#comment-2072752)
    
    Thank you so much brother literally I have been struggling since morning to get the sum of the filtered category, however, after reading your blog attentively i got my solution, so thanks a lot once again.
    
    [Reply](https://chandoo.org/wp/formula-forensics-023/#comment-2072752)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-023/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Sort Pivot Tables the way you want \[Quick tip\]](https://chandoo.org/wp/custom-sort-pivot-tables/) | [Thermo-meter chart with Marker for Last Year Value](https://chandoo.org/wp/thermo-meter-chart-with-last-year-marker/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)