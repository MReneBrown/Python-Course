db.books.insert({
    "name": "Deep Work: Rules for Focused Success in a Distracted World",
    "publishedDate": new Date(),
    "reviews": 100,
    "authors": [
        {"name": "Cal Newport"}
    ]
})

WriteResult({ "nInserted" : 1 })


// db.books.find({ reviews: {$exists: true }})

// { "_id" : ObjectId("5e3335662f3ad99bf1fd5742"), "name" : 
// "Deep Work: Rules for Focused Success in a Distracted World", 
// "publishedDate" : ISODate("2020-01-30T19:58:30.323Z"), "reviews" : 100, 
// "authors" : [ { "name" : "Cal Newport" } ] }


db.books.find({ reviews: {$exists: false }})

{ "_id" : ObjectId("5e31ab9bf9a255a545b0091c"), "name" : "Confident Ruby", 
"publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : 
[ { "name" : "Avdi Grimm" } ] }

{ "_id" : ObjectId("5e31ab9bf9a255a545b0091d"), "name" : "The War of Art", 
"publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : [ 
    { "name" : "Steven Pressfield" } ] }

{ "_id" : ObjectId("5e31ab9bf9a255a545b0091e"), "name" : "Blink", 
"publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : [ 
    { "name" : "Malcolm Gladwell" } ] }

{ "_id" : ObjectId("5e31d3584fc77ded4b30d1f5"), "name" : "Blink", 
"publishedDate" : ISODate("2020-01-29T18:47:52.474Z"), "authors" : [ 
    { "name" : "Malcolm Gladwell" }, { "name" : "Ghost Writer" } ] }

{ "_id" : ObjectId("5e331143e8973afc56f6f35f"), "name" : "Blink", 
"publishedDate" : ISODate("2020-01-30T17:24:19.522Z"), "authors" : [ 
    { "name" : "Malcolm Gladwell", "active" : "true" }, 
    { "name" : "Ghost Writer", "active" : "true" } ] }

{ "_id" : ObjectId("5e3325767abbca6511299f84"), "name" : "Deep Work: 
Rules for Focused Success in a Distracted World", "publishedDate" : 
ISODate("2020-01-30T18:50:30.026Z"), "authors" : [ { "name" : "Cal Newport" } ] }