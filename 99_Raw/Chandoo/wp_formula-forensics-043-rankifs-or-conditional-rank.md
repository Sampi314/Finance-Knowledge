# Develop a Conditional Rank or Rankifs formula in Excel

**Source:** https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank

---

Formula Forensics 043: Rankifs or Conditional Rank
==================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 18 comments

  

Excel has had a native Rank() function since its very first versions. This function has been updated in 2010 to include Rank.eq and Rank.Avg.

These functions allow you to Rank a list in either an Ascending or Descending order

Recently on Linkedin I came across a formula at [Excel Champs](https://excelchamps.com/blog/conditional-ranking-sumproduct-rank-if/)
 for calculating a Conditional Rank effectively a Rankif() function. The Excel Champs post is based on [Michael Girvin’s Youtube Video](https://www.youtube.com/watch?v=rCeTG2k2T6I)
.

Despite having used Excel since its introduction and despite the fact that there are at kleast a dozen posts in the Chandoo.org Forums discussing Rank If, I thought it strange that I had never seen or had need to use a Rankif() function and so was drawn to it to understand how it worked.

This post will look at how this technique works, how to use it for Ascending and Descending Ranks and then how to extend it to Multiple Criteria.

Then finally we will move the function into the 21st Century and replace the base function that the technique is based on with a newer function.

As always with Formula Forensics posts you can follow along with a sample file, [Download Here](https://assets.chandoo.org/wp/wp-content/uploads/2017/10/Rank-If.xlsx "FF 23 Sample File")
.

Conditional Rank or Rankifs
---------------------------

What is a Conditional Rank or Rankif/s() function.

Just as the words describe, Conditional Rank is a Rank that is based on conditions. So just as Countif() or Sumif() count or sum based on a condition so does Conditional Rank, effectively it is the missing Rankifs() function.

Open the sample file and look at the data set

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/Rankif001.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/Rankif001.png)

You can see that we have the Scores for 12 Students. The table also has fields for Department and Area.

I have highlighted the 4 Engineering Students which we will examine during the post

John has a Score of 38, Chandoo has a score of 72, Donna a score of 62 and Bob a score of 84.

So manually Ranking these 4 students from Highest to Lowest would have the following order

1.  Bob 84
2.  Chandoo 72
3.  Donna 62
4.  John 38

This is shown in the Dep’t Wise Rank Asc, column **E**

So examining the highest Engineering student, Bob, Cell **E8** you will see that it has a formula:

\=SUMPRODUCT(($B$2:$B$13=B8)\*(D8<$D$2:$D$13))+1

lets look at how this formula works

\=SUMPRODUCT(($B$2:$B$13=B8)\*(D8<$D$2:$D$13))+1

We will refer to these sections later, but the first or Green component is a Conditional part of the formula

The 2nd or Red section is the Ranking part of the Formula.

We know from other Formula Forensics posts that Sumproduct adds “Sums” the Products of its constituent arrays. You can read more about how Sumproduct works here [Formula Forensics 007 Sumproduct](https://chandoo.org/wp/2011/12/21/formula-forensics-no-007/)

In this case there will only be a Single array which is actually made up, as the product of 2 other arrays

($B$2:$B$13=B8)\*(D8<$D$2:$D$13)

**The Conditonal Section**

Lets look at the first array, the Conditional Section

($B$2:$B$13=B8)

This says is range B2:B13 equal to B8

ie: It is saying are you an Engineering Student ?

If you select Cell E8, then select the ($B$2:$B$13=B8) component and press **F9**

Excel will show: {TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}

This is an array showing which of Cells in B2:B13 are equal to B8

We can see that the 1st, 4th, 5th and 7th elements of the array are True

{**TRUE**;FALSE;FALSE;**TRUE;TRUE**;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE}

These correspond to cells B2, B5, B6 and B8 which are all Engineering.

**The Ranking Section**

Escape out of that formula and we will now look at the second Array

If you select Cell E8, then Edit the cell **F2** and select the (D8<$D$2:$D$13) component and press **F9**

Excel will show: {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE}

This is an array showing which of Cells in D2:D13 are greater than D8

That is the 3rd, 10th and 11th elements are greater than D8

{FALSE;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;**TRUE**;**TRUE**;FALSE}

But lets notice here that none of the the 3rd, 10th or 11th elements are Engineering

They are Admin, Sales and Admin, respectively.

So for our cell D8, None of the Engineering Scores are greater than it.

**Combining the Two Sections**

Escape back out of that formula and we will now look at the internal multiplication of the two arrays

If you select Cell E8, then Edit the cell **F2** and select the whole ($B$2:$B$13=B8)\*(D8<$D$2:$D$13) component and press **F9**

Excel will display: {0;0;0;0;0;0;0;0;0;0;0;0}

This array is the product of the previous two arrays

ie:

{**TRUE**;FALSE;FALSE;**TRUE;TRUE**;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE} \* {FALSE;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;**TRUE**;**TRUE**;FALSE}

We can see here that none of the True values line up

So that when the arrays are multiplied the resultant array is {0;0;0;0;0;0;0;0;0;0;0;0}

It will only have a 1 in the final array when the two corresponding array elements both have true values.

Finally this array is available to the Sumproduct Function for evaluation

Escape back out of that formula and we will now look at how Sumproduct treats the two arrays

If you select Cell E8, then Edit the cell **F2** and select the whole \=Sumproduct($B$2:$B$13=B8)\*(D8<$D$2:$D$13)) component and press **F9**

Excel will display a {0}

That is the sum of the products of the arrays is 0

Finally the formula adds a 1 to this to get the final Rank of 1

That is that none of the Engineering Students have a higher score than Bob and so he has a Value of 1

ie: The steps in the solution being

\=SUMPRODUCT(($B$2:$B$13=B8)\*(D8<$D$2:$D$13))+1

\=SUMPRODUCT( {**TRUE**;FALSE;FALSE;**TRUE;TRUE**;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE} \* {FALSE;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;**TRUE**;**TRUE**;FALSE} )+1

\=SUMPRODUCT( {0;0;0;0;0;0;0;0;0;0;0;0} )+1

\=0 + 1

\=1

Lets now examine how Chandoo, in Row 5, went with a score of 72

Select Cell, E5  

You can edit the cell by pressing **F2**

\=SUMPRODUCT(($B$2:$B$13=B5)\*(D5<$D$2:$D$13))+1

Evaluate the component sections

\=SUMPRODUCT( {**TRUE**;FALSE;FALSE;**TRUE**;**TRUE**;FALSE;**TRUE**;FALSE;FALSE;FALSE;FALSE;FALSE} \*  {FALSE;**TRUE**;**TRUE**;FALSE;FALSE;**TRUE**;**TRUE**;FALSE;FALSE;**TRUE**;**TRUE**;FALSE} )+1

\=SUMPRODUCT( {0;0;0;0;0;0;1;0;0;0;0;0} )+1

\=1 + 1

\=2

We can see using the same analysis technique for Row 5, that Chandoo’s score of 72 was the 5th, highest score overall, It had 4 higher scores than Chandoo did.

But only 1 of these was an Engineering student

The 7th element in each array is True

So overall Chandoo had 1 Engineering Student with a Higher Score and so he is gets a Rank of 2.

You can use the technique above to examine other students and see how they Ranked.

### Rank Descending

The technique and formulas above use \=SUMPRODUCT(($B$2:$B$13=B2)\*(D2<$D$2:$D$13))+1 to rank the Students in Ascending Order.

That is the Highest Score has nobody with a Higher score and so Scores a 1 (0+1)

The second highest student only has 1 person above him and so they score a 2 (1+1)etc.

To change the Ranking Order from Ascending to Descending we simply reverse the comparison sign in the counting array

**Ascending**   : \=SUMPRODUCT(($B$2:$B$13=B2)\*(D2**<**$D$2:$D$13))+1

**Descending** : \=SUMPRODUCT(($B$2:$B$13=B2)\*(D2**\>**$D$2:$D$13))+1

In the Descending formula the highest Ranked Engineering Student, Bob, will have 3 other Engineering students below him and so scores a 4 (3+1)

The second highest Ranked Engineering Student, Chandoo, will have 2 other Engineering students below him and so scores a 3 (2+1)

You can see how that works by looking at the column **G**

### Adding More Conditions

In the examples above the Ascending and Descending formulas have only applied a single Condition to our Conditional Rank formula.

In our example we required that the student is an Engineering student

\=SUMPRODUCT(($B$2:$B$13=B2)\*(D2**<**$D$2:$D$13))+1

The Green array is checking that the array for that cell is, in the example of Row 2, an Engineering Student.

We can add further conditions simply by adding more Conditional Sections to the formula

ie: To Rank Engineering Students from the South we simply add a second Conditional Section to the Sumproduct Formula.

**Ascending**: \=SUMPRODUCT(($B$2:$B$13=B2)\*($C$2:$C$13=C2)\*(D2<$D$2:$D$13))+1

**Descending**: \=SUMPRODUCT(($B$2:$B$13=B2)\*($C$2:$C$13=C2)\*(D2>$D$2:$D$13))+1

You can continue to add multiple sections to suit your needs

To Rank Engineering Students from the South named Bob we simply add a second and third Conditional Section to the Sumproduct Formula.

**Ascending**: \=SUMPRODUCT(($B$2:$B$13=B2)\*($C$2:$C$13=C2)\*($A$2:$A$13=A2)\*(D2<$D$2:$D$13))+1

**Descending**: \=SUMPRODUCT(($B$2:$B$13=B2)\*($C$2:$C$13=C2)\*($A$2:$A$13=A2)\*(D2>$D$2:$D$13))+1

Removing Duplicates from the Rankings
-------------------------------------

If we modify the data a little and accidentally add a few duplicates scores we can see that the Formulas shown above introduce an error

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/Rankif002.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/Rankif002.png)

We can see that both Fred and Bob are Engineering students and they both scored 84. The existing function has scored them equally as 1.

We can see that both Chandoo and Danielle are also Engineering students and they both scored 72. The existing function has scored them equally as 2.

Luckily there is a work around for this.

The base formula in our new data set is

\=SUMPRODUCT(($B$20:$B$31=B20)\*(D20<($D$20:$D$31)))+1

We can modify this to add a small but slightly different value to each row in the Counting Section of the Sumproduct formula

\=SUMPRODUCT(($B$20:$B$31=B20)\*((D20+ROW()/1000)<($D$20:$D$31+(ROW($I$20:$I$31)/1000))))+1

you can see that the sections highlighted in Green above add a small number based on the Row Number / 1000 to both the Score and the Score Column. This way numbers closer to the bottom of the Table will have a higher chance of getting a lower rank.

If you want the students higher in the list to have a Higher Ranking you can change the logic as such

\=SUMPRODUCT(($B$20:$B$31=B20)\*((D20+(100-ROW())/1000)<($D$20:$D$31+((100\-ROW($I$20:$I$31))/1000))))+1

Just make sure the value 100 is greater than the last Row number of the data

Updating the Formula
--------------------

In the Introduction I made note that I would bring the Formula into the 21st Century.

The Conditional Rank Formula is based on the use of the Sumproduct Function.

\=SUMPRODUCT(($B$2:$B$13=B2)\*(D2**<**$D$2:$D$13))+1

The Sumproduct function must be the most versatile function ever introduced to Excel.

However if you examine the formula you will see it basically says “Sum the number of entries where a Condition is met, But Sum is effectively Counting

So it sort of sounds like a Countifs() Function?

You can examine the Countifs() based equivalent functions below

**Ascending version**

**Sumproduct** \=SUMPRODUCT(($B$2:$B$13=B2)\*(D2**<**$D$2:$D$13))+1

**Countifs** \=COUNTIFS($B$2:$B$13,B2,$D$2:$D$13,”>”&D2)+1

**Descending version**

**Sumproduct** \=SUMPRODUCT(($B$2:$B$13=B2)\*(D2**\>**$D$2:$D$13))+1

**Countifs** \=COUNTIFS($B$2:$B$13,B2,$D$2:$D$13,”<“&D2)+1

Unfortunately Excel doesn’t allow us to use the F9 evaluate facility on the components of Countifs()

But reading each formula from left to right, they say

Count the cells If, The First Column B is equal to the Rows Value of Column B and the second Column D is greater than the Rows Value of Column D

That is = Countif ( Department Column = Engineering & Score Column > Current Cell)

Closing
-------

This post has explained two techniques for evaluating Conditional Rank and included several variations as well.

Despite the fact that this was new to me I have since seen at least a dozen posts here on the Chandoo.org Forums where these techniques have been used.

Do you have any applications where this is applicable or other techniques to perform a Conditonal Rank or Rankifs() functionality?

Let us know in the comments below.

Formula Forensics “The Series”
------------------------------

This is the 47th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](https://chandoo.org/wp/formula-forensics-homepage/)

Formula Forensics Needs Your Help
---------------------------------

If you want to see more Formulas pulled apart and explained Forensically we need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
, or even drop it in the Comments below.

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
| Written by Hui...  <br>Tags: [Condional Rank](https://chandoo.org/wp/tag/condional-rank/)<br>, [rank()](https://chandoo.org/wp/tag/rank/)<br>, [Rankif](https://chandoo.org/wp/tag/rankif/)<br>, [Rankifs](https://chandoo.org/wp/tag/rankifs/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 18 Responses to “Formula Forensics 043: Rankifs or Conditional Rank”

1.  ![](https://secure.gravatar.com/avatar/2e6abaf5ac49344b95f76181c0d2c52d1cb33bf95c3606caec5af112482bfc3d?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
     says:
    
    [October 19, 2017 at 7:50 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517127)
    
    Hi Hui,  
    Very detailed explanation of using SUMPRODUCT for solving this problem, awesome!
    
    I have a blogpost discussing the use of COUNTIFS to solve the problem.  
    [https://wmfexcel.com/2016/03/12/rank-in-subgroup-rankif/](https://wmfexcel.com/2016/03/12/rank-in-subgroup-rankif/)
    
    Hope it gives your readers additional reference on how the COUNTIFS works for this problem.
    
    Cheers,
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517127)
    
2.  ![](https://secure.gravatar.com/avatar/f35ffdd7aaa4fce279235ffee1de2e503bb6fce1f0e24d74537393ed4bed128a?s=64&d=mm&r=g) Hazel says:
    
    [October 19, 2017 at 7:56 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517129)
    
    Your download link is broken!
    
    [https://assets.chandoo.org/wp/wp-content/uploads/2017/01/Reverse-Text.xlsx](https://assets.chandoo.org/wp/wp-content/uploads/2017/01/Reverse-Text.xlsx)
    
    and not
    
    [https://assets.chandoo.org/wp/wp-content/uploads/2017/10/Rank-If.xlsx](https://assets.chandoo.org/wp/wp-content/uploads/2017/10/Rank-If.xlsx)
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517129)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [October 19, 2017 at 9:00 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517141)
        
        Damn Proof Reader...
        
        Thanx Hazel
        
        It is fixed now
        
        [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517141)
        
        *   ![](https://secure.gravatar.com/avatar/f35ffdd7aaa4fce279235ffee1de2e503bb6fce1f0e24d74537393ed4bed128a?s=64&d=mm&r=g) Hazel says:
            
            [October 19, 2017 at 10:08 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517149)
            
            Fantastic blog btw ... currently playing with it and really liking the potential it has for my analysis reports 🙂
            
            [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517149)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [October 19, 2017 at 3:02 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517205)
                
                @Hazel
                
                Thanx for the kind words
                
                I'll assume the usual 5% commission ?
                
                [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517205)
                
3.  ![](https://secure.gravatar.com/avatar/549f0f05e61393eca81e962cd1a516d56a4078f8737b04ea652e80dc45e70cb1?s=64&d=mm&r=g) Black Moses says:
    
    [October 19, 2017 at 3:00 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517203)
    
    Thanks a lot for this post,
    
    Like you, I've never needed to use a conditional ranking formula despite using Excel forever, but I found this incredibly interesting and I'm sure I'll come back to this post if I need to use conditional ranking in the future. Plus, I tend to avoid SUMPRODUCT like the plague and just use array formulae instead so anything that gets me thinking about SUMPRODUCT can only be a good thing.
    
    In terms of functions that we want explained, I'd love it if you could explain MMULT. I can't remember where but I remember seeing MMULT being used in the solution to a formula problem that would have been really complicated to solve otherwise. It really intrigued me but I don't fully understand how it works, or rather how you can use it to solve problems/what kinds of problems it works best with.
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517203)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [October 19, 2017 at 3:05 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517208)
        
        @Black Moses
        
        Sumproduct can destroy spreadsheet performance when incorrectly used  
        However when used properly, it is the Swiss Army Knife of Excel Problem solving
        
        Specifically have a read of :  
        [http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/](http://chandoo.org/wp/2011/12/21/formula-forensics-no-007/)
          
        [http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/](http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/)
        
        For some great ideas
        
        [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517208)
        
4.  ![](https://secure.gravatar.com/avatar/028d37308327c214a626cd36939a66ce94ee7410dde285bd46f6a22b08102ce6?s=64&d=mm&r=g) Abhay Gadiya says:
    
    [October 21, 2017 at 3:41 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517757)
    
    I checked this Power Query solution here -
    
    [https://blog.crossjoin.co.uk/2015/05/11/nested-calculations-in-power-query/amp/](https://blog.crossjoin.co.uk/2015/05/11/nested-calculations-in-power-query/amp/)
    
    Checkout my YouTube channel for video as well.
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1517757)
    
5.  ![](https://secure.gravatar.com/avatar/026628c726a1b17e82402cf62c48df1bcc4f7a8307f13f190e888a46fc7438fc?s=64&d=mm&r=g) esg says:
    
    [November 5, 2017 at 12:20 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1520754)
    
    Inspiring.  
    Just a warning in sumproduct vs summing product's  
    in sumproduct, in excel2010, blank cells are evaluated as ZERO, while in product, they are ignored (unless all elements are blank).  
    Maybe this is because I have the wrong defaults on my system.  
    hth.
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1520754)
    
6.  ![](https://secure.gravatar.com/avatar/c7db5b0f3d9a0799a97109f1f51c0416751e3421c7ea6f963e0072ccf811bccd?s=64&d=mm&r=g) Peter B says:
    
    [April 24, 2018 at 8:30 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1544740)
    
    A further advantage of these formulas over RANK is that they work on text strings, where they sort alphabetically, as well as numbers. The COUNTIFS form can also be used as an array formula though it requires the criteria ranges to be references and not arrays 🙁
    
    Multi-criteria sorts can be achieved by adding COUNTIFS. Thus
    
    \= 1 +  
    COUNTIFS(\[Department\],\[Department\],\[Score\],">"&\[Score\]) +  
    COUNTIFS(\[Department\],\[Department\],\[Score\],\[Score\],\[Student\],"<"&\[Student\])
    
    would use the student's name as the tie-break criterion. Not exactly fair but there you go!
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1544740)
    
7.  ![](https://secure.gravatar.com/avatar/e4171cd018508db71a22e9292e3de22fe3273bd7a44d880d3ac297c18b32dab9?s=64&d=mm&r=g) Kenneth Focht says:
    
    [January 3, 2019 at 11:19 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1608828)
    
    Thanks for this great Excel lesson!
    
    I would like some help figuring out how to keep the rank for duplicates. Example: Using your example but changing it up to not copy 100%.....I have a spreadsheet with employees, business areas, years experience, and senority (rank). In my spreadsheet I have ranked by years experience and business area. 2 people in IT rank 2 since they have the same experience. I want to keep it this way. My problem is that the next rank should be 3 but is actually 4.
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1608828)
    
8.  ![](https://secure.gravatar.com/avatar/f32eae9b0f86c714ddabb24149fdf480ad4c27a6b6715494dc19d300c6a7912b?s=64&d=mm&r=g) neelakantan says:
    
    [March 5, 2020 at 8:14 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1754922)
    
    DEAR CHANDOO..  
    I AM HAVING A SITUATION THAT I WANT TO RANK MY STUDENTS BASED ON THEIR TOTAL MARK.  
    I AM HAVING FIVE SUBJECTS. RANKING SHOULD BE DONE IF A STUDENT PASSES IN ALL SUBJECTS, i.e.,HE/SHE SHOULD GET MINIMUM OF 35 IN ALL THE SUBJECTS. I'M TRYING ALL FORMULAE LIKE SUMPRODUCT, COUNTIF AND SO ON.. BUT NONE OF THEM WORKING CORRECTLY. COULD YOU PLEASE HELP ME ..
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1754922)
    
    *   ![](https://secure.gravatar.com/avatar/befa63abfce1c5321ca2704fc397d1ca056cd335ecd37d61312e672ae7f580a1?s=64&d=mm&r=g) Himanshu Jain says:
        
        [April 16, 2020 at 7:53 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1779857)
        
        hi,  
        first of all you can use if along with and function to get check whether the student passed or not...if the student passed then get the sum of the marks...and if the student failed then assign 0 against the total marks =IF(AND(B134>35,C134>35,D134>35,E134>35,F134>35),SUM(B134:F134),0)  
        B134,C134 AND SO ON CELLS CONTAIN THE MARKS....if the condition holds true you will get the sum else you will get 0  
        now you can use rank function on the result that you have got  
        \=RANK(G134,$G$134:$G$136,0)  
        make sure to use descending order so that the student who failed get the last rank  
        students m1 m2 m3 m4 m5 total marks rank  
        a 37 78 45 98 12 0 3  
        s 76 55 44 37 76 288 1  
        d 56 56 76 87 45 37 2
        
        [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1779857)
        
9.  ![](https://secure.gravatar.com/avatar/763da4dbf19700820da047b623057e4f77d5fc748ccc84823b5fe8e83c8075df?s=64&d=mm&r=g) CGI says:
    
    [June 12, 2020 at 8:05 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1809926)
    
    Super easy to follow along! My boss wanted to filter a list by dates that he can change and this fit the bill. Thank you!
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1809926)
    
10.  ![](https://secure.gravatar.com/avatar/34e14efcd195dc5d98e9ef7bb91dbb65304130d8307d5936d6a0683a3e5a442a?s=64&d=mm&r=g) Thomas Crosby says:
    
    [June 26, 2020 at 10:30 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1819793)
    
    I am trying to use the Removing Duplicates from Ranking and not having success. I am using named ranges versus defined rows. Does that make a difference?
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1819793)
    
11.  ![](https://secure.gravatar.com/avatar/b910ded09012e065556d2050b1a393b793b24686d94d22075ab0665aace91de8?s=64&d=mm&r=g) Andrew Wilkins says:
    
    [February 13, 2021 at 2:45 pm](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1974628)
    
    Hi,  
    I have a wonderful application of this technique in analysing the performance of footballers in the the UK Fantasy Premiership game.
    
    Since forever I've been trying to find a way of of ranking players without having to filter them by position, sort them by e.g. descending points and then messing about with copying and pasting as values.
    
    Using this technique I know now that, this week, Fernandes is the highest ranking player by points but is 45th (out of 269 Midfielders) in terms of pts/£ (bcr) which is significant if you need a midfielder on a limited budget.
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1974628)
    
12.  ![](https://secure.gravatar.com/avatar/73ca9fab779ecb6cd8541ea64681f51c70133bbc00e69f73ee85e356dd0780ba?s=64&d=mm&r=g) Arpan Kumar says:
    
    [March 30, 2021 at 6:39 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1987939)
    
    This formula is soo helpful and beautifully explained.  
    However, what if there are "0" zero values in the column and we don't want to consider those 0's as part of the ranking.
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-1987939)
    
13.  ![](https://secure.gravatar.com/avatar/3d4c8808432e63c3bc88774f865df970d6bf4a809a8a8d8cd1302dcba6c4e18e?s=64&d=mm&r=g) Lalitkumar says:
    
    [December 2, 2022 at 8:09 am](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-2109127)
    
    same rank show in two condition raking formula,  
    how to correct this  
    Kindly help
    
    \=SUMPRODUCT(($C$11:$C$28=C11)\*(B11>$B$11:$B$28))+1
    
    [Reply](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#comment-2109127)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How to Distribute Players Between Teams – Evenly](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/) | [Conditional Rank, the easy way \[quick tip\]](https://chandoo.org/wp/pivot-table-rank-example/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)