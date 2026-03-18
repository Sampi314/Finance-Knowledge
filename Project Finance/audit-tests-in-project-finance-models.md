# Audit Tests in Project Finance Models

**Source:** https://edbodmer.com/audit-tests-in-project-finance-models

---

This webpage discusses my opinion on the A for Accuracy in FAST (I call the A accuracy while some call this appropriate). The fundamental thing to do is to let excel tell you where you have made your errors using TRUE/FALSE flags and an audit page. This is really not a big deal and can test the incredible joy of the balance sheet balancing. Please not that the accuracy is often better tested by making clean, structured and transparent equations.  When making your automatic audits, you can overdo things if you follow some kind of horrible bureaucratic and disgusting rules. Instead, please to not be a petty mind and instead make your tests more creative. My idea is that you make sure the crucial places where you can make an error are addressed in your audit page. As I often say, modelling should be a creative process and not follow some kind of SMART/FAST blah blah rules. 

The screenshots below present a couple of examples of the audit sheet. Note that you can press the CNTL, \[ and the F5 keys to find where the errors are located. You can put the summary description shown on the top of the first screenshot. In this example, if there is a False test somewhere, the “Model Ok” will show the problem. Then you can go down to the false and press the CNTL, \[ to find the error and work on the problem.\
\
### The Incredible Great Feeling of Your Balance Sheet Balancing\
\
One necessity is to make a balance sheet and test that it balances in each year. In this case I start with a bad example where a balance sheet was not included.  When you have a lot of MIN/MAX functions in the cash flow statement and multiple debt issues, the balance sheet check is important.  In the example below, there was no balance sheet.\
\
![](https://edbodmer.com/wp-content/uploads/2020/11/image-6.png)\
\
![](https://edbodmer.com/wp-content/uploads/2019/07/No-Balance-Sheet.jpg)\
\
The screenshot below illustrates how you can use one of the formulas to the left to make tests.  You could throw all of these tests into an audit page.  But when you make the audit tests too complex and too extensive, people will stop paying attention. The real tests are probably three.  First, the balance sheet must balance. Second, the debt must be fully repaid. Third, the circular references in the construction financing and created from debt sculpting must be resolved correctly. The example below is for a test in one of the left columns and makes sure there is only one flag that is on.  Note that the conditional TRUE/FALSE formatting also may help.  Note again, how the conditional formatting from the generic macros works where the flags that are on are in green and the flags that are off are in grey.\
\
![](https://edbodmer.com/wp-content/uploads/2019/07/Example-of-Test.jpg)\
\
A bad example of auditing is shown below. In this case a TRUE/FALSE is not used and there is an absurd use of quotes in the test as well as a long OR function.  Finally, the OK rather than a TRUE/FALSE is used as the output.\
\
![](https://edbodmer.com/wp-content/uploads/2019/07/Bad-Audit.jpg)\
\
![](https://edbodmer.com/wp-content/uploads/2020/07/image-67.png)\
\
![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9714&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13756&rand=0.3023566289362747)