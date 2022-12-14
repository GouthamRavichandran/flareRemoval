# How to Train Neural Networks for Flare Removal

A Reimplementation of the paper https://yichengwu.github.io/flare-removal/

## To train
``python -m flare_removal.python.train \ --train_dir="A:\google-research\google-research-master\flare_removal\train4" \ --scene_dir="A:\google-research\google-research-master\flare_removal\scene2" \ --flare_dir="A:\google-research\google-research-master\flare_removal\lens-flare"``

## TO Remove flare
``python -m flare_removal.python.remove_flare \ --ckpt="A:\google-research\google-research-master\flare_removal\train4\model"  \ --input_dir="A:\google-research\google-research-master\flare_removal\test" \ --out_dir="A:\google-research\google-research-master\flare_removal\out13"``
