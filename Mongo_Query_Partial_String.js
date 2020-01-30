db.books.insert({
    "name": "Deep Work: Rules for Focused Success in a Distracted World",
    "publishedDate": new Date(),
    "authors": [
        {"name": "Cal Newport"}
    ]
});

WriteResult({ "nInserted" : 1 })


db.books.findOne({name: /.*deep work.*/i})

// {
//     "_id" : ObjectId("5e3325767abbca6511299f84"),
//     "name" : "Deep Work: Rules for Focused Success in a Distracted World",
//     "publishedDate" : ISODate("2020-01-30T18:50:30.026Z"),
//     "authors" : [
//             {
//                     "name" : "Cal Newport"
//             }
//     ]
// }

db.books.findOne({name: 'deep work'})

null