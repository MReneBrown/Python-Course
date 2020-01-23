db.createUser({
  user: 'jordan',
  pwd: 'password',
  customData: { startDate: new Date() },
  roles: [
    { role: 'clusterAdmin', db: 'admin' },
    { role: 'readAnyDatabase', db: 'admin' },
    'readWrite'
  ]
})

db.getUsers()
db.dropUser('jon')


# db.getUsers()
# [
#         {
#                 "_id" : "test.jon",
#                 "userId" : UUID("a0f8c1df-f104-4a5d-8718-63acde1b27de"),
#                 "user" : "jon",
#                 "db" : "test",
#                 "customData" : {
#                         "startDate" : ISODate("2020-01-23T18:09:40.635Z")
#                 },
#                 "roles" : [
#                         {
#                                 "role" : "clusterAdmin",
#                                 "db" : "admin"
#                         },
#                         {
#                                 "role" : "readAnyDatabase",
#                                 "db" : "admin"
#                         },
#                         {
#                                 "role" : "readWrite",
#                                 "db" : "test"
#                         }
#                 ],
#                 "mechanisms" : [
#                         "SCRAM-SHA-1",
#                         "SCRAM-SHA-256"
#                 ]
#         },
#         {
#                 "_id" : "test.jordan",
#                 "userId" : UUID("2e072ab0-09f2-4d88-9b31-7056cdb9d459"),
#                 "user" : "jordan",
#                 "db" : "test",
#                 "customData" : {
#                         "startDate" : ISODate("2020-01-23T18:03:58.778Z")
#                 },
#                 "roles" : [
#                         {
#                                 "role" : "clusterAdmin",
#                                 "db" : "admin"
#                         },
#                         {
#                                 "role" : "readAnyDatabase",
#                                 "db" : "admin"
#                         },
#                         {
#                                 "role" : "readWrite",
#                                 "db" : "test"
#                         }
#                 ],
#                 "mechanisms" : [
#                         "SCRAM-SHA-1",
#                         "SCRAM-SHA-256"
#                 ]
#         }
# ]



# db.dropUser('jon')
# true
# > db.getUsers()
# [
#         {
#                 "_id" : "test.jordan",
#                 "userId" : UUID("2e072ab0-09f2-4d88-9b31-7056cdb9d459"),
#                 "user" : "jordan",
#                 "db" : "test",
#                 "customData" : {
#                         "startDate" : ISODate("2020-01-23T18:03:58.778Z")
#                 },
#                 "roles" : [
#                         {
#                                 "role" : "clusterAdmin",
#                                 "db" : "admin"
#                         },
#                         {
#                                 "role" : "readAnyDatabase",
#                                 "db" : "admin"
#                         },
#                         {
#                                 "role" : "readWrite",
#                                 "db" : "test"
#                         }
#                 ],
#                 "mechanisms" : [
#                         "SCRAM-SHA-1",
#                         "SCRAM-SHA-256"
#                 ]
#         }
# ]