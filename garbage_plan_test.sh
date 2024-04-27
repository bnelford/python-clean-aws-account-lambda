#!/bin/bash
echo "Starting garbage cleanup test locally with emulambda..."

#First, shut down all instances - this may need about 1 min
emulambda -v aws_lambda_stop_all_instances.lambda_handler test-event.json
sleep 30
#Next, terminate all instances
emulambda -v aws_lambda_terminate_all_instances.lambda_handler test-event.json
sleep 30

#Next, detach all volumes
emulambda -v aws_lambda_detach_all_volumes.lambda_handler test-event.json
sleep 30

#Next, delete all volumes
emulambda -v aws_lambda_delete_all_volumes.lambda_handler test-event.json
sleep 30

#Next, delete all snapshots
emulambda -v aws_lambda_delete_all_snapshots.lambda_handler test-event.json
sleep 30

#clean up the s3 buckets
emulambda -v aws_lambda_delete_all_buckets.lambda_handler test-event.json
sleep 30

echo "Garbage has been removed."

exit 0
