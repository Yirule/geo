# geo
- https://perso.liris.cnrs.fr/eguerin/new/blog/deep-terrains-code-and-data/
## Prequesites
### Download pre-trained model
https://perso.liris.cnrs.fr/eguerin/download/multi_train.tgz
다운 후 압축 해제

### Install tensorflow
```sh
pip3 install tensorflow
```

### Download pix2pix
```sh
git clone -b png16bits-support --single-branch https://github.com/eric-guerin/pix2pix-tensorflow.git
```

### Use tensorflow v1
`pix2pix.py`에서
```py
import tensorflow as tf
```
를
```py
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
```
로 대체

### Run!
```sh
python pix2pix-tensorflow/pix2pix.py --png16bits --mode test --output_dir multi_test --input_dir multi/val --checkpoint multi_train
```