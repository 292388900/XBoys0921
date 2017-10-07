1变异测试得分
2变异得分
3测试变异体数
4成功构建比例
5一共执行了
6个变异体程序的测试
7其中
8个程序成功构建
个程序被被测试用例检测出错误
选择的变异体
变异算子类型
变异算子
变异文件
选择变异体中构建成功并执行测试的

y1 56
y2 62
y3 56/62
y4 95
y5 62/95

keylist1 ['AndroidOp','ClassOp','TrandtionalOp','ExceptionOp','XmlOp']

maplist
[
                {value:335, name:'AndroidOp'},
                {value:310, name:'ClassOp'},
                {value:234, name:'TrandtionalOp'},
                {value:135, name:'ExceptionOp'},
                {value:1548, name:'XmlOp'}
            ]

[10, 52, 200, 334, 390, 330, 220]

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
