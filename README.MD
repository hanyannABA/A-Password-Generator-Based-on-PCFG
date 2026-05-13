# 密码生成与分析项目 (PCFG-based Password Generation and Analysis)

## 项目概述

本项目基于概率上下文无关文法 (PCFG) 模型，实现密码的生成和概率分析。通过分析大量真实密码数据，学习密码的结构模式和字符段概率分布，从而生成类似真实密码的样本，或计算给定密码的出现概率。

## 文件说明

### 数据文件
- `10-million-password-list-top-1000000.txt`: 包含100万个常见密码的训练数据集，用于学习密码模式。
- `password_given.txt`: 示例密码文件，用于测试概率计算。
- `patterns_possibilities.json`: 存储密码结构模式的概率分布（例如L8D0S0表示8个字母的纯字母密码）。
- `res_possibilities.json`: 存储各类型字符段的概率分布（例如L4段中各4字母组合的频率）。
- `possibilities_top5.json`: 提取的前5个最常见模式和字符段。
- `generated_passwords.json`: 使用模型生成的示例密码。
- `generate_password_prob.json`: （可能为生成概率相关数据）

### 脚本文件
- `train.py`: 训练脚本。从密码列表中提取结构模式和字符段，计算概率分布并保存到JSON文件中。
- `generate_password.py`: 密码生成脚本。基于学习的概率模型随机生成新密码。
- `generate.py`: 概率计算脚本。计算给定密码的出现概率。
- `list.py`: 数据分析脚本。提取并保存最常见的模式和字符段。

### 文档
- `README.MD`: 本说明文件。
- `开发报告.docx`: 项目开发报告。

## 运行环境

- Python 3.x
- 依赖库：json, random, re, argparse

## 使用方法

### 1. 训练模型
运行训练脚本以学习密码模式：
```bash
python train.py
```
这将生成 `patterns_possibilities.json` 和 `res_possibilities.json` 文件。

### 2. 生成密码
运行密码生成脚本：
```bash
python generate_password.py
```
默认生成20个密码，可修改脚本中的 `__COUNTER__` 变量调整数量。结果保存到 `generated_passwords.json`。

### 3. 计算密码概率
运行概率计算脚本：
```bash
python generate.py
```
这将读取 `password_given.txt` 中的密码，计算每个密码的概率并打印结果。

### 4. 数据分析
运行分析脚本：
```bash
python list.py
```
这将提取前5个最常见的模式和字符段，保存到 `possibilities_top5.json`。

## 算法原理

### PCFG模型
- **结构模式**: 将密码分解为字母(L)、数字(D)、符号(S)的组合，例如 `L3D2S1` 表示3个字母+2个数字+1个符号。
- **字符段**: 将连续相同类型的字符作为一个段，例如 "abc123!" 分解为 L3("abc") + D3("123") + S1("!")。
- **概率计算**: 基于训练数据计算各模式的出现频率和各字符段的条件概率。

### 密码生成
1. 根据模式概率随机选择一个结构模式。
2. 对每个段，根据段类型概率随机选择对应的字符段。
3. 拼接生成完整密码。

### 概率分析
对于给定密码，计算其结构模式概率乘以各字符段概率的积。

## 注意事项

- 训练数据较大（100万个密码），训练过程可能需要一些时间。
- 生成的密码仅用于研究目的，请勿用于实际安全场景。
- 所有路径在脚本中硬编码为相对路径 "train\\"，请确保在正确目录下运行。

## 实验目的

本项目用于程序安全检测技术实验6，演示如何使用机器学习方法分析和生成密码模式，以了解密码安全性和常见弱点。