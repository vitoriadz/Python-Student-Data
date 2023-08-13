from random import randint 

print("-"*141)
print('\033[1;92m' + 'LIST OF ENROLLMENTS AND GRADES OF STUDENTS IN THE "CONNECTED FLUENCY" LANGUAGE COURSE IN THE PERIOD OF 2023.2' + '\033[0;0m')
print("-"*141)

print('\033[1;92m' + '\nLIST OF REGISTERED STUDENTS:' + '\033[0;0m')

class Students:
  """_summary_
  """    
  def __init__(self, name):
        self.name = name
        self.registration = '2023202'
        for x in range(4):
            self.registration += str(randint(0, 9))
        print(f'\nNAME: \033[1;92m {self.name} \033[0;0m \nREGISTRATION: \033[1;92m {self.registration}\n\033[0;0m')

class Enrollment(Students):
    def __init__(self, name):
        super().__init__(name)

class Subject:
  def __init__ (self, name):
    self.name = name
    self.students = [
      [], 
      [], 
      [], 
      [],
      []
    ]

  def enroll_student(self, student):
   self.students[0].append(student)

  def aevaluate_student(self, index, test_score1, test_score2, status):
    
   self.media = media = (test_score1 + test_score2)/2
   if media >= 6:
      self.status = status = 'APP' 
   elif media < 6:
      self.status = status = ('\033[1;31m' + 'DISAPP' + 	'\033[0;0m')
         
   for x in self.students[0]:
     if index == self.students[0].index(x):
       self.students[1].insert(index, test_score1)
       self.students[2].insert(index, test_score2)
       self.students[3].insert(index, media)
       self.students[4].insert(index, status)
                             
       break
     
  def list_students(self):
    print(f'\nSUBJECT: \033[1;96m {self.name} \033[0;0m')
    print("-"*141)

    for x in self.students[0]:
      index = self.students[0].index(x)
   
      print(f'Nº: {index}| FULL NAME: \033[1;92m {x.name:<5} \033[0;0m|TEST 1: \033[1;96m {self.students[1][index]:<3}\033[0;0m|TEST 2: \033[1;96m {self.students[2][index]:<3}\033[0;0m|FINAL MEDIA: \033[1;96m {self.students[3][index]:<5}\033[0;0m|REGISTRATION: \033[1;92m {x.registration:<5}\033[0;0m |APPROVAL STATUS: \033[1;92m {self.students[4][index]:<5}\033[0;0m')      

#.ALUNOS
student1 = Enrollment('Anna Lettícia Machado')
student2 = Enrollment('Beatriz Mariah Campos')
student3 = Enrollment('Benício Souza Clement')
student4 = Enrollment('Eduardo de Matos Dias')
student5 = Enrollment('Fabiana Loures Fontes')
student6 = Enrollment('Gabriel Brandão Faria')

#. DISCIPLINAS
subject1 = Subject('ENGLISH I')
subject2 = Subject('SPANISH I')
subject3 = Subject('SPANISH II')
subject4 = Subject('GERMAN I')
subject5 = Subject('FRENCH I')
subject6 = Subject('FRENCH II')

#. MATRICULANDO OS ALUNOS NAS DISCIPLINAS
subject1.enroll_student(student4)
subject1.enroll_student(student5)

subject2.enroll_student(student3)
subject2.enroll_student(student4)

subject3.enroll_student(student1)
subject3.enroll_student(student5)

subject4.enroll_student(student1)
subject4.enroll_student(student5)

subject5.enroll_student(student5)
subject5.enroll_student(student3)
subject5.enroll_student(student2)

subject6.enroll_student(student6)

#. REALIZANDO A AVALIAÇÃO POR NÚMEROS
subject1.aevaluate_student(0, randint(0, 10), randint(0, 10), 0)
subject1.aevaluate_student(1, randint(0, 10), randint(0, 10), 0)

subject2.aevaluate_student(0, randint(0, 10), randint(0, 10), 0)
subject2.aevaluate_student(1, randint(0, 10), randint(0, 10), 0)

subject3.aevaluate_student(0, randint(0, 10), randint(0, 10), 0)
subject3.aevaluate_student(1, randint(0, 10), randint(0, 10), 0)

subject4.aevaluate_student(0, randint(0, 10), randint(0, 10), 0)
subject4.aevaluate_student(1, randint(0, 10), randint(0, 10), 0)

subject5.aevaluate_student(0, randint(0, 10), randint(0, 10), 0)
subject5.aevaluate_student(1, randint(0, 10), randint(0, 10), 0)
subject5.aevaluate_student(2, randint(0, 10), randint(0, 10), 0)

subject6.aevaluate_student(0, randint(0, 10), randint(0, 10), 0)

#. EXIBINDO OS DADOS
subject1.list_students()
subject2.list_students()
subject3.list_students()
subject4.list_students()
subject5.list_students()
subject6.list_students() 