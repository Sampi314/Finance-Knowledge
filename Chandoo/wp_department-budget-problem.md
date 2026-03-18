# Write a formula to get Department Budget for a Month [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/department-budget-problem

---

Write a formula to get Department Budget for a Month \[Homework\]
=================================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 40 comments

  

Time for another homework. You got a spreadsheet of department budgets and need to write a formula to get **budget** for a given _department, month_ combination.

![department-budget-2d-lookup-problem](https://chandoo.org/wp/wp-content/uploads/2021/03/department-budget-2d-lookup-problem.png)

Homework Specifics:
-------------------

Assume your data is in the table named **budgets**, D18 has department and D19 has month values.

You can use any formula in Excel to get the answer. Let’s get creative and have fun.

**Post your solutions in the comments section. GO!!!**

Need a sample file? [Get it from here](https://chandoo.org/wp/wp-content/uploads/2021/03/2d-lookup-homework.xlsx)
.

Need a hint? [Check out my 2D lookups article](https://chandoo.org/wp/2way-lookup-formulas/)
.

Want more homework problems? [See this page](https://chandoo.org/wp/tag/homework/)
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
| Written by Chandoo  <br>Tags: [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [INDEX()](https://chandoo.org/wp/tag/index/)<br>, [MATCH()](https://chandoo.org/wp/tag/match/)<br>, [vlookup](https://chandoo.org/wp/tag/vlookup/)<br>, [vlookup or index+match](https://chandoo.org/wp/tag/vlookup-or-indexmatch/)<br>, [xlookup](https://chandoo.org/wp/tag/xlookup/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 40 Responses to “Write a formula to get Department Budget for a Month \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/81fb5055a836e4622977f86a7e7179b41f11f744e2b3d9bbca0d02b97b7c7fa7?s=64&d=mm&r=g) TheQ47 says:
    
    [March 12, 2021 at 10:25 am](https://chandoo.org/wp/department-budget-problem/#comment-1981562)
    
    I'd use nested XLOOKUPs, as follows:
    
    \=XLOOKUP(D18,budgets\[Department\],XLOOKUP(D19,budgets\[#Headers\],budgets))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981562)
    
    *   ![](https://secure.gravatar.com/avatar/0e4d5424c36074f60f391f22fcc5eafb0be7d1f5b61fbfe4494f22b0a6992505?s=64&d=mm&r=g) Kathi says:
        
        [May 19, 2022 at 8:01 pm](https://chandoo.org/wp/department-budget-problem/#comment-2077742)
        
        Almost the same, just accounted for "not found" and forced exact match.  
        \=XLOOKUP(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],XLOOKUP(D18,budgets\[Department\],budgets\[\[Jan\]:\[Jun\]\],"",0))
        
        Verification pointed out that Administration was misspelled so I added Data Validation to D18 and D19.
        
        [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2077742)
        
2.  ![](https://secure.gravatar.com/avatar/40d90286d3beb769efa75c1cfe88346c01126957a7bca29da096ff5a3aa64dd1?s=64&d=mm&r=g) [Finnur](http://www.excel.is/)
     says:
    
    [March 12, 2021 at 10:57 am](https://chandoo.org/wp/department-budget-problem/#comment-1981565)
    
    Old school:
    
    \=HLOOKUP(D19;budgets\[#All\];MATCH(D18;budgets\[\[#All\];\[Department\]\];0);0)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981565)
    
3.  ![](https://secure.gravatar.com/avatar/04b5a93edbc655803abe74ca9048a5e604383b69481c0cb5e200048e7b6d86e4?s=64&d=mm&r=g) Prashant says:
    
    [March 12, 2021 at 11:31 am](https://chandoo.org/wp/department-budget-problem/#comment-1981570)
    
    \=SUMPRODUCT(budgets\[\[Jan\]:\[Jun\]\]\*(budgets\[Department\]=D18)\*(budgets\[\[#Headers\],\[Jan\]:\[Jun\]\]=D19))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981570)
    
4.  ![](https://secure.gravatar.com/avatar/04b5a93edbc655803abe74ca9048a5e604383b69481c0cb5e200048e7b6d86e4?s=64&d=mm&r=g) Prashant says:
    
    [March 12, 2021 at 11:34 am](https://chandoo.org/wp/department-budget-problem/#comment-1981572)
    
    \=INDEX(FILTER(budgets\[\[Jan\]:\[Jun\]\],budgets\[Department\]=D18),MATCH(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981572)
    
5.  ![](https://secure.gravatar.com/avatar/3539d7ccb0681f6f06b71623bc6b3fe79d845af92137fe358e6edee4ca7226c8?s=64&d=mm&r=g) Daniel says:
    
    [March 12, 2021 at 11:34 am](https://chandoo.org/wp/department-budget-problem/#comment-1981573)
    
    \=INDEX(FILTER(budgets,INDEX(budgets,,1)=D18),XMATCH(D19,budgets\[#Headers\],FALSE))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981573)
    
6.  ![](https://secure.gravatar.com/avatar/36427f04e94ae552af22bab409412a23406658f759d38f7d1451e09b53d1a3a0?s=64&d=mm&r=g) Tan Yann Lin says:
    
    [March 12, 2021 at 12:50 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981582)
    
    \=XLOOKUP(D18,budgets\[Department\],XLOOKUP(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],budgets\[\[Jan\]:\[Jun\]\]))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981582)
    
7.  ![](https://secure.gravatar.com/avatar/a113ff47613b22c20f7b8247006bbd13fd13da2d701f9974e61c440444389b5a?s=64&d=mm&r=g) Jomili says:
    
    [March 12, 2021 at 7:58 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981628)
    
    Way old school:  
    \=VLOOKUP(D18,budgets\[#All\],MATCH(D19,budgets\[#Headers\],0),FALSE)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981628)
    
8.  ![](https://secure.gravatar.com/avatar/a2ce73364d19179c6ea9c2faafdbc068646d29946dc41fd2fa77a0efe48ea2c6?s=64&d=mm&r=g) Frank McCraw says:
    
    [March 12, 2021 at 9:49 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981651)
    
    \=INDEX(budgets\[\[Jan\]:\[Jun\]\],MATCH(D18,budgets\[Department\],0),MATCH(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981651)
    
9.  ![](https://secure.gravatar.com/avatar/65bec3eab87b735a2b5c637107afcf08f25c1975ec932ddd8d65a2d597b37949?s=64&d=mm&r=g) Craig says:
    
    [March 12, 2021 at 10:24 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981653)
    
    So many functions to choose from.
    
    My first thought was an "old school" solution using OFFSET with MATCH. In trying to learn something new I came up with...
    
    \=FILTER(FILTER(budgets,budgets\[Department\]=D18),budgets\[#Headers\]=D19)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981653)
    
10.  ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
    
    [March 13, 2021 at 2:23 am](https://chandoo.org/wp/department-budget-problem/#comment-1981683)
    
    \=vlookup(Dept,Budgets,match(Month,index(Budgets,1),0)-1,0)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981683)
    
    *   ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
        
        [March 13, 2021 at 2:26 am](https://chandoo.org/wp/department-budget-problem/#comment-1981685)
        
        Using cell references, rather than range names:
        
        \=vlookup(D18,Budgets,match(D19,index(Budgets,1),0)-1,0)
        
        [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981685)
        
        *   ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
            
            [March 13, 2021 at 10:33 am](https://chandoo.org/wp/department-budget-problem/#comment-1981729)
            
            Whoops. Hadn't noticed "budgets" didn't include the header row. Third time lucky?
            
            \=VLOOKUP(D18,budgets,MATCH(D19,OFFSET(INDEX(budgets,1,),-1,0),0),0)
            
            [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981729)
            
11.  ![](https://secure.gravatar.com/avatar/f907534c8010f5652c25fb6c3b2555e5678589bd3adb7eb2306032a06d9b41e4?s=64&d=mm&r=g) mohammed mustafa says:
    
    [March 13, 2021 at 5:04 am](https://chandoo.org/wp/department-budget-problem/#comment-1981694)
    
    Using the old Index and Match function  
    \=INDEX(budgets\[#All\],XMATCH(D18,budgets\[\[#All\],\[Department\]\],0),XMATCH(D19,budgets\[#Headers\],0))
    
    And using the new Xlookup  
    \=XLOOKUP(D18,budgets\[Department\],XLOOKUP(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],budgets\[\[Jan\]:\[Jun\]\]))
    
    Using Filter  
    \=FILTER(FILTER(budgets,budgets\[Department\]=D18),budgets\[#Headers\]=D19)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981694)
    
12.  ![](https://secure.gravatar.com/avatar/d47cad9596bb35f97ecded49e1e7e79dba86436555723fa814126eb808140f6b?s=64&d=mm&r=g) fethi ben yahia says:
    
    [March 13, 2021 at 9:43 am](https://chandoo.org/wp/department-budget-problem/#comment-1981722)
    
    {=INDEX(budgets\[#Tout\];EQUIV(D18;budgets\[Department\];0);EQUIV(D19;budgets\[\[#En-têtes\];\[Jan\]:\[Jun\]\];0))}
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981722)
    
13.  ![](https://secure.gravatar.com/avatar/d47cad9596bb35f97ecded49e1e7e79dba86436555723fa814126eb808140f6b?s=64&d=mm&r=g) fethi ben yahia says:
    
    [March 13, 2021 at 9:46 am](https://chandoo.org/wp/department-budget-problem/#comment-1981723)
    
    {=INDEX(budgets\[\[Jan\]:\[Jun\]\];EQUIV(D18;budgets\[Department\];0);EQUIV(D19;budgets\[\[#En-têtes\];\[Jan\]:\[Jun\]\];0))}
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981723)
    
14.  ![](https://secure.gravatar.com/avatar/c91d019058246092be3e973ebdb0b90418ee323fcd5f21d2891e7ab9949bc9d4?s=64&d=mm&r=g) John Johnston says:
    
    [March 13, 2021 at 10:32 am](https://chandoo.org/wp/department-budget-problem/#comment-1981728)
    
    Just to be different....
    
    \=XLOOKUP(D19,budgets\[#Headers\],FILTER(budgets,budgets\[Department\]=D18,""),"Not Found")
    
    I also found that the following works:
    
    \=INDEX(budgets,XMATCH(D18,budgets\[Department\]),XMATCH(D19,budgets\[#Headers\]))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981728)
    
15.  ![](https://secure.gravatar.com/avatar/81f48a32390da65fb98f20e1ac3524c314d6a136b5eb35cb363ccf6f269a6dfb?s=64&d=mm&r=g) Michael says:
    
    [March 13, 2021 at 1:22 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981738)
    
    \=INDEX(budgets\[\[Jan\]:\[Jun\]\],MATCH(D18,budgets\[Department\],1),MATCH(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],0))
    
    Will get you the answer
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981738)
    
16.  ![](https://secure.gravatar.com/avatar/1f3bb712086db3cfab3e5074581b05707aebf9e8466a61498f2175107ff38560?s=64&d=mm&r=g) SAM MO says:
    
    [March 13, 2021 at 3:52 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981750)
    
    Name Monthly Ranges first
    
    \=XLOOKUP(D18,budgets\[Department\],INDIRECT(D19))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981750)
    
17.  ![](https://secure.gravatar.com/avatar/77256092f89a9a647022af2dbf4fa1ae3991047d36647915fbaffe41ce358393?s=64&d=mm&r=g) Eric Surdez says:
    
    [March 13, 2021 at 4:07 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981755)
    
    \=SUMPRODUCT(budgets\[\[Jan\]:\[Jun\]\],MMULT((budgets\[Department\]=D18)\*1,(budgets\[\[#Headers\],\[Jan\]:\[Jun\]\]=D19)\*1))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981755)
    
18.  ![](https://secure.gravatar.com/avatar/be2d2563e42099e75bd078764fc7a14fb7f3b8243627e83bc17bce5959b628d3?s=64&d=mm&r=g) [Mohammad Rizwi](http://anwarprojectmanagementservices.com/)
     says:
    
    [March 13, 2021 at 5:33 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981760)
    
    \=VLOOKUP(D18,budgets\[#All\],MATCH(D19,budgets\[#Headers\],0),FALSE)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981760)
    
19.  ![](https://secure.gravatar.com/avatar/742c0cd8054cda2c8a360cb1da6bb40ce40758332a72895ada32c028382be2c4?s=64&d=mm&r=g) Zaig says:
    
    [March 14, 2021 at 12:14 am](https://chandoo.org/wp/department-budget-problem/#comment-1981787)
    
    \=INDEX(budgets,MATCH(D18,budgets\[Department\],0),MATCH(D19,budgets\[#Headers\],0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981787)
    
20.  ![](https://secure.gravatar.com/avatar/053bf911385b2736456ee9e2671e1b72f1e6b58a6cf1e4e8bb3279265910472e?s=64&d=mm&r=g) Borg says:
    
    [March 14, 2021 at 4:14 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981874)
    
    This approach should be quite pretty :
    
    in French  
    \=SOMME(RECHERCHEX(D18;C4:C11;D4:I11) RECHERCHEX(D19;D3:I3;D4:I11))
    
    in English, it should be :  
    \=SUM(XLOOKUP(D18;C4:C11;D4:I11) XLOOKUP(D19;D3:I3;D4:I11))
    
    with a space between the 2 XLOOKUP
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981874)
    
    *   ![](https://secure.gravatar.com/avatar/053bf911385b2736456ee9e2671e1b72f1e6b58a6cf1e4e8bb3279265910472e?s=64&d=mm&r=g) Borg says:
        
        [March 14, 2021 at 4:19 pm](https://chandoo.org/wp/department-budget-problem/#comment-1981875)
        
        Sorry not using table address language. I prefer using classic addresses.
        
        [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981875)
        
21.  ![](https://secure.gravatar.com/avatar/74109386ba52281ab563ea69b958a57e826b12389dee8862aea34f6c363bf0a5?s=64&d=mm&r=g) ari says:
    
    [March 15, 2021 at 2:53 am](https://chandoo.org/wp/department-budget-problem/#comment-1981913)
    
    well sumproduct is powerfull  
    \=SUMPRODUCT((C4:C11=D18)\*(D3:I3=D19)\*D4:I11)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981913)
    
22.  ![](https://secure.gravatar.com/avatar/d19fab3f9d11b52a87330aad23ffc0a5ee796a80aa14698330cbca8a22a938ab?s=64&d=mm&r=g) Sanditon needs a Season2 says:
    
    [March 15, 2021 at 4:38 am](https://chandoo.org/wp/department-budget-problem/#comment-1981919)
    
    \=SUMPRODUCT((budgets\[\[Jan\]:\[Jun\]\])\*(budgets\[\[#Headers\],\[Jan\]:\[Jun\]\]=$D$19)\*(budgets\[Department\]=$D$18))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981919)
    
23.  ![](https://secure.gravatar.com/avatar/ab9d074b4e23227910c1e81442c0fbe041301a1f85a4d8a5154392d6d28c030d?s=64&d=mm&r=g) Adem Kür?at Karaçil says:
    
    [March 15, 2021 at 5:56 am](https://chandoo.org/wp/department-budget-problem/#comment-1981926)
    
    \=+?ND?S(budgets\[\[Jan\]:\[Jun\]\];KAÇINCI(D18;budgets\[Department\];0);KAÇINCI(D19;budgets\[\[#Üst Bilgiler\];\[Jan\]:\[Jun\]\];0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981926)
    
24.  ![](https://secure.gravatar.com/avatar/4965b0fe3f46482139a38d06839971b32e16944b688e70c4b8aece431f8268a9?s=64&d=mm&r=g) Nadeem says:
    
    [March 15, 2021 at 7:25 am](https://chandoo.org/wp/department-budget-problem/#comment-1981936)
    
    \=HLOOKUP(D19,budgets\[#All\],MATCH(D18,budgets\[\[#All\],\[Department\]\],1),)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981936)
    
25.  ![](https://secure.gravatar.com/avatar/9b019c3e6f174eec375c6e0ea4da3c75df50f39a4849c92a11f937ae7fc81446?s=64&d=mm&r=g) venky says:
    
    [March 15, 2021 at 11:50 am](https://chandoo.org/wp/department-budget-problem/#comment-1981954)
    
    \=INDIRECT(ADDRESS(MATCH(D18,$A$1:$A$9,0),MATCH(D19,$A$1:$F$1,0)))
    
    Assuming table starts in A1
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1981954)
    
26.  ![](https://secure.gravatar.com/avatar/40a07d8584bddcd4afa99819cc40ba8284b80f9d3205d8afaf9edc44730b683e?s=64&d=mm&r=g) R1DZ says:
    
    [March 16, 2021 at 10:31 am](https://chandoo.org/wp/department-budget-problem/#comment-1982063)
    
    Using Index and Matching Look Up row & column wise
    
    \=INDEX(budgets\[\[Jan\]:\[Jun\]\],MATCH(D18,budgets\[Department\],0),MATCH(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1982063)
    
27.  ![](https://secure.gravatar.com/avatar/982b12f91e5201c8538e4960e9b557dcb038c22b66d39bd71b1fab85201eb76e?s=64&d=mm&r=g) Guido says:
    
    [March 19, 2021 at 10:56 am](https://chandoo.org/wp/department-budget-problem/#comment-1983696)
    
    1\. define rangenames for the rows and columns  
    2\. then use the fomule =Marketing Apr
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-1983696)
    
28.  ![](https://secure.gravatar.com/avatar/3a2f9d9994a327184c4d0c22a21e5d2e7f2ea34e0debeb450efa16b6a8d5cc56?s=64&d=mm&r=g) Parshwa says:
    
    [June 18, 2021 at 5:42 am](https://chandoo.org/wp/department-budget-problem/#comment-2006749)
    
    \=XLOOKUP(D18,budgets\[Department\],XLOOKUP(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],budgets\[\[Jan\]:\[Jun\]\]))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2006749)
    
29.  ![](https://secure.gravatar.com/avatar/24f30d101126499f3f7a19be48a4b6cdd271aa66db147e9c3b5ad11f476f1ea8?s=64&d=mm&r=g) Mohan Krishna says:
    
    [July 4, 2021 at 6:37 pm](https://chandoo.org/wp/department-budget-problem/#comment-2009536)
    
    \=INDEX(D4:I11,MATCH(D18,C4:C11,0),MATCH(D19,D3:I3,0))
    
    Please tell me if I am correct or wrong?
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2009536)
    
30.  ![](https://secure.gravatar.com/avatar/aba57ba33e1273dd8b0721a98663b02fb37261eec5e3b946e51c658fee636716?s=64&d=mm&r=g) [andok](http://m/a)
     says:
    
    [August 5, 2022 at 7:19 pm](https://chandoo.org/wp/department-budget-problem/#comment-2084731)
    
    \=INDEX(budgets\[#All\],MATCH(D18,budgets\[\[#All\],\[Department\]\],0),MATCH(D19,budgets\[#Headers\],0))
    
    here's mine, I hope this is a viable solution
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2084731)
    
31.  ![](https://secure.gravatar.com/avatar/ed45184312336d86af9f6a4e8610bd8bf112637ae95bfb2a7eb7982a8fb4481c?s=64&d=mm&r=g) Sandra says:
    
    [August 15, 2022 at 1:50 pm](https://chandoo.org/wp/department-budget-problem/#comment-2085737)
    
    I used INDEX+MATCH+MATCH:
    
    \=INDEX(budgets\[\[Jan\]:\[Jun\]\],MATCH(D18,budgets\[Department\],0),MATCH(D19,budgets\[\[#Headers\],\[Jan\]:\[Jun\]\],0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2085737)
    
32.  ![](https://secure.gravatar.com/avatar/cd08d8a28bab7b7e4634db3d067ba2ab1bf5b3026f351e4fe1f43f9723242326?s=64&d=mm&r=g) Anjali says:
    
    [August 23, 2022 at 7:03 am](https://chandoo.org/wp/department-budget-problem/#comment-2086596)
    
    \=VLOOKUP(D18,budgets\[#All\],5,FALSE)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2086596)
    
33.  ![](https://secure.gravatar.com/avatar/cc746c29a0202ff3decd052e67d8ad9847e631ec7bdbc530ebf127c774997bf1?s=64&d=mm&r=g) Sathish says:
    
    [October 11, 2022 at 6:21 pm](https://chandoo.org/wp/department-budget-problem/#comment-2101716)
    
    \=VLOOKUP(D18,budgets,5,0)
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2101716)
    
34.  ![](https://secure.gravatar.com/avatar/6cf7f6c25026e963fc67b581817c92a0d275e723c7f89a1503c8ac1938bea924?s=64&d=mm&r=g) jaime says:
    
    [December 20, 2022 at 12:52 am](https://chandoo.org/wp/department-budget-problem/#comment-2112382)
    
    \=INDICE(importes,COINCIDIR(D18,departamentos,0),COINCIDIR(D19,meses,0))
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2112382)
    
35.  ![](https://secure.gravatar.com/avatar/46d9b7b5f6a8fc9f1125b5025ea17f35a9d31b929223b53fb73f7a2187d1ea41?s=64&d=mm&r=g) MM says:
    
    [June 24, 2023 at 4:46 am](https://chandoo.org/wp/department-budget-problem/#comment-2131073)
    
    {=SUM(IF((M8=M2:M5)\*(N1:P1=N7),N2:P5,0))}
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2131073)
    
36.  ![](https://secure.gravatar.com/avatar/46d9b7b5f6a8fc9f1125b5025ea17f35a9d31b929223b53fb73f7a2187d1ea41?s=64&d=mm&r=g) Mudit says:
    
    [June 24, 2023 at 4:52 am](https://chandoo.org/wp/department-budget-problem/#comment-2131074)
    
    {=SUM(IF((D19=budgets\[\[#Headers\],\[Jan\]:\[Jun\]\])\*(D18=budgets\[Department\]),budgets\[\[Jan\]:\[Jun\]\],0))}
    
    [Reply](https://chandoo.org/wp/department-budget-problem/#comment-2131074)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/department-budget-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How to embed Excel files, calculators on your website? – Step by step instructions](https://chandoo.org/wp/embed-excel-file-on-your-website/) | [10 Advanced IF formula tricks you must know](https://chandoo.org/wp/advanced-if-tricks/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)