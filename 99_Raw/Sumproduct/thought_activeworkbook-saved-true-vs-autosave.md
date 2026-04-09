# ActiveWorkbook.Saved = True vs AutoSave

**Source:** https://sumproduct.com/thought/activeworkbook-saved-true-vs-autosave/

---

[Home](https://sumproduct.com/)

\> ActiveWorkbook.Saved = True vs AutoSave

*   January 11, 2019

ActiveWorkbook.Saved = True vs AutoSave
=======================================

VBA Blogs: ActiveWorkbook.Saved = True vs AutoSave
==================================================

11 January 2019

_When you thought that AutoSave couldn’t get any worse…_

As you might be aware, we’re not particularly fond of the AutoSave feature here at SumProduct. From our perspective, AutoSave is only good for overwriting files when you open them up just to do some quick test calculations, intending on hitting “No” when asked if you want to save the file, only to find that AutoSave has ruined your perfectly balanced balance sheets and models.

Well, a recently raised issue between the AutoSave feature and the long-standing VBA command “ActiveWorkbook.Saved = True” has given us more ammunition in the battle against AutoSave.

In a nutshell, ActiveWorkbook.Saved is the property in Excel that helps to determine whether changes have been made in a file, and therefore, whether you are prompted to save the file before closing. A common use for this bit of code is to ‘trick’ Excel into thinking that the file has been saved to avoid popping up further dialog boxes. We use this when we have BeforeSave macros that change the sheet presentation when the file is saved. Because these changes are generally reverted once the file is saved, setting ActiveWorkbook.Saved = True will stop Excel from prompting you to save the file again when you try to close it.

Unfortunately, this is intrinsically linked to the way that AutoSave looks at changes in your file and determines whether to resync and save it back to the server. The technical basis for this is a bit long to go into here, but the Microsoft team just released a good primer on what is causing the issue, and some suggested workarounds: [https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/how-autosave-impacts-addins-and-macros](https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/how-autosave-impacts-addins-and-macros)

![](<Base64-Image-Removed>)

This is Microsoft’s suggested script to get rid of AutoSave for files where you might be using ActiveWorkbook.Saved = True. Now, if only we could make this default in every file… See you next week!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/activeworkbook-saved-true-vs-autosave/#0)
    
*   [Register](https://sumproduct.com/thought/activeworkbook-saved-true-vs-autosave/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/activeworkbook-saved-true-vs-autosave/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/activeworkbook-saved-true-vs-autosave/#0)

[](https://sumproduct.com/thought/activeworkbook-saved-true-vs-autosave/#0 "close")

top