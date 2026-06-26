from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

#MySQL配置
DB_CONFIG={
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "student_manage",
    "charset": "utf8mb4"
}
@app.route("/")
def index():
    return render_template("student.html")
@app.route("/student")
def student():
    return render_template("student.html")
@app.route("/source")
def source():
    return render_template("source.html")
@app.route("/teacher")
def teacher():
    return render_template("teacher.html")
@app.route("/score")
def score():
    return render_template("score.html")
@app.route("/teaching")
def teaching():
    return render_template("teaching.html")
#显示所有已有学生名单
@app.route('/student/getstudent',methods=['GET'])
def get_student():
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name,student_id,sex,class_name,phone FROM student")
        students = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":students})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
#查询某个学生的信息
@app.route('/student/selectstudent',methods=['GET'])
def select_student():
    try:
        student_id = request.args.get('student_id')
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="SELECT name,student_id,sex,class_name,phone FROM student WHERE student_id=%s"
        cursor.execute(sql,(student_id,))
        student = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":student})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
#添加学生的信息
@app.route('/student/addstudent', methods=['POST'])
def add_student():
    try:
        data = request.json
        name = data["name"]
        student_id = data["student_id"]
        sex = data["sex"]
        class_name = data["class_name"]
        phone = data["phone"]

        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "INSERT INTO student(name,student_id,sex,class_name,phone) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(sql, (name,student_id,sex, class_name, phone))
        db.commit()

        cursor.close()
        db.close()
        return jsonify({"code": 200, "msg": "添加成功！"})
    except Exception as e:
        return jsonify({"code": 500, "msg": "添加失败：" + str(e)})
#删除学生信息
@app.route('/student/deletestudent', methods=['POST'])
def delete_student():
    try:
        data = request.json
        student_id = data["student_id"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "DELETE FROM student WHERE student_id=%s"
        cursor.execute(sql,(student_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code":200,"msg":"删除成功"})
    except Exception as e:
        return jsonify({"code":500,"msg":"删除失败"+str(e)})
@app.route("/source/getsource",methods=['GET'])
def get_source():
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT source_id,source_name,source_hours,semester,type,credit FROM source")
        sources = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":sources})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route('/source/selectsource',methods=['GET'])
def select_source():
    try:
        source_id = request.args.get('source_id')
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="SELECT source_id,source_name,source_hours,semester,type,credit FROM source WHERE source_id=%s"
        cursor.execute(sql,(source_id,))
        source = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":source})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route('/source/addsource', methods=['POST'])
def add_source():
    try:
        data = request.json
        source_id = data["source_id"]
        source_name = data["source_name"]
        source_hours = data["source_hours"]
        semester = data["semester"]
        type = data["type"]
        credit = data["credit"]

        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "INSERT INTO source(source_id,source_name,source_hours,semester,type,credit) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (source_id,source_name,source_hours,semester,type,credit))
        db.commit()

        cursor.close()
        db.close()
        return jsonify({"code": 200, "msg": "添加成功！"})
    except Exception as e:
        return jsonify({"code": 500, "msg": "添加失败：" + str(e)})
@app.route("/source/deletesource",methods=['POST'])
def delete_source():
    try:
        data = request.json
        source_id = data["source_id"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "DELETE FROM source WHERE source_id=%s"
        cursor.execute(sql,(source_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code":200,"msg":"删除成功"})
    except Exception as e:
        return jsonify({"code":500,"msg":"删除失败"+str(e)})
@app.route("/teacher/getteacher",methods=['GET'])
def get_teacher():
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="""SELECT t.teacher_id,t.teacher_name,t.title,c.college_name,t.work_years,t.phone 
        FROM teacher t
        INNER JOIN college c ON t.college_id=c.college_id"""
        cursor.execute(sql)
        teachers = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":teachers})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route("/teacher/selectteacher",methods=['GET'])
def select_teacher():
    try:
        teacher_id = request.args.get('teacher_id')
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="""SELECT t.teacher_id,t.teacher_name,t.title,c.college_name,t.work_years,t.phone 
                FROM teacher t
                INNER JOIN college c ON t.college_id=c.college_id
                WHERE t.teacher_id=%s"""
        cursor.execute(sql,(teacher_id,))
        teacher = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":teacher})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route("/teacher/deleteteacher",methods=['POST'])
def delete_teacher():
    try:
        data = request.json
        teacher_id = data["teacher_id"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "DELETE FROM teacher WHERE teacher_id=%s"
        cursor.execute(sql,(teacher_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code":200,"msg":"删除成功"})
    except Exception as e:
        return jsonify({"code":500,"msg":"删除失败"+str(e)})
@app.route("/teacher/addteacher",methods=['POST'])
def add_teacher():
    try:
        data = request.json
        teacher_id = data["teacher_id"]
        teacher_name = data["teacher_name"]
        title = data["title"]
        college_id = data["college_id"]
        work_years = data["work_years"]
        phone = data["phone"]

        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "INSERT INTO teacher(teacher_id,teacher_name,title,college_id,work_years,phone) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (teacher_id,teacher_name,title,college_id,work_years,phone))
        db.commit()

        cursor.close()
        db.close()
        return jsonify({"code": 200, "msg": "添加成功！"})
    except Exception as e:
        return jsonify({"code": 500, "msg": "添加失败：" + str(e)})
@app.route("/score/getscore",methods=['GET'])
def get_score():
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="""SELECT s.name,s.student_id,c.source_name,r.score
        FROM score r
        INNER JOIN student s ON r.student_id=s.student_id
        INNER JOIN source c ON r.source_id=c.source_id"""
        cursor.execute(sql)
        scores = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":scores})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route("/score/selectscore",methods=['GET'])
def select_grade():
    try:
        student_id = request.args.get('student_id')
        source_id = request.args.get('source_id')
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="""SELECT s.name,s.student_id,c.source_name,r.score
            FROM score r
            INNER JOIN student s ON r.student_id=s.student_id
            INNER JOIN source c ON r.source_id=c.source_id
            WHERE r.student_id=%s and r.source_id=%s"""
        cursor.execute(sql,(student_id,source_id,))
        score = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":score})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route("/score/addscore",methods=['POST'])
def add_score():
    try:
        data = request.json
        student_id = data["student_id"]
        source_id = data["source_id"]
        score = data["score"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "INSERT INTO score(student_id,source_id,score) VALUES(%s,%s,%s)"
        cursor.execute(sql, (student_id,source_id,score))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code": 200, "msg": "添加成功！"})
    except Exception as e:
        return jsonify({"code": 500, "msg": "添加失败：" + str(e)})
@app.route("/score/deletescore",methods=['POST'])
def delete_score():
    try:
        data = request.json
        student_id = data["student_id"]
        source_id = data["source_id"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "DELETE FROM score WHERE student_id=%s and source_id=%s"
        cursor.execute(sql,(student_id,source_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code":200,"msg":"删除成功"})
    except Exception as e:
        return jsonify({"code":500,"msg":"删除失败"+str(e)})
@app.route("/teaching/getteaching",methods=['GET'])
def get_teaching():
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="""SELECT t.teacher_name,s.source_name,ti.location,ti.weekday,ti.class_time,ti.semester
        FROM teaching ti
        INNER JOIN teacher t ON ti.teacher_id=t.teacher_id
        INNER JOIN source s ON ti.source_id=s.source_id"""
        cursor.execute(sql)
        teachings = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":teachings})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route("/teaching/selectteaching",methods=['GET'])
def select_teaching():
    try:
        teacher_id = request.args.get('teacher_id')
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql="""SELECT t.teacher_name,s.source_name,ti.location,ti.weekday,ti.class_time,ti.semester
        FROM teaching ti
        INNER JOIN teacher t ON ti.teacher_id=t.teacher_id
        INNER JOIN source s ON ti.source_id=s.source_id
        WHERE ti.teacher_id=%s"""
        cursor.execute(sql,(teacher_id,))
        teaching = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({"code":200,"data":teaching})
    except Exception as e:
        return jsonify({"code":500,"msg":"查询失败"+str(e)})
@app.route("/teaching/addteaching",methods=['POST'])
def add_teaching():
    try:
        data = request.json
        teaching_id = data["teaching_id"]
        teacher_id = data["teacher_id"]
        source_id = data["source_id"]
        location = data["location"]
        weekday = data["weekday"]
        class_time = data["class_time"]
        semester = data["semester"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "INSERT INTO teaching(teaching_id,teacher_id,source_id,location,weekday,class_time,semester) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (teaching_id,teacher_id,source_id,location,weekday,class_time,semester))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code": 200, "msg": "添加成功！"})
    except Exception as e:
        return jsonify({"code": 500, "msg": "添加失败：" + str(e)})
@app.route("/teaching/deleteteaching",methods=['POST'])
def delete_teaching():
    try:
        data = request.json
        teacher_id = data["teacher_id"]
        source_id = data["source_id"]
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        sql = "DELETE FROM teaching WHERE teacher_id=%s and source_id=%s"
        cursor.execute(sql,(teacher_id,source_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"code":200,"msg":"删除成功"})
    except Exception as e:
        return jsonify({"code":500,"msg":"删除失败"+str(e)})
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
