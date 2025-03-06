# blink-to-type
Blink to type from a file using OpenCV.

**TODO:**
1. clean up code and housekeeping
	- isolate functions
	- change names that feel weird
	- slightly better documentation
2. fix relative paths so code can be run from outermost directory
~~3. write installation guide~~
4. write a fun lil write up
	- eventually a blog post
5. e-beg for a job
6. optional: add typing velocity feature
7. optional: deploy online demo
8. *rewrite code so that input txt file can be passed in as argument with a flag*
9. *change after making requirements.txt*
10. *change after making requirements.txt*
11. add machine specs

## Installation
Requirements:
- Tested on *insert my machine's specs here*

Install required packages
```
pip install opencv-python numpy dlib imutils
```

Create `Models` directory and download required dlib model
```
cd blink_to_type
mkdir Models
cd Models
curl -O https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
bzip2 -d filename.bz2
```

## Local Usage
