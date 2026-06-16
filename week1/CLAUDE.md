# CLAUDE.md

本文件为在代码仓库中工作时向 Claude Code (claude.ai/code) 提供指导。

## 项目概述

这是斯坦福大学 2025 年秋季 CS146S：现代软件开发课程作业仓库。主要内容是通过本地 LLM（使用 [Ollama](https://ollama.com/)）练习 LLM 提示词工程技巧。

## 环境配置

```bash
# 安装依赖
poetry install --no-interaction

# 下载所需模型（一次性操作）
ollama run mistral-nemo:12b
ollama run llama3.1:8b

# 启动 Ollama 服务
ollama serve
```

## 运行测试

每周的技术练习都是独立的 Python 脚本，直接运行即可：

```bash
python week1/k_shot_prompting.py
python week1/chain_of_thought.py
python week1/tool_calling.py
python week1/self_consistency_prompting.py
python week1/rag.py
python week1/reflexion.py
```

## 架构说明

- **week1/**：六个提示词技术练习 — 每个文件都有 `TODO` 部分需要填写提示词。只需修改提示词字符串（`YOUR_SYSTEM_PROMPT`、`YOUR_REFLEXION_PROMPT` 等）和 `YOUR_CONTEXT_PROVIDER` 函数。
- **week1/data/**：包含辅助文件，如 RAG 练习中使用的 `api_docs.txt`。
- **week1/chromadb/**：RAG 练习的持久化向量存储目录（运行 `pe-rag-cn.ipynb` 时生成）。
- **week1/pe-rag.ipynb、pe-rag-cn.ipynb**：RAG 练习的 Notebook 版本（中英两版，中文版经过运行验证）。是逐步教程而非脚本：依次演示安装依赖 → 构建向量库 → 嵌入与检索 → 生成回答。数据源为 `data/ml-potw-10232023.csv`。
- 仓库覆盖 week1–week8，每周结构类似；此 CLAUDE.md 仅针对 week1，每周可能需要独立维护。

## 主要模型

- `mistral-nemo:12b` — 用于 k-shot 提示
- `llama3.1:8b` — 用于链式思考、工具调用、自洽性、RAG 和自我反思

## 环境变量

环境变量通过 `python-dotenv` 从 `.env` 文件加载。由于 Ollama 本地运行，无需 API Key。