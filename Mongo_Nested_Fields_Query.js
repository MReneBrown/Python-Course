db.books.insert({
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Malcolm Gladwell", "active": "true" },
        { "name": "Ghost Writer", "active": "true" }
    ]
});


// WriteResult({ "nInserted" : 1 })

db.books.find(
    {
        name: "Blink"
    },
    {
        name: 1,
        publishedDate: 1,
        "authors.name": 1
    }
).pretty()

// {
//     "_id" : ObjectId("5e331143e8973afc56f6f35f"),
//     "name" : "Blink",
//     "publishedDate" : ISODate("2020-01-30T17:24:19.522Z"),
//     "authors" : [
//             {
//                     "name" : "Malcolm Gladwell"
//             },
//             {
//                     "name" : "Ghost Writer"
//             }
//     ]
// }



db.books.find(
    {
        name: "Blink"
    },
    {
        name: 1,
        publishedDate: 1,
        authors: 1
    }
).pretty()


// {
//     "_id" : ObjectId("5e331143e8973afc56f6f35f"),
//     "name" : "Blink",
//     "publishedDate" : ISODate("2020-01-30T17:24:19.522Z"),
//     "authors" : [
//             {
//                     "name" : "Malcolm Gladwell",
//                     "active" : "true"
//             },
//             {
//                     "name" : "Ghost Writer",
//                     "active" : "true"
//             }
//     ]
// }