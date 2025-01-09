# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.0.6](https://github.com/yszaryszar/xy-ai/compare/v0.0.4...v0.0.6) (2025-01-09)


### Bug Fixes

* :bug: 修正了 Dockerfile 中的 FastAPI 启动路径，并更新了 nginx 配置以支持根域名和子域名的 HTTPS 访问 ([91afc92](https://github.com/yszaryszar/xy-ai/commit/91afc92cb33683ce5996f78c857332924114c53f))
* :bug: 修正了 Nginx 配置文件，未找到文件时返回 404 错误 ([b501c12](https://github.com/yszaryszar/xy-ai/commit/b501c12dba8676f3db801047287320af7576ff77))
* :bug: 移除冗余的子域名配置以简化 Nginx 配置文件 ([e3a0220](https://github.com/yszaryszar/xy-ai/commit/e3a0220ebc33f016f28308bde573e7b7be3317b7))

### [0.0.5](https://github.com/yszaryszar/xy-ai/compare/v0.0.3...v0.0.5) (2025-01-08)

### [0.0.4](https://github.com/yszaryszar/xy-ai/compare/v0.0.3...v0.0.4) (2025-01-08)

### [0.0.3](https://github.com/yszaryszar/xy-ai/compare/v0.0.2...v0.0.3) (2025-01-08)

### [0.0.2](https://github.com/yszaryszar/xy-ai/compare/v0.0.1...v0.0.2) (2025-01-08)


### Features

* :sparkles: 添加了自动部署到服务器的 GitHub Actions 工作流，以及后端和前端的 Docker 支持，并更新了前端构建流程和依赖项。这一改进简化了部署过程，增强了项目的可移植性和持续集成能力 ([caae021](https://github.com/yszaryszar/xy-ai/commit/caae0214fdbc7bf283386db36a54b6ef8eb6588f))

### [0.0.1](https://github.com/yszaryszar/xy-ai/compare/v0.0.0...v0.0.1) (2025-01-06)

## 0.0.0 (2025-01-06)


### Features

* :sparkles: 添加了项目配置文件和基本的项目结构，包括.gitignore文件、README.md文档和后端FastAPI应用的初始设置，为项目开发规范和环境隔离提供了基础 ([49a96e9](https://github.com/yszaryszar/xy-ai/commit/49a96e9ce53fbeb2feba9f778f3331fdc6d6fcbf))
