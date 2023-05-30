--DROP TABLE dbo.News
--DROP TABLE dbo.Origin


CREATE TABLE dbo.Origin(
    OriginId INT IDENTITY NOT NULL PRIMARY KEY, -- primary key column
    [Description] NVARCHAR(100) NOT NULL,
);
GO

CREATE TABLE dbo.News(
    NewsId INT IDENTITY NOT NULL PRIMARY KEY, -- primary key column
    [TextNews] NTEXT NOT NULL,
    [Date] DATE NOT NULL,
    [Time] TIME NOT NULL,
    [Label] BIT,
    [OriginId] INT NOT NULL,
    FOREIGN KEY (OriginId) REFERENCES Origin(OriginId),
);
GO
CREATE TABLE dbo.Users(
    UserId INT IDENTITY NOT NULL PRIMARY KEY, -- primary key column
    [Name] VARCHAR(50) NOT NULL,
    [Surname] VARCHAR(50),
    [Email] VARCHAR(100),
);
GO

CREATE TABLE dbo.YourTable(
    [Date] VARCHAR(10) NOT NULL,
    [Time] VARCHAR(10) NOT NULL,
    [TextNews] TEXT NOT NULL,
    [Label] VARCHAR(10),
);
GO