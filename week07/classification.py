# -*- coding: utf-8 -*-
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', as_frame=False)

print(mnist.keys())   # data와 target만 사용

x, y = mnist.data, mnist.target
print(x)
print(x.shape)      # 28 x 28 개의 픽셀 특징을 가진 이미지 70,000개
print(y)
print(y,shape)

