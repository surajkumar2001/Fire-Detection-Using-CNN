
import random
import os
import shutil
path = r"D:\AI Project\dataset\fire_dataset\non_fire_images"
src = "D:\\AI Project\\dataset\\fire_dataset\\non_fire_images\\"
dest = "D:\\AI Project\\Newly_formed_dataset\\train\\non_fire"

random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

files = os.listdir(path)
for i in range(int(len(files)/2)):
    while os.path.exists(dest+'/'+str(random_filename)):
        random_filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])

    print(random_filename)
    shutil.move(src+str(random_filename), dest)
