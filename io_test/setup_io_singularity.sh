singularity build io_test.sif docker://docker.elastic.co/elasticsearch/elasticsearch:7.4.2

singularity run --network-args "portmap=9202:9200/tcp" io_test.sif &

sleep 10s

curl -XPUT 'localhost:9202/companydatabase?pretty' -H 'Content-Type: application/json' -d' {"mappings" : { "employees" : { "properties" : { "FirstName" : { "type" : "text" }, "LastName" : { "type" : "text" }, "Designation" : { "type" : "text" }, "Salary" : { "type" : "integer" }, "DateOfJoining" : { "type" : "date", "format": "yyyy-MM-dd" }, "Address" : { "type" : "text" }, "Gender" : { "type" : "text" }, "Age" : { "type" : "integer" }, "MaritalStatus" : { "type" : "text" }, "Interests" : { "type" : "text" }}}}}' 
curl -XPUT 'localhost:9202/companydatabase/_bulk' --data-binary @Employees50K.json