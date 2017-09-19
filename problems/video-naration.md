# Video Naration

## Problem statement

- Describe contents of video in real time to users that may or may not be able to see the scene themselves.
- Respond to user voice commands and requests for information about the visual scene.

## Caveat

This architecture was developed "open loop" based on what I'm familiar with. A real architecture design would require collaboration among stakeholders, most importantly the engineers tasked with implementing and maintaining it.

## User (Client Hardware)

### Client Sensor Data

- camera: images, video, and metadata including focal length, exposure, etc)
- IMU: acceleration and rotational rate
- GPS: approximate geolocation augmented by WIFI RSS triangulation within Android/iOS and KF
- temperature, atmospheric pressure: irrelevant?

### Client Processing

- CPU: 64-bit ARM, Snapdragon
- GPU: low throughput, limited HPC library support; no CUDA, but [tensorflow maybe](https://github.com/samjabrahams/tensorflow-on-raspberry-pi)

### Example Hardware Options

- Google Glass type headsets tethered to a mobile device
- Handheld mobile device pointed at the scene
- Mobile device in a chest pocket a.la. the movie "Her"

### UX

User is wearing an ear-piece or headset or listening to audio from the phone to receive voice descriptions of the scene or objects in it from an Aira agent (e.g. Cleo and/or a human).

User may issue voice commands through microphones in their headset and/or mobile device.
Mobile hardware transcribes user voice commands to text (e.g. using Android voice recognition service or on-board library). Increasing complex commands are added to the agent's repertoire as features during product development based on user feedback and developer assessment (Agile poker scoring).

#### Voice Data Flow

1. user: voice
2. mobile: speech-to-text
3. mobile: some limited Alexa-like command recognition and response ("identify", "describe", "read")
4. Aira (AWS or Aira Cleo API): correlate user commands with semantic information from images (see below)
5. Aira (AWS or Aira Cleo API): generate natural language voice or text response
5. mobile: text-to-speech on text from Cleo or stream audio from Cleo or human agent directly

#### Video Data Flow

1. user: point camera
2. mobile: compress video
3. mobile: layers of neural net up to "neck-down" (detected features) to reduce comm bandwidth
4. mobile: stream features or compressed video to Aira service
5. Aira (Google service or Aira Cleo): semantic analysis of image frames and video using a deep net

#### Example Interactions

Some example problems/features in approximate order of increasing complexity:

1. "What am I looking at?": object recognition -- one prominent object in center of FOV
2. "Read this text.": OCR on a stitched+registered image (panorama from multiple frames of video)
3. "Summarize this text." OCR (work for braille too) and text summarization, read menu, street sign, computer screen, etc
4. "Describe this.": image semantic analysis, more complete description of scene/image and multiple objects in it)
5. "What's around me?: semantic SLAM -- use stitched "videosphere" or "videorama" (synthetic/stitched low frame rate video panorama) to estimate current state of the environment, objects nearby, and user location within it
6. "Is it safe for me to go?" (requires interaction with agent who will ask user to look in particular directions)
7. "Who is this?": face recognition and contacts lookup with fallback to stereotyping (race/gender/hair-color/clothing-color/body-build even sexual-orientation)
8. "What is this person is doing?": facial expression recognition and narration, gesture/pose/activity recognition and narration

... etc ...

## Training Servers

An always-on cluster of GPUs for training on all labeled data as it arrives from customers and mechanical turk.

Cluster should be optimized for back propagation of neural networks and image processing/transformation.

- prioritize high reliability labeled data over unsupervised or low reliability data (from users)
- image and video transforms to augment labeled training data and use up entire capacity of cluster
- it may make sense to have a small in-house rack of GPUs optimized for image processing

A scalable cluster for experiments and "catch-up" on backlog of training data scheduled for always-on cluster.

## "Production" Client-Server Software Architecture

### Components

#### Video Processing

These are the major video processing algorithms in the system.
The first two are required for an MVP.
The last two add advanced functionality.

1. image registration: Kalman Filter on Accels+Gyros to register images on sphere around user with short (1 s?) time constant (like Google image sphere)
2. image segmentation and object recognition: neural net to identify and localize objects in the "photo sphere" with 10-100 ms time constant
3. SLAM: long time-constant (30-min) SLAM (KF on image features) to track object and user locations over time
4. direct video-narration: train a CNN+LSTM+? network on compressed(?) video using frame-based semantic analysis

#### Speech

These are the major NLP algorithms in the system.
Speech-to-text and text-to-speech components are available for free or for low cost.
The first two are required for an MVP.
The last one adds advanced functionality.

1. template/FSM-based natural language command/request recognition
2. template-based natural language description from list of objects and their fixed locations in the visual field
3. conversation engine (natural language agent) to respond to user requests other than limited keyword-based commands

### 1. Image Registration

If possible this task should be offloaded to the client hardware as much as possible.
Crude real-time registration is possible with the mobile device IMU alone.
Registered image sequences (video-panorama) would then be compressed and streamed to both human agents and Cleo at a rate and image quality compatible the network connection bandwidth.

### 2. Image Semantic Analysis

Neural networks like RESNET or VGG for simultaneous image segmentation and object recognition (see TED talk video by MS with laptop demo tracking 100+ objects with ms latency on a laptop with GPU)

### 3. SLAM

Existing SLAM packages would be deployed to the production server cluster (below) to track objects identified by Image Semantic Analysis.

### 4. Direct Video Semantic Analysis?

It may ultimately be possible to directly "translate" compressed or uncompressed video streams into text. Training data could be acquired from human agent descriptions of scenes following "narration" requests from users.
Frame-based narration neural nets could also be used to generate training data from any archived or streaming video.
Video Semantic Analysis is like frame-based image semantic analysis but must also incorporate location and movement information from SLAM, such as:

- "a person is moving left to right"
- "a cat is lying on the sidewalk in 6 feet in front of you"
- "car is driving directly towards you." ("move to your right quickly to get behind a barrier")

These text streams would be aligned with the video to train a sequence to sequence deep learning model.

### Server Hardware

Build up to an AWS "fleet" over time as customer base grows. Client mobile/wearable app exercises Aira streaming API using compressed image stream or stream of extracted features (image sequence embeddings)

1. utilize CPU on wearable and tethered phone for image/video compression and streaming to Aira API
2. utilize CPU on wearable and tethered phone for forward-propogation of video through first layer of neural net
3. utilize CPU+GPU  on wearable and phone for first few layers (to neckdown) of neural net

Incrementally scaled up servers, all optimized for image processing/compression and forward propagation of neural networks.

1. DRF or APIstar on a single-core single-threaded server serving a single request at a time
2. Single 16-core 16-worker (Celery) server serving a maximum of 16 simultaneous clients
2. Static cluster of 16-core 16-worker (celery) server serving a maximum of 16 simultaneous clients
3. Elastic load balancer to distribute load from <1000 simultaneous requests to <100 [dynamically scaled](https://aws.amazon.com/autoscaling/#dynamic) AWS EC2 instances
4. research/experiment with AWS lambda "nodes" to determine scalability economics


## Crowd-Sourcing Development

If Aira open sourced individual modules and data sets (equivalent to sponsoring in-house Kaggle competitions) Total Good could manage a competition + mentorship program to manage an open source developer community.
Visually impaired developers might even be enlisted in training and software development tasks.

, (not the executive that combines them)

## References

1. [Start Training YOLO with Our Own Data - Guanghan Ning's Blog](http://guanghan.info/blog/en/my-works/train-yolo/)
1. [Basic YOLOv2 in keras for an MVP?](https://github.com/experiencor/basic-yolo-keras)
2. [Andrew Ng at Spark Summit mentioning DuLight project for visually impaired](https://www.youtube.com/watch?v=4eJhcxfYR4I&feature=youtu.be)
3. [Demo video of DuLight in China urban environment](https://www.youtube.com/watch?v=Xe5RcJ1JY3c)
4. [Example Day in the Life of Visually Impaired in China](https://www.youtube.com/watch?v=XRWG4WhwXvI)
5. [eSight enhances video to expand what lowsight users (legally blind) can see](https://www.esighteyewear.com/)
6. [visualization of keras CNNs like VGG](https://github.com/experiencor/deep-viz-keras)
