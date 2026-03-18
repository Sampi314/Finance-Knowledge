# The 1.4m Excel formula

**Source:** https://www.financialmodellinghandbook.org/the-14m-formula

---

My friend Gerard shared this one.

It measures 1.4m if you stretch it out. Brilliant.

Keep them coming.  

\=IF(AND( $N97<>1,$O97<>1),$F97\*$I97 \* IF( AND( HeavyVehInd=2, X$4>=RoadStartYr), (1-$L97),(1-$K97))\*(1-INDEX( X$5:X$7, MATCH($Q97,$Q$5:$Q$7,0))), IF(AND($N97=1,$O97=1), IF(OR(BiomassInd=1,AgInd=1),0, IF(X$4>= MAX(BiomassStartYr,AgStartYr), $F97\*$I97\* IF(AND(HeavyVehInd=2,X$4>=RoadStartYr), (1-$L97), (1-$K97))\*(1-INDEX(X$5:X$7,MATCH($Q97,$Q$5:$Q$7,0))),0)), IF($N97=1,IF(BiomassInd=1,0, IF(X$4>=BiomassStartYr, $F97\*$I97\* IF(AND(HeavyVehInd=2,X$4>=RoadStartYr), (1-$L97), (1-$K97))\*(1-INDEX(X$5:X$7, MATCH($Q97,$Q$5:$Q$7,0))),0)), IF($O97=1, IF(AgInd=1,0, IF(X$4>=AgStartYr, $F97\*$I97\*IF(AND(HeavyVehInd=2, X$4>=RoadStartYr), (1-$L97),(1-$K97)) \* (1-INDEX(X$5:X$7,MATCH($Q97,$Q$5:$Q$7,0))),0))))))

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--112.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

Sorry, comments couldn't be loaded. It looks like this account is not currently active.

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/the-14m-formula#/portal/signup)