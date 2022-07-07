import os
import numpy as np

gso_scene_names, gso_scene_names_400= [], []
if os.path.exists('data/google_scanned_objects'):
    for fn in os.listdir('data/google_scanned_objects'):
        if os.path.isdir(os.path.join('data/google_scanned_objects',fn)):
            gso_scene_names.append(f'gso/{fn}/black_raw')
            gso_scene_names_400.append(f'gso/{fn}/black_400')

dtu_names=['birds','bricks','snowman','tools']
dtu_name2scan_id={'tools':'scan37', 'snowman':'scan69', 'bricks':'scan40', 'birds':'scan106'}
dtu_train_scene_names = []
dtu_test_scene_names_400 = []
dtu_test_scene_names_800 = []
dtu_test_scene_names_1600 = []
if os.path.exists('data/dtu_train') and os.path.exists('data/dtu_test'):
    fns = os.listdir('data/dtu_train')
    fns = [fn for fn in fns if fn.startswith('scan')]
    test_scenes = os.listdir('data/dtu_test')

    test_scans = np.loadtxt('configs/dtu_test_scans.txt',dtype=np.str).tolist()
    train_scans = [fn for fn in fns if fn not in test_scans]
    dtu_train_scene_names = [f'dtu_train/{fn}' for fn in train_scans]
    dtu_test_scene_names_400 = [f'dtu_test/{fn}/black_400' for fn in test_scenes]
    dtu_test_scene_names_800 = [f'dtu_test/{fn}/black_800' for fn in test_scenes]
    dtu_test_scene_names_1600 = [f'dtu_test/{fn}/black_1600' for fn in test_scenes]

real_iconic_scene_names_8 = []
real_iconic_scene_names_4 = []
if os.path.exists('data/real_iconic_noface'):
    fns = os.listdir('data/real_iconic_noface')
    real_iconic_scene_names_8 = [f'real_iconic/{fn}/8' for fn in fns]
    real_iconic_scene_names_4 = [f'real_iconic/{fn}/4' for fn in fns]

space_scene_names = []
if os.path.exists('data/spaces_dataset'):
    fns = os.listdir('data/spaces_dataset/data/800')
    space_scene_names = [f'space/{fn}' for fn in fns]

real_estate_scene_names = []
if os.path.exists('data/real_estate_dataset'):
    fns = os.listdir('data/real_estate_dataset/train/frames')
    real_estate_scene_names = [f'real_estate/{fn}/450_800' for fn in fns]

nerf_syn_val_ids=['val-r_39', 'val-r_2', 'val-r_94', 'val-r_62', 'val-r_23', 'val-r_36']
nerf_syn_names = ['chair','drums','ficus','hotdog','lego','materials','mic','ship']

llff_names = ['fern','flower','fortress','horns','leaves','orchids','room','trex']
LLFF_ROOT = f'data/llff_colmap'

NERF_SYN_ROOT = f'data/nerf_synthetic'




# Comparison dataset.
dataset_dir = 'data'

dtu_dir = os.path.join(dataset_dir,'dtu')
if os.path.exists(dtu_dir):
    file_list_train = os.path.join(dtu_dir, 'new_train.lst')
    file_list_test = os.path.join(dtu_dir, 'new_val.lst')
    
    with open(file_list_train, "r") as f:
        train_scenes = [x.strip() for x in f.readlines()]
    
    with open(file_list_test, "r") as f:
        test_scenes = [x.strip() for x in f.readlines()]

    dtu_train_scene_names = [os.path.join('dtu', x) for x in train_scenes]
    dtu_test_scene_names = [os.path.join('dtu', x) for x in test_scenes]


real_iconic_noface_dir = os.path.join(dataset_dir,'real_iconic_noface')
if os.path.exists(dtu_dir):
    file_list_train = os.path.join(real_iconic_noface_dir, 'new_train.lst')
    file_list_test = os.path.join(real_iconic_noface_dir, 'new_val.lst')
    
    with open(file_list_train, "r") as f:
        train_scenes = [x.strip() for x in f.readlines()]
    
    with open(file_list_test, "r") as f:
        test_scenes = [x.strip() for x in f.readlines()]

    real_iconic_noface_train_scene_names = [os.path.join('real_iconic_noface', x) for x in train_scenes]
    real_iconic_noface_test_scene_names = [os.path.join('real_iconic_noface', x) for x in test_scenes]

ibrnet_collected_1_dir = os.path.join(dataset_dir,'ibrnet_collected_1')
if os.path.exists(dtu_dir):
    file_list_train = os.path.join(ibrnet_collected_1_dir, 'new_train.lst')
    file_list_test = os.path.join(ibrnet_collected_1_dir, 'new_val.lst')
    
    with open(file_list_train, "r") as f:
        train_scenes = [x.strip() for x in f.readlines()]
    
    with open(file_list_test, "r") as f:
        test_scenes = [x.strip() for x in f.readlines()]

    ibrnet_collected_1_train_scene_names = [os.path.join('ibrnet_collected_1', x) for x in train_scenes]
    ibrnet_collected_1_test_scene_names = [os.path.join('ibrnet_collected_1', x) for x in test_scenes]

ibrnet_collected_2_dir = os.path.join(dataset_dir,'ibrnet_collected_2')
if os.path.exists(dtu_dir):
    file_list_train = os.path.join(ibrnet_collected_2_dir, 'new_train.lst')
    file_list_test = os.path.join(ibrnet_collected_2_dir, 'new_val.lst')
    
    with open(file_list_train, "r") as f:
        train_scenes = [x.strip() for x in f.readlines()]
    
    with open(file_list_test, "r") as f:
        test_scenes = [x.strip() for x in f.readlines()]

    ibrnet_collected_2_train_scene_names = [os.path.join('ibrnet_collected_2', x) for x in train_scenes]
    ibrnet_collected_2_test_scene_names = [os.path.join('ibrnet_collected_2', x) for x in test_scenes]