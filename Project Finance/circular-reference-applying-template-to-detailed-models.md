# Multiple Debt Issues Example

**Source:** https://edbodmer.com/circular-reference-applying-template-to-detailed-models

---

On this page I demonstrate how you can add the parallel model into complex examples to solve some more difficult project finance issues that contain circular references including debt sculpting with multiple debt issues. The first example illustrates how to evaluate debt sizing in a P99 or P90 case while establishing a tariff from a P50 case.  I describe the modelling process for the project finance issue (in this case, sculpting with multiple debt facilities). I have taken a few real examples of models that have circular references that are either solved with copy and paste macros or iteration buttons.  Before beginning the examples, I walk through the circular template function.

Example 1: Multiple Debt Facilities, Sculpting and Circular References
----------------------------------------------------------------------

### A Walk Through the Circular Reference Resolution Template

The video below shows how the circular reference template works.  I have tried to make it flexible so you can use different options such as debt sizing with different mechanics, different DSRA funding etc.  But it is likely that you will have something that is not in the template.  For this you must not be afraid to try new things.  The first step in this process is to not be afraid of the equations, the variable declarations, the loops, the outputs or the routines to get data into the program.

Example 2: Adding the Circular Template to an Airport Model
-----------------------------------------------------------

The model below is a complete model with a series of copy and paste macros to avoid a series of different circular references.  The video explains how to do this.  The process involves the folling steps:

**Step 1:** Copy the UDF from the circular reference template and copy the template into a new sheet.

**Step 2:** Attach the different input variables to the variables that are in the circular reference template.

**Step 3:** Run the circular template function and use the SHIFT F3 function to find the variable names.

**Step 4:** Find the variables that a causing the circular reference in the file and attach those variables to the function output in the circular template page.

Technical Notes:
----------------

When setting the dimension on variables, use public variables that can be accessed by any function.  Also use the Double instead of Single to define the variables so that you don’t get the small decimals at the end.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1085&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.828106372452393)