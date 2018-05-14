# [Repeat Buyers Prediction-Challenge the Baseline](https://tianchi.aliyun.com/getStart/information.htm?spm=5176.11165291.5678.2.4cb96764mpRgOE&raceId=231576)

## 任务
需要预测(这些)新客户在6个月之内从同一商家购买商品的概率。对指定的商家预测在未来（这些）新客户是否将成为忠诚的消费者。

## 数据
data_format2中数据特征：

|**label**|含义|解释|
|---------|----|---|
|1|user_id是merchant_id的一个重复购买者|也就是说在双十一及之前的6个月里user_id在这个merchant_id中购买过商品|
|0|不是|前6个月内没有买过东西，那6个月之前呢？如果买过是不是和-1这个标签重复了？|
|-1|user_id不是merchant_id的一个新消费者，只是超出了本次预测|有可能在一年前买过东西|
|NULL|仅存在于test中，是我们本次需要预测的|


