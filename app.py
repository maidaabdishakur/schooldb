from flask import Flask,render_template,redirect,request
from supabase import create_client, Client
url='https://iwyrpnruzuenqfeibrwj.supabase.co'
key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml3eXJwbnJ1enVlbnFmZWlicndqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ5MDk2ODQsImV4cCI6MjA3MDQ4NTY4NH0.K-YQ5B5nAtczQd2PEgEPAB-lnhwZWM7u7KyvSbAItUY'
supabase: Client = create_client(url, key)
app = Flask(__name__)
@app.route('/')
def index():
data = supabase.table('students').select('*').execute()
students = data.data
return render_template("index.html", students=students)
@app.route('/add_student', methods=['POST'])
def add_student():
   name = request.form['name']
   faculty = request.form['faculty']
supabase.table('students').insert({
'name': name,
'faculty': faculty
}).execute()
return redirect('/')
@app.route('/delete_student/<int:id>')
def delete_student(id):
 supabase.table('students').delete().eq('id', id).execute()
return redirect('/')
@app.route('/edit_student/<int:id>',methods=['GET'])
def edit_student(id):
  student =supabase.table('students').select('*').eq('id',id).single().execute().data
return render_template("edit.html", student=student)
@app.route('/update_student/<int:id>', methods=['POST'])
def update_student(id):
 name = request.form['name']
 faculty = request.form['faculty']
supabase.table('students').update({
'name': name,
'faculty': faculty
}).eq('id', id).execute()
return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)