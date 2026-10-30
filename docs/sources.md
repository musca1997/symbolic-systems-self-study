# 来源与维护

[← 首页](../README.md)

## 培养结构的出处

查阅日期：**2026-10-30**。

本指南独立编写：本科结构参考 Stanford Symbolic Systems 官网，书目、学习安排和硕博专题由编者整理。

| 来源 | 参考内容 |
|---|---|
| [Core Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements/core-requirements) | Preparations、四类 Breadth、Cross-Area、Advanced Small Seminar、Capstone 与展示要求；页面版本为 G4.3 |
| [Concentrations](https://symsys.stanford.edu/undergraduates/concentrations) | 方向名称与分类；具体选课规则见各方向页面 |
| [Master's Program](https://symsys.stanford.edu/graduates/masters-program) | 研究型硕士定位，以及语言、信息、智能和跨学科研究主题 |

正式选课与学位规划请查阅对应年份的 Stanford Bulletin。博士部分按相关学科的共同研究问题设计，适合专题阅读与读书会使用。

## 选书原则

1. 优先作者、大学、出版社、原始论文与开放出版平台。
2. 每个模块设置主线与进阶，说明先修、阅读重点与建议产物。
3. 付费书提供书介或图书目录入口，方便购买与图书馆借阅。
4. 开放资源标注全文、课程或预印本，引用时记录版本。
5. 经典与近期研究结合阅读，同时关注竞争解释、批评与负结果。

## 链接维护

仓库提供 `scripts/check_links.py`，依赖 Python 3 与 curl：

```bash
python scripts/check_links.py --local-only
python scripts/check_links.py > link-check.tsv
```

首轮检查修正了 HCI 资源地址与一处 DOI 编码，本地文件链接检查通过。部分外链遇到超时、403 或传输错误，主要涉及 WorldCat、出版社、部分 DOI 和大学网站；这些链接留待后续复查。

访问遇到问题时，可按作者与完整标题到图书馆、出版社或作者主页查找。欢迎提交 Issue，附上链接、错误信息和查阅日期。

## 后续扩充

当前重点是逻辑、AI、认知、语言、神经科学与社会技术研究。生物医学、计算机音乐等方向已列入导航，欢迎补充专业书目与课程。

## 授权

原创文字采用 [CC BY 4.0](../LICENSE)；外链书籍、论文、课程与数据遵循各自的版权和使用条款。
