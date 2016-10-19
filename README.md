# Cascade-Training

## Preparing the samples

### Positive Images

For this project we have judged that the best was to create our own original data, instead of using opencv_createsamples to create artificial data. 
For this we recommend that the files should be taken from your camera. 

Once you have the photos you will need to crop all the images and place them in the CroppedImages directory. After that you should run the 'resize_imgs.py'. That will create a directory 'positive' with all the resized images in grayscale.

### Negative Images

For your convinience this project already have 2606 negative images (that include people, foods and plants). If more are needed there is a python file with a function that given a file in a url (downloaded from [image-net](http://image-net.org/)) downloads all the images listed and resize them to the scale of 200x200px in grayscale.

Enter the neg_imgs.py and alter the url of negative images, ajust the number of the last pic in the neg directory and ajust the size if needed.

After downloaded the images find the images that are unavailable (there is always a pic that is offline and you end up downloading a placeholder) and place one of each kind in the uglies directory. After that run the function find_uglies() inside neg_imgs.py. Finally run the create_neg_txt() to create a bg.txt listing all the negative files.

This is a workaroud to the lazy ones.

## Train the cascade

The script trainCascade has the commands that should be used to acquire the cascade file.
The script assumes that there is available 6000MB in memory available.

Use the script trainCascade.sh to begin training the cascade.

To execute the script enter the terminal an do the following:

$ chmod u+x trainCascade.sh
$ ./trainCascade.sh

Then wait for the process to end

For more informations open the script in your favorite editor and consult the [OpenCV Documents](http://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html?highlight=cascade%2520classifier%2520training).

## Testing the cascade

Run the python file detect.py and place all the testing images in the folder 'Euschistus Heros'. You will be able to see wether the cascade could detect Euschistus H. in the image, or not.
