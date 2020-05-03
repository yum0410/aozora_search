# Run Service

```
docker-compose up -d
curl http://localhost:9200/aozora\?pretty -X PUT -H "Content-Type: application/json" -d @./es-data/mapping.json
python insert_book_data.py

# check registration
curl http://localhost:9200/aozora/_doc/_search\?pretty -X GET -H "Content-Type: application/json"

# check search_api
curl http://localhost:9200/aozora/_search -X GET -H "Content-Type: application/json" -d @sample_request.json
```

# Show HTML

* Open `./search_view/index.html` in your web browser.