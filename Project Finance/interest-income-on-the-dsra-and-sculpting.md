# Interest Income on the DSRA and Sculpting

**Source:** https://edbodmer.com/interest-income-on-the-dsra-and-sculpting

---

Interest income can be earned on the DSRA account and it is generally a small amount. This does not mean it should be ignored. Developing a project finance model that can efficiently evaluate how interest income affects sculpting of debt can be difficult. The problem is that interest income from the DSRA is included in the CFADS (maybe it should be deducted from debt service), and the interest income depends on the DSRA, which depends on the level of debt, which depends on the sculpting. Videos and files on this page describe how you can resolve difficult circular reference issues that arise from interest income and sculpting. a series of issues associated with structuring that require more complex programming and financial equations.

There are a couple of key files where I put the financial formulas, modelling examples and the VBA code for cases where you run into circular references.  You can file these file on the google drive in the Project Finance Section under exercises and then Section D for the Sculpting course.  The files are available for download by pressing the button below.

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

 UDF Function for Resolving Interest Income on DSRA and Sculpting
-----------------------------------------------------------------

If the DSRA account or the MRA or any other reserve account is funded with cash and not a letter of credit, then the modelling can become painful if you do not use a UDF function.  This is particularly true for the DSRA account.  In the case of the DSRA account, interest income changes the CFADS and therefore changes the amount of debt. But when you change the amount of debt, the DSRA account changes.  Dreaded blue lines and a nasty circular reference. Many modellers just say that the interest income rate is so low that we should assume a zero rate. Maybe true.  But what about currencies where the interest rate is positive.  But what about when interest rates change. But why make such a simplifying assumption when you go crazy about other tiny assumptions like getting the days of interest correct.

Resolving the interest rate can be accomplished efficiently with a UDF.  With a copy and paste macro you would have to copy the entire line of interest income and then paste special.  It would then be part of the interation where you copy and paste multiple items …. A better method is to include interest income in a UDF and compute the DSRA.  The first time you try this it is a pain.  Eventually it should become easier. The trick is to model the DSRA account in a separate loop and keep track of the interest income in an array. The method for writing such VBA code is described in the  video below.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3329&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.6450711264090538)