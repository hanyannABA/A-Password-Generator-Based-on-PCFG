# A Password Generator Based on PCFG

> 基于 PCFG（Probabilistic Context-Free Grammar，概率上下文无关文法）的密码结构分析、概率估计与密码样本生成实验项目。

## 项目简介

本项目通过统计真实密码数据中的结构模式，构建一个简单的 PCFG 密码模型。模型会把密码拆解为三类连续片段：

- `L`：字母片段（Letters）
- `D`：数字片段（Digits）
- `S`：符号片段（Symbols）

例如，密码 `abc123!` 可以拆分为：

```text
L3("abc") + D3("123") + S1("!")
```

项目基于训练得到的结构概率和片段概率，可以完成以下任务：

1. 统计并查看常见密码结构与常见片段；
2. 按概率模型随机生成密码样本；
3. 估计指定密码在模型下的出现概率。

> **重要提醒**：本项目仅用于课程实验、密码安全研究和弱口令模式分析。生成结果不应作为真实账户密码使用。

## 仓库内容

| 文件 | 说明 |
| --- | --- |
| `10-million-password-list-top-1000000.txt` | 常见密码数据集，包含约 100 万条密码样本。 |
| `patterns_possibilities.json` | 密码整体结构模式的概率分布，例如 `L8D0S0`、`L6D2S0`。 |
| `possibilities_top5.json` | 从概率文件中整理出的 Top 5 常见结构与常见片段示例。 |
| `password_given.txt` | 待计算概率的示例密码输入文件。 |
| `generated_passwords.json` | 已生成的密码样本输出示例。 |
| `generate_password_prob.json` | 已计算的密码概率输出示例。 |
| `generate_password.py` | 根据 PCFG 概率模型随机生成密码。 |
| `generate.py` | 读取指定密码并计算其模型概率。 |
| `list.py` | 提取并保存常见结构、常见片段的 Top 5 结果。 |
| `LICENSE` | MIT 开源许可证。 |

## 环境要求

- Python 3.8 或更高版本；
- 无需安装第三方依赖，脚本仅使用 Python 标准库：
  - `json`
  - `random`
  - `re`
  - `argparse`

检查 Python 版本：

```bash
python --version
```

## 数据与路径说明

当前脚本中的输入、输出路径写成了 Windows 风格的相对路径，例如：

```python
train\patterns_possibilities.json
train\res_possibilities.json
train\password_given.txt
```

因此，在直接运行脚本前，请注意以下两点：

1. 脚本默认希望相关数据文件位于 `train` 目录下；
2. 如果你在 Linux/macOS 环境中运行，建议先把脚本中的 `train\xxx.json` 改为 `train/xxx.json`，或统一改为当前仓库根目录下的文件路径。

此外，`generate_password.py`、`generate.py` 和 `list.py` 都依赖 `res_possibilities.json` 片段概率文件。如果该文件不存在，需要先准备或重新生成该文件后再运行相关脚本。

## 快速开始

### 1. 查看常见结构与片段

运行：

```bash
python list.py
```

该脚本会读取结构概率和片段概率，并生成：

```text
possibilities_top5.json
```

输出内容包括：

- 最常见的密码结构；
- `L4` 四位字母片段的常见值；
- `D3` 三位数字片段的常见值；
- `S2` 两位符号片段的常见值。

### 2. 生成密码样本

运行：

```bash
python generate_password.py
```

默认生成 20 个密码，并写入：

```text
generated_passwords.json
```

如需修改生成数量，可以调整 `generate_password.py` 中的常量：

```python
__COUNTER__ = 20
```

### 3. 计算指定密码的概率

先在 `password_given.txt` 中按行写入待分析密码，例如：

```text
abc123
pass66!
```

然后运行：

```bash
python generate.py
```

脚本会输出每个密码对应的模型概率，并写入：

```text
generate_password_prob.json
```

## PCFG 建模思路

### 1. 密码结构抽象

密码会被抽象为由 `L`、`D`、`S` 组成的结构模式。例如：

| 密码 | 结构示例 | 含义 |
| --- | --- | --- |
| `password` | `L8D0S0` | 8 个字母，无数字和符号。 |
| `abc123` | `L3D3S0` | 3 个字母 + 3 个数字。 |
| `a1!` | `L1D1S1` | 1 个字母 + 1 个数字 + 1 个符号。 |

### 2. 片段概率统计

除整体结构外，模型还会统计不同长度片段的出现概率。例如：

- `L4`：长度为 4 的字母片段，如 `love`、`alex`；
- `D3`：长度为 3 的数字片段，如 `123`、`777`；
- `S2`：长度为 2 的符号片段，如 `!!`、`@@`。

### 3. 密码生成过程

生成一个密码时，程序会：

1. 按结构概率随机选择一个结构模式；
2. 将结构模式拆成若干片段，例如 `L4D3S1`；
3. 按对应片段概率随机选择具体片段；
4. 拼接所有片段，得到最终密码。

### 4. 密码概率计算

对于一个给定密码，程序会计算：

```text
P(password) = P(pattern) × P(segment_1) × P(segment_2) × ... × P(segment_n)
```

也就是说，密码概率由整体结构概率和每个片段的条件概率共同决定。

## 示例结果

`possibilities_top5.json` 中记录的高频结构示例包括：

```json
{
  "patterns_possibilities": [
    ["L8D0S0", 0.10721521443042886],
    ["L6D0S0", 0.10346420692841386],
    ["L7D0S0", 0.07174714349428699]
  ]
}
```

这说明在训练数据中，纯字母密码以及固定长度字母密码是非常常见的弱口令模式。

## 注意事项

- 训练数据中包含大量真实世界常见弱口令，请仅在合法、合规的安全研究或教学环境中使用。
- 生成的密码反映的是常见弱口令分布，不代表高强度随机密码。
- 当前仓库主要保留了模型使用、分析和示例输出文件；如果需要完整复现实验训练过程，需要补充训练脚本或重新生成片段概率文件。
- 如果脚本运行时报 `FileNotFoundError`，请优先检查数据文件路径是否与脚本中的路径一致。

## 许可证

本项目基于 MIT License 开源，详见 [`LICENSE`](LICENSE)。
