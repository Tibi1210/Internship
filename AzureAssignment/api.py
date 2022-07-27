from sqlalchemy import create_engine
import random
import names
import string
import datetime

db = create_engine('postgresql+psycopg2://student:admin@localhost/azure')

##########INSERT##########
def insert_user(uid,emplnum,cdate,uname,passwd,lvl):
    insert_str='INSERT INTO "Users" ("User ID","Employer Number","Creation Date","Username","Password","Level")'+" VALUES ("+uid+","+emplnum+",'"+cdate+"','"+uname+"','"+passwd+"',"+lvl+")"
    db.execute(insert_str)

def insert_course(cid,cname,pid,dur,cdate,tags,photo):
    insert_str='INSERT INTO "Courses" ("Course ID","Course Name","Platform ID","Duration","Creation Date","Tags","Photo")'+" VALUES ("+cid+",'"+cname+"',"+pid+","+dur+",'"+cdate+"','"+tags+"','"+photo+"')"
    db.execute(insert_str)

def insert_platform(pid,pname,path):
    insert_str='INSERT INTO "Platforms" ("Platform ID","Platform Name","Hyperlink Path")'+" VALUES ("+pid+",'"+pname+"','"+path+"')"
    db.execute(insert_str)

def insert_review(uid,cid,feedback,ld,rank):
    insert_str='INSERT INTO "Reviews" ("User ID","Course ID","Feedback", "Like/Dislike", "Ranking Score (out of 5)")'+" VALUES ("+uid+","+cid+",'"+feedback+"',"+ld+","+rank+" )"
    db.execute(insert_str)

def insert_photo(cid,pid,path):
    insert_str='INSERT INTO "Photos" ("Course ID","Platform ID","Image Object")'+" VALUES ("+cid+","+pid+",'"+path+"')"
    db.execute(insert_str)

def insert_certification(certid,uid,cid,dur,date):
    insert_str='INSERT INTO "Certifications" ("Certification ID","User ID","Course ID", "Completion Duration", "Completion Date")'+" VALUES ("+certid+","+uid+","+cid+","+dur+","+date+")"
    db.execute(insert_str)

def insert_training(tid,uid,cid,status,completion,start,finish,lastupd):
    insert_str='INSERT INTO "Ongoing Trainings" ("Training ID","User ID","Course ID", "Status", "Completion Percentage", "Start Date", "Finish Date", "Last Updated")'+" VALUES ("+tid+","+uid+","+cid+",'"+status+"',"+completion+",'"+start+"',"+finish+","+lastupd+")"
    db.execute(insert_str)

##########GENERATE RANDOM##########
def random_date(start_date= datetime.date(2000, 1, 1),end_date = datetime.date(2022, 7, 27)):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    rnd = start_date + datetime.timedelta(days=random_number_of_days)
    return rnd

def generate_user(n):
    for i in range(1,n+1):
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
        boss="Null" if random.randint(0,10)==0 else str(random.randint(1,n))
        lvl="Null" if random.randint(0,10)==0 else str(random.randint(1,5))
        insert_user(str(i),boss,str(random_date()),names.get_full_name(),password,lvl)

def generate_platform(n):
    for i in range(1,n+1):
        platform = ''.join(random.choice(string.ascii_letters) for i in range(6))
        link="" if random.randint(0,10)==0 else 'https://www.'+platform+"/"+str(i)+".com"
        insert_platform(str(i),platform,link)

def generate_course(n):
    for i in range(1,n+1):
        course = ''.join(random.choice(string.ascii_letters) for i in range(6))
        duration="Null" if random.randint(0,10)==0 else str(random.randint(60,180))
        tags="" if random.randint(0,10)==0 else "tags"
        photo="" if random.randint(0,10)==0 else "photo"
        insert_course(str(i),course,str(random.randint(1,n)),duration,str(random_date()),tags,photo)

def generate_review(n):
    for i in range(1,n+1):
        feedback ="" if random.randint(0,10)==0 else ''.join(random.choice(string.ascii_letters) for i in range(120))
        rating=str(random.randint(1,5)) if random.randint(0,10)!=0 or feedback=="" else "Null" 
        liked= ("'1'" if int(rating)>2 else "'0'") if rating!="Null" else "NULL"
        insert_review(str(random.randint(1,n)),str(random.randint(1,n)),feedback,liked,rating)

def generate_photo(n):
    for i in range(0,n+1):
        path = ''.join(random.choice(string.ascii_letters) for i in range(10))
        course="Null" if random.randint(0,10)==0 else random.randint(1,n)
        insert_photo(str(course),str(random.randint(1,n)) if course=="Null" else "Null",path+".png")

def generate_certification(n):
    for i in range(1,n+1):
        dur="Null" if random.randint(0,10)==0 else str(random.randint(30,180))
        date="NULL" if random.randint(0,10)==0 else "'"+str(random_date())+"'"
        insert_certification(str(i),str(random.randint(0,n)),str(random.randint(0,n)),dur,date)

def generate_training(n):
    for i in range(0,n+1):
        percentage=100 if random.randint(0,1)==0 else random.randint(0,100)
        status = "Ongoing" if percentage<100 else "Completed"
        startdate=random_date()
        enddate="'"+str(random_date(start_date=startdate,end_date=datetime.date(startdate.year+1,12,31)))+"'" if percentage==100 else "Null" 
        lastupdated=enddate if status=="Completed" else "'"+str(random_date(start_date=startdate,end_date=datetime.date(startdate.year+1,12,31)))+"'"
        insert_training(str(random.randint(0,n)),str(random.randint(0,n)),str(random.randint(0,n)),status,str(percentage),str(startdate),str(enddate),str(lastupdated))


def generate_all(n):
    generate_user(n)
    generate_platform(n)
    generate_course(n)
    generate_review(n)
    generate_photo(n)
    generate_certification(n)
    generate_training(n)

##########SELECT##########
def select_table(columns, table):
    result_set = db.execute('SELECT '+columns+' FROM "'+table+'"')  
    for r in result_set:  
        print(r)

##########DELETE##########
def delete_row(where,how, n=-1):
    if n==-1:
        for i in range(0,1001):
            db.execute('DELETE FROM "'+where+'" WHERE "'+how+'"='+str(i))  
    else:
        db.execute('DELETE FROM "'+where+'" WHERE "'+how+'"='+str(n)) 

def delete_all():
    delete_row("Users", "User ID")
    delete_row("Platforms", "Platform ID")
    delete_row("Courses", "Course ID")
    delete_row("Reviews", "Course ID")
    delete_row("Photos", "Platform ID")
    delete_row("Photos", "Course ID")
    delete_row("Certifications", "Course ID")
    delete_row("Ongoing Trainings", "Course ID")

