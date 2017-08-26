# Torrent parser with connection to MongoDB

### Description
Script that gets all the torrents currently only from torrention.me the book section
Script connect's through pymongo to local MongoDB Server and insert's all the information in the DB.
To function properly: install MongoDB and start the server OR change the connection OR change the code.
If you prefer to change the code to see it work:
1. Remove ```books.insert(i)``` and instead write ```books.append(i)
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
OR Manually in terminal
```
pip install requests
pip install bs4
```

