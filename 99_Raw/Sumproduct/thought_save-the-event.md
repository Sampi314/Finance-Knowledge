# Save the event!

**Source:** https://sumproduct.com/thought/save-the-event/

---

[Home](https://sumproduct.com/)

\> Save the event!

*   July 14, 2017

Save the event!
===============

VBA Blogs: Save the event!
==========================

14 July 2017

This month is Event month! Today, we’re going to be looking at how to set up events to trigger on saving a file.

We’re going to start off by reusing some of the code that we used last week. Remember we created a Disclaimer macro that would run when the file is open? What happens if the person opening the file simply doesn’t enable macros?

This is where Workbook\_BeforeSave comes in handy. Instead of running some sort of disclaimer that hides everything when the model is opened, why not run it instead just before we save the file? That way, when we save the file, before it saves, it will run the Disclaimer, and when someone opens the file, sheets will be hidden already.

Of course, that begs the question, once it’s saved, do we need to click “I agree” before we can move on? Well, if we use the Workbook\_AfterSave event, then we can have it unhide again once the file has been saved, meaning that we don’t need to lift a finger to reset the file back to an ‘unlocked’ status.

![](<Base64-Image-Removed>)

There are actually some other tools that we can use as part of this function. If someone were to use “Save As”, this will transmit that fact to a variable called “SaveAsUI” which can be used to create some additional rules, perhaps some new details that should be incorporated into the file to reflect the fact it will be a new file. You can also see that there is a “Cancel” variable that will check if someone cancels a Save As operation, as maybe you will not want the macro to run if the file isn’t actually saved.

These are useful tools that can help you manage your files and automate processes that you might not trust people to actively do when they save a file. Other useful things to run before saving might include resetting the viewable area of worksheets to the top left hand side, changing scenario values back to base case values, or other similar “file clean up” activities.

Next week, we’ll take a look at some in-sheet events, such as selecting particular cells. See you then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/save-the-event/#0)
    
*   [Register](https://sumproduct.com/thought/save-the-event/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/save-the-event/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/save-the-event/#0)

[](https://sumproduct.com/thought/save-the-event/#0 "close")

top