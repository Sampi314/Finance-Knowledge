# Formula Forensics looks at MaxIf

**Source:** https://chandoo.org/wp/formula-forensics-no-008

---

Formula Forensics No. 008 – Elkhan’s MaxIf
==========================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 31 comments

  

Last week Chandoo received an email from Elkhan, “_I have a data table with several parameters. My aim is to calculate the maximum value of the parameter5 if the parameter3 is “A” and the parameter4 is C1._ _O__f course I can do it by sorting the data by par3 and then by par4 and then subtotaling by max, however I wonder if it can be done by a formula and I am sure it can because I believe Excel has the absolute power to do anything with any set of data. Could you please help me._”

Chandoo responded with a nice Array Formula:

\=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0)) <**Ctrl, Shift, Enter**\>  

So today in Formula Forensics we will have a look at how this **MaxIf** formula works.

As always, please follow along using a sample file you can [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Elkhan-MaxIf.xls "Elkhan MaxIf Sample")

The Max If Formula
------------------

\=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0))

  

### Named Formula

Firstly, we should note that the formula uses 3 Named Ranges. These are **Parameter\_3**, **Parameter\_4** and **Parameter\_5**.

This is good practice as it simplifies the formula and makes the formula more readable and extendable as we will see later.

I think it is clear that:

\=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0))

is much clearer to Read and Understand than

\=MAX(IF((Data1!$D$2:$D$12=D13)\*(Data1!$E$2:$E$12=E13),Data1!$F$2:$F$12,0))

If you open the [Sample File](https://chandoo.org/wp/wp-content/uploads/2012/01/Elkhan-MaxIf.xls "Elkhans Sample File")
 and goto the Name Manager you will see the named formula listed

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/Elk000.png "Elk000")](https://chandoo.org/wp/wp-content/uploads/2012/01/Elk000.png)

Each named formula eg: Parameter\_3 simply refers to a range on the **Data** worksheet

**Parameter\_3**: =Data1!$D$2:$D$12

The Max If Formula
------------------

\=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0))

Reading this formula it is saying, I want the Maximum value of Parameter\_5 If Parameter\_3= the value in D13 and Parameter\_4= the value in E13,

But how does it work.

We can see looking at the above formula that the formula is returning the Maximum value of an If Function.

The formula IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0)

We have seen in previous Formula Forensics, the Excel **If()** function has this format

\=If(Condition, Value if True, Value if False)

**Condition**:  (Parameter\_3=D13)\*(Parameter\_4=E13)

**Value if True**: Parameter\_5

**Value if False**: 0

So this is saying

If (Parameter\_3=D13) and (Parameter\_4=E13) then use the value in Parameter\_5

and

If (Parameter\_3<>D13) or (Parameter\_4<>E13) then use the value **0**

We can check this

In a spare cell, say **F15**, Type:  =(Parameter\_3=D13)\*(Parameter\_4=E13), Press **F9** not Enter

Excel returns: \={1;0;1;0;1;0;0;1;0;0;1}

This is saying that the 1st, 3rd, 5th, 8th and 11th cells all contain values that match our Criteria

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/Elk001.png "Elk001")](https://chandoo.org/wp/wp-content/uploads/2012/01/Elk001.png)

So the 1st, 3rd, 5th, 8th and 11th cells match our criteria, How do we use that to get the values from Column F ?

The Criteria is part of an **If()** Function, which says

If the Criteria is True, Return the value in Parameter\_5 else 0

In another spare cell, Say **F17**, Enter:  \=IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0)

Excel will now return \={0.08;0;0.198;0;0.019;0;0;0.545;0;0;0.246}

This is a list of the values from Parameter\_5 (Column F) that match the If() statement

Note that the 1st, 3rd, 5th, 8th and 11th values contain values and the remaining 2nd, 4th, 6th, 7th, 9th and 10th values contain 0’s as they failed the criteria test in the If() statement.

This array made by the **If()** function is then passed to the **Max()** function

\=MAX({0.08;0;0.198;0;0.019;0;0;**0.545**;0;0;0.246} )

Which you can check in Cell **F19**

Excel returns **0.545** as it should as it is the maximum value in the array.

### Extension

Elkhan hinted in a follow-up email at wanting to extend this to all criteria, not just the 2 criteria questioned.

The beauty of using Named Ranges in these formula is highlighted here where we simply add two more parameters to our Criteria part of the **If()** function, see in Red below.

\=MAX(IF((Parameter\_1=B22)\*(Parameter\_2=C22)\*(Parameter\_3=D22)\*(Parameter\_4=E22),Parameter\_5,0))

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/Elk002.png "Elk002")](https://chandoo.org/wp/wp-content/uploads/2012/01/Elk002.png)
  

We see that Excel returns the correct value of **0.198**, as there are now only two records that match our criteria

DOWNLOAD
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Elkhan-MaxIf.xls "Elkhan's MaxIf Sample")
.

OTHER POSTS IN THIS SERIES
--------------------------

You can learn more about how to pull Excel Formulas apart and how they work internally in the following post:

[Formula Forensic Series:](http://chandoo.org/wp/tag/formula-forensics/ "Show All Formula Forensics")

WE NEED YOUR ONGOING HELP
-------------------------

I have received a few more ideas since last week and these will feature in coming weeks.

However I do need more ideas though and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above, or

If you have a formula that you would like explained but don’t want to write a post also send it in to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Myself](http://chandoo.org/wp/about-hui/ "Contact Hui")
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
| Written by Hui...  <br>Tags: [array formulas](https://chandoo.org/wp/tag/array-formulas/)<br>, [if()](https://chandoo.org/wp/tag/if/)<br>, [max()](https://chandoo.org/wp/tag/max/)<br>, [MaxIf](https://chandoo.org/wp/tag/maxif/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 31 Responses to “Formula Forensics No. 008 – Elkhan’s MaxIf”

1.  ![](https://secure.gravatar.com/avatar/cc4b853fd36b35396620e0b26021ec71636879af745d850dd5b5bcffc2fd5272?s=64&d=mm&r=g) derek says:
    
    [January 24, 2012 at 10:25 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219613)
    
    Instead of multiplying several individual logical tests together, you can also use MMULT to do it in one.
    
    \=MAX(IF(MMULT(--(Parameters1\_4=B22:E22),{1;1;1;1})=4,Parameter\_5,0))
    
    This formula uses a new range that is the combination of all four ranges, and tests that all four are matched. you can change "=4" to ">=3" to test that at least three out of four are matched, and you can replace {1;1;1;1} with {1;2;4;8} to test any combination of matches: "=5" then tests that parameters 1 and 3 are matched, but 2 and 4 are not.
    
    Can anyone simplify this formula (such as eliminating the awkward {1;1;1;1} range)?
    
    Also, can anyone extend this to non-contiguous parameter ranges? I would like to test arbitrary columns in a large data table, but it using INDEX(TABLE,{A,B,C,D},)doesn't seem to work for me to make a range MMULT can use.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219613)
    
    *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
        
        [January 26, 2012 at 1:32 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219690)
        
        Hi Derek,
        
        I've wanted to use MMULT for some time, but could not think of a practical use for it in my line of work...but now you have. Thanks!
        
        As for simplifying the formula, I don't have anything that hasn't been said before, but I would put those array constants in a named formula, which would allow you to easily type it in a formula. If you want to be able to change the number of criteria (for the 2nd array in MMULT) on the fly, rather than having to change the {1;1;1;1} manually, you could set up a little dynamic range that refers with say 4 cells \[A1:D1\] with 1 in each cell and in the named formula do =Transpose(A1:D1), which will give you {1;1;1;1}. And if you add/delete/change criteria, the range will grow/shrink and update the array for MMULT.
        
        As for non-contiguous ranges, try something like this:  
        In a named formula  
        \=CHOOSE({1,2},Data!$B$2:$B$12,Data!$D$2:$D$12)
        
        This will choose both B2:B12 and D2:D12 for the comparison. That is extensible to as many non-contiguous ranges as needed, though they need to be the same size otherwise N/A errors will appear. I'm sure something can be set up to make those ranges dynamic as well.
        
        Also, I'd modify the formula you posted to incorporate the tip that Asa posted below: taking out the ,0 for the false parameter in the IF statement, allowing the formula to pickup negative numbers.
        
        Thanks again for showing a great way for using MMULT.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219690)
        
        *   ![](https://secure.gravatar.com/avatar/cc4b853fd36b35396620e0b26021ec71636879af745d850dd5b5bcffc2fd5272?s=64&d=mm&r=g) derek says:
            
            [January 30, 2012 at 10:00 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219794)
            
            Thanks, CHOOSE works but has the same problem of having to specify each column. So If I have a data table of a hundred columns, four of which are to be chosen using the values in B22:E22, then the expression must be
            
            \=CHOOSE(B22:E22,Data!$B$2:$B$12,Data!$C$2:$C$12,Data!$D$2:$D$12,Data!$E$2:$E$12,\[...and so on until\],Data!$CW$2:$CW$12)
            
            An absurdly long expression.
            
            I tried defining the four columns out of a hundred as a named range, but still no result. But if I array-entered the named range in an actual spreadsheet range somewhere, and pointed the MMULT expression at that, it worked! This is so frustrating, when Excel demands a range and rejects an array expression, but accepts the array expression as long as it's displayed in a range.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219794)
            
    *   ![](https://secure.gravatar.com/avatar/0370bac09b925b6048485cbf11496e12f9e96b1987da48f1f3e33f44df5b0925?s=64&d=mm&r=g) strickep says:
        
        [January 30, 2012 at 10:14 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219813)
        
        Seems to me that the "if" statement isn't required. You'll get the same answer with: =MAX((Parameter\_3=D13)\*(Parameter\_4=E13)\*Parameter\_5)... array entered. Where the parameter conditions aren't true, you still end up with zero values and, where the conditions are true, you end up with the values from parameter\_5. Does the if statement add some value that I am missing? Also, this formula only works if the max is above zero. How can you handle negative values, or taking the minimum?
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219813)
        
        *   ![](https://secure.gravatar.com/avatar/d1e8d85bfb532cf9c104b47724bacf60fb4cdc6de6bc5e398902cc8c427d386e?s=64&d=mm&r=g) Asa says:
            
            [January 31, 2012 at 2:39 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219846)
            
            If comes in handy to allow negatives like this:  
            \=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5))
            
            You can eliminate the 0 for false part of the if(). IF will return a boolean FALSE in those cases, and MAX will ignore them.. so only values that meet your criteria parameters are considered.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219846)
            
2.  ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
    
    [January 24, 2012 at 7:07 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219623)
    
    Good Afternoon Hui. I have been trying to get someone to bit on this. I am not sure if I am giving enough info or not. But here it goes.
    
    I am looking for a financial formula with a little twist. Let say I want to Deposit a sum of money ($500K) into an account that earns a guaranteed interest rate that varies(GIR increases every 5 years by .5% Starting with a 1.5%) This account will pay out a level amount for a stated number of years till the account = $0 (Lets say 21 years). Question... What is the level amount?
    
    My hope is that I can input in individual cells the lump sum deposit and the number of years the account will pay out. Then a separate cell will show the level payout amount.
    
    I have created a calculator and at this time I need to use the Goal Seek function. This is a step I would like to do away with if possible.
    
    If you are interested to take this on,or any one for that matter, please let me know and I can give whatever additional info needed.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219623)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 25, 2012 at 1:39 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219634)
        
        Jim
        
        I have seen your post several times
        
        I am not an accountant by any means and so I would suggest you contact and accountant or review an accounting text book as it seems that should be possible.
        
        Hui...
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219634)
        
        *   ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
            
            [January 25, 2012 at 1:11 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219652)
            
            Hey Hui.
            
            I do not think an accountant would have the kind of understanding in writing formulas in Excel as the people here in any way, shape or form. I could be wrong. The problem would be to call all accountants ask if they know excel formulas and then get charged.  
            if I find one.  
            I am kind of confused, I read all the time people needing help and they get it. I step out and I get see an accountant.? What is it with my need that no one wants to takle it? Is it to hard? Can it not be done?
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219652)
            
            *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
                
                [January 25, 2012 at 4:09 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219661)
                
                Hi Jim,
                
                Follow the link to my skydrive folder and open the workbook called "Annuity with changing interest rates.xlsx". It needs more work to make it more dynamic/flexible but it should get you started. I also included the formula for when the interest rate remains constant.  
                Let me know if the link does not work.
                
                [https://skydrive.live.com/redir.aspx?cid=9a0721b634391421&resid=9A0721B634391421!150&parid=9A0721B634391421!143](https://skydrive.live.com/redir.aspx?cid=9a0721b634391421&resid=9A0721B634391421!150&parid=9A0721B634391421!143)
                
                Kyle
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219661)
                
                *   ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
                    
                    [January 25, 2012 at 6:11 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219675)
                    
                    Kyle,
                    
                    Thank you, but unfortunitly It states "We can't show you that page". I would have loved to take a look at the workbook.
                    
                    Is there another way that you can think of?  
                    You can always connect with me on LinkedIn. See below.
                    
                    [](http://www.linkedin.com/pub/james-hemmerly/34/862/b7)
                    
                    [](http://www.linkedin.com/pub/james-hemmerly/34/862/b7)
                    
                    [](http://www.linkedin.com/pub/james-hemmerly/34/862/b7)
                    
                *   ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
                    
                    [January 25, 2012 at 6:12 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219676)
                    
                    [http://www.linkedin.com/pub/james-hemmerly/34/862/b7](http://www.linkedin.com/pub/james-hemmerly/34/862/b7)
                    
                *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
                    
                    [January 25, 2012 at 7:57 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219680)
                    
                    I'm not on Linkedin or any other networking/social media site for that matter.
                    
                    The previous link directly opened the excel file in the browser; i meant to link to the folder that contains the file, so try this link first, before we try something else:
                    
                    [https://skydrive.live.com/redir.aspx?cid=9a0721b634391421&resid=9A0721B634391421!143&parid=9A0721B634391421!136](https://skydrive.live.com/redir.aspx?cid=9a0721b634391421&resid=9A0721B634391421!143&parid=9A0721B634391421!136)
                    
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [January 26, 2012 at 2:46 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219693)
                    
                    Even if it opens in a Browser just select  
                    File, Download and save it your computer
                    
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [January 26, 2012 at 2:49 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219694)
                    
                    @ Jim & Kyle  
                    I have uploaded Kyles file to my Rapidshare account  
                    You can download it here:  
                    [https://rapidshare.com/files/3058949059/Annuity\_with\_changing\_interest\_rates.xlsx](https://rapidshare.com/files/3058949059/Annuity_with_changing_interest_rates.xlsx)
                    
                *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
                    
                    [January 26, 2012 at 2:51 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219695)
                    
                    I re-posted a cleaned up version, if anyone happened to download it.  
                    Thanks.
                    
                *   ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
                    
                    [January 26, 2012 at 3:20 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219711)
                    
                    Kyle & Hui
                    
                    Thank you for your time. Do you have this in Excel 2003. It only copies vaues into 03.
                    
                *   ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
                    
                    [January 26, 2012 at 5:55 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219715)
                    
                    Hui,  
                    Thanks for posting the file.
                    
                    Jim,  
                    I uploaded the 2003 version to my skydrive folder. Use the second link I posted. If you cannot access the skydrive, then you will have to ask Hui to repost the file to his rapidshare account. I cannot access such sites at this time.
                    
                *   ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
                    
                    [January 27, 2012 at 1:41 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219736)
                    
                    Thank you Kyle.
                    
                    Hui, could you grab the 2003 version and send me a Rapidshare link again?
                    
                    Thanks again guys for all your help.
                    
                    I wish you much success in 2012
                    
                    Jim
                    
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [January 27, 2012 at 2:10 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219737)
                    
                    Here is the 2003 Version on Rapidshare  
                    [https://rapidshare.com/files/1093175066/2003\_Annuity\_with\_changing\_interest\_rates.xls](https://rapidshare.com/files/1093175066/2003_Annuity_with_changing_interest_rates.xls)
                    
            *   ![](https://secure.gravatar.com/avatar/49ba1b45553dc134e8d8c3783511aec692125e9fb32895de95d4f3ffaa5bc586?s=64&d=mm&r=g) Jimhemm says:
                
                [January 27, 2012 at 9:02 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219748)
                
                Thank You!Thank You!Thank You!Thank You!
                
                Wish you all the best!
                
                Jim H.
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219748)
                
3.  ![](https://secure.gravatar.com/avatar/61f624855f677c1065ffb0d764333dfb38930387464f520403adf18ec710d011?s=64&d=mm&r=g) Paul says:
    
    [January 24, 2012 at 7:34 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219624)
    
    Nice job... just one small comment since it tool me a minute to understand why the results were showing #VALUE!.
    
    Press F2 then F9 for 1 time solution or CTRL + SHIFT + ENTER to sustainable solution.
    
    I feel array solutions can be very powerful; however, it is an area of growth for me since I tend to struggle with the purpose of double negatives and array's seperated by "," or "\*", etc.
    
    The graphical explanations are very helpful, e.g. [http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219624)
    
4.  ![](https://secure.gravatar.com/avatar/d1e8d85bfb532cf9c104b47724bacf60fb4cdc6de6bc5e398902cc8c427d386e?s=64&d=mm&r=g) Asa says:
    
    [January 25, 2012 at 1:57 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219636)
    
    Hi Hui and Chandoo! I'd add that if you eliminate the ,0 at the end of the IF function, the formula will work correctly for positive and negative values. As is, if the MAX would be negative, the result if the formula would incorrectly state 0. If you leave the ,0 (value if false part) out, Excel will use FALSE instead of 0 at those positions int he array, and booleans are disregarded entirely by MAX and most other aggregate functions.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219636)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [January 25, 2012 at 7:16 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219648)
        
        Very good tip Asa...
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219648)
        
5.  [Cleaning Up Imported Data - A Brief Case Study | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2012/01/25/cleaning-up-imported-data/)
     says:
    
    [January 25, 2012 at 7:01 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-219647)
    
    \[...\] in Formula Forensics 008 we looked at Elkhans MaxIf \[...\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219647)
    
6.  ![](https://secure.gravatar.com/avatar/89544c1dd5712abd1f6b3194bbb13d9be0c2f50d84caea6f26a21b2628723308?s=64&d=mm&r=g) Kyle McGhee says:
    
    [January 28, 2012 at 5:37 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-219764)
    
    I was picking around this file/topic with my morning coffee and realized with the current setup of the file, the following formula will do the trick.
    
    \=DMAX(B1:F12,F1,B21:E22)
    
    not sure if can be simpler than that!...1 non-array formula
    
    there is one change that is needed for this to work and that is to copy and paste the headers of the table directly above the criteria.  
    i.e. for the sample workbook, copy B1:E1 and paste to B21:E21
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-219764)
    
7.  ![](https://secure.gravatar.com/avatar/5194eb54ab6536661185a1c50a30bc0abaab4e7a52919975227f02565cb2e5c0?s=64&d=mm&r=g) nick says:
    
    [May 15, 2012 at 9:20 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-223902)
    
    the formula is so hard to understand
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-223902)
    
8.  ![](https://secure.gravatar.com/avatar/84e6ba90414fea062ba3fa2e3070d6515b96519629bc448f9bb33ac232ea2f78?s=64&d=mm&r=g) [Annuity Rates UK](http://www.annuityratesuk.org/)
     says:
    
    [May 18, 2012 at 3:44 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-224058)
    
    Nice!  Thank you for sharing this formula.  I will be sharing this with my accountant since it seems accurate and easy to work with. Thanks!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-224058)
    
9.  ![](https://secure.gravatar.com/avatar/84057a754cca0b26cf3f77508270959d04857f2cc11344f41feccf8caea69279?s=64&d=mm&r=g) Kdu Bonalume says:
    
    [July 18, 2012 at 5:15 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-227248)
    
    I sent a similar question to Chandoo a few weeks ago. But, in my case, I was looking for the MIN value. With the above answer, it would fail, because the 0's from the false args are smaller than the values we really want to check. So, I added a IF in the middle, asking if the criterias were false and then, replacing those 0s (and also blank cells that excel convert to zeros) with a huge value (9e99). Then it worked.
    
    Here is the formula:
    
    \=MIN(- -(IF(MONTH(rngDate)=5,1,9E+99))\*(IF(rngDate="",9E+99,rngDate))) **Ctrl+Shift+Enter**
    
    PS: I was looking for the MIN date of a given month in a range with multiple months (in this case, the formula will find the min date for May). 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-227248)
    
10.  ![](https://secure.gravatar.com/avatar/a281c9af605f405d0ca8708201a0fab981b768dfd5414a1a3c06211b053d523f?s=64&d=mm&r=g) Peter says:
    
    [October 23, 2012 at 3:21 pm](https://chandoo.org/wp/formula-forensics-no-008/#comment-275256)
    
    Hi Chandoo,  
    How could be this formula done in VBA? Not using the application.formula statement. I mean how would look like the code?  
    Thanks
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-275256)
    
11.  [How to find the lowest value? \[Quick tip\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2013/08/12/how-to-find-the-lowest-value-quick-tip/)
     says:
    
    [August 12, 2013 at 8:02 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-442959)
    
    \[...\] Finding maximum value subject to conditions – MAXIF \[...\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-442959)
    
12.  ![](https://secure.gravatar.com/avatar/af327b45480d0b0df193c12b96d9f01f48f1cd020c8e8411f4383a10ec06ab6b?s=64&d=mm&r=g) Eric Lind says:
    
    [July 2, 2016 at 5:50 am](https://chandoo.org/wp/formula-forensics-no-008/#comment-1225414)
    
    I love this tip so much!
    
    I'm just now trying a modified version to make SmallIF, and it appears to work exactly as expected.
    
    Thanks Elkhan, Hui, and Chandoo! 😀
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-008/#comment-1225414)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-008/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Excel’s Auditing Functions \[Spreadsheet Risk Management – Part 3 of 4\]](https://chandoo.org/wp/excel-auditing-functions/) | [Cleaning Up Imported Data – A Recent Case Study](https://chandoo.org/wp/cleaning-up-imported-data/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)