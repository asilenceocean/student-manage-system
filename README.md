# 学生信息管理系统

数据库系统概论课程设计项目 —— 学生信息管理系统的数据库设计与前端实现。

## 技术栈

| 层 | 技术 |
|---|------|
| 前端 | HTML5 + CSS3 + JavaScript (ES6+) |
| 后端 | Python Flask 3.1 |
| 数据库 | MySQL 8.0 (InnoDB) |

## 功能模块

- **学生管理** —— 学生信息的增删查
- **课程管理** —— 课程信息的增删查
- **教师管理** —— 教师信息的增删查（关联学院表）
- **成绩管理** —— 选课成绩的增删查（联合主键，三表联查）
- **授课管理** —— 授课安排的增删查（多对多关系）

## 数据库设计

6 张数据表（满足 3NF）：

| 表 | 主键 | 说明 |
|----|------|------|
| college | college_id | 学院字典表 |
| student | student_id | 学生信息 |
| source | source_id | 课程信息 |
| teacher | teacher_id | 教师信息（外键→college） |
| score | (student_id, source_id) | 成绩（联合主键，双外键） |
| teaching | teaching_id | 授课安排（双外键） |

## 运行方式

```
# 1. 导入数据库
# 在 MySQL 中执行 附录B 的建表脚本

# 2. 修改 app.py 中的数据库密码
# DB_CONFIG = { "password": "你的密码", ... }

# 3. 安装依赖并启动
pip install -r requirements.txt
python app.py

# 4. 浏览器打开
http://127.0.0.1:5000
```

## 项目结构

```
├── app.py              # Flask 主程序
├── requirements.txt    # Python 依赖
├── templates/          # 5 个 HTML 页面
│   ├── student.html
│   ├── source.html
│   ├── teacher.html
│   ├── score.html
│   └── teaching.html
└── static/
    └── css/            # 5 个 CSS 样式文件
```
