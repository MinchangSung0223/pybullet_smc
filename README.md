## Install bullet3
```bash
git clone https://github.com/bulletphysics/bullet3.git
cd bullet3
export bullet3_HOME=$PWD
./build_cmake_pybullet_double.sh
rm -r data
cp -r  ../data/ data
cp ../examples/* examples/pybullet/examples/
python3 examples/pybullet/examples/indy7_table.py 

```

