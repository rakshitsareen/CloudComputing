import boto3
import json
import yelp_fusion_api
import datetime



#api_key="-5dBnE7ZnbVw1RshcBve1t-Ayg00nnw4PEMj-in726bQM4jODmHTgdUKIEQXzKKgq4hrainJdwniItyA5tZOFg71e9yrEDuqa-tDoxlPpxxzFtQ20Jlr6AcSXRDlW3Yx"
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'

#details = {"area": "Manhattan", "time": "8:30", "dining": "dinner", "cuisine": "Indian", "date": "2018-11-09"}

def time_convert(time, date):
    
    date = date.split("-")
    year, month, day = int(date[0]), int(date[1]), int(date[2])
    time = time.split(":")
    hours, minute = int(time[0]), int(time[1])

    return int(datetime.datetime(year, month, day, hours, minute, tzinfo=datetime.timezone.utc).timestamp())


def get_info_yelp(details, api_key):
    area = details['area']
    time = details['time']
    dining = details['dining']
    cuisine = details['cuisine']
    date = details['date']
    print("The date is "+str(date))
    categories = dining+","+cuisine
    converted_time = time_convert(time, date)
    print("The converted_time is "+str(converted_time))
    
    url_params = {
        'term': cuisine.replace(' ', '+'),
        'categories': categories.replace(' ', '+'),
        'location': area.replace(' ', '+'),
        'open_at': converted_time,
        'limit': 5

    }
    resp2 = yelp_fusion_api.request(API_HOST, SEARCH_PATH, api_key, url_params)
    print("The Response from yelp is "+str(resp2))
    # logger.info("The Response from yelp is "+str(resp2))
    yelp_data_array = []
    for i in resp2['businesses']:
        name,price,rating,phone_number,address = "NA","NA","NA","NA","NA"
    
        if 'name' in i:
            name = i['name']
    
        if 'price' in i:
            price = i['price']
    
        if 'rating' in i:
            rating = i['rating']
    
        if 'display_phone' in i :
            phone_number = i['display_phone']
    
        if 'location' in i:
            if 'display_address' in i['location']:
                address = ''.join(str(e) for e in i['location']['display_address'])
    
        data = {
            "restaurant_name" : name,
            "rating" : str(rating),
            "price" : price,
            "phone" : phone_number,
            "address" : address
        }
    
        yelp_data_array.append(data)
    
    print("The final yelp data array "+str(yelp_data_array))
    return yelp_data_array
   
