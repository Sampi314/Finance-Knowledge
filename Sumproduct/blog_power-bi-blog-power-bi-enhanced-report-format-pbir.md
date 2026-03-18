# Power BI Blog: Power BI Enhanced Report Format (PBIR)

**Source:** https://sumproduct.com/blog/power-bi-blog-power-bi-enhanced-report-format-pbir/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Power BI Enhanced Report Format (PBIR)

*   July 24, 2024

Power BI Blog: Power BI Enhanced Report Format (PBIR)
=====================================================

Power BI Blog: Power BI Enhanced Report Format (PBIR)
=====================================================

25 July 2024

Microsoft has recently announced the **Power BI enhanced report format (PBIR)** for Power BI Project files (PBIP). This marks a significant milestone in achieving the primary goal of Power BI Desktop developer mode: to provide source control friendly file formats that unblock co-development and enhance development efficiency.

Power BI Projects (PBIP) now support saving the report and semantic model into a folder using source-control friendly formats: **PBIR** for the report and **TMDL** for the semantic model.

![](<Base64-Image-Removed>)

The PBIR file format greatly simplifies the tracking of changes and resolution of merge conflicts by using properly formatted JSON and organizing each visual, page, bookmark, _etc._, in separate individual files within a folder structure.

![](<Base64-Image-Removed>)

You can also greatly enhance your report development efficiency, either by simply copying and pasting or pasting visuals / pages / bookmarks/… files between reports or apply manual / programmatic batch changes to the PBIR files.

Unlike PBIR-Legacy (report.json), PBIR is a publicly documented format and allows modifications from non-Power BI applications. Each file has a public JSON schema, which documents each property and lets code editors like Visual Studio Code perform syntax validation while editing. On open, Power BI Desktop will validate the changed PBIR files to guarantee successful loading.

To open it , do remember PBIR is currently in Preview, and you can only create or convert existing Power BI project files to PBIR using Power BI Desktop. You must first enable the feature in Power BI Desktop preview features: go to **File -> Options and settings -> Options -> Preview features** and check the box next to ‘Store reports using enhanced metadata format (PBIR)’.

During Preview, Fabric Git Integration and Fabric REST Apis will continue to use PBIR-Legacy (report.json) when exporting the report definitions. However, if the report is imported into Fabric using PBIR format, then both features will start exporting the report definition using PBIR format. At General Availability, PBIR will become the default report format.

Initially, the PBIR format will have some service restrictions, such as:

*   unable to publish the report in Power BI App
*   unable to use subscriptions
*   unable to download PBIX.

These restrictions will be removed in the following months.

That’s it for this week. Please stay tuned and don’t miss out on more thoughts and insights from [https://www.sumproduct.com](https://www.sumproduct.com/)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-power-bi-enhanced-report-format-pbir/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-power-bi-enhanced-report-format-pbir/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-power-bi-enhanced-report-format-pbir/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-power-bi-enhanced-report-format-pbir/#0)

[](https://sumproduct.com/blog/power-bi-blog-power-bi-enhanced-report-format-pbir/#0 "close")

top