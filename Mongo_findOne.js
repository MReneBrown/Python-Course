db.books.find({name: "Blink"})

// { "_id" : ObjectId("5e31ab9bf9a255a545b0091e"), "name" : "Blink", 
// "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : 
// [ { "name" : "Malcolm Gladwell" }rs" : [ { "name" : "Malcolm Gladwell" } ] }

// { "_id" : ObjectId("5e31d3584fc77ded4b30d1f5"), "name" : "Blink", 
// "publishedDate" : ISODate("2020-01-29T18:47:52.474Z"), "authors" : 
// [ { "name" : "Malcolm Gladwell" }rs" : [ { "name" : "Malcolm Gladwell" }, 
// { "name" : "Ghost Writer" } ] }

// { "_id" : ObjectId("5e331143e8973afc56f6f35f"), "name" : "Blink", 
// "publishedDate" : ISODate("2020-01-30T17:24:19.522Z"), "authors" : 
// [ { "name" : "Malcolm Gladwell", rs" : [ { "name" : "Malcolm Gladwell", 
// "active" : "true" }, { "name" : "Ghost Writer", "active" : "true" } ] }


db.books.find({name: "Blink"}).length()

3

db.books.findOne({name: "Blink"})

{
    "_id" : ObjectId("5e31ab9bf9a255a545b0091e"),
    "name" : "Blink",
    "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
    "authors" : [
            {
                    "name" : "Malcolm Gladwell"
            }
    ]
}
