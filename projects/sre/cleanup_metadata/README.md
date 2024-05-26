# tic-mts-es-metadata-cleanup  
Utility to clear off stale mts metadata  
  
  
# Design  
The mts indices are evergrowing. Unfortunately, that means constantly increasing size of shards  
The ttl means we can clean them up  
  
  
  
### Effort breakdown  
  
##### Core functionality   
1. able to read data from each configured mts cluster  
   1. can reach cluster  
   2. can select correct index dynamically  
     
2. able to make correct determination whether or not to run the delete   
   1. can query data first to determine amount of docs to delete  
   2. can make a go/nogo call based on amount of docs  
  
3. constructs and runs the delete  
   1. constructs the delete query  
   2. runs the delete query  
   3. waits for query to complete (after initial run should be just the days worth of data)  
   4. if error -> log error, notify slack. move on to the next cluster (?)  
   5. if success -> log success, send message. Can be a single message with the logs of errors and successes  
  
  
##### Additional functionality  
1. Run snapshot before each delete  
   1. This is a super low overhead item, only takes a few minutes  
   2. log it  
2. Run forcemerge after each delete unless time/resource prohibitive  
3. Multithread this - no need to wait on each cluster sequentially  
  
### things to be configurable  
ttl  
max_docs - a circuit breaker  
index names or patterns  
cluster names