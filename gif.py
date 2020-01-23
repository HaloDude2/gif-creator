import imageio
images = []
filenames = ["Asset 1.png", "Asset 2.png", "Asset 3.png", "Asset 4.png", "Asset 5.png", "Asset 6.png", "Asset 7.png", "Asset 8.png"]
for filename in filenames:
        images.append(imageio.imread(filename))
imageio.mimsave('anamate.gif' , images, duration=0.5)