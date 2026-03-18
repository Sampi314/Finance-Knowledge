# Unforget-TABLE, That’s What You Are

**Source:** https://sumproduct.com/thought/unforget-table-thats-what-you-are/

---

[Home](https://sumproduct.com/)

\> Unforget-TABLE, That’s What You Are

*   November 10, 2017

Unforget-TABLE, That’s What You Are
===================================

VBA Blogs: Unforget-TABLE, That’s What You Are
==============================================

10 November 2017

_The first in a series about using ListObjects to manipulate Tables within an Excel workbook in VBA._

**Warning! This was written whilst listening to a Nat King Cole playlist…**

“Look What You’ve Done To Me”, storing all the data in a table in the Excel workbook. How does one access the table from VBA and “Make Her Mine”? It’s a lot simpler than one would think, “Pick Yourself Up” and consider the ListObjects method in VBA.

First let’s create a table from a Range in VBA. “I’m Never Satisfied” with storing data as raw, it’s nicer to make it into a table. This involves using the _Add_ method of ListObjects.

![](<Base64-Image-Removed>)

The parameters are as follows:

*   _SourceType_ – the SourceType. _xlSrcRange_ indicates that is a Range item not a “Make Believe Island”
*   _Source_ – this is only applicable when _xlSrcRange_ is used so that VBA doesn’t have to go searching “To The Ends of the Earth”
*   _LinkSource_ – this is when external data sets are used, and not applicable when using the Range item. “Don’t Blame Me” for skipping it in this case as it isn’t necessary
*   _xlListObjectHasHeaders_ – if the first row of the Range is actually a header row.

The _Name_ method is added to the end of the ListObjects call to rename the table as required and stamp it “My Personal Possession”.

Before:

![](<Base64-Image-Removed>)

After:

![](<Base64-Image-Removed>)

“You Call It Madness” but if _xlListObjectHasHeaders_ is set to _xlNo_ for headers the following result is achieved:

![](<Base64-Image-Removed>)

The range of the data is actually shifted down by one and generic headers created! By default, VBA will assume _xlGuess_ where it makes a judgement call on the data. It is best practice to specify to VBA directly the header intention otherwise there may be “Looking Back” on unexpected results thinking “That Ain’t Right” at all.

Stay in tune to see “Whatcha’ Gonna Do” in order to manipulate the data in the table!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/unforget-table-thats-what-you-are/#0)
    
*   [Register](https://sumproduct.com/thought/unforget-table-thats-what-you-are/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/unforget-table-thats-what-you-are/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/unforget-table-thats-what-you-are/#0)

[](https://sumproduct.com/thought/unforget-table-thats-what-you-are/#0 "close")

top