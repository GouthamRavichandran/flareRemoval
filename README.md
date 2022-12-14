# How to Train Neural Networks for Flare Removal

A Reimplementation of the paper https://yichengwu.github.io/flare-removal/

## To Train
``python -m python.train \ --train_dir=training_out \ --scene_dir=input_data_set \ --flare_dir=input_flare_images``

## To Remove flare
``python -m python.remove_flare \ --ckpt=model_location  \ --input_dir=test_images_folder \ --out_dir=output_folder``



