# Commodity Price Database Including Futures Download

**Source:** https://edbodmer.com/databases-and-graphs/databases-from-internet/commodity-price-database

---

This webpage describes a database file along with videos that allows you to download and create analyses of historic commodity prices as well as commodity futures prices.  You can automatically download data and then evaluate some prices. Databases on commodity prices use information from the world bank “pink data” and from the Chicago Mercantile Exchange (CME). The database file from the world bank is structured so that you can compare time series and analyze commodity price trends. The database file with futures prices allows you to evaluate futures prices for various different commodities including oil, natural gas, coal and electricity. I have also included VBA code to create the commodity databases where you can read the data and upload it.  As with all of the databases, they are structured so that you can delete the old data and then upload new data. If you upload the data and then it does not work, please send me an e-mail at edwardbodmer@gmail.com.

Commodity prices can be very volatile, have mean reversion and be correlated with one another. The first step for analysis of assumptions related to commodity prices should therefore be gathering historic data. Sources for acquiring data include the world bank and futures markets. The world bank website includes a lot of monthly data on many commodity prices  (except, unfortunately, diesel prices, petrochemical prices, petrol prices, steel prices and other prices that are from refined products). Local electricity commodity prices are also not in the database and are included in the energy analysis part of the website.  The website for the world bank for the historic monthly data is below:

[http://pubdocs.worldbank.org/en/561011486076393416/CMO-Historical-Data-Monthly.xlsx.](http://pubdocs.worldbank.org/en/561011486076393416/CMO-Historical-Data-Monthly.xlsx.)

.

**[Database of Commodity Prices that Reads from World Bank PinkData and Adjusts for Inflation with Flexible Graphs](https://edbodmer.com/wp-content/uploads/2026/01/Commodity-Price-Analysis-16.04.2025.xlsm)
**

.

**[File that Contains Monthly Commodity Price History and World Bank Commodity Price Forecasts with Automatic Updates](https://edbodmer.com/wp-content/uploads/2021/09/Commodity-Price-Analysis.xlsm)
**

.

Commodity Price History and Forecast Database
---------------------------------------------

I think there are a few sources for financial and economic data that are really good. One of the sources is the world bank data base that records and updates commodity prices called for some reason pink data. On this World Bank web site you can download monthly nominal prices since 1960 for more than 100 commodity price series. The workbook file listed below goes to the pink data part of the world bank website and updates historic commodity price data as well as forecast data published by the world bank. To update the history data you just have to press the macro button. You can download this file by pressing the button below. As with any of the databases or financial models, if you are having any issues with running and updating the program (sometimes the URLs or the formats change), you would help me by sending an e-mail to my address at edwardbodmer@gmail.com.

You may have to update the URL for the monthly data using the world bank data. To do this, go to the world bank website on commodity prices using the link:

[https://www.worldbank.org/en/research/commodity-markets](https://www.worldbank.org/en/research/commodity-markets)

![](https://edbodmer.com/wp-content/uploads/2021/06/image-10.png)

Then, right click on the monthly prices download illustrated above and copy the URL to the spreadsheet in the workbook. This link is in the sheet named “download data.” The URL should be placed in Cell D6.

![](https://edbodmer.com/wp-content/uploads/2021/06/image-11.png)

Basic VBA Code to Download Link
-------------------------------

The link sometimes changes, but the code is very simple. The code below goes to the worldbank site and downloads the data. It also puts the data into the same sheet.

    Sub read_file()
    
    base_book = ActiveWorkbook.Name     ' define the current book
    
    Workbooks.Open (Range("url"))       ' open the monthly file
    
    temp_book = ActiveWorkbook.Name    ' name of the new workbook that is read and will be closed
    
     Sheets("Monthly Prices").Select   ' sheet name in the file that is read in
     Cells.Select
     Selection.Copy                    ' copy the whole sheet to the current workbook
     Workbooks(base_book).Activate
     
     Sheets("Monthly Prices").Select   ' sheet in the base commodity price file
     Range("A1").Select
     ActiveSheet.Paste
     Application.CutCopyMode = False
        
     Workbooks(temp_book).Close
            
    tot_num = WorksheetFunction.CountA(Range("A8:A8000"))
        
    Range("tot_num") = tot_num          ' total number of months for making graph with offset function
        
    End Sub
    

The link that was relevant for 2021 prices is the link below. It is very possible that this link will change and you will have to update the file to read the natural gas prices.

https://www.eex.com/fileadmin/EEX/Downloads/Market\_Data/EEX\_Group\_DataSource/KWK/20210701\_KWK.xls

You can update the file every month or couple of months and you can use the file to perform statistical analysis of the various commodity prices. The historic data can be updated very easily by pressing the macro button. To update reading of the forecast you have to look-up the link that sometimes changes.

The file allows you to analyse historic data and compare forecast and projected data for a large series of commodity prices.

You can also find commodity price data on the FRED database. The second file goes to the FRED database and puts together a whole bunch of the commodity price series.

Commodity Price Data from the FRED Database
-------------------------------------------

If you want daily prices, you can go to the FRED data.

    Sub Macro2()
    '
    ' Alternative to Indirect
    '
    
    '
    For col = 1 To Range("sheet_names").Columns.Count              ' sheet_names is range name with sheets to get
            
        name_of_sheet = Range("sheet_names").Cells(1, col)         ' Work through the name of each sheet
        
        name_to_replace = "'" & name_of_sheet & "'"                ' create a range name for lookup
            
                                                                   '    MsgBox name_to_replace
            
        cell_address = Range("row_1").Cells(1, 0).Address
        
                                                                   '    MsgBox cell_address
            
        lookup_name = "=LOOKUP(" & cell_address & "," & name_to_replace & "!A:A," & name_to_replace & "!B:B)"
            
                                                                   '    MsgBox lookup_name
            
        Range("row_1").Cells(1, col) = lookup_name                 ' Make sure the row_1 name is there
        
    
    Next col
    
        Range("row_1").Select
        Range(Selection, Selection.End(xlDown)).Select
        Selection.FillDown
    
    
    End Sub
    

Database that Retrieves Commodity Futures Prices
------------------------------------------------

  In addition to the historic prices, you can retrieve data from futures markets using the workbooks.open method and putting together the summary of different futures prices.  The file that you can used to download futures prices and update them is available for download below.  The website for acquiring futures data has changed in the past which can create some problems.  If there are any issues with running and updating the program, please do not hesitate to send me an e-mail at edwardbodmer@gmail.com. . .   **[Database file with Commodity Futures Prices from the CME that you can Update Automatically](https://edbodmer.com/wp-content/uploads/2018/05/Gas-and-Oil-Futures2.xlsm)
** . .     The futures data is downloaded from:[http://www.cmegroup.com/trading/energy/crude-oil/brent-crude-oil.html](http://www.cmegroup.com/trading/energy/crude-oil/brent-crude-oil.html)
.  

  .  

   

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=513&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10336&rand=0.8179283970421942)