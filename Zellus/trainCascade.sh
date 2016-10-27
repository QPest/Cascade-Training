#!/bin/bash
# Danilo Barros Mendes
# Under license APGLv3
find positive -name '*.jpg' -exec identify -format '%i 1 0 0 %w %h' \{\} \; > positives.lst

opencv_createsamples -info positives.lst -vec positives.vec -h 20 -w 20

echo "Try to train now."

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 400 -numNeg 1200 -numStage 15 -w 20 -h 20 -precalcValBufSize 6000 -precalcIdxBufSize 6000 -mode ALL

# Alternative training
# for i in {1..133}
# do
#  opencv_createsamples -bg bg$i.txt samples -maxxangle 0.5 -maxyangle 0.5 -num 30 -img positive/$i.jpg -info info$i.lst
# done

# echo "Done creating samples."

# cat *.lst > final.lst

# opencv_createsamples -info final.lst -vec final.vec -h 20 -w 20
# echo "Try to train now."
# opencv_traincascade -data data -vec final.vec -bg bg.txt -numPos 3500 -numNeg 2000 -numStages 10 -w 20 -h 20

