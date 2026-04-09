# Find out if a number has repetitive digits [formula homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/number-has-repetitive-digits-formula

---

Find out if a number has repetitive digits \[formula homework\]
===============================================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 - 56 comments

  

Time for a quick formula finesse check. Let’s say you have a number in A1. **What formula can you use to find out if it has duplicate digits**.

![](https://chandoo.org/wp/wp-content/uploads/2017/10/number-has-repetitive-digits.png)For example, if A1 has 123405, then answer should be FALSE  
and if A1 has 123455, then answer should be TRUE

**_Go ahead and post your answers (formulas, VBA or M script) in the comments section_**.

**Clues and hints**

Check out below formula tips to get some clues on how to solve this problem.

*   [Check if a range has 1 to n numbers](https://chandoo.org/wp/2016/09/30/check-if-a-range-has-all-numbers/)
    
*   [Check if a range has duplicate values](https://chandoo.org/wp/2012/06/28/check-list-for-duplicate-numbers/)
    
*   [One more way to check if a list has duplicate items](https://chandoo.org/wp/2009/03/25/using-array-formulas-example1/)
    

**More home work:**

Why not indulge in some cheese, wine and Excel? That is how I like to enjoy my Tuesdays. Take up these homework problems to work out your formula muscles.

*   [How many employees are away during that big game?](https://chandoo.org/wp/2017/04/07/how-many-employees-are-on-leave-during-easter-holidays-homework/)
    
*   [Can you solve the blood pressure problem?](https://chandoo.org/wp/2016/11/04/bp-category-problem/)
    
*   More [home work](http://chandoo.org/wp/tag/homework)
     and [challenges](https://chandoo.org/wp/category/excel-challenges/)
    

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
| Written by Chandoo  <br>Tags: [duplicates](https://chandoo.org/wp/tag/duplicates/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [unique](https://chandoo.org/wp/tag/unique/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 56 Responses to “Find out if a number has repetitive digits \[formula homework\]”

1.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
     says:
    
    [October 3, 2017 at 10:01 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513734)
    
    \=ISNUMBER(MODE(--MID(A1,ROW(OFFSET(A1,,,LEN(A1))),1)))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513734)
    
2.  ![](https://secure.gravatar.com/avatar/549f0f05e61393eca81e962cd1a516d56a4078f8737b04ea652e80dc45e70cb1?s=64&d=mm&r=g) Black Moses says:
    
    [October 3, 2017 at 11:27 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513754)
    
    My solution isn't very elegant, but it works:
    
    \=IF(ISERROR(SUM(1\*SUBSTITUTE(A1,ROW($A$1:$A$10)-1,"x",2))),TRUE,FALSE)
    
    Entered as CSE of course
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513754)
    
    *   ![](https://secure.gravatar.com/avatar/384f7e1fad91b1e90ce2f79dc014b35f72d3d1d88cab22be283fe73808a8a9ef?s=64&d=mm&r=g) Asheesh says:
        
        [October 4, 2017 at 7:40 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513983)
        
        Hi,
        
        There is no need to use IF function in the proposed solution..
        
        ISERROR(SUM(1\*SUBSTITUTE(A1,ROW($A$1:$A$10)-1,"x",2)))
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513983)
        
        *   ![](https://secure.gravatar.com/avatar/549f0f05e61393eca81e962cd1a516d56a4078f8737b04ea652e80dc45e70cb1?s=64&d=mm&r=g) Black Moses says:
            
            [October 4, 2017 at 9:58 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514011)
            
            Haha you're right of course, thanks
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514011)
            
3.  ![](https://secure.gravatar.com/avatar/5429b39774f039a27e6d637d3c6ac2f288edcc315710479f944519f7bfa4464b?s=64&d=mm&r=g) Hossat says:
    
    [October 3, 2017 at 1:08 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513774)
    
    for french users :  
    \=ESTNUM(MODE(--STXT(A11;LIGNE(DECALER($A$1;;;NBCAR(A11)));1)))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513774)
    
4.  ![](https://secure.gravatar.com/avatar/aa687df58e3eef4947e1d25590c7637f19edf271bf711f93a2ce843289e52dcb?s=64&d=mm&r=g) Bob says:
    
    [October 3, 2017 at 1:11 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513776)
    
    \=(MID(A38,LEN(A38)-1,1)-RIGHT(A38,1))=0
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513776)
    
5.  ![](https://secure.gravatar.com/avatar/4db989f6b4667dd871e354866e877dc975b67efdb49b6e1ac8aeaceee17b3464?s=64&d=mm&r=g) RingBinder says:
    
    [October 3, 2017 at 1:30 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513781)
    
    {=LEN(A1)>MIN(LEN(SUBSTITUTE(A1,REPT(ROW($A$1:$A$10)-1,2),"")))}
    
    CSE formula
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513781)
    
6.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) [David Hager](https://dhexcel1.wordpress.com/)
     says:
    
    [October 3, 2017 at 1:38 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513782)
    
    Repetitive digits is different than duplicate digits. For example, 123454 would have duplicate digits whereas 123445 would have repetitive digits. Which did you want?
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513782)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [October 3, 2017 at 3:31 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513796)
        
        Both.
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513796)
        
        *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) [David Hager](https://dhexcel1.wordpress.com/)
             says:
            
            [October 3, 2017 at 7:54 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513843)
            
            [https://twitter.com/dhExcel/status/915238696286347266](https://twitter.com/dhExcel/status/915238696286347266)
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513843)
            
        *   ![](https://secure.gravatar.com/avatar/5236c611eb079e607e221e7b6641b52ff0fc1e404d74f725a49ab3e9d0bf8955?s=64&d=mm&r=g) Bhagwat says:
            
            [February 9, 2021 at 11:00 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1974157)
            
            What is the right answer?
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1974157)
            
7.  ![](https://secure.gravatar.com/avatar/9a549fca4e5e262f141e615c69fe15de125cf44636de0a41543548fc2cf5157a?s=64&d=mm&r=g) Tom Smith says:
    
    [October 3, 2017 at 1:43 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513783)
    
    The easiest way for numbers would be using SUBSTITUTION calculations, such as:
    
    \=IF(LEN(B2)-LEN(SUBSTITUTE(B2,"0",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"1",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"2",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"3",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"4",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"5",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"6",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"7",""))>1,TRUE,  
    IF(LEN(B2)-LEN(SUBSTITUTE(B2,"8",""))>1,TRUE,IF(LEN(B2)-LEN(SUBSTITUTE(B2,"9",""))>1,TRUE,FALSE))))))))))
    
    If you want to know which digit had the most, you could simply use the logic portion comparing each number:
    
    \=LEN(B2)-LEN(SUBSTITUTE(B2,"5",""))
    
    This way it doesn't matter where in the string the duplication of digits occurs, they all will be "counted."
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513783)
    
8.  ![](https://secure.gravatar.com/avatar/b78f96961d5b35d266480e8fc8058e910aca72c585bb0fbc81350ac30f0b670e?s=64&d=mm&r=g) Dave Ramage says:
    
    [October 3, 2017 at 1:50 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513784)
    
    Similar to Tom's solution, but array entered to save some typing!
    
    \=(LEN(A1)-MIN(LEN(SUBSTITUTE(A1,ROW($A$1:$A$10)-1,""))))<2
    
    Cheers,  
    Dave
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513784)
    
    *   ![](https://secure.gravatar.com/avatar/6c6b4e770fff1b8023b83395a4bcf85866db21b952c8328ac83fb67310e05508?s=64&d=mm&r=g) Tonosam says:
        
        [October 5, 2017 at 7:00 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514209)
        
        Great! May be you coud use {0,1,2,3,4,5,6,7,8,9} instead ROW() for clarity but it's a great solution anyway.
        
        Thank you for sharing!
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514209)
        
9.  ![](https://secure.gravatar.com/avatar/eb185de62ca0d5a1a9176efa5144fef3dd1d136d6dd62de4cd40d25817477770?s=64&d=mm&r=g) Steve says:
    
    [October 3, 2017 at 3:56 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513802)
    
    Similar to Tom Smith's solution, just run through all the cases:  
    \=0<IFERROR(SEARCH("00",B1),0)+IFERROR(SEARCH("11",B1),0)+IFERROR(SEARCH("22",B1),0)+IFERROR(SEARCH("33",B1),0)+IFERROR(SEARCH("44",B1),0)+IFERROR(SEARCH("55",B1),0)+IFERROR(SEARCH("66",B1),0)+IFERROR(SEARCH("77",B1),0)+IFERROR(SEARCH("88",B1),0)+IFERROR(SEARCH("99",B1),0)
    
    As I'm ready to post, it appears this is not what you wanted. Oh well, it may be useful to someone in the future. I know I've found many solutions in the Chandoo comments section.
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513802)
    
    *   ![](https://secure.gravatar.com/avatar/9df4c772feeaa2f3745b31e6829a57c29d308cb57406a955b7d4e516effb88d5?s=64&d=mm&r=g) UniMord says:
        
        [October 3, 2017 at 8:33 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513850)
        
        A simpler solution, but, along the same lines:  
        \=COUNT(SEARCH({"00","11","22","33","44","55","66","77","88","99"}, A1))>0
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513850)
        
        *   ![](https://secure.gravatar.com/avatar/9df4c772feeaa2f3745b31e6829a57c29d308cb57406a955b7d4e516effb88d5?s=64&d=mm&r=g) UniMord says:
            
            [October 3, 2017 at 8:37 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513851)
            
            Note: Only the "00" needs to be a string - otherwise, it'll turn into a single 0. All the others can be numbers, but, it seemed sloppy to me to have an array of one string and 9 numbers.
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513851)
            
10.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [October 3, 2017 at 6:26 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513822)
    
    \=IF(MOD(MID(A1,LEN(A1)-1,2),11)=0,"Duplicate Digits","")
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513822)
    
    *   ![](https://secure.gravatar.com/avatar/2f453e74af5b89fc30ab301b58a751d147f6366ba7b74ad1e857b5097346242b?s=64&d=mm&r=g) Greg G says:
        
        [October 4, 2017 at 3:34 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514057)
        
        This only works if duplicate (repeated) numbers are last 2 digits of the number, ie. 12345677, due to MID(A1, LEN(A1)-1, 2). If the dupicates are the first numbers (112345) or not repeated side by side (123145, note the 1's) then the formula will return the FALSE result.
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514057)
        
        *   ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
            
            [October 6, 2017 at 4:54 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514524)
            
            The example by chandoo stated only last two digits!
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514524)
            
11.  ![](https://secure.gravatar.com/avatar/16dcd8a859ed0d598472c65539bb0fecce294ace8f86497c039fd08190ce77ef?s=64&d=mm&r=g) Faseeh says:
    
    [October 3, 2017 at 6:40 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513828)
    
    This one too..
    
    \=IF(MOD(D3-ROUNDDOWN(D3,-2),11)=0,"Duplicate","")
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513828)
    
12.  ![](https://secure.gravatar.com/avatar/9df4c772feeaa2f3745b31e6829a57c29d308cb57406a955b7d4e516effb88d5?s=64&d=mm&r=g) UniMord says:
    
    [October 3, 2017 at 6:58 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513830)
    
    {=IFNA(MATCH(0, MOD(MID(A1&"|",ROW(INDIRECT("1:"&LEN(A1)+1)),1)&MID("|"&A1,ROW(INDIRECT("1:"&LEN(A1)+1)),1),11), 0)>0, FALSE)}
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513830)
    
13.  ![](https://secure.gravatar.com/avatar/9df4c772feeaa2f3745b31e6829a57c29d308cb57406a955b7d4e516effb88d5?s=64&d=mm&r=g) UniMord says:
    
    [October 3, 2017 at 7:48 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513842)
    
    To determine if there are any duplicates, consecutive or otherwise:
    
    \=MAX(FREQUENCY(--MID(A1,ROW(INDIRECT("1:" & LEN(A1))), 1), {0,1,2,3,4,5,6,7,8,9}))>1
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513842)
    
14.  ![](https://secure.gravatar.com/avatar/3502aaa90ca3d1a86a284f6843e52996e8271cf2c0c04a31bfaab2cc630b5788?s=64&d=mm&r=g) Bill Szysz says:
    
    [October 4, 2017 at 12:44 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513892)
    
    For text and numbers - my proposal (CSE formula)  
    \=OR(FREQUENCY(CODE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)),CODE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)))>1)
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513892)
    
15.  ![](https://secure.gravatar.com/avatar/3502aaa90ca3d1a86a284f6843e52996e8271cf2c0c04a31bfaab2cc630b5788?s=64&d=mm&r=g) Bill Szysz says:
    
    [October 4, 2017 at 12:49 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513893)
    
    I do not know why my formula was cutted in my previous post, so this is next try  
    \=OR(FREQUENCY(CODE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)),  
    CODE(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)))>1)
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513893)
    
16.  ![](https://secure.gravatar.com/avatar/3502aaa90ca3d1a86a284f6843e52996e8271cf2c0c04a31bfaab2cc630b5788?s=64&d=mm&r=g) Bill Szysz says:
    
    [October 4, 2017 at 12:55 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513896)
    
    Here is a code for PQ  
    let  
    Source = Excel.CurrentWorkbook(){\[Name="tblNumbers"\]}\[Content\],  
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"TextOrNumbers", type text}}),  
    #"Added Custom" = Table.AddColumn(#"Changed Type", "Result", each List.Distinct(Text.ToList(\[TextOrNumbers\])) Text.ToList(\[TextOrNumbers\]) )  
    in  
    #"Added Custom"
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513896)
    
17.  ![](https://secure.gravatar.com/avatar/3502aaa90ca3d1a86a284f6843e52996e8271cf2c0c04a31bfaab2cc630b5788?s=64&d=mm&r=g) Bill Szysz says:
    
    [October 4, 2017 at 12:59 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513898)
    
    hmm... this site cut some part of the code so this is challenge for readers to put in the last step in correct place two signs :-))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513898)
    
18.  ![](https://secure.gravatar.com/avatar/f1b558f49b2be9258ba01b30fd11270b4aa0d3bf365a0d0c89d3ce6eaabf4e0e?s=64&d=mm&r=g) Alok Kumar Jena says:
    
    [October 4, 2017 at 4:36 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513933)
    
    Hi Team,
    
    Find the repeated number from cell either true or false by this formula.
    
    \=COUNT(SEARCH(REPT({1,2,3,4,5,6,7,8,9},2),A2))>0
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513933)
    
    *   ![](https://secure.gravatar.com/avatar/92f6db045719630ef748b06e7407ae1e40df13f0f57d447085d4cd3dbce5ba63?s=64&d=mm&r=g) NItin says:
        
        [October 4, 2017 at 2:51 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514051)
        
        Its not a give correct Output when you apply this function on when duplicate number not in consecutive seq.  
        For Example:-102565
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514051)
        
        *   ![](https://secure.gravatar.com/avatar/f1b558f49b2be9258ba01b30fd11270b4aa0d3bf365a0d0c89d3ce6eaabf4e0e?s=64&d=mm&r=g) Alok Kumar Jena says:
            
            [October 14, 2017 at 12:03 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1516235)
            
            It's asking about repetitive number means continue like (12344) not like 102565.
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1516235)
            
    *   ![](https://secure.gravatar.com/avatar/8f2968a246416722d4d0ef90986f2e8254b344a9b83934be2b7d9096c05690f2?s=64&d=mm&r=g) lori says:
        
        [October 6, 2017 at 12:36 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514489)
        
        that does consecutive digits, a small tweak might do the trick:
        
        \=COUNT(SEARCH(REPT({0,1,2,3,4,5,6,7,8,9}&"\*",2),A2))>0
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514489)
        
19.  ![](https://secure.gravatar.com/avatar/384f7e1fad91b1e90ce2f79dc014b35f72d3d1d88cab22be283fe73808a8a9ef?s=64&d=mm&r=g) Asheesh says:
    
    [October 4, 2017 at 7:43 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513984)
    
    One more for the sake of fun
    
    Solution for duplicates or consecutive or otherwise
    
    LEN(A1)>COUNT(IFERROR(SEARCH(ROW(A1:A10)-1,A1),""))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513984)
    
20.  ![](https://secure.gravatar.com/avatar/a96812162ecaadcfd666346bace7214aac1bfd61457d2a56e38510a4a005560d?s=64&d=mm&r=g) Rishi Kumar says:
    
    [October 4, 2017 at 7:56 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513986)
    
    Use below function in Cell b2 and put the number in cell A2.
    
    \=MODE(--MID(A2,ROW(OFFSET($A$1,,,LEN(A2))),1))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513986)
    
21.  ![](https://secure.gravatar.com/avatar/a96812162ecaadcfd666346bace7214aac1bfd61457d2a56e38510a4a005560d?s=64&d=mm&r=g) Rishi Kumar says:
    
    [October 4, 2017 at 7:57 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513987)
    
    \=IFERROR(MODE(--MID(A2,ROW(OFFSET($A$1,,,LEN(A2))),1)),"")
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1513987)
    
22.  ![](https://secure.gravatar.com/avatar/c72d023366260ebef49fa7df98159f503f920992df6e18250421b1ab86019c06?s=64&d=mm&r=g) John Jairo V says:
    
    [October 4, 2017 at 5:45 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514076)
    
    Your solution can avoid IFERROR:
    
    With CSE:  
    \=LEN(A1)>COUNT(SEARCH(ROW(1:10)-1,A1))
    
    Without CSE:  
    \=LEN(A1)>COUNT(INDEX(SEARCH(ROW(1:10)-1,A1),))
    
    Blessings!
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514076)
    
23.  ![](https://secure.gravatar.com/avatar/036392219fa42f7d54e74786f1e7bc769c17f67a3361e3ddb8a77d92c3db9647?s=64&d=mm&r=g) Sunny says:
    
    [October 5, 2017 at 2:14 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514146)
    
    \=LEN(A1) NE COUNT(SEARCH({"0","1","2","3","4","5","6","7","8","9"}, A1))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514146)
    
24.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [October 5, 2017 at 4:33 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514181)
    
    \=SUMPRODUCT(--(FREQUENCY(VALUE(MID(A1,ROW($A$1:INDEX(A:A,LEN(A1))),1)),{0,1,2,3,4,5,6,7,8,9})>1))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514181)
    
25.  ![](https://secure.gravatar.com/avatar/9b019c3e6f174eec375c6e0ea4da3c75df50f39a4849c92a11f937ae7fc81446?s=64&d=mm&r=g) Venky says:
    
    [October 5, 2017 at 1:23 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514266)
    
    Thanks John, this is clever
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514266)
    
26.  ![](https://secure.gravatar.com/avatar/62ca8680f3f6e0a22e72ecdb344e6c10cb805240dd0a56f4e4f68e763dcc5197?s=64&d=mm&r=g) Vipul Patel says:
    
    [October 6, 2017 at 6:00 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514425)
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    #"Split Column by Position" = Table.ExpandListColumn(Table.TransformColumns(Table.TransformColumnTypes(Source, {{"Column1", type text}}, "en-IN"), {{"Column1", Splitter.SplitTextByRepeatedLengths(1), let itemType = (type nullable text) meta \[Serialized.Text = true\] in type {itemType}}}), "Column1"),  
    #"Grouped Rows" = Table.Group(#"Split Column by Position", {"Column1"}, {{"Count", each Table.RowCount(\_)>1, type number}}),  
    #"Changed Type" = Table.TransformColumnTypes(#"Grouped Rows",{{"Count", type text}}),  
    #"Added Conditional Column" = Table.AddColumn(#"Changed Type", "Custom", each if \[Count\] = "false" then "0" else "1" ),  
    #"Changed Type1" = Table.TransformColumnTypes(#"Added Conditional Column",{{"Custom", Int64.Type}}),  
    #"Calculated Sum" = List.Sum(#"Changed Type1"\[Custom\])  
    in  
    #"Calculated Sum"
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514425)
    
27.  ![](https://secure.gravatar.com/avatar/8f2968a246416722d4d0ef90986f2e8254b344a9b83934be2b7d9096c05690f2?s=64&d=mm&r=g) lori says:
    
    [October 6, 2017 at 10:25 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514470)
    
    another variation (non-cse / non-volatile):
    
    \=LEN(A1)>COUNT(FIND({0,1,2,3,4}+{0;5},A1))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514470)
    
28.  ![](https://secure.gravatar.com/avatar/d7e836f28dcf336f887c4c64197ece24e1052eb8216c21bffc34f9662d5dbe26?s=64&d=mm&r=g) Tanuja says:
    
    [October 7, 2017 at 6:13 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514763)
    
    This was really very helpful! I got my answer!
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1514763)
    
29.  ![](https://secure.gravatar.com/avatar/549f0f05e61393eca81e962cd1a516d56a4078f8737b04ea652e80dc45e70cb1?s=64&d=mm&r=g) Black Moses says:
    
    [October 10, 2017 at 11:35 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515336)
    
    It's interesting how many responses this article got compared to the ones immediately before and after it. It's not a perfect comparison; other articles perhaps do not invite responses in the same way. Regardless, I would surmise that people enjoy these Excel challenges.
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515336)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [October 10, 2017 at 1:58 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515351)
        
        @Black Moses
        
        I have never been able to work out why some posts get huge responses and others get very few.
        
        Posts I have made that I thought were fantastic have been lucky to gets comments, but others seemingly of lesser standard get inundated
        
        Go figure?
        
        Any ideas as to what makes one post more appealing than any others will be appreciated
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515351)
        
        *   ![](https://secure.gravatar.com/avatar/549f0f05e61393eca81e962cd1a516d56a4078f8737b04ea652e80dc45e70cb1?s=64&d=mm&r=g) Black Moses says:
            
            [October 11, 2017 at 12:17 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515518)
            
            I guess I'm as guilty as anyone of reading but not commenting,
            
            I, for one, find your formula forensics series incredibly interesting and useful, and your latest post on conditional formatting on chart data labels is a cool trick that I hope I will have opportunity to use, but I rarely comment on articles unless there's some direct/indirect question posed (doesn't have to be a challenge, but just something to respond to), that's pretty much the key for engaging me.
            
            I \*could\* simply post "that's awesome, thanks for posting this" when I read something on here I like, which I'm sure would be welcome, but in actual fact wouldn't do much for advancing meaningful, insightful discourse on the site. And actually me posting "that's awesome" could simply be replicated with a 'like' button a la Facebook.
            
            I have no idea what makes some posts more appealing than others, maybe a 'like' button, or a 'How appealing did you find this post on a scale of 1-10?' web form straw poll on every article would generate some insight.
            
            [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515518)
            
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [October 10, 2017 at 7:26 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515405)
        
        It is surprising, but at least it is consistent (ie we get more responses for homework / challenge type questions). Also, over the years I think blog has gone quieter (despite having way more traffic than earlier times). It does feel like an echo chamber sometimes and I am not sure if a certain topic / article is useful to the audience or not. But we march along, one post at a time.
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1515405)
        
30.  ![](https://secure.gravatar.com/avatar/9f942def620166af705e1f528e2cce5bc0741a7ccd5979f8af95b162cd49d2c6?s=64&d=mm&r=g) [Shweta Jain](https://excelvbatipsforbeginners.blogspot.in/)
     says:
    
    [October 14, 2017 at 4:23 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1516282)
    
    \=IF(SUM((FREQUENCY(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)\*1,MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)\*1)>1)\*1)=1,TRUE,FALSE)
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1516282)
    
31.  ![](https://secure.gravatar.com/avatar/dd1cbf173f5e103ca41da0e0aad271fc5857086324a8135c953a1612334221ca?s=64&d=mm&r=g) James says:
    
    [October 23, 2017 at 9:59 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1518158)
    
    for the fun of it one more  
    {=SUM(IFERROR(SEARCH({0,1,2,3,4,5,6,7,8,9},A1),0))=LEN(A1)\*(LEN(A1)+1)/2}
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1518158)
    
32.  ![](https://secure.gravatar.com/avatar/f06b48d201991bdbb5d1252b313f611a51c77f1f20834e04c80d474213b2647c?s=64&d=mm&r=g) trainsauce says:
    
    [January 11, 2018 at 9:13 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1531633)
    
    \=LEN(A1)COUNT(SEARCH({1,2,3,4,5,6,7,8,9,0},A1))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1531633)
    
    *   ![](https://secure.gravatar.com/avatar/6ddb4aad4bd3f636e7895c6048287a211130412f56657b48b579d056f1db6e5a?s=64&d=mm&r=g) cad says:
        
        [June 27, 2024 at 1:21 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-2226419)
        
        \=LET(x, SEQUENCE(10,1,0), y, IFERROR(FIND(x,A1),""), z, COUNT(y),NOT(z=LEN(A1)))
        
        [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-2226419)
        
33.  ![](https://secure.gravatar.com/avatar/8489739dd730bf0b9e7fdd290d07e05ef155be1c4fb173c3a7077d96ef9b9587?s=64&d=mm&r=g) [Maxwell Deutsch](http://lake.k12.fl.us/mrdeutsch)
     says:
    
    [January 30, 2018 at 6:58 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1533859)
    
    \=AND(ISERR(FIND("00",TEXT(A1,"0"))),ISERR(FIND("11",TEXT(A1,"0"))),ISERR(FIND("22",TEXT(A1,"0"))),ISERR(FIND("33",TEXT(A1,"0"))),ISERR(FIND("44",TEXT(A1,"0"))),ISERR(FIND("55",TEXT(A1,"0"))),ISERR(FIND("66",TEXT(A1,"0"))),ISERR(FIND("77",TEXT(A1,"0"))),ISERR(FIND("88",TEXT(A1,"0"))),ISERR(FIND("99",TEXT(A1,"0"))))
    
    I challenged myself to come up with any solution before looking through the comments. I'm blown away by how much I can learn from this post alone. I knew there'd be an easier way out there.
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1533859)
    
34.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [February 10, 2018 at 3:34 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1535586)
    
    \=COUNT(FIND((ROW(1:10)-1),A1))=LEN(A1)
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1535586)
    
35.  ![](https://secure.gravatar.com/avatar/08cc1ad470c52d479f2a8b76dbaf25746e968ea92f698313549c202e59abca9e?s=64&d=mm&r=g) Kutty says:
    
    [February 12, 2018 at 6:07 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1535829)
    
    IF(IFERROR(FIND(9,A1)<FIND(9,A1,FIND(9,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(8,A1)<FIND(8,A1,FIND(8,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(7,A1)<FIND(7,A1,FIND(7,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(6,A1)<FIND(6,A1,FIND(6,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(5,A1)<FIND(5,A1,FIND(5,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(4,A1)<FIND(4,A1,FIND(4,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(3,A1)<FIND(3,A1,FIND(3,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(2,A1)<FIND(2,A1,FIND(2,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(1,A1)<FIND(1,A1,FIND(1,A1)+1),FALSE)=TRUE,TRUE,IF(IFERROR(FIND(0,A1)<FIND(0,A1,FIND(0,A1)+1),FALSE)=TRUE,TRUE,FALSE))))))))))
    
    it's too long formula but it's perfect formula for within the cell conditional
    
    if you want excel file i will upload with your permission.
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1535829)
    
36.  ![](https://secure.gravatar.com/avatar/5a885f56e0a46e5d619e7251bd48f043a2973759181cce613e36e26527173abb?s=64&d=mm&r=g) Paul says:
    
    [July 22, 2018 at 9:55 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1566070)
    
    \=SUMPRODUCT(--(MID(A1,ROW(INDIRECT("1:"&LEN(A1)-1)),1)=  
    MID(A1,ROW(INDIRECT("2:"&LEN(A1))),1)))>0
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1566070)
    
37.  ![](https://secure.gravatar.com/avatar/8b875c9820cb7b0be4f327283b40e70cf5d3cfcb0e612d17996ef90694e81067?s=64&d=mm&r=g) PipO says:
    
    [May 23, 2020 at 3:09 pm](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1798283)
    
    Maybe late ...  
    \=IF(ISNUMBER(AGGREGATE(15,6,FIND(SEQUENCE(10,,0)&SEQUENCE(10,,0),B5),1)),"Yes","No")  
    starting from B5
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-1798283)
    
38.  ![](https://secure.gravatar.com/avatar/6ddb4aad4bd3f636e7895c6048287a211130412f56657b48b579d056f1db6e5a?s=64&d=mm&r=g) cad says:
    
    [June 27, 2024 at 1:22 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-2226420)
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table2"\]}\[Content\],  
    #"Duplicated Column" = Table.DuplicateColumn(Source, "Column1", "Column1 - Copy"),  
    #"Split Column by Position" = Table.ExpandListColumn(Table.TransformColumns(Table.TransformColumnTypes(#"Duplicated Column", {{"Column1 - Copy", type text}}, "en-GB"), {{"Column1 - Copy", Splitter.SplitTextByRepeatedLengths(1), let itemType = (type nullable text) meta \[Serialized.Text = true\] in type {itemType}}}), "Column1 - Copy"),  
    #"Changed Type" = Table.TransformColumnTypes(#"Split Column by Position",{{"Column1 - Copy", type number}, {"Column1", type text}}),  
    #"Removed Duplicates" = Table.Distinct(#"Changed Type"),  
    #"Grouped Rows" = Table.Group(#"Removed Duplicates", {"Column1"}, {{"Count", each Table.RowCount(\_), Int64.Type}}),  
    #"Added Custom" = Table.AddColumn(#"Grouped Rows", "Custom", each if Text.Length(\[Column1\]) -\[Count\] = 0 then false else true),  
    #"Removed Columns" = Table.RemoveColumns(#"Added Custom",{"Count"})  
    in  
    #"Removed Columns"
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-2226420)
    
39.  ![](https://secure.gravatar.com/avatar/6ddb4aad4bd3f636e7895c6048287a211130412f56657b48b579d056f1db6e5a?s=64&d=mm&r=g) cad says:
    
    [June 27, 2024 at 1:23 am](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-2226421)
    
    \=LET(x, SEQUENCE(10,1,0), y, IFERROR(FIND(x,A1),""), z, COUNT(y),NOT(z=LEN(A1)))
    
    [Reply](https://chandoo.org/wp/number-has-repetitive-digits-formula/#comment-2226421)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/number-has-repetitive-digits-formula/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [D’oh – Visualizing Homer’s favorite sayings in Power BI](https://chandoo.org/wp/doh-powerbi/) | [Histograms & Pareto charts in Excel – tutorial, tips and downloadable template](https://chandoo.org/wp/histograms-pareto-charts-in-excel/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)