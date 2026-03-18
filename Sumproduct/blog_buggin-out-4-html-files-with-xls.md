# Buggin’ Out #4: HTML Files with .xls

**Source:** https://sumproduct.com/blog/buggin-out-4-html-files-with-xls/

---

[Home](https://sumproduct.com/)

\> Buggin’ Out #4: HTML Files with .xls

*   August 6, 2016

Buggin’ Out #4: HTML Files with .xls
====================================

Buggin’ Out #4: HTML Files with .xls
====================================

7 August 2016

_Microsoft updates means new and improved features, but it also means the odd bug slipping through. In this incidental series we cover some of the recent known issues that have cropped up and how to fix and / or circumvent them._

_**HTML Files with .xls**_

Users have reported that HTML files with .xls extensions are not opening outside Protected View in Excel 2010, 2013 or 2016.

In order to increase security, the behaviour of certain file types has been changed. These changes have emanated from security updates [KB3115262](https://support.microsoft.com/en-us/kb/3115262)
, [KB3170008](https://support.microsoft.com/en-us/kb/3170008)
 and [KB3115322](https://support.microsoft.com/en-us/kb/3115322)
. The security update changed how Excel handles documents that are opened from untrusted locations (such the Internet zone) which are not supported in Protected View, such as HTML, xml and xla files. Opening these documents without Protected View is seen as a security vulnerability and therefore files open from such locations have now been blocked.

Therefore, users will need to manually trust the file before they open them in Excel. Excel can still open these files without an issue if they are trusted. It would be nice though if Excel displayed a more helpful error message with information about what to do next rather than showing a blank screen.

Microsoft strongly recommends against removing the security updates. These actions will leave your systems vulnerable. More information is located [here](https://technet.microsoft.com/library/security/MS16-088?f=255&MSPPError=-2147217396)
. In particular, please refer to the section regarding “Microsoft Office Security Feature Bypass Vulnerability – CVE-2016-3279” if this affects you.

As workarounds, the best option is to move away from using HTML wrapped as an .xls document. If you use native formats (_e.g._ xls, xlsx, xlsb) which will open in protected view when untrusted, this will provide some level of protection from the documents being opened.

Otherwise, you can unblock access for individual files you know are safe. To do this

*   Right-click the file, and choose **Properties**
*   On the **General** tab, click **Unblock**
*   Click **OK**.

Alternatively, you can make use of existing Trusted Locations capabilities in Excel 2010, 2013 and 2016 via **File > Options > Trust Center > Trust Center Settings > Trusted Locations**.

You can save the web html file to a trusted location on the local machine (Excel comes with a set of default trust locations). If you do not see the local folder location you trust for these files, then press “Add new location…” button and add it in the Trusted Location dialog. If the HTML document is in a trusted location the KB fix is not applied (_e.g._ the unsafe HTML file is not blocked).

This approach may unblock you, but it carries some risk as files of any file type in Trusted Locations are fully trusted. If an attacker can drop files into the trusted location they can easily exploit users who open such documents. Be especially cautious when specifying a custom folder as a trusted location.

There are further resources on implementing workaround options, by product version:

**_Office 2016_**

[Office Trusted Locations](https://technet.microsoft.com/en-us/library/cc179039(v=office.16).aspx)

[Protected View Settings](https://technet.microsoft.com/en-us/library/ee857087(v=office.16).aspx)

**_Office 2013_**

[Office Trusted Locations](https://technet.microsoft.com/en-us/library/cc179039(v=office.15).aspx)

[Protected View Settings](https://technet.microsoft.com/en-us/library/ee857087(v=office.15).aspx)

**_Office 2010_**

[Office Trusted Locations](https://technet.microsoft.com/en-us/library/cc179039(v=office.14).aspx)

[Protected View Settings](https://technet.microsoft.com/en-us/library/ee857087(v=office.14).aspx)

_We will report on other bug fixes and workarounds as and when necessary. Hopefully, this will not be too regular a feature!! In the meantime, if you experience any Excel issues and require help, do feel free to drop us a line at [contact@sumproduct.com](mailto:contact@sumproduct.com)
 – we can’t promise to answer every question, but we’ll try our best._

![](<Base64-Image-Removed>)

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/buggin-out-4-html-files-with-xls/#0)
    
*   [Register](https://sumproduct.com/blog/buggin-out-4-html-files-with-xls/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/buggin-out-4-html-files-with-xls/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/buggin-out-4-html-files-with-xls/#0)

[](https://sumproduct.com/blog/buggin-out-4-html-files-with-xls/#0 "close")

top