# Torrent parser with connection to MongoDB and Flask Search Interface

### The Flask interface only is being developed
At this moment the Flask interface is just an example of how to get started
on the work with Flask and MongoDb.

The description for the Flask interface will be made after the complete version will be done!

### Description of the Parser
Script that gets all the torrents (currently only from torrentino.me book section) <br />
Script connect's through pymongo to the local MongoDB Server and insert's all the information in the DB. <br />
To function properly: <br />
install MongoDB and start the server OR change the connection OR change the code. <br />
If you prefer to change the code to see it work:
1. Remove ```books.insert(i)``` and instead write ```books.append(i)```
2. Make an empty list before the cycle ```books = []```


### Installation
1. Clone repository or download zip
```
git clone https://github.com/rusnano0/torrent_parser.git
```
2. Install requirements
Auto from requirements.txt
```
pip install -r requirements.txt
```

### Creating Indexes in Pymongo after inserting the data
```
books.create_index([('title', pymongo.TEXT)], name='search_index', default_language='russian')
```

### Usefull links about indexes in MongoDB
1. [https://docs.mongodb.com/manual/indexes/](https://docs.mongodb.com/manual/indexes/)
2. [https://docs.mongodb.com/v3.4/core/index-text/](https://docs.mongodb.com/v3.4/core/index-text/)
3. [http://learnmongodbthehardway.com/schema/indexes/](http://learnmongodbthehardway.com/schema/indexes/)
4. [https://www.guru99.com/working-mongodb-indexes.html](https://www.guru99.com/working-mongodb-indexes.html)

### Usefull link on $text query operator
[https://docs.mongodb.com/manual/reference/operator/query/text/](https://docs.mongodb.com/manual/reference/operator/query/text/)

