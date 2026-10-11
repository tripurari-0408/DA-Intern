
CREATE DATABASE SalesAnalyticsDB;
USE SalesAnalyticsDB;

CREATE TABLE product_reference (
    Product VARCHAR(100) PRIMARY KEY,
    Category VARCHAR(100),
    Unit_Price DECIMAL(10, 2)
);

CREATE TABLE sales_records (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Customer VARCHAR(100),
    Customer_Age INT,
    Gender VARCHAR(10),
    City VARCHAR(50),
    Product VARCHAR(100),
    Quantity INT,
    Total_Sales DECIMAL(10, 2),
    FOREIGN KEY (Product) REFERENCES product_reference(Product)
);

INSERT INTO product_reference (Product, Category, Unit_Price) VALUES
('Laptop', 'Electronics', 1200.00),
('Headphones', 'Electronics', 150.00),
('Running Shoes', 'Sports', 80.00);

INSERT INTO sales_records (Order_ID, Order_Date, Customer, Customer_Age, Gender, City, Product, Quantity, Total_Sales) VALUES
(1001, '2026-01-05', 'John Doe', 28, 'Male', 'New York', 'Laptop', 2, 2400.00),
(1002, '2026-01-06', 'Jane Smith', 34, 'Female', 'Chicago', 'Headphones', 3, 450.00),
(1003, '2026-01-08', 'Sam Wilson', 22, 'Male', 'New York', 'Running Shoes', 1, 80.00),
(1004, '2026-01-10', 'Emily Davis', 29, 'Female', 'Los Angeles', 'Laptop', 1, 1200.00);



-- TASK 1: Introduction to Databases & SELECT Statement

SELECT * FROM sales_records;

SELECT 
    Customer AS Customer_Name, 
    Total_Sales AS Revenue 
FROM sales_records;

-- TASK 2: WHERE, ORDER BY & Aggregate Functions
SELECT Customer, Total_Sales 
FROM sales_records 
WHERE Total_Sales > 500 
ORDER BY Total_Sales DESC;

SELECT 
    COUNT(Order_ID) AS Total_Orders,
    SUM(Total_Sales) AS Grand_Total,
    AVG(Total_Sales) AS Average_Sale,
    MIN(Total_Sales) AS Minimum_Sale,
    MAX(Total_Sales) AS Maximum_Sale
FROM sales_records;


-- TASK 3: GROUP BY & HAVING


SELECT 
    City, 
    COUNT(Order_ID) AS Order_Count, 
    SUM(Total_Sales) AS City_Revenue
FROM sales_records
GROUP BY City;

SELECT 
    City, 
    SUM(Total_Sales) AS City_Revenue
FROM sales_records
GROUP BY City
HAVING SUM(Total_Sales) > 1000;


-- TASK 4: SQL Joins (INNER, LEFT, RIGHT)

SELECT s.Order_ID, s.Customer, p.Category, s.Total_Sales
FROM sales_records s
INNER JOIN product_reference p ON s.Product = p.Product;

SELECT p.Product, s.Order_ID, s.Customer
FROM product_reference p
LEFT JOIN sales_records s ON p.Product = s.Product;

SELECT s.Order_ID, p.Category, s.Total_Sales
FROM product_reference p
RIGHT JOIN sales_records s ON p.Product = s.Product;


-- TASK 5: SQL Subqueries
SELECT Order_ID, Customer, Total_Sales 
FROM sales_records 
WHERE Total_Sales > (SELECT AVG(Total_Sales) FROM sales_records);
