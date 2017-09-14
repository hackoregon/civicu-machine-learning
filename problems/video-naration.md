# Video Narration Problem

## Problem statement

Describe contents of video in real time to users that may or may not be able to see the scene themselves.

## Caveat

Architecture chosen based on what I'm familiar with. A real architecture would involve collaborative design with the engineers tasked with implementing and maintaining it. 

## User (Client Hardware)

### Capability/Data

- camera: images, video, and metadata including focal length, exposure, etc)
- IMU: acceleration and rotational rate
- GPS: approximate geolocation augmented by WIFI RSS triangulation within Android/iOS and KF

### Examples

- Google Glass type headsets tethered to a mobile device
- Handheld mobile device pointed at the scene
- Mobile device in a chest pocket a.la. the movie "Her"

### Interaction

User is wearing an ear-piece or headset or listening to audio from the phone to receive voice descriptions of the scene or objects in it from an Aira agent (e.g. Cleo and/or a human).

User is able to issue voice commands through microphones in their headset and/or mobile device. Mobile hardware transcribes user voice commands to text (e.g. using Android voice recognition service or onboard library). Increasing complex commands are added to the agent's repertoire as features during product development based on user feedback and developer assessment (Agile poker scoring).

#### Example Interactions

Some example problems/features in approximate order of increasing complexity:

1. "What am I looking at?": object recognition -- one prominent object in center of FOV is in the field of view
2. "Read this text.": OCR on a stitched image/sphere
3. "Summarize this text." OCR (work for braille too) and text summarization, read menu, street sign, computer screen, etc
4. "Describe this.": image semantic analysis, more complete description of scene/image and multiple objects in it) 
5. "What's around me?: semantic SLAM -- use stitched "videosphere" or "videorama" (synthetic/stitched low frame rate video panorama) to estimate current state of the environment, objects nearby, and user location within it
6. "Is it safe for me to go?" (requires interaction with agent who will ask user to look in particular directions)
7. "Who is this?": face recognition and contacts lookup with fallback to stereotyping (race/gender/body-build even sexual-orientation)
8. "Let me know what this person is doing?": facial expression recognition and narration, gesture/pose/activity recognition and narration

... etc ...

## Training Servers

An always-on cluster of GPUs for training on all labeled data as it arrives from customers and mechanical turk.

Cluster should be optimized for back propagation of neural networks and image processing/transformation.

- prioritize high reliability labeled data over unsupervised or low reliability data (from users) 
- image and video transforms to augment labeled training data and use up entire capacity of cluster
- it may make sense to have a small rack of GPUs optimized for image processing in-house

A scalable cluster for experiments and 

## "Production" Client-Server Architecture

### Components

The main components of the algorithm that I can think of include

1. image registration: Kalman Filter on Accels+Gyros to register images on sphere around user with short (1 s?) time constant (like Google image sphere)
2. image segmentation and object recognition: neural net to identify objects in the "photo sphere" with 10-100 ms time constant
3. SLAM: long time-constant (30-min) SLAM (KF on image features) to track feature and user location over time

### 1. Image Registration

If possible this task should be offloaded to the client hardware as much as possible. Crude real-time registration is possible with IMU alone.
These registered images would then be compressed and streamed to both human agents and Cleo at a rate and image quality compatible the network connection bandwidth.

### 2. Image Semantic Analysis

Neural networks like RESNET or VGG for simultaneous image segmentation and object recognition (see TED talk video by MS with laptop demo tracking 100+ objects with ms latency on a laptop with GPU)

### 3. SLAM

Existing SLAM packages would be deployed to the production server cluster (below) to track objects identified by Image Semantic Analysis.

### Client Hardware

team deadicated to performainImage stream registration

### Server Hardware

Build up to an AWS "fleet" over time as customer base grows. Client mobile/wearable app exercises Aira streaming API using compressed image stream or stream of extracted features (image sequence embeddings)

1. utilize CPU on wearable and tethered phone for image/video compression and streaming to Aira API
2. utilize CPU on wearable and tethered phone for forward-propogation of video through first layer of neural net
3. utilize CPU+GPU  on wearable and phone for first layer of neural net

Incremental scaling of servers optimized for image processing/compression and forward propagation of neural networks.

1. DRF or APIstar on a single-core single-threaded server serving a single request at a time
2. Single 16-core 16-worker (Celery) server serving a maximum of 16 simultaneous clients
2. Static cluster of 16-core 16-worker (celery) server serving a maximum of 16 simultaneous clients
3. Elastic load balancer to distribute load from <1000 simultaneous requests to <100 [dynamically scaled](https://aws.amazon.com/autoscaling/#dynamic) AWS EC2 instances
4. research/experiment with AWS lambda "nodes" to determine scalability economics


