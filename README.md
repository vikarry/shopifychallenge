# Shopify Challenge

## Question 1: 
Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

#### Question 1.a	
Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

#### Question 1.b	 
What metric would you report for this dataset?

#### Question 1.c	 
What is its value?

## Question 2:
For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below

#### Question 2.a		
How many orders were shipped by Speedy Express in total

#### Question 2.b	
What is the last name of the employee with the most orders?

#### Question 2.c	
What product was ordered the most by customers in Germany?

# Solutions:

## [Question 1.a](#Question-1.a)
Looking at the original data, the AOV is 3145.128, however the standard deviation is extremely high indicating the inaccuracy

![Screen Shot 2022-05-18 at 12 23 30 PM](https://user-images.githubusercontent.com/59035332/169093560-09a5206a-856d-4c6d-b9db-4b55db849b54.png)

Scanning through the data given, a few obvious outliers can be observed. A scatter dot graph was created to explictly display and track the outliers. From the graph, there is a clear distinction and variation in the data for shop 42 and shop 78. While shop 42 contributes to a signle value outlier of 700,000, shop 78 has multple values that does not belong. 

<img width="625" alt="WeChat9ded99c454af21ce4ce0f73ab6c3c397" src="https://user-images.githubusercontent.com/59035332/169094308-984cb1c2-d863-4e53-ad1a-6c9accb67133.png">

To further analyze the details of the outliers. Shop 42 and shop 78 were ploted individually. 
From the graph, shop 42 had multiple bulk orders in the time frame given each with 2,000 items and total value of 700,000. 
Whereas shop 78, instead of selling bulk quantities per order, individual items are sold at a much higher price of $25,725 per pair of sneakers. 

![Screen Shot 2022-05-18 at 12 35 29 PM](https://user-images.githubusercontent.com/59035332/169095591-80e09b41-f721-47db-a02f-6eddbdee542a.png)


![Screen Shot 2022-05-18 at 12 35 06 PM](https://user-images.githubusercontent.com/59035332/169095607-250bbd85-1ae8-4765-8f61-843c7559d5b6.png)


