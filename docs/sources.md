# 来源、编辑原则与核验说明

[← 首页](../README.md)

## 官方事实的来源

查阅日期：**2026-10-30**。仅下列关于培养结构的陈述来自官方页面；自学安排与书目是编辑判断。

| 来源 | 本仓库据此采用的事实 |
|---|---|
| [Core Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements/core-requirements) | Preparations、四类 Breadth、Cross-Area、Advanced Small Seminar、Capstone 及展示要求；页面标注 G4.3 |
| [Concentrations](https://symsys.stanford.edu/undergraduates/concentrations) | 方向名称；具体选课要求需进入各方向页面核对 |
| [Master's Program](https://symsys.stanford.edu/graduates/masters-program) | 研究型硕士定位、语言/信息/智能、跨至少两个相关学科 |

Core 与 Master's Program 页面在整理时成功获取正文；方向名称亦见官网本科导航。本仓库未逐一重建每个方向、每种入学年份的学位审查规则，也不把硕士官网简介扩展解读为博士培养方案。

## 非官方部分

- 主线与选读的选择、阅读顺序、先修判断。
- 本科/研究生/博士层次划分；实际课程难度因学校与学生背景而异。
- 学习时长、能力标准、项目方案及博士专题。
- 一本书在清单中不代表 Stanford 官方曾将其列为指定教材。

## 资源选择原则

1. 优先作者、大学、出版社、原始论文与正规开放出版平台。
2. 付费书保留书介或图书目录检索入口，不提供盗版下载。
3. “全文”表示合法可读入口，不等于 CC 授权或可重新上传。
4. 课程主页可能按学期更新；草稿与预印本引用须注明版本。
5. 经典文献用于理解问题史；当前研究仍需补近年论文与反例。
6. 对同一问题保留竞争立场，不把某一研究纲领当作无争议共识。

## 链接检查

提供 `scripts/check_links.py`，只依赖 Python 3 与 curl：

```bash
python scripts/check_links.py --local-only
python scripts/check_links.py > link-check.tsv
```

首次 HTTP 探测后修正了一处 HCI 资源地址和 DOI 中括号的 URL 编码问题。本地文件链接在交付前单独检查。

**已知限制：**部分站点（包括 WorldCat、出版社、部分 DOI、Harvard、Columbia 等）出现超时、403 或传输错误；不能据此判定资源不存在，也不能声称全站链接已通过验证。HTTP 200 也不证明标题、版次或正文完整正确，自动检测不替代内容审查。

若遇访问问题：优先按作者与完整标题在图书馆、出版社、作者主页或正规开放仓储检索；不要绕过付费墙或使用侵权镜像。提 Issue 时请附链接、错误与查阅日期，不上传受限全文。

## 维护范围

本指南偏向心智、语言与计算的共同方法基础，较深入覆盖逻辑、AI、认知、语言、神经与社会技术问题。生物医学、计算机音乐等专门方向仅作导航，尚不提供完整领域训练。
