db.books.insert({
    "name": "OOP Programming",
    "publishedDate": new Date(),
    "authors": [
      {"name": "Jon Snow"},
      {"name": "Ned Stark"}
    ]
})

db.books.insert({
    "name": "OOP Programming",
    "publishedDate": new Date(),
    "authors": [
      {"name": "Jon Snow Jr"},
    ]
})

db.books.insert({
    "name": "OOP Programming",
    "startDate": new Date(),
    "authors": [
      {"name": "Jon Snow Jr"},
    ]
})


db.books.find()
{ "_id" : ObjectId("5e29f97ba7b549acc04dc046"), "name" : "OOP Programming", "publishedDate" : 
ISODate("2020-01-23T19:52:27.200Z"), "authors" : [ { "name" : "Jon Snow" }, { "name" : "Ned Stark" } ] }

{ "_id" : ObjectId("5e2a0151a7b549acc04dc047"), "name" : "OOP Programming", "publishedDate" : 
ISODate("2020-01-23T20:25:53.497Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }

{ "_id" : ObjectId("5e2a016ba7b549acc04dc048"), "name" : "OOP Programming", "startDate" : 
ISODate("2020-01-23T20:26:19.272Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }

