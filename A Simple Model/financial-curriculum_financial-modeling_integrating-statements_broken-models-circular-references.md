# Broken Models & Circular References | A Simple Model

**Source:** https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references

---

[Curriculum](https://www.asimplemodel.com/financial-curriculum/financial-modeling "Curriculum")
![](https://www.asimplemodel.com/wp-content/themes/DiviChildTheme/images/breadcrumb_arrow.png)[Integrating Financial Statements](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements "Introduction to Financial Statements")
![](https://www.asimplemodel.com/wp-content/themes/DiviChildTheme/images/breadcrumb_arrow.png)Broken Models & Circular References

[View Full Screen](javascript:void(0);) [Take the Quiz](https://portal.asimplemodel.com/login.aspx)
[Next Lesson »](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/balancing-model)

![Video Thumbnail](https://embed-ssl.wistia.com/deliveries/c9385522b40943a8000569ef020e84364fd29de5.webp?image_crop_resized=1280x720)

Click for sound

0:00

Broken Models & Circular References

Download Notes Download Notes

ChaptersRewind [![](https://www.asimplemodel.com/wp-content/themes/DiviChildTheme/images/rewind.gif)](javascript:void(0);) 

1.  [Manual Fix](javascript:void(0); "Manual Fix")
    
2.  [Circularity Explanation](javascript:void(0); "Circularity Explanation")
    
3.  [Iterative Calculations](javascript:void(0); "Iterative Calculations")
    
4.  [Formula Fix](javascript:void(0); "Formula Fix")
    

### Summary Text

The purpose of this video (and the one that follows) is to help avoid extreme frustration as you learn to build models. This video focuses on circular reference errors, which can cause a model to “ref out.” The saying is used because Excel will display “#REF!” for invalid cell references. If an error occurs Excel might also display #DIV/0! or #VALUE! depending on the kind of error.

To demonstrate what happens when your model “refs out” on account of a circular reference error the video starts out by creating one in the model:

![Fixing a Broken Model](https://portal.asimplemodel.com/userfiles/Image/Image%201.PNG "Fixing a Broken Model")

As a first-time modeler this can be pretty terrifying, but it is so common that it is actually used to play pranks on analysts (or I just had evil superiors…). Fortunately it is also easy to fix.

Fixing the error requires two steps. First you must undo what caused the error, and in this example the error was caused by deleting revenue in period 20X2.

![Fixing a Broken Financial Model](https://portal.asimplemodel.com/userfiles/Image/Image%202.PNG "Fixing a Broken Financial Model")

You will notice that replacing revenue is an improvement, but your model still shows multiple errors. Step two is to delete the source of the circularity, which in this case is interest expense.

![Fixing a Broken Financial Model](https://portal.asimplemodel.com/userfiles/Image/Image%203.PNG "Fixing a Broken Financial Model")

With interest expense deleted you have fixed the error and the model will calculate properly. At that point you can link the model back to interest expense and keep working.

![A Balanced Three Statement Model](https://portal.asimplemodel.com/userfiles/Image/Image%204.PNG "A Balanced Three Statement Model")

Having fixed the error the video explores the cause of the circular reference error. In other words, what happens in the model that causes so many cells to display an error message?

Lets take a look at the full model on the following page for an explanation.

![Circular Reference in a Financial Model](https://portal.asimplemodel.com/userfiles/Image/Image%205.png "Circular Reference in a Financial Model")

The circular reference is created as follows:

1.  Interest Expense is used to calculate Net Income
2.  Net Income is used to calculate Cash Flow
3.  Cash Flow is used to calculate the Revolver / Line of Credit
4.  Revolver / Line of Credit impacts the amount of Interest Expense: More (or less) debt requires greater (or smaller) interest payments 

![Circular Reference in a Three-Statement Model](https://portal.asimplemodel.com/userfiles/Image/Circular%20Reference%20in%20a%20Three-Statement%20Model_ASM.png "Circular Reference in a Three-Statement Model")

As you can see the calculation creates a circular reference (or in this case an oddly shaped loop).   
The video demonstrates how this occurs in a couple models to provide more visuals.

The video then demonstrates how to Enable Iterative Calculation in Excel. Without this functionality enabled, Excel will not properly calculate any circular references.  
To turn on iterative calculation select the File menu > Options > Formulas and check the box for “Enable iterative calculation” (circled red below).

![Enable Iterative Calculation](https://portal.asimplemodel.com/userfiles/Image/Image%207.PNG "Enable Iterative Calculation")

The video concludes by offering a more elegant solution to fix circular reference errors. Rather than delete and relink interest expense every time your model refs out, you can use a formula to work around it.  
The “=IF” formula checks whether a condition is met, and then returns one value if TRUE, and another value if FALSE (definition of =IF formula taken from Excel).   
Condition: B21 = “ON”   
Value if TRUE: Links to Interest Expense (cell E128)  
Value if FALSE: 0

![Fix Circular Reference in Excel](https://portal.asimplemodel.com/userfiles/Image/Image%208.PNG "Fix Circular Reference in Excel")

In this way, you can input “OFF” in cell B21while you are working on the model, and work without creating circular reference errors. Once you’re done with the model input “ON” to run interest expense through the model.

  

[Take the Quiz](https://portal.asimplemodel.com/login.aspx)
[Next Lesson »](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/balancing-model)

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
 and [Privacy Policy](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
 and [Privacy Policy](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
 and [Privacy Policy](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
 and [Privacy Policy](https://www.asimplemodel.com/financial-curriculum/financial-modeling/integrating-statements/broken-models-circular-references#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.