# AWP API Documentation

So, you want to use the AWP API in your project? Well, you've come to the right place! This guide will walk you through the steps to get started with the AWP API.

This documentation will assume basic knowledge of RESTful APIs. If you are unfamiliar with RESTful APIs, you can read more about them [here](https://aws.amazon.com/what-is/restful-api/).

## Table of Contents

- [AWP API Documentation](#awp-api-documentation)
  - [Table of Contents](#table-of-contents)
  - [Requests](#requests)
  - [Entrypoints](#entrypoints)
    - [Manual Input](#manual-input)
    - [Future Prediction](#future-prediction)
    - [Present Prediction](#present-prediction)

## Requests

The AWP API is a RESTful API, meaning that it uses HTTP requests to GET, PUT, POST and DELETE data. The API is hosted on [Railway](https://railway.app/), and can be accessed [here](awp-production.up.railway.app/).

## Entrypoints

There are 3 entrypoints to the AWP API:

- `manual`: Allows you to manually input temperature, wind speed, humidity and rain values to get a prediction.
- `future`: Allows you to get a prediction for one of the next 9 days.
- `present`: Allows you to get a prediction for the current day, given the place.

### Manual Input

To get a prediction from the API with your own temperature, wind speed, humidity and rain values, you make the following request:

```shell
GET https://awp-production.up.railway.app/manual?temp=TEMP&wind=WS&rh=HUM&rain=RAIN
```

Where `TEMP` is the temperature, `WS` is the wind speed, `HUM` is the humidity and `RAIN` is the rain. For example, if you wanted to get a prediction for a temperature of 20 degrees Celsius, a wind speed of 10 km/h, a humidity of 50% and no rain, you would make the following request:

```shell
GET https://awp-production.up.railway.app/manual?temp=20&wind=10&rh=50&rain=0
```

The API will then return a JSON object with the following structure:

```json
{
    "data": "prediction"
}
```

Where `prediction` is the prediction, as a float. The following is an example of a response:

```json
{
    "data": 0.123456789
}
```

### Future Prediction

To get a prediction from the API for one of the next 9 days, you make the following request:

```shell
GET https://awp-production.up.railway.app/future?day=DAY
```

Where `DAY` is the (integer) day you want to get a prediction for. You would input a number from 1-9, where 1 is tomorrow, 2 is the day after, etc. For example, if you wanted to get a prediction for tomorrow, you would make the following request:

```shell
GET https://awp-production.up.railway.app/future?day=1
```

The API will then return a JSON object with the following structure:

```json
{
    "data": "prediction"
}
```

Where `prediction` is the prediction, as a float. The following is an example of a response:

```json
{
    "data": 0.123456789
}
```

### Present Prediction

To get a prediction from the API for the current day, you make the following request:

```shell
GET https://awp-production.up.railway.app/present?place=PLACE
```

Where `PLACE` is the place you want to get a prediction for. For example, if you wanted to get a prediction for Tung Chung, you would make the following request:

```shell
GET https://awp-production.up.railway.app/present?place=tung%20chung
```

*If the place requested is not available, it will default to a random place in Hong Kong.*

The API will then return a JSON object with the following structure:

```json
{
    "data": "prediction"
}
```

Where `prediction` is the prediction, as a float. The following is an example of a response:

```json
{
    "data": 0.123456789
}
```
