mongoimport --host $HOST --port $PORT --jsonArray --db nobel --collection countries --file country.json
mongoimport --host $HOST --port $PORT --jsonArray --db nobel --collection prizes --file prize.json
mongoimport --host $HOST --port $PORT --jsonArray --db nobel --collection laureates --file laureate.json