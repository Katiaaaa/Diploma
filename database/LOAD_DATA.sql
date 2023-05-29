
BULK INSERT dbo.YourTable
FROM 'D:\Radarixx\University\4 KYPC\2\diploma\myData\data\data_news.csv'
WITH (
    FIRSTROW = 2,  -- Skip the header row if present
    FORMAT='CSV'
   --FIELDTERMINATOR = ',',  -- Specify the field delimiter
   --ROWTERMINATOR = '\n'  -- Specify the row delimiter
);

select top 10 * from dbo.YourTable

INSERT INTO dbo.News(TextNews, [Date], [Time], Label, OriginId)
SELECT
    TextNews,
    CONVERT(DATE, temp.[Date], 103),
    CAST(temp.Time as time),
    CASE
        WHEN temp.Label = 'true' THEN 1
        WHEN temp.Label = 'false' THEN 0
    END,
    CASE
        WHEN temp.Label = 'true' THEN 2
        WHEN temp.Label = 'false' THEN 1
    END
FROM dbo.YourTable AS temp


select * from dbo.News