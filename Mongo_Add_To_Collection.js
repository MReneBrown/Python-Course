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


// db.books.find()
// { "_id" : ObjectId("5e29f97ba7b549acc04dc046"), "name" : "OOP Programming", "publishedDate" : 
// ISODate("2020-01-23T19:52:27.200Z"), "authors" : [ { "name" : "Jon Snow" }, { "name" : "Ned Stark" } ] }

// { "_id" : ObjectId("5e2a0151a7b549acc04dc047"), "name" : "OOP Programming", "publishedDate" : 
// ISODate("2020-01-23T20:25:53.497Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }

// { "_id" : ObjectId("5e2a016ba7b549acc04dc048"), "name" : "OOP Programming", "startDate" : 
// ISODate("2020-01-23T20:26:19.272Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }


db.books.insertMany([
  {
      "name": "Confident Ruby",
      "publishedDate": new Date(),
      "authors": [
          { "name": "Avdi Grimm"}
      ]    
  },
  
  {
    "name": "The War of Art",
    "publishedDate": new Date(),
    "authors": [
      {"name": "Steven Pressfield"}
    ]
  },
  {
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
      {"name": "Malcolm Gladwell"}
    ]
  }
])


// {                                         INSERTMANY()
//   "acknowledged" : true,
//   "insertedIds" : [
//           ObjectId("5e31ab9bf9a255a545b0091c"),
//           ObjectId("5e31ab9bf9a255a545b0091d"),
//           ObjectId("5e31ab9bf9a255a545b0091e")
//   ]
// }
// > db.books.find()
// { "_id" : ObjectId("5e29f97ba7b549acc04dc046"), "name" : "OOP Programming", "publishedDate" : ISODate("2020-01-23T19:52:27.200Z"), "authors" : [ { "name" : "Jon Snow" }, { "name" : "Ned Stark" } ] }
// { "_id" : ObjectId("5e2a0151a7b549acc04dc047"), "name" : "OOP Programming", "publishedDate" : ISODate("2020-01-23T20:25:53.497Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }
// { "_id" : ObjectId("5e2a016ba7b549acc04dc048"), "name" : "OOP Programming", "startDate" : ISODate("2020-01-23T20:26:19.272Z"), 
// "authors" : [ { "name" : "Jon Snow Jr" } ] }
// { "_id" : ObjectId("5e31ab9bf9a255a545b0091c"), "name" : "Confident Ruby", "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : [ { "name" : "Avdi Grimm" } ] }
// { "_id" : ObjectId("5e31ab9bf9a255a545b0091d"), "name" : "The War of Art", "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : [ { "name" : "Steven Pressfield" } ] }
// { "_id" : ObjectId("5e31ab9bf9a255a545b0091e"), "name" : "Blink", "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : [ { "name" : "Malcolm Gladwell" } ] }
// > db.books.find().pretty()
// {
//   "_id" : ObjectId("5e29f97ba7b549acc04dc046"),
//   "name" : "OOP Programming",
//   "publishedDate" : ISODate("2020-01-23T19:52:27.200Z"),
//   "authors" : [
//           {
//                   "name" : "Jon Snow"
//           },
//           {
//                   "name" : "Ned Stark"
//           }
//   ]
// }
// {
//   "_id" : ObjectId("5e2a0151a7b549acc04dc047"),
//   "name" : "OOP Programming",
//   "publishedDate" : ISODate("2020-01-23T20:25:53.497Z"),
//   "authors" : [
//           {
//                   "name" : "Jon Snow Jr"
//           }
//   ]
// }
// {
//   "_id" : ObjectId("5e2a016ba7b549acc04dc048"),
//   "name" : "OOP Programming",
//   "startDate" : ISODate("2020-01-23T20:26:19.272Z"),
//   "authors" : [
//           {
//                   "name" : "Jon Snow Jr"
//           }
//   ]
// }
// {
//   "_id" : ObjectId("5e31ab9bf9a255a545b0091c"),
//   "name" : "Confident Ruby",
//   "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
//   "authors" : [
//           {
//                   "name" : "Avdi Grimm"
//           }
//   ]
// }
// {
//   "_id" : ObjectId("5e31ab9bf9a255a545b0091d"),
//   "name" : "The War of Art",
//   "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
//   "authors" : [
//           {
//                   "name" : "Steven Pressfield"
//           }
//   ]
// }
// {
//   "_id" : ObjectId("5e31ab9bf9a255a545b0091e"),
//   "name" : "Blink",
//   "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
//   "authors" : [
//           {
//                   "name" : "Malcolm Gladwell"
//           }
//   ]
// }
// > db.books.find({ name: "The War of Art"}).pretty()                FIND()
// {
//   "_id" : ObjectId("5e31ab9bf9a255a545b0091d"),
//   "name" : "The War of Art",
//   "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
//   "authors" : [
//           {
//                   "name" : "Steven Pressfield"
//           }
//   ]
// }

// db.books.find(
//   {
//     name: "Confident Ruby"
//   }
// )

// { "_id" : ObjectId("5e31ab9bf9a255a545b0091c"), "name" : "Confident Ruby", 
// "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"), "authors" : 
// [ { "name" : "Avdi Grimm" } ] }



db.books.find(
  {
    name: "Confident Ruby"
  },
  {
    publishedDate: 1,
    authors: 1
  }
).pretty()

OUTPUT
{
  "_id" : ObjectId("5e31ab9bf9a255a545b0091c"),
  "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
  "authors" : [
          {
                  "name" : "Avdi Grimm"
          }
  ]
}



db.books.find(
  {
    name: "Confident Ruby"
  },
  {
    _id: 0,
    publishedDate: 1,
    authors: 1
  }
).pretty()

OUTPUT
{
  "publishedDate" : ISODate("2020-01-29T15:58:19.085Z"),
  "authors" : [
          {
                  "name" : "Avdi Grimm"
          }
  ]
}






db.books.insert({
  "name": "Blink",
  "publishedDate": new Date(),
  "authors": [
    { "name": "Malcolm Gladwell" },
    { "name": "Ghost Writer" }
  ]
});


db.books.find(
  {
    name: "Blink"
  },
  {
    publishedDate: 1,
    name: 1,
    authors: { $slice: 1}
  }
).pretty()

OUTPUT
{
  "_id" : ObjectId("5e31d3584fc77ded4b30d1f5"),
  "name" : "Blink",
  "publishedDate" : ISODate("2020-01-29T18:47:52.474Z"),
  "authors" : [
          {
                  "name" : "Malcolm Gladwell"
          }
  ]
}


db.books.find(
  {
    name: "Blink"
  },
  {
    publishedDate: 1,
    name: 1,
    authors: { $slice: 2}
  }
).pretty()

OUTPUT
{
  "_id" : ObjectId("5e31d3584fc77ded4b30d1f5"),
  "name" : "Blink",
  "publishedDate" : ISODate("2020-01-29T18:47:52.474Z"),
  "authors" : [
          {
                  "name" : "Malcolm Gladwell"
          },
          {
                  "name" : "Ghost Writer"
          }
  ]
}


db.books.find(
  {
    name: "Blink"
  },
  {
    publishedDate: 1,
    name: 1,
    authors: { $slice: -1}
  }
).pretty()

OUTPUT
{
  "_id" : ObjectId("5e31d3584fc77ded4b30d1f5"),
  "name" : "Blink",
  "publishedDate" : ISODate("2020-01-29T18:47:52.474Z"),
  "authors" : [
          {
                  "name" : "Ghost Writer"
          }
  ]
}


db.remove({name: "OPP Programming"}, 1)

WriteResult({ "nRemoved" : 1 })

db.remove({name: "OPP Programming"})

NO RESULT AS ALL OPP PROGRAMMING DOCUMENTS HAVE BEEN DELETED


