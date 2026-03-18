# Power Pivot 2010: Microsoft Interim Fix for Windows 10

**Source:** https://sumproduct.com/news/power-pivot-2010-microsoft-interim-fix-for-windows-10/

---

[Home](https://sumproduct.com/)

\> Power Pivot 2010: Microsoft Interim Fix for Windows 10

*   August 5, 2015

Power Pivot 2010: Microsoft Interim Fix for Windows 10
======================================================

Power Pivot 2010: Microsoft Interim Fix for Windows 10
======================================================

5 August 2015

Over the past few days, we have kept our readers up to date with the issue that Power Pivot 2010 was not working in Excel 2010 after the Windows 10 Update. A similar issue was discovered by some users who had installed Visual Studio 2015.

Today, Microsoft has made a formal announcement. It transpires that with the release of these two products an issue was found in the 64-bit versions of the following products:

*   Power Pivot for Microsoft Excel 2010; and
*   Data Mining Add-ins for Microsoft Excel (Table Analysis Tools and Data Mining Client).

When installing either of these products, .NET (version 4.6), the default .NET version that comes with Windows 10 and Visual Studio 2015, users discovered that opening Excel with either add-in enabled will result in Excel crashing. When users then attempt to re-start Excel, one of the following error messages appears:

*   **For PowerPivot for Microsoft Excel 2010:** “Excel experienced a serious problem with ‘Power Pivot for Excel’ add-in. If you have seen this message multiple times, you should disable this add-in and check to see if an update is available. Do you want to disable this add-in?”
*   **For the Data Mining Add-ins:** “Excel experienced a serious problem with ‘sqlserver.dmclientxladdin’ add-in. If you have seen this message multiple times, you should disable this add-in and check to see if an update is available. Do you want to disable this add-in?”.

This is caused by a change to the 64-bit JIT compiler in .NET 4.6, which has exposed an issue with both add-ins that has remained hidden until now.

Microsoft is continuing to investigate the issue and agree a final fix. In the meantime, a workaround is available by allowing Excel to use the previous 64-bit JIT for .NET by adding a file to your Excel folder as follows:

*   Navigate to the folder with your Excel executable (Excel.exe), usually “C:Program FilesMicrosoft OfficeOffice14?. If you cannot find the folder:
    *   Open windows explorer
    *   Select This PC
    *   Search for “Excel.exe” in the “Search this PC” box on the upper right side of Explorer
    *   Right-click on the file and select “open file location”
*   Create a file “Excel.exe.config” in this folder and then open the file with notepad and add the following contents:

<configuration>

<runtime>

<useLegacyJit enabled=”1? />

</runtime>

*   Save the file
*   Reopen Excel.

Adding this file causes Excel to use the same 64-bit JIT as was available the previous version of .NET. When a ‘proper’ fix has been released for this issue, users might wisht to change this behaviour back to the default JIT by deleting the file just created in the workaround.

We would provide a copy of the file for you here but we don’t want you to think we are asking you to download dodgy files. If you want to download the file rather than create it, it can be downloaded from Microsoft’s website [here](http://blogs.msdn.com/b/analysisservices/archive/2015/08/05/data-mining-and-power-pivot-for-excel-2010-add-in-issues-with-windows-10-and-visual-studio-2015.aspx)
 where you can also read Microsoft’s full article on the subject (pretty much reproduced here!). Further details regarding RyuJIT may also be found [here](https://github.com/Microsoft/dotnet/blob/master/docs/testing-with-ryujit.md)
.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/power-pivot-2010-microsoft-interim-fix-for-windows-10/#0)
    
*   [Register](https://sumproduct.com/news/power-pivot-2010-microsoft-interim-fix-for-windows-10/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/power-pivot-2010-microsoft-interim-fix-for-windows-10/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/power-pivot-2010-microsoft-interim-fix-for-windows-10/#0)

[](https://sumproduct.com/news/power-pivot-2010-microsoft-interim-fix-for-windows-10/#0 "close")

top