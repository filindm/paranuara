#!/usr/bin/env bash

set -e
dir=/docker-entrypoint-initdb.d
mongoimport --db paranuara --collection companies --file $dir/companies.json --jsonArray
mongoimport --db paranuara --collection people --file $dir/people.json --jsonArray
