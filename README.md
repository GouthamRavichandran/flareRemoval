# How to Train Neural Networks for Flare Removal

A Reimplementation of the paper https://yichengwu.github.io/flare-removal/

## To Train
Create a python environment and install packages from requirements.txt.

``python -m python.train \ --train_dir=training_out \ --scene_dir=input_data_set \ --flare_dir=input_flare_images``

## To Remove flare
``python -m python.remove_flare \ --ckpt=model_location  \ --input_dir=test_images_folder \ --out_dir=output_folder``


## Our Contribution
Edwin Lingson: Ran the code in his machine and stored the outputs and the summary folder.

Goutham Ravichandran: Helped in implementing the code by running the PSNR and SSIM metrics for assessing the test images quality. Also helped in preparing the final project report.
