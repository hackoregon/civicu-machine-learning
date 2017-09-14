## Training Servers

An always-on cluster of GPUs for training on all labeled data as it arrives from customers and mechanical turk.

Cluster should be optimized for back propogation of neural networks and image processing/transformation.

- prioritize high reliability labeled data over unsupervised or low reliability data (from users) 
- image and video transforms to augment labeled training data and use up entire capacity of cluster
- it may make sense to have a small rack of GPUs optimized for image processing in-house

A scalable cluster for experiments and 

## "Production" Servers

Build up to an AWS "fleet" over time as customer base grows.

Incremental rollout and scaling of servers optimized for image processing/compression and forward propagation of neural networks.

1. microsevice (DRF) with a single-core single-threaded server serving a single request at a time
2. microsevice with a 16-core 16-worker (celery) server serving a maximum of 16 simultaneous clients
3. Elastic load balancer to distribute load from <1000 simultaneous requests to <100 [dynamically scaled](https://aws.amazon.com/autoscaling/#dynamic) AWS EC2 instances
4. research/experiment with AWS lambda "nodes" to determine scalability economics
5. 

