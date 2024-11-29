# NetSecChallenge
NetSecChallenge 是一个基于 Flask 构建的网络安全挑战应用，旨在通过设计与网络安全相关的题库，帮助学习者在实际场景中巩固和提升网络安全知识。该应用允许用户进行在线答题，系统根据题库生成随机题目，用户答题后系统会提供反馈和成绩。
NetSecChallenge 项目说明

提供一个在线网络安全测试平台，包含选择题和判断题等多种类型的网络安全相关题目。
通过 Flask Web 框架实现用户交互界面，前端界面简洁明了，后端逻辑稳定高效。
支持多种文件类型的题库导入与管理（如 Excel 文件），使得题库内容可以方便地更新和扩展。

技术栈
后端框架：Flask
前端技术：HTML, CSS, JavaScript
数据存储：题库数据存储在 Excel 文件中（.xlsx 格式），通过 Pandas 进行读取和处理
依赖库：
Flask：Web 框架，提供应用的路由和视图处理功能。
Pandas：用于读取 Excel 文件，并从题库文件中动态加载题目。
openpyxl：Pandas 的 Excel 读取支持库。
Jinja2：Flask 使用的模板引擎，负责动态渲染 HTML 页面。
Werkzeug：Flask 的 WSGI 工具集，提供请求和响应处理功能。
项目结构
NetSecChallenge/
│
├── quiz_app.py             # Flask 应用的入口文件
├── requirements.txt        # Python 项目的依赖文件
├── static/                 # 存放静态文件（如 CSS, JS, 图片）
│   └── ...
├── templates/              # 存放模板文件（如 HTML）
│   └── ...
├── data/                   # 存放题库数据文件（如 Excel）
│   └── 题库1.xlsx
└── venv/                   # 虚拟环境（如果存在）
主要文件说明
quiz_app.py：Flask 应用的主文件，包含应用的路由和视图处理逻辑。
templates/：存放 HTML 模板文件，Flask 使用 Jinja2 引擎渲染。
static/：存放 CSS、JS 文件以及其他静态资源。
data/：存放 Excel 格式的题库文件，系统会从这些文件中读取题目并生成挑战。
功能说明
1. 用户界面
用户通过 Web 浏览器访问该应用，主要界面包括：

首页：提供简单的介绍和开始答题按钮。
答题页面：用户可以选择开始答题，系统会从题库中随机生成题目，用户完成答题后提交答案。
结果页面：显示答题结果、正确答案以及用户的得分。
2. 题库管理
题库数据存储在 Excel 文件（.xlsx）中，包含题目、选项、正确答案等信息。
使用 Pandas 和 openpyxl 读取和处理 Excel 文件，动态加载题目并提供给用户答题。
3. 后端功能
题目随机生成：系统从 Excel 文件中读取所有题目，并从中随机抽取一定数量的题目作为当前挑战。
成绩统计：系统会根据用户的答题情况，自动计算得分并显示正确答案。
数据管理：通过 Pandas 库提供的数据框架，方便管理和更新题库内容。
图片演示：
![6686d4ed3a1a18bcd10d9c2dae49fa3](https://github.com/user-attachments/assets/dcb66a28-9cbb-406f-a94b-895bc8bb94c9)
![8e8bcfd7d1123658fd949d0f59725cb](https://github.com/user-attachments/assets/bf9a9519-241d-4d1b-a3ac-06ee0c84f4a1)
![89be24bc51346122b647d92bb9eb7ca](https://github.com/user-attachments/assets/ce7360c2-4549-49ed-ad75-006122970eb6)
![Uploading cbb1355c1e29f5c61ed39a783a89054.png…]()

安装与运行
环境要求
Python 3.x
操作系统：Windows / Linux / macOS
依赖：Flask, Pandas, openpyxl
安装步骤
克隆或下载项目： 将 NetSecChallenge 项目文件夹下载到本地。

创建虚拟环境（推荐）： 在项目目录下，使用以下命令创建虚拟环境：
python -m venv venv

激活虚拟环境：
Windows：
venv\Scripts\activate

Linux/macOS：
source venv/bin/activate
安装项目依赖： 在虚拟环境激活后，运行以下命令安装依赖：

pip install -r requirements.txt
运行 Flask 应用： 在项目根目录下运行 Flask 应用：

python quiz_app.py
访问应用： 打开浏览器，访问 http://127.0.0.1:5000，开始进行网络安全挑战。

项目部署
1. 使用 Docker 部署
可以使用 Docker 容器化该应用，方便跨平台部署。

安装 Docker：确保已经安装 Docker。

构建 Docker 镜像：

docker build -t netsecchallenge .
运行 Docker 容器：

docker run -p 5000:5000 netsecchallenge
通过 http://127.0.0.1:5000 访问 Flask 应用。

2. 使用 Heroku 部署
在 GitHub 上将该项目上传。

创建一个 Procfile 文件：

web: python quiz_app.py
使用 Heroku CLI 部署：

heroku create
git push heroku master
heroku open
通过 Heroku 部署后，你可以将应用发布到云端，其他用户也能通过 Heroku 提供的 URL 访问应用。

未来工作与扩展
增加用户认证功能：支持用户登录、注册以及成绩历史记录。
题库管理：开发后台管理界面，用于管理员管理题库（添加、删除、编辑题目）。
前端优化：使用现代前端框架（如 React 或 Vue）优化用户界面体验。
多语言支持：支持多种语言的界面和题库。
结语
NetSecChallenge 是一个有趣且具有教育意义的项目，旨在帮助学习者通过互动式挑战加深对网络安全的理解。希望该项目能够为你提供实际操作经验，并帮助你在网络安全领域不断提升技能。
