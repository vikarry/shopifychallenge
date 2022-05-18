# Shopify Challenge

## Question 1 [code](master/sneaker/sneakers.py): 
Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

[1.a Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.](#question-1a)

[1.b What metric would you report for this dataset?](#question-1b)

[1.c What is its value?](#question-1c)

## Question 2:
For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below

[2.a	How many orders were shipped by Speedy Express in total](#question-2a)

[2.b	What is the last name of the employee with the most orders?](#question-2b)

[2.c	What product was ordered the most by customers in Germany?](#question-2c)

# Solutions:

### Question 1.a
  Looking at the original data, the AOV is 3145.128, however the standard deviation is extremely high indicating the inaccuracy

![Screen Shot 2022-05-18 at 12 23 30 PM](https://user-images.githubusercontent.com/59035332/169093560-09a5206a-856d-4c6d-b9db-4b55db849b54.png)

  Scanning through the data given, a few obvious outliers can be observed. A scatter dot graph was created to explictly display and track the outliers. From the graph, there is a clear distinction and variation in the data for shop 42 and shop 78. While shop 42 contributes to a signle value outlier of 700,000, shop 78 has multple values that does not belong. 

<img width="625" alt="WeChat9ded99c454af21ce4ce0f73ab6c3c397" src="https://user-images.githubusercontent.com/59035332/169094308-984cb1c2-d863-4e53-ad1a-6c9accb67133.png">

  To further analyze the details of the outliers. Shop 42 and shop 78 were ploted individually. 
From the graph, shop 42 had multiple bulk orders in the time frame given each with 2,000 items and total value of 700,000. 
Whereas shop 78, instead of selling bulk quantities per order, individual items are sold at a much higher price of $25,725 per pair of sneakers. 

![Screen Shot 2022-05-18 at 12 35 29 PM](https://user-images.githubusercontent.com/59035332/169095591-80e09b41-f721-47db-a02f-6eddbdee542a.png)


![Screen Shot 2022-05-18 at 12 35 06 PM](https://user-images.githubusercontent.com/59035332/169095607-250bbd85-1ae8-4765-8f61-843c7559d5b6.png)

  Calcualting the total sales of shop 42 and shop 78 and finding its percentage of the total sales of all shops leads to the conclusion of excluding these two shops for the calculation of AOV should reduce the large deviation since these outliers contributed to nearly 90% of the total amount.

![Screen Shot 2022-05-18 at 1 19 52 PM](https://user-images.githubusercontent.com/59035332/169104772-a949985c-140f-4aa6-b6cf-9a24b8b3c720.png)


### Question 1.b

  Instead of looking at the mean, we could also use median as a metric since the mean is proven to be skewed due to outliers from shop 42 and shop 78


### Question 1.c

  284


### Question 2.a
  54
  
  ```
  SELECT COUNT(*) 
  FROM Orders o LEFT OUTER JOIN Shippers p on o.ShipperID = p.ShipperID
  WHERE ShipperName = 'Speedy Express';
  ```

### Question 2.b
  Peacock
  
  ```
  SELECT LastName 
  FROM Employees e LEFT OUTER JOIN Orders o on e.EmployeeID = o.EmployeeID
  GROUP BY e.EmployeeID
  ORDER BY COUNT(*) DESC
  LIMIT 1;
  ```
  
### Question 2.c

  Steeleye Stout
  
  ```
  SELECT ProductName
  FROM (Orders o LEFT OUTER JOIN OrderDetails d ON o.OrderID = d.OrderID) 
  LEFT OUTER JOIN Customers c on o.CustomerID = c.CustomerID
  LEFT OUTER JOIN Products p on p.ProductID = d.ProductID
  WHERE c.Country = 'Germany'
  ORDER BY d.Quantity DESC
  LIMIT 1
  ```
