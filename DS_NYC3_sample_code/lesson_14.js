use test;
db.createCollection('people');
show collections;


// Add in a new document to the people collection
db.people.insert({'name' : 'Ed'});
db.people.insert({'name' : 'John'});

// Update a previously written document in a collection
db.people.update({'name' : 'Ed'}, { $set : { 'weight' : 185 }})
db.people.update({'name' : 'John'}, { $set : { 'height' : 72, 'gender' : 'male'}
person = db.people.findOne()
person.gender


