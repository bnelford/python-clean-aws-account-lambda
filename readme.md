#Lambda Sandbox Account Cleanup

##WARNING! Be sure to apply this ONLY to a sandbox account, or it will wipe out all your EC2 instances, volumes, snapshots, & buckets. 

#Description
This is used to keep a "sandbox" AWS account clean - to be executed periodically in order to reduce research & training costs. 

#Usage
$./garbage_plan_test.sh

#Requirements
-for testing, the python egg emulambda