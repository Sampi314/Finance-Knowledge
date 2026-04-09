# Extract words from a cell, when they occur in a list of words

**Source:** https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell

---

Formula Forensics No. 34. Extract words from a cell, where they occur in a list of words.
=========================================================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 16 comments

  

At the Chandoo.org Forums user **RMajare** posted a request:

[http://chandoo.org/forums/topic/find-a-list-of-words-in-a-cell](http://chandoo.org/forum/threads/find-a-list-of-words-in-a-cell.8278/ "http://chandoo.org/forum/threads/find-a-list-of-words-in-a-cell.8278/#post-47624")

His request was to list all names that appeared in the sentence to be shown in one cell separated by commas.

While it is possible with a dash of VBA (Google for [ACONCAT by Harlan Grove](http://www.mrexcel.com/forum/excel-questions/510382-harlan-groves-custom-function.html "Shortcut")
), Excel formulas straight away do not provide this flexibility using the CONCATENATE function.

So Shrivallabha suggested an alternative which was to list the words found across columns.

This post written by Shrivallabha will explain how his solution works.

As always at formula Forensics You can follow along in a sample file here: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2013/09/FF34-sample.xlsx "Download Sample File")

Objective
---------

Cells _B3:B12 \[Namelist _Column_\]_ holds a list of names which are to be searched in sentences in the Cells _C3:C7 \[Sentence Column\]_.

The results are then to be listed across starting from cell _D3 \[_Formula_ Columns\]_.

So we will write a formula in Cell _D3_ and then copy it down and across.

**Note:** We could have easily kept the _Sentence_ column to the left of _NameList_ but we may need free space to keep adding columns in _Formula section_ and we don’t know how many columns we’ll need. This arrangement ensures that we don’t have to change layout to adjust.

Formula
-------

Here’s the formula used which needs to be array entered in Cell _D3_:

\=IFERROR(INDEX(NameList,SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)-2),COLUMNS($D$2:D2))),”-“) then press **Ctrl+Shift+Enter**  

Where, **NameList** is a named formula which refers to the Range **_B3:B12_**.

**Note:** The formula above can be used for Excel Versions 2007 and above. For Excel Versions 2003 and previous we’ll need to resort to **\=IF(ISERROR(_Formula_),_Formula_,”-“)**

or

\=If(Iserror( INDEX(NameList,SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)-2),COLUMNS($D$2:D2))) ), INDEX(NameList,SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)-2),COLUMNS($D$2:D2))),”-“)

Now let’s understand how above first formula works

Always remember, any complex formula is made up of more than one formula similar to a big program built up using small sub-routines.

To begin with, it may seem daunting but as you delve deeper and break the formula down to basic functions then it is just becomes a matter of understanding the inter-dependency of these basic functions with one another.

We’ll do the same to understand this formula.

By doing away with IFERROR what remains is the core formula which gets us the results we are interested in:

\=IFERROR(INDEX(NameList,SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)-2),COLUMNS($D$2:D2))),”-“)

We will examine the internal formula starting with Index

INDEX(NameList,SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)-2),COLUMNS($D$2:D2)))

We are using INDEX which is one of the frequently used functions in Excel which has following construct:

\=INDEX(_array, row\_num, column\_num_)

This function returns an element based on the _row\_num_, _column\_num_ arguments passed e.g. if we write formula as:

\=INDEX(A1:E5, 2, 3)

Then it will return value in Cell _C2_.

We use this function to return the match found in Named Range “**NameList**”.

To find out the name that exists in given sentence we use following construct:

IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)-2)

Here we need to use Excel’s “Evaluate Formula” functionality which shows the steps that Excel takes internally to arrive at the result.

“Evaluate Formula” is accessed by selecting part of the formula and pressing F9 and will show results as below for Cell _D3_:

*   The NameList array will be searched up like IF(ISNUMBER(FIND(**{“Alka”;”Aniket”;”Anil”;….;”Vrunda”}**,$C3,1)),ROW(NameList)-2).

**Note:** **SEARCH** function shall be used in place of **FIND** if we do not need search to be case sensitive.

*   And then it will be searched in sentence cell _C3_ which will result in array which has numerical results along with #value! errors like IF(ISNUMBER(**{1;#value!; #value!;….;10; #value!}**),ROW(NameList)-2).
*   **ISNUMBER** is another useful function which handles errors and numerical results (**#value!**) and creates BOOLEAN results as required by **FIND** function as IF(**{TRUE;FALSE;FALSE;….;TRUE; FALSE}**),ROW(NameList)-2).
*   The **ROW(NameList)** function returns results as **{3;4;5;6;7;…;11;12}** so when we are processing these results which come from if function. So the numerical results will be correlated with following TRUE results: {3, 11}.
*   If we look at our **NameList** array then they will refer to 3rd and 11th row respectively. But our data has only 10 elements and 3rd element is “Anil” which is incorrect and then 11 will cause #REF error. What you’ll notice is the result is always offset by 2 rows. That is because our data range starts at 3rd row. So we adjust it by subtracting 2 from it. So it refers to correct results: {1, 9}.

I hope by now we have understood how we use above IF construct to get the results. At this point, you might be still wondering why we used **SMALL** function around **IF.**

SMALL(_If\_function_, n)

*   We have multiple results and we need to show one result at a time which is done by SMALL(_If\_formula_, COLUMNS($D$3:D3)).

COLUMNS ($D$3:D3) results in 1 in cell _D3_ i.e. count of columns.

As we copy across _$D$2_ remains constant and _D2_ changes.

So in _E2_ the value becomes 2, in _F2_ it becomes 3 and so forth.

*   So in cell _D3_ we get first result of **SMALL** formula i.e. 1 and therefore it returns “Alka” and in _E3_ “Vinay” and then there is no third match in _F3_ so INDEX formula errors out which is then handled by IFERROR function.

Refer the attached workbook and play with it.

I hope this formula helps you somewhere someday.

_**Shrivallabha**_

DOWNLOAD
--------

You can download a copy of the above file and follow along, [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2013/09/FF34-sample.xlsx "Download Sample File")
.

**OTHER POSTS IN THIS SERIES**
------------------------------

The Formula Foerensics Series contains a wealth of useful solutions and information.

You can learn more about how to pull Excel Formulas apart in the following posts: [http://chandoo.org/wp/formula-forensics-homepage/](http://chandoo.org/wp/formula-forensics-homepage/ "Formula Forensics Homepage")

THANK-YOU and a CHALLENGE
-------------------------

Firstly, Congratulations to **Shrivallabha** on taking up the challenge and on your First Post at Chandoo.org.

Thank-you for explaining to us all how this formula, which has appeared a number of times on the [Chandoo.org Forums](http://chandoo.org/forum/ "Chandoo.org Forums")
, works.

### Your Challenge?

If you have a clever formula and would like to become an author here at Chandoo.org please consider writing it up as Shrivallabha has done above.

You can submit it to [Chandoo](http://chandoo.org/wp/contact/ "Contact Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
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
| Written by Hui...  <br>Tags: [columns()](https://chandoo.org/wp/tag/columns/)<br>, [find](https://chandoo.org/wp/tag/find/)<br>, [iferror](https://chandoo.org/wp/tag/iferror/)<br>, [Index(). Small()](https://chandoo.org/wp/tag/index-small/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 16 Responses to “Formula Forensics No. 34. Extract words from a cell, where they occur in a list of words.”

1.  ![](https://secure.gravatar.com/avatar/42bd63ea0d64697e2e562a86d6e2a349e353b6ab006b1ddc3fff4bbda791c2b9?s=64&d=mm&r=g) Elias says:
    
    [September 12, 2013 at 2:10 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445780)
    
    Different approach and same results, but different order. However, it doesn’t get mess if you insert rows before NameList range.
    
    \=IFERROR(LOOKUP(0,-FIND(NameList,$C3)/(COUNTIF($C$3:C3,NameList)=0),NameList),"-")
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445780)
    
2.  ![](https://secure.gravatar.com/avatar/0f06096fbc06cd5d43fad1f3a2f6090c2cd7756f154c6e0709da3939b54b153c?s=64&d=mm&r=g) Robert says:
    
    [September 12, 2013 at 9:27 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445795)
    
    thanks, i used it today (with modification) and works great (haven't really used array formulas much in the past).
    
    a slight modification, depending on what you're doing, to get around the case where rows above NameList may be added or deleted  
    \=IFERROR(INDEX(B:B,SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),ROW(NameList)),COLUMNS($D$2:D2))),”-”)  
    ("INDEX(NameList" >> "INDEX(B:B" .... "ROW(NameList)-2" >> drop the "-2")
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445795)
    
3.  ![](https://secure.gravatar.com/avatar/42bd63ea0d64697e2e562a86d6e2a349e353b6ab006b1ddc3fff4bbda791c2b9?s=64&d=mm&r=g) Elias says:
    
    [September 12, 2013 at 9:54 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445796)
    
    If order is important here is another option,
    
    \=IFERROR(INDEX(NameList,MATCH(1,ISNUMBER(FIND(NameList,$C3))/(COUNTIF($C$3:C3,NameList)=0),0)),"-")
    
    Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445796)
    
4.  ![](https://secure.gravatar.com/avatar/3f690fb41d94e8f40e86e29c0393a1cedfa6f246ceda474909739bbe73588852?s=64&d=mm&r=g) Hamza asghar says:
    
    [September 13, 2013 at 4:48 am](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445823)
    
    Good morning chando Sir, i am Hamza asghar s/o asghar ali i am 11 yrs old & 6th class student , i have my desktop computer but sometime i use my papa's laptop & and his e.mail ID too. i like to understand excel , as like as you hav command on its. can will you teach me ?? i like to know all formulas but easy . i am waiting for ur reply .  
    Best Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445823)
    
5.  ![](https://secure.gravatar.com/avatar/277ba8442ad34ff3999a69b2f194f2c6726bf89c5e219572a5a877222855b865?s=64&d=mm&r=g) Priyanka Poojari says:
    
    [September 14, 2013 at 7:09 am](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445977)
    
    alternate method could be  
    DATA - TEXT TO COLUMNS -DELIMITED - COMMAS. (put symbol ( , )- FINISH
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-445977)
    
    *   ![](https://secure.gravatar.com/avatar/be0942581ecf6840ea793380b8ea9cc3b0c55d1890674298d87ad1ac87d70b0c?s=64&d=mm&r=g) shrivallabha says:
        
        [September 17, 2013 at 6:45 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-446217)
        
        Priyanka,
        
        Check out the workbook and requirement. Those words are interspersed in the sentence.
        
        e.g.  
        Ram likes to visit Durgapur
        
        Namelist has Ram, Shyam, Seeta.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-446217)
        
6.  ![](https://secure.gravatar.com/avatar/97a03975012b3492790508983b16d58753e86cb5ab267efd40715aae8eb9e88b?s=64&d=mm&r=g) Aditya says:
    
    [September 16, 2013 at 12:03 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-446125)
    
    Nice formula
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-446125)
    
7.  ![](https://secure.gravatar.com/avatar/8ceae07ad389f92037be72df1988137e1d17a29339ab2d5c34385d27a027ad2f?s=64&d=mm&r=g) Ola says:
    
    [September 21, 2013 at 8:42 am](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-446652)
    
    Isn't it time for Excel to become simpler.  
    The same basic problems has existed for years, giving rise to ever more elaborate work around's.
    
    Even though they can be fun to make/decipher. Isn't it time to find the missing main building blocks (formulas) that could make Excel simpler in the long run.
    
    For example =concatenate() that still can not concatenate an array. Isn't Harlan Grove's Aconcat work around (which must be more than 10 years old) a prime example of a problem that has existed for years and still has no simple solution.  
    Or am I just getting old.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-446652)
    
    *   ![](https://secure.gravatar.com/avatar/a0297802d4d0639c3c3d01f8a80b99004089f5949b7126dc0b2c4a04ea70ec15?s=64&d=mm&r=g) Anon says:
        
        [October 2, 2013 at 11:21 am](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-447817)
        
        An ugly modification to the formula which will give you the names in the order they appear in the sentence (in cell c3).
        
        \=IFERROR(INDEX(NameList,MATCH(SMALL(IF(ISNUMBER(FIND(NameList,$C3,1)),FIND(NameList,$C3,1),FALSE),COLUMNS($D$2:D2)),IF(ISNUMBER(FIND(NameList,$C3,1)),FIND(NameList,$C3,1),FALSE),0)),"-")
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-447817)
        
8.  ![](https://secure.gravatar.com/avatar/155322585990f135bb5146c4fd38811aa2170227db45e14bbebc46b95a86ce17?s=64&d=mm&r=g) Haseeb A says:
    
    [October 3, 2013 at 2:19 am](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-447870)
    
    Here is another one, which will extract in order as they appear in NameList. Also will ignore DUPLICATE, if there is.
    
    \=IFERROR(INDEX(NameList,MATCH(0,0\*FIND(IF(ISNA(MATCH(NameList,$C3:C3,0)),NameList),$C3),0)),"-")
    
    To compatibility with all versions,
    
    \=LOOKUP("zzz",IF({1,0},"-",INDEX(NameList,MATCH(0,0\*FIND(IF(ISNA(MATCH(NameList,$C3:C3,0)),NameList),$C3),0))))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-447870)
    
9.  ![](https://secure.gravatar.com/avatar/3ebdf8758f9098840a6c69900371010cb94c9777e126032d99c2aa025ec81af8?s=64&d=mm&r=g) Renan says:
    
    [August 5, 2015 at 5:36 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1019281)
    
    Hi,  
    I am having a slight problem with the formula shown.  
    The first time I use, it returns some incorrect values, but if I Press F2 and F9, the value returned is correct.
    
    Can you help me with that?  
    Best Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1019281)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [August 6, 2015 at 12:30 am](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1019397)
        
        @Renan
        
        Did you press Ctrl+Shift+Enter instead of Enter after originally entering the formula ?
        
        Pressing F2, then F9 is effectively doing that
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1019397)
        
10.  ![](https://secure.gravatar.com/avatar/d6d22b29c8d4d1f6abb6a948351cdca1bd3b041a73b99961adf3978623344225?s=64&d=mm&r=g) Giuseppe says:
    
    [January 2, 2016 at 7:53 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1115346)
    
    Hi all, Im trying to follow all your amazing solution(really are great congrats), but Im not able to apply them on my case. I'll try to explain briefly. Have 3 columns Like these below
    
    1a. City |1b.Data ||| 2. Universities  
    Rome | 20% ||| University of Padua blablabla  
    Pisa | 5% ||| University of Rome blablabla  
    Bologna | 17% ||| University of Palermo Blablabla  
    ||| University of Pisa blablabla  
    ||| University of Something
    
    What im trying to do is something like:
    
    If the first cell of Tab Universities contains one of the cities from table 1.a City, then write in another cell the corresponding value from 1b.Data. that corresponds to the found city.
    
    Do u may have some suggestions?
    
    Thank u all for your time
    
    G
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1115346)
    
11.  ![](https://secure.gravatar.com/avatar/49be073ac55924cbc11b614564f3ce87d45482ac1e64544cc1010c45445b14f0?s=64&d=mm&r=g) Jenny says:
    
    [January 14, 2016 at 11:22 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1120123)
    
    Just loved the sample file tutorial! With its step-by-step instructions & illustrations I was able to modify the formula to meet my particular needs! Thanks for the assistance you didn't know you were giving.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1120123)
    
12.  ![](https://secure.gravatar.com/avatar/3caf5ab4e9d8d18468054b319d5eb88027c258d600eb6136c58fa566dfb0b245?s=64&d=mm&r=g) Indra Kusuma says:
    
    [June 2, 2018 at 3:48 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1550535)
    
    [https://eileenslounge.com/viewtopic.php?f=27&t=30006](https://eileenslounge.com/viewtopic.php?f=27&t=30006)
    
    Interesting, this has been my case for many years. Macro code on above link can be an option.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-1550535)
    
13.  ![](https://secure.gravatar.com/avatar/79302d23f014eb8ee1d7fc87e9694a6ea0e63a019b152c1557fbebcb8e773de9?s=64&d=mm&r=g) Siavash says:
    
    [May 4, 2022 at 9:06 pm](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-2076462)
    
    Hi Chandoo, many thanks for your great tutorial. It helped me a lot and saved me a lot of time and effort. Great job!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#comment-2076462)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-34-find-a-list-of-words-in-a-cell/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Calculating average of every nth value \[Formula tips\]](https://chandoo.org/wp/calculating-average-of-every-nth-value-formula-tips/) | [Using Arrays To Update Table Columns](https://chandoo.org/wp/using-arrays-to-update-table-columns/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)