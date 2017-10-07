# qwqeqweqwe

|$$度量方法$$|$$preprocess$$| $$norm$$|$$similarity$$|
|:-----:|:------:|:-----:|:----:|
|余弦相似度|$$\frac{v}{\left \| v \right \|^2}$$|-|$$dot_{ij}$$|
|皮尔逊相似度|$$\frac{v-\bar{v}}{\left \| v-\bar{v} \right \|^2}$$|-|$$dot_{ij}$$|
|欧式距离|-|$$\hat{v}^2$$|$$\sqrt{n_{i}-2\times dot_{ij}+n_{j}}$$|
|杰卡距离| $$bin(v)$$ | $${\left \| \hat{v} \right \|_{1}}$$ |$$\frac{dot_{ij}}{n_{i}+n_{j}-dot_{ij}}$$|
|曼哈顿距离| $$bin(v)$$ | $${\left \| \hat{v} \right \|_{1}}$$ |$$n_{i}+n_{j}-2\times dot_{ij}$$|
| Log-likelihood ratio| $$bin(v)$$ |$${\left \| \hat{v} \right \|_{1}}$$|$$2\times (H(dot_{ij},n_j-dot_{ij},n_j-dot_{ij},|U|-n_i-n_j+dot_{ij})-
H(n_j,|U|-n_j)-H(n_i,|U|-n_i))$$|
<center>表1 标准化的计算算子</center>
