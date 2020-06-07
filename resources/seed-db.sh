#!/usr/bin/env bash

set -e
dir=/docker-entrypoint-initdb.d
mongoimport --db paranuara --collection companies --file $dir/companies.json --jsonArray
mongoimport --db paranuara --collection people --file $dir/people.json --jsonArray
mongo paranuara <<EOF
    db.companies.createIndex({
        index: 1
    },{
        unique: true,
    })
    db.people.createIndex({
        company_id: 1
    },{})
    db.people.createIndex({
        index: 1
    },{
        unique: true,
    })
EOF
