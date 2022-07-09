#! /bin/sh

for f in $(find /app/input -name '*.mp4' -or -name '*.jpg'); do
    n=$(ls /app/tmp | wc -l)
    ((n=n+1))
    ffmpeg -hide_banner -i $f -r 0.2 -start_number $n /app/tmp/frame_%04d.jpg
done

for f in $(find /app/tmp -name 'frame_*.jpg'); do
    filename=$(basename "$p")
    ./recognizer --assets ../../../assets --charset latin --openvino_enalbed false --image $f > /app/output/${filename}.txt
done

/bin/bash
