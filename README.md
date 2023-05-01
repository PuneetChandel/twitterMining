1. create virtual env - virtualenv -p python3 vtwit
   source source vtwit/bin/activate

2. install dependencies from requirements.txt
3. replace credentials in config.yml for twitter app
4. run app.py to start flask API
5. run runStream.py to activate twitter stream
6. To get top 5 locations for Iphone tweets:
http://0.0.0.0:9001/v1/gadgetscore/Iphone

sample: Top 5 locations

[  
    {  
        "location": "USA",  
        "name": "Iphone",  
        "score": 300  
    },  
    {  
        "location": "Unknown",  
        "name": "Iphone",  
        "score": 99  
    },  
    {  
        "location": "China",  
        "name": "Iphone",  
        "score": 9  
    },  
    {  
        "location": "California, USA",  
        "name": "Iphone",  
        "score": 8  
    },  
    {  
        "location": "Austin, TX",  
        "name": "Iphone",  
        "score": 6  
    }  

]  


Test Merge 
