from soupsieve import select
from sqlalchemy import create_engine
import random
import names
import string
import datetime

db = create_engine('postgresql+psycopg2://student:admin@localhost/azure')

##########INSERT##########
def insert_user(uid,emplnum,cdate,uname,passwd,lvl, active='1'):
    insert_str='INSERT INTO "Users" ("User ID","Employer Number","Creation Date","Username","Password","Level", "Active")'+" VALUES ("+uid+","+emplnum+",'"+cdate+"','"+uname+"','"+passwd+"',"+lvl+",'"+active+"')"
    db.execute(insert_str)

def insert_course(cid,cname,pid,dur,cdate,tags,photo, active='1'):
    insert_str='INSERT INTO "Courses" ("Course ID","Course Name","Platform ID","Duration","Creation Date","Tags","Photo", "Active")'+" VALUES ("+cid+",'"+cname+"',"+pid+","+dur+",'"+cdate+"','"+tags+"','"+photo+"','"+active+"')"
    db.execute(insert_str)

def insert_platform(pid,pname,path, active='1'):
    insert_str='INSERT INTO "Platforms" ("Platform ID","Platform Name","Hyperlink Path", "Active")'+" VALUES ("+pid+",'"+pname+"','"+path+"','"+active+"')"
    db.execute(insert_str)

def insert_review(uid,cid,feedback,ld,rank, active='1'):
    insert_str='INSERT INTO "Reviews" ("User ID","Course ID","Feedback", "Like/Dislike", "Ranking Score (out of 5)", "Active")'+" VALUES ("+uid+","+cid+",'"+feedback+"',"+ld+","+rank+",'"+active+"')"
    db.execute(insert_str)

def insert_photo(cid,pid,path, active='1'):
    insert_str='INSERT INTO "Photos" ("Course ID","Platform ID","Image Object", "Active")'+" VALUES ("+cid+","+pid+",'"+path+"','"+active+"')"
    db.execute(insert_str)

def insert_certification(certid,uid,cid,dur,date, active='1'):
    insert_str='INSERT INTO "Certifications" ("Certification ID","User ID","Course ID", "Completion Duration", "Completion Date", "Active")'+" VALUES ("+certid+","+uid+","+cid+","+dur+",'"+date+"','"+active+"')"
    db.execute(insert_str)

def insert_training(tid,uid,cid,status,completion,start,finish,lastupd, active='1'):
    insert_str='INSERT INTO "Ongoing Trainings" ("Training ID","User ID","Course ID", "Status", "Completion Percentage", "Start Date", "Finish Date", "Last Updated", "Active")'+" VALUES ("+tid+","+uid+","+cid+",'"+status+"',"+completion+",'"+start+"',"+finish+","+lastupd+",'"+active+"')"
    db.execute(insert_str)

##########GENERATE RANDOM##########
def random_date(start_date= datetime.date(2000, 1, 1),end_date = datetime.date(2022, 7, 27)):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    rnd = start_date + datetime.timedelta(days=random_number_of_days)
    return rnd

def generate_user(n=1):
    for i in range(1,n+1):
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
        boss="Null" if random.randint(0,10)==0 else str(random.randint(1,n))
        lvl="Null" if random.randint(0,10)==0 else str(random.randint(1,5))
        insert_user(str(i),boss,str(random_date()),names.get_full_name(),password,lvl)

def generate_platform(n=1):
    for i in range(1,round(n/2)):
        platform = ''.join(random.choice(string.ascii_letters) for i in range(6))
        link="" if random.randint(0,10)==0 else 'https://www.'+platform+"/"+str(i)+".com"
        insert_platform(str(i),platform,link)

def generate_course(n=1):
    for i in range(1,n+1):
        course = ''.join(random.choice(string.ascii_letters) for i in range(6))
        duration="Null" if random.randint(0,10)==0 else str(random.randint(60,180))
        tags="" if random.randint(0,10)==0 else "tags"
        photo="" if random.randint(0,10)==0 else "photo"
        platform=str(random.randint(1,round(n/2)+100))
        insert_course(str(i),course,platform,duration,str(random_date()),tags,photo)

def generate_review(n=1):
    for i in range(1,round(n/2)):
        feedback ="" if random.randint(0,10)==0 else ''.join(random.choice(string.ascii_letters) for i in range(120))
        rating=str(random.randint(1,5)) if random.randint(0,10)!=0 or feedback=="" else "Null" 
        liked= ("'1'" if int(rating)>2 else "'0'") if rating!="Null" else "NULL"
        insert_review(str(random.randint(1,n)),str(random.randint(1,n)),feedback,liked,rating)

def generate_photo(n=1):
    for i in range(0,round(n/2)):
        path = ''.join(random.choice(string.ascii_letters) for i in range(10))
        course="Null" if random.randint(0,10)==0 else random.randint(1,n)
        insert_photo(str(course),str(random.randint(1,n)) if course=="Null" else "Null",path+".png")

def generate_certification():
        completed = db.execute('SELECT "User ID", "Course ID", "Finish Date" FROM "Ongoing Trainings" WHERE "Completion Percentage"=100') 
        i=1
        for r in completed: 
            insert_certification(str(i),str(r[0]),str(r[1]),str(random.randint(60,240)),str(r[2])) 
            i+=1

def generate_training(n=1):
    for i in range(1,n+1):
        percentage=100 if random.randint(0,1)==0 else random.randint(0,100)
        status = "Ongoing" if percentage<100 else "Completed"

        uid=str(random.randint(1,n))
        cid=str(random.randint(1,n))
        udate=0
        cdate=0

        res = db.execute('SELECT "Creation Date" FROM "Users" WHERE "User ID"='+str(uid))
        for r in res:
            udate=r[0]
        res = db.execute('SELECT "Creation Date" FROM "Courses" WHERE "Course ID"='+str(cid))
        for r in res:
            cdate=r[0]

        startdate=random_date(start_date=udate if udate>=cdate else cdate)
        enddate="'"+str(random_date(start_date=startdate,end_date=datetime.date(startdate.year+1,12,31)))+"'" if percentage==100 else "Null" 
        lastupdated=enddate if status=="Completed" else "'"+str(random_date(start_date=startdate,end_date=datetime.date(startdate.year+1,12,31)))+"'"
        insert_training(str(i),uid,str(random.randint(1,n)),status,str(percentage),str(startdate),str(enddate),str(lastupdated))


def generate_all(n):
    generate_user(n)
    generate_platform(n)
    generate_course(n)
    generate_review(n)
    generate_photo(n)
    generate_training(n)
    generate_certification()

##########DELETE##########

def delete_record(table, idColumn, id):
    db.execute('DELETE FROM "'+table+'" WHERE "'+idColumn+'"='+str(id))  

def delete_all_records(table, idColumn):
    res = db.execute('SELECT "'+idColumn+'" FROM "'+table+'"')
    for r in res:
        if str(r[0])!="None":
            db.execute('DELETE FROM "'+table+'" WHERE "'+idColumn+'"='+str(r[0]))  

def purge():
    delete_all_records("Courses", "Course ID")
    delete_all_records("Users", "User ID")
    delete_all_records("Platforms", "Platform ID")
    delete_all_records("Photos", "Course ID")
    delete_all_records("Photos", "Platform ID")
    delete_all_records("Ongoing Trainings", "Course ID")
    delete_all_records("Certifications", "Course ID")

##########ACTIVATE/DEACTIVATE##########

def deactivate(table, idColumn, id):
    db.execute('UPDATE "'+table+'" SET "Active"='+"'0'"+' WHERE "'+idColumn+'"='+str(id))

def activate(table, idColumn, id):
    db.execute('UPDATE "'+table+'" SET "Active"='+"'1'"+' WHERE "'+idColumn+'"='+str(id))

##########UPDATE##########

def update_record(table,updColumn, newValue, where, oldValue):
    db.execute('UPDATE "'+table+'" SET "'+updColumn+'"='+"'"+newValue+"'"+' WHERE "'+where+'"='+str(oldValue))

##########SELECT##########

def select_table(columns, table, whereCol="", filter=""):
    if whereCol=="":
        result_set = db.execute('SELECT '+columns+' FROM "'+table+'"') 
        for r in result_set:  
            print(r)
    else:
        result_set = db.execute('SELECT '+columns+' FROM "'+table+'" WHERE "'+whereCol+'"='+str(filter)) 
        for r in result_set:  
            print(r)
            print()
